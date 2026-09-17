# CKA v1.35 — 100-page Weekend Sprint QA

Review date: 2026-09-17

## Automated checks

- [x] 100 lesson pages
- [x] Cluster 25
- [x] Workloads 15
- [x] Networking 20
- [x] Storage 10
- [x] Troubleshooting 30
- [x] Every page command path
- [x] Every page verification
- [x] Every page hands-on drill
- [x] Every page trap
- [x] Every page docs keywords
- [x] v1.35 current alignment
- [x] 66% pass threshold context
- [x] Current price context
- [x] No pass guarantee
- [x] Print fixed page sections

## Review Round 1 — Official curriculum mapping
- Verified current CKA domains and competencies against Linux Foundation/CNCF materials.
- Exact print lesson allocation: Cluster 25 / Workloads 15 / Networking 20 / Storage 10 / Troubleshooting 30.

## Review Round 2 — 2025 change coverage
- Explicit coverage: Helm, Kustomize, CRDs/operators, Gateway API, workload autoscaling, HA control plane, CNI/CSI/CRI, kubeadm lifecycle.
- iThome 2024 experience is used for preparation method; its historical price/task-count statements are not treated as 2026 official facts.

## Review Round 3 — Command and verification fidelity
- Every page contains a command path, hands-on drill, final-state verification, common trap, and official-doc search terms.
- Avoided hard-coding an arbitrary kubeadm patch version; task-specified version + official version-skew policy remain source of truth.

## Review Round 4 — Environment fidelity
- Mac mini + kind is explicitly treated as suitable for API objects/workloads/networking practice, not as a replacement for real systemd Linux nodes.
- Real Linux/simulator required for kubeadm upgrade, HA control plane, kubelet/systemd/runtime troubleshooting.

## Review Round 5 — Freshness, exam ethics, and publication structure
- No confidential/remembered exam questions are reproduced. Labs are self-authored from public competencies and docs.
- Exam price/version/rules are marked as re-check-before-scheduling facts.
- 100 independent printable lesson sections are present; screen UI includes progress persistence and navigation.

## Review Round 6 — KodeKloud cross-map and short-sprint routing
- Reviewed the public KodeKloud CKA repository snapshot `506b5418` dated 2026-09-01: 17 course sections and 198 Markdown resources.
- Added a chapter-to-page map, four-phase 48-hour route, priority labels, mock-exam gate, and explicit `kind` versus real-Linux practice boundaries.
- Linked to the upstream repository rather than reproducing its notes verbatim; current official competencies remain the source of truth.

## Review Round 7 — Pod lifecycle, controllers, Static Pods, and Admission
- Added a Traditional Chinese printable module covering Pod update restrictions, owner-aware replacement, ReplicaSet versus DaemonSet, Static versus regular Pods, mirror Pods, and kubelet-local diagnosis.
- Diagnosed the supplied `static-busybox.yaml`: removed API-managed metadata/status and ServiceAccount projected volume, and corrected `command: ["sleep"]` with `args: ["1000"]`.
- Added the Admission request order, mutating versus validating behavior, built-in plugins versus webhooks/policies, inspection commands, and the connection between admission defaults and an exported regular Pod manifest.
- Cross-linked the module from lessons 6, 26, 30, 31, and 40 while preserving the exact 100-page domain allocation.
- Rechecked nuanced claims against current upstream Kubernetes documentation; version-sensitive behavior is explicitly routed to `kubectl explain`, server-side dry-run, and task-version docs.

## Readiness gate
- 100/100 hands-on pages completed.
- Existing 50 CKA Labs completed once; random 10 >= 8 without step-by-step solution and with verification.
- At least one 120-minute full mock / Killer.sh >= 80%.
- Every mistake redone the next day from a clean state.
- Real Linux kubeadm / HA / kubelet-systemd drills completed.

## Publication result
**PASS.** This materially reduces preparation risk but cannot guarantee an exam outcome.
