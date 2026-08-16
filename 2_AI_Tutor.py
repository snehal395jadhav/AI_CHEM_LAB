import streamlit as st
import streamlit.components.v1 as components
import sys, os, json as _json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.styles import MAIN_CSS
from utils.openrouter_ai import MODELS, call_openrouter, CHEM_SYSTEM_PROMPT

st.set_page_config(page_title="Chem Agent | ChemVerse AI", page_icon=":material/smart_toy:", layout="wide")
st.markdown(MAIN_CSS, unsafe_allow_html=True)
from u
    background:linear-gradient(135deg,#7c3aed,#0ea5e9);
    display:flex;align-items:center;justify-content:center;
    font-size:14px;box-shadow:0 0 12px rgba(139,92,246,0.4);
}

/* ── Control bar (mode + settings above chat) ── */
.cv-control-bar{
    display:flex;align-items:center;gap:8px;
    padding:8px 14px;
    background:rgba(10,5,30,0.9);
    border:1px solid rgba(100,60,200,0.18);
    border-radius:14px;margin-bottom:6px;
}

/* ── Selectbox (mode + model) ── */
div[data-testid="stSelectbox"] > div > div{
    background:rgba(8,4,22,0.9)!important;
    border:1px solid rgba(100,60,200,0.28)!important;
    border-radius:12px!important;
    color:rgba(210,190,255,0.9)!important;
    font-family:'Inter',sans-serif!important;font-size:13px!important;
}
div[data-testid="stSelectbox"] > div > div:focus-within{
    border-color:rgba(139,92,246,0.65)!important;
    box-shadow:0 0 14px rgba(139,92,246,0.14)!important;
}

/* ── Divider ── */
.cv-div{height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,0.2),transparent);margin:8px 0;}

/* ── Chat sub-header ── */
.cv-chat-subhdr{
    display:flex;align-items:center;gap:10px;
    padding:9px 14px;
    background:rgba(12,6,36,0.9);
    border:1px solid rgba(100,60,210,0.18);
    border-radius:12px;margin-bottom:8px;
}
.cv-ai-ava{
    width:36px;height:36px;border-radius:50%;flex-shrink:0;
    background:linear-gradient(135deg,#7c3aed,#0ea5e9);
    display:flex;align-items:center;justify-content:center;font-size:16px;
    box-shadow:0 0 14px rgba(139,92,246,0.42);
}
.cv-dot{width:7px;height:7px;border-radius:50%;background:#00FFB4;
        box-shadow:0 0 7px #00FFB4;display:inline-block;vertical-align:middle;margin-right:4px;}
.cv-chip{padding:2px 8px;border-radius:14px;
         font-family:'Share Tech Mono',monospace;font-size:10px;white-space:nowrap;}
.cv-c1{background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.28);color:rgba(192,132,252,0.85);}
.cv-c2{background:rgba(34,211,238,0.07);border:1px solid rgba(34,211,238,0.25);color:rgba(34,211,238,0.78);}
.cv-c3{background:rgba(0,255,180,0.05);border:1px solid rgba(0,255,180,0.2);color:rgba(0,255,180,0.7);}

/* ── Message bubbles ── */
.cv-user-wrap{display:flex;justify-content:flex-start;margin:10px 0;}
.cv-user-bubble{
    max-width:55%;
    background:linear-gradient(135deg,rgba(26,12,72,0.9),rgba(18,8,50,0.95));
    border:1px solid rgba(100,65,220,0.38);border-radius:14px 14px 14px 4px;
    padding:10px 14px;
}
.cv-user-label{
    font-family:'Share Tech Mono',monospace;font-size:10px;
    color:rgba(100,65,220,0.55);letter-spacing:2px;display:block;margin-bottom:5px;
}
.cv-user-text{
    font-family:'Inter',sans-serif;font-size:13.5px;
    color:rgba(205,190,255,0.92);line-height:1.55;
}
.cv-ai-wrap{display:flex;justify-content:flex-end;margin:10px 0;}
.cv-ai-card{
    max-width:72%;
    background:linear-gradient(135deg,rgba(14,8,40,0.92),rgba(10,5,28,0.96));
    border:1px solid rgba(80,45,190,0.22);border-radius:14px 14px 4px 14px;
    padding:13px 15px;
}
.cv-ai-card-hdr{
    display:flex;align-items:center;gap:8px;
    padding-bottom:9px;margin-bottom:9px;
    border-bottom:1px solid rgba(100,60,200,0.15);
}
.cv-ai-card-ava{
    width:26px;height:26px;border-radius:50%;flex-shrink:0;
    background:linear-gradient(135deg,#7c3aed,#0ea5e9);
    display:flex;align-items:center;justify-content:center;font-size:12px;
}
.cv-ai-card-name{
    font-family:'Orbitron',monospace;font-size:0.56em;font-weight:700;
    letter-spacing:2px;color:rgba(180,155,255,0.7);
}
.cv-ai-text{
    font-family:'Inter',sans-serif;font-size:13.5px;
    color:rgba(210,195,255,0.9);line-height:1.68;white-space:pre-wrap;
}
.cv-reasoning{
    background:rgba(139,92,246,0.06);border-radius:8px;
    padding:6px 10px;margin-bottom:8px;
    font-family:'Share Tech Mono',monospace;font-size:11px;
    color:rgba(155,125,220,0.65);
}

/* ── Quick start buttons ── */
div[data-testid="stButton"] button[kind="secondary"]{
    background:rgba(12,6,36,0.9)!important;
    border:1px solid rgba(100,60,200,0.25)!important;
    border-radius:10px!important;
    font-family:'Inter',sans-serif!important;font-size:11px!important;
    font-weight:600!important;letter-spacing:0.3px!important;
    color:rgba(160,135,255,0.75)!important;
    padding:6px 4px!important;line-height:1.3!important;
    transition:all 0.15s!important;white-space:nowrap!important;
    overflow:hidden!important;text-overflow:ellipsis!important;
}
div[data-testid="stButton"] button[kind="secondary"]:hover{
    background:rgba(139,92,246,0.18)!important;
    border-color:rgba(139,92,246,0.5)!important;
    color:rgba(220,200,255,0.98)!important;
    box-shadow:0 0 10px rgba(139,92,246,0.18)!important;
}
/* Checkbox label inline */
div[data-testid="stCheckbox"] label{
    font-family:'Inter',sans-serif!important;font-size:12.5px!important;
    color:rgba(170,145,255,0.75)!important;white-space:nowrap!important;
}

/* ── Input area ── */
div[data-testid="stTextInput"] input{
    background:rgba(10,5,30,0.92)!important;
    border:1px solid rgba(100,60,200,0.3)!important;border-radius:22px!important;
    color:rgba(220,205,255,0.92)!important;
    font-family:'Inter',sans-serif!important;font-size:14px!important;
    padding:10px 18px!important;
    transition:border-color 0.2s,box-shadow 0.2s!important;
}
div[data-testid="stTextInput"] input:focus{
    border-color:rgba(139,92,246,0.68)!important;
    box-shadow:0 0 18px rgba(139,92,246,0.14)!important;outline:none!important;
}
div[data-testid="stTextInput"] input::placeholder{color:rgba(130,100,200,0.38)!important;}

/* Thin chat scrollbar */
div[data-testid="stVerticalBlockBorderWrapper"]{
    scrollbar-width:thin!important;
    scrollbar-color:rgba(139,92,246,0.28) rgba(8,4,20,0.5)!important;
}

.cv-lbl{font-family:'Orbitron',monospace;font-size:0.53em;font-weight:700;
        letter-spacing:3px;color:rgba(139,92,246,0.5);display:block;margin:10px 0 5px;}
</style>""", unsafe_allow_html=True)

# ── Three.js compact hero ──────────────────────────────────────────────────────
_HERO = f"""
<div style="position:relative;border-radius:18px;overflow:hidden;height:110px;
            background:linear-gradient(135deg,#020817,#0d0528 55%,#040d1a);
            box-shadow:0 0 48px rgba(139,92,246,0.12),inset 0 1px 0 rgba(255,255,255,0.03);
            margin-bottom:8px;">
  <canvas id="molhero" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(2,8,23,0.7),transparent 18%,transparent 82%,rgba(2,8,23,0.7));pointer-events:none;z-index:1;"></div>
  <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
              flex-direction:column;z-index:2;pointer-events:none;gap:3px;">
    <div style="font-family:'Orbitron',monospace;font-size:1.7em;font-weight:900;letter-spacing:8px;
         background:linear-gradient(135deg,#c084fc,#a855f7 38%,#22d3ee 72%,#06b6d4);
         -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
         CHEM AGENT</div>
    <div style="font-family:'Inter',sans-serif;color:rgba(180,160,255,0.35);letter-spacing:3px;font-size:10px;font-weight:500;">
         AI · CHEMISTRY · EXPERT · SYSTEM</div>
    <div style="display:flex;gap:6px;margin-top:4px;">
      <span style="background:rgba(34,211,238,0.08);border:1px solid rgba(34,211,238,0.22);border-radius:20px;
                   padding:2px 9px;font-family:'Share Tech Mono',monospace;font-size:9px;color:rgba(34,211,238,0.7);"> 3D MAPS</span>
      <span style="background:rgba(139,92,246,0.08);border:1px solid rgba(139,92,246,0.22);border-radius:20px;
                   padding:2px 9px;font-family:'Share Tech Mono',monospace;font-size:9px;color:rgba(192,132,252,0.7);"> QUIZ</span>
      <span style="background:rgba(255,0,255,0.06);border:1px solid rgba(255,0,255,0.18);border-radius:20px;
                   padding:2px 9px;font-family:'Share Tech Mono',monospace;font-size:9px;color:rgba(255,100,255,0.65);"> REACTIONS</span>
      <span style="background:rgba(0,255,180,0.05);border:1px solid rgba(0,255,180,0.18);border-radius:20px;
                   padding:2px 9px;font-family:'Share Tech Mono',monospace;font-size:9px;color:rgba(0,255,180,0.62);"> AI</span>
    </div>
  </div>
  <script src="{_THREE}"></script>
  <script>
  (function(){{
    function go(){{
      if(!window.THREE){{setTimeout(go,60);return;}}
      var c=document.getElementById("molhero");
      var W=c.offsetWidth||900,H=110;
      var rr=new THREE.WebGLRenderer({{canvas:c,antialias:true,alpha:true}});
      rr.setSize(W,H);
      var sc=new THREE.Scene(),cam=new THREE.PerspectiveCamera(60,W/H,0.1,100);
      cam.position.set(0,0,9);
      sc.add(new THREE.AmbientLight(0xffffff,0.08));
      var l1=new THREE.PointLight(0x8B5CF6,5,30); l1.position.set(-9,5,5); sc.add(l1);
      var l2=new THREE.PointLight(0x22d3ee,5,30); l2.position.set(9,-5,-4); sc.add(l2);
      var l3=new THREE.PointLight(0xFF00FF,3,22); l3.position.set(0,9,2); sc.add(l3);
      var cMesh=new THREE.Mesh(
        new THREE.SphereGeometry(0.68,40,40),
        new THREE.MeshPhongMaterial({{color:0xFFD700,emissive:0xFFD700,emissiveIntensity:0.55,shininess:200}})
      ); sc.add(cMesh);
      sc.add(new THREE.Mesh(new THREE.TorusGeometry(1.05,0.03,16,64),
        new THREE.MeshBasicMaterial({{color:0xFFD700,transparent:true,opacity:0.18}})));
      [{{rad:2.2,rx:0,ry:0,rz:0,col:0x22d3ee}},
       {{rad:2.5,rx:1.047,ry:0.2,rz:0,col:0x8B5CF6}},
       {{rad:2.0,rx:0,ry:0.785,rz:0.524,col:0xFF00FF}}
      ].forEach(function(d){{
        var t=new THREE.Mesh(new THREE.TorusGeometry(d.rad,0.02,12,80),
          new THREE.MeshBasicMaterial({{color:d.col,transparent:true,opacity:0.2}}));
        t.rotation.set(d.rx,d.ry,d.rz); sc.add(t);
      }});
      var eData=[
        {{r:2.2,a:0,     s:0.008,yamp:0,  col:0x22d3ee,sz:0.21}},
        {{r:2.2,a:2.094, s:0.008,yamp:0,  col:0x22d3ee,sz:0.21}},
        {{r:2.2,a:4.189, s:0.008,yamp:0,  col:0x22d3ee,sz:0.21}},
        {{r:2.5,a:0,     s:0.006,yamp:1.9,col:0x8B5CF6,sz:0.17}},
        {{r:2.5,a:3.14,  s:0.006,yamp:1.9,col:0x8B5CF6,sz:0.17}},
        {{r:2.0,a:1.57,  s:0.007,yamp:0.8,col:0xFF00FF,sz:0.15}}
      ];
      var eMeshes=eData.map(function(d){{
        var m=new THREE.Mesh(new THREE.SphereGeometry(d.sz,18,18),
          new THREE.MeshPhongMaterial({{color:d.col,emissive:d.col,emissiveIntensity:0.5,shininess:120}}));
        m.userData=d; sc.add(m); return m;
      }});
      var pts=[];
      for(var i=0;i<260;i++) pts.push((Math.random()-0.5)*40,(Math.random()-0.5)*12,(Math.random()-0.5)*12);
      var ppg=new THREE.BufferGeometry();
      ppg.setAttribute("position",new THREE.Float32BufferAttribute(pts,3));
      sc.add(new THREE.Points(ppg,new THREE.PointsMaterial({{color:0xa855f7,size:0.055,transparent:true,opacity:0.4}})));
      var fr=0;
      (function anim(){{
        requestAnimationFrame(anim); fr++;
        eMeshes.forEach(function(m){{
          var d=m.userData; d.a+=d.s;
          m.position.x=d.r*Math.cos(d.a); m.position.z=d.r*Math.sin(d.a);
          m.position.y=d.yamp*Math.sin(d.a);
          m.material.emissiveIntensity=0.38+0.22*Math.sin(fr*0.09+d.a*2);
        }});
        cMesh.rotation.y+=0.008; cMesh.rotation.x+=0.003;
        l1.intensity=4+Math.sin(fr*0.055)*1.5;
        cam.position.x=Math.sin(fr*0.0017)*1.8; cam.lookAt(0,0,0);
        rr.render(sc,cam);
      }})();
    }}
    go();
  }})();
  </script>
</div>"""

# ── Helper functions ───────────────────────────────────────────────────────────
def _detect_intent(q):
    ql = q.lower()
    if any(w in ql for w in ["quiz","mcq","test me","practice question","give question","exam question"]):
        return "quiz"
    if any(w in ql for w in ["explain","what is","define","how does","describe","tell me","mechanism","why is","theory","concept"]):
        return "explain"
    return "general"

def _extract_concepts(text, topic):
    seen, nodes = set(), []
    for m in re.finditer(r'\b([A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)+)\b', text):
        t = m.group(1)
        if t not in seen and len(nodes) < 8:
            seen.add(t); nodes.append({"label": t, "color": _PAL[len(nodes) % 8]})
    for m in re.finditer(r'(?<=[a-z,;] )([A-Z][a-z]{3,}(?:\s[A-Z][a-z]+)?)\b', text):
        t = m.group(1)
        if t not in seen and t.lower() not in topic.lower() and len(nodes) < 8:
            seen.add(t); nodes.append({"label": t, "color": _PAL[len(nodes) % 8]})
    if len(nodes) < 3:
        for w in re.split(r'[\s,;:\n]+', text):
            if w and w[0].isupper() and 4 < len(w) < 20 and w not in seen and len(nodes) < 8:
                seen.add(w); nodes.append({"label": w, "color": _PAL[len(nodes) % 8]})
    return nodes

def _concept_map_3d(topic, nodes, h=440):
    uid = abs(hash(topic + str(len(nodes)))) % 99997
    njs = _json.dumps(nodes)
    tc  = topic[:24].replace('"','').replace("'","").replace('\\','')
    return f"""
<div style="width:100%;height:{h}px;border-radius:16px;overflow:hidden;
            background:linear-gradient(135deg,#030912,#080420,#030b12);
            border:1px solid rgba(139,92,246,0.22);">
  <canvas id="cm{uid}" style="width:100%;height:{h}px;display:block;"></canvas>
  <script src="{_THREE}"></script>
  <script>
  (function(){{
    var _nodes={njs}, _topic="{tc}";
    function go(){{
      if(!window.THREE){{setTimeout(go,60);return;}}
      var c=document.getElementById("cm{uid}");
      var W=c.offsetWidth||720, H={h};
      var rr=new THREE.WebGLRenderer({{canvas:c,antialias:true,alpha:true}});
      rr.setSize(W,H); rr.setPixelRatio(Math.min(devicePixelRatio,2));
      var sc=new THREE.Scene(), cam=new THREE.PerspectiveCamera(56,W/H,0.1,100);
      sc.add(new THREE.AmbientLight(0xffffff,0.18));
      var l1=new THREE.PointLight(0x8B5CF6,3.5,30); l1.position.set(-8,8,8); sc.add(l1);
      var l2=new THREE.PointLight(0x22d3ee,3.5,30); l2.position.set(8,-6,-8); sc.add(l2);
      var l3=new THREE.PointLight(0xFF00FF,2.2,24); l3.position.set(0,10,3); sc.add(l3);
      function mkLabel(txt,col){{
        var cv=document.createElement("canvas"); cv.width=340; cv.height=76;
        var cx=cv.getContext("2d");
        cx.clearRect(0,0,340,76);
        cx.fillStyle="rgba(4,6,20,0.9)"; cx.beginPath(); cx.roundRect(4,4,332,68,8); cx.fill();
        cx.strokeStyle=col; cx.lineWidth=2.2; cx.beginPath(); cx.roundRect(4,4,332,68,8); cx.stroke();
        cx.shadowColor=col; cx.shadowBlur=12; cx.font="bold 18px Orbitron,monospace";
        cx.textAlign="center"; cx.textBaseline="middle";
        cx.fillStyle=col; cx.fillText(txt.substring(0,17),170,38);
        var sp=new THREE.Sprite(new THREE.SpriteMaterial({{map:new THREE.CanvasTexture(cv),transparent:true,depthTest:false}}));
        sp.scale.set(4.2,1.0,1); return sp;
      }}
      var N=_nodes.length, rad=N>5?5.4:4.4;
      sc.add(new THREE.Mesh(new THREE.TorusGeometry(rad,0.022,8,96),
        new THREE.MeshBasicMaterial({{color:0x1e0f48,transparent:true,opacity:0.55}})));
      var cMat=new THREE.MeshPhongMaterial({{color:0xFFD700,emissive:0xFFD700,emissiveIntensity:0.55,shininess:160}});
      var cSph=new THREE.Mesh(new THREE.SphereGeometry(0.82,40,40),cMat); sc.add(cSph);
      var cLbl=mkLabel(_topic,"#FFD700"); cLbl.position.set(0,1.55,0); sc.add(cLbl);
      sc.add(new THREE.Mesh(new THREE.TorusGeometry(1.22,0.04,16,64),
        new THREE.MeshBasicMaterial({{color:0xFFD700,transparent:true,opacity:0.28}})));
      sc.add(new THREE.Mesh(new THREE.SphereGeometry(1.1,20,20),
        new THREE.MeshBasicMaterial({{color:0xFFD700,transparent:true,opacity:0.06,side:THREE.BackSide}})));
      var nObjs=[];
      _nodes.forEach(function(nd,i){{
        var ang=(i/N)*Math.PI*2, x=rad*Math.cos(ang), z=rad*Math.sin(ang), y=(i%3-1)*1.1;
        var col=parseInt(nd.color.replace('#',''),16);
        var mat=new THREE.MeshPhongMaterial({{color:col,emissive:col,emissiveIntensity:0.42,shininess:90}});
        var sph=new THREE.Mesh(new THREE.SphereGeometry(0.46,30,30),mat);
        sph.position.set(x,y,z); sc.add(sph); nObjs.push(sph);
        sc.add(new THREE.Mesh(new THREE.SphereGeometry(0.65,20,20),
          new THREE.MeshBasicMaterial({{color:col,transparent:true,opacity:0.1,side:THREE.BackSide}}))).position.set(x,y,z);
        var lbl=mkLabel(nd.label,nd.color); lbl.position.set(x,y+1.12,z); sc.add(lbl);
        sc.add(new THREE.Line(
          new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0,0,0),new THREE.Vector3(x,y,z)]),
          new THREE.LineBasicMaterial({{color:col,transparent:true,opacity:0.35}})
        ));
      }});
      var grid=new THREE.GridHelper(16,16,0x0d0830,0x0d0830); grid.position.y=-3.8; sc.add(grid);
      var pv=[];
      for(var i=0;i<120;i++) pv.push((Math.random()-0.5)*20,(Math.random()-0.5)*14,(Math.random()-0.5)*20);
      var ppg2=new THREE.BufferGeometry();
      ppg2.setAttribute("position",new THREE.Float32BufferAttribute(pv,3));
      sc.add(new THREE.Points(ppg2,new THREE.PointsMaterial({{color:0x8B5CF6,size:0.065,transparent:true,opacity:0.4}})));
      var th=0,fr=0;
      (function anim(){{
        requestAnimationFrame(anim); th+=0.005; fr++;
        cam.position.set(16*Math.sin(th),5*Math.sin(th*0.31)+1.2,16*Math.cos(th)); cam.lookAt(0,0,0);
        nObjs.forEach(function(n,i){{
          var s=1+0.13*Math.sin(fr*0.05+i*0.88); n.scale.set(s,s,s);
          n.material.emissiveIntensity=0.32+0.22*Math.sin(fr*0.06+i);
        }});
        cMat.emissiveIntensity=0.42+0.16*Math.sin(fr*0.04);
        cSph.rotation.y+=0.013; l1.intensity=2.8+Math.sin(fr*0.07)*0.9;
        rr.render(sc,cam);
      }})();
    }}
    go();
  }})();
  </script>
</div>"""

def _extract_reactions(text):
    rxns = []
    for line in text.split('\n'):
        if any(s in line for s in ['→','⇌','->']):
            c = line.strip().lstrip('•*-– ')
            if 5 < len(c) < 200: rxns.append(c)
    return rxns[:4]

def _reaction_cards_html(rxns):
    if not rxns: return ""
    rows = "".join(
        f'<div style="font-family:\'Share Tech Mono\',monospace;font-size:13px;color:#00FFB4;'
        f'padding:8px 13px;margin:4px 0;border-left:3px solid #00FFB4;'
        f'background:rgba(0,255,180,0.05);border-radius:0 9px 9px 0;">'
        f'{r.replace("<","&lt;").replace(">","&gt;")}</div>' for r in rxns)
    return ('<div style="background:rgba(0,255,180,0.03);border:1px solid rgba(0,255,180,0.15);'
            'border-radius:12px;padding:14px;margin:8px 0;">'
            '<div style="font-family:\'Orbitron\',monospace;font-size:0.58em;color:rgba(0,255,180,0.68);'
            'letter-spacing:3px;margin-bottom:10px;"> EXAMPLE REACTIONS</div>'
            + rows + '</div>')

def _quiz_cards_html(text):
    blocks = re.split(r'\n(?=\s*\d+[\.\)]|\s*Q\d+)', '\n' + text.strip())
    cards  = [b.strip() for b in blocks if b.strip() and len(b.strip()) > 25
              and re.search(r'(?:^|\n)\s*[A-Da-d][)\.]', b)]
    if not cards: return ""
    items = "".join(
        f'<div style="background:rgba(139,92,246,0.07);border:1px solid rgba(139,92,246,0.22);'
        f'border-radius:10px;padding:12px;margin:8px 0;">'
        f'<div style="font-family:\'Share Tech Mono\',monospace;font-size:12.5px;'
        f'color:rgba(210,190,255,0.9);white-space:pre-wrap;">'
        f'{c.replace("<","&lt;").replace(">","&gt;")}</div></div>' for c in cards[:5])
    return ('<div style="margin:8px 0;">'
            '<div style="font-family:\'Orbitron\',monospace;font-size:0.6em;color:rgba(139,92,246,0.8);'
            'letter-spacing:3px;margin-bottom:8px;"> QUIZ QUESTIONS</div>' + items + '</div>')

def _definition_html(text):
    for sent in re.split(r'(?<=[.!?])\s+', text):
        sent = sent.strip()
        if len(sent) > 30:
            return ('<div style="background:rgba(255,215,0,0.04);border:1px solid rgba(255,215,0,0.16);'
                    'border-radius:12px;padding:13px;margin:8px 0;">'
                    '<div style="font-family:\'Orbitron\',monospace;font-size:0.58em;'
                    'color:rgba(255,215,0,0.62);letter-spacing:3px;margin-bottom:8px;"> KEY DEFINITION</div>'
                    f'<div style="font-family:\'Share Tech Mono\',monospace;font-size:12.5px;'
                    f'color:rgba(210,200,180,0.85);line-height:1.7;">'
                    f'{sent.replace("<","&lt;").replace(">","&gt;")}</div></div>')
    return ""

# ── Session state ──────────────────────────────────────────────────────────────
for _k, _v in [("chat_history",[]), ("reasoning_history",[]), ("tutor_mode","General Chemistry Q&A")]:
    st.session_state.setdefault(_k, _v)

# ══════════════════════════════════════════════════════════════════════════════
# TOP BAR — full width
# ══════════════════════════════════════════════════════════════════════════════
n_msgs_top = len([m for m in st.session_state.chat_history if m["role"] == "user"])
st.markdown(f"""
<div class="cv-topbar">
  <div style="display:flex;align-items:center;gap:10px;">
    <div style="width:32px;height:32px;border-radius:50%;flex-shrink:0;
                background:linear-gradient(135deg,#7c3aed,#0ea5e9);
                display:flex;align-items:center;justify-content:center;
                font-size:17px;box-shadow:0 0 14px rgba(139,92,246,0.55);"></div>
    <span class="cv-topbar-title">CHEM AGENT CHAT</span>
  </div>
  <div class="cv-topbar-right">
    <div class="cv-search-box"> &nbsp;<span>Search chemistry topics…</span></div>
    <div class="cv-user-avatar"></div>
  </div>
</div>""", unsafe_allow_html=True)

# THREE.JS HERO
components.html(_HERO, height=118)

# ══════════════════════════════════════════════════════════════════════════════
# CONTROL ROW — selectbox mode + model + options + creativity
# ══════════════════════════════════════════════════════════════════════════════
c_mode, c_model, c_r, c_m, c_temp = st.columns([2.2, 2.0, 0.65, 0.65, 1.5], gap="small")

_MODE_OPTIONS = [
    "  General Chemistry Q&A",
    "  Equation Balancer",
    "  Reaction Predictor",
    "  Problem Solver",
    "  Mechanism Explainer",
    "  Quiz Generator",
    "  Lab Safety Advisor",
    "  Spectroscopy Helper",
]

with c_mode:
    st.markdown('<span class="cv-lbl"> SUBJECT</span>', unsafe_allow_html=True)
    mode = st.selectbox("Mode", _MODE_OPTIONS, label_visibility="collapsed")
    mode_clean = mode.split("  ", 1)[1] if "  " in mode else mode.strip()
    st.session_state.tutor_mode = mode_clean

with c_model:
    st.markdown('<span class="cv-lbl"> MODEL</span>', unsafe_allow_html=True)
    selected_model = st.selectbox("Model", list(MODELS.keys()),
                                  index=list(MODELS.keys()).index(
                                      st.session_state.get("SELECTED_MODEL", list(MODELS.keys())[0])),
                                  label_visibility="collapsed")
    st.session_state["SELECTED_MODEL"] = selected_model

with c_r:
    st.markdown('<span class="cv-lbl"></span>', unsafe_allow_html=True)
    show_reasoning = st.checkbox("Reasoning", value=True, label_visibility="collapsed",
                                 help="Show AI chain-of-thought reasoning")
    st.markdown('<div style="margin-top:4px;font-family:\'Share Tech Mono\',monospace;'
                'font-size:10px;color:rgba(139,92,246,0.5);text-align:center;">REASON</div>',
                unsafe_allow_html=True)

with c_m:
    st.markdown('<span class="cv-lbl"></span>', unsafe_allow_html=True)
    show_map = st.checkbox("Map", value=True, label_visibility="collapsed",
                           help="Show 3D concept map after AI response")
    st.markdown('<div style="margin-top:4px;font-family:\'Share Tech Mono\',monospace;'
                'font-size:10px;color:rgba(139,92,246,0.5);text-align:center;">3D MAP</div>',
                unsafe_allow_html=True)

with c_temp:
    st.markdown('<span class="cv-lbl"> CREATIVITY</span>', unsafe_allow_html=True)
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7, 0.05, label_visibility="collapsed")

# ══════════════════════════════════════════════════════════════════════════════
# QUICK START — 8 compact buttons, short labels, no wrapping
# ══════════════════════════════════════════════════════════════════════════════
QUICK_PROMPTS = {
    " Balance":   "Balance this equation step by step: H₂ + O₂ → H₂O",
    " Hybrid":    "Explain sp, sp², and sp³ hybridization with examples",
    " Acid-Base": "Explain Arrhenius, Brønsted-Lowry, and Lewis acid-base theories",
    " Le Chat":   "Explain Le Chatelier's principle with 3 practical examples",
    " IUPAC":     "Teach me IUPAC nomenclature for organic compounds",
    " Trends":    "Explain periodic trends: atomic radius, IE, electronegativity",
    " Gibbs ΔG":  "Explain Gibbs free energy and spontaneous reactions",
    " Org Quiz":  "Give me 5 MCQ quiz questions on organic chemistry with answers",
}
st.markdown('<span class="cv-lbl"> QUICK START</span>', unsafe_allow_html=True)
qs_cols = st.columns(len(QUICK_PROMPTS))
for i, (label, prompt) in enumerate(QUICK_PROMPTS.items()):
    with qs_cols[i]:
        if st.button(label, key=f"qp_{label}", use_container_width=True):
            st.session_state["pending_prompt"] = prompt

st.markdown('<div class="cv-div"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CHAT PANEL — full width, maximum space
# ══════════════════════════════════════════════════════════════════════════════
MODE_CONTEXTS = {
    "Equation Balancer":     "\n\nBalance chemical equations step-by-step using algebraic/matrix method.",
    "Reaction Predictor":    "\n\nPredict reaction products and types (synthesis, decomposition, redox, etc.).",
    "Problem Solver":        "\n\nSolve stoichiometry/thermodynamics/kinetics problems step-by-step with units.",
    "Mechanism Explainer":   "\n\nExplain organic reaction mechanisms with electron movement and intermediates.",
    "Quiz Generator":        "\n\nGenerate 5 numbered MCQ questions with A) B) C) D) and Answer: X) explanation.",
    "Lab Safety Advisor":    "\n\nFocus on lab safety, MSDS, PPE requirements, and emergency procedures.",
    "Spectroscopy Helper":   "\n\nInterpret IR/NMR/MS/UV-Vis spectra: peaks, functional groups, structural fragments.",
    "General Chemistry Q&A": "",
}
CHEM_AGENT_SYS = (
    "You are CHEM AGENT, an advanced AI chemistry expert. "
    "For explanations: (1) clear definition, (2) theory/mechanism, "
    "(3) 2-4 example reactions using → symbol, (4) list key related concepts. "
    "For quizzes: number questions 1. 2. 3., give A) B) C) D) options, "
    "then Answer: X) with explanation. Be thorough yet concise."
)

model_short = (selected_model.split("/")[-1][:20] if "/" in selected_model else selected_model[:20])
n_msgs      = len([m for m in st.session_state.chat_history if m["role"] == "user"])

# Sub-header
st.markdown(f"""
<div class="cv-chat-subhdr">
  <div class="cv-ai-ava"></div>
  <div style="flex:1;min-width:0;">
    <div style="font-family:'Orbitron',monospace;font-size:0.78em;font-weight:900;
                letter-spacing:2px;color:rgba(225,205,255,0.95);">CHEM AGENT AI</div>
    <div style="font-family:'Inter',sans-serif;font-size:11.5px;
                color:rgba(139,92,246,0.55);margin-top:1px;">{mode_clean}</div>
  </div>
  <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
    <span><span class="cv-dot"></span>
          <span style="font-family:'Share Tech Mono',monospace;font-size:10px;
                       color:rgba(0,255,180,0.7);">ONLINE</span></span>
    <span class="cv-chip cv-c2"> {model_short}</span>
    <span class="cv-chip cv-c3"> {n_msgs} msg{'s' if n_msgs!=1 else ''}</span>
  </div>
</div>""", unsafe_allow_html=True)

# ── Scrollable chat — full width, tall ────────────────────────────────────────
with st.container(height=540, border=False):
    if not st.session_state.chat_history:
        st.markdown("""
        <div style="display:flex;flex-direction:column;align-items:center;
                    justify-content:center;height:460px;text-align:center;padding:30px;">
          <div style="width:70px;height:70px;border-radius:50%;margin:0 auto 18px;
                      background:linear-gradient(135deg,#7c3aed,#0ea5e9);
                      display:flex;align-items:center;justify-content:center;
                      font-size:32px;box-shadow:0 0 28px rgba(139,92,246,0.45);"></div>
          <div style="font-family:'Orbitron',monospace;font-size:1em;font-weight:900;
                      letter-spacing:3px;color:rgba(220,200,255,0.75);margin-bottom:8px;">
               CHEM AGENT AI</div>
          <div style="font-family:'Inter',sans-serif;font-size:13px;
                      color:rgba(139,92,246,0.5);margin-bottom:20px;letter-spacing:0.5px;">
               Your personal AI chemistry tutor — full-width, maximum space</div>
          <div style="width:44px;height:1px;
                      background:linear-gradient(90deg,transparent,rgba(139,92,246,0.4),transparent);
                      margin:0 auto 20px;"></div>
          <div style="font-family:'Inter',sans-serif;font-size:13.5px;
                      color:rgba(140,115,210,0.38);line-height:2.0;max-width:480px;">
            Ask for an <b style="color:rgba(0,255,180,0.52);">explanation</b>
              → 3D concept map + reactions<br>
            Ask for <b style="color:rgba(139,92,246,0.62);">quiz questions</b>
              → interactive MCQ cards<br>
            Pick a <b style="color:rgba(34,211,238,0.48);">subject</b>
              from the pills above to begin
          </div>
        </div>""", unsafe_allow_html=True)
    else:
        for i, msg in enumerate(st.session_state.chat_history):
            if msg["role"] == "user":
                esc = msg["content"].replace("<","&lt;").replace(">","&gt;")
                st.markdown(f"""
                <div class="cv-user-wrap">
                  <div class="cv-user-bubble">
                    <span class="cv-user-label">YOU</span>
                    <div class="cv-user-text">{esc}</div>
                  </div>
                </div>""", unsafe_allow_html=True)

            elif msg["role"] == "assistant":
                esc = msg["content"].replace("<","&lt;").replace(">","&gt;")
                rd_html = ""
                if show_reasoning and (i // 2) < len(st.session_state.reasoning_history):
                    r_data = st.session_state.reasoning_history[i // 2]
                    if r_data:
                        snip = str(r_data)[:440] + ("…" if len(str(r_data)) > 440 else "")
                        rd_html = f'<div class="cv-reasoning"> {snip}</div>'
                model_tag = (selected_model.split('/')[0]
                             if '/' in selected_model else selected_model[:16])
                st.markdown(f"""
                <div class="cv-ai-wrap">
                  <div class="cv-ai-card">
                    <div class="cv-ai-card-hdr">
                      <div class="cv-ai-card-ava"></div>
                      <span class="cv-ai-card-name">CHEM AGENT · {model_tag}</span>
                    </div>
                    {rd_html}
                    <div class="cv-ai-text">{esc}</div>
                  </div>
                </div>""", unsafe_allow_html=True)

# ── Post-response tabs ────────────────────────────────────────────────────────
_last_ai  = next((m["content"] for m in reversed(st.session_state.chat_history)
                  if m["role"] == "assistant"), "")
_last_usr = next((m["content"] for m in reversed(st.session_state.chat_history)
                  if m["role"] == "user"), "")

if _last_ai and show_map:
    intent   = _detect_intent(_last_usr)
    concepts = _extract_concepts(_last_ai, _last_usr)
    rxns     = _extract_reactions(_last_ai)
    st.markdown('<div class="cv-div" style="margin:12px 0;"></div>', unsafe_allow_html=True)
    tab_map, tab_info = st.tabs(["3D Concept Map", "Reactions & Cards"])
    with tab_map:
        if concepts:
            components.html(_concept_map_3d(_last_usr[:28] or "Chemistry", concepts, h=440), height=448)
        else:
            st.info("No distinct chemistry concepts found — try a more specific question.")
    with tab_info:
        if rxns:
            st.markdown(_reaction_cards_html(rxns), unsafe_allow_html=True)
        if intent == "quiz" or mode_clean == "Quiz Generator":
            qc = _quiz_cards_html(_last_ai)
            if qc: st.markdown(qc, unsafe_allow_html=True)
        st.markdown(_definition_html(_last_ai), unsafe_allow_html=True)

# ── Reasoning expander ────────────────────────────────────────────────────────
if show_reasoning and st.session_state.reasoning_history:
    latest_rd = st.session_state.reasoning_history[-1]
    if latest_rd:
        with st.expander("Latest AI Reasoning Chain", expanded=False):
            body = (
                "\n".join(
                    str(s.get("thinking", s.get("content", str(s)))
                        if isinstance(s, dict) else str(s))[:1500]
                    for s in latest_rd)
                if isinstance(latest_rd, list)
                else str(latest_rd)[:1500]
            )
            st.markdown(
                f'<div style="background:rgba(139,92,246,0.05);border-radius:8px;'
                f'padding:9px 12px;font-family:\'Share Tech Mono\',monospace;'
                f'font-size:11px;color:rgba(175,150,255,0.7);">{body}</div>',
                unsafe_allow_html=True)

# ── Input bar ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cv-div" style="margin:14px 0 5px;"></div>
<div style="font-family:'Orbitron',monospace;font-size:0.5em;letter-spacing:3px;
            color:rgba(139,92,246,0.42);margin-bottom:5px;"> TYPE YOUR QUESTION</div>""",
            unsafe_allow_html=True)

pending = st.session_state.pop("pending_prompt", None)
inp_c, clr_c, snd_c = st.columns([8, 1.25, 1.25])
with inp_c:
    user_input = st.text_input("Message", value=pending or "",
                               placeholder=f"Ask about {mode_clean.lower()}…",
                               label_visibility="collapsed", key="chat_input")
with clr_c:
    if st.button("Clear", icon=":material/delete:", key="clr_btn", help="Clear conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.reasoning_history = []
        st.rerun()
with snd_c:
    send = st.button("Send", icon=":material/send:", key="send_btn", help="Send message", use_container_width=True)

# ── AI call ───────────────────────────────────────────────────────────────────
if (send or pending) and (user_input or pending):
    query  = user_input or pending
    intent = _detect_intent(query)
    extra  = MODE_CONTEXTS.get(mode_clean, "")
    if intent == "explain":
        extra += ("\n\nUser wants EXPLANATION: give definition, theory, 2-4 example reactions "
                  "using → symbol, and a list of key related concepts.")
    elif intent == "quiz":
        extra += ("\n\nUser wants a QUIZ: generate 5 numbered MCQ questions with "
                  "A) B) C) D) options. End each with 'Answer: X) explanation.'")

    system_prompt = CHEM_AGENT_SYS + "\n\n" + CHEM_SYSTEM_PROMPT + extra
    api_messages  = [{"role": "system", "content": system_prompt}]
    for m in st.session_state.chat_history:
        if m["role"] in ("user", "assistant"):
            api_messages.append({"role": m["role"], "content": m.get("content", "")})
    api_messages.append({"role": "user", "content": query})

    with st.spinner("Chem Agent thinking…"):
        content, reasoning_details, err = call_openrouter(
            api_messages, model_key=selected_model,
            reasoning=True, temperature=temperature, max_tokens=2048)

    if err:
        st.markdown(f'<div class="danger-box"> {err}</div>', unsafe_allow_html=True)
    else:
        st.session_state.chat_history.append({"role": "user", "content": query})
        st.session_state.chat_history.append({
            "role": "assistant", "content": content,
            "reasoning_details": reasoning_details})
        st.session_state.reasoning_history.append(reasoning_details)
        st.rerun()

# ── Quick Reference Cards ──────────────────────────────────────────────────────
st.markdown("""
<div style="height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,0.16),transparent);
            margin:26px 0 18px;"></div>
<div style="font-family:'Orbitron',monospace;font-size:0.68em;font-weight:700;
            letter-spacing:3px;color:rgba(185,158,255,0.58);margin-bottom:16px;">
      QUICK REFERENCE</div>""", unsafe_allow_html=True)

r1, r2, r3, r4 = st.columns(4)
_refs = [
    ("#22d3ee"," Common Acids",
     ["HCl — Hydrochloric acid","H₂SO₄ — Sulfuric acid","HNO₃ — Nitric acid",
      "H₃PO₄ — Phosphoric acid","CH₃COOH — Acetic acid"]),
    ("#8B5CF6"," Key Reactions",
     ["Acid + Base → Salt + H₂O","2H₂ + O₂ → 2H₂O",
      "N₂ + 3H₂ ⇌ 2NH₃ (Haber)","CaCO₃ → CaO + CO₂",
      "Zn + H₂SO₄ → ZnSO₄ + H₂"]),
    ("#FF00FF"," Constants",
     ["R = 8.314 J/mol·K","Nₐ = 6.022×10²³","F = 96485 C/mol",
      "kB = 1.38×10⁻²³ J/K","h = 6.626×10⁻³⁴ J·s"]),
    ("#FFD700"," Formulas",
     ["pH = -log[H⁺]","ΔG = ΔH - TΔS","PV = nRT",
      "E = E° - (RT/nF)lnQ","ln(k₂/k₁) = Eₐ/R·(1/T₁-1/T₂)"]),
]
for col, (color, title, items) in zip([r1,r2,r3,r4], _refs):
    with col:
        st.markdown(f"""
        <div style="background:rgba(8,4,24,0.8);border:1px solid rgba(255,255,255,0.05);
                    border-top:2.5px solid {color};border-radius:14px;padding:16px 14px;">
          <div style="font-family:'Orbitron',monospace;font-size:0.65em;font-weight:700;
                      color:{color};letter-spacing:2px;margin-bottom:12px;">{title}</div>
          <ul style="color:rgba(180,158,240,0.62);font-family:'Share Tech Mono',monospace;
                     font-size:11px;line-height:2.0;padding-left:14px;margin:0;">
            {"".join(f"<li>{it}</li>" for it in items)}
          </ul>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;font-family:'Share Tech Mono',monospace;
            font-size:10.5px;color:rgba(100,85,140,0.22);padding:20px 0 8px;">
     2026 Snehal Laxman Jadhav · AI Engineer · Navneet Education Limited · ChemVerse AI
</div>""", unsafe_allow_html=True)
