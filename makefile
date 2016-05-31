TESTDIR=tests
DOCDIR=docs
SPHINX_API=sphinx-apidoc --no-toc --force -o $(DOCDIR)/api

all: doc

test:
	cd $(TESTDIR) && py.test

doc:
	$(SPHINX_API) hqgreek
	$(SPHINX_API) hqvocab
	cd $(DOCDIR) && make html

clean:
	rm -r $(DOCDIR)/api
	rm -r $(DOCDIR)/_build

.PHONY: all, test, doc, clean
