<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
      </div>
      <!-- <div class="col-md-6 mb-4">
        <img
          v-if="!preview"
          :src="recipe.picture"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
        />
        <img
          v-else
          :src="preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
        />
      </div> -->
      <div class="col-md-4">
        <form @submit.prevent="submitRecipe">
          <div class="form-group">
            <label for>Recipe Name</label>
            <input v-model="recipe.name" type="text" class="form-control" />
          </div>
          <div class="form-group">
            <label for>Ingredients</label>
            <input
              v-model="recipe.ingredients"
              type="text"
              class="form-control"
              name="Ingredients"
            />
          </div>
          <!-- <div class="form-group">
            <label for>Food picture</label>
            <input @change="onFileChange" type="file" />
          </div> -->
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Difficulty</label>
                <select v-model="recipe.difficulty" class="form-control">
                  <option value="easy">Easy</option>
                  <option value="medium">Medium</option>
                  <option value="hard">Hard</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  Prep time
                  <small>(minutes)</small>
                </label>
                <input
                  v-model="recipe.prep_time"
                  type="text"
                  class="form-control"
                  name="Ingredients"
                />
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>Preparation guide</label>
            <textarea
              v-model="recipe.prep_guide"
              class="form-control"
              rows="8"
            ></textarea>
          </div>
          <button type="submit" class="btn btn-success">Save</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: 'Edit Recipe'
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
      },
      preview: ''
    }
  },
  async asyncData({ $axios, params }) {
    try {
      const recipe = await $axios.$get(`/recipes/${params.id}`)
      return { recipe }
    } catch (e) {
      return { recipe: [] }
    }
  },
  methods: {
    // onFileChange(e) {
    //   const files = e.target.files || e.dataTransfer.files
    //   if (!files.length) {
    //     return
    //   }
    //   this.recipe.picture = files[0]
    //   this.createImage(files[0])
    // },
    // createImage(file) {
    //   const reader = new FileReader()
    //   const vm = this
    //   reader.onload = (e) => {
    //     vm.preview = e.target.result
    //   }
    //   reader.readAsDataURL(file)
    // },
    async submitRecipe() {
      const editedRecipe = this.recipe
      // if (editedRecipe.picture.includes('http://')) {
      //   delete editedRecipe.picture
      // }

      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }

      const formData = new FormData()
      for (const data in editedRecipe) {
        formData.append(data, editedRecipe[data])
      }

      try {
        // eslint-disable-next-line no-unused-vars
        const response = await this.$axios.$patch(
          `/recipes/${editedRecipe.id}/`,
          formData,
          config
        )
        this.$router.push('/recipes/')
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style></style>
