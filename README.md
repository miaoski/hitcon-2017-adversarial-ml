Adversarial Machine Learning - HITCON 2017
==========================================

This repo stores the source code and experiments done for a talk in HITCON Pacific 2017, Adversarial Machine Learning and Countermeasures, by miaoski and ch0upi.

*N.B.* Severeal repos are forked from people's works (see `LICENSE`).  We don't have copyright on these repos.  They are added in this repo merely for the sake of conveniences.  Without the contribution of the respective authors, we could never accomplish the research.  We are greateful and would like to say "Thank you!"

We also used the docker image built by https://hub.docker.com/r/born2data/caffecv/  It is not included in this repo, but we really appreciated it!


Directories
-----------

* ./binary/ : fooling machine-leraning based anti-virus products
* ./neural-nets-are-weird/ : Panda or not panda? Gradient ascent. Forked from https://github.com/jvns/neural-nets-are-weird
* ./neural-nets-are-weird/notebooks/experimental_attack_images : Please manually download it from https://iotsecurity.eecs.umich.edu/#roadsigns
* ./keras/ : Cheating traffic signs recognition and facial recognition
* ./keras/CarND-Traffic-Sign-Classifier-P2 : forked from https://github.com/tomaszkacmajor/CarND-Traffic-Sign-Classifier-P2


References
==========

* 1412.1897 Deep Neural Networks are Easily Fooled.pdf
* 1607.02533v3 Adversarial Examples in the Physical World.pdf
* 1707.08945 Robust Physical-World Attacks on Deep Learning Models.pdf
* Adversarial Machine Learning for AV software.pdf
* parkhi15.pdf


LICENSE
=======
* Our code: MIT License.
* https://github.com/jvns/neural-nets-are-weird Not sure, confirming with Julia Evans.
* https://github.com/tomaszkacmajor/CarND-Traffic-Sign-Classifier-P2 Not sure, confirming with @tomaszkacmajor.
* https://github.com/rcmalli/keras-vggface MIT License by Refik Can Malli.
* GoogLeNet in Keras is adopted from https://gist.github.com/joelouismarino/a2ede9ab3928f999575423b9887abd14 by Joe Marino
* vgg_face_demo.ipynb is forked from https://aboveintelligent.com/face-recognition-with-keras-and-opencv-2baf2a83b799 by m.zaradzki
