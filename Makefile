build:
	pip install -r requirements.txt

up-normal:
	python src/start.py NM 10 cfc/cfquery cfc/cf74 cfc/cf75 cfc/cf76 cfc/cf77 cfc/cf78 cfc/cf79

up-otimizado:
	python src/start.py OTM 10 cfc/cfquery cfc/cf74 cfc/cf75 cfc/cf76 cfc/cf77 cfc/cf78 cfc/cf79
