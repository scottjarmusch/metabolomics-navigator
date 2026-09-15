"""Build tool-entry history from committed changes, never inferred review events."""
import subprocess
from common import ROOT


def history_for(slug):
    path = f'content/tools/{slug}.yml'
    try:
        result = subprocess.run(
            ['git', 'log', '--format=%H%x09%cs%x09%s', '--', path],
            cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=True)
        shallow = subprocess.run(['git','rev-parse','--is-shallow-repository'],
            cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip() == 'true'
    except (OSError, subprocess.CalledProcessError):
        return {'events': [], 'complete': False}
    events = []
    for line in result.stdout.splitlines():
        fields = line.split('\t', 2)
        if len(fields) == 3:
            sha, date, summary = fields
            events.append({'sha':sha, 'date':date, 'summary':summary})
    # A shallow checkout must not label its oldest available commit as the original.
    for index, event in enumerate(events):
        event['kind'] = 'First committed entry' if not shallow and index == len(events)-1 else 'Entry update'
    return {'events':events, 'complete':not shallow}
