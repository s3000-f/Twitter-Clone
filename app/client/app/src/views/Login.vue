<template>
  <section>
    <div class="level login-logo">
      <div class="level-item has-text-centered">
          <img src="../assets/img/logo.png">
      </div>
    </div>
    <div class="level">
      <div class="level-item has-text-centered">
        <login-component/>
      </div>
    </div>
    <div class="level">
      <div class="level-item has-text-centered">
        <router-link tag="a" :to="{ path: 'Home'}" class="button">Login</router-link>
      </div>
  </div>
</section>
</template>

<script>
import LoginComponent from '../components/LoginComponent'
export default {
  name: 'Login',
  components: {
    LoginComponent
  },
  data () {
    return {

    }
  },
  computed: {

  }
}
</script>

<style lang="sass" scoped>

.login-logo
  margin-top: 200px

  img
    height: 150px

</style>
