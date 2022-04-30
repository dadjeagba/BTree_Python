PROJECT=Project Btree
AUTHOR= Aissatou Ibrahima Diallo ,AGBA Pascal Sébastien
SOURCES=Btree.py Node.py
FULL_SOURCES=$(addprefix src/, $(SOURCES))

define execute-command
$(1)

endef

.PHONY: clean doc archive author test

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__
	rm -rf $(DOC)
	rm -f $(PROJECT).zip
	rm -f conf.py-e
	rm -f */*.pyc
	rm -rf .DS_Store

doc: author
	mkdocs build

archive: $(PROJECT).zip

$(PROJECT).zip: 
	rm -f $@
	zip -r $@ . -x "sol/*" -x "site/*" -x "*~" -x "*.pyc" -x "*.DS_Store" -x "*__MACOSX/*" -x "*__pycache__/*" -x ".git/*" -x "enonce*"

test:
	@$(foreach file, $(FULL_SOURCES), $(call execute-command,python3 $(file)))
author:
	sed -i -e 's/^site_name:.*/site_name: "Module $(PROJECT)"/g' mkdocs.yml
	sed -i -e 's/^copyright:.*/copyright: "2021-2022, $(AUTHOR), Univ. Lille"/g' mkdocs.yml
	sed -i -e 's/^site_author:.*/site_author: "$(AUTHOR)"/g' mkdocs.yml
