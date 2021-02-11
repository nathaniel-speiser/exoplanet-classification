#This file contains redundant functions with Model testing.ipynb, but I wrote it to work better with my end of project workflow,
#which was in another notebook (Final Model tuning), and exclusively uses XGBoost

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, \
                             RandomForestClassifier, StackingClassifier
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb

from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV, KFold
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, \
                            recall_score, roc_auc_score, roc_curve, classification_report
""""""
def plot_roc_curve(classifier, df , features, target='disposition_num', xgb = True, title=''):
    """
    Plot ROC curve and output ROC_AUC metric for an sklearn or XGBoost model on a validation set

    Args:
    classifier: sklearn model or something that similar that can be used by cross_validate
    df: pandas dataframe that contains all training/validation data
    features: list of strings representing the columns in df to use as features
    target: string for name of column to use as target (y)
    xgb: Use True if model is an XGBoost classifier - passes fit with extra parameters to ensure fast fitting
    """
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .25, random_state=1)

    if xgb:
        eval_set = [(X_test, y_test)]
        classifier.fit(
                        X_train, y_train,
                        eval_set=eval_set,
                        eval_metric='error',
                        early_stopping_rounds=50,
                        verbose=False)
    else: classifier.fit(X_train, y_train)

    fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])

    plt.figure(dpi=150)
    plt.plot(fpr, tpr,lw=2)
    plt.plot([0,1],[0,1],c='violet',ls='--')
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title(title +' ROC curve')

    print("ROC AUC score = ", roc_auc_score(y_test, classifier.predict_proba(X_test)[:,1]))
    plt.show()


def plot_confusion_matrix(classifier, df, features, target='disposition_num', xgb = True, title=''):
    """
    Print classification report and graph confusion matrix for an sklearn or XGBoost model on a
    validation set

    Args:
    classifier: sklearn model or something that similar that can be used by cross_validate
    df: pandas dataframe that contains all training/validation data
    features: list of strings representing the columns in df to use as features
    target: string for name of column to use as target (y)
    xgb: Use True if model is an XGBoost classifier - passes fit with extra parameters to ensure fast fitting
    """
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .25, random_state=1)
    if xgb:
        eval_set = [(X_test, y_test)]
        classifier.fit( X_train, y_train,
                        eval_set=eval_set,
                        eval_metric='error',
                        early_stopping_rounds=50,
                        verbose=False)
    else: classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print(classification_report(y_test,y_pred, target_names=['Not a Candidate', 'Candidate']))

    plt.figure(dpi=150)
    cm = confusion_matrix(y_test, y_pred)
    cm=np.rot90(cm, k=2)
    plt.figure(dpi=150)
    annot = [[1,1],[1,1]]
    annot[0][0] = str(cm[0,0])+'\nTP'
    annot[0][1] = str(cm[0,1])+'\nFN'
    annot[1][0] = str(cm[1,0])+'\nFP'
    annot[1][1] = str(cm[1,1])+'\nTN'
    sns.heatmap(cm, cmap = plt.cm.Blues, annot=annot, fmt = '', square=True,cbar = False,
               xticklabels=['Candidate','Not Candidate'],
               yticklabels=['Candidate','Not Candidate'])
    plt.yticks(va='center')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title+' confusion matrix')
    plt.show()

def xgb_test_model_CV(classifier, df, features, target='disposition_num', preprocessor = None):
    """
    Report cross validation results for an XGBoost model across several metrics

    Args:
    classifier: sklearn model or something that similar that can be used by cross_validate
    df: pandas dataframe that contains all training/validation data
    features: list of strings representing the columns in df to use as features
    target: string for name of column to use as target (y)
    preprocessor: Object implementing sklearn fit_transform signature for transforming data before fitting (StandardScaler, PolynomialFeatures, etc.)

    """
    X = np.array(df[features])
    y = np.array(df[target])
    if preprocessor:
        X = preprocessor.fit_transform(X)
    accuracies = []
    recalls = []
    precisions = []
    f1s =[]
    roc_aucs= []

    kf = KFold(n_splits=4, shuffle=True)
    for train_index, val_index in kf.split(X):
        X_train, X_val = X[train_index], X[val_index]
        y_train, y_val = y[train_index], y[val_index]

        eval_set=[(X_train,y_train),(X_val,y_val)]
        fit_model = classifier.fit(
                        X_train, y_train,
                        eval_set=eval_set,
                        eval_metric='error',
                        early_stopping_rounds=50,
                        verbose=False
                        )
        y_pred = classifier.predict(X_val)

        accuracies.append(accuracy_score(y_val, y_pred))
        recalls.append(recall_score(y_val, y_pred))
        precisions.append(precision_score(y_val, y_pred))
        f1s.append(f1_score(y_val, y_pred))
        roc_aucs.append(roc_auc_score(y_val, classifier.predict_proba(X_val)[:,1]))
    print('Mean validation accuracy: {:.3f}'.format(np.mean(accuracies)))
    print('Mean validation recall  : {:.3f}'.format(np.mean(recalls)))
    print('Mean validation precision: {:.3f}'.format(np.mean(precisions)))
    print('Mean validation f1  : {:.3f}'.format(np.mean(f1s)))
    print('Mean validation roc_auc: {:.3f}'.format(np.mean(roc_aucs)))
