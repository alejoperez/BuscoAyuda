(function (ng) {
    var mod = ng.module('profileModule');

    mod.service('profileService', ['$http', 'profileContext', function ($http, context) {

        this.editProfile = function () {
            return $http({
                method: 'POST',
                url: 'https://ancient-plains-90032.herokuapp.com/profile',
                //url: 'http://127.0.0.1:8000/profile',
                data:{

                }
            });
        };

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: 'https://ancient-plains-90032.herokuapp.com/profile'
                //url: 'http://127.0.0.1:8000/jobs'
            });
        };

    }]);
})(window.angular);