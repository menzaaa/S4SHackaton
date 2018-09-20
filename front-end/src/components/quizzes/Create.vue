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
                                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter name">
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
    export default {
        data () {
            return {
                loading: false
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
                        this.createQuiz()
                    })
                }
            },
            createQuiz() {
                //doe api call
                alert('Quiz aangemaakt');
                this.$router.push({ name: 'quizzes'})
            }
        },
    }
</script>