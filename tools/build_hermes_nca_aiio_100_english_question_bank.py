# -*- coding: utf-8 -*-
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "aiio/weekend/materials/data/hermes-nca-aiio-100-original-english-questions.json"
OUT = ROOT / "aiio/weekend/materials/hermes-nca-aiio-100-english-question-blueprint-mock.html"

SOURCES = {
    "S1": ("NVIDIA NCA-AIIO Certification and Exam Blueprint", "https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/"),
    "S2": ("NVIDIA NCA-AIIO Exam Study Guide", "https://dam-cdn.nvd.orangelogic.com/AssetLink/x874j05hy3m3r2sor84kpvp70750m468.pdf"),
    "S3": ("NVIDIA TensorRT", "https://developer.nvidia.com/tensorrt"),
    "S4": ("NVIDIA TensorRT Documentation", "https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html"),
    "S5": ("NVIDIA GPU Operator Documentation", "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html"),
    "S6": ("NVIDIA: Scaling Storage for AI", "https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing/"),
    "S7": ("NVIDIA: Large Language Models", "https://blogs.nvidia.com/blog/what-are-large-language-models-used-for/"),
    "S8": ("IBM: Machine Learning", "https://www.ibm.com/think/topics/machine-learning"),
    "S9": ("SAS: Machine Learning", "https://www.sas.com/en_us/insights/analytics/machine-learning.html"),
    "S10": ("AWS: CPU vs. GPU", "https://aws.amazon.com/compare/the-difference-between-gpus-cpus/"),
    "S11": ("NVIDIA CUDA Documentation", "https://docs.nvidia.com/cuda/"),
    "S12": ("NVIDIA NCCL Documentation", "https://docs.nvidia.com/deeplearning/nccl/"),
    "S13": ("NVIDIA Triton Inference Server Documentation", "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/"),
    "S14": ("NVIDIA NGC Catalog", "https://catalog.ngc.nvidia.com/"),
    "S15": ("NVIDIA DCGM Documentation", "https://docs.nvidia.com/datacenter/dcgm/latest/"),
    "S16": ("NVIDIA MIG User Guide", "https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/"),
    "S17": ("NVIDIA Data Processing Unit", "https://www.nvidia.com/en-us/networking/products/data-processing-unit/"),
    "S18": ("NVIDIA AI Enterprise Documentation", "https://docs.nvidia.com/ai-enterprise/index.html#overview"),
    "S19": ("NVIDIA System Management Interface", "https://docs.nvidia.com/deploy/nvidia-smi/index.html"),
    "S20": ("Kubernetes: Assigning Pods to Nodes", "https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/"),
    "S21": ("Slurm Generic Resource Scheduling", "https://slurm.schedmd.com/gres.html"),
    "S22": ("NVIDIA GPU Operator: GPU Sharing", "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html"),
    "S23": ("NVIDIA DCGM Exporter", "https://docs.nvidia.com/datacenter/dcgm/latest/gpu-telemetry/dcgm-exporter.html"),
    "S24": ("NVIDIA DGX Platform", "https://www.nvidia.com/en-us/data-center/dgx-platform/"),
    "S25": ("NVIDIA Omniverse", "https://www.nvidia.com/en-us/omniverse/"),
    "S26": ("NVIDIA Jetson Embedded Systems", "https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/"),
    "S27": ("NVIDIA InfiniBand", "https://www.nvidia.com/en-us/networking/products/infiniband/"),
    "S28": ("NVIDIA DGX SuperPOD Network Fabrics", "https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-h100/latest/network-fabrics.html"),
    "S29": ("NVIDIA GPUDirect Storage Overview", "https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html"),
}
LABELS = {
    "essential": "Essential AI Knowledge",
    "infrastructure": "AI Infrastructure",
    "operations": "AI Operations",
}

questions = json.loads(DATA.read_text(encoding="utf-8"))
assert len(questions) == 100
assert [q["id"] for q in questions] == list(range(1, 101))
assert {d: sum(q["domain"] == d for q in questions) for d in LABELS} == {
    "essential": 38,
    "infrastructure": 40,
    "operations": 22,
}

cards = []
for q in questions:
    options = "".join(
        f'<label class="option"><input type="radio" name="q{q["id"]}" value="{i}"><span><b>{chr(65+i)}</b>{html.escape(choice)}</span></label>'
        for i, choice in enumerate(q["choices"])
    )
    citations = " ".join(f'<a href="#source-{key}">[{key}]</a>' for key in q["source_keys"])
    cards.append(
        f'''<article class="question-card" id="q-{q['id']}" data-id="{q['id']}" data-domain="{q['domain']}" data-answer="{q['answer']}">
<header><span>QUESTION {q['id']:03d}</span><b>{LABELS[q['domain']]} · Objective {html.escape(q['objective'])}</b></header>
<h2>{html.escape(q['question'])}</h2><div class="options">{options}</div>
<section class="explanation" hidden><p><strong>Correct answer: {chr(65+q['answer'])}</strong> — {html.escape(q['choices'][q['answer']])}</p><p>{html.escape(q['explanation'])}</p><p class="cite">Verification sources: {citations}</p></section></article>'''
    )

source_items = "".join(
    f'<li id="source-{key}"><a href="{url}" target="_blank" rel="noopener noreferrer"><b>[{key}]</b> {html.escape(name)}</a></li>'
    for key, (name, url) in SOURCES.items()
)

DOC = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="100 original English NCA-AIIO practice questions aligned to the official 38/40/22 blueprint."><title>NCA-AIIO English Practice Bank — 100 Original Questions</title><style>
:root{{--green:#76b900;--black:#050705;--paper:#f7f9f3;--ink:#171b16;--line:#dce2d5;--amber:#f0ad00;--red:#cf4949}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;overflow-x:hidden;background:var(--black);color:#fff;font:16px/1.65 Inter,Arial,sans-serif}}a{{color:inherit}}.top{{position:sticky;top:0;z-index:20;background:rgba(0,0,0,.96);border-bottom:1px solid #30372e}}.topin{{max-width:1240px;margin:auto;padding:12px 20px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}}.brand{{font-weight:900;text-decoration:none}}.brand i{{font-style:normal;color:var(--green)}}button{{border:2px solid var(--green);background:transparent;color:#fff;font-weight:800;padding:8px 12px;cursor:pointer}}button.primary{{background:var(--green);color:#000}}#timer{{margin-left:auto;font:900 1.5rem ui-monospace,monospace;color:var(--green)}}.hero{{max-width:1240px;margin:auto;padding:65px 20px 42px;display:grid;grid-template-columns:1.4fr .6fr;gap:44px}}.hero>*{{min-width:0}}.kicker{{font-size:.72rem;letter-spacing:.15em;color:var(--green);font-weight:900}}h1{{font-size:clamp(2.6rem,6vw,5.6rem);line-height:1.02;letter-spacing:-.055em;margin:.15em 0}}.lead{{color:#c7cdc3;font-size:1.08rem}}.notice{{border-left:4px solid var(--amber);background:#211a06;color:#f6dfa1;padding:14px 16px}}.stats{{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:#30372e;border:1px solid #30372e;align-self:end}}.stat{{background:#0d100d;padding:20px}}.stat b{{display:block;color:var(--green);font-size:2rem}}.toolbar{{position:sticky;top:67px;z-index:15;background:#0a0d0a;border-block:1px solid #30372e}}.toolbarin{{max-width:1240px;margin:auto;padding:12px 20px;display:flex;gap:8px;flex-wrap:wrap}}.toolbar button.active{{background:var(--green);color:#000}}main{{max-width:980px;margin:auto;padding:34px 20px 85px}}.question-card{{scroll-margin-top:140px;background:var(--paper);color:var(--ink);padding:28px;margin:0 0 22px;border-top:3px solid var(--green)}}.question-card>header{{display:flex;justify-content:space-between;gap:16px;border-bottom:1px solid var(--line);padding-bottom:10px;font-size:.72rem;letter-spacing:.07em}}.question-card>header b{{color:#527d00}}.question-card h2{{font-size:1.3rem;line-height:1.42}}.options{{display:grid;gap:9px}}.option{{display:block;cursor:pointer}}.option input{{position:absolute;opacity:0}}.option span{{display:flex;gap:12px;align-items:flex-start;background:#fff;border:1px solid var(--line);padding:12px 14px}}.option b{{display:grid;place-items:center;min-width:26px;height:26px;background:#e8eddf}}.option input:checked+span{{border:2px solid var(--green);padding:11px 13px;background:#f4fae9}}.question-card.correct{{border-color:var(--green)}}.question-card.wrong{{border-color:var(--red)}}.question-card.correct .option input:checked+span{{background:#e6f4cf}}.question-card.wrong .option input:checked+span{{background:#ffe5e5;border-color:var(--red)}}.explanation{{margin-top:16px;background:#101410;color:#fff;padding:16px;border-left:4px solid var(--green)}}.cite{{font-size:.78rem;color:#afb7aa}}.cite a{{color:var(--green);font-weight:800}}#result{{max-width:980px;margin:0 auto 20px;padding:0 20px}}.resultbox{{display:none;border:2px solid var(--green);padding:20px;background:#101410}}.resultbox.show{{display:block}}.resultbox b{{font-size:2rem;color:var(--green)}}.sources{{max-width:980px;margin:0 auto 80px;padding:0 20px}}.sourcebox{{border:1px solid #30372e;background:#0c0f0c;padding:28px}}.sourcebox a{{text-underline-offset:4px;text-decoration-color:var(--green)}}footer{{border-top:1px solid #2b302a;text-align:center;color:#7c8679;padding:25px}}[hidden]{{display:none!important}}@media(max-width:800px){{.hero{{grid-template-columns:1fr}}.topin{{display:grid;grid-template-columns:1fr auto;gap:9px}}.brand{{grid-column:1;grid-row:1;font-size:.8rem}}#timer{{grid-column:2;grid-row:1;margin:0;font-size:1.05rem}}.top button{{display:block!important;font-size:.72rem;padding:8px}}#timer-start{{grid-column:1;grid-row:2}}.top .primary{{grid-column:2;grid-row:2}}.question-card{{padding:20px 15px}}.question-card>header{{display:block}}}}@media print{{.top,.hero,.toolbar,#result,.sources,footer{{display:none!important}}body{{background:#fff}}main{{max-width:none;padding:0}}.question-card{{page-break-inside:avoid}}.explanation{{display:block!important;color:#000;background:#fff;border:1px solid #aaa}}}}
</style></head><body><header class="top"><div class="topin"><a class="brand" href="../"><i>HERMES</i> NCA-AIIO ENGLISH 100Q</a><button id="timer-start">Start 60-Minute Timer</button><button class="primary" id="score">Score Visible Questions</button><span id="timer">60:00</span></div></header>
<section class="hero"><div><div class="kicker">ORIGINAL ENGLISH PRACTICE · BLUEPRINT ALIGNED</div><h1>100 English<br>Practice Questions</h1><p class="lead">Practice certification-style English while reviewing the official NCA-AIIO blueprint: 38 Essential AI Knowledge questions, 40 AI Infrastructure questions, and 22 AI Operations questions.</p><p class="notice"><strong>Integrity notice:</strong> These are Original practice questions, not actual or recalled exam questions. This study resource does not guarantee a passing result. NVIDIA currently lists a $125 exam fee, 50 questions, and a 60-minute limit.</p></div><div class="stats"><div class="stat"><b>38</b>Essential</div><div class="stat"><b>40</b>Infrastructure</div><div class="stat"><b>22</b>Operations</div><div class="stat"><b>50 / 60</b>Questions / minutes</div></div></section>
<nav class="toolbar"><div class="toolbarin"><button class="active" data-filter="all">All 100 Questions</button><button data-filter="essential">Essential 38</button><button data-filter="infrastructure">Infrastructure 40</button><button data-filter="operations">Operations 22</button><button id="mock50">Random 50-Question Mock</button><button id="reset">Clear Answers</button><button onclick="window.print()">Print</button></div></nav><section id="result"><div class="resultbox" id="resultbox"><b id="resultscore">0 / 0</b><p id="resulttext"></p></div></section><main>{''.join(cards)}</main>
<section class="sources"><div class="sourcebox"><div class="kicker">VERIFICATION SOURCES</div><h2>References used to verify explanations</h2><ol>{source_items}</ol></div></section><footer>Hermes original English edition · Public blueprint-aligned practice · 2026</footer><script>
const cards=[...document.querySelectorAll('.question-card')],key='hermes-nca-aiio-english-100q-v1';let state=JSON.parse(localStorage.getItem(key)||'{{}}');function save(){{localStorage.setItem(key,JSON.stringify(state))}}cards.forEach(c=>{{let id=c.dataset.id;if(state[id]!==undefined){{let r=c.querySelector(`input[value="${{state[id]}}"]`);if(r)r.checked=true}}c.querySelectorAll('input').forEach(r=>r.addEventListener('change',()=>{{state[id]=+r.value;save()}}))}});function show(domain){{cards.forEach(c=>c.hidden=domain!=='all'&&c.dataset.domain!==domain)}}document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('[data-filter]').forEach(x=>x.classList.toggle('active',x===b));show(b.dataset.filter)}}));document.getElementById('mock50').addEventListener('click',()=>{{const take=(a,n)=>a.sort(()=>Math.random()-.5).slice(0,n),selected=new Set([...take(cards.filter(c=>c.dataset.domain==='essential'),19),...take(cards.filter(c=>c.dataset.domain==='infrastructure'),20),...take(cards.filter(c=>c.dataset.domain==='operations'),11)]);cards.forEach(c=>c.hidden=!selected.has(c));document.querySelectorAll('[data-filter]').forEach(x=>x.classList.remove('active'));window.scrollTo({{top:document.querySelector('.toolbar').offsetTop,behavior:'smooth'}})}});document.getElementById('score').addEventListener('click',()=>{{let visible=cards.filter(c=>!c.hidden),answered=0,correct=0;visible.forEach(c=>{{let checked=c.querySelector('input:checked'),ans=+c.dataset.answer;c.classList.remove('correct','wrong');if(checked){{answered++;if(+checked.value===ans){{correct++;c.classList.add('correct')}}else c.classList.add('wrong')}}c.querySelector('.explanation').hidden=false}});let pct=visible.length?Math.round(correct/visible.length*100):0,box=document.getElementById('resultbox');document.getElementById('resultscore').textContent=`${{correct}} / ${{visible.length}} (${{pct}}%)`;document.getElementById('resulttext').textContent=`Answered ${{answered}} question(s). Use missed questions to identify weak objectives.`;box.classList.add('show');box.scrollIntoView({{behavior:'smooth'}})}});document.getElementById('reset').addEventListener('click',()=>{{if(!confirm('Clear all saved answers and results?'))return;state={{}};save();cards.forEach(c=>{{c.hidden=false;c.classList.remove('correct','wrong');c.querySelectorAll('input').forEach(r=>r.checked=false);c.querySelector('.explanation').hidden=true}});document.getElementById('resultbox').classList.remove('show')}});let remaining=3600,tick;document.getElementById('timer-start').addEventListener('click',()=>{{if(tick)return;tick=setInterval(()=>{{remaining--;let m=String(Math.floor(remaining/60)).padStart(2,'0'),s=String(remaining%60).padStart(2,'0');document.getElementById('timer').textContent=`${{m}}:${{s}}`;if(remaining<=0){{clearInterval(tick);document.getElementById('score').click()}}}},1000)}});
</script></body></html>'''

OUT.write_text(DOC, encoding="utf-8")
print(f"wrote {OUT} questions={len(questions)}")
