<template>
  <div>
    <h2 class="text-center">Login</h2>
    <hr />
    <b-alert v-if="error" show variant="danger">{{ error + '' }}</b-alert>
    <b-alert v-if="$auth.$state.redirect" show>
      You have to login before accessing to
      <strong>{{ $auth.$state.redirect }}</strong>
    </b-alert>
    <b-row align-h="center" class="pt-4">
      <b-col md="4">
        <b-card bg-variant="light">
          <form @keydown.enter="login">
            <b-form-group label="Username">
              <b-input
                ref="username"
                v-model="username"
                placeholder="anything"
              />
            </b-form-group>

            <b-form-group label="Password">
              <b-input v-model="password" type="password" placeholder="123" />
            </b-form-group>

            <div class="text-center">
              <b-btn @click="login" variant="primary" block>Login</b-btn>
              <b-btn @click="localRefresh" variant="primary" block>
                Login with Refresh
              </b-btn>
            </div>
          </form>
        </b-card>
      </b-col>
      <b-col md="1" align-self="center">
        <div class="text-center"><b-badge pill>OR</b-badge></div>
      </b-col>
      <b-col md="4" class="text-center">
        <b-card title="Social Login" bg-variant="light">
          <div v-for="s in strategies" :key="s.key" class="mb-2">
            <b-btn
              @click="$auth.loginWith(s.key)"
              :style="{ background: s.color }"
              block
              class="login-button"
            >
              Login with {{ s.name }}
            </b-btn>
          </div>
          <div class="mb-2">
            <b-btn
              @click="$auth.loginWith('oauth2mock')"
              :style="{ background: 'purple' }"
              block
              class="login-button"
            >
              Login with oauth2
            </b-btn>
          </div>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  middleware: ['auth'],
  data() {
    return {
      username: '',
      password: '123',
      error: null
    }
  },
  computed: {
    strategies() {
      return [
        { key: 'auth0', name: 'Auth0', color: '#ec5425' },
        { key: 'google', name: 'Google', color: '#4284f4' },
        { key: 'facebook', name: 'Facebook', color: '#3c65c4' },
        { key: 'github', name: 'GitHub', color: '#202326' }
      ]
    },
    redirect() {
      return (
        this.$route.query.redirect &&
        decodeURIComponent(this.$route.query.redirect)
      )
    },
    isCallback() {
      return Boolean(this.$route.query.callback)
    }
  },
  methods: {
    login() {
      this.error = null
      return this.$auth
        .loginWith('local', {
          data: {
            username: this.username,
            password: this.password
          }
        })
        .catch((e) => {
          this.error = e + ''
        })
    },
    localRefresh() {
      this.error = null
      return this.$auth
        .loginWith('localRefresh', {
          data: {
            username: this.username,
            password: this.password
          }
        })
        .catch((e) => {
          this.error = e + ''
        })
    }
  }
}
</script>

<style scoped>
.login-button {
  border: 0;
}
</style>
