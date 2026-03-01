.PHONY: verify verify-repeat verify-tvs verify-pinned verify-precedence verify-imports cli-smoke feature-gate feature-gate-live vendor-scan vendor-scan-sync protection-audit release-check release-receipt cut-release

verify:
	python3 conformance/verify_conformance.py

verify-repeat:
	python3 conformance/verify_conformance.py > /tmp/aaa_verify_run1.txt
	python3 conformance/verify_conformance.py > /tmp/aaa_verify_run2.txt
	diff -u /tmp/aaa_verify_run1.txt /tmp/aaa_verify_run2.txt

verify-tvs:
	python3 spec/verify_test_vectors.py

verify-pinned:
	python3 spec/verify_pinned_artifacts.py

verify-precedence:
	@python3 -c "\
	import json, sys; \
	sys.path.insert(0, '.'); \
	from aaa_eal.core import EAL_PRECEDENCE; \
	pinned = json.load(open('spec/failure/failure_precedence_v1.json'))['precedence']; \
	ok = list(EAL_PRECEDENCE) == pinned; \
	print('PASS' if ok else 'FAIL: EAL_PRECEDENCE != pinned artifact'); \
	sys.exit(0 if ok else 1)"

verify-imports:
	python3 spec/verify_kernel_imports.py

cli-smoke:
	./eal verify-receipt --help >/dev/null
	./eal revalidate --help >/dev/null
	./eal compat --help >/dev/null

feature-gate:
	python3 conformance/verify_vendor_feature_gates.py

feature-gate-live:
	python3 conformance/verify_vendor_feature_gates.py --live-check --require-codex

vendor-scan:
	python3 conformance/collect_vendor_surface_evidence.py

vendor-scan-sync:
	python3 conformance/collect_vendor_surface_evidence.py --update-gate
	python3 conformance/verify_vendor_feature_gates.py

protection-audit:
	./scripts/audit_branch_protection.sh main

release-check:
	$(MAKE) verify
	$(MAKE) verify-repeat
	$(MAKE) verify-tvs
	$(MAKE) verify-pinned
	$(MAKE) verify-precedence
	$(MAKE) verify-imports
	$(MAKE) feature-gate
	$(MAKE) protection-audit

release-receipt:
	@test -n "$(TAG)" || (echo "Usage: make release-receipt TAG=vX.Y.Z" >&2; exit 1)
	./scripts/verify_release_receipt.sh "$(TAG)"

cut-release:
	@test -n "$(VERSION)" || (echo "Usage: make cut-release VERSION=vX.Y.Z" >&2; exit 1)
	./scripts/cut_release.sh "$(VERSION)"
