(function (ng) {

    var helpApp = ng.module('helpApp', [
        'ngRoute',
        'independentsModule',
        'profileModule'
    ]);

    helpApp.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/independents', {
                templateUrl: 'static/src/modules/independents/independents.tpl.html',
                controller: 'independentsCtrl',
                controllerAs: 'ctrl'
            })
            .when('/profile', {
                templateUrl: 'static/src/modules/profile/profile.tpl.html',
                controller: 'profileCtrl',
                controllerAs: 'ctrl'
            })
            .when('/register', {
                templateUrl: 'static/src/modules/independents/registration.tpl.html',
                controller: 'independentsCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/independents');



    }]);
})(window.angular);
