# step no 1
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
# step no 2
hours_studied = [2.5,1.5,3.0,1.8,4.0,2.0,3.5,2.7]
prev_exam_score = [80,70,75,60,85,80,90,65]
exam_outcome = ['Pass','Fail','Pass','fail','Pass', 'Pass','Pass','Fail']
# step no 3
label_encoder = LabelEncoder()
encoded_exam_outcome = label_encoder.fit_transform(exam_outcom)
# step no 4
x = np.column_stack((hours_studied, prev_exam_score))
y = encoded_exam_outcome
# step no 5
clf = MLPClassifier(hidden_layer_sizes=(4,),activation ='logistic', max_iter = 1000,random_state = 42)
clf.fit(x,y)
# step mo 6
new_student_data = np.array([[2.0,78]]) #hours studied and previous exam score
# step no 7
predicted_outcome = clf.predict(new_student_data)
# step no 8
predicted_outcome_decode = label_encoder.inverse_transform(predicted_outcome)
# step no 9
print("Predicted Exam Outcome for the new student : {}".format(predicted_outcome_decode[0]))
