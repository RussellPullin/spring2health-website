#!/usr/bin/env python3
"""
Spring 2 Health website rebuild.
- Logo referenced as logo.png (real file, not base64)
- Font Awesome 6 icons (no emoji)
- Supported Independent Living removed
"""

BASE = '/Users/pristinelifestylesolutions/Desktop/S2H website'

# --------------------------------------------------------------------------
# SHARED CSS
# --------------------------------------------------------------------------
SHARED_CSS = """
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --forest:      #1B4D35;
    --forest-dark: #0D2C1E;
    --forest-mid:  #2A6B4A;
    --forest-lt:   #4D9970;
    --forest-pale: #EAF5EE;
    --forest-frost:#F2FAF5;
    --amber:       #D97706;
    --amber-dark:  #B45309;
    --amber-lt:    #F59E0B;
    --amber-pale:  #FEF9EE;
    --cream:       #F4F0E8;
    --sand:        #EDE4D3;
    --white:       #FFFFFF;
    --charcoal:    #1A2A1C;
    --mid:         #3D5247;
    --soft:        #6A7C6E;
    --border:      rgba(27,77,53,0.15);
    --serif: 'Playfair Display', Georgia, serif;
    --sans: 'Nunito', sans-serif;
    --r: 10px;
    --shadow:    0 4px 24px rgba(13,44,30,0.12);
    --shadow-lg: 0 16px 60px rgba(13,44,30,0.22);
  }
  html { scroll-behavior: smooth; }
  body { font-family: var(--sans); background: var(--cream); color: var(--charcoal); line-height: 1.6; overflow-x: hidden; }
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--forest-dark); }
  ::-webkit-scrollbar-thumb { background: var(--amber); border-radius: 3px; }

  /* Icon sizing */
  .icon-wrap i { display: flex; align-items: center; justify-content: center; }
  .svc-ico i, .hcard-icon i { font-size: 1.2rem; color: var(--forest-lt); }
  .svc-full-icon i { font-size: 2.6rem; color: var(--forest-mid); }
  .av-icon i { font-size: 0.9rem; color: var(--forest-mid); }
  .cd-icon i { font-size: 1.1rem; color: var(--forest-mid); }
  .diff-icon i { font-size: 1.8rem; color: var(--amber); }
  .ref-info-icon i { font-size: 1rem; color: var(--amber-lt); }

  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 500; display: flex; align-items: center; justify-content: space-between; padding: 0.9rem 4rem; background: rgba(13,44,30,0.97); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(77,153,112,0.25); }
  .nav-logo { display: flex; align-items: center; gap: 0.85rem; text-decoration: none; }
  .logo-img { height: 42px; width: auto; display: block; }
  .logo-sub { font-size: 0.58rem; font-weight: 400; color: rgba(255,255,255,0.45); letter-spacing: 0.18em; text-transform: uppercase; margin-top: 2px; }
  .nav-links { display: flex; align-items: center; gap: 0.2rem; list-style: none; }
  .nav-links a { font-size: 0.82rem; font-weight: 600; letter-spacing: 0.03em; color: rgba(255,255,255,0.65); text-decoration: none; padding: 0.5rem 0.9rem; border-radius: 6px; transition: color 0.2s, background 0.2s; }
  .nav-links a:hover, .nav-links a.active { color: var(--amber-lt); background: rgba(217,119,6,0.12); }
  .nav-btn { background: var(--amber) !important; color: #1A1A1A !important; padding: 0.55rem 1.4rem !important; border-radius: 8px !important; font-weight: 700 !important; }
  .nav-btn:hover { background: var(--amber-dark) !important; color: #fff !important; }
  @media(max-width:900px){ nav{padding:0.9rem 1.5rem;} .nav-links{display:none;} }

  footer { background: var(--forest-dark); padding: 4rem 4rem 2rem; border-top: 1px solid rgba(77,153,112,0.25); }
  .footer-inner { max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 4rem; padding-bottom: 2.5rem; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 2rem; }
  .footer-logo { display: flex; align-items: center; gap: 0.85rem; margin-bottom: 1.25rem; }
  .footer-logo-img { height: 50px; width: auto; display: block; }
  .footer-tagline { font-size: 0.875rem; color: rgba(255,255,255,0.4); line-height: 1.75; max-width: 280px; }
  .footer-heading { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(217,119,6,0.7); margin-bottom: 1.1rem; }
  .footer-links { list-style: none; display: flex; flex-direction: column; gap: 0.6rem; }
  .footer-links a { font-size: 0.88rem; color: rgba(255,255,255,0.45); text-decoration: none; transition: color 0.2s; }
  .footer-links a:hover { color: var(--amber-lt); }
  .footer-bottom { max-width: 1300px; margin: 0 auto; display: flex; justify-content: space-between; font-size: 0.78rem; color: rgba(255,255,255,0.2); }
  .footer-bottom a { color: rgba(255,255,255,0.3); text-decoration: none; }
  .footer-bottom a:hover { color: var(--amber-lt); }
  @media(max-width:900px){ footer{padding:3rem 1.5rem 2rem;} .footer-inner{grid-template-columns:1fr;gap:2rem;} .footer-bottom{flex-direction:column;gap:0.4rem;} }

  /* Social icons */
  .footer-social { display:flex; gap:0.65rem; margin-top:1.25rem; }
  .footer-social-link { width:38px; height:38px; border-radius:9px; display:flex; align-items:center; justify-content:center; font-size:1rem; text-decoration:none; transition:transform 0.2s, opacity 0.2s; opacity:0.75; }
  .footer-social-link:hover { transform:translateY(-3px); opacity:1; }
  .footer-social-link.ig { background:linear-gradient(135deg,#833ab4,#fd1d1d,#fcb045); color:#fff; }
  .footer-social-link.fb { background:#1877F2; color:#fff; }
  .social-btn { display:inline-flex; align-items:center; gap:0.65rem; padding:0.92rem 1.75rem; border-radius:var(--r); font-family:var(--sans); font-size:0.88rem; font-weight:700; text-decoration:none; transition:transform 0.2s, opacity 0.2s; }
  .social-btn:hover { transform:translateY(-2px); opacity:0.92; }
  .social-btn.ig { background:linear-gradient(135deg,#833ab4,#fd1d1d,#fcb045); color:#fff; }
  .social-btn.fb { background:#1877F2; color:#fff; }

  .section { padding: 8rem 0; }
  .section-inner { max-width: 1300px; margin: 0 auto; padding: 0 4rem; }
  .pill-label { display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(27,77,53,0.1); border: 1px solid rgba(27,77,53,0.28); border-radius: 100px; padding: 0.3rem 1rem; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--forest-mid); margin-bottom: 1.25rem; }
  .pill-label .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--forest-mid); }
  .pill-label.light { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.22); color: rgba(255,255,255,0.85); }
  .pill-label.light .dot { background: var(--amber-lt); }
  .sh2 { font-size: clamp(2rem, 3.2vw, 3.25rem); font-weight: 700; line-height: 1.15; letter-spacing: -0.02em; color: var(--charcoal); margin-bottom: 1.25rem; }
  .sh2 em { font-style: italic; font-family: var(--serif); font-weight: 400; color: var(--forest); }
  .sh2.light { color: var(--white); }
  .sh2.light em { color: var(--amber-lt); }
  .sbody { font-size: 1rem; font-weight: 400; color: var(--mid); line-height: 1.9; }
  .sbody.light { color: rgba(255,255,255,0.62); }
  .btn-primary { background: var(--amber); color: #1A1A1A; padding: 0.92rem 2.25rem; font-family: var(--sans); font-size: 0.88rem; font-weight: 700; text-decoration: none; border-radius: var(--r); transition: background 0.2s, transform 0.15s; display: inline-block; box-shadow: 0 6px 24px rgba(217,119,6,0.28); }
  .btn-primary:hover { background: var(--amber-dark); transform: translateY(-2px); }
  .btn-outline { background: rgba(255,255,255,0.06); border: 1.5px solid rgba(255,255,255,0.28); color: rgba(255,255,255,0.9); padding: 0.92rem 2.25rem; font-family: var(--sans); font-size: 0.88rem; font-weight: 600; text-decoration: none; border-radius: var(--r); transition: border-color 0.2s, background 0.2s, transform 0.15s; display: inline-block; }
  .btn-outline:hover { border-color: var(--amber-lt); background: rgba(217,119,6,0.1); transform: translateY(-2px); }
  .btn-dark { background: var(--forest); color: var(--white); padding: 0.92rem 2.25rem; font-family: var(--sans); font-size: 0.88rem; font-weight: 700; text-decoration: none; border-radius: var(--r); display: inline-block; transition: background 0.2s, transform 0.15s; }
  .btn-dark:hover { background: var(--forest-dark); transform: translateY(-2px); }
  .btn-submit { width: 100%; margin-top: 1.75rem; background: var(--amber); color: #1A1A1A; border: none; padding: 1.05rem; font-family: var(--sans); font-size: 0.88rem; font-weight: 700; border-radius: 10px; cursor: pointer; transition: background 0.2s, transform 0.15s; box-shadow: 0 6px 24px rgba(217,119,6,0.28); }
  .btn-submit:hover { background: var(--amber-dark); transform: translateY(-1px); }
  .ff { display: flex; flex-direction: column; gap: 0.35rem; }
  .ff.s2 { grid-column: 1 / -1; }
  .ff label { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--mid); }
  .ff input, .ff select, .ff textarea { padding: 0.78rem 1rem; border: 1.5px solid rgba(27,77,53,0.18); border-radius: 8px; font-family: var(--sans); font-size: 0.9rem; color: var(--charcoal); background: var(--cream); outline: none; width: 100%; transition: border-color 0.2s, box-shadow 0.2s; }
  .ff input:focus, .ff select:focus, .ff textarea:focus { border-color: var(--forest-mid); background: var(--white); box-shadow: 0 0 0 3px rgba(27,77,53,0.1); }
  .ff textarea { min-height: 90px; resize: vertical; }
  .fg2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.25rem; }
  @media(max-width:900px){ .section-inner{padding:0 1.5rem;} .fg2{grid-template-columns:1fr;} .ff.s2{grid-column:1;} }
  @keyframes fadeUp { from{opacity:0;transform:translateY(24px);} to{opacity:1;transform:translateY(0);} }
  .form-msg { margin-top:1.1rem; padding:0.85rem 1.25rem; border-radius:8px; font-size:0.88rem; font-weight:600; display:none; }
  .form-msg:not(:empty) { display:block; }
  .form-success { background:rgba(27,77,53,0.1); color:var(--forest); border:1px solid rgba(27,77,53,0.25); }
  .form-error { background:rgba(185,28,28,0.07); color:#b91c1c; border:1px solid rgba(185,28,28,0.18); }

  .av { display: flex; align-items: flex-start; gap: 1.1rem; padding: 1.3rem 1.6rem; border-bottom: 1.5px solid rgba(27,77,53,0.1); background: var(--forest-frost); transition: background 0.2s; }
  .av:last-child { border-bottom: none; }
  .av:hover { background: var(--forest-pale); }
  .av-icon { width: 36px; height: 36px; flex-shrink: 0; border-radius: 8px; background: rgba(27,77,53,0.12); display: flex; align-items: center; justify-content: center; font-size: 0.95rem; }
  .av strong { display: block; font-size: 0.92rem; font-weight: 700; color: var(--charcoal); margin-bottom: 0.15rem; }
  .av span { font-size: 0.83rem; color: var(--soft); }
  .about-values { margin-top: 2.5rem; border: 1.5px solid rgba(27,77,53,0.12); border-radius: 12px; overflow: hidden; }
  .quote-card { background: linear-gradient(150deg, var(--forest-dark) 0%, var(--forest) 100%); border-radius: 18px; padding: 3.5rem; position: relative; overflow: hidden; box-shadow: var(--shadow-lg); }
  .quote-card::before { content: ''; position: absolute; top: -60px; right: -60px; width: 250px; height: 250px; border-radius: 50%; background: rgba(77,153,112,0.15); }
  .qm { font-family: var(--serif); font-size: 5.5rem; line-height: 0; vertical-align: -2.2rem; color: var(--amber-lt); opacity: 0.6; margin-right: 0.1rem; }
  .quote-text { font-family: var(--serif); font-size: 1.55rem; font-style: italic; color: rgba(255,255,255,0.92); line-height: 1.55; margin-bottom: 2.25rem; position: relative; z-index: 1; }
  .quote-footer { display: flex; align-items: center; gap: 1rem; position: relative; z-index: 1; }
  .quote-line { width: 32px; height: 2px; background: var(--amber); border-radius: 2px; }
  .quote-name { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--amber-lt); }
  .quote-badge { position: absolute; bottom: -1.25rem; right: 2.5rem; background: var(--amber); border-radius: 12px; padding: 1.25rem 1.75rem; box-shadow: 0 12px 40px rgba(217,119,6,0.35); text-align: center; min-width: 130px; }
  .quote-badge strong { display: block; font-size: 2rem; font-weight: 700; color: #1A1A1A; line-height: 1; }
  .quote-badge span { font-size: 0.68rem; font-weight: 700; text-transform: uppercase; color: rgba(26,26,26,0.7); display: block; margin-top: 0.2rem; }
"""

PAGE_HERO_CSS = """
  .page-hero { padding:12rem 0 6rem; background:linear-gradient(145deg,#0A1F14 0%,#1B4D35 52%,#0E3020 100%); position:relative; overflow:hidden; }
  .page-hero::before { content:''; position:absolute; inset:0; background-image:radial-gradient(rgba(255,255,255,0.06) 1px,transparent 1px); background-size:36px 36px; pointer-events:none; }
  .page-hero::after { content:''; position:absolute; top:-60px; right:-60px; width:500px; height:500px; border-radius:50%; background:radial-gradient(circle,rgba(77,153,112,0.2) 0%,transparent 70%); pointer-events:none; }
  .page-hero-inner { max-width:1300px; margin:0 auto; padding:0 4rem; position:relative; z-index:1; }
  .page-title { font-size:clamp(2.5rem,5vw,4rem); font-weight:700; color:var(--white); line-height:1.1; letter-spacing:-0.02em; margin-bottom:1.25rem; }
  .page-title em { font-style:italic; font-family:var(--serif); color:var(--amber-lt); font-weight:400; }
  .page-subtitle { font-size:1.1rem; color:rgba(255,255,255,0.62); max-width:600px; line-height:1.8; }
"""

INDEX_CSS = SHARED_CSS + """
  #hero { min-height:100vh; background:linear-gradient(145deg,#0A1F14 0%,#1B4D35 50%,#0E3020 100%); position:relative; overflow:hidden; display:flex; align-items:center; }
  .hc { position:absolute; border-radius:50%; pointer-events:none; }
  .hc1 { width:600px; height:600px; background:radial-gradient(circle,rgba(77,153,112,0.22) 0%,transparent 70%); top:-100px; right:-120px; }
  .hc2 { width:350px; height:350px; background:radial-gradient(circle,rgba(217,119,6,0.18) 0%,transparent 70%); bottom:80px; right:220px; }
  .hero-dots { position:absolute; inset:0; pointer-events:none; background-image:radial-gradient(rgba(255,255,255,0.07) 1px,transparent 1px); background-size:36px 36px; }
  .hero-mountain { position:absolute; bottom:0; left:0; right:0; height:200px; pointer-events:none; }
  .hero-inner { position:relative; z-index:2; max-width:1300px; margin:0 auto; padding:0 4rem; width:100%; display:grid; grid-template-columns:1.1fr 0.9fr; gap:5rem; align-items:center; padding-top:4rem; }
  .hero-left { padding:7rem 0 6rem; }
  .hero-badge { display:inline-flex; align-items:center; gap:0.6rem; background:rgba(77,153,112,0.15); border:1px solid rgba(77,153,112,0.4); border-radius:100px; padding:0.4rem 1.1rem 0.4rem 0.6rem; margin-bottom:2rem; }
  .hero-badge-dot { width:8px; height:8px; border-radius:50%; background:var(--amber-lt); animation:pulse 2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{transform:scale(1);opacity:1;} 50%{transform:scale(1.4);opacity:0.7;} }
  .hero-badge span { font-size:0.73rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:rgba(255,255,255,0.82); }
  .hero-h1 { font-size:clamp(2.75rem,4.5vw,4.75rem); font-weight:700; color:var(--white); line-height:1.1; letter-spacing:-0.02em; margin-bottom:1.5rem; }
  .hero-h1 .accent { color:var(--amber-lt); }
  .hero-h1 .italic { font-style:italic; font-family:var(--serif); font-weight:400; }
  .hero-sub { font-size:1.05rem; font-weight:300; color:rgba(255,255,255,0.65); max-width:460px; line-height:1.85; margin-bottom:2.5rem; }
  .hero-pills { display:flex; flex-direction:column; gap:0.6rem; margin-bottom:3rem; }
  .hero-pill { display:flex; align-items:center; gap:0.85rem; font-size:0.92rem; color:rgba(255,255,255,0.82); }
  .hero-pill-check { width:20px; height:20px; border-radius:50%; flex-shrink:0; background:rgba(77,153,112,0.18); border:1.5px solid var(--forest-lt); display:flex; align-items:center; justify-content:center; font-size:0.6rem; color:var(--amber-lt); font-weight:700; }
  .hero-btns { display:flex; gap:1rem; flex-wrap:wrap; }
  .hero-right { display:flex; flex-direction:column; gap:1rem; }
  .hcard { background:rgba(255,255,255,0.06); border:1px solid rgba(77,153,112,0.2); border-radius:14px; padding:1.5rem 1.75rem; display:flex; align-items:flex-start; gap:1rem; transition:background 0.3s,transform 0.25s; }
  .hcard:hover { background:rgba(77,153,112,0.12); transform:translateX(5px); }
  .hcard.featured { background:rgba(77,153,112,0.12); border-color:rgba(77,153,112,0.38); }
  .hcard-icon { width:40px; height:40px; flex-shrink:0; border-radius:10px; background:rgba(77,153,112,0.15); display:flex; align-items:center; justify-content:center; font-size:1.1rem; }
  .hcard-name { font-size:0.88rem; font-weight:700; color:var(--white); margin-bottom:0.2rem; }
  .hcard-desc { font-size:0.78rem; color:rgba(255,255,255,0.5); line-height:1.55; }
  .stats-band { background:var(--amber); padding:2rem 4rem; display:flex; justify-content:center; }
  .sband-item { flex:1; text-align:center; padding:0.5rem 2rem; border-right:1px solid rgba(26,26,26,0.12); }
  .sband-item:last-child { border-right:none; }
  .sband-num { font-size:2.25rem; font-weight:700; color:#1A2A1C; line-height:1; margin-bottom:0.3rem; }
  .sband-lbl { font-size:0.78rem; color:rgba(26,42,28,0.65); font-weight:600; }
  .home-about { padding:8rem 0; background:var(--cream); }
  .ha-grid { display:grid; grid-template-columns:1fr 1fr; gap:6rem; align-items:center; }
  .home-services { padding:8rem 0; background:linear-gradient(180deg,#0D2C1E 0%,#1B4D35 100%); }
  .svc-grid-home { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; }
  .svc-card { background:rgba(255,255,255,0.05); border:1px solid rgba(77,153,112,0.18); border-radius:14px; padding:2rem 1.75rem; transition:background 0.3s,transform 0.25s,border-color 0.3s; position:relative; overflow:hidden; text-decoration:none; display:block; }
  .svc-card::before { content:''; position:absolute; bottom:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--forest-lt),var(--amber)); transform:scaleX(0); transform-origin:left; transition:transform 0.4s ease; }
  .svc-card:hover { background:rgba(77,153,112,0.1); transform:translateY(-4px); border-color:rgba(77,153,112,0.45); }
  .svc-card:hover::before { transform:scaleX(1); }
  .svc-ico { width:48px; height:48px; border-radius:12px; background:rgba(77,153,112,0.12); border:1px solid rgba(77,153,112,0.28); display:flex; align-items:center; justify-content:center; font-size:1.2rem; margin-bottom:1.4rem; color:var(--forest-lt); }
  .svc-title { font-size:1.05rem; font-weight:700; color:var(--white); margin-bottom:0.65rem; }
  .svc-desc { font-size:0.83rem; color:rgba(255,255,255,0.5); line-height:1.75; }
  .svcs-footer { text-align:center; margin-top:3.5rem; }
  .home-cta { background:var(--forest); padding:6rem 4rem; text-align:center; position:relative; overflow:hidden; }
  .home-cta::before { content:''; position:absolute; top:-80px; left:50%; transform:translateX(-50%); width:700px; height:350px; border-radius:50%; background:rgba(77,153,112,0.12); pointer-events:none; }
  .home-cta h2 { font-size:clamp(2rem,3vw,3rem); font-weight:700; color:var(--white); margin-bottom:1rem; position:relative; }
  .home-cta h2 em { font-style:italic; font-family:var(--serif); color:var(--amber-lt); }
  .home-cta p { font-size:1.05rem; color:rgba(255,255,255,0.65); margin-bottom:2.5rem; max-width:500px; margin-left:auto; margin-right:auto; position:relative; }
  @keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
  .hero-left > * { animation:fadeUp 0.7s ease both; }
  .hero-left > *:nth-child(1){animation-delay:0.05s;} .hero-left > *:nth-child(2){animation-delay:0.18s;} .hero-left > *:nth-child(3){animation-delay:0.3s;} .hero-left > *:nth-child(4){animation-delay:0.42s;} .hero-left > *:nth-child(5){animation-delay:0.54s;}
  .home-social { background:var(--forest-pale); padding:6rem 0; border-top:1px solid rgba(27,77,53,0.1); border-bottom:1px solid rgba(27,77,53,0.1); }
  .home-social-inner { max-width:1300px; margin:0 auto; padding:0 4rem; text-align:center; }
  .home-social-btns { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; margin-top:2.5rem; }
  @media(max-width:1100px){ .hero-inner,.ha-grid{grid-template-columns:1fr;} .hero-right{display:none;} .hero-left{padding:7rem 0 5rem;} .svc-grid-home{grid-template-columns:1fr 1fr;} .stats-band{padding:1.75rem 1.5rem;} .home-cta{padding:5rem 1.5rem;} .home-social-inner{padding:0 1.5rem;} }
  @media(max-width:700px){ .svc-grid-home{grid-template-columns:1fr;} .sband-item{flex:0 0 50%;border-right:none;border-bottom:1px solid rgba(26,42,28,0.1);padding:1rem;} .stats-band{flex-wrap:wrap;} }
"""

ABOUT_CSS = SHARED_CSS + PAGE_HERO_CSS + """
  .about-grid { display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:start; padding:8rem 0; }
  .about-dark { background:linear-gradient(180deg,#0D2C1E 0%,#1B4D35 100%); padding:8rem 0; }
  .diff-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; margin-top:3.5rem; }
  .diff-card { background:rgba(255,255,255,0.06); border:1px solid rgba(77,153,112,0.2); border-radius:14px; padding:2rem 1.75rem; }
  .diff-icon { font-size:1.8rem; margin-bottom:1rem; color:var(--amber); }
  .diff-title { font-size:1rem; font-weight:700; color:var(--white); margin-bottom:0.6rem; }
  .diff-body { font-size:0.85rem; color:rgba(255,255,255,0.52); line-height:1.75; }
  .team-form { background:var(--sand); border-radius:16px; padding:3rem; border:1.5px solid rgba(27,77,53,0.1); }
  .team-section { padding:8rem 0; background:var(--cream); }
  .team-grid { display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:start; }
  @media(max-width:1000px){ .about-grid,.team-grid{grid-template-columns:1fr;gap:3rem;} .diff-grid{grid-template-columns:1fr 1fr;} .page-hero-inner{padding:0 1.5rem;} }
  @media(max-width:700px){ .diff-grid{grid-template-columns:1fr;} }
"""

SERVICES_CSS = SHARED_CSS + PAGE_HERO_CSS + """
  .services-list { padding:7rem 0; }
  .svc-full { display:grid; grid-template-columns:1fr 1fr; gap:5rem; align-items:center; padding:5rem 0; border-bottom:1.5px solid rgba(27,77,53,0.1); }
  .svc-full:last-child { border-bottom:none; }
  .svc-full.flip { direction:rtl; }
  .svc-full.flip > * { direction:ltr; }
  .svc-full-icon { font-size:2.6rem; margin-bottom:1.25rem; display:block; color:var(--forest-mid); }
  .svc-full-title { font-size:1.75rem; font-weight:700; color:var(--charcoal); margin-bottom:1rem; font-family:var(--serif); }
  .svc-full-body { font-size:0.975rem; color:var(--mid); line-height:1.9; margin-bottom:1.75rem; }
  .svc-visual { background:var(--forest-frost); border:1.5px solid rgba(27,77,53,0.12); border-radius:14px; padding:2rem; }
  .svc-point { display:flex; align-items:center; gap:0.9rem; padding:0.65rem 0; border-bottom:1px solid rgba(27,77,53,0.08); }
  .svc-point:last-child { border-bottom:none; }
  .svc-point-dot { width:8px; height:8px; border-radius:50%; background:var(--forest-lt); flex-shrink:0; }
  .svc-point-text { font-size:0.88rem; color:var(--mid); }
  .svc-cta { background:var(--forest); padding:6rem 4rem; text-align:center; position:relative; overflow:hidden; }
  .svc-cta::before { content:''; position:absolute; inset:0; background-image:radial-gradient(rgba(255,255,255,0.04) 1px,transparent 1px); background-size:28px 28px; pointer-events:none; }
  .svc-cta h2 { font-size:clamp(1.8rem,3vw,2.75rem); font-weight:700; color:var(--white); margin-bottom:1rem; position:relative; }
  .svc-cta h2 em { font-style:italic; font-family:var(--serif); color:var(--amber-lt); }
  .svc-cta p { font-size:1rem; color:rgba(255,255,255,0.62); margin-bottom:2.5rem; max-width:480px; margin-left:auto; margin-right:auto; position:relative; }
  @media(max-width:1000px){ .svc-full,.svc-full.flip{grid-template-columns:1fr;direction:ltr;gap:2.5rem;} .page-hero-inner{padding:0 1.5rem;} .svc-cta{padding:4rem 1.5rem;} }
"""

CONTACT_CSS = SHARED_CSS + PAGE_HERO_CSS + """
  .contact-section { padding:8rem 0; background:var(--cream); }
  .contact-grid { display:grid; grid-template-columns:1fr 1.4fr; gap:5rem; align-items:start; }
  .contact-detail { display:flex; align-items:flex-start; gap:1rem; padding:1.5rem; border:1.5px solid rgba(27,77,53,0.1); border-radius:12px; background:var(--white); margin-bottom:1rem; transition:border-color 0.2s; }
  .contact-detail:hover { border-color:rgba(27,77,53,0.28); }
  .cd-icon { width:42px; height:42px; flex-shrink:0; border-radius:10px; background:rgba(27,77,53,0.1); display:flex; align-items:center; justify-content:center; font-size:1.1rem; color:var(--forest-mid); }
  .cd-label { font-size:0.72rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:var(--soft); margin-bottom:0.25rem; }
  .cd-value { font-size:0.95rem; font-weight:600; color:var(--charcoal); }
  .contact-form-wrap { background:var(--white); border:1.5px solid rgba(27,77,53,0.1); border-radius:16px; padding:3rem; box-shadow:var(--shadow); }
  @media(max-width:1000px){ .contact-grid{grid-template-columns:1fr;gap:3rem;} .page-hero-inner{padding:0 1.5rem;} .contact-section{padding:5rem 0;} }
"""

REFERRAL_CSS = SHARED_CSS + PAGE_HERO_CSS + """
  .referral-section { padding:8rem 0; background:var(--cream); }
  .referral-grid { display:grid; grid-template-columns:1fr 1.6fr; gap:5rem; align-items:start; }
  .ref-info-card { background:linear-gradient(150deg,var(--forest-dark),var(--forest)); border-radius:16px; padding:2.5rem; color:white; margin-bottom:1.5rem; }
  .ref-info-card h3 { font-size:1.15rem; font-weight:700; color:var(--white); margin-bottom:0.75rem; }
  .ref-info-card p { font-size:0.88rem; color:rgba(255,255,255,0.62); line-height:1.75; }
  .ref-step { display:flex; align-items:flex-start; gap:1rem; padding:1rem 0; border-bottom:1px solid rgba(27,77,53,0.1); }
  .ref-step:last-child { border-bottom:none; }
  .ref-step-num { width:28px; height:28px; border-radius:50%; background:var(--amber); color:#1A1A1A; font-size:0.78rem; font-weight:700; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
  .ref-step-text { font-size:0.88rem; color:var(--mid); line-height:1.6; padding-top:4px; }
  .ref-steps { margin-top:1.5rem; }
  .referral-form-wrap { background:var(--white); border:1.5px solid rgba(27,77,53,0.1); border-radius:16px; padding:3rem; box-shadow:var(--shadow); }
  @media(max-width:1000px){ .referral-grid{grid-template-columns:1fr;gap:3rem;} .page-hero-inner{padding:0 1.5rem;} .referral-section{padding:5rem 0;} }
"""

# --------------------------------------------------------------------------
# NAV + FOOTER  (logo.png — real file)
# --------------------------------------------------------------------------
NAV_HOME   = '<a href="index.html" class="active">'
NAV_ABOUT  = '<a href="about.html" class="active">'
NAV_SVC    = '<a href="services.html" class="active">'
NAV_CON    = '<a href="contact.html" class="active">'
NAV_REF    = '<a href="referral.html" class="active">'

def nav(active='home'):
    links = {
        'home':    ('index.html',   'Home'),
        'about':   ('about.html',   'About'),
        'services':('services.html','Services'),
        'gallery': ('gallery.html', 'Gallery'),
        'contact': ('contact.html', 'Contact'),
    }
    items = ''
    for key,(href,label) in links.items():
        cls = ' class="active"' if key==active else ''
        items += f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f"""<nav>
  <a href="index.html" class="nav-logo">
    <img src="logo.png" alt="Spring 2 Health" class="logo-img">
    <span class="logo-sub">Disability Support &middot; Queensland</span>
  </a>
  <ul class="nav-links">{items}<li><a href="referral.html" class="nav-btn">Make a Referral</a></li></ul>
</nav>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div>
      <div class="footer-logo"><img src="logo.png" alt="Spring 2 Health" class="footer-logo-img"></div>
      <p class="footer-tagline">A disability support provider based in Queensland, dedicated to improving the quality of life of our participants through holistic, person-centred care.</p>
      <div class="footer-social">
        <a href="https://instagram.com/spring2health" target="_blank" rel="noopener" aria-label="Instagram" class="footer-social-link ig"><i class="fa-brands fa-instagram"></i></a>
        <a href="https://facebook.com/spring2health" target="_blank" rel="noopener" aria-label="Facebook" class="footer-social-link fb"><i class="fa-brands fa-facebook-f"></i></a>
      </div>
    </div>
    <div>
      <div class="footer-heading">Navigation</div>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About Us</a></li>
        <li><a href="services.html">Our Services</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="referral.html">Make a Referral</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-heading">Our Services</div>
      <ul class="footer-links">
        <li><a href="services.html">Social Work Services</a></li>
        <li><a href="services.html">Adventure Therapy</a></li>
        <li><a href="services.html">Community Access</a></li>

        <li><a href="services.html">Respite Care</a></li>
        <li><a href="services.html">Positive Behaviour Support</a></li>
      </ul>
      <div class="footer-heading" style="margin-top:1.5rem;">Policies</div>
      <ul class="footer-links">
        <li><a href="#">Privacy Policy</a></li>
        <li><a href="#">Terms &amp; Conditions</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2025 Spring 2 Health. All rights reserved. Formerly Pristine Lifestyle Solutions.</span>
    <span><a href="#">Privacy</a> &middot; <a href="#">Terms</a></span>
  </div>
</footer>"""

# --------------------------------------------------------------------------
# INDEX BODY
# --------------------------------------------------------------------------
INDEX_BODY = nav('home') + """
<section id="hero">
  <div class="hc hc1"></div><div class="hc hc2"></div><div class="hero-dots"></div>
  <svg class="hero-mountain" viewBox="0 0 1440 200" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0,200 L0,120 L160,58 L280,108 L420,28 L560,88 L700,18 L840,78 L980,38 L1120,92 L1280,48 L1440,88 L1440,200 Z" fill="rgba(13,44,30,0.55)"/>
    <path d="M0,200 L0,148 L200,88 L360,138 L500,68 L660,128 L820,58 L960,118 L1100,72 L1260,122 L1440,78 L1440,200 Z" fill="rgba(10,31,20,0.75)"/>
  </svg>
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-badge"><div class="hero-badge-dot"></div><span>NDIS Registered Provider &mdash; Queensland</span></div>
      <h1 class="hero-h1">Providing you with<br>the support you<br><span class="accent italic">truly deserve</span></h1>
      <p class="hero-sub">We take a holistic, strength-based, person-centred approach &mdash; working in close partnership with you, your family, and your support network.</p>
      <ul class="hero-pills">
        <li class="hero-pill"><div class="hero-pill-check"><i class="fa-solid fa-check"></i></div>Specialists in Mental Health &amp; Psychosocial Disability</li>
        <li class="hero-pill"><div class="hero-pill-check"><i class="fa-solid fa-check"></i></div>Respite Care &amp; Accommodation</li>
        <li class="hero-pill"><div class="hero-pill-check"><i class="fa-solid fa-check"></i></div>Social Work &amp; Therapeutic Services</li>
        <li class="hero-pill"><div class="hero-pill-check"><i class="fa-solid fa-check"></i></div>Adventure Therapy &amp; Community Access</li>
      </ul>
      <div class="hero-btns"><a href="referral.html" class="btn-primary">Make a Referral</a><a href="services.html" class="btn-outline">Explore Our Services</a></div>
    </div>
    <div class="hero-right">
      <div class="hcard featured"><div class="hcard-icon"><i class="fa-solid fa-mountain-sun"></i></div><div><div class="hcard-name">Adventure Therapy</div><div class="hcard-desc">Innovative outdoor programs building resilience and well-being.</div></div></div>
      <div class="hcard"><div class="hcard-icon"><i class="fa-solid fa-handshake-angle"></i></div><div><div class="hcard-name">Social Work Services</div><div class="hcard-desc">Qualified social workers guiding you through life&#39;s challenges.</div></div></div>
      <div class="hcard"><div class="hcard-icon"><i class="fa-solid fa-people-group"></i></div><div><div class="hcard-name">Community Access</div><div class="hcard-desc">Supporting you to engage and build meaningful connections.</div></div></div>
      <div class="hcard"><div class="hcard-icon"><i class="fa-solid fa-bed"></i></div><div><div class="hcard-name">Respite Care</div><div class="hcard-desc">Flexible short-term care giving caregivers a well-earned break.</div></div></div>
    </div>
  </div>
</section>
<div class="stats-band">
  <div class="sband-item"><div class="sband-num">6+</div><div class="sband-lbl">Support Services</div></div>
  <div class="sband-item"><div class="sband-num">24/7</div><div class="sband-lbl">Support Available</div></div>
  <div class="sband-item"><div class="sband-num">NDIS</div><div class="sband-lbl">Registered Provider</div></div>
  <div class="sband-item"><div class="sband-num">QLD</div><div class="sband-lbl">Gold Coast</div></div>
</div>
<section class="home-about">
  <div class="section-inner">
    <div class="ha-grid">
      <div>
        <div class="pill-label"><div class="dot"></div>About Spring 2 Health</div>
        <h2 class="sh2">We are <em>curious</em> to get to know you</h2>
        <p class="sbody" style="margin-bottom:1.25rem;">At Spring 2 Health, we want to get to know all about you as the expert in your own life. We take a person-centred approach to understanding who you are at a deeper level so we can provide individualised disability support that speaks to exactly who you are.</p>
        <p class="sbody" style="margin-bottom:2rem;">Our focus is improving your quality of life through working in close partnership with yourself, your family, and support network.</p>
        <a href="about.html" class="btn-primary" style="display:inline-block;">Learn More About Us</a>
        <div class="about-values" style="margin-top:2.5rem;">
          <div class="av"><div class="av-icon"><i class="fa-solid fa-bullseye"></i></div><div><strong>Uniquely Tailored to You</strong><span>Support designed around your individual needs, goals, and aspirations.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-handshake"></i></div><div><strong>Collaborative by Nature</strong><span>Working alongside you and your entire support network.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-lightbulb"></i></div><div><strong>Deeper Understanding</strong><span>Operating from curiosity &mdash; learning about your strengths and aspirations.</span></div></div>
        </div>
      </div>
      <div style="position:relative;padding-bottom:2rem;">
        <div class="quote-card">
          <div class="quote-text"><span class="qm">&#8220;</span>We provide support differently. Most organisations think of their bottom line. We&#39;re in this for our participants.</div>
          <div class="quote-footer"><div class="quote-line"></div><div class="quote-name">Spring 2 Health &mdash; Our Promise</div></div>
        </div>
        <div class="quote-badge"><strong>100%</strong><span>Participant<br>Centred</span></div>
      </div>
    </div>
  </div>
</section>
<section class="home-services">
  <div class="section-inner">
    <div style="text-align:center;max-width:560px;margin:0 auto 4rem;">
      <div class="pill-label light" style="margin:0 auto 1.25rem;"><div class="dot"></div>Our Support Services</div>
      <h2 class="sh2 light">Improving your <em>quality of life</em></h2>
    </div>
    <div class="svc-grid-home">
      <a href="services.html" class="svc-card"><div class="svc-ico"><i class="fa-solid fa-handshake-angle"></i></div><div class="svc-title">Social Work Services</div><div class="svc-desc">Qualified social workers providing guidance and advocacy for NDIS participants.</div></a>
      <a href="services.html" class="svc-card"><div class="svc-ico"><i class="fa-solid fa-bed"></i></div><div class="svc-title">Respite Care</div><div class="svc-desc">Short and medium-term relief for caregivers with flexible arrangements.</div></a>
      <a href="services.html" class="svc-card"><div class="svc-ico"><i class="fa-solid fa-people-group"></i></div><div class="svc-title">Community Access</div><div class="svc-desc">Breaking down barriers so you can actively participate in your community.</div></a>

      <a href="services.html" class="svc-card"><div class="svc-ico"><i class="fa-solid fa-mountain-sun"></i></div><div class="svc-title">Adventure Therapy</div><div class="svc-desc">Innovative outdoor programs for mental health and personal growth.</div></a>
      <a href="services.html" class="svc-card"><div class="svc-ico"><i class="fa-solid fa-clipboard-check"></i></div><div class="svc-title">Behaviour Support</div><div class="svc-desc">Positive behaviour support plans tailored to your unique circumstances.</div></a>
    </div>
    <div class="svcs-footer"><a href="services.html" class="btn-primary">View All Services</a></div>
  </div>
</section>
<section class="home-social">
  <div class="home-social-inner">
    <div class="pill-label" style="margin:0 auto 1.25rem;"><div class="dot"></div>Stay Connected</div>
    <h2 class="sh2">Follow our <em>journey</em></h2>
    <p class="sbody" style="max-width:520px;margin:0 auto;">See our adventures, community moments, and participant stories on social media &mdash; or browse our full gallery.</p>
    <div class="home-social-btns">
      <a href="https://instagram.com/spring2health" target="_blank" rel="noopener" class="social-btn ig"><i class="fa-brands fa-instagram"></i> Follow on Instagram</a>
      <a href="https://facebook.com/spring2health" target="_blank" rel="noopener" class="social-btn fb"><i class="fa-brands fa-facebook-f"></i> Follow on Facebook</a>
      <a href="gallery.html" class="btn-dark"><i class="fa-solid fa-images" style="margin-right:0.5rem;"></i>View Gallery</a>
    </div>
  </div>
</section>
<section class="home-cta">
  <h2>Ready to <em>get started?</em></h2>
  <p>Our team are here to support you. Make a referral today and we&#39;ll be in touch to discuss how we can help.</p>
  <a href="referral.html" class="btn-primary">Make a Referral</a>
</section>
""" + FOOTER

# --------------------------------------------------------------------------
# ABOUT BODY
# --------------------------------------------------------------------------
ABOUT_BODY = nav('about') + """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="pill-label light" style="margin-bottom:1.25rem;"><div class="dot"></div>About Us</div>
    <h1 class="page-title">Who we <em>are</em></h1>
    <p class="page-subtitle">A disability support provider that puts people first &mdash; always curious, always collaborative, always person-centred.</p>
  </div>
</div>
<div style="background:var(--cream);">
  <div class="section-inner">
    <div class="about-grid">
      <div>
        <div class="pill-label"><div class="dot"></div>Our Philosophy</div>
        <h2 class="sh2">We are <em>curious</em> to get to know you</h2>
        <p class="sbody" style="margin-bottom:1.5rem;">At Spring 2 Health, we want to get to know all about you as the expert in your own life. We take a person-centred approach to understanding who you are at a deeper level so that we can provide individualised disability support that speaks to exactly who you are.</p>
        <p class="sbody" style="margin-bottom:1.5rem;">We operate from a curiosity standpoint and are constantly seeking to learn more about our participants and their unique situations. Our approach is strength-based &mdash; we focus on abilities and potential rather than limitations.</p>
        <p class="sbody">We recognise that our participants are experts in their own lives, and we work to empower them to make their own decisions and live their lives to the fullest. We operate from a place of diversity and inclusion, ensuring that everyone feels valued and respected.</p>
      </div>
      <div>
        <div class="about-values">
          <div class="av"><div class="av-icon"><i class="fa-solid fa-bullseye"></i></div><div><strong>Uniquely Tailored to You</strong><span>Every participant receives support designed around their individual needs, goals, and aspirations.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-handshake"></i></div><div><strong>Collaborative by Nature</strong><span>We work alongside you and your entire support network, never in isolation.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-lightbulb"></i></div><div><strong>Understanding at a Deeper Level</strong><span>Operating from curiosity &mdash; constantly seeking to learn more about you and your strengths.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-scale-balanced"></i></div><div><strong>Fairness &amp; Transparency</strong><span>Committed to fairness and transparency in all interactions, with the highest standards of integrity.</span></div></div>
        </div>
      </div>
    </div>
  </div>
</div>
<section class="about-dark">
  <div class="section-inner">
    <div style="text-align:center;max-width:580px;margin:0 auto 4rem;">
      <div class="pill-label light" style="margin:0 auto 1.25rem;"><div class="dot"></div>Why Spring 2 Health</div>
      <h2 class="sh2 light">We provide support <em>differently</em></h2>
      <p class="sbody light">Through providing a tailored service unique to you &mdash; your obstacles and your aspirations &mdash; we deliver care that supports you as an individual.</p>
    </div>
    <div class="diff-grid">
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-person-hiking"></i></div><div class="diff-title">Adventure Therapy</div><div class="diff-body">Innovative outdoor programs using nature and adventure to build resilience, self-esteem, and mental well-being in a supported environment.</div></div>
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-scale-balanced"></i></div><div class="diff-title">Social Work &amp; Advocacy</div><div class="diff-body">Our qualified social workers are specialists in navigating complex disability systems, advocating for your rights every step of the way.</div></div>
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-seedling"></i></div><div class="diff-title">Strength-Based Approach</div><div class="diff-body">We focus on your abilities, strengths, and potential &mdash; not your limitations. Every plan is built around what you can do and where you want to go.</div></div>
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-brain"></i></div><div class="diff-title">Evidence-Based Therapy</div><div class="diff-body">Therapeutic services grounded in current best practice &mdash; helping you develop coping strategies and improve mental health and well-being.</div></div>
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-people-arrows"></i></div><div class="diff-title">Community Connected</div><div class="diff-body">We break down barriers to community participation, helping you build meaningful relationships and engage with the things that matter to you.</div></div>
      <div class="diff-card"><div class="diff-icon"><i class="fa-solid fa-heart-pulse"></i></div><div class="diff-title">Trauma-Informed Practice</div><div class="diff-body">All our services are delivered through a trauma-informed lens &mdash; safe, empowering, and grounded in compassion and respect.</div></div>
    </div>
    <div style="max-width:700px;margin:5rem auto 0;">
      <div class="quote-card">
        <div class="quote-text"><span class="qm">&#8220;</span>We provide support differently. Most organisations think of their bottom line. We&#39;re in this for our participants &mdash; putting you first in everything we do.</div>
        <div class="quote-footer"><div class="quote-line"></div><div class="quote-name">Spring 2 Health &mdash; Our Promise</div></div>
      </div>
    </div>
  </div>
</section>
<section class="team-section">
  <div class="section-inner">
    <div class="team-grid">
      <div>
        <div class="pill-label"><div class="dot"></div>Join Our Team</div>
        <h2 class="sh2">Want to work with <em>Spring 2 Health?</em></h2>
        <p class="sbody" style="margin-bottom:2rem;">We&#39;d love to hear from passionate people who share our values. Complete the form and we&#39;ll be in touch about available roles that suit your experience.</p>
        <div class="about-values">
          <div class="av"><div class="av-icon"><i class="fa-solid fa-bullseye"></i></div><div><strong>Purpose-Driven Work</strong><span>Make a real difference in the lives of people living with disability every day.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-mountain-sun"></i></div><div><strong>Adventure Therapy Opportunities</strong><span>Deliver innovative outdoor programs that genuinely change lives in the community.</span></div></div>
          <div class="av"><div class="av-icon"><i class="fa-solid fa-handshake"></i></div><div><strong>Supportive Team Culture</strong><span>Join a values-led team that genuinely cares about each other and participants.</span></div></div>
        </div>
      </div>
      <div>
        <div class="team-form">
          <h3 style="font-size:1.3rem;font-weight:700;color:var(--charcoal);margin-bottom:0.5rem;">Express Your Interest</h3>
          <p style="font-size:0.88rem;color:var(--soft);margin-bottom:2rem;">Tell us a little about yourself and what role you&#39;re interested in.</p>
          <div class="fg2">
            <div class="ff"><label>First Name</label><input type="text" placeholder="First name"></div>
            <div class="ff"><label>Last Name</label><input type="text" placeholder="Last name"></div>
            <div class="ff s2"><label>Email Address</label><input type="email" placeholder="Your email address"></div>
            <div class="ff s2"><label>Role of Interest</label><select><option value="">Select a role...</option><option>Support Worker</option><option>Social Worker</option><option>Adventure Therapy Facilitator</option><option>Team Leader</option><option>Other</option></select></div>
            <div class="ff s2"><label>Tell Us About Yourself</label><textarea style="min-height:110px;" placeholder="Your background, experience, and why you want to join our team..."></textarea></div>
          </div>
          <button class="btn-submit">Send Expression of Interest</button>
        </div>
      </div>
    </div>
  </div>
</section>
""" + FOOTER

# --------------------------------------------------------------------------
# SERVICES BODY  (SIL removed)
# --------------------------------------------------------------------------
SERVICES_BODY = nav('services') + """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="pill-label light" style="margin-bottom:1.25rem;"><div class="dot"></div>What We Offer</div>
    <h1 class="page-title">Our Support <em>Services</em></h1>
    <p class="page-subtitle">We collaborate closely with our participants and their support networks to ensure the best possible care &mdash; making a genuine and positive impact on every life we touch.</p>
  </div>
</div>
<section class="services-list">
  <div class="section-inner">

    <div class="svc-full">
      <div>
        <span class="svc-full-icon"><i class="fa-solid fa-handshake-angle"></i></span>
        <h2 class="svc-full-title">Social Work Services</h2>
        <p class="svc-full-body">Our team of qualified social workers are here to provide you with the support and guidance you need to achieve your goals and improve your quality of life. We navigate complex issues that can arise when living with a disability.</p>
        <a href="referral.html" class="btn-primary" style="display:inline-block;">Make a Referral</a>
      </div>
      <div class="svc-visual">

        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Advocacy and rights support</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Referrals to appropriate community services</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Personalised support plan development</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Collaborative work with your full care team</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">NDIS plan guidance and coordination</div></div>
      </div>
    </div>

    <div class="svc-full flip">
      <div>
        <span class="svc-full-icon"><i class="fa-solid fa-mountain-sun"></i></span>
        <h2 class="svc-full-title">Adventure Therapy</h2>
        <p class="svc-full-body">Our innovative Adventure Therapy program is designed to help you build resilience, overcome challenges, and develop a deeper understanding of yourself through outdoor activities and adventure. Hiking, climbing, camping and more &mdash; all in a safe, professionally supported environment.</p>
        <a href="referral.html" class="btn-primary" style="display:inline-block;">Make a Referral</a>
      </div>
      <div class="svc-visual">
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Hiking, rock climbing, camping and more</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Personalised program for your needs</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Resilience and self-esteem building</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Mental health through outdoor engagement</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Safe and fully supported environment</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Experienced adventure therapy team</div></div>
      </div>
    </div>

    <div class="svc-full">
      <div>
        <span class="svc-full-icon"><i class="fa-solid fa-bed"></i></span>
        <h2 class="svc-full-title">Respite Care</h2>
        <p class="svc-full-body">Our NDIS respite care services are designed to provide temporary relief to primary caregivers and support workers, enabling you to take a break and recharge. We offer flexible and personalised respite care tailored to each individual.</p>
        <a href="referral.html" class="btn-primary" style="display:inline-block;">Make a Referral</a>
      </div>
      <div class="svc-visual">
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">In-home respite care support</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Centre-based and community-based care</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Short and medium term accommodation</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Flexible scheduling around your needs</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Experienced and compassionate care team</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Safe environment for all participants</div></div>
      </div>
    </div>

    <div class="svc-full flip">
      <div>
        <span class="svc-full-icon"><i class="fa-solid fa-people-group"></i></span>
        <h2 class="svc-full-title">Community Access</h2>
        <p class="svc-full-body">At Spring 2 Health, we are dedicated to helping you access the services and activities in your community. We work closely with you to understand your interests and goals, then develop a personalised plan to achieve them.</p>
        <a href="referral.html" class="btn-primary" style="display:inline-block;">Make a Referral</a>
      </div>
      <div class="svc-visual">
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Attendance at community events and activities</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Access to local services and programs</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Building meaningful community relationships</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Transport and accompaniment support</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Tailored to your individual interests</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Breaking down barriers to participation</div></div>
      </div>
    </div>


    <div class="svc-full flip">
      <div>
        <span class="svc-full-icon"><i class="fa-solid fa-clipboard-check"></i></span>
        <h2 class="svc-full-title">Positive Behaviour Support</h2>
        <p class="svc-full-body">We are dedicated to supporting individuals with challenging behaviours to lead more fulfilling lives. Our experienced behaviour support specialists take a proactive, person-centred approach.</p>
        <a href="referral.html" class="btn-primary" style="display:inline-block;">Make a Referral</a>
      </div>
      <div class="svc-visual">
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Comprehensive Positive Behaviour Support Plans</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Proactive rather than reactive strategies</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Collaborative with your full care network</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Practical coping tools and strategies</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Tailored to your unique circumstances</div></div>
        <div class="svc-point"><div class="svc-point-dot"></div><div class="svc-point-text">Regular review and adaptation of plans</div></div>
      </div>
    </div>

  </div>
</section>
<section class="svc-cta">
  <h2>Ready to <em>get started?</em></h2>
  <p>Our team are here to support you. Make a referral today and we&#39;ll be in touch to discuss how we can help.</p>
  <a href="referral.html" class="btn-primary">Make a Referral</a>
</section>
""" + FOOTER

# --------------------------------------------------------------------------
# FORM SUBMISSION JS  (injected into contact + referral pages)
# --------------------------------------------------------------------------
FORM_JS = """<script>
(function () {
  document.querySelectorAll('.s2h-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('.btn-submit');
      var msg = form.querySelector('.form-msg');
      var orig = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending…';
      msg.className = 'form-msg';
      msg.textContent = '';
      var data = { type: form.dataset.type };
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function () {
        msg.textContent = '✓ Thank you — we'll be in touch soon.';
        msg.className = 'form-msg form-success';
        form.reset();
        btn.disabled = false;
        btn.textContent = orig;
      })
      .catch(function () {
        msg.textContent = 'Something went wrong. Please email us at info@spring2health.com.au';
        msg.className = 'form-msg form-error';
        btn.disabled = false;
        btn.textContent = orig;
      });
    });
  });
})();
</script>"""

# --------------------------------------------------------------------------
# CONTACT BODY
# --------------------------------------------------------------------------
CONTACT_BODY = nav('contact') + """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="pill-label light" style="margin-bottom:1.25rem;"><div class="dot"></div>Get In Touch</div>
    <h1 class="page-title">Let&#39;s <em>Connect</em></h1>
    <p class="page-subtitle">Are you or a loved one ready to start receiving Spring 2 Health care? Our team are here to support you.</p>
  </div>
</div>
<section class="contact-section">
  <div class="section-inner">
    <div class="contact-grid">
      <div>
        <div class="pill-label"><div class="dot"></div>Contact Details</div>
        <h2 class="sh2">We&#39;d love to <em>hear from you</em></h2>
        <p class="sbody" style="margin:1.25rem 0 2.5rem;">Our team can&#39;t wait to get to know more about you and help you achieve your goals. Reach out via any of the channels below.</p>
        <div class="contact-detail"><div class="cd-icon"><i class="fa-solid fa-location-dot"></i></div><div><div class="cd-label">Location</div><div class="cd-value">Gold Coast, Queensland</div></div></div>
        <div class="contact-detail"><div class="cd-icon"><i class="fa-solid fa-phone"></i></div><div><div class="cd-label">Phone</div><div class="cd-value">Available on request</div></div></div>
        <div class="contact-detail"><div class="cd-icon"><i class="fa-solid fa-envelope"></i></div><div><div class="cd-label">Email</div><div class="cd-value">info@spring2health.com.au</div></div></div>
        <div class="contact-detail"><div class="cd-icon"><i class="fa-solid fa-clock"></i></div><div><div class="cd-label">Hours</div><div class="cd-value">24/7 Support Available</div></div></div>
      </div>
      <div>
        <div class="contact-form-wrap">
          <h3 style="font-size:1.3rem;font-weight:700;color:var(--charcoal);margin-bottom:0.5rem;">Send Us a Message</h3>
          <p style="font-size:0.88rem;color:var(--soft);margin-bottom:2rem;">We&#39;ll get back to you as soon as possible.</p>
          <form class="s2h-form" data-type="contact" novalidate>
          <div class="fg2">
            <div class="ff"><label>First Name</label><input type="text" name="first_name" placeholder="First name" required></div>
            <div class="ff"><label>Last Name</label><input type="text" name="last_name" placeholder="Last name" required></div>
            <div class="ff s2"><label>Contact Number</label><input type="tel" name="phone" placeholder="Your phone number"></div>
            <div class="ff s2"><label>Email Address</label><input type="email" name="email" placeholder="Your email address" required></div>
            <div class="ff s2"><label>Your Message</label><textarea name="message" style="min-height:130px;" placeholder="How can we help you?" required></textarea></div>
          </div>
          <div class="form-msg"></div>
          <button type="submit" class="btn-submit">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
""" + FORM_JS + FOOTER

# --------------------------------------------------------------------------
# REFERRAL BODY
# --------------------------------------------------------------------------
REFERRAL_BODY = nav('home') + """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="pill-label light" style="margin-bottom:1.25rem;"><div class="dot"></div>Get Started</div>
    <h1 class="page-title">Make a <em>Referral</em></h1>
    <p class="page-subtitle">Refer yourself or someone you care about to Spring 2 Health. We&#39;ll be in touch quickly to discuss how we can help.</p>
  </div>
</div>
<section class="referral-section">
  <div class="section-inner">
    <div class="referral-grid">
      <div>
        <div class="ref-info-card">
          <h3>Why Spring 2 Health?</h3>
          <p>We are an NDIS-registered provider committed to holistic, person-centred disability support in Queensland. From adventure therapy to social work, we offer a full range of services tailored to you.</p>
        </div>
        <h3 style="font-size:1rem;font-weight:700;color:var(--charcoal);margin-bottom:1rem;">How It Works</h3>
        <div class="ref-steps">
          <div class="ref-step"><div class="ref-step-num">1</div><div class="ref-step-text">Complete and submit the referral form</div></div>
          <div class="ref-step"><div class="ref-step-num">2</div><div class="ref-step-text">Our team reviews your referral within 1&ndash;2 business days</div></div>
          <div class="ref-step"><div class="ref-step-num">3</div><div class="ref-step-text">We contact you to discuss needs and appropriate services</div></div>
          <div class="ref-step"><div class="ref-step-num">4</div><div class="ref-step-text">We develop a personalised support plan together</div></div>
          <div class="ref-step"><div class="ref-step-num">5</div><div class="ref-step-text">Support begins &mdash; and we&#39;re with you every step of the way</div></div>
        </div>
      </div>
      <div>
        <div class="referral-form-wrap">
          <h3 style="font-size:1.3rem;font-weight:700;color:var(--charcoal);margin-bottom:0.5rem;">Referral Form</h3>
          <p style="font-size:0.88rem;color:var(--soft);margin-bottom:2rem;">Please provide as much detail as possible so we can best support the individual.</p>
          <form class="s2h-form" data-type="referral" novalidate>
          <div class="fg2">
            <div class="ff"><label>Participant First Name</label><input type="text" name="participant_first" placeholder="First name" required></div>
            <div class="ff"><label>Participant Last Name</label><input type="text" name="participant_last" placeholder="Last name" required></div>
            <div class="ff s2"><label>Date of Birth</label><input type="date" name="dob"></div>
            <div class="ff s2"><label>NDIS Number (if applicable)</label><input type="text" name="ndis_number" placeholder="e.g. 43000000000"></div>
            <div class="ff s2"><label>Contact Number</label><input type="tel" name="phone" placeholder="Phone number" required></div>
            <div class="ff s2"><label>Email Address</label><input type="email" name="email" placeholder="Email address"></div>
            <div class="ff s2"><label>Referral Source</label><select name="referral_source"><option value="">Who is making this referral?</option><option>Self-referral</option><option>Family / Carer</option><option>Support Coordinator</option><option>Healthcare Professional</option><option>Other</option></select></div>
            <div class="ff s2"><label>Services Required</label><select name="services_required"><option value="">Select primary service...</option><option>Social Work Services</option><option>Adventure Therapy</option><option>Respite Care</option><option>Community Access</option><option>Positive Behaviour Support</option></select></div>
            <div class="ff s2"><label>Additional Information</label><textarea name="additional_info" style="min-height:120px;" placeholder="Please describe the participant&#39;s needs, goals, and any other relevant information..."></textarea></div>
          </div>
          <div class="form-msg"></div>
          <button type="submit" class="btn-submit">Submit Referral</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
""" + FORM_JS + FOOTER

# --------------------------------------------------------------------------
# BUILD + WRITE
# --------------------------------------------------------------------------
FA_CDN = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">'

def build_page(title, css, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &mdash; Spring 2 Health</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
{FA_CDN}
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>"""

GALLERY_CSS = SHARED_CSS + PAGE_HERO_CSS + """
  .gallery-section { padding:6rem 0 8rem; background:var(--cream); }
  .gallery-social { background:var(--forest); padding:3.5rem 0; }
  .gallery-social-inner { max-width:1300px; margin:0 auto; padding:0 4rem; display:flex; align-items:center; justify-content:space-between; gap:2rem; flex-wrap:wrap; }
  .gallery-social-text h3 { font-size:1.2rem; font-weight:700; color:var(--white); margin-bottom:0.3rem; }
  .gallery-social-text p { font-size:0.88rem; color:rgba(255,255,255,0.5); }
  .gallery-social-links { display:flex; gap:0.85rem; }
  .gallery-section-inner { max-width:1300px; margin:0 auto; padding:0 4rem; }
  .gallery-intro { max-width:620px; margin:0 auto 3.5rem; text-align:center; }
  .gallery-grid { columns:3; column-gap:1.1rem; }
  .gal-item { break-inside:avoid; margin-bottom:1.1rem; border-radius:12px; overflow:hidden; position:relative; background:var(--sand); cursor:pointer; }
  .gal-item img { width:100%; display:block; transition:transform 0.4s ease; }
  .gal-item:hover img { transform:scale(1.04); }
  .gal-cap { position:absolute; bottom:0; left:0; right:0; padding:0.85rem 1rem; background:linear-gradient(transparent,rgba(10,31,20,0.88)); color:var(--white); font-size:0.8rem; font-weight:600; line-height:1.4; transform:translateY(100%); transition:transform 0.28s ease; }
  .gal-item:hover .gal-cap { transform:translateY(0); }
  .gal-item.gal-video { break-inside:avoid; margin-bottom:1.1rem; border-radius:12px; overflow:hidden; background:#000; }
  .gal-item.gal-video .gal-video-wrap { position:relative; padding-bottom:56.25%; }
  .gal-item.gal-video iframe { position:absolute; top:0; left:0; width:100%; height:100%; border:none; }
  .gal-item.gal-video .gal-cap { position:relative; transform:none; background:rgba(10,31,20,0.9); padding:0.75rem 1rem; }
  .gallery-empty { text-align:center; padding:6rem 2rem; }
  .gallery-empty-icon { font-size:3.5rem; color:rgba(27,77,53,0.18); margin-bottom:1.25rem; }
  .gallery-empty h3 { font-size:1.3rem; font-weight:700; color:var(--charcoal); margin-bottom:0.75rem; }
  .gallery-empty p { font-size:0.9rem; color:var(--soft); max-width:420px; margin:0 auto 0.5rem; line-height:1.75; }
  .gallery-empty code { font-size:0.8rem; background:var(--sand); padding:0.2rem 0.5rem; border-radius:4px; color:var(--forest-mid); }
  @media(max-width:1000px){ .gallery-grid{columns:2;} .gallery-social-inner{flex-direction:column;text-align:center;} .gallery-section-inner{padding:0 1.5rem;} .gallery-social-links{justify-content:center;} }
  @media(max-width:600px){ .gallery-grid{columns:1;} }
"""

GALLERY_BODY = nav('gallery') + """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="pill-label light" style="margin-bottom:1.25rem;"><div class="dot"></div>Our Community</div>
    <h1 class="page-title">Gallery &amp; <em>Stories</em></h1>
    <p class="page-subtitle">A window into the adventures, milestones, and everyday moments that make Spring 2 Health special.</p>
  </div>
</div>
<div class="gallery-social">
  <div class="gallery-social-inner">
    <div class="gallery-social-text">
      <h3>Follow us on social media</h3>
      <p>Stay up to date with our latest adventures and community events.</p>
    </div>
    <div class="gallery-social-links">
      <a href="https://instagram.com/spring2health" target="_blank" rel="noopener" class="social-btn ig"><i class="fa-brands fa-instagram"></i> Instagram</a>
      <a href="https://facebook.com/spring2health" target="_blank" rel="noopener" class="social-btn fb"><i class="fa-brands fa-facebook-f"></i> Facebook</a>
    </div>
  </div>
</div>
<section class="gallery-section">
  <div class="gallery-section-inner">
    <div class="gallery-intro">
      <div class="pill-label" style="margin:0 auto 1.25rem;"><div class="dot"></div>Photo &amp; Video</div>
      <h2 class="sh2">Moments that <em>matter</em></h2>
      <p class="sbody">From adventure therapy sessions to community events &mdash; a glimpse into life with Spring 2 Health.</p>
    </div>
    <div class="gallery-grid" id="media-grid"></div>
    <div class="gallery-empty" id="media-empty" style="display:none;">
      <div class="gallery-empty-icon"><i class="fa-solid fa-images"></i></div>
      <h3>Photos &amp; videos coming soon</h3>
      <p>Add your media to the <code>media/</code> folder and update the list below to display them here.</p>
      <p style="margin-top:0.75rem;color:var(--soft);font-size:0.82rem;">Open <code>gallery.html</code> and edit the <code>MEDIA</code> array in the &lt;script&gt; tag.</p>
    </div>
  </div>
</section>
<script>
(function () {
  // ─── ADD YOUR MEDIA HERE ────────────────────────────────────────────────
  // 1. Create a folder called  media/  next to this HTML file (if needed).
  // 2. Drop your image / video files into it.
  // 3. Add an entry below and save the file — it will appear on the page.
  //
  //  Photo:    { type: 'image',   src: 'media/photo.jpg',  cap: 'Caption' }
  //  YouTube:  { type: 'youtube', id:  'YOUTUBE_VIDEO_ID', cap: 'Caption' }
  //
  // Tall portrait shots look great mixed with landscape — just drop them in!
  // ────────────────────────────────────────────────────────────────────────
  var MEDIA = [

    // ---- paste your entries below this line ----

    // { type: 'image',   src: 'media/adventure1.jpg',   cap: 'Rock climbing session' },
    // { type: 'image',   src: 'media/community1.jpg',   cap: 'Community market day' },
    // { type: 'youtube', id:  'YOUTUBE_VIDEO_ID',        cap: 'Our adventure therapy program' },

    // ---- paste your entries above this line ----

  ];
  // ────────────────────────────────────────────────────────────────────────

  var grid  = document.getElementById('media-grid');
  var empty = document.getElementById('media-empty');

  if (!MEDIA.length) { empty.style.display = 'block'; return; }
  empty.style.display = 'none';

  MEDIA.forEach(function (item) {
    var el = document.createElement('div');
    if (item.type === 'image') {
      el.className = 'gal-item';
      el.innerHTML =
        '<img src="' + item.src + '" alt="' + (item.cap || '') + '" loading="lazy">' +
        (item.cap ? '<div class="gal-cap">' + item.cap + '</div>' : '');
    } else if (item.type === 'youtube') {
      el.className = 'gal-item gal-video';
      el.innerHTML =
        '<div class="gal-video-wrap"><iframe src="https://www.youtube.com/embed/' + item.id +
        '?rel=0" allowfullscreen loading="lazy"></iframe></div>' +
        (item.cap ? '<div class="gal-cap">' + item.cap + '</div>' : '');
    }
    if (el.className) grid.appendChild(el);
  });
})();
</script>
""" + FOOTER

# --------------------------------------------------------------------------
pages = [
    ('index.html',   'Home',     INDEX_CSS,    INDEX_BODY),
    ('about.html',   'About Us', ABOUT_CSS,    ABOUT_BODY),
    ('services.html','Services', SERVICES_CSS, SERVICES_BODY),
    ('contact.html', 'Contact',  CONTACT_CSS,  CONTACT_BODY),
    ('referral.html','Referral', REFERRAL_CSS, REFERRAL_BODY),
    ('gallery.html', 'Gallery',  GALLERY_CSS,  GALLERY_BODY),
]

for filename, title, css, body in pages:
    html = build_page(title, css, body)
    with open(f'{BASE}/{filename}', 'w') as f:
        f.write(html)
    print(f"OK  {filename}  ({len(html):,} bytes)")

print("\nDone. Cleanup transform.py if not needed.")
