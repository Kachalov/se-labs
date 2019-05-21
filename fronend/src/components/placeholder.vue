<template>
  <span
    class="badge badge-secondary"
    :style="{width: len * 0.65 + 'rem', 'background-color': color}"
  >&nbsp;</span>
</template>

<script>
  export default {
    props: {
      len: {
        type: Number,
        default: 10
      },
      color: {
        type: String,
        default: '#cfcfcf'
      }
    }
  }
</script>
