(function (ng) {
    var mod = ng.module('independentsModule');

    mod.controller('independentsCtrl', ['$scope', 'independentsService', '$window', function ($scope, independentsService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.getIndependents = function () {
            return independentsService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };

        this.registerIndependent = function(){
            return independentsService.registerIndependent({
                'name':angular.element('#name').val(),
                'lastName':angular.element('#last_name').val(),
                'job':angular.element('#job').val(),
                'yearsOfExperience':angular.element('#years_of_experience').val(),
                'phoneNumber':angular.element('#phone_number').val(),
                'email':angular.element('#email').val(),
                'imageFileUrl':angular.element('#imageFileUrl').val(),
                'username':angular.element('#username').val(),
                'password':angular.element('#password').val()
            }).then(function (response) {
                $window.location.href = '/#/independents';
            }, responseError);
        };

        this.getJobs = function () {
            return independentsService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
