export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    'bootstrap-vue/nuxt',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/auth'
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    // `baseURL` will be prepended to `url` unless `url` is absolute.
    // It can be convenient to set `baseURL` for an instance of axios to pass relative URLs
    // to methods of that instance.
    baseURL: 'http://tomatobridge.io:8088'
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {}
  },
  /*
   ** Auth module configuration
   ** See https://auth.nuxtjs.org/guide/setup.html
   */
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: {
            url: 'http://tomatobridge.io:8087/auth/login/',
            method: 'post',
            propertyName: 'access_token'
          },
          logout: {
            url: 'http://tomatobridge.io:8087/auth/logout/',
            method: 'post'
          },
          user: {
            url: 'http://tomatobridge.io:8087/auth/user/',
            method: 'get',
            propertyName: 'user'
          }
        },
        autoFetchUser: true,
        tokenRequired: true,
        tokenName: 'Authorization',
        tokenType: 'Bearer'
      }
    },
    redirect: { home: '/' }
  },
  router: {
    middleware: ['auth']
  }
}
