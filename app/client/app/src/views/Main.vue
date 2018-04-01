<template>
  <section>
    <div class="level login-logo">
      <div class="level-item has-text-centered">
          <img src="../assets/img/logo.png">
      </div>
    </div>
    <div class="level">
      <div class="level-left">
        <div class="level-item has-text-centered">
          <login-component/>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item has-text-centered">
          <singup-component/>
        </div>
      </div>
    </div>
</section>
</template>

<script>
import LoginComponent from '../components/LoginComponent'
import SingupComponent from '../components/SignupComponent'

export default {
  name: 'main',
  components: {
    LoginComponent,
    SingupComponent
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
