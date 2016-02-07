(function (ng) {

    var helpApp = ng.module('helpApp', [
        'ngRoute',
        'independentsModule'
    ]);

    helpApp.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/independents', {
                templateUrl: 'templates/polls/src/modules/independents/independents.tpl.html',
                controller: 'independentsCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/independents');



    }]);
})(window.angular);
