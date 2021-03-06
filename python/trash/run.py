#!/usr/bin/python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import caffe
import os
import sys

MODEL_FILE = '/home/praveen/deep-learning/caffe/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '/home/praveen/deep-learning/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
MEAN_FILE = '/home/praveen/deep-learning/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy'
IMAGE_FILE = '/home/praveen/deep-learning/caffe/examples/images/15.jpg'
#IMAGE_FILE = sys.argv[1]

#print(IMAGE_FILE)
LABEL_FILE = '/home/praveen/deep-learning/caffe/data/ilsvrc12/destfile.txt'

net = caffe.Classifier(MODEL_FILE, PRETRAINED,mean=np.load(MEAN_FILE).mean(1).mean(1),channel_swap=(2,1,0),raw_scale=255, image_dims=(256, 256))

input_image = caffe.io.load_image(IMAGE_FILE)

plt.imshow(input_image)
plt.savefig('/home/praveen/deep-learning/caffe/outputs/15.png')
plt.close()

opf = open("output.txt", "w")

prediction = net.predict([input_image])
#print prediction.shape
#print 'prediction shape:', prediction[0].shape[0]
#print 'predicted class:', prediction[0].argmax()

count=0
for scores in prediction[0]:
	#print count, scores
	
	count=count+1 
	if scores > 0.01:
		 opf.write("%s, %s\n" %(scores, count))
		 for i in range(scores):
			sorted(scores)
			print count, scores
		

print 'predicted class:', prediction[0].argmax()
f = open('/home/praveen/deep-learning/caffe/data/ilsvrc12/det_synset_words.txt')
labels = f.readlines()
#print 'predicted name:', labels[0],
opf.close()

plt.plot(prediction[0])
#plt.plot(scores[0])
plt.savefig('/home/praveen/deep-learning/caffe/prediction.png')
#plt.savefig('/home/praveen/deep-learning/caffe/score.png')

mydic = {}
with open("sample.txt", 'r') as f:
	for line in f:
		splitline = line.split()
		mydic[(splitline[0])] = ",".join(splitline[1:])
		

