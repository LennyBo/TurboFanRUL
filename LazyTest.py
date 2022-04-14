from lazypredict.Supervised import LazyClassifier

from Preprocessing import getData

x_train,x_val,x_test,y_train,y_val,y_test = getData()

clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(x_train, x_test, y_train, y_test)

print(models)