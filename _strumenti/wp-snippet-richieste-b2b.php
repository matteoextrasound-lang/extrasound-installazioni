<?php
/**
 * Extrasound B2B — ricezione delle liste prodotti inviate da
 * https://matteoextrasound-lang.github.io/extrasound-installazioni/richiesta.html
 *
 * Da incollare in Code Snippets (ambito: "Esegui ovunque").
 * - Endpoint: POST /wp-json/extrasound-b2b/v1/richiesta
 * - Ogni richiesta viene salvata in Bacheca > Richieste B2B (non pubblica)
 * - Email a info@extrasound.it (Rispondi a = referente) e copia al referente.
 */

const ES_B2B_DEST    = 'info@extrasound.it';
const ES_B2B_ORIGINI = array( 'https://matteoextrasound-lang.github.io', 'https://www.extrasound.it', 'https://extrasound.it' );

add_action( 'init', function () {
	register_post_type( 'es_richiesta_b2b', array(
		'labels'          => array( 'name' => 'Richieste B2B', 'singular_name' => 'Richiesta B2B', 'menu_name' => 'Richieste B2B' ),
		'public'          => false,
		'show_ui'         => true,
		'show_in_menu'    => true,
		'show_in_rest'    => false,
		'menu_icon'       => 'dashicons-clipboard',
		'supports'        => array( 'title', 'editor' ),
		'capability_type' => 'post',
		'capabilities'    => array( 'create_posts' => 'do_not_allow' ),
		'map_meta_cap'    => true,
	) );
} );

add_action( 'rest_api_init', function () {
	register_rest_route( 'extrasound-b2b/v1', '/richiesta', array(
		'methods'             => 'POST',
		'permission_callback' => '__return_true',
		'callback'            => 'es_b2b_richiesta',
	) );
} );

function es_b2b_errore( $msg, $code = 400 ) {
	return new WP_REST_Response( array( 'ok' => false, 'message' => $msg ), $code );
}

function es_b2b_richiesta( WP_REST_Request $req ) {
	$origin = get_http_origin();
	if ( $origin && ! in_array( untrailingslashit( $origin ), ES_B2B_ORIGINI, true ) ) {
		return es_b2b_errore( 'Origine non ammessa.', 403 );
	}
	// campo trappola per i bot: se compilato si risponde "ok" senza fare nulla
	if ( '' !== trim( (string) $req->get_param( 'sito_web' ) ) ) {
		return new WP_REST_Response( array( 'ok' => true ), 200 );
	}
	// massimo 5 richieste l'ora per indirizzo
	$ip  = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REMOTE_ADDR'] ) ) : '';
	$key = 'es_b2b_' . md5( $ip );
	$n   = (int) get_transient( $key );
	if ( $n >= 5 ) {
		return es_b2b_errore( 'Troppe richieste. Riprova più tardi o scrivi a ' . ES_B2B_DEST . '.', 429 );
	}

	$campi = array( 'ragione_sociale', 'piva', 'cf', 'sdi', 'pec', 'indirizzo', 'citta', 'cap', 'provincia',
		'referente', 'email', 'telefono', 'consegna', 'indirizzo_consegna', 'riferimento', 'note' );
	$d = array();
	foreach ( $campi as $c ) {
		$v       = (string) $req->get_param( $c );
		$d[ $c ] = in_array( $c, array( 'note', 'indirizzo_consegna' ), true ) ? sanitize_textarea_field( $v ) : sanitize_text_field( $v );
		$d[ $c ] = mb_substr( $d[ $c ], 0, 2000 );
	}
	foreach ( array( 'ragione_sociale', 'piva', 'indirizzo', 'citta', 'cap', 'provincia', 'referente', 'email', 'telefono' ) as $c ) {
		if ( '' === $d[ $c ] ) {
			return es_b2b_errore( 'Campo obbligatorio mancante: ' . $c );
		}
	}
	if ( ! is_email( $d['email'] ) ) {
		return es_b2b_errore( 'Email non valida.' );
	}
	if ( ! preg_match( '/^(IT)?\d{11}$/i', preg_replace( '/\s+/', '', $d['piva'] ) ) ) {
		return es_b2b_errore( 'Partita IVA non valida.' );
	}
	if ( '' === $d['sdi'] && '' === $d['pec'] ) {
		return es_b2b_errore( 'Serve il codice SDI oppure la PEC.' );
	}
	if ( '1' !== (string) $req->get_param( 'privacy' ) && 'on' !== (string) $req->get_param( 'privacy' ) ) {
		return es_b2b_errore( 'Manca il consenso privacy.' );
	}

	$prodotti = json_decode( (string) $req->get_param( 'prodotti' ), true );
	if ( ! is_array( $prodotti ) || ! $prodotti || count( $prodotti ) > 150 ) {
		return es_b2b_errore( 'Lista prodotti vuota o non valida.' );
	}
	$righe = array();
	foreach ( $prodotti as $p ) {
		$slug = isset( $p['slug'] ) ? sanitize_title( $p['slug'] ) : '';
		$qty  = isset( $p['qty'] ) ? max( 1, min( 999, (int) $p['qty'] ) ) : 1;
		if ( ! $slug ) {
			continue;
		}
		$righe[] = array(
			'slug'  => $slug,
			'nome'  => sanitize_text_field( ( $p['brand'] ?? '' ) . ' ' . ( $p['model'] ?? '' ) ),
			'qty'   => $qty,
		);
	}
	if ( ! $righe ) {
		return es_b2b_errore( 'Lista prodotti vuota.' );
	}

	$base = 'https://matteoextrasound-lang.github.io/extrasound-installazioni/scheda-';
	$e    = 'esc_html';
	$html = '<h2>Richiesta preventivo B2B</h2>'
		. '<p><strong>' . $e( $d['ragione_sociale'] ) . '</strong><br>P. IVA ' . $e( $d['piva'] )
		. ( $d['cf'] ? ' · C.F. ' . $e( $d['cf'] ) : '' ) . '<br>SDI ' . $e( $d['sdi'] ?: '-' ) . ' · PEC ' . $e( $d['pec'] ?: '-' )
		. '<br>' . $e( $d['indirizzo'] ) . ', ' . $e( $d['cap'] ) . ' ' . $e( $d['citta'] ) . ' (' . $e( strtoupper( $d['provincia'] ) ) . ')</p>'
		. '<p>Referente: ' . $e( $d['referente'] ) . '<br>Email: ' . $e( $d['email'] ) . '<br>Telefono: ' . $e( $d['telefono'] ) . '</p>'
		. '<p>Consegna: ' . $e( $d['consegna'] ) . ( $d['indirizzo_consegna'] ? '<br>' . nl2br( $e( $d['indirizzo_consegna'] ) ) : '' )
		. ( $d['riferimento'] ? '<br>Riferimento: ' . $e( $d['riferimento'] ) : '' ) . '</p>'
		. ( $d['note'] ? '<p>Note:<br>' . nl2br( $e( $d['note'] ) ) . '</p>' : '' )
		. '<table cellpadding="6" style="border-collapse:collapse" border="1"><tr><th>Q.tà</th><th>Prodotto</th></tr>';
	foreach ( $righe as $r ) {
		$html .= '<tr><td style="text-align:right">' . (int) $r['qty'] . '</td><td><a href="' . esc_url( $base . $r['slug'] . '.html' ) . '">' . $e( $r['nome'] ) . '</a></td></tr>';
	}
	$html .= '</table>';

	$id = wp_insert_post( array(
		'post_type'    => 'es_richiesta_b2b',
		'post_status'  => 'private',
		'post_title'   => $d['ragione_sociale'] . ' · ' . $d['referente'],
		'post_content' => $html,
	) );
	$numero = $id && ! is_wp_error( $id ) ? 'B2B-' . $id : '';
	if ( $numero ) {
		update_post_meta( $id, '_es_b2b_dati', $d );
		update_post_meta( $id, '_es_b2b_prodotti', $righe );
	}

	$h      = array( 'Content-Type: text/html; charset=UTF-8', 'Reply-To: ' . $d['referente'] . ' <' . $d['email'] . '>' );
	$ogg    = 'Richiesta preventivo B2B ' . $numero . ' · ' . $d['ragione_sociale'];
	$inviata = wp_mail( ES_B2B_DEST, $ogg, $html, $h );
	wp_mail( $d['email'], 'Extrasound B2B: abbiamo ricevuto la tua lista ' . $numero,
		'<p>Grazie, abbiamo ricevuto la richiesta. Ti rispondiamo con il preventivo.</p>' . $html
		. '<p>Extrasound · Via Archimede 605, 47521 Cesena (FC) · 0547 645626 · ' . ES_B2B_DEST . '</p>',
		array( 'Content-Type: text/html; charset=UTF-8', 'Reply-To: Extrasound <' . ES_B2B_DEST . '>' ) );

	if ( ! $numero && ! $inviata ) {
		return es_b2b_errore( 'Invio non riuscito.', 500 );
	}
	set_transient( $key, $n + 1, HOUR_IN_SECONDS );
	return new WP_REST_Response( array( 'ok' => true, 'numero' => $numero ), 200 );
}
