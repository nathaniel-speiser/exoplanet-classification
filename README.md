# Classifying Observations from the Kepler Space Telescope


## Description

This project aimed to classify objects of interest catalogued by the Kepler Space Telescope as a Candidate exoplanet or as a False Positive (i.e. an observation that caught the telescopes attention, but was not an exoplanet). For more information on exoplanets and the Kepler Space Telescope, see the [NASA page](https://www.nasa.gov/mission_pages/kepler/overview/index.html) and [Wikipedia entry](https://en.wikipedia.org/wiki/Kepler_space_telescope) on the topic. In short, the goal of this project was to emulate the step in the planet search/verification process wherein a team of scientists decided if an observation should move forward and be verified through other means (such as a ground based telescope).

A wide variety of models were tested, but ultimately an XGBoost classifier was used as it gave the best overall performance, with a focus on recall, out of all the models tested. This project focused on recall because it would be better to have to comb through a few extra false positives than miss a potential major discovery (such as a potentially habitable, Earth-like exoplanet). After all, grad students' time is cheap.

The final model achieved a recall of 91% on a held-out test set and an accuracy of 89%. The metric it actually performs best on is ROC area under the curve, with a score of 96%. These scores together suggest the model is fairly good at identifying candidate exoplanets and is especially good at separating the two classes, evidenced by the high ROC AUC score.

To explore the data and the results, I have created a [Tableau dashboard](https://public.tableau.com/views/Keplertelescopevisualization/Dashboard1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link) that shows the location of the observations in space and some of their important properties.

## Data

The data used in the project was downloaded directly from the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative). The table contains roughly 10,000 objects of interest that were reviewed by scientists, more than 2000 of which have gone on to be verified as exoplanets, with verification still pending on another 2500 or so. The table contains fit parameters from fits of the light curves of stars as planets potentially pass in front of them. These fit parameters are properties of the planet, star, and transit, as well as the size of the error on those fits for many of those features. The table also contains categorical and other information that was not relevant to the fitting process.

## Tools

* pandas
* numpy
* scikit-learn
* XGBoost
* matplotlib
* seaborn
* ipywidgets (highly recommended for EDA!)


## Impacts

It should first be said that this model is *absolutely not a replacement for the planet verification process*. Given that it emulates human classification of exoplanet candidates fairly well, it could replace the human verification step of the planet finding process, though given the scienitfic importance of this work it may not be desireable to take humans out of the process completely. More realistically, it could be used to optimize the planet finding process. For missions where much more data is coming in and time is limited, it could be used to prioritize which observations are looked at by humans first, or to prioritize the order in which planets should be verified by ground telescopes or other methods.

## Future directions

A model based on the raw light curves would most likely be able to create more advanced features and perform better, though the signal processing that would be involved would much more complex than the work done in this project. The model could also incorporate features that humans use to classify the observations as exoplanet candidates (described in [this paper](https://arxiv.org/abs/1202.5852)) in order to perform better and/or be more interpretable.
