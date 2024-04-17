<script lang="ts" setup>
import type { CompareDataProduct } from '@/types'

const isExpand = ref(false)

const products: CompareDataProduct[] = [
  {
    "url_thumbnail": "https://vn-live-01.slatic.net/p/a1a8cbb1c861b6b4aed0fd9d7c60cf24.jpg",
    "is_official_shop": false,
    "price": 511668,
    "rating_avg": 5,
    "product_base_id": "2__1394744990",
    "name": "Bộ Hub mở rộng Baseus Metal Gleam Series LVM001",
    "historical_sold": 30,
    "rating_count": 6,
    "price_insight": {
      "product_base_id": "2__1394744990",
      "classify_price": "no_comment",
      "current_price": 511668,
      "ratio": 0.2633333,
      "min_price": 373210,
      "max_price": 899000,
      "avg_price": 619097.7,
      "delta_price": -197332
    }
  },
  {
    "url_thumbnail": "https://vn-live-01.slatic.net/p/8f0e6b96c7d98adc0bacbaabe672b3ac.jpg",
    "is_official_shop": false,
    "price": 524000,
    "rating_avg": 0,
    "product_base_id": "2__1579177856",
    "name": "Hub Baseus Metal Gleam Series Multifunctional Type-C HUB Docking Station",
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "2__1579177856",
      "classify_price": "best",
      "current_price": 524000,
      "ratio": 0,
      "min_price": 524000,
      "max_price": 698000,
      "avg_price": 626117.6,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://salt.tikicdn.com/cache/280x280/ts/product/1e/3d/9e/99245ba4815b032d4119ca520365427c.jpg",
    "price": 529900,
    "rating_avg": 0,
    "name": "Bộ Hub mở rộng 8 in 1 Baseus Metal Gleam Series LVM001 - hàng chính hãng",
    "product_base_id": "3__98822512__136102612",
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "3__98822512__136102612",
      "classify_price": "bad",
      "current_price": 529900,
      "ratio": 1,
      "min_price": 489900,
      "max_price": 529900,
      "avg_price": 516350,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/8c9492e2c063ca4f71d9cf25c142b5bc",
    "is_official_shop": false,
    "price": 540000,
    "rating_avg": 0,
    "product_base_id": "1__8133637233__186275673",
    "name": "Bộ Hub mở rộng 4 in 1/5 in 1 /6 in 1/8 in 1 Baseus Metal Gleam Series LVM001",
    "historical_sold": 0,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__8133637233__186275673",
      "classify_price": "normal",
      "current_price": 540000,
      "ratio": -1,
      "min_price": 540000,
      "max_price": 540000,
      "avg_price": 540000,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/be82e16ddc37dcf2657d02a30171a050",
    "is_official_shop": false,
    "price": 549000,
    "rating_avg": 4.90566037735849,
    "product_base_id": "1__5382617241__227642622",
    "name": "Bộ Hub mở rộng Baseus Metal Gleam Series LVM001",
    "historical_sold": 169,
    "rating_count": 53,
    "price_insight": {
      "product_base_id": "1__5382617241__227642622",
      "classify_price": "good",
      "current_price": 549000,
      "ratio": 0.20449686,
      "min_price": 381650,
      "max_price": 1200000,
      "avg_price": 566246.94,
      "delta_price": 22110
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/8660712cfde2319c2fc25b270204cae2",
    "is_official_shop": false,
    "price": 549000,
    "rating_avg": 0,
    "product_base_id": "1__2931302536__75149586",
    "name": "Bộ Hub mở rộng 8 in 1 Baseus Metal Gleam Series LVM001",
    "historical_sold": 2,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__2931302536__75149586",
      "classify_price": "good",
      "current_price": 549000,
      "ratio": 0.09514748,
      "min_price": 449000,
      "max_price": 1500000,
      "avg_price": 610267.2,
      "delta_price": 60000
    }
  },
  {
    "url_thumbnail": "https://salt.tikicdn.com/cache/280x280/ts/product/1e/3d/9e/99245ba4815b032d4119ca520365427c.jpg",
    "price": 549000,
    "rating_avg": 4.3,
    "product_base_id": "3__98822512__98822516",
    "name": "Bộ Hub mở rộng 8 in 1 Baseus Metal Gleam Series LVM001 - hàng chính hãng",
    "historical_sold": 24,
    "rating_count": 10,
    "price_insight": {
      "product_base_id": "3__98822512__98822516",
      "classify_price": "good",
      "current_price": 549000,
      "ratio": 0.21022402,
      "min_price": 461160,
      "max_price": 879000,
      "avg_price": 626745.9,
      "delta_price": -211000
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/8660712cfde2319c2fc25b270204cae2",
    "is_official_shop": false,
    "price": 550000,
    "rating_avg": 0,
    "product_base_id": "1__3882740592__360074534",
    "name": "Bộ Hub mở rộng 8 in 1 Baseus Metal Gleam Series LVM001",
    "historical_sold": 1,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__3882740592__360074534",
      "classify_price": "good",
      "current_price": 550000,
      "ratio": 0.17721519,
      "min_price": 410000,
      "max_price": 1200000,
      "avg_price": 673841.06,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/e3ba81ee32931d9343df50e4b0300336",
    "is_official_shop": false,
    "price": 550000,
    "rating_avg": 0,
    "product_base_id": "1__8386723869__50400888",
    "name": "Hub Baseus Metal Gleam Series Multifunctional Type-C HUB Docking Station",
    "historical_sold": 0,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__8386723869__50400888",
      "classify_price": "normal",
      "current_price": 550000,
      "ratio": -1,
      "min_price": 550000,
      "max_price": 550000,
      "avg_price": 550000,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/b73ec815d83637a6febeb9ca3e682429",
    "is_official_shop": false,
    "price": 550000,
    "rating_avg": 0,
    "product_base_id": "1__11835362799__199781762",
    "name": "HUB chuyển đa năng Baseus Metal Gleam Series Multifunctional Docking Station",
    "historical_sold": 0,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__11835362799__199781762",
      "classify_price": "bad",
      "current_price": 550000,
      "ratio": 1,
      "min_price": 479000,
      "max_price": 550000,
      "avg_price": 535477.25,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://vn-live-01.slatic.net/p/0f96423c22d795766a98dfbe22a502b8.jpg",
    "is_official_shop": false,
    "rating_avg": 0,
    "price": 550000,
    "product_base_id": "2__1492102365",
    "name": "Bộ Hub mở rộng 4 in 1/5 in 1 /6 in 1/8 in 1 Baseus Metal Gleam Series LVM001",
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "2__1492102365",
      "classify_price": "normal",
      "current_price": 550000,
      "ratio": -1,
      "min_price": 550000,
      "max_price": 550000,
      "avg_price": 550000,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/8c9492e2c063ca4f71d9cf25c142b5bc",
    "is_official_shop": false,
    "price": 550000,
    "rating_avg": 0,
    "product_base_id": "1__7183751899__85776939",
    "name": "Bộ Hub mở rộng 4 in 1/5 in 1 /6 in 1/8 in 1 Baseus Metal Gleam Series LVM001",
    "historical_sold": 0,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__7183751899__85776939",
      "classify_price": "normal",
      "current_price": 550000,
      "ratio": -1,
      "min_price": 550000,
      "max_price": 550000,
      "avg_price": 550000,
      "delta_price": null
    }
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/b78750f30e6b9bd7950aa869b0ccdc46",
    "is_official_shop": false,
    "price": 559500,
    "rating_avg": 0,
    "product_base_id": "1__9733272694__304541051",
    "name": "Hub chuyển đa năng Baseus Metal Gleam Series Multifunctional Docking Station",
    "historical_sold": 0,
    "rating_count": 0,
    "price_insight": {
      "product_base_id": "1__9733272694__304541051",
      "classify_price": "good",
      "current_price": 559500,
      "ratio": 0.1686874,
      "min_price": 399500,
      "max_price": 1348000,
      "avg_price": 886798,
      "delta_price": -559500
    }
  }
]

const totalProducts = computed(() => {
  return products.length
})

const minPrice = computed(() => {
  return products.reduce((prev, curr) => prev.price < curr.price ? prev : curr).price
})

const maxPrice = computed(() => {
  return products.reduce((prev, curr) => prev.price > curr.price ? prev : curr).price
})

const allShopeeProducts = computed(() => products.filter(p => p.product_base_id.startsWith('1__')))
const shopeeProducts = computed(() => {
  return isExpand.value ? allShopeeProducts.value : allShopeeProducts.value.slice(0, 3)
})

const allLazadaProducts = computed(() => products.filter(p => p.product_base_id.startsWith('2__')))
const lazadaProducts = computed(() => {
  return isExpand.value ? allLazadaProducts.value : allLazadaProducts.value.slice(0, 3)
})

const allTikiProducts = computed(() => products.filter(p => p.product_base_id.startsWith('3__')))
const tikiProducts = computed(() => {
  return isExpand.value ? allTikiProducts.value : allTikiProducts.value.slice(0, 3)
})

const isExpandable = computed(() => allShopeeProducts.value.length > 3 || allLazadaProducts.value.length > 3 || allTikiProducts.value.length > 3)
const productToExpandNum = computed(() => products.length - shopeeProducts.value.length - lazadaProducts.value.length - tikiProducts.value.length)

const startPos = ref<HTMLElement>()
function toggleExpand() {
  isExpand.value = !isExpand.value
  startPos.value?.scrollIntoView()
}
</script>

<template>
  <div ref="startPos" class="scroll-mt-16">
    <div class="my-3 text-gray-600">
      Tìm thấy
      <span class="text-gray-700 font-medium">{{ totalProducts }}</span>
      nơi bán khác, giá từ
      <span class="text-gray-700 font-medium">{{ minPrice }} ₫ -
        {{ maxPrice }} ₫</span>
    </div>
    <div class="space-y-4">
      <div>
        <img
          src="https://lh3.googleusercontent.com/OwDr2GswbeYne43OtdOL1cqPx_Q7MoXNPbGAAalXumcCojcbb-KcUQqjP4l2EHOPXySoPWqk5YKDcRqT4_22Yv0L0g0NS6owVBz5ZRFCmUEyyC3NcZd4Nndb6vLEkFJ6k29I5fOb=w556-h50-no"
          alt="shopee" class="h-8 md:h-10">
      </div>
      <ProductComparePriceRow v-for="product in shopeeProducts" :key="product.product_base_id" :product="product" />
    </div>
    <div class="mt-6 space-y-4">
      <div>
        <img
          src="https://lh3.googleusercontent.com/DF4aF5VZEz_NYkI_eJIyYFD6SM21UyBxiEeWVRaYY3Cr-MUZ8AuUgB6kI6L6DBCzmCJf7TIMRQYdHgZ9m4WEA4e41oglDoWQIpwoK0Tj784azJsPky9g3w6tUR7mhsfi4U8o_NSGJw=w765-h50-no"
          alt="shopee" class="h-8 md:h-10">
      </div>
      <ProductComparePriceRow v-for="product in lazadaProducts" :key="product.product_base_id" :product="product" />
    </div>
    <div class="mt-6 space-y-4">
      <div>
        <img
          src="https://lh3.googleusercontent.com/VaYiFU3XqGRArjLz8nZhSv2VWl39KbeU3Kv3HiK7c5LNA-JqSRZo22Ds2JK0kK04SENns6F8c-vrtQLlC7VHkvh3Y-grYu2HKF6hVAfY0rH_ivBDwdQXB2wc1hkPbBNjp_2Sme5wTA=w515-h50-no"
          alt="shopee" class="h-8 md:h-10">
      </div>
      <ProductComparePriceRow v-for="product in tikiProducts" :key="product.product_base_id" :product="product" />
    </div>
    <div class="text-center mt-4">
      <UButton v-if="isExpandable" :label="isExpand ? 'Rút gọn' : `Xem thêm ${productToExpandNum} nơi bán khác`"
        variant="ghost" color="gray" size="xl" :icon="isExpand ? 'i-ph-caret-up' : 'i-ph-caret-down'" trailing
        @click="toggleExpand()" />
    </div>
  </div>
</template>
