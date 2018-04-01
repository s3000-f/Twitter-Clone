<template>
<div>

    <nav>
        <router-view name="navbar"></router-view>
        <router-view name="subnavbar"></router-view>
    </nav>

    <section class="section columns">
      <transition name="fade">
        <div class="container">

          <router-view name="main"></router-view>


        </div>
      </transition>
    </section>

</div>
</template>

<script>
//"2d6e52686c5f3defa86a883758e34701"
export default {
  name: 'App',
  data () {
  	return {
  	  token: ''
    }
  },
  components: {
  },
  computed: {
    isLoading () {
      return this.$store.state.isLoading
    }
  }
}
</script>

<style lang="sass">
// Main.sass is imported into all Components using Webpack Data Parameter

</style>
