<template>
    <div class="quizzes">
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <h2>Quizzes</h2>
        <table v-if="quizzes" class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Attend</th>
                    <th scope="col">Edit</th>
                    <th scope="col">Delete</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="quiz in quizzes" :key="quiz.id" v-bind:data-quiz-id="quiz.id">
                    <th scope="row">{{ quiz.id }}</th>
                    <td>{{ quiz.name }}</td>
                    <td><router-link :to="{ name: 'quiz', params: { id: quiz.id}}">Here</router-link></td>
                    <td><router-link :to="{ name: 'quiz.edit', params: { id: quiz.id}}">Here</router-link></td>
                    <td><button v-on:click='deleteQuiz(quiz.id)'>Delete</button></td>
                </tr>
            </tbody>
        </table>
        <router-link :to="{ name: 'quiz.create' }">Create quiz</router-link>
    </div>
</template>

<script>
    const axios = require('axios')
	const instance = axios.create({
		baseURL: 'http://localhost:5000/'
    })
    
    export default {
        data () {
            return {
                quizzes: null,
                loading: false
            }
        },
        mounted(){
            this.setEventListeners()
        },
        created () {
            this.fetchData()
        },
        methods: {


            fetchData () {
                const axios = require('axios')			
                instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
				const that = this
				instance.get('/quizzes' )
					.then(function (response) {
						console.log(response);
						that.quizzes = response.data
						that.loading = false
					});
                // setTimeout(this.setTimeout, 1000)
            },
            setTimeout() {
                this.loading = false
                this.quizzes = [
                    { id: 1, name: "quiz 1", user: { first_name: "menno", last_name: "prinzhorn"}},
                    { id: 2, name: "quiz 2", user: { first_name: "menno", last_name: "prinzhorn"}},
                    { id: 3, name: "quiz 3", user: { first_name: "menno", last_name: "prinzhorn"}},
                    { id: 4, name: "quiz 4", user: { first_name: "menno", last_name: "prinzhorn"}},
                ]
            },
            setEventListeners() {
                const submitBtn = document.querySelector('.delete-quiz-btn')
                console.log(submitBtn);
                if(submitBtn){
                    submitBtn.addEventListener('click', () => {
                        this.deleteQuiz()
                    })
                }
            },
            deleteQuiz(id){
                const axios = require('axios')
				instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
                const that = this
                var a = document.querySelector('tr[data-quiz-id="' + id +'"]');
                console.log(a);
				instance.delete('/quizzes/' + id )
					.then(function (response) {
                        console.log(response);
                        // var a = document.querySelector('a[data-quiz-id="1"]');
                        // console.log(a);
                        a.remove().remove();
					});
                // axios.delete('/quiz/' + id)
            }
        },
        
    }
</script>