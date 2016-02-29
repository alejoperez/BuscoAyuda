(function (ng) {
    var mod = ng.module('profileModule');

    mod.service('profileService', ['$http', 'profileContext', function ($http, context) {

        this.editProfile = function (independent) {
            return $http({
                method: 'POST',
                url: '/profile',
                data:{
                    name: independent.fields.name,
                    last_name: independent.fields.lastName,
                    experience: independent.fields.yearsOfExperience,
                    phone_number: independent.fields.phoneNumber,
                    email: independent.fields.email,
                    image:  independent.fields.imageFileUrl,
                    job:  independent.fields.job

                }
            });
        };

        this.getProfile = function () {
            return $http({
                method: 'GET',
                url: '/profile'
            });
        }

        this.getJobs = function () {
            return $http({
                method: 'GET',
                url: '/jobs'
            });
        };

    }]);
})(window.angular);