from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

if __name__ == "__main__":
    # 2 qubit回路
    qc = QuantumCircuit(2, 2)
    # 2 qbit と 2 bitの系を用意

    # Bell状態作成
    qc.h(0) # q0をアダマールゲートで重ね合わせ状態へ
    qc.cx(0, 1) # q0の状態に合わせて、q1を操作(量子もつれ)(CNOTゲート)

    # 測定
    qc.measure([0, 1], [0, 1])

    print(qc)

    # シミュレーション
    simulator = AerSimulator()

    result = simulator.run(
        qc,
        shots=1000
    ).result()

    counts = result.get_counts()

    print(counts)

    """
    uv run main.py
         ┌───┐     ┌─┐
    q_0: ┤ H ├──■──┤M├───
         └───┘┌─┴─┐└╥┘┌─┐
    q_1: ─────┤ X ├─╫─┤M├
              └───┘ ║ └╥┘
    c: 2/═══════════╩══╩═
                    0  1
    {'11': 495, '00': 505}
    """
