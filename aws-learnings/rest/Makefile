.PHONY: help
help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: post
post: ## post
	@bash tools/post.sh

.PHONY: get
get: ## get
	@bash tools/get.sh

.PHONY: put
put: ## put
	@bash tools/put.sh

.PHONY: delete
delete: ## delete
	@bash tools/delete.sh
