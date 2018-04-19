import numpy as np
import heapq
from sklearn import preprocessing
import glob
import os
import subprocess

def music():
    arr = np.load(r"/Users/janelabumanglag/FYP/models/research/audioset/samples/index.npy")
    f = open(r"/Users/janelabumanglag/FYP/models/research/audioset/samples/filenames.txt", 'r')
    names = []
    for line in f:
        names.append(line)

    wav_file_recent = glob.glob('/Users/janelabumanglag/FYP/models/research/audioset/static/*.wav')
    latest_file = max(wav_file_recent, key=os.path.getctime)

    subprocess.call(["python","vggish_inference_demo.py","--wav_file",latest_file])

    npy_file_recent = glob.glob('/Users/janelabumanglag/FYP/models/research/audioset/static/*.wav.npy')
    npy_file = max(npy_file_recent, key=os.path.getctime)

    query = np.load(npy_file)
    l2Query = preprocessing.normalize(query, norm='l2', axis=1)
    sumQuery = np.sum(l2Query, axis=0)
    newQuery = np.array(sumQuery)[None, :]
    finalQuery = preprocessing.normalize(newQuery, norm='l2', axis=1)

    dot_positive = np.dot(arr, finalQuery.T)

    top5 = heapq.nlargest(5, range(len(dot_positive)), dot_positive.__getitem__)
    list_vids = []
    for i in top5:
        s = names[i]
        list_vids.append(s)

    print(list_vids)
    return list_vids

music()