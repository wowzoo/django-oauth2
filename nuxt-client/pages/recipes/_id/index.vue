<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
      </div>
      <!-- <div class="col-md-6 mb-4">
        <img
          :src="recipe.picture"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          alt
        />
      </div> -->
      <div class="col-md-6">
        <div class="recipe-details">
          <h4>Ingredients</h4>
          <p>{{ recipe.ingredients }}</p>
          <h4>Preparation time ⏱</h4>
          <p>{{ recipe.prep_time }} mins</p>
          <h4>Difficulty</h4>
          <p>{{ recipe.difficulty }}</p>
          <h4>Preparation guide</h4>
          <textarea
            v-html="recipe.prep_guide"
            class="form-control"
            rows="10"
            disabled
          />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: 'View Recipe'
    }
  },
  data() {
    return {
      recipe: {
        name: '',
        // picture: '',
        ingredients: '',
        difficulty: '',
        prep_time: null,
        prep_guide: ''
      }
    }
  },
  async asyncData({ $axios, params }) {
    try {
      const recipe = await $axios.$get(`/recipes/${params.id}`)
      return { recipe }
    } catch (e) {
      return { recipe: [] }
    }
  }
}
</script>

<style scoped></style>
