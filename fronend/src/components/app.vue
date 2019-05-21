<template>
  <div class='app'>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="stylus">
@import '~vuetify/src/stylus/main'

html, body, .app
  height: 100%

.container
  max-width: 900px

.app
  font-size: 18px
  @media (max-width: 640px)
    font-size: 16px
  font-family: 'Roboto', sans-serif;
</style>
