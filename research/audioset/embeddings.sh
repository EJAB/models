#!/bin/bash

cd samples

for i in *.wav
do
python ../vggish_inference_demo.py --wav_file $i
done
