
check:
	bash scripts/system_check.sh

search_extensions:
	python python_scripts/search_for_extensions.py

list_files_menu:
	python python_scripts/list_files_menu.py

install_python:
	bash scripts/setup_python3_9.sh

update_repo:
	git pull origin main

install_pip_requirements:
	python -m pip install -r requirements.txt

complete_setup:
	bash scripts/setup_python3_9.sh
	bash scripts/install_docker.sh
	bash scripts/install_aws.sh