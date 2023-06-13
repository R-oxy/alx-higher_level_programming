#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t list_len = PyList_Size(p);
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %zd\n", list_len);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (Py_ssize_t i = 0; i < list_len; ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *item_type = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, item_type);
    }
}
