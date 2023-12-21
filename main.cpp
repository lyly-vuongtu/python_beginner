#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(my_module, m) {
    m.def("add", &add, "Add two numbers");
}