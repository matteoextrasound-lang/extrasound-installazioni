"""Link "Dati tecnici" delle schede: solo pagine e documenti dei produttori, verificati (25/11/2026).

- PAGINE: pagina ufficiale del prodotto (o della serie, quando il produttore non ha una pagina per modello).
- Dalle fonti già presenti nei JSON si tengono solo i documenti su domini dei produttori (UFFICIALI)
  e non elencati in ROTTI. Siti di rivenditori, archivi di manuali e copie su altri server vengono tolti.
- ArtSound, Garvan e Gallo non hanno un sito del produttore raggiungibile: nessun link.
"""
from urllib.parse import urlparse

UFFICIALI = ("elac.com", "resources.elac.com", "assets.kef.com", "kef.com", "jbl.com", "focal.com",
             "elipson.com", "arcam.co.uk", "hegel.com", "lyngdorf.com", "steinwaylyngdorf.com",
             "marantz.com", "rotel.com", "polkaudio.com")
ROTTI = {
    # rimandano a pagine 404 o vuote (segnalato 25/11/2026)
    "https://se.yamaha.com/files/download/other_assets/2/1229902/web_VCM9300_XDA-QS5400RK_om_UAGLF_EnFrEs_C0.pdf",
    "https://au.yamaha.com/files/download/other_assets/7/1229907/web_VCM9320_XDA-AMP5400RK_om_UAGLF_EnFrEs_C0.pdf",
    "https://global.jbl.com/built-in-audio-systems/Studio-2-88IW-.html",
}

F = "https://www.focal.com/products/"
E = "https://elac.com/"
J2 = "https://support.jbl.com/gb/en/speakers/speakers-in-wall-in-ceiling/"
J6 = "https://support.jbl.com/gb/en/jblpremium/jblpremium-speakers/jblpremium-speakers-inwall/"
STUDIO2 = ("serie JBL Studio 2 Architectural", "https://ca.jbl.com/studio2-architectural-series")
STAGE2 = ("serie JBL Stage 2 Architectural", "https://kh.jbl.com/stage2-architectural-series")
ARCH = ("gamma Elipson Architect", "https://en.elipson.com/architect")
INF = ("gamma Elipson Infinite", "https://en.elipson.com/infinite")
RAIN = ("Elipson Rain", "https://en.elipson.com/enceintes/rain")
ATRIUM = ("serie Polk Atrium", "https://www.polkaudio.com/en-gb/category/atrium-series/")
FOCAL_CI = ("gamma Focal Custom Install", "https://www.focal.com/product-comparison")
FOCAL_300 = ("istruzioni Focal serie 300", "https://focal.com/notice-300-series")
ROTEL_BRO = ("catalogo Rotel 2025", "https://www.rotel.com/sites/default/files/download/Rotel_Brochure%202025.pdf")
KEF_XHT = ("scheda KEF Extreme Home Theatre", "https://assets.kef.com/pdf_doc/ci/Extreme-Home-Theatre-Info-sheet-EN.pdf")
KEF_QLM = ("manuale KEF Ci3120QLM / Ci5120QLM", "https://assets.kef.com/pdf_doc/ci/KEF_Ci3120QLM_Ci5120QLM_User_Manual.pdf")

PAGINE = {
    # Focal
    "focal-100-icw5": [("pagina Focal 100 ICW5", F + "100-icw5")],
    "focal-100-icw6": [("pagina Focal 100 ICW6", F + "100-icw6")],
    "focal-100-icw8": [("pagina Focal 100 ICW8", F + "100-icw8")],
    "focal-100-iw6": [("pagina Focal 100 IW6", F + "100-iw6")],
    "focal-100-iwlcr5": [("pagina Focal 100 IWLCR5", F + "100-iwlcr5")],
    "focal-100-iwsub8": [("pagina Focal 100 IWSUB8", F + "100-iwsub8")],
    "focal-100-iwsub8-amplifier": [("pagina Focal 100 IWSUB8", F + "100-iwsub8")],
    "focal-100-ic6st": [("pagina Focal 100 IC6ST", F + "100-ic6st")],
    "focal-100-od8": [("pagina Focal 100 OD8", F + "100-od-8")],
    "focal-100-od6": [("Focal 100 Series outdoor", "https://www.focal.com/catalog/integrated-systems/home-solutions/outdoor-solutions/100-series")],
    "focal-100-iclcr5": [FOCAL_CI],
    "focal-300-ica6": [("pagina Focal 300 ICA6", F + "300-ica6")],
    "focal-300-icw6": [("pagina Focal 300 ICW6", F + "300-icw6")],
    "focal-300-iw6": [("pagina Focal 300 IW6", F + "300-iw6")],
    "focal-300-icw4": [FOCAL_300], "focal-300-icw8": [FOCAL_300], "focal-300-iclcr5": [FOCAL_300], "focal-300-iwlcr6": [FOCAL_300],
    # ELAC
    "elac-vertex-i-ic-vt61": [("pagina ELAC IC-VT61", E + "ic-vt61")],
    "elac-vertex-i-iw-vc51": [("pagina ELAC IW-VC51", E + "iw-vc51")],
    "elac-is-amp1275": [("pagina ELAC IS-AMP1275", E + "is-amp1275-bk")],
    "elac-is-amp1650": [("pagina ELAC IS-AMP1650", E + "is-amp1650-bk")],
    "elac-is-amp8100": [("pagina ELAC IS-AMP8100", E + "is-amp8100-bk")],
    "elac-vertex-iii-ic-vj63": [("pagina ELAC IC-VJ63", E + "ic-vj63")],
    "elac-muro-od-m61": [("pagina ELAC Muro OD-M61", E + "od-m61-bk")],
    "elac-muro-od-m81": [("scheda ELAC Muro Outdoor", "https://resources.elac.com/hubfs/Muro%20Outdoor%20Sales%20Sheet.pdf")],
    # JBL
    "jbl-studio-2-6ic": [("pagina JBL Studio 2 6IC", J2 + "STUDIO2+6IC.html")],
    "jbl-studio-2-8ic": [("pagina JBL Studio 2 8IC", J2 + "STUDIO2+8IC.html")],
    "jbl-studio-2-6icdt": [STUDIO2], "jbl-studio-2-6iw": [STUDIO2], "jbl-studio-2-8iw": [STUDIO2],
    "jbl-studio-2-55iw": [STUDIO2], "jbl-studio-2-88iw": [STUDIO2],
    "jbl-studio-6iw": [("pagina JBL Studio 6IW", "https://global.jbl.com/built-in-audio-systems/STUDIO-6-6IW.html")],
    "jbl-studio-8iw": [("pagina JBL Studio 8IW", "https://global.jbl.com/built-in-audio-systems/STUDIO-6-8IW.html")],
    "jbl-studio-66lcr": [("pagina JBL Studio 66LCR", "https://ca.jbl.com/en_CA/STUDIO-6-66LCR.html")],
    "jbl-studio-88lcr": [("pagina JBL Studio 88LCR", "https://ca.jbl.com/en_CA/STUDIO-6-88LCR.html")],
    "jbl-studio-6-theater": [("pagina JBL Studio 6 Theater", "https://id.jbl.com/STUDIO-6-THTR.html")],
    "jbl-stage-260c": [("pagina JBL Stage 260C", "https://global.jbl.com/Stage-260C.html")],
    "jbl-stage-xd-5": [("pagina JBL Stage XD-5", "https://kh.jbl.com/outdoor/Stage-XD5.html")],
    "jbl-stage-xd-6": [("serie JBL Stage XD", "https://kh.jbl.com/jbl-stage-xd-series.html")],
    "jbl-conceal-c62": [("pagina JBL Conceal C62", "https://global.jbl.com/built-in-audio-systems/C62.html")],
    "jbl-conceal-c82w": [("serie JBL Conceal", "https://ca.jbl.com/conceal-series")],
    "jbl-conceal-c83": [("serie JBL Conceal", "https://ca.jbl.com/conceal-series")],
    "jbl-conceal-c86": [("serie JBL Conceal", "https://ca.jbl.com/conceal-series")],
    # KEF
    "kef-ci3120qlm-thx": [KEF_XHT, KEF_QLM], "kef-ci5120qlm-thx": [KEF_XHT, KEF_QLM],
    "kef-ci3160rlm-thx": [KEF_XHT], "kef-ci5160rlm-thx": [KEF_XHT],
    "kef-ventura-5": [("pagina KEF Ventura 5", "https://eu.kef.com/products/ventura-5")],
    "kef-ventura-6": [("pagina KEF Ventura 6", "https://eu.kef.com/products/ventura-6")],
    "kef-ci3-80qt": [("pagina KEF Ci3-80QT", "https://eu.kef.com/products/ci3-80qt")],
    # Elipson
    "elipson-ic6": [("pagina Elipson IC6", "https://en.elipson.com/product-page/ic6")],
    "elipson-ic4": [ARCH], "elipson-ic6st": [ARCH], "elipson-ic8": [ARCH], "elipson-ic8-ultra-slim": [ARCH],
    "elipson-iw6": [ARCH], "elipson-iw8": [ARCH], "elipson-iw14c": [ARCH],
    "elipson-infinite-8": [INF], "elipson-infinite-14": [INF], "elipson-infinite-s12": [INF], "elipson-infinite-a1000": [INF],
    "elipson-rain-4": [RAIN], "elipson-rain-6": [RAIN], "elipson-rain-8": [RAIN],
    # Elettroniche
    "yamaha-xda-qs5400rk": [("pagina Yamaha XDA-QS5400RK", "https://europe.yamaha.com/en/audio/home-audio/products/multi-room-amplifiers/xda-qs5400rk/")],
    "yamaha-xda-amp5400rk": [("pagina Yamaha XDA-AMP5400RK", "https://europe.yamaha.com/en/audio/home-audio/products/multi-room-amplifiers/xda-amp5400rk/")],
    "marantz-model-m4": [("pagina Marantz Model M4", "https://marantz.com/en/product/amplifiers/model-m4/MODELM4.html")],
    "marantz-amp-10": [("pagina Marantz AMP 10", "https://marantz.com/en-us/pdp-amp-10-300586.html")],
    "marantz-amp-20": [("pagina Marantz AMP 20", "https://www.marantz.com/en/product/av-separates/amp-20/AMP20.html")],
    "rotel-c8": [("pagina Rotel C8 / C8+", "https://rotel.com/product/c8")],
    "rotel-c8-plus": [("pagina Rotel C8 / C8+", "https://rotel.com/product/c8")],
    "rotel-rmb-1587mkii": [ROTEL_BRO], "rotel-rmb-1585mkii": [ROTEL_BRO], "rotel-rsp-1576-mkii": [ROTEL_BRO],
    "arcam-av41": [("pagina Arcam AV41", "https://www.arcam.co.uk/product,hda,av-processors,av41.htm"),
                   ("scheda tecnica Arcam AV41", "https://www.arcam.co.uk/ugc/tor/AV41/Specification Sheet/ARCAM_AV41_Spec_Sheet_V1.pdf")],
    "arcam-avp45": [("pagina Arcam AVP45", "https://www.arcam.co.uk/product,radia,av-processors,avp45.htm"),
                    ("scheda tecnica Arcam AVP45", "https://www.arcam.co.uk/ugc/tor/AVP45/Specification Sheet/LS_ARCAM_AVP45_SpecSheet_EN_v1.2.pdf")],
    "arcam-pa410": [("pagina Arcam PA410", "https://www.arcam.co.uk/product,hda,power-amplifiers,pa410.htm")],
    "arcam-pa720": [("pagina Arcam PA720", "https://www.arcam.co.uk/product,hda,power-amplifiers,pa720.htm")],
    "hegel-c55": [("pagina Hegel C55", "https://hegel.com/products/custom/c55")],
    "lyngdorf-mp-40-2-1": [("pagina Lyngdorf MP-40", "https://lyngdorf.com/lyngdorf-mp-40/")],
    "lyngdorf-mp-60-2-1": [("pagina Lyngdorf MP-60", "https://lyngdorf.steinwaylyngdorf.com/lyngdorf-mp-60/")],
    "lyngdorf-mxa-8400": [("supporto Lyngdorf MXA-8400", "https://lyngdorf.steinwaylyngdorf.com/support-for-mxa-8400/")],
}
for s in ("polk-audio-atrium-4", "polk-audio-atrium-5", "polk-audio-atrium-6", "polk-audio-atrium-8-sdi",
          "polk-audio-atrium-sat300", "polk-audio-atrium-sub100"):
    PAGINE[s] = [ATRIUM]
for s in ("jbl-stage-250wl", "jbl-stage-260cdt", "jbl-stage-260csa", "jbl-stage-260w", "jbl-stage-280c",
          "jbl-stage-280csa", "jbl-stage-280w"):
    PAGINE[s] = [STAGE2]


def ufficiale(url):
    h = (urlparse(url).hostname or "").lower()
    return url not in ROTTI and any(h == d or h.endswith("." + d) for d in UFFICIALI)


def fonti(p):
    out, visti = [], set()
    for lab, url in PAGINE.get(p["slug"], []):
        out.append({"label": lab, "url": url}); visti.add(url)
    for f in p.get("fonti") or []:
        u = f.get("url", "")
        if u and u not in visti and ufficiale(u):
            out.append(f); visti.add(u)
    return out
