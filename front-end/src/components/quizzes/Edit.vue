<template>
    <div class="create-quiz">
        <div class="row justify-content-center">
            <div class="col col-lg-8">
                <div class="card">
                    <div class="card-header">
                        Edit your quiz
                    </div>
                    <div class="card-body">
                        <form>
                            <div class="form-group">
                                <label for="exampleInputEmail1">Name</label>
                                <input type="text" class="form-control" v-bind:value="quiz.name" id="exampleInputEmail1" aria-describedby="emailHelp">
                            </div>
                            <button type="submit" class="btn btn-primary edit-quiz-btn">Submit</button>
                        </form>
                    </div>
                    <table v-if="quiz" class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Name</th>
                                <th scope="col">description</th>
                                <th scope="col">answer</th>
                                <th scope="col">Edit</th>
                                <th scope="col">Remove</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="question in quiz.questions" :key="question.id">
                                <th scope="row">{{ question.id }}</th>
                                <td>{{ question.name }}</td>
                                <td>{{ question.description }}</td>
                                <td>{{ question.answer }}</td>
                                <td><router-link :to="{ name: 'quiz', params: { id: quiz.id}}">Here</router-link></td>
                                <td><a href="#" class="remove-question">Here</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                loading: false,
                quiz: {
                    id: 1, 
                    name: "quiz 1",
                    user: { first_name: "menno", last_name: "prinzhorn" },
                    questions: [
                        { id: 1, name: "Los dit programmeer probleem op 1", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3, answers: { id: 1, user_id: 1, question_id: 1, input: "<test>"} },
                        { id: 2, name: "Los dit programmeer probleem op 2", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 },
                        { id: 3, name: "Los dit programmeer probleem op 3", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 },
                        { id: 4, name: "Los dit programmeer probleem op 4", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: 3 }
                    ]
                }
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
                const submitBtn = document.querySelector('.edit-quiz-btn')
                const deleteBtn = document.querySelector('.remove-question')
                if(submitBtn){
                    submitBtn.addEventListener('click', () => {
                        this.editQuiz()
                    })
                }
                if(deleteBtn){
                    deleteBtn.addEventListener('click', () => {
                        this.removeQuestion()
                    })

                }
            },
            editQuiz() {
                //doe api call
                alert('Quiz aangepast');
                this.$router.push({ name: 'quizzes'})
            },
            removeQuestion() {
                //doe api call
                alert('Question removed');
                this.$router.push({ name: 'quizzes'})
            }
        },
    }
</script>