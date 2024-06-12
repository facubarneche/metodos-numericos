# TP METODOS NUMERICOS

El proyecto contiene 1 ejecutable, tp-minimos-y-regresion.ipynb contiene el respectivo codigo sobre el trabajo practico.

# Integrantes

* Andres Hernandez
* Facundo Barneche

# Como ejecutar el proyecto

En caso de no contar con alguna de estas tecnologias se dejan los comandos para seguir y ejecutar el proyecto.
En caso contrario, se puede ejecutar el código por parte o entero.

# Step 1: Update Your System

Before you begin the installation process, it’s important to make sure your Ubuntu system is up to date. You can do this by running the following command in your terminal:

sudo apt-get update

This will update your package list and ensure that you have the latest versions of all the software on your system.

# Step 2: Install Python

Jupyter Notebook is written in Python, so you’ll need to have Python installed on your system before you can install Jupyter. To install Python, run the following command:

sudo apt-get install python3

This will install Python 3, which is the latest version of Python.

# Step 3: Install pip

pip is a package manager for Python that allows you to easily install and manage Python packages. To install pip, run the following command:

sudo apt-get install python3-pip

This will install pip for Python 3.

# Step 4: Install Jupyter Notebook

Now that you have Python and pip installed, you can use pip to install Jupyter Notebook. Run the following command:

sudo pip3 install jupyter

This will install Jupyter Notebook and all its dependencies.

# Step 5: Launch Jupyter Notebook

To launch Jupyter Notebook, run the following command in your terminal:

jupyter notebook

# Posible errores

<pre>
ModuleNotFoundError Traceback (most recent call last) File ~\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pandas\compat_optional.py:135, in import_optional_dependency(name, extra, errors, min_version) 134 try: --> 135 module = importlib.import_module(name) 136 except ImportError
</pre>

pip install openpyxl