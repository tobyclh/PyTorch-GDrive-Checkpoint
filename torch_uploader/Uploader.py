import torch
from pathlib import Path
import subprocess

class CheckpointManager:
    is_init = False
    folder = Path('.')
    local_checkpoints = []
    cloud_checkpoints = []
    keep_n = 0
    @classmethod
    def init(cls, folder, keep_n=10):
        folder = Path(folder)
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
        CheckpointManager.folder = folder
        CheckpointManager.is_init = True
        CheckpointManager.keep_n = keep_n

    @classmethod
    def torchsave(cls, obj, f):
        assert CheckpointManager.is_init, 'Must call init before saving'
        filename = Path(str(f))
        if filename.parent != CheckpointManager.folder:
            filename = CheckpointManager.folder / filename
        if not filename.parent.exists():
            filename.parent.mkdir(parents=True, exist_ok=True)
        torch.save(obj, filename)
        CheckpointManager._cleanup(filename)
        
    @classmethod
    def _upload(cls, new_checkpoint):
        return

    @classmethod
    def _cleanup(cls, new_checkpoint):
        CheckpointManager.local_checkpoints.append(new_checkpoint)
        # delete the local file
        while len(CheckpointManager.local_checkpoints) > CheckpointManager.keep_n:
            filename = CheckpointManager.local_checkpoints.pop()
            filename.unlink()
        return

def upload_folder(path, parent_id):
    subprocess.check_call(['./utils/upload_folder.sh', str(path), str(parent_id)])
    return

if __name__ == '__main__':
    CheckpointManager.init('result/banana')
    CheckpointManager.torchsave({'sdfa':123}, 'ducker/123.pt')

