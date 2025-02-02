### Definition
`venv` is a module in Python that provides support for creating lightweight "virtual environments", each with its own independent set of Python packages. This isolation allows developers to manage dependencies for different projects effectively without conflicts.

### Functionalities
- **Create a Virtual Environment**
	- `python -m venv path_to_new_virtual_environment`
	- This command uses `-m` to run `venv` as a module, which then creates a new virtual environment in the specified directory. Commonly, developers use `env` or `.venv` as the directory name.
- **Activate Virtual Environment**
    - **Windows:** `path_to_venv\Scripts\activate.bat`
    - **macOS/Linux:** `source path_to_venv/bin/activate`
    - Activation changes your shell’s environment to use the Python and pip executables from within the venv.
- **Deactivate Virtual Environment**
    - `deactivate`
    - This command stops the use of the active virtual environment, reverting to the system’s default Python interpreter.
- **Install Packages in a Virtual Environment**
    - Once activated, use `pip install package_name` to install packages that will be local to the virtual environment, not the global Python installation.
- **List Installed Packages with [[pip]]**
    - `pip list` 
    - Lists all packages installed in the currently active virtual environment.

#### Tags
#python #venv #virtual-environments #development-tools