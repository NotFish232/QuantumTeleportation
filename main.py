import qiskit as Q
from qiskit import transpile
from qiskit_aer import AerSimulator

q_registers = [Q.QuantumRegister(3)]
c_registers = [Q.ClassicalRegister(2)]
circuit = Q.QuantumCircuit(*q_registers, *c_registers)
circuit.h(1)
circuit.cx(1, 2)
circuit.barrier()

circuit.cx(0, 1)
circuit.h(0)
circuit.barrier()

circuit.measure(range(2), range(2))
circuit.barrier()

circuit.z(2).c_if(c_registers[0]._bits[0], 1)
circuit.x(2).c_if(c_registers[0]._bits[1], 1)

backend = AerSimulator()
compiled_circuit = transpile(circuit, backend)
job_simulation = backend.run(compiled_circuit, shots=1024)
job_result = job_simulation.result()
counts = job_result.get_counts()

print(circuit)
print(counts)