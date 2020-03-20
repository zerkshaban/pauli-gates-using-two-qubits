%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, execute, Aer
import numpy as np
import math as m
S_simulator = Aer.backends(name='statevector_simulator')[0]
M_simulator = Aer.backends(name='qasm_simulator')[0]

q = QuantumRegister(2)
two_qubits = QuantumCircuit(q)
# Got two minus/zero vector by default.
# q32_0: |0>
# q32_1: |0>
two_qubits.iden(q[0])
two_qubits.iden(q[1])
# Applying identity gate to zero vectors.
#           ┌────┐
# q33_0: |0>┤ Id ├
#           ├────┤
# q33_1: |0>┤ Id ├
#           └────┘

two_qubits.h(q[0])
two_qubits.h(q[1])
# Applying Hadamard gate to zero vectors.
#           ┌───┐
# q35_0: |0>┤ H ├
#           ├───┤
# q35_1: |0>┤ H ├
#           └───┘

two_qubits.h(q[0])
two_qubits.cx(q[0], q[1])
# Applying Hadamard and CX gate to zero vectors.
#           ┌───┐
# q37_0: |0>┤ H ├──■──
#           └───┘┌─┴─┐
# q37_1: |0>─────┤ X ├
#                └───┘
job = execute(two_qubits, S_simulator)
result.get_statevector()

# Iden Gate Result
# result.get_statevector()
# array([0.70710678+0.j, 0.70710678+0.j]) Is the result on excuting the circuit.

# Hadamard Gate Result
# result.get_statevector()
# array([0.70710678+0.j, 0.70710678+0.j]) Is the result on excuting the circuit.

# Hadamard and CNOT Gate Combination Result
# result.get_statevector()
# array([0.70710678+0.j, 0.70710678+0.j]) Is the result on excuting the circuit.
