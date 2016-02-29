(function (ng) {
    var mod = ng.module('independentsModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('independentsService', ['$http', 'independentsContext', function ($http, context) {

        this.getIndependents = function () {
            return $http({
                method: 'GET',
                url: '/independents'
            });
        };

        this.registerIndependent = function (data) {
            return $http({
                method: 'POST',
                url: '/register',
                data:data
            });
        };

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: '/jobs'
            });
        };

    }]);
})(window.angular);