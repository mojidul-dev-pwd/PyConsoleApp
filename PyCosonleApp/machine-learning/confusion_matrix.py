import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9, size=1000)
predicted = numpy.random.binomial(1,.9, size=1000)

Accuracy = metrics.accuracy_score(actual, predicted)
print('Accuracy',Accuracy)
Precision = metrics.precision_score(actual, predicted)
print('Precision',Precision)
Sensitivity_recall = metrics.recall_score(actual, predicted)
print('Sensitivity_recall',Sensitivity_recall)
#Opposite of recall
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
print('Specificity',Specificity)
#F-score
#2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
F1_score = metrics.f1_score(actual, predicted)
print('F1_score',F1_score)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0,1])

cm_display.plot()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

"""
True Negative (Top-Left Quadrant)
False Positive (Top-Right Quadrant)
False Negative (Bottom-Left Quadrant)
True Positive (Bottom-Right Quadrant)
"""
