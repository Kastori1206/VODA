<template>
  <div class="customer">
      <div class="voda-logo">
        <img alt="voda logo" src="../assets/logo_transparent.png" width="300" height="300">
      </div>
      <div class="customer-input">
        <div>
            별명: <input type="text">
        </div>
        <div>
            이메일: <input type="text">
        </div>
      </div>
      <div class="enter-button">
          <a href="/meeting/start"><button>다음</button></a>
      </div>
  </div>
</template>

<script>
export default {
    name: 'Customer',
}
</script>

<style>

</style>