# PyTorch-GDrive-Checkpoint

A really simply checkpoint managing device to automatically remove.
This uses Pathlib that comes with Python 3.4+

```
import CheckpointManager as CM
# save all checkpoint under result_dir, upload the checkpoints to google drive (free for education), keep only the last n in local, 
CM.init('result_dir', 'gdrive_folder_id', keep_n=10) 
CM.torchsave(state_dict, 'name.pt') #save like how you normally would do with torch
```