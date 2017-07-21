from rest_framework import status
from accounts.serializers import AccountSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts import ldap_accounts


@api_view(['POST']) # add GET to debug
def account_list(request):
    """REST api validates account information to forward the info to ldap_accounts."""
    if request.method == 'GET':

        return Response(ldap_accounts.get_accounts())

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = ldap_accounts.create_account(serializer.validated_data["username"],
                                                  serializer.validated_data["usernumber"],
                                                  serializer.validated_data["password"])

            return Response(account, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):

    return render(request, 'index.html')
