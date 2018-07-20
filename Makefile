UH_programs_URL = 'http://publications.uh.edu/content.php?catoid=21&navoid=5494'
GENERATED_FILES = data/UHD_programs_page.html data/program_links.csv program_data

all: $(GENERATED_FILES)

install:
	python3.6 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt;

clean:
	cd data && rm program_links.csv && rm UHD_programs_page.html
	cd data/program_data && $(MAKE) clean

program_data: data/program_links.csv
	cd data/program_data && $(MAKE)

data/program_links.csv: data/UHD_programs_page.html
	source env/bin/activate; \
	cat $< | python processors/extract_program_links.py > $@

data/UHD_programs_page.html:
	source env/bin/activate; \
	python processors/jsget.py $(UH_programs_URL) > $@

