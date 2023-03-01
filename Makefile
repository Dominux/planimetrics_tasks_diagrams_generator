gen_dataset:
	cd planimetrics_tasks_generator/math_tasks_generator && poetry run python generator.py || true && cd -
