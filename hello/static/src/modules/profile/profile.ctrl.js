(function (ng) {
    var mod = ng.module('profileModule');

    mod.controller('profileCtrl', ['$scope', 'profileService', function ($scope, profileService) {

        function responseError(response) {
            console.log(response);
        }

        this.editProfile = function () {
            return profileService.editProfile().then(function (response) {
                //TODO: Show success
            }, responseError);
        };

        this.getJobs = function () {
            return profileService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
