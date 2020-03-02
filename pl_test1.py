import pennylane as qml
from pennylane import numpy as np

num_wires = 5
dev1 = qml.device('default.qubit', wires=num_wires)

@qml.qnode(dev1)
def circuit():
	output = []
	
	# Encoding the data (Variational Encoding)
	qml.RX(1.01, wires=[0])
	qml.RX(0.81, wires=[1])
	qml.RX(0.81, wires=[2])
	qml.RX(1.3e-2, wires=[3])
	qml.RX(0.16, wires=[4])

	qml.RZ(1.01, wires=[0])
	qml.RZ(0.81, wires=[1])
	qml.RZ(0.81, wires=[2])
	qml.RZ(1.3e-2, wires=[3])
	qml.RZ(0.16, wires=[4])

	# Making the Parameterised QUantum Circuit (PQC)
	qml.RX(1.10, wires=[0])
	qml.RZ(0.75, wires=[0])
	qml.CNOT(wires=[0, 1])
	qml.RX(0.82, wires=[0])
	qml.RX(0.84, wires=[1])
	qml.RZ(0.53, wires=[0])
	qml.RZ(0.81, wires=[1])
	qml.CNOT(wires=[1, 2])
	qml.CNOT(wires=[0, 1])
	qml.RX(0.60, wires=[2])

	qml.RX(0.56, wires=[1])
	qml.RZ(0.98, wires=[2])
	qml.RZ(0.93, wires=[1])
	qml.CNOT(wires=[2, 3])
	qml.CNOT(wires=[1, 2])
	qml.RX(0.34, wires=[3])

	qml.RX(0.21, wires=[2])
	qml.RZ(1.20, wires=[3])
	qml.RZ(8.7e-2, wires=[2])
	qml.CNOT(wires=[3, 4])
	qml.CNOT(wires=[2, 3])
	qml.RX(0.90, wires=[4])

	qml.RX(-0.18, wires=[3])
	qml.RZ(0.49, wires=[4])
	qml.RZ(0.83, wires=[3])
	qml.CNOT(wires=[3, 4])

	qml.RX(0.72, wires=[4])
	qml.RZ(87, wires=[4])

	for i in range(num_wires):
		output.append(qml.expval(qml.PauliZ(i)))

	return output

print(circuit())