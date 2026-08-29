# Kubernetes KCNA + CKA 教材品質 Review

Review date: 2026-08-29

## 目標

這套教材的目標不是「湊 100 頁 / 50 Labs」，而是讓學習者能從 KCNA foundational knowledge 走到 CKA performance-based hands-on 能力。

## 官方基準

### KCNA current domains

- Kubernetes Fundamentals — 44%
  - Kubernetes Core Concepts
  - Administration
  - Scheduling
  - Containerization
- Container Orchestration — 28%
  - Networking
  - Security
  - Troubleshooting
  - Storage
- Cloud Native Application Delivery — 16%
  - Application Delivery
  - Debugging
- Cloud Native Architecture — 12%
  - Observability
  - Cloud Native Ecosystem and Principles
  - Cloud Native Community and Collaboration

Current exam facts re-checked on 2026-08-29:

- Online proctored multiple-choice exam
- 60 questions
- 90 minutes
- Multiple-choice pass score: 75%
- Certification validity: 2 years

Sources: Linux Foundation KCNA certification / program changes / multiple-choice exam instructions and FAQ.

### CKA current domains / competencies

- Storage — 10%
- Troubleshooting — 30%
- Workloads and Scheduling — 15%
- Cluster Architecture, Installation and Configuration — 25%
- Services and Networking — 20%

Specific current competencies checked: RBAC, kubeadm, cluster lifecycle, highly-available control plane, Helm, Kustomize, CNI/CSI/CRI, CRDs/operators, rolling updates/rollbacks, ConfigMaps/Secrets, autoscaling, scheduling, NetworkPolicy, Service types/endpoints, Gateway API, Ingress, CoreDNS, StorageClass/dynamic provisioning, node/component troubleshooting, resource usage and container output streams.

Current CKA exam version re-checked: Kubernetes v1.35; 2-hour performance-based exam.

## Review Round 1 — 教學品質

### KCNA

- 問題：原版大量 Q2 重複使用「看到相關故障時，最好的第一步是？」。
- 判定：FAIL。這是模板，不足以證明情境判斷。
- 修正：renderer 不再顯示舊 Q2；新增 topic-aware teaching engine，依 scheduler / RBAC / PVC / Service / DNS / probes / CNI / storage / observability 等主題產生不同 scenario question。
- 加強：每頁新增「白話比喻」、「最容易搞錯」、「Teach-back」。

### CKA

- 問題：50 Labs 大方向完整，但 Mac kind 無法等價覆蓋 production kubeadm/systemd/HA control-plane。
- 判定：PARTIAL。
- 修正：新增官方 competency coverage matrix，區分 Mac 可完整練、object/concept 可練、Linux/Simulator 必補。
- 加強：新增 kubeadm lifecycle/upgrade、HA control plane、真 kubelet/systemd troubleshooting 三組必補 drills。

## Review Round 2 — Mock 與程式整合

### KCNA Mock

- 問題：初稿題庫實際 61 題（26 + 17 + 11 + 7），UI 卻標示 60。
- 判定：FAIL。
- 修正：正式 BANK 固定 26 / 17 / 10 / 7 = 60 題，約對齊官方 44 / 28 / 16 / 12。
- 計分分母改用 BANK length，並加 count mismatch console check。

### Shared JS

- 問題：KCNA v2 初稿呼叫 `setupStudyPage()`，但舊 shared JS 沒有 wrapper。
- 判定：FAIL。
- 修正：新增 `setupStudyPage({storageKey,total})`，統一初始化 progress + filter。

## Review Round 3 — UI / 可讀性

- 問題：CKA coverage table 使用 `table-wrap`，Simulator 區使用 `trapbox`，但樣式未全部提升到 Kubernetes 共用 CSS。
- 判定：PARTIAL。
- 修正：加入共用 responsive table、warning/trap box 樣式，KCNA/CKA 在桌面與手機維持同一套教學視覺。

## Review Round 4 — CKA Lab command fidelity

### Lab 19 Taint / Toleration

- 問題：舊版題目要求「加 toleration」，但 command 最後只是移除 taint，實際上繞過了考點。
- 判定：FAIL。
- 修正：改成對照實驗：
  1. Node 加 `dedicated=gpu:NoSchedule`。
  2. `no-tol` Pod 用 nodeSelector 指到該 Node，確認 FailedScheduling。
  3. `with-tol` Pod 加 matching toleration，確認能排到該 Node。
  4. 最後才清理 taint。
- 加強：明確教「toleration 不是吸引 Pod，只是不被 taint 排斥」。

## Review Round 5 — 官方事實再驗證

- KCNA 2026 domains: 44 / 28 / 16 / 12 — PASS。
- KCNA exam: multiple-choice / 90 min / 60 questions / 75% pass — PASS against current LF docs。
- CKA exam: v1.35 / 2 hours / performance-based — PASS against current LF certification page。
- CKA updated competencies include Helm/Kustomize, CRD/operator, Gateway API, CoreDNS, HA control plane, kubeadm lifecycle — coverage matrix updated。

## Certification readiness gate

### KCNA 建議達標

1. 100 lessons 全部至少完成一次。
2. 高頻主題可 20 秒 Teach-back：用途 + 責任邊界 + 一個例子。
3. Mini lab 跑完能指出「哪個輸出證明了本頁概念」。
4. 60 題 full mock 第一次不查資料至少 80%。
5. 錯題回教材，隔一段時間重做至少 90%。
6. 任一 domain 低於 75% 就先補該 domain，不用總分掩蓋弱點。

### CKA 建議達標

1. 50 Labs 至少完整做過一次。
2. 隨機抽 10 Labs，不看 step-by-step solution 能完成至少 8。
3. Troubleshooting 15 Labs 看到症狀能先選正確 evidence path：
   - Pending → describe / Events / scheduling constraints
   - CrashLoop → logs / `--previous`
   - ImagePull → Events / image / registry auth
   - Service → selector / EndpointSlice / readiness / port
   - DNS → client lookup / resolv.conf / CoreDNS / kube-dns Service
   - Storage → PVC / PV / StorageClass / events
   - Node → conditions / kubelet / runtime / CNI / systemd (real Linux)
4. 真 Linux / simulator 補完 kubeadm lifecycle、HA control plane、kubelet/systemd troubleshooting。
5. Killer.sh 兩次用 2 小時計時練習，重點是 task triage、文件查找、verification。

## 環境誠實性

- Mac mini + Docker Desktop + kind：適合 API object、workload、RBAC、Service/DNS、storage object、部分 networking 與大量 application troubleshooting。
- kind node 是 container，不等同完整 systemd Linux Node。
- NetworkPolicy enforcement 取決於 CNI。
- Gateway API / Ingress 完整 data plane 取決於 CRDs/controller。
- Dynamic provisioning 取決於 provisioner/StorageClass。
- 真 kubeadm package upgrade、`systemctl/journalctl kubelet`、production HA control plane：必須用 Linux VM / exam simulator / 其他真實 cluster 補。

## Exam ethics

所有題目與 Lab 依公開 syllabus / Kubernetes docs 自編，不使用、重製或宣稱是真實非公開 exam questions。

## Current status

- KCNA public competency coverage: PASS
- KCNA plain-language teaching layer: PASS
- KCNA repeated-Q2 issue in rendered教材: PASS / fixed
- KCNA certification readiness mock: PASS / exact 60-question rendered bank
- Shared progress/filter/copy UI: PASS after integration fix
- CKA public competency mapping: PASS with explicit Linux/simulator supplements
- CKA Lab 19 fidelity: PASS after command correction
- Mac-only production-equivalence claim: intentionally NOT made

下一次內容更新時，應重新對照 Linux Foundation 當下 exam version / program changes，再跑同一份 review checklist。