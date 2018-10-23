/**
 * Angular JavaScript that controls the user interface interactions .
 * @module App module
 * @author Santiago Flores Kanter <sfloresk@cisco.com>
 * @copyright Copyright (c) 2018 Cisco and/or its affiliates.
 * @license Cisco Sample Code License, Version 1.0
 */

/**
 * @license
 * Copyright (c) 2018 Cisco and/or its affiliates.
 *
 * This software is licensed to you under the terms of the Cisco Sample
 * Code License, Version 1.0 (the "License"). You may obtain a copy of the
 * License at
 *
 *                https://developer.cisco.com/docs/licenses
 *
 * All use of the material herein must be in accordance with the terms of
 * the License. All rights not expressly granted by the License are
 * reserved. Unless required by applicable law or agreed to separately in
 * writing, software distributed under the License is distributed on an "AS
 * IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */
var appModule = angular.module('appModule',['ngRoute','ngAnimate'])

/*  Configuration    */

// Application routing
appModule.config(function($routeProvider, $locationProvider){
    // Maps the URLs to the templates located in the server
    $routeProvider
        .when('/', {templateUrl: 'ng/home'})
        .when('/home', {templateUrl: 'ng/home'})
        .when('/l3vpn-new', {templateUrl: 'ng/l3vpn-new'})
        .when('/l3vpn-list', {templateUrl: 'ng/l3vpn-list'})
        .when('/l3vpn-detail/:serviceName', {templateUrl: 'ng/l3vpn-detail'})

    $locationProvider.html5Mode(true);
});

// To avoid conflicts with other template tools such as Jinja2, all between {a a} will be managed by Angular instead of {{ }}
appModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);


/*  Controllers    */

// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope, $routeParams){

    // Variables initialization
    $scope.error = "";
    $scope.success = "";
    $scope.loading = false;
    $scope.service = {};
    $scope.service.devices = [];
    $scope.devices = [];
    $scope.allowedInteraces = [{name: "GigabitEthernet 0/0/0/0", id: "0/0/0/0"},{name: "GigabitEthernet 0/0/0/1", id: "0/0/0/1"},{name: "GigabitEthernet 0/0/0/2", id: "0/0/0/2"},{name: "GigabitEthernet 0/0/0/3",id: "0/0/0/3"}]
    $scope.l3vpnServices = [];


    // Functions
    $scope.go = function ( path ) {
        $location.path( path );
    };

    $scope.clearError = function(){
        $scope.error = "";
    };

    $scope.clearSuccess = function(){
        $scope.success = "";
    };

    $scope.getL3vpnServices = function(){

        $scope.loading = true;
        // Does a GET call to api/services/l3vpn to get l3vpn service list
        $http
            .get('api/services/l3vpn')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.l3vpnServices variable
                $scope.l3vpnServices = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };

    $scope.getL3vpnServices();

    $scope.showL3vpnDetails = function(pservice){
        $scope.service = pservice
        $scope.go("l3vpn-detail/" + pservice.name);
    }


    $scope.newL3vpnService = function(){
        $scope.service = {};
        $scope.go('l3vpn-new');
    }

    $scope.deployL3vpnService = function(){
        $scope.loading = true;

        $http
            .post('api/services/l3vpn', $scope.service)
            .then(function (response, status, headers, config){
                $scope.success = "Servicio implementado exitosamente";
                $scope.go('l3vpn-list');
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
                $scope.getL3vpnServices();
            })
    };
    $scope.deleteL3vpnService = function(){
        $scope.loading = true;

        $http
            .delete('api/services/l3vpn/' + $routeParams.serviceName)
            .then(function (response, status, headers, config){
                $scope.success = "Servicio removido"
                $scope.go("l3vpn-list");
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message;

            })
            .finally(function(){
                $scope.loading = false;
                // After the deployment is done, refresh the EPGs/VLANs items
                $scope.getL3vpnServices();
            })
    };

    $scope.getDevices = function(){

        // Does a GET call to api/devices to get a device list
        $http
            .get('api/device')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.devices variable
                $scope.devices = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };
    $scope.getDevices();

    $scope.loadAllowedParameters = function(device){
        $scope.allowedInputQoS = [];
        $scope.allowedOutputQoS = [];
        if(device["config"]["tailf-ned-cisco-ios-xr:policy-map"]){
            for (var i = 0; i < device["config"]["tailf-ned-cisco-ios-xr:policy-map"].length; i++) {
                if (device["config"]["tailf-ned-cisco-ios-xr:policy-map"][i]["name"].includes("PARENT-IN")){
                    $scope.allowedInputQoS.push(device["config"]["tailf-ned-cisco-ios-xr:policy-map"][i])
                }
                else if (device["config"]["tailf-ned-cisco-ios-xr:policy-map"][i]["name"].includes("PARENT-OUT")){
                    $scope.allowedOutputQoS.push(device["config"]["tailf-ned-cisco-ios-xr:policy-map"][i])
                }
            }
        }
    };
});
