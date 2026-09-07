# CKA 100-page Weekend Sprint — Quality Review

Review date: 2026-09-07

## Source hierarchy

1. Linux Foundation current CKA certification page / program changes / candidate docs = exam facts and competencies.
2. Kubernetes / Helm / Gateway API official docs = technical behavior and command/document references.
3. iThome article 10354313 = preparation workflow and practical study ideas; 2024 price/version facts were intentionally not copied forward.
4. Killercoda / community CKA Exercises = optional practice inspiration only.

## Review Round 1 — Official competency coverage

Expected page allocation exactly mirrors official weights: 25 / 15 / 20 / 10 / 30.

- Cluster Architecture, Installation & Configuration: 25 pages — PASS
- Workloads & Scheduling: 15 pages — PASS
- Services & Networking: 20 pages — PASS
- Storage: 10 pages — PASS
- Troubleshooting: 30 pages — PASS

Keyword/competency coverage:
- Cluster Architecture, Installation & Configuration: PASS
- Workloads & Scheduling: PASS
- Services & Networking: PASS
- Storage: PASS
- Troubleshooting: PASS

Result: PASS. The 2025+ additions are explicitly represented: Helm, Kustomize, CRDs/operators, extension interfaces, Gateway API, workload autoscaling, and troubleshooting-heavy practice.

## Review Round 2 — Command/version/structure fidelity

Checks performed:

- Exactly 100 unique lesson titles: PASS.
- Exactly 100 rendered `<article class="lesson ...">` pages: PASS.
- Domain counts equal official exam weights: PASS.
- Every page includes Command Path, Hands-on Drill and Verification: PASS.
- Current CKA facts in front matter: Kubernetes v1.35, 2 hours, 66% pass threshold, exam-only list price US$445, two exam attempts: PASS against current LF pages checked 2026-09-07.
- Stale US$395 fact from the 2024 iThome article is not present: PASS.
- kubeadm upgrade is deliberately version-placeholder based (`v1.35.x` / task-specified version), avoiding unsafe hard-coded patch memorization: PASS.
- VPA is identified as an add-on CRD/controller, not a built-in core API: PASS.
- Gateway API pages require CRD/controller presence and teach status conditions: PASS.
- NetworkPolicy enforcement is correctly caveated as CNI-dependent: PASS.

## Review Round 3 — Exam realism / one-pass risk reduction

The material explicitly drills all of these high-value actions:

- context/namespace discipline
- `--dry-run=client -o yaml`, `-h`, `kubectl explain`
- kubeadm lifecycle and upgrade
- kubelet/systemd/journalctl
- crictl when API is down
- Helm and Kustomize
- CRD/operator discovery
- Gateway API / HTTPRoute status
- EndpointSlice-first service troubleshooting
- CoreDNS / NetworkPolicy
- PV/PVC/StorageClass
- `kubectl logs --previous` and multi-container logs
- `kubectl top` / resource usage

Result: PASS.

## Review Round 4 — Targeted high-risk command/document spot-check

- `kubectl create job NAME --image=... -- [COMMAND] [args...]`: PASS against current Kubernetes kubectl reference.
- `kubectl create cronjob NAME --image=... --schedule=... -- [COMMAND] [args...]`: PASS against current Kubernetes kubectl reference.
- CKA domain weights and 2026 exam version/duration/price/attempts re-checked immediately before publication: PASS.
- iThome 2024/2025 advice was used only as preparation strategy; stale price and pre-2025 scope were not treated as current authority: PASS.
- Final HTML/JS syntax and 100-object data count: PASS.
- Every lesson renders Command Path, Hands-on Drill, Verification, official-doc search keywords and a 60-second self-check: PASS.

Result: PASS.

## Important limitation

No study material can guarantee a first-attempt pass. The HTML therefore uses a readiness gate rather than a guarantee: complete all 100 pages, repeat the 30 troubleshooting pages, complete real-Linux kubeadm/kubelet/static-Pod drills, and score >=85% on two timed mocks with no domain below 75%.

## Environment honesty

Mac mini + kind is appropriate for API-object practice and many workload/network/storage object drills, but it is not treated as equivalent to a full systemd Linux node for kubeadm package upgrades, kubelet service debugging or production HA.
