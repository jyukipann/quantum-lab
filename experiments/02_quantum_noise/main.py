from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def clean():
    qc = QuantumCircuit(1, 1)
    # 測定
    qc.measure(0, 0)
    print(qc)
    simulator = AerSimulator()
    result = simulator.run(
        qc,
        shots=1000
    ).result()
    print(result.get_counts())

def noisy():
    qc = QuantumCircuit(1, 1)
    # 反転でノイズを再現
    qc.x(0)
    # 測定
    qc.measure(0, 0)
    print(qc)
    simulator = AerSimulator()
    result = simulator.run(
        qc,
        shots=1000
    ).result()
    print(result.get_counts())

def noisy_with_hadamard():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    # 反転でノイズを再現
    qc.x(0)
    # 測定
    qc.measure(0, 0)
    print(qc)
    simulator = AerSimulator()
    result = simulator.run(
        qc,
        shots=1000
    ).result()
    print(result.get_counts())

if __name__ == '__main__':
    clean()
    noisy()
    noisy_with_hadamard()
