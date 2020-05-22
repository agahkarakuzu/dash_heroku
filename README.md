## Deploy your dash app to Heroku in 5 steps :rocket:

### 1. Fork this repository 

### 2. [Create a free Heroku account](https://signup.heroku.com/)

### 3. [Generate an API key on your account settings](https://dashboard.heroku.com/account)

### 4. [Create an encrypted secret for your repo](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository) with the name `HEROKU_API. 

### 5. Do the following changes in the GitHub Actions configuration (`.github/workflows/deploy.yml`)

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

## That's it! 

Check the `Actions` tab of your repository, if the run is successful, your app will be available at:

https://your-app-name.herokuapp.com

You can simply modify `app.py` to contain your dash app. Each time you push a commit to the `master`, action will be triggered to deploy the new version. 

Note: Do not push commits to `master` one after another too frequently, it may break the deployment. 
