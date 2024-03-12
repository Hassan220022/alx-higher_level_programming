#include <Python.h>

void print_python_list(PyObject *p)
{
	long int size, i;

	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

void print_python_bytes(PyObject *p)
{
	long int size, i;

	char *trying_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	trying_str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%s", trying_str[i], i + 1 < size + 1 && i + 1 < 10 ? " " : "\n");
}
