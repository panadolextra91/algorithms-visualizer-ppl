ANTLR_JAR=server/antlr4-4.9.2-complete.jar
GRAMMAR=server/grammar/AlgoDSL.g4
OUT_DIR=server/parser

.PHONY: generate clean

generate:
	@mkdir -p $(OUT_DIR)
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -o $(OUT_DIR) $(GRAMMAR)

clean:
	rm -rf $(OUT_DIR)



