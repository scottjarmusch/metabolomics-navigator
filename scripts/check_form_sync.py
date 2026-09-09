#!/usr/bin/env python
from __future__ import annotations

import sys
from pathlib import Path
import yaml
from common import ROOT, load_vocab, label_maps

CHECKS={
 ROOT/'.github/ISSUE_TEMPLATE/submit-tool.yml':{
  'resource-types':'resource_types','primary-function':'functions','secondary-functions':'functions',
  'platforms':'platforms','interfaces':'interfaces','access-model':'access_models','submitter-role':'submission_roles'},
 ROOT/'.github/ISSUE_TEMPLATE/submit-strategy.yml':{
  'platforms':'platforms','objective':'strategy_objectives','role':'strategy_submission_roles',
  'analysis-types':'analysis_types','components':'strategy_components','sample-types':'sample_types','biological-contexts':'biological_contexts'}
}

def main():
    labels=label_maps(load_vocab()); failed=False
    for form_path, expected_fields in CHECKS.items():
        form=yaml.safe_load(form_path.read_text(encoding='utf-8'))
        body={item.get('id'):item for item in form.get('body',[]) if item.get('id')}
        for field_id,vocab_key in expected_fields.items():
            actual=body[field_id]['attributes']['options']; expected=list(labels[vocab_key].values())
            if actual!=expected:
                failed=True
                print(f'ERROR: {form_path.name}:{field_id} options differ from controlled vocabulary')
                print('  expected:',expected); print('  actual:  ',actual)
    if failed: return 1
    print('Tool and strategy submission forms match the controlled vocabulary.')
    return 0

if __name__=='__main__': sys.exit(main())
