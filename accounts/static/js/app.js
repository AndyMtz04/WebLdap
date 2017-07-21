var app = angular.module("app", ['ngResource']);

app.controller("test", test);

app.config(function ($interpolateProvider, $httpProvider, $resourceProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

});


function test($scope, $http) {
    var currentDate = new Date;
    $scope.timeString = currentDate.toTimeString();

    $scope.submitData = function() {

        $http({method: 'POST', url: '/account/', data: {'username': $scope.userName, 'usernumber': $scope.userNumber, 'password': $scope.passWord}}).
        then(function(response) {
            $scope.status = response.status;
            $scope.data = response.data;
        }, function(response) {
            $scope.data = response.data || 'Request failed';
            $scope.status = response.status;
            $scope.info = "This user exists!"
        }).then(function() {
            $scope.method = 'GET';
            $scope.url = '/account/';
            $scope.response = null;

        $http({method: $scope.method, url: $scope.url}).
            then(function(response) {
                $scope.status = response.status;
                $scope.data = response.data;
            }, function(response) {
                $scope.data = response.data || 'Request failed';
                $scope.status = response.status;
            });

        });
        $scope.userName = null
        $scope.userNumber = null
        $scope.passWord = null
    }


 //create a service for the stuff below
 //can possibly delete, only need POST
    $scope.method = 'GET';
    $scope.url = '/account/';
    $scope.response = null;

    $http({method: $scope.method, url: $scope.url}).
        then(function(response) {
            $scope.status = response.status;
            $scope.data = response.data;
        }, function(response) {
            $scope.data = response.data || 'Request failed';
            $scope.status = response.status;

        });

}