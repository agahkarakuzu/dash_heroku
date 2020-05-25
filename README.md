## Deploy your `Plotly-Dash` app to Heroku in 5 steps :rocket:

### 1. Fork this repository 

### 2. [Create a free Heroku account](https://signup.heroku.com/)

### 3. [Generate an API key on your account settings](https://dashboard.heroku.com/account)

### 4. [Create an encrypted secret for your repo](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository) with the name `HEROKU_API` and value from step-3

### 5. Do the following changes in the [GitHub Actions configuration](/.github/workflows/deploy.md):

```diff          
 name: Deploy

 on:
   push:
     branches:
-      - none
+      - master

 jobs:
   build:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v2
       - uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
         with:
           heroku_api_key: ${{secrets.HEROKU_API}}
-          heroku_app_name: "dash-brainhack"
+          heroku_app_name: "your-app-name"
-          heroku_email: "agahkarakuzu@gmail.com"
+          heroku_email: "your-heroku-email@xyz.com" 
```

| :exclamation:  **Warning**|
|---------------------------------------|
Your `heroku_app_name` must be a unique name. If there exists a herokuapp with that name, the deployment will fail. You can check for availability [here](https://dashboard.heroku.com/new-app). 

## That's it! 

Check the `Actions` tab of your repository, if the run is successful, your app will be available at:

https://your-app-name.herokuapp.com

Each time you push a commit to the `master`, action will be triggered to deploy the new version. 

| :exclamation:  **Warning**|
|---------------------------------------|
Do not push commits to `master` one after another too frequently, it may break the deployment. 

## How to develop and debug your Dash app? 

Assuming that you have a the [`datvis36` conda environment](https://github.com/agahkarakuzu/datavis_edu#3--create-a-new-conda-environment), you can follow these steps: 

1. Clone your (forked) repository to your computer

```
git clone https://github.com/your-github-handle/dash_heroku.git
```

2. Activate `datvis36` environment and navigate into the `dash_heroku`

```
source activate datvis36
cd /dash_heroku
```

3. Make sure that you've completed the first 5 steps to configure your deployment. 

4. Modify your project as you like. Assuming that the `app.py` is your main entrypoint calling the `app.run_server(debug=True)` method, run the following in your terminal:

```
python app.py
```

This will start a local `development server` and your application will be accessible through an IP address (something like `http://127.0.0.1:8050/`) from your web browser. 

It'll give you the following warning:

```
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
```

but don't worry, this is exactly what we are doing with [`gunicorn`](https://gunicorn.org/), [`Heroku`](https://www.heroku.com/) and [`GitHub Actions`](https://github.com/marketplace/actions/deploy-to-heroku) :) 

Each time you change `app.py` (or `whatever_entry_point.py`) and save the script, the Dashboard will update itself in `debug` mode. This is really useful to trace errors if your app crashes after your changes. 

5. When you are ready to push your changes

```
git add .
git commit -m "Commit message" 
git push
```

If your push refers to `master`, `Github Actions` will be triggered and deploy the latest version of your app to Heroku! 

| :point_up: **Please use GitHub Actions fairly**|
|--------------------------------------------------|
It is not only a bad development practice to modify your `app.py` on GitHub editor and see if it works on production (https://your-app-name.herokuapp.com) each time you commit, but also a wasteful use of public compute resources.

| ⏱ **Heroku gives you 550hrs per month for free**|
|----------------------------------------------------|
Quite generous, is not it! When your app does not receive web traffic for 30 minutes, it sleeps. If a sleeping web dyno receives web traffic, it will become active again after a short delay. Free web dynos do not consume free dyno hours while sleeping 🎉. You can find further details about free dyno hours [here](https://devcenter.heroku.com/articles/free-dyno-hours).

## Multi-page Dash apps are possible! 

[Real-time fMRI dashboard](https://github.com/jsheunis/rtfmri-methods-dash) by @jsheunis is a great example. If a single page is not enough for your purpose, you can use the structure of this project as a reference. 

In rtfmri repo, `pages` is a module (simply a directory that contains `__init.py__`) that contains individual Dash apps to be displayed on separate pages. These pages are accessed from a front page, which is defined by `index.py` script placed at the root of the repository. This script serves as a main entry point, in which `app.run_server()` call is made. Sub-pages do not call this function, but just describe their `layout` and `callbacks`. They are imported into the `index.py`: 

```python
from pages import home, page1, page2, page3, page4
```

You can inspect the rest of the [`index.py`](https://github.com/jsheunis/rtfmri-methods-dash/blob/master/index.py) to grasp how to handle multi-page layouts. 

*** 

Note that the differences in  [`Procfile`](https://devcenter.heroku.com/articles/procfile): here, it contains `web: gunicorn app:server`. Whereas on the rtfmri repo it contains `web: gunicorn index:server`.

The `Procfile` configuration is depends on where we make the following call:

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

In our repo, this call is made in `app.py`, whereas in rtfmri it is in `index.py`. Bottomline, if you'd like to create a multi-page dash application pay attention to this detail before you let GitHub actions deploy your application.

***

## More examples to be inspired by

[More examples](https://github.com/plotly/dash-sample-apps/tree/master/apps) are available by Plotly Dash, including a [brain viewer](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-brain-viewer).
