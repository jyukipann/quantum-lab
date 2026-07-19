from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def init_qc()->QuantumCircuit:
    qc = QuantumCircuit(3, 3)
    # 初期状態
    # |000>
    return qc

def measure(qc: QuantumCircuit):
    qc.measure(
        [0,1,2],
        [0,1,2]
    )
    print(qc)
    simulator = AerSimulator()
    result = simulator.run(
        qc,
        shots=1000
    ).result()
    print(result.get_counts())

def no_coding():
    qc = init_qc()
    measure(qc)

def coding():
    qc = init_qc()
    qc.x(0)
    qc.cx(0,1)
    qc.cx(0,2)
    measure(qc)

def coding_with_noise():
    qc = init_qc()
    qc.cx(0,1)
    qc.cx(0,2)
    qc.x(1)
    measure(qc)


if __name__ == "__main__":
    no_coding()
    coding()
    coding_with_noise()
