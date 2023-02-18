test:
	cd dataset_generator && poetry run python -m unittest || true && cd -

gen_dataset:
	cd dataset_generator && poetry run python math_tasks_generator/generator.py || true && cd -
