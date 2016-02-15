(function (ng) {

    var helpApp = ng.module('helpApp', [
        'ngRoute',
        'independentsModule',
        'profileModule',
        'mainModule',
        'loginModule'
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
            .when('/login', {
                templateUrl: 'static/src/modules/login/login.tpl.html',
                controller: 'loginCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/independents');



    }]);
})(window.angular);
