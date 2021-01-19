$(document).ready(function () {


    var baseUrl = 'http://'+ window.location.host + '/';

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');

    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Realmente deseja deletar essa tarefa?');
        if (result){
            window.location.href = delLink;
        }
    });


    $(searchBtn).on('click', function(){
        searchForm.submit();
    });

    $(filter).change(function(){
        
        var filter = $(this).val();
        console.log(filter);
        window.location.href = baseUrl + '?filter=' + filter;
    });
})