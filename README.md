# WebLdap
WebLdap is a webapp tool for creating open ldap user accounts.


# About WebLdap
WebLdap is a prototype and should not be used in production.

The ideal use, if production ready, is within an organization's intranet.

# Setup
Install Python3

````
git clone https://github.com/AndyMtz04/WebLdap.git
````
```` 
pip install -r requirements
````

Start a django project

Add WebLdap to django project settings

Migrate models

Add ldap server credentials to ldap_accounts.py

Start django webserver

# Todo

Create a login for admins only