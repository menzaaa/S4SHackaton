<template>
    <div class="quiz">
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <h2>{{ quiz.name }}</h2>
        <table v-if="quiz" class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Vraag</th>
                    <th scope="col">Omschrijving</th>
                    <th scope="col">Attend</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="question in quiz.questions" :key="question.id">
                    <th scope="row">{{ question.id }}</th>
                    <td>{{ question.name }}</td>
                    <td>{{ question.description }}</td>
                    <td v-if="question.answer">"Answered"</td>
                    <td v-else><router-link :to="{ name: 'questions', params: { id: question.id}}">Here</router-link></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                id: null,
                quiz: null,
            }
        },
        created () {
            this.fetchData()
        },
        methods: {
            fetchData () {
                this.loading = true
                setTimeout(this.setTimeout, 1000)
            },
            setTimeout() {
                this.loading = false
                this.quiz = {
                    id: 1, 
                    name: "quiz 1",
                    user: { first_name: "menno", last_name: "prinzhorn" },
                    questions: [
                        { id: 1, name: "Los dit programmeer probleem op 1", description: "Tel variable 'A' op bij 'B' en return de uitkomst", answer: { id: 1, user_id: 1, question_id: 1, input: "<test>"} },
                        { id: 2, name: "Los dit programmeer probleem op 2", description: "Tel variable 'A' op bij 'B' en return de uitkomst" },
                        { id: 3, name: "Los dit programmeer probleem op 3", description: "Tel variable 'A' op bij 'B' en return de uitkomst" },
                        { id: 4, name: "Los dit programmeer probleem op 4", description: "Tel variable 'A' op bij 'B' en return de uitkomst" }
                    ]
                }
            }
        },
    }
</script>