import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torchvision import models
import matplotlib.pyplot as plt
import io
from PIL import Image

def get_prediction(image):
    #load the model
    model = models.resnet18(pretrained = True)
    original_class_len = model.fc.in_features
    model.fc = nn.Linear(original_class_len, 4)

    checkpoint = torch.load("statedict20")
    model.load_state_dict(checkpoint)
    model.eval()

    #prep the image
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean = [0.485, 0.456, 0.406],
            std = [0.229, 0.224, 0.225])
    ])

    img = Image.open(image)
    tensor = transform(img)
    tensor = tensor.unsqueeze(0)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)

    class_labels ={
    0 : 'Alligator Cracking', 
    1 : 'Good Condition',
    2 : 'Longitudinal Cracking', 
    3 : 'Pothole'}

    return y_hat, class_labels[y_hat.item()], outputs


