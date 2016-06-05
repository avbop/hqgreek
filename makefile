TESTDIR=tests
DOCDIR=docs
WEBDIR=web
JSONDIR=$(WEBDIR)/data
SPHINX_API=sphinx-apidoc --no-toc --force -o $(DOCDIR)/api
TMPDIR=/tmp/hqgreek
REPO_URL=git@github.com:avbop/hqgreek.git

all: doc json
travis: test doc json

test:
	cd $(TESTDIR) && py.test

doc:
	$(SPHINX_API) hqgreek
	$(SPHINX_API) hqvocab
	cd $(DOCDIR) && make html
	cp -r $(DOCDIR)/_build/html $(WEBDIR)/docs

json:
	mkdir -p $(JSONDIR)
	python3 generate_website_data.py $(JSONDIR)

site: doc json
	mkdir $(TMPDIR)
	cd $(TMPDIR) && git clone -b gh-pages $(REPO_URL)
	cd $(TMPDIR)/hqgreek && git rm -rf * && git commit -m "Clearing gh-pages via makefile."
	cp -r $(WEBDIR)/. $(TMPDIR)/hqgreek
	cp -r $(DOCDIR)/_build/html $(TMPDIR)/hqgreek/docs
	cd $(TMPDIR)/hqgreek && git add .
	cd $(TMPDIR)/hqgreek && git commit -m "Updating site via makefile."
	cd $(TMPDIR)/hqgreek && git push -u origin gh-pages
	rm -rf $(TMPDIR)
	git pull

server: json doc
	cd $(WEBDIR) && python3 -m http.server 8080

clean:
	rm -r $(DOCDIR)/api
	rm -r $(DOCDIR)/_build
	rm -r $(JSONDIR)

.PHONY: all, test, doc, clean, travis, json, server
.IGNORE: clean
