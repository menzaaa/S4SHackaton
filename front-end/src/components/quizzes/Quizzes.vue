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
                </tr>
            </thead>
            <tbody>
                <tr v-for="quiz in quizzes" :key="quiz.id">
                    <th scope="row">{{ quiz.id }}</th>
                    <td>{{ quiz.name }}</td>
                    <td><router-link :to="{ name: 'quiz', params: { id: quiz.id}}">Here</router-link></td>
                    <td><router-link :to="{ name: 'quiz.edit', params: { id: quiz.id}}">Here</router-link></td>
                </tr>
            </tbody>
        </table>
        <router-link :to="{ name: 'quiz.create' }">Here</router-link>
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
        created () {
            this.fetchData()
        },
        methods: {
            fetchData () {
                this.loading = true
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
            }
        },
    }
</script>