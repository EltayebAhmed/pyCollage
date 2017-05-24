from subprocess import Popen
from os import path
from os import getcwd
pdf_reader_path = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

chart = "class_flow_chart"
builder = Popen(["dot", ("%s.dot" % chart), "-O", "-Tpdf"])
builder.communicate()
pdf_reader = Popen([pdf_reader_path, path.join(getcwd(), "%s.dot.pdf" % chart)])
pdf_reader.communicate()