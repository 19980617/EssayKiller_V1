# -*- coding: gbk -*-

# Original work Copyright 2018 The Google AI Language Team Authors.
# Modified work Copyright 2019 Rowan Zellers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# ����Ŀ������ѧ���뽻����;��������Դ���֣���ֹ�����κ���ҵ��;
# ʹ�ô��غõ�EssayKilelrBrain����ģ�鹹��pipeline���˵�������ı�
# ���ֺ��Ĵ����Ѽ��ܣ���Ҫ��ȡ�����汾�븽�ϸ���/�о���������֤��

from absl import app
from absl import flags
import collections
import tensorflow as tf
import sys
import requests
from utils import *
from AutoDetect.text_detection_video import *
from AutoFormatter.formatter import *
from AutoRecog.ocr import *
from AutoScorer.DNN_Scorer import *
from AutoWritter.scripts import *
from Essaykiller import AutoBrainBase

tf.logging.set_verbosity(tf.logging.ERROR)
tf.get_logger().setLevel('INFO')
tf.autograph.set_verbosity(1)

FLAGS = flags.FLAGS
flags.DEFINE_string('gpu', None, 'comma separated list of GPU(s) to use.')

result = []

class EssayKillerPipeline(AutoBrainBase):
	"""
	@params
	input_feed: text input_feed
	sequence_len: sequence length
	...
	
	Ϊ��ֹ�Զ���EK��ܱ��˶�����ע�����û򸴿̣�pipeline���Ĵ����빹�����ݲ���Դ
	����ѧ����Ҫ������ϸ��˻������ѧ����������������ʼ���deanyuton@gmail.com
	���ݳ�����Ϣ���ҽ��ᷢ��������Ĵ�����������ݵ����������䡣лл���
	"""
	def __init__():
		self.config = FLAGS.config
		pass 

	def enable_visiondetect():
		'''
		������Ƶ��⣬��Ӳ������˻�ȡ��Ƶ���ļ�
		Ӳ�����ã�Logitech C930C
		@params:video��Ƶ������˿�
		...
		'''
		pass

	def generage_char_from_videostream():
		pass 

	def extract_topic_sentence():
		pass 

	def essay_writter_core():
		pass

	def scoring_to_best_essay():
		pass 

	def formatting_essay_to_exam():
		pass


		
def main(argv):
    del argv
    if FLAGS.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu
    else:
        print('Please assign GPUs.')
        exit()

print("test sample in trained model...")
if __name__ == "__main__":
	try:
		pass
	except:
		print("pipeline has failed...")
	#dicts = result[0].split(":")
	#plexity = result.get['ppl']
	print("the final ppl score is: \n",scores )
	print("the final text output as :", text)
	print(sum(result))
