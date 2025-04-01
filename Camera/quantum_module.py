from qiskit.providers.basic_provider import BasicSimulator
from qiskit import QuantumCircuit, transpile
import random

def get_quantum_random_number(num_bits):
    random.seed(12345)
    qc = QuantumCircuit(num_bits, num_bits)
    qc.h(range(num_bits))
    qc.measure(range(num_bits), range(num_bits))
    simulator = BasicSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    random_number = int(list(counts.keys())[0], 2)
    return random_number
