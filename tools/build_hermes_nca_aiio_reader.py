from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "aiio/weekend/materials/hermes-nca-aiio-cert-pass-100-unit-reader.html"

SOURCES = {
"S1": ("NVIDIA NCA-AIIO Certification & Exam Blueprint", "https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/"),
"S2": ("NVIDIA NCA-AIIO Exam Study Guide (PDF)", "https://dam-cdn.nvd.orangelogic.com/AssetLink/x874j05hy3m3r2sor84kpvp70750m468.pdf"),
"S3": ("NVIDIA TensorRT", "https://developer.nvidia.com/tensorrt"),
"S4": ("NVIDIA TensorRT Documentation", "https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html"),
"S5": ("NVIDIA GPU Operator Documentation", "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html"),
"S6": ("NVIDIA: Scaling Storage for AI Training and Inferencing", "https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing/"),
"S7": ("NVIDIA: What Are Large Language Models Used For?", "https://blogs.nvidia.com/blog/what-are-large-language-models-used-for/"),
"S8": ("IBM: What Is Machine Learning?", "https://www.ibm.com/think/topics/machine-learning"),
"S9": ("SAS: Machine Learning", "https://www.sas.com/en_us/insights/analytics/machine-learning.html"),
"S10": ("AWS: What’s the Difference Between a CPU and a GPU?", "https://aws.amazon.com/compare/the-difference-between-gpus-cpus/"),
"S11": ("NVIDIA CUDA Documentation", "https://docs.nvidia.com/cuda/"),
"S12": ("NVIDIA NCCL Documentation", "https://docs.nvidia.com/deeplearning/nccl/"),
"S13": ("NVIDIA Triton Inference Server Documentation", "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/"),
"S14": ("NVIDIA NGC Catalog", "https://catalog.ngc.nvidia.com/"),
"S15": ("NVIDIA DCGM Documentation", "https://docs.nvidia.com/datacenter/dcgm/latest/"),
"S16": ("NVIDIA MIG User Guide", "https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/"),
"S17": ("NVIDIA Data Processing Unit", "https://www.nvidia.com/en-us/networking/products/data-processing-unit/"),
"S18": ("NVIDIA AI Enterprise Documentation", "https://docs.nvidia.com/ai-enterprise/index.html#overview"),
}

def parse(domain, raw):
    rows=[]
    for line in raw.strip().splitlines():
        if not line.strip():
            continue
        parts=[p.strip() for p in line.split("¦")]
        if len(parts)!=6: raise ValueError((domain,line,len(parts)))
        title, concept, clue, question, answer, src=parts
        rows.append(dict(domain=domain,title=title,concept=concept,clue=clue,question=question,answer=answer,sources=src.split(',')))
    return rows

ESSENTIAL = parse("essential", r'''
官方藍圖與得分策略¦NCA-AIIO 為入門級 AI 基礎設施與維運認證；官方藍圖分成 Essential AI Knowledge 38%、AI Infrastructure 40%、AI Operations 22%。¦準備時間也應依 38/40/22 分配，而不是只背 GPU 產品。¦若你只有 10 小時，哪一領域至少應分配約 4 小時？¦AI Infrastructure，因為官方權重最高為 40%。¦S1,S2
AI、ML、DL 的集合關係¦AI 是能運用資訊做決策或預測的總稱；ML 是從資料學模式的 AI 子集；DL 是以深層神經網路為核心的 ML 子集。¦看到「所有 ML 都是 AI」正確；反過來通常錯。¦規則式專家系統一定屬於 ML 嗎？¦不一定；它可能是 AI，但沒有從資料學習。¦S8,S9
監督式學習¦使用帶標籤資料學習輸入到目標輸出的映射，常見任務是分類與回歸。¦題目若同時給 training examples 與正確答案，優先想到 supervised learning。¦垃圾郵件分類有每封信的 spam/ham 標籤，屬於哪類學習？¦監督式學習。¦S8,S9
非監督式學習¦沒有明確標籤，模型從資料中找結構、群集或低維表示。¦題目出現 clustering、customer segmentation、pattern discovery 時要想到 unsupervised。¦沒有客戶類別標籤，仍想自動分群，應選哪類方法？¦非監督式學習。¦S8,S9
強化學習¦Agent 在環境中採取行動，根據 reward 學習策略；核心不是標籤，而是延遲回饋。¦看到 policy、reward、environment、agent 即鎖定 reinforcement learning。¦機器人以成功抓取物體取得獎勵，這是什麼學習？¦強化學習。¦S8
模型訓練生命週期¦資料準備、訓練、驗證、部署、監控與再訓練形成循環；部署不是終點。¦題目問 lifecycle 時，要同時想到 data、model、runtime 與 monitoring。¦模型上線後資料分布改變，下一步只調伺服器就夠嗎？¦不夠；需監控 drift，必要時更新資料並再訓練。¦S1,S2,S8
推論的本質¦Inference 使用已訓練且通常固定的權重，對新輸入產生預測或生成結果。¦「是否更新權重」是分辨 training 與 inference 的最快線索。¦線上 API 讀取固定模型回答請求，屬於哪個階段？¦Inference。¦S3,S4,S8
訓練與推論比較¦Training 重長時間吞吐、資料與反向傳播；inference 重 latency、throughput、可靠性與單次成本。¦同一模型在兩階段的硬體與軟體最佳化方向不同。¦要求每個請求 100ms 內回應，主要是哪個階段的考量？¦推論階段。¦S1,S2,S3
資料品質與代表性¦模型只能從提供的資料學習；偏差、缺漏、錯標與不代表真實世界的資料會限制泛化。¦「更多資料」不必然勝過「更乾淨且代表性更高的資料」。¦訓練準確率高但新客群表現差，先檢查什麼？¦資料分布、代表性與泛化問題。¦S8,S9
泛化與過度擬合¦Generalization 是對未見資料仍有效；overfitting 則過度記住訓練資料。¦訓練分數高、驗證分數差，是 overfitting 的典型訊號。¦模型在 training set 99%、validation 70%，最可能是什麼？¦過度擬合。¦S8
模型評估與指標¦分類常看 precision、recall、F1；回歸常看 MAE/MSE；production 還需 latency、cost 與可靠性。¦不要只選 accuracy；先看錯誤代價與業務目標。¦漏掉病患的代價極高，應特別重視哪個分類指標？¦Recall。¦S8,S9
生成式 AI¦生成式模型根據學到的分布產生新內容，例如文字、圖像、音訊或程式碼。¦分類模型選標籤；生成模型產生內容，兩者輸出型態不同。¦產生新的產品描述屬於預測分類還是生成？¦生成式 AI。¦S7
Transformer 與 LLM¦Transformer 以 attention 處理序列並支援高度平行的訓練；LLM 是其成功應用。¦考試通常測架構用途，不要求推導 attention 公式。¦為什麼 transformer 適合大型語言模型？¦能有效建模長距依賴，且訓練時可平行處理序列。¦S7
Token、Prompt 與 Context¦Token 是模型處理的基本序列單位；prompt 是輸入指令；context window 是可參考的上下文範圍。¦較長 context 通常增加記憶體與計算需求。¦輸入 token 倍增時，推論成本通常如何變化？¦通常上升，且可能增加延遲與記憶體需求。¦S7
RAG、微調與提示工程¦RAG 在生成前檢索外部知識；fine-tuning 調整參數；prompt engineering 不必改權重。¦題目問「更新知識且要可追溯來源」時，RAG 常比重訓更直接。¦內規每天更新，想避免頻繁重訓，優先考慮什麼？¦RAG。¦S7
加速運算¦把適合平行化的計算交給專用加速器，讓 CPU 與 GPU 分工，而非所有工作都由 CPU 處理。¦先判斷 workload 是否具高度資料平行性。¦含大量矩陣乘法的深度學習工作適合哪種處理器？¦GPU。¦S1,S2,S10
CPU 與 GPU 架構¦CPU 以較少而強的核心處理序列控制與低延遲分支；GPU 以大量較小核心處理平行工作。¦不是「GPU 永遠更快」，而是架構是否匹配 workload。¦資料庫控制流程與大量分支邏輯通常優先使用什麼？¦CPU。¦S10
GPU Streaming Multiprocessor¦SM 是 GPU 執行與排程大量 threads 的主要計算單元，內含多種運算資源。¦認識 SM 的角色即可，不要把 SM 與整張 GPU 混為一談。¦大量 threads 在 GPU 上由哪個主要硬體單元組織執行？¦Streaming Multiprocessor。¦S2,S11
Tensor Core¦Tensor Cores 專門加速矩陣乘加與支援的低精度運算，對深度學習訓練與推論重要。¦題目提到 mixed precision 與矩陣運算加速時要想到 Tensor Core。¦FP16 矩陣乘法想取得專用硬體加速，關鍵單元是什麼？¦Tensor Core。¦S2,S3
GPU 記憶體階層¦Registers、cache、shared memory 與 HBM/VRAM 有不同容量、延遲與可見範圍；資料移動會影響效能。¦算力高但 memory bandwidth 不足，GPU 仍可能等待資料。¦模型放不進 GPU memory，最直接限制的是什麼？¦可用 GPU 記憶體容量。¦S2,S6
平行主義：資料與模型¦Data parallel 複製模型、切資料；model parallel 切分模型；大型模型常混合多種並行策略。¦模型放不進單卡時，單純增加 data parallel 不會解決容量問題。¦模型權重超過單卡 VRAM，優先考慮哪類並行？¦模型或張量/管線並行。¦S2,S12
CUDA 的定位¦CUDA 是 NVIDIA GPU 平行運算平台與程式設計模型，提供執行 kernel、管理記憶體與開發 GPU 應用的基礎。¦CUDA 是底層平台，不等於 TensorRT 或 serving server。¦要撰寫自訂 GPU kernel，最直接使用哪個平台？¦CUDA。¦S11
cuDNN 的定位¦cuDNN 提供深度神經網路常用運算的 GPU 最佳化 primitives，供深度學習框架呼叫。¦cuDNN 是 library，不是模型登錄庫或叢集排程器。¦卷積與 activation 的最佳化函式庫是哪一類元件？¦cuDNN。¦S2
NCCL 的定位¦NCCL 實作 GPU 間高效 collective communication，如 all-reduce、all-gather 與 broadcast。¦多 GPU 訓練同步梯度時，NCCL 是高頻答案。¦Data-parallel training 要同步各 GPU 梯度，常用什麼？¦NCCL all-reduce。¦S12
TensorRT 的定位¦TensorRT 將已訓練模型最佳化並編譯為 NVIDIA GPU 推論 engine，目標是低延遲與高吞吐。¦TensorRT 是 inference optimizer/runtime，不負責原始模型訓練。¦部署 ONNX 模型並希望降低 NVIDIA GPU latency，應先想到什麼？¦TensorRT。¦S3,S4
混合精度與量化¦降低數值精度可減少記憶體、頻寬與計算成本，但必須重新驗證準確率。¦FP16/FP8/INT8 不是無條件更好；硬體支援與 accuracy 都要看。¦INT8 推論變快但 accuracy 掉太多，應怎麼做？¦重新校準/量化策略並以準確率門檻驗證。¦S3,S4
Triton Inference Server¦Triton 提供多模型、多框架 serving、dynamic batching、concurrent execution 與標準化部署能力。¦TensorRT 最佳化模型；Triton 管理與服務模型，層次不同。¦要在同一服務管理多模型版本與動態批次，應想到什麼？¦Triton Inference Server。¦S3,S13
NGC Catalog¦NGC 提供 NVIDIA 最佳化容器、模型、Helm charts 與 SDK 等可重用資產。¦NGC 是 catalog/registry 生態，不是 GPU driver。¦想取得 NVIDIA 最佳化框架容器，應去哪裡？¦NGC Catalog。¦S14
NVIDIA NeMo 概念¦NeMo 是 NVIDIA 生成式 AI 模型開發與客製化框架，可涵蓋訓練、微調與部署工作流。¦NeMo 偏模型開發；TensorRT-LLM 偏 LLM inference optimization。¦企業想客製化大型語言模型，哪類工具更接近開發層？¦NVIDIA NeMo。¦S2,S18
RAPIDS 概念¦RAPIDS 使用 GPU 加速資料處理與傳統資料科學工作流，減少 CPU 與 GPU 間不必要搬移。¦資料前處理慢不一定要換模型，可能需加速 data pipeline。¦大型表格資料前處理成為瓶頸，哪個 NVIDIA 生態工具值得評估？¦RAPIDS。¦S2
Base Command 與叢集管理概念¦NVIDIA 叢集管理解決方案聚焦工作負載、資源、使用者與基礎設施的可視化及管理。¦不要把 cluster management 與單機 inference runtime 混淆。¦要管理多使用者 GPU 叢集資源，而非只加速一個模型，應看哪一層？¦叢集管理與排程層。¦S1,S2
NVIDIA AI Enterprise¦AI Enterprise 是企業級 AI 軟體套件，重視支援、生命週期、相容性與 production deployment。¦企業採購題常不只比較功能，也比較支援與驗證矩陣。¦需要受支援的企業 AI 軟體堆疊，應評估什麼？¦NVIDIA AI Enterprise。¦S18
醫療與生命科學用例¦AI 可支援影像分析、藥物探索、文件處理與研究，但資料治理與風險要求高。¦用例題先找資料型態、輸出與錯誤代價。¦放射影像判讀屬於哪種常見 AI workload？¦Computer vision inference。¦S7,S9
金融、零售與製造用例¦金融常見詐欺/風險；零售常見推薦/需求預測；製造常見視覺檢測/預知維護。¦不要只背產業名，需配對 workload 和 KPI。¦產線即時瑕疵檢測最在意哪些指標？¦低延遲、可靠性與視覺模型準確率。¦S7,S9
Edge AI¦Edge AI 在資料產生地附近執行，降低往返延遲與頻寬需求，但受功耗、散熱與容量限制。¦題目提到現場即時、斷網可用與隱私，通常偏 edge。¦工廠相機需毫秒級反應且網路不穩，部署在哪裡較合理？¦Edge。¦S1,S2
軟體生命週期角色配對¦Framework 用於開發訓練，TensorRT 最佳化推論，Triton 提供服務，DCGM 監控 GPU，NGC 提供資產。¦高頻考法是「哪個元件負責哪一層」。¦哪個元件最適合監控 GPU health，而不是 serving 模型？¦DCGM。¦S1,S2,S3,S13,S15
NVIDIA 平台配對¦DGX 偏完整 AI 系統；HGX 是伺服器平台基礎；MGX 提供模組化伺服器架構；Jetson 聚焦 edge/embedded。¦平台題先看部署位置與系統整合程度。¦自主機器的嵌入式 AI 通常配對哪個平台？¦Jetson。¦S1,S2
Essential AI Knowledge 總複習¦把 AI/ML/DL、training/inference、CPU/GPU 與 CUDA/cuDNN/NCCL/TensorRT/Triton 串成一條 stack。¦若不能用一句話說清每個元件，先別背產品規格。¦請由底到上排列 CUDA、TensorRT、Triton。¦CUDA 提供底層 GPU 平台，TensorRT 最佳化推論模型，Triton 提供 serving。¦S1,S2,S3,S11,S13
''')

INFRASTRUCTURE = parse("infrastructure", r'''
從 Workload 反推硬體¦先確認模型大小、資料量、precision、batch、SLA、併行數與成長需求，再選 GPU、CPU、memory、network、storage。¦「最強 GPU」不是需求分析的替代品。¦離線訓練和即時推論能直接用同一 sizing 假設嗎？¦不能；兩者的吞吐、延遲、容量與可用性需求不同。¦S1,S2
訓練 GPU Sizing¦訓練 sizing 要看模型/activation/optimizer memory、batch、訓練時間目標與多 GPU scaling efficiency。¦參數量不是唯一記憶體來源。¦模型權重放得下但 training OOM，還可能是哪類資料佔用？¦Activation、gradient 與 optimizer states。¦S1,S2
推論 GPU Sizing¦推論 sizing 要看模型權重、KV cache、batching、concurrency、latency SLA 與精度。¦平均流量不足以代表尖峰容量。¦LLM 使用者數增加時，除了 weights 還要關注哪個主要 memory 消耗？¦KV cache。¦S3,S4,S7
Scale-up 與 Scale-out¦Scale-up 增強單節點與高速 GPU 互連；scale-out 增加節點並依賴網路與 distributed software。¦節點增加後，communication overhead 可能降低 scaling efficiency。¦模型主要卡在跨節點同步，繼續加節點一定線性加速嗎？¦不一定，網路與 collective overhead 會限制效率。¦S1,S2,S12
AI 叢集核心元件¦Compute nodes、management/login nodes、high-speed network、storage、scheduler、monitoring 與安全服務共同構成叢集。¦GPU nodes 只是叢集的一部分。¦使用者登入、提交 job 與 compute 執行是否應全放同一角色節點？¦通常分離，以提高安全、穩定與可管理性。¦S1,S2
CPU、RAM 與 GPU 平衡¦CPU 負責資料準備、I/O、控制與系統服務；RAM 容納 staging data；比例失衡會讓 GPU 閒置。¦GPU utilization 低時先看 host bottleneck。¦GPU 常等待 dataloader，應先檢查什麼？¦CPU、system memory、storage 與 preprocessing pipeline。¦S2,S6,S10
PCIe 的角色¦PCIe 連接 CPU、GPU、NIC、DPU 與 storage；lane、generation 與拓撲會影響可用頻寬。¦裝置都支援高速不代表整條 path 沒有共享瓶頸。¦兩張 GPU 共用受限 PCIe root complex 可能造成什麼？¦資料傳輸競爭與有效頻寬下降。¦S2,S6
NVLink 與 NVSwitch¦NVLink 提供 GPU 間高速互連；NVSwitch 讓多 GPU 建立高頻寬互連 fabric。¦它們不取代 data-center scale-out network。¦單節點多 GPU 模型並行最希望使用哪類互連？¦NVLink/NVSwitch。¦S2
Storage Hierarchy¦GPU memory 最快但固定；data fabric 連接 storage 與 GPU；storage devices 提供容量與持久性。¦容量、延遲、吞吐要分開討論。¦訓練時頻繁 swap 到磁碟會發生什麼？¦效能大幅下降，GPU 等待資料。¦S6
資料管線與 GPU 餵料¦讀取、解碼、augmentation、shuffle、batch 與 transfer 都可能成為 pipeline bottleneck。¦GPU utilization 低且 compute 短，常不是 GPU 算力問題。¦影像解碼耗盡 CPU，應優化哪一段？¦資料前處理與輸入管線。¦S6
平行檔案系統概念¦多節點訓練需要同時高吞吐與 metadata 能力；平行檔案系統可把 I/O 分散到多個 storage target。¦單一 NAS 可能在大規模並行讀取時成為瓶頸。¦上百節點同時讀 dataset，應關注什麼？¦Aggregate throughput、metadata scalability 與 network path。¦S1,S2,S6
GPUDirect Storage 概念¦目標是縮短 storage 到 GPU memory 的資料路徑，減少 CPU bounce buffer 與額外複製。¦不是所有 storage/network/platform 都自動支援，需看相容性。¦資料搬移被 CPU memory copy 限制時，可評估什麼方向？¦GPUDirect Storage 與完整 data path 最佳化。¦S6
網路需求推導¦Training 的 east-west collective traffic、storage traffic、management traffic 應分辨；不同流量對 latency/bandwidth 有不同要求。¦只看 NIC peak bandwidth 不足以設計網路。¦All-reduce 對網路最敏感的是什麼？¦低延遲、高頻寬與穩定的 collective communication。¦S1,S2,S12
Ethernet 與 InfiniBand¦Ethernet 生態廣、通用性高；InfiniBand 針對 HPC/AI 高效網路與 RDMA；選擇取決於規模、技能與目標。¦沒有「所有 AI 一律選某一種」的絕對答案。¦既有 Ethernet 團隊與中型 workload，要先做什麼？¦根據 SLA、規模與成本評估，不應只因品牌直接更換。¦S1,S2
Latency、Bandwidth、Throughput¦Latency 是傳輸等待；bandwidth 是理論容量；throughput 是實際完成量。¦三者不能互換，應對應 workload。¦許多小訊息頻繁同步，哪個指標通常更敏感？¦Latency。¦S1,S2
RDMA 與 RoCE¦RDMA 讓資料直接在端點記憶體間移動、降低 CPU involvement；RoCE 在 Ethernet 上承載 RDMA。¦RoCE 要求適當的 fabric 設計與 congestion management。¦想在 Ethernet 上使用 RDMA，常見技術是什麼？¦RoCE。¦S1,S2
Collective Communication 基礎¦All-reduce、all-gather、reduce-scatter 等操作是 distributed training 常見 communication pattern。¦不同 parallelism 會產生不同 collective。¦Data parallel 梯度同步最典型的 collective 是什麼？¦All-reduce。¦S12
DPU 的目的¦DPU 可卸載 networking、storage 與 security infrastructure services，釋放 CPU 並強化隔離。¦DPU 不是用來取代 GPU 執行模型張量運算。¦要把虛擬交換、storage 與 security offload 從 host CPU 移開，可用什麼？¦DPU。¦S1,S2,S17
BlueField DPU¦BlueField 結合可程式化處理器與高速網路，定位在 data-center infrastructure acceleration。¦考題問 infrastructure services offload 時比問 model training 更接近 BlueField。¦BlueField 主要加速哪一層？¦資料中心網路、儲存與安全基礎設施層。¦S17
AI Network Fabric 設計¦Clos/fat-tree 等拓撲追求可預測的 bisection bandwidth；oversubscription 會影響大規模 collective。¦邏輯拓撲與實際 cable/port mapping 都重要。¦為何 AI training fabric 常降低 oversubscription？¦避免多節點同步時網路成為瓶頸。¦S1,S2
On-prem 優缺點¦優點是控制、資料主權、可預測長期使用；缺點是前期資本、建置時間、容量與維運責任。¦高利用率、長期穩定需求較能攤提 on-prem。¦資料不能離場且 workload 穩定，哪種模式較有吸引力？¦On-prem。¦S1,S2
Cloud 優缺點¦優點是快速取得資源、彈性與託管服務；缺點是持續成本、資料移動、配額與供應差異。¦Burst workload 不必為尖峰永久買設備。¦短期實驗且需求不確定，哪種模式較靈活？¦Cloud。¦S1,S2
Hybrid 架構¦Hybrid 依資料、成本、容量與合規，把 workload 分配在 on-prem 與 cloud。¦資料與模型搬移成本會影響設計。¦敏感資料留本地、尖峰訓練借用雲端，屬於什麼？¦Hybrid。¦S1,S2
虛擬化考量¦Virtualization 提供隔離、可管理性與彈性，但需評估 GPU passthrough、vGPU、NUMA 與效能 overhead。¦不是所有 workload 都要求 bare metal。¦多桌面使用者共享 GPU 且重視隔離，應評估什麼？¦vGPU/虛擬化。¦S1,S2,S18

功率基本概念¦設計需估計 IT load、峰值、冗餘、conversion loss 與成長；不能只把 GPU TDP 相加。¦Nameplate、typical、peak 與 facility capacity 不同。¦機櫃 GPU 額定功耗總和等於實際設施需求嗎？¦不等於，還需 CPU、network、storage、loss、冗餘與安全餘裕。¦S1,S2
TDP 與容量規劃¦TDP 是熱設計與功耗規劃參考，不代表每時每刻的精確耗電；應以平台與 workload 測量驗證。¦考題問電力設計時要保留 headroom。¦為什麼不能用單顆 GPU TDP 直接決定 PDU？¦系統還有其他元件、瞬時峰值與冗餘需求。¦S1,S2
電力冗餘¦A/B feeds、UPS、PDU 與 PSU 冗餘降低單點失效，但可用容量需按冗餘模式計算。¦安裝容量不等於故障後可承載容量。¦要求任一電源路徑失效仍滿載，應如何規劃？¦A/B 路徑各自能承擔必要負載。¦S1,S2
氣冷與液冷¦高密度 AI rack 可能超出傳統氣冷能力；液冷能更直接移除熱量，但需要設施、監控與維護配套。¦選 cooling 需看 rack density，而非只看總機房冷量。¦單櫃熱密度急升且 airflow 已飽和，應評估什麼？¦液冷或其他高密度散熱方案。¦S1,S2
溫度與熱監控¦Inlet/outlet temperature、GPU temperature、fan、throttling 與 coolant 狀態可揭露熱風險。¦只看房間平均溫度可能漏掉 hot spot。¦GPU clock 因 thermal throttling 下降，先檢查什麼？¦設備與機櫃層的溫度、airflow/coolant 與風扇。¦S15
機櫃密度與空間¦Rack units、重量、功率、冷卻、cabling、service clearance 與 floor loading 都是設施要求。¦空間「放得下」不等於可安全供電與散熱。¦高密度 rack 上線前除了 RU 還要驗證什麼？¦重量、電力、冷卻、網路與維護空間。¦S1,S2
機房設施需求¦Power、cooling、network demarcation、fire safety、physical security、floor loading 與 maintenance workflow 共同決定可部署性。¦AI infrastructure 是跨 IT 與 facility 的工程。¦伺服器已到貨但機房供電不足，問題屬於哪一層？¦Facility readiness。¦S1,S2

Fault Domain¦把節點、rack、電源、switch 與 storage failure domain 納入 placement，可避免單一故障同時影響所有副本。¦冗餘若落在同一 fault domain 就是假冗餘。¦兩個副本都在同一 rack 的同一 PDU，算完整冗餘嗎？¦不算，仍共享單點故障。¦S1,S2
Availability 與冗餘設計¦HA 來自消除單點、快速偵測、failover、備份與復原演練；不是單靠昂貴元件。¦Recovery procedure 未演練就不能視為已驗證。¦有備份但從未測試 restore，風險是什麼？¦災難時可能無法在目標時間內復原。¦S1,S2
DGX 系統定位¦DGX 是整合 NVIDIA GPU、networking 與軟體的 AI 系統，降低自行整合完整節點的負擔。¦DGX 是系統級產品，不只是 GPU 卡。¦想快速取得整合式 NVIDIA AI 系統，應評估什麼？¦DGX。¦S1,S2
HGX 平台定位¦HGX 是供 OEM/系統建構 GPU 伺服器的高效能平台基礎，聚焦多 GPU 與高速互連。¦HGX 不等於完整資料中心 solution。¦伺服器 OEM 要建多 GPU 高效平台，核心基礎可選什麼？¦HGX。¦S1,S2
MGX 平台定位¦MGX 提供模組化伺服器架構，讓不同 CPU、GPU、DPU 與 workload 配置更有彈性。¦題目強調 modular、multiple configurations 時要想到 MGX。¦要用一致架構支援多種加速伺服器配置，應評估什麼？¦MGX。¦S1,S2
Reference Architecture¦Reference architecture 提供經驗證的元件、拓撲與規模設計起點，降低整合風險，但仍需依 workload 調整。¦Reference 不等於可以跳過 site survey。¦採用 reference architecture 後還要做 sizing 嗎？¦要，仍需依 workload、設施與 SLA 驗證。¦S1,S2
部署前驗證¦驗收應涵蓋 firmware/driver、GPU health、network bandwidth/latency、storage throughput、power/cooling 與 burn-in。¦「能開機」不代表 ready for AI。¦新叢集上線前最重要的整體動作是什麼？¦依設計基準做端到端驗收與 burn-in。¦S1,S2,S15
BOM 與容量預留¦BOM 應包含 compute、network、storage、rack、power、cooling、cables、spares 與 support；並預留成長。¦只列 GPU 數量會漏掉大量關鍵相依項。¦採購清單只有 GPU servers，缺少哪些常見項？¦Network、storage、rack/power/cooling、cabling、spares 與 support。¦S1,S2
AI Infrastructure 情境總複習¦從 workload → sizing → fabric → storage → facility → validation 依序推導，才能避免單點優化。¦情境題先圈出 bottleneck 與限制，再選最直接的元件。¦GPU utilization 低、storage latency 高，第一優先是加 GPU 嗎？¦不是；先修復 data path/storage bottleneck。¦S1,S2,S6
''')

OPERATIONS = parse("operations", r'''
AI Operations 的責任範圍¦Operations 涵蓋 provisioning、scheduling、monitoring、incident、capacity、change、security 與 lifecycle。¦模型 accuracy 不是 operations 唯一責任。¦GPU 正常但 job 長期排不到，屬於哪個維運面向？¦Resource management 與 scheduling。¦S1,S2
叢集管理基礎¦需要 inventory、node state、configuration、user/project、quota、health 與 lifecycle 的一致視圖。¦手動 SSH 每台節點不適合規模化維運。¦叢集節點設定逐漸不一致，應導入什麼思路？¦集中化、宣告式 configuration 與 drift detection。¦S1,S2
Monitoring Stack¦Metric、log、event、trace 與 alert 共同建立可觀測性；dashboard 不是監控的全部。¦能看到圖表但沒有告警與 runbook，仍不足以應變。¦GPU 錯誤發生後只能人工看 dashboard，缺少什麼？¦Alerting、事件流程與 runbook。¦S1,S2,S15
DCGM 的角色¦DCGM 提供資料中心 GPU 的 monitoring、diagnostics、health 與管理能力。¦DCGM 監控 GPU；它不是 training framework。¦要做 GPU health diagnostics，優先使用什麼？¦DCGM。¦S15
DCGM Exporter¦DCGM Exporter 把 GPU metrics 暴露給 Prometheus 生態，便於 dashboard 與 alerting。¦Exporter 是 metrics bridge，不是 scheduler。¦Kubernetes 想以 Prometheus 收集 GPU 指標，可用什麼？¦DCGM Exporter。¦S5,S15
核心 GPU 指標¦Utilization、memory use、temperature、power、clock、ECC/Xid errors 與 throttling 原因可描述健康與瓶頸。¦單看 utilization 不能判斷所有問題。¦利用率低但 power/clock 正常，還要看哪些外部訊號？¦CPU、network、storage、queue 與 workload behavior。¦S1,S2,S15
告警與基線¦告警應以正常基線、持續時間與業務影響設計，避免 noisy alerts；同時保留趨勢做 capacity planning。¦單次尖峰不一定是故障。¦GPU temperature 短暫上升就 page on-call 合理嗎？¦應結合門檻、持續時間、throttling 與 workload 基線。¦S15
Kubernetes 基礎¦Kubernetes 以 pod、node、scheduler、controller 與宣告式 API 管理容器工作負載。¦Kubernetes 本身不會自動安裝 NVIDIA driver stack。¦Pod 是什麼？¦Kubernetes 中最小的可部署/排程工作負載單位。¦S5
NVIDIA Device Plugin¦Device plugin 向 Kubernetes 註冊 GPU 資源，讓 scheduler 能依 resource request 分配 GPU。¦沒有 device plugin，pod 看不到可排程 GPU resource。¦Pod 要求 nvidia.com/gpu 但 cluster 沒該資源，先查什麼？¦NVIDIA device plugin 與 node GPU registration。¦S5
GPU Operator¦GPU Operator 以 Operator pattern 自動管理 driver、Container Toolkit、device plugin、GFD 與 DCGM monitoring 等元件。¦它解決 GPU software stack lifecycle，不是模型 serving。¦新 GPU node 需要一致安裝 NVIDIA 元件，應用什麼？¦GPU Operator。¦S5
NVIDIA Container Toolkit¦Container Toolkit 讓容器 runtime 能安全存取 NVIDIA GPU 與必要 libraries。¦Container image 通常不應取代 host kernel driver。¦Container 裡有 CUDA app 但看不到 GPU，應檢查什麼？¦Host driver、Container Toolkit、runtime 設定與 resource allocation。¦S5
排程與 Queue¦Scheduler 依資源、priority、policy、quota、affinity 與 topology 決定 job 何時在哪裡執行。¦排程問題不是只看「有沒有空 GPU」。¦高優先權 production job 被測試 job 佔滿資源，應用什麼機制？¦Priority、quota、preemption 或獨立資源池。¦S1,S2
Slurm 與 Kubernetes¦Slurm 常見於 HPC/batch scheduling；Kubernetes 常見於 container orchestration/service；實際環境可能整合或並存。¦不應只因 workload 有 GPU 就選其中一個。¦長時間 batch training 與佇列公平性是主需求，哪類 scheduler 常見？¦Slurm 類 HPC scheduler。¦S1,S2
MIG¦MIG 將支援的 GPU 劃分為具硬體隔離的 instances，提供較可預測的資源與多租戶隔離。¦MIG profile 是固定切分，不等同時間共享。¦多個小 inference workload 需要隔離與可預測資源，應評估什麼？¦MIG。¦S16
Time-slicing¦Time-slicing 讓多工作負載輪流使用 GPU，可提升共享彈性，但效能與隔離可預測性弱於 MIG。¦共享不等於 memory 硬隔離。¦開發環境想提高 GPU 使用率且可接受干擾，可用什麼？¦Time-slicing。¦S5,S16
vGPU¦vGPU 在虛擬化環境分配 GPU 能力，適合 VDI、VM 隔離與受支援企業環境。¦vGPU 與 MIG 可解決不同層次的 sharing。¦多個 VM 需要受控 GPU 存取，應評估什麼？¦NVIDIA vGPU。¦S1,S2,S18
Job Orchestration¦Pipeline 把 data prep、training、evaluation、registration 與 deployment 串接，需處理重試、artifact 與 dependency。¦單一 container 成功不等於 pipeline 可靠。¦Training 完成後 evaluation 失敗，正確 orchestrator 行為是什麼？¦阻止後續發布、保留 artifact/log 並依 policy 重試或告警。¦S1,S2
Logs 與 Troubleshooting¦從症狀定位層次：application → container → runtime → driver → hardware → network/storage；保留時間同步與 correlation ID。¦先建立假設，再用證據縮小範圍。¦所有 pod 同時出現 GPU access error，先查單一模型程式嗎？¦先查共同層：node、runtime、driver、device plugin。¦S5,S15
Driver、CUDA 與 Firmware 相容性¦Driver、CUDA runtime、framework、operator 與 firmware 需符合支援矩陣；任意升級可能破壞 stack。¦「最新版」不等於「相容」。¦升級 framework 後所有 job 失敗，第一步是什麼？¦比對完整支援矩陣與實際版本。¦S4,S5,S18
維護與滾動升級¦先驗證、分批 drain、升級、health check、再納回；保留 rollback 與 spare capacity。¦直接全叢集同時升級會放大 blast radius。¦GPU Operator 升級前應先做什麼？¦確認支援矩陣、備份設定、建立 canary/rollback 計畫。¦S5
安全與治理¦最小權限、image provenance、secrets、network policy、tenant isolation、audit 與資料治理都屬 production readiness。¦GPU 隔離不代表資料與網路已安全。¦使用者能拉任意不明 container image，主要風險是什麼？¦Supply-chain、惡意程式與未受控依賴風險。¦S14,S18
最終 60 分鐘考試策略¦官方考試為 50 題、60 分鐘；先做直接配對題，標記計算/情境題，最後回頭檢查否定詞與限制條件。¦平均約 72 秒一題，但不要在單題消耗過久。¦兩個選項都合理時怎麼選？¦回到題目限制，選最直接符合官方元件角色與主要 KPI 的答案。¦S1,S2
''')

UNITS = ESSENTIAL + INFRASTRUCTURE + OPERATIONS
assert [len(ESSENTIAL),len(INFRASTRUCTURE),len(OPERATIONS)] == [38,40,22]
assert len(UNITS)==100
assert len({u['title'] for u in UNITS})==100

DOMAIN_LABEL={"essential":"Essential AI Knowledge","infrastructure":"AI Infrastructure","operations":"AI Operations"}
DOMAIN_PCT={"essential":"38%","infrastructure":"40%","operations":"22%"}

cards=[]
for i,u in enumerate(UNITS,1):
    cites=' '.join(f'<a href="#source-{s}" title="{html.escape(SOURCES[s][0])}">[{s}]</a>' for s in u['sources'])
    cards.append(f'''<article class="study-unit" id="unit-{i}" data-unit="{i}" data-domain="{u['domain']}" data-search="{html.escape((u['title']+' '+u['concept']+' '+u['clue']).lower())}">
<header><span>UNIT {i:03d}</span><b>{DOMAIN_LABEL[u['domain']]} · {DOMAIN_PCT[u['domain']]}</b></header>
<h2>{html.escape(u['title'])}</h2>
<div class="unit-layout"><section><h3>核心理解</h3><p>{html.escape(u['concept'])}</p><h3>考場判斷線索</h3><p>{html.escape(u['clue'])}</p><p class="citations">依據 {cites}</p></section>
<aside><span>CHECK</span><p><strong>{html.escape(u['question'])}</strong></p><details><summary>顯示答案</summary><p>{html.escape(u['answer'])}</p></details></aside></div>
<label class="done"><input type="checkbox" data-check="{i}">完成這個單元</label>
</article>''')

mock=[]
# 50 distinct practice prompts: odd-numbered units, broad coverage across all domains.
for qn,idx in enumerate(range(0,100,2),1):
    u=UNITS[idx]
    mock.append(f'''<details class="mock-question"><summary><span>Q{qn:02d}</span>{html.escape(u['question'])}</summary><p><b>答案：</b>{html.escape(u['answer'])}</p><p><b>對應單元：</b><a href="#unit-{idx+1}">Unit {idx+1:03d} · {html.escape(u['title'])}</a></p></details>''')

source_html=''.join(f'<li id="source-{k}"><a class="source-link" href="{url}" target="_blank" rel="noopener noreferrer"><b>[{k}]</b> {html.escape(name)}</a></li>' for k,(name,url) in SOURCES.items())

DOC=f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="赫少獨立重新生成的 NVIDIA NCA-AIIO 100 單元週末考照準備教材，精準對齊官方 38/40/22 考試藍圖。"><title>赫少版｜NCA-AIIO 100 單元考照準備教材</title>
<style>
:root{{--g:#76b900;--bg:#070907;--ink:#161a16;--paper:#fbfcf8;--muted:#667064;--line:#d9ded2;--warn:#f2a900}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:#fff;font-family:Inter,"Noto Sans TC",system-ui,-apple-system,sans-serif;line-height:1.65}}a{{color:inherit}}.bar{{position:sticky;top:0;z-index:30;background:rgba(0,0,0,.94);border-bottom:1px solid #303630}}.bar-inner{{max-width:1320px;margin:auto;padding:12px 22px;display:flex;gap:14px;align-items:center}}.brand{{text-decoration:none;font-weight:900}}.brand i{{font-style:normal;color:var(--g)}}.search{{margin-left:auto;background:#141714;border:1px solid #3a4235;padding:8px 12px;min-width:280px}}.search input{{width:100%;background:none;border:0;outline:0;color:#fff}}button{{background:transparent;color:#fff;border:2px solid var(--g);padding:7px 11px;font-weight:800;cursor:pointer}}#progress{{height:4px;background:var(--g);display:block;width:0;transition:.2s}}.hero{{background:radial-gradient(circle at 80% 20%,rgba(118,185,0,.18),transparent 30%),#000}}.hero-inner{{max-width:1320px;margin:auto;padding:76px 22px 62px;display:grid;grid-template-columns:1.35fr .65fr;gap:48px}}.kicker{{color:var(--g);font-weight:900;letter-spacing:.15em;font-size:.75rem}}h1{{font-size:clamp(2.6rem,6vw,5.5rem);line-height:1.02;letter-spacing:-.055em;margin:12px 0 24px}}.lead{{font-size:1.12rem;color:#c8cec3;max-width:780px}}.disclaimer{{border-left:4px solid var(--warn);padding:12px 16px;background:#231a04;color:#f7dfa1}}.blueprint{{display:grid;gap:1px;background:#333;border:1px solid #333;align-self:end}}.weight{{background:#0c0e0c;padding:20px;display:grid;grid-template-columns:72px 1fr;align-items:center}}.weight b{{font-size:2rem;color:var(--g)}}.weight span{{color:#aaa;font-size:.86rem;white-space:nowrap}}.shell{{max-width:1320px;margin:auto;padding:38px 22px 88px;display:grid;grid-template-columns:250px minmax(0,1fr);gap:34px}}.side{{position:sticky;top:82px;height:calc(100vh - 96px);overflow:auto}}.side h2{{font-size:.72rem;letter-spacing:.14em;color:#8a9388}}.side a{{display:block;text-decoration:none;border-bottom:1px solid #2c312b;padding:9px 0;color:#c2c9bf;font-size:.84rem}}.side a:hover{{color:var(--g)}}.plan{{margin-top:20px;border:1px solid #303630;padding:15px;font-size:.78rem;color:#abb2a8}}.filters{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}}.filters button.active{{background:var(--g);color:#000}}.study-unit{{scroll-margin-top:82px;background:var(--paper);color:var(--ink);border-top:3px solid var(--g);padding:32px;margin:0 0 22px;box-shadow:0 10px 24px rgba(0,0,0,.28)}}.study-unit>header{{display:flex;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:9px;font-size:.72rem;letter-spacing:.08em}}.study-unit>header b{{color:#4e7900}}.study-unit h2{{font-size:clamp(1.55rem,3vw,2.25rem);letter-spacing:-.035em;line-height:1.2}}.unit-layout{{display:grid;grid-template-columns:1.5fr .65fr;gap:24px}}.unit-layout>section{{background:#fff;border:1px solid var(--line);padding:22px}}.unit-layout h3{{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;margin:0 0 7px}}.unit-layout h3:not(:first-child){{margin-top:22px}}.unit-layout aside{{background:#111;color:#fff;padding:22px;border-left:4px solid var(--g)}}.unit-layout aside>span{{color:var(--g);font-weight:900;font-size:.72rem;letter-spacing:.15em}}details summary{{cursor:pointer;font-weight:800}}.citations{{font-size:.76rem;color:var(--muted)}}.citations a{{color:#4c7600;font-weight:800}}.done{{display:flex;gap:8px;align-items:center;margin-top:18px;color:#667064;font-size:.82rem}}.done input{{width:18px;height:18px;accent-color:var(--g)}}.exam,.sources{{max-width:1320px;margin:0 auto 80px;padding:0 22px}}.exam-box,.source-box{{background:#0c0e0c;border:1px solid #343a32;padding:30px}}.exam-head{{display:flex;justify-content:space-between;align-items:end;gap:20px}}#exam-timer{{font:800 2rem ui-monospace,monospace;color:var(--g)}}.mock-question{{background:#151915;border:1px solid #303630;padding:14px 18px;margin:10px 0}}.mock-question summary{{display:flex;gap:12px}}.mock-question summary span{{color:var(--g)}}.mock-question p{{color:#c7cec4}}.source-box li{{margin:.55rem 0;color:#bac1b7}}.source-link{{text-decoration-color:var(--g);text-underline-offset:4px}}footer{{text-align:center;color:#7f897c;border-top:1px solid #2b302a;padding:28px}}[hidden]{{display:none!important}}
@media(max-width:900px){{.hero-inner,.shell{{grid-template-columns:1fr}}.weight span{{white-space:normal}}.side{{position:static;height:auto}}.unit-layout{{grid-template-columns:1fr}}.search{{min-width:0}}}}@media(max-width:620px){{.bar-inner{{padding:10px}}.brand span,button.print{{display:none}}.search{{width:100%}}.hero-inner{{padding:48px 16px}}.shell,.exam,.sources{{padding-left:12px;padding-right:12px}}.study-unit{{padding:22px 16px}}}}@media print{{.bar,.hero,.side,.filters,.done,.exam,.sources,footer{{display:none!important}}body{{background:#fff}}.shell{{display:block;padding:0;max-width:none}}.study-unit{{box-shadow:none;margin:0;page-break-after:always;min-height:95vh}}}}
</style></head><body>
<header class="bar"><div class="bar-inner"><a class="brand" href="../"><i>赫少</i> NCA-AIIO <span>PASS KIT</span></a><label class="search"><input id="search" type="search" placeholder="搜尋 100 單元…"></label><button class="print" onclick="window.print()">列印 / PDF</button></div><span id="progress"></span></header>
<section class="hero"><div class="hero-inner"><div><div class="kicker">INDEPENDENTLY REBUILT · OFFICIAL BLUEPRINT ALIGNED</div><h1>NCA-AIIO<br>考照準備教材</h1><p class="lead">赫少獨立重新生成的 100 單元 HTML 閱讀版。內容依 NVIDIA 官方藍圖精準配置：Essential AI Knowledge 38、AI Infrastructure 40、AI Operations 22。</p><p class="disclaimer">「必過」是準備目標，不是通過保證。本教材不是 NVIDIA 官方教材，也不包含真實考題；正式要求請以官方頁面為準。</p></div><div class="blueprint"><div class="weight"><b>38%</b><span>Essential AI Knowledge · Units 001–038</span></div><div class="weight"><b>40%</b><span>AI Infrastructure · Units 039–078</span></div><div class="weight"><b>22%</b><span>AI Operations · Units 079–100</span></div><div class="weight"><b>50</b><span>獨立自製模擬題 · 60 分鐘</span></div></div></div></section>
<div class="shell"><aside class="side"><h2>100-UNIT INDEX</h2><a href="#unit-1">001–038 Essential AI Knowledge</a><a href="#unit-39">039–078 AI Infrastructure</a><a href="#unit-79">079–100 AI Operations</a><a href="#mock-exam">50 題模擬考</a><a href="#sources">已驗證來源</a><div class="plan"><b>週六</b><br>Units 001–038 → 039–058<br><b>週日</b><br>Units 059–100 → 50 題模擬考<br><br><b>過關規則</b><br>每單元先閉卷回答 CHECK，再開答案。</div></aside><main><div class="filters"><button class="active" data-filter="all">全部 100</button><button data-filter="essential">Essential 38</button><button data-filter="infrastructure">Infrastructure 40</button><button data-filter="operations">Operations 22</button></div>{''.join(cards)}<p id="no-results" hidden>找不到符合的單元。</p></main></div>
<section class="exam" id="mock-exam"><div class="exam-box"><div class="exam-head"><div><div class="kicker">50-QUESTION PRACTICE</div><h2>60 分鐘模擬考</h2><p>非真實考題。先收合答案完成 50 題，再逐題訂正並回到對應單元。</p></div><div><div id="exam-timer">60:00</div><button id="timer-button">開始計時</button></div></div>{''.join(mock)}</div></section>
<section class="sources" id="sources"><div class="source-box"><div class="kicker">VERIFIED REFERENCES</div><h2>官方藍圖與已驗證來源</h2><ol>{source_html}</ol></div></section><footer>赫少獨立重建版 · NCA-AIIO 100-Unit Certification Prep · 2026</footer>
<script>
const units=[...document.querySelectorAll('.study-unit')],checks=[...document.querySelectorAll('[data-check]')],key='hermes-nca-aiio-pass-kit-v1';let done=new Set(JSON.parse(localStorage.getItem(key)||'[]'));function progress(){{checks.forEach(c=>c.checked=done.has(+c.dataset.check));document.getElementById('progress').style.width=done.size+'%'}}checks.forEach(c=>c.addEventListener('change',()=>{{c.checked?done.add(+c.dataset.check):done.delete(+c.dataset.check);localStorage.setItem(key,JSON.stringify([...done]));progress()}}));document.getElementById('search').addEventListener('input',e=>{{let q=e.target.value.trim().toLowerCase(),n=0;units.forEach(u=>{{u.hidden=!!q&&!u.dataset.search.includes(q);if(!u.hidden)n++}});document.getElementById('no-results').hidden=n>0}});document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('[data-filter]').forEach(x=>x.classList.toggle('active',x===b));let f=b.dataset.filter;units.forEach(u=>u.hidden=f!=='all'&&u.dataset.domain!==f)}}));let seconds=3600,timer=null;const display=document.getElementById('exam-timer'),timerButton=document.getElementById('timer-button');timerButton.addEventListener('click',()=>{{if(timer)return;timerButton.textContent='計時中';timer=setInterval(()=>{{seconds--;let m=String(Math.floor(seconds/60)).padStart(2,'0'),s=String(seconds%60).padStart(2,'0');display.textContent=m+':'+s;if(seconds<=0){{clearInterval(timer);display.textContent='00:00';timerButton.textContent='時間到'}}}},1000)}});progress();
</script></body></html>'''
OUT.write_text(DOC,encoding='utf-8')
print(f'wrote {OUT} units={len(UNITS)} mock={len(mock)} sources={len(SOURCES)}')
