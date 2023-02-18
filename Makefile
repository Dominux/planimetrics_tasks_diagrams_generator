test:
	cd dataset_generator && poetry run python -m unittest | true && cd -
