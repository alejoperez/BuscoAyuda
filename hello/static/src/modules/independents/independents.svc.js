(function (ng) {
    var mod = ng.module('independentsModule');

    mod.service('independentsService', ['$http', 'independentsContext', function ($http, context) {

        this.getIndependents = function () {
            return $http({
                method: 'GET',
                url: 'https://shielded-headland-12840.herokuapp.com/independents'
                //url: 'http://127.0.0.1:8000/independents/'
            });
        };

    }]);
})(window.angular);