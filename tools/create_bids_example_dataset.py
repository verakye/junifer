from tempfile import TemporaryDirectory
from pathlib import Path

import datalad.api as dl

dst = 'https://gin.g-node.org/juaml/datalad-example-bids'


with TemporaryDirectory() as tmpdir_name:
    tmpdir = Path(tmpdir_name)
    ds = dl.create(tmpdir)

    base_dir = tmpdir / 'example_bids'
    base_dir.mkdir()

    for i_sub in range(1, 10):
        t_sub = f'sub-{i_sub:02d}'
        sub_dir = base_dir / t_sub
        sub_dir.mkdir()

        for dname in ['anat', 'func']:
            (sub_dir / dname).mkdir()

        fnames = [f'anat/{t_sub}_T1w.nii.gz',
                  f'func/{t_sub}_task-rest_bold.nii.gz',
                  f'func/{t_sub}_task-rest_bold.json']
        for fname in fnames:
            with open(sub_dir / fname, 'w') as f:
                f.write('placeholder')

    dl.save(recursive=True)