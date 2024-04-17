<script lang="ts" setup>
const props = defineProps<{
  images: string[]
}>()

const currentSlide = ref(0)
function slideTo(val: number) {
  currentSlide.value = val
}
function previous() {
  if (currentSlide.value === 1) {
    currentSlide.value = props.images.length - 1
  } else {
    currentSlide.value -= 1
  }
}
function next() {
  if (currentSlide.value === props.images.length - 1) {
    currentSlide.value = 0
  } else {
    currentSlide.value += 1
  }
}
</script>

<template>
  <div class="w-full lg:w-1/2 flex-shrink-0 mr-4 lg:p-6 lg:border rounded-xl">
    <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
      <Slide v-for="img, i in images" :key="i">
        <img :src="img" alt="" class="cursor-zoom-in h-72 lg:h-fit object-contain">
      </Slide>
    </Carousel>
    <div class="2xl:hidden mt-2 flex items-center justify-center gap-2">
      <div v-for="img, i in images" :key="i" class="w-2 h-2 rounded-full"
        :class="currentSlide === i ? 'bg-orange-500' : 'bg-gray-500'" @click="currentSlide = i">
      </div>
    </div>

    <div class="hidden 2xl:flex">
      <div class="bg-gray-200/60 hover:bg-gray-400/60 px-1 flex items-center cursor-pointer">
        <UIcon name="i-ph-arrow-left" @click="previous" />
      </div>
      <Carousel id="thumbnails" :items-to-show="5" :wrap-around="true" :transition="500" ref="carousel">
        <Slide v-for="img, i in images" :key="i">
          <img :src="img" alt="" @mouseover="slideTo(i)" class="border w-[104px] h-[104px] cursor-zoom-in"
            :class="currentSlide === i ? 'border-orange-500' : ''">
        </Slide>
      </Carousel>
      <div class="bg-gray-200/60 hover:bg-gray-400/60 px-1 flex items-center cursor-pointer">
        <UIcon name="i-ph-arrow-right" @click="next" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.carousel__slide {
  scroll-snap-stop: auto;
  flex-shrink: 0;
  margin-right: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translateZ(0);
}
</style>