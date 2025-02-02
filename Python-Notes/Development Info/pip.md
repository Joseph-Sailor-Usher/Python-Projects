### Definition
`pip` is Python's official package manager, primarily used to install and manage software packages from the Python Package Index (PyPI).

### Functionalities
- **Install Packages**
	`pip install package_name`
- **Upgrade Packages** 
	`pip install --upgrade package_name` 
- **Uninstall Packages**
	`pip uninstall package_name`.
- **Manage Requirements**
	`pip install -r requirements.txt`.
- **List and Freeze Packages**
	`pip list` shows installed packages
	`pip freeze` outputs them in a format useful for creating `requirements.txt`
	`pip freeze < requirements.txt` creates or updates `requirements.txt` with the current environment's package list.

#### Tags
#python #pip #tools #package-management