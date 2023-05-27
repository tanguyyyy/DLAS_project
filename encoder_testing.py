import torch
from torch import nn
from encoder.model import SpeakerEncoder

#model = torch.jit.load('encoder/encoder_test.pt')
#model.eval()

#model = torch.load('encoder/encoder_test.pt')
#print(model.keys())
#SpeakerEncoder(nn.Module)

#model = nn.Module()
#model.load_state_dict(torch.load('encoder/encoder_test.pt'))
#model.eval()

_device=None

weights_fpath='saved_models/dev/encoder.pt'

_model = SpeakerEncoder(_device, torch.device("cpu"))
checkpoint = torch.load(weights_fpath, _device)
_model.load_state_dict(checkpoint["model_state"])
_model.eval()