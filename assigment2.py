import pandas
from sklearn.tree import DecisionTreeClassifier


def main():
    all_data = pandas.read_csv('titanic.csv', index_col='PassengerId')
    data = all_data[['Survived', 'Pclass', 'Fare', 'Age', 'Sex']] \
        .dropna() \
        .replace({"male": 1, 'female': 0})
    clf = DecisionTreeClassifier()
    clf.fit(data[['Pclass', 'Fare', 'Age', 'Sex']], data['Survived'])
    print(clf.feature_importances_)

if __name__ == "__main__":
    main()
