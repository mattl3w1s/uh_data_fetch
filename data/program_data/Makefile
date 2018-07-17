FILE = '../program_links.csv'
SLUGS = $(shell csvcut -c3 -d'|' $(FILE))

all: $(SLUGS:=.html)

clean:
	for f in $(SLUGS:=.html); do rm $$f; done

$(SLUGS:=.html):
	python ../../processors/jsget.py -o $@ $$(python ../../processors/get_url_by_filename.py \
	$(patsubst %.html,%,$@))