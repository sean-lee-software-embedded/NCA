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

Source: Linux Foundation KCNA program changes / certification pages.

### CKA current domains / competencies

- Storage — 10%
- Troubleshooting — 30%
- Workloads and Scheduling — 15%
- Cluster Architecture, Installation and Configuration — 25%
- Services and Networking — 20%

Specific current competencies checked in this review include RBAC, kubeadm, cluster lifecycle, highly-available control plane, Helm, Kustomize, CNI/CSI/CRI, CRDs/operators, rolling updates/rollbacks, ConfigMaps/Secrets, autoscaling, scheduling, NetworkPolicy, Service types/endpoints, Gateway API, Ingress, CoreDNS, StorageClass/dynamic provisioning, node/component troubleshooting, resource usage and container output streams.

Source: Linux Foundation CKA certification and program changes pages. Current exam version: Kubernetes v1.35.

## Review Round 1 — 找到的問題

### KCNA

- 問題：原版大量 Q2 重複使用「看到相關故障時，最好的第一步是？」。
- 判定：FAIL。這只是模板化練習，無法證明學習者能把概念套進不同情境。
- 修正：KCNA lesson renderer 不再顯示舊 Q2；新增 topic-aware teaching engine，依 scheduler / RBAC / PVC / Service / DNS / probes / CNI / storage / observability 等不同主題產生不同 scenario question。
- 加強：每頁新增「白話比喻」、「最容易搞錯」、「Teach-back」。

### CKA

- 問題：50 Labs 大方向完整，但 Mac kind 無法等價覆蓋 production kubeadm/systemd/HA control-plane。
- 判定：PARTIAL。
- 修正：新增官方 competency coverage matrix，明確區分 Mac 可完整練、object/concept 可練、Linux/Simulator 必補。
- 加強：新增 kubeadm lifecycle/upgrade、HA control plane、真 kubelet/systemd troubleshooting 三組必補 drills。

## Review Round 2 — 找到的問題

### KCNA Mock

- 問題：初稿題庫實際為 61 題（26 + 17 + 11 + 7），但 UI 標示 60 題。
- 判定：FAIL。
- 修正：正式 mock 固定採 26 / 17 / 10 / 7 = 60 題；約對齊 44 / 28 / 16 / 12 的官方 domain weighting。
- UI 計分分母改為實際 BANK length，並加 assertion / console error 保護。

### Shared JS

- 問題：KCNA v2 page 初稿呼叫 `setupStudyPage()`，舊 shared JS 尚未提供 wrapper。
- 判定：FAIL。
- 修正：新增 `setupStudyPage({storageKey,total})`，統一初始化 progress + filter。

## Certification readiness gate

### KCNA 建議達標

1. KCNA 100 lessons 全部至少完成一次。
2. 高頻主題可以 20 秒 Teach-back：用途 + 責任邊界 + 一個例子。
3. Mini lab 的輸出要能解釋「哪一欄證明這個概念」。
4. 60 題 full mock 第一次不查資料至少 80%。
5. 錯題回教材、隔一段時間再做，至少 90%。
6. 若某 domain 低於 75%，不要用總分掩蓋弱點，先補該 domain。

### CKA 建議達標

1. 50 Labs 至少完整做過一次。
2. 隨機抽 10 Labs，不看 step-by-step reference solution 能完成至少 8。
3. Troubleshooting 15 Labs 要熟到看到症狀能先選正確 evidence path：
   - Pending → describe / Events / scheduling constraints
   - CrashLoop → logs / --previous
   - ImagePull → Events / image / registry auth
   - Service → selector / EndpointSlice / readiness / port
   - DNS → client lookup / resolv.conf / CoreDNS / kube-dns Service
   - Storage → PVC/PV/StorageClass/events
   - Node → conditions / kubelet/runtime/CNI/systemd (real Linux)
4. 真 Linux / simulator 補完 kubeadm lifecycle、HA control plane、kubelet/systemd troubleshooting。
5. Killer.sh 兩次用 2 小時計時方式練習，重點是 task triage、文件查找、verification。

## 環境誠實性

- Mac mini + Docker Desktop + kind：適合 API object、workload、RBAC、Service/DNS、storage object、部分 networking 與大量 application troubleshooting。
- kind node 是 container，不等同完整 systemd Linux Node。
- NetworkPolicy enforcement 取決於 CNI。
- Gateway API / Ingress 完整 data plane 取決於 CRDs/controller。
- Dynamic provisioning 取決於 provisioner/StorageClass。
- 真 kubeadm package upgrade、systemctl/journalctl kubelet、production HA control plane：必須用 Linux VM / exam simulator / 其他真實 cluster 補。

## Exam ethics

所有題目與 Lab 依公開 syllabus / Kubernetes docs 自編，不使用、重製或宣稱是真實非公開 exam questions。

## Current status

- KCNA concept coverage: PASS against current public domain/competency map.
- KCNA question variety: PASS after v2 scenario-question rebuild.
- KCNA mock exact count / weighting: PASS after Round 2 fix.
- CKA public competency mapping: PASS with explicit Linux/simulator supplements.
- Mac-only completeness: intentionally NOT claimed; limitations are documented instead of被包裝成完整 production-equivalent environment。
