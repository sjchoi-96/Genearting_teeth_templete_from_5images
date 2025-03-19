# Smartee project: Model-based 3D Teeth Reconstruction from Five Intra-oral Orthodontic Photos

## preprocessing

Please see cpdGp_align_ssm.py, ssm_utils.py, gp_non_rigid_registration.py

## Usage

1） To train a teeth boundary segmentation model:

1-1） Put your train and validation data into the folders in ./seg/train and ./seg/valid respectively

1-2） Train a model with default settings, Run "python -m seg.run_train"

Note: The labeled teeth boundary is dilated during training and evaluation to serve as the real label. It is because the manually labelel teeth boundary is too thin and not highly accurate for edge detection. The dilation process is controlled by a factor named EXPANSION_RATE in ./seg/seg_const.py

Attention: the provided teeth boundary segmentation model is not accurate and a precise teeth boundary is important for the 3D following teeth reconstruction.

2） To run teeth reconstrution demo: "python main.py"

3） To visualize the projection of teeth reconstruction into input photo: "python visualization.py"


## Overview
Based on the work of Wu. et al. [1], we develop a template-based framework leveraging the prior shape knowledge of human teeth to reconstruct digital 3D models of upper and lower teeth from the typical five orthodontic intra-oral photographs. The framework consists of three phases: parameterization of the arrangement and shape of teeth through statistical shape modelling, U-net based teeth boundary extraction in intra-oral images, and 3D teeth reconstruction based on the prior parametric teeth model.
<p align="center">
    <img src=".\demo\assets\teeth_reconstruction_framework.png" alt="teeth reconstruction framework" width="800"/>
</p>

## Reconstruction result

Maxillary view |  Mandibular view | Left view | Right view | Anterior view
:----:|:----:|:----:|:----:|:----:
<img src=".\seg\valid\image\1-0.png" alt="orthodontic photo: maxillary view" width="100"/>|<img src=".\seg\valid\image\1-1.png" alt="orthodontic photo: mandibular view" width="100"/>|<img src=".\seg\valid\image\1-2.png" alt="orthodontic photo: left view" width="100"/>|<img src=".\seg\valid\image\1-3.png" alt="orthodontic photo: right view" width="100"/>|<img src=".\seg\valid\image\1-4.png" alt="orthodontic photo: anterior view" width="100"/>
<img src=".\demo\visualization\mesh-tag=1-PHOTO.UPPER.png" alt="reconstructed teeth: maxillary view" width="100"/>|<img src=".\demo\visualization\mesh-tag=1-PHOTO.LOWER.png" alt="reconstructed teeth: mandibular view" width="100"/>|<img src=".\demo\visualization\mesh-tag=1-PHOTO.LEFT.png" alt="reconstructed teeth: left view" width="100"/>|<img src=".\demo\visualization\mesh-tag=1-PHOTO.RIGHT.png" alt="reconstructed teeth: right view" width="100"/>|<img src=".\demo\visualization\mesh-tag=1-PHOTO.FRONTAL.png" alt="reconstructed teeth: anterior view" width="100"/>
<img src=".\demo\visualization\overlay-tag=1-PHOTO.UPPER.png" alt="projection: maxillary view" width="100"/>|<img src=".\demo\visualization\overlay-tag=1-PHOTO.LOWER.png" alt="projection teeth: mandibular view" width="100"/>|<img src=".\demo\visualization\overlay-tag=1-PHOTO.LEFT.png" alt="projection teeth: left view" width="100"/>|<img src=".\demo\visualization\overlay-tag=1-PHOTO.RIGHT.png" alt="projection teeth: right view" width="100"/>|<img src=".\demo\visualization\overlay-tag=1-PHOTO.FRONTAL.png" alt="projection teeth: anterior view" width="100"/>


## Requirements
python 3.8.10
absl-py==2.1.0
aiosignal==1.3.1
asttokens==3.0.0
astunparse==1.6.3
attrs==25.3.0
backcall==0.2.0
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
clang==5.0
click==8.0.4
colorama==0.4.6
comm==0.2.2
ConfigArgParse==1.7
cycler==0.12.1
cycpd==0.25
dash==2.10.2
dash-core-components==2.0.0
dash-html-components==2.0.0
dash-table==5.0.0
decorator==5.2.1
distlib==0.3.9
executing==2.2.0
fastjsonschema==2.21.1
filelock==3.16.1
Flask==2.2.5
flatbuffers==25.2.10
fonttools==4.56.0
frozenlist==1.5.0
gast==0.4.0
google-auth==2.38.0
google-auth-oauthlib==1.0.0
google-pasta==0.2.0
grpcio>=1.48.2
h5py==3.1.0
idna==3.10
imageio==2.35.1
importlib_metadata==8.5.0
importlib_resources==6.4.5
ipython==8.12.3
ipywidgets==8.1.5
itsdangerous==2.2.0
jedi==0.19.2
Jinja2==3.1.6
joblib==1.4.2
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
jupyter_core==5.7.2
jupyterlab_widgets==3.0.13
keras==2.13.1
Keras-Preprocessing==1.1.2
kiwisolver==1.4.7
libclang==18.1.1
Markdown==3.7
MarkupSafe==2.1.5
matplotlib==3.5.3
matplotlib-inline==0.1.7
msgpack==1.1.0
narwhals==1.30.0
nbformat==5.5.0
networkx==3.1
numpy==1.24.3
oauthlib==3.2.2
objgraph==3.6.2
open3d==0.16.0
opencv-contrib-python==4.6.0.66
opencv-python==4.6.0.66
opt-einsum==3.3.0
packaging==24.2
pandas==1.4.3
parso==0.8.4
pickleshare==0.7.5
pillow==10.4.0
pkgutil_resolve_name==1.3.10
platformdirs==4.3.6
plotly==6.0.0
prompt_toolkit==3.0.50
protobuf==3.20.3
psutil==5.9.0
pure_eval==0.2.3
pyaml==25.1.0
pyasn1==0.6.1
pyasn1_modules==0.4.1
Pygments==2.19.1
pyparsing==3.1.4
python-dateutil==2.9.0.post0
pytz==2025.1
PyWavelets==1.4.1
pywin32==310
PyYAML==6.0.2
ray==2.3.0
referencing==0.35.1
requests==2.32.3
requests-oauthlib==2.0.0
rpds-py==0.20.1
rsa==4.9
scikit-image==0.19.3
scikit-learn==1.1.1
scikit-optimize==0.9.0
scipy==1.8.1
Shapely==1.8.5.post1
six==1.15.0
stack-data==0.6.3
tensorboard==2.13.0
tensorboard-data-server==0.7.2
tensorboard-plugin-wit==1.8.1
tensorflow==2.13.0
tensorflow-addons==0.16.1
tensorflow-estimator==2.13.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==1.1.0
threadpoolctl==3.5.0
tifffile==2023.7.10
traitlets==5.14.3
trimesh==3.15.5
typeguard==2.13.3
typing-extensions==3.7.4.3
urllib3==2.2.3
virtualenv==20.29.3
wcwidth==0.2.13
Werkzeug==2.2.3
wheel==0.45.1
widgetsnbextension==4.0.13
wrapt==1.12.1
zipp==3.20.2


## Reference

[1] Yizhou Chen, Shuojie Gao, Puxun Tu, and Xiaojun Chen, Automatic 3D Teeth Reconstruction from Five Intra-oral Photos Using Parametric Teeth Model, IEEE Transactions on Visualization and Computer Graphics, 2023, DOI: 10.1109/TVCG.2023.3277914

[2] Wu, C., Bradley, D., Garrido, P., Zollhöfer, M., Theobalt, C., Gross, M. H., & Beeler, T. (2016). Model-based teeth reconstruction. ACM Trans. Graph., 35(6), 220-1.
# Genearting_teeth_templete_from_5images
