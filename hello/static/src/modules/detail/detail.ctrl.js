(function (ng) {
    var mod = ng.module('detailModule');

    mod.controller('detailCtrl', ['$scope', 'detailService','$routeParams', function ($scope, detailService,$routeParams) {

        $scope.independent = {};
        $scope.success = '';

        function responseError(response) {
            console.log(response);
            this.success = 'ERROR';
        }

        this.editDetail = function () {
            return detailService.editDetail($scope.independent).then(function (response) {
                $scope.success = 'OK';
            }, responseError);
        };

        this.getInfo = function () {
            detailService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);

            detailService.getDetail($routeParams.idIndependent).then(function (response) {
                console.log(response.data);
                $scope.independent = response.data[0];
            }, responseError);

        };

    }]);
})(window.angular);
