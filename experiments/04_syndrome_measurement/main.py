from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

if __name__ == '__main__':
    qc = QuantumCircuit(5,2)
    # errorを入れる
    # q1を反転
    qc.x(1)
    # syndrome 0: q0 と q1 の比較
    qc.cx(0,3)
    qc.cx(1,3)
    # syndrome 1: q1 と q2 の比較
    qc.cx(1,4)
    qc.cx(2,4)
    # syndrome測定
    qc.measure(3,0)
    qc.measure(4,1)
    print(qc)
    sim = AerSimulator()
    result = sim.run(
        qc,
        shots=1000
    ).result()
    print(result.get_counts())
