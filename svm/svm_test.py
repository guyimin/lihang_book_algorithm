# encoding=utf-8
# @Author: WenDesi
# @Date:   12-11-16
# @Email:  wendesi@foxmail.com
# @Last modified by:   WenDesi
# @Last modified time: 13-11-16

import time
import csv
import random
import logging

from sklearn.metrics import accuracy_score
from generate_dataset import *
from svm import SVM
from sklearn import svm


if __name__ == "__main__":


    writer = csv.writer(file('svm_vs_svm.csv', 'ab'))

    # for i in xrange(10):
    #     print 'competition now in lap %d' % i

    my_svm1 = SVM()
    my_svm2 = SVM(kernel='poly')

    his_svm1 = svm.SVC(kernel='linear')
    his_svm2 = svm.SVC(kernel='poly')

    train_features, train_labels, test_features, test_labels = generate_dataset(2000,visualization=False)

    my_svm1.train(train_features,train_labels)
    my_svm2.train(train_features,train_labels)
    his_svm1.fit(train_features,train_labels)
    his_svm2.fit(train_features,train_labels)

    result = []

    predict = my_svm1.predict(test_features)
    score=accuracy_score(test_labels,predict)
    result.append(score)

    predict = my_svm2.predict(test_features)
    score=accuracy_score(test_labels,predict)
    result.append(score)

    predict = his_svm1.predict(test_features)
    score=accuracy_score(test_labels,predict)
    result.append(score)

    predict = his_svm2.predict(test_features)
    score=accuracy_score(test_labels,predict)
    result.append(score)

    writer.writerow(result)
