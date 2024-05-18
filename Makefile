gen_dataset:
	cd planimetrics_tasks_generator/math_tasks_generator && poetry run python generator.py || true && cd -

train:
	cd planimetrics_tasks_generator/model && poetry run python main.py || true && cd -

run:
	cd planimetrics_tasks_generator && poetry run python main.py || cd -
