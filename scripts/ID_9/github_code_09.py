import torch.nn as nn
import torch.nn.functional as F

"""
Source: https://github.com/lonePatient/TorchBlocks/blob/445140f8190a037b590d3344cdbd6cae5b850da0/src/torchblocks/losses/triplet_loss.py
"""

DISTANCE2METRIC = {'cosine': lambda x, y: 1 - F.cosine_similarity(x, y),
                   'educlidean': lambda x, y: F.pairwise_distance(x, y, p=2),
                   'manhattan': lambda x, y: F.pairwise_distance(x, y, p=1)}


class TripletLoss(nn.Module):
    def __init__(self, margin=1.0, distance_metric='educlidean', average=True):
        super(TripletLoss, self).__init__()
        self.margin = margin
        self.average = average
        self.distance_metric = DISTANCE2METRIC[distance_metric]

    def forward(self, anchor, positive, negative):
        distance_positive = self.distance_metric(anchor, positive)
        distance_negative = self.distance_metric(anchor, negative)

        ## Inserted Code

        return (distance_positive - distance_negative) + self.margin

        ## Inserted Code

        losses = F.relu(
            (distance_positive - distance_negative) + self.margin
        )
        return losses.mean() if self.average else losses.sum()
