ANTLR_JAR=server/antlr4-4.9.2-complete.jar
ANTLR_URL=https://www.antlr.org/download/antlr-4.9.2-complete.jar
GRAMMAR=server/grammar/AlgoDSL.g4
OUT_DIR=server/parser

.PHONY: generate clean download-antlr

generate:
	@# Check if Java is available
	@if ! command -v java >/dev/null 2>&1; then \
		echo "Warning: Java is not installed. Skipping parser generation."; \
		echo "Parser files are already generated and committed, so this is optional."; \
		exit 0; \
	fi
	@# Check if ANTLR jar exists, if not try to download it
	@if [ ! -f $(ANTLR_JAR) ]; then \
		echo "ANTLR jar not found. Attempting to download..."; \
		if command -v curl >/dev/null 2>&1; then \
			curl -L -o $(ANTLR_JAR) $(ANTLR_URL) || { \
				echo "Warning: Failed to download ANTLR jar."; \
				echo "Parser files are already generated and committed, so this is optional."; \
				exit 0; \
			}; \
		else \
			echo "Warning: curl not available. Cannot download ANTLR jar."; \
			echo "Parser files are already generated and committed, so this is optional."; \
			exit 0; \
		fi; \
	fi
	@mkdir -p $(OUT_DIR)
	@echo "Generating ANTLR parser files..."
	@java -jar $(ANTLR_JAR) -Dlanguage=Python3 -o $(OUT_DIR) $(GRAMMAR) || { \
		echo "Warning: Parser generation failed."; \
		echo "Parser files are already generated and committed, so this is optional."; \
		exit 0; \
	}
	@echo "Parser generation complete."

download-antlr:
	@if [ ! -f $(ANTLR_JAR) ]; then \
		if command -v curl >/dev/null 2>&1; then \
			echo "Downloading ANTLR 4.9.2..."; \
			curl -L -o $(ANTLR_JAR) $(ANTLR_URL); \
			echo "Download complete."; \
		else \
			echo "Error: curl is required to download ANTLR jar."; \
			exit 1; \
		fi; \
	else \
		echo "ANTLR jar already exists."; \
	fi

clean:
	rm -rf $(OUT_DIR)
	@echo "Note: ANTLR jar file preserved. Run 'rm $(ANTLR_JAR)' to remove it."



