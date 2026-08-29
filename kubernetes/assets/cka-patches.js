(function(){
  if(!window.CKA_DATA||CKA_DATA.length<20)return;
  CKA_DATA[18]=[
    'Lab 19 - Taint / Toleration',
    'Workloads & Scheduling 15%',
    'dedicated worker 不允許一般 Pods；只有帶正確 toleration 的 workload 才能通過該 taint。這題要真的練「允許」，不能靠把 taint 刪掉來繞過考點。',
    ['在 cka-worker 加 dedicated=gpu:NoSchedule taint。','建立 no-tol Pod 並指定到該 worker，確認 FailedScheduling。','建立 with-tol Pod，加入 matching toleration。','確認 with-tol 成功排到 tainted node。','最後清理 taint。'],
    `kubectl label node cka-worker disk=ssd --overwrite
kubectl taint node cka-worker dedicated=gpu:NoSchedule --overwrite

cat > /tmp/no-tol.yaml <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: no-tol
spec:
  nodeSelector:
    disk: ssd
  containers:
  - name: nginx
    image: nginx:1.27
EOF
kubectl apply -f /tmp/no-tol.yaml
kubectl describe pod no-tol

cat > /tmp/with-tol.yaml <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: with-tol
spec:
  nodeSelector:
    disk: ssd
  tolerations:
  - key: dedicated
    operator: Equal
    value: gpu
    effect: NoSchedule
  containers:
  - name: nginx
    image: nginx:1.27
EOF
kubectl apply -f /tmp/with-tol.yaml`,
    `kubectl get pods no-tol with-tol -o wide
kubectl describe pod no-tol | grep -A8 -i Events
# with-tol 應能排到 cka-worker；no-tol 應保持 Pending
kubectl taint node cka-worker dedicated=gpu:NoSchedule-`,
    'Mac mini + kind 可完整完成。',
    'Toleration 不是「吸引 Pod 到 Node」；它只讓 Pod 不被 matching taint 排斥。所以本題同時用 nodeSelector 固定 placement，才能清楚驗證 toleration。',
    'Review fix：舊版用移除 taint 當作修復，沒有真正練到 toleration；新版已改成兩個 Pod 對照實驗。'
  ];
})();