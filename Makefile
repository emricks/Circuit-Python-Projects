default:
	cp code.py /Volumes/CIRCUITPY

serial:
	cp serial-example.py /Volumes/CIRCUITPY/code.py

wifi:
	cp wifi-example.py /Volumes/CIRCUITPY/code.py
	cp animate_functions.py /Volumes/CIRCUITPY/lib
	rm -rf /Volumes/CIRCUITPY/html
	cp -r html /Volumes/CIRCUITPY
