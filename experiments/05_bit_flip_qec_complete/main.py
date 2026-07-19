from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

# 3量子ビット・ビットフリップ符号の完全版
# エンコード → エラー注入 → シンドローム抽出 → 動的回路で in-circuit 訂正 → 読み出し

if __name__ == '__main__':
    data = QuantumRegister(3, "d")   # データ（論理量子ビットを担う3つ）
    anc = QuantumRegister(2, "a")    # アンシラ（シンドローム測定用）
    syn = ClassicalRegister(2, "syn")  # シンドローム値
    out = ClassicalRegister(3, "out")  # 最終読み出し（syn とは別レジスタ）
    qc = QuantumCircuit(data, anc, syn, out)

    # エンコード: 論理 |1> を |111> に符号化（自明でない状態を守る）
    qc.x(data[0])
    qc.cx(data[0], data[1])
    qc.cx(data[0], data[2])
    qc.barrier()

    # エラー注入: d1 をビットフリップ
    qc.x(data[1])
    qc.barrier()

    # シンドローム抽出
    # a0 = d0 ⊕ d1 の比較
    qc.cx(data[0], anc[0])
    qc.cx(data[1], anc[0])
    # a1 = d1 ⊕ d2 の比較
    qc.cx(data[1], anc[1])
    qc.cx(data[2], anc[1])
    qc.measure(anc[0], syn[0])
    qc.measure(anc[1], syn[1])
    qc.barrier()

    # in-circuit フィードフォワード訂正（syn の値で分岐）
    # syn = a1*2 + a0 :  01→d0, 11→d1, 10→d2, 00→エラー無し
    with qc.if_test((syn, 0b01)):
        qc.x(data[0])
    with qc.if_test((syn, 0b11)):
        qc.x(data[1])
    with qc.if_test((syn, 0b10)):
        qc.x(data[2])

    # 読み出し
    qc.measure(data, out)
    print(qc)

    sim = AerSimulator()
    counts = sim.run(qc, shots=1000).result().get_counts()
    print(counts)  # 期待: "out syn" = "111 11"（訂正されて |111> に回復）
