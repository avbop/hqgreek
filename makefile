TESTDIR=tests
DOCDIR=docs
SPHINX_API=sphinx-apidoc --no-toc --force -o $(DOCDIR)/api
TMPDIR=/tmp/hqgreek
REPO_URL=git@github.com:avbop/hqgreek.git

all: doc site
travis: test doc

test:
	cd $(TESTDIR) && py.test

doc:
	$(SPHINX_API) hqgreek
	$(SPHINX_API) hqvocab
	cd $(DOCDIR) && make html

site: doc
	mkdir $(TMPDIR)
	cd $(TMPDIR) && git clone -b gh-pages $(REPO_URL)
	cp -r docs/_build/html/* $(TMPDIR)/hqgreek
	cd $(TMPDIR)/hqgreek && git add .
	cd $(TMPDIR)/hqgreek && git commit -m "Updating site via makefile."
	cd $(TMPDIR)/hqgreek && git push -u origin gh-pages
	rm -rf $(TMPDIR)

clean:
	rm -r $(DOCDIR)/api
	rm -r $(DOCDIR)/_build

.PHONY: all, test, doc, clean, travis
