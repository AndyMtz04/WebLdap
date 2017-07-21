import ldap3

# ldap server must exist for this script and webapp to work

# set the credentials
LDAP_URI = ''
OU = ''
DC_1 = ''
DC_2 = ''
LDAP_ADMIN = ''
ADMIN_PASSWORD = ''


server = ldap3.Server(LDAP_URI, get_info=ldap3.ALL)

conn = ldap3.Connection(server, 'cn={0},dc={1},dc={2}'.format(LDAP_ADMIN, DC_1, DC_2), ADMIN_PASSWORD, auto_bind=True)


def create_account(username, user_number, user_password):
    """Function creates the openldap user accounts."""
    uid = username
    uid_number = user_number
    password = user_password

    dn = 'uid={0},ou={1},dc={2},dc={3}'.format(uid, OU, DC_1, DC_2)
    conn.add(dn, attributes={'objectClass': ['top', 'account', 'posixAccount', 'shadowAccount'],
                             'uidNumber': uid_number,
                             'gidNumber': '100',
                             'homeDirectory': '/home/{}'.format(uid),
                             'loginShell': '/bin/bash',
                             'cn': uid,
                             'userPassword': '{crypt}x'})
    conn.modify(dn, {'userPassword': [(ldap3.MODIFY_REPLACE, [password])]})

    return conn.result


def get_accounts():
    """For debugging purposes"""
    conn.search('ou={0},dc={1},dc={2}'.format(OU, DC_1, DC_2),
                '(objectClass=posixAccount)',
                ldap3.LEVEL, attributes=['uidNumber'])

    return conn.response


def delete_account(username):
    """For debugging purposes"""
    conn.delete('uid={0},ou={1},dc={2},dc={3}'.format(username, OU, DC_1, DC_2))

    return conn.result
