from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from cifar_exp_config import ResNet32Config


def get_config(dataset, model):
  if model == "resnet-50":
    return ResNet50Config()
  elif model == "resnet-101":
    return ResNet101Config()
  else:
    raise Exception("Unknown model")
  pass


class ResNet50Config(ResNet32Config):

  def __init__(self):
    super(ResNet50Config, self).__init__()
    self.batch_size = 256
    self.height = 224
    self.width = 224
    self.num_residual_units = [3, 4, 6, 3]  # ResNet-50
    self.strides = [1, 2, 2, 2]
    self.activate_before_residual = [True, False, False, False]
    self.init_stride = 2
    self.init_max_pool = True
    self.init_filter = 7
    self.use_bottleneck = True
    self.filters = [64, 64, 128, 256, 512]
    self.wd = 0.0001
    self.momentum = 0.9
    self.base_learn_rate = 1e-1
    self.max_train_iter = 600000
    self.lr_decay_steps = [160000, 320000, 480000]
    self.lr_list = [1e-2, 1e-3, 1e-4]
    self.model = "resnet-50"
    self.disp_iter = 10
    self.save_iter = 5000
    self.trainval_iter = 1000
    self.valid_iter = 5000
    self.valid_batch_size = 64  ### Use this if necessary.
    self.div255 = True
    self.run_validation = False
    self.num_classes = 1000


class ResNet101Config(ResNet50Config):

  def __init__(self):
    super(ResNet101Config, self).__init__()
    self.num_residual_units = [3, 4, 23, 3]  # ResNet-101
    self.batch_size = 256
