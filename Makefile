init:
	pip install -r requirements.txt

create_db:
	python src/create.py

insert:
	python src/insert.py

select:
	python src/selects.py

update:
	python src/update.py

delete:
	python src/delete.py

change_feeds:
	python src/changefeeds.py

.PHONY: 
	clean-pyc clean-build