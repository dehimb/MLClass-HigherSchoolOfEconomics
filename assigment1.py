from __future__ import division
import pandas
import re
from collections import Counter


def main():
    data = pandas.read_csv('titanic.csv', index_col='PassengerId')
    print(question6(data))


def question1(data):
    return data['Sex'].value_counts()


def question2(data):
    return round(data['Survived'].value_counts()[1] / len(data) * 100, 2)


def question3(data):
    return round(data['Pclass'].value_counts()[1] / len(data) * 100, 2)


def question4(data):
    return str(round(data['Age'].mean(), 2)) + ' ' + str(round(data['Age'].median(), 2))


def question5(data):
    return round(data['SibSp'].corr(data['Parch']), 2)


def question6(data):
    names = []
    full_names = data.loc[data['Sex'] == 'female']['Name']
    for index, name in full_names.iteritems():
        names.append(re.sub('\)', '', name.rsplit(' ', 1)[-1]))
    return Counter(names).most_common(1)[0][0]

if __name__ == "__main__":
    main()
