# import pickle
# import sys
# sys.path.append("../tools/")
# from feature_format import featureFormat, targetFeatureSplit
#
# data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )
#
# ### first element is our labels, any added elements are predictor
# ### features. Keep this the same for the mini-project, but you'll
# ### have a different feature list when you do the final project.
# features_list = ["poi", "salary"]
#
# data = featureFormat(data_dict, features_list)
# labels, features = targetFeatureSplit(data)