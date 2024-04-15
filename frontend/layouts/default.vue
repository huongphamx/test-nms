<script lang="ts" setup>

</script>

<template>
  <div>
    <div class="py-3 md:py-4 md:border-b">
      <div class="max-w-7xl mx-auto flex">
        <img
          src="https://lh3.googleusercontent.com/pw/ADCreHd5PMvwKUSbjtSRpUfeyDaazAbdXF1H0arvHtS62AyfivDEAN6hRSq-GTJ6wKiyn-9IEr63aaiNtFq6J2fP_I6VtpGAIwqAQu4B2mL64M2h2HHkPY4VhRWoDpag5VXN3Dxtwb277ZDkXPa0mnDxTTGL=w512"
          alt="logo" class="h-12">
        <div class="border rounded-full px-5 py-1 w-full max-w-xl mx-auto flex items-center">
          <input type="text" placeholder="Dán link hoặc tìm sản phẩm" class="flex-1 focus:outline-none">
          <UIcon name="i-ph-magnifying-glass" />
        </div>
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1">
            <UIcon name="i-ph-list" class="w-5 h-5" /> DANH MỤC
          </div>
          <div>BLOG</div>
        </div>
      </div>
    </div>
    <slot />
  </div>
</template>
