

#ifndef PYREPEATFINDER_H
#define PYREPEATFINDER_H

static PyObject * python_input(PyObject *self, PyObject *args);

static PyMethodDef PyRepeatFinderMethods[] = {
    {"find_repeats", python_input, METH_VARARGS, "Python interface for C++ repeat finder for DNA sequences"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef PyRepeatFinderModule = {
    PyModuleDef_HEAD_INIT,
    "find_repeats",
    "Python for a C++ repeat finder to find repeats in DNA sequences",
    -1,
    PyRepeatFinderMethods
};

#endif //PYREPEATFINDER_H
