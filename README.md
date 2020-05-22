## Deploy your dash app to Heroku in 5 steps :rocket:

### 1. Fork this repository 

### 2. [Create a free Heroku account](https://signup.heroku.com/)

### 3. [Generate an API key on your account settings](https://dashboard.heroku.com/account)
While this key does not have a hard-coded expiration date, it will expire whenever your account password changes

### 4. [Create an encrypted secret for your repo](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository). 
:warning: **IMPORTANT** Set the name of the secret to `HEROKU_API`. 

### 5. Edit following sections in the GitHub Actions configuration (`.github/workflows/deploy.yml`)

```          
        heroku_app_name: "name_of_your_deployment"
        heroku_email: "email_address_of_your_heroku_account"

```
