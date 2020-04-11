<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>La Recipes</h3>
          <nuxt-link to="/recipes/add" class="btn btn-info">
            Add Recipe
          </nuxt-link>
        </div>
      </div>
      <template v-for="recipe in recipes">
        <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import RecipeCard from '~/components/RecipeCard.vue'

export default {
  head() {
    return {
      title: 'Recipes list'
    }
  },
  components: {
    RecipeCard
  },
  data() {
    return {
      recipes: []
    }
  },
  async asyncData({ $axios, params }) {
    try {
      // this is a short version of
      // const response = await $axios.get('/recipes')
      // const recipes = response.data
      const recipes = await $axios.$get('/recipes')
      return { recipes }
    } catch (e) {
      return { recipes: [] }
    }
  },
  methods: {
    async deleteRecipe(recipeID) {
      try {
        await this.$axios.$delete(`/recipes/${recipeID}`)
        const newRecipes = await this.$axios.$get('/recipes')
        this.recipes = newRecipes
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style scoped></style>
