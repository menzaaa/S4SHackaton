<template>
    <div class="create-quiz">
        <div class="row justify-content-center">
            <div class="col col-lg-8">
                <div class="card">
                    <div class="card-header">
                        Create your quiz
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="form-group">
                                <label for="exampleInputEmail1">Name</label>
                                <input type="text" class="form-control quiz-name" name="quiz-name" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter name">
                            </div>
                            <button type="submit" class="btn btn-primary create-quiz-btn">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
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
                loading: false,
                inputName: null
            }
        },
        created () {
            this.fetchData()
        },
        mounted () {
            this.setEventListeners()
        },
        methods: {
            fetchData () {
                this.loading = true
                setTimeout(this.setTimeout, 1000)
            },
            setTimeout() {
                this.loading = false
            },
            setEventListeners() {
                const submitBtn = document.querySelector('.create-quiz-btn')
                if(submitBtn){
                    submitBtn.addEventListener('click', () => {
                        this.inputName = document.querySelector('.quiz-name').value
                        this.createQuiz()
                    })
                }
            },
            createQuiz() {
                instance.defaults.headers.common['Authorization'] = 'Basic ' + btoa('max' + ':' + 'qwerty');
				const that = this
				instance.post('/quizzes', {
					name: this.inputName,
					user_id: 1
				} )
					.then(function (response) {
						console.log(response);
						that.user = response.data
						that.loading = false
					});
                alert('Quiz aangemaakt');
                this.$router.push({ name: 'quizzes'})
            }
        },
    }
</script>