function loadProjects(){
    var projects_arr = [];
    fetch(`/load_projects`) 
    .then(response => {
        return response.json()
    })
    .then(json => {
        console.log('json', json)
        
        console.log(typeof projects_arr)

        for(var i = 0; i < json.length; i++){
            var title = json[i].title
            projects_arr.push({title: title})
        }

        console.log(projects_arr)
        console.log(typeof projects_arr)
        })
    .then( () => {
        console.log(projects_arr)
        return projects_arr
    })
};
