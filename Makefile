UHD_programs_URL = 'http://catalog.uhd.edu/content.php?catoid=7&navoid=559'
GENERATED_FILES = data/UHD_programs_page.html data/program_links.csv program_data

all: $(GENERATED_FILES)

install:
	python3.6 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt;

clean:
	cd data && rm program_links.csv && rm UHD_programs_page.html
	cd data/program_data && $(MAKE) clean

program_data:
	cd data/program_data && $(MAKE)

data/program_links.csv: data/UHD_programs_page.html
	source env/bin/activate; \
	cat $< | python processors/extract_program_links.py > $@

data/UHD_programs_page.html:
	source env/bin/activate; \
	python processors/jsget.py $(UHD_programs_URL) > $@

