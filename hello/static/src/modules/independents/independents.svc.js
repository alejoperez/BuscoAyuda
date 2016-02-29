(function (ng) {
    var mod = ng.module('independentsModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('independentsService', ['$http', 'independentsContext', function ($http, context) {

        this.getIndependents = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/independents'
                //url: 'http://127.0.0.1:8000/independents'
            });
        };

        this.registerIndependent = function (data) {
            return $http({
                method: 'POST',
                url: 'https://ancient-plains-90032.herokuapp.com/register',
                //url: 'http://127.0.0.1:8000/register',
                data:data
            });
        };

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/jobs'
                //url: 'http://127.0.0.1:8000/jobs'
            });
        };

    }]);
})(window.angular);