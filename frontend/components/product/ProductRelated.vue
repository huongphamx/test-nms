<script lang="ts" setup>
interface RelatedProduct {
  url_thumbnail: string
  product_count: number
  price: number
  rating_avg?: number,
  name: string
  id: number
  rating_count: number
}

const relatedProducts: RelatedProduct[] = [
  {
    "url_thumbnail": "https://cf.shopee.vn/file/be82e16ddc37dcf2657d02a30171a050",
    "product_count": 1,
    "price": 530000.0,
    "name": "BỘ HUB MỞ RỘNG 8 IN 1 BASEUS METAL GLEAM LVM001",
    "id": 288753,
    "rating_count": 0
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/d01055f6a5df466979ad3b6d0b1323f2",
    "product_count": 3,
    "price": 445000.0,
    "name": "HUB CHIA CỔNG LIGHTNING BASEUS L47",
    "id": 281703,
    "rating_count": 0
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/1c9dc6173430f906fcf3c320f3391f70",
    "product_count": 6,
    "price": 550000.0,
    "rating_avg": 5.0,
    "name": "BỘ HUB CHUYỂN ĐỔI 5 TRONG 1 BASEUS CAHUB-TD0G",
    "id": 260195,
    "rating_count": 7
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/03f074338bc5815fb00fdb9ab2e85f3d",
    "product_count": 26,
    "price": 310000.0,
    "rating_avg": 5.0,
    "name": "BỘ HUB CHUYỂN ĐỔI 5 TRONG 1 BASEUS CAHUB-K0G",
    "id": 260194,
    "rating_count": 94
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/3bff7e5f6cec689fda2a2a6fc1017a3d",
    "product_count": 14,
    "price": 560000.0,
    "rating_avg": 5.0,
    "name": "BỘ HUB CHUYỂN ĐỔI 5 TRONG 1 BASEUS CAHUB-TD03",
    "id": 288749,
    "rating_count": 3
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/53e424b4e24a5a07412a1be9b46043ea",
    "product_count": 3,
    "price": 305000.0,
    "name": "Bộ chia Hub USB 3.0 Unitek Y3082B",
    "id": 30786,
    "rating_count": 0
  },
  {
    "url_thumbnail": "https://salt.tikicdn.com/cache/280x280/ts/product/30/aa/9d/58b541beca9cec3c585dfc69678a6bc5.jpg",
    "product_count": 4,
    "price": 600000.0,
    "rating_avg": 5.0,
    "name": "BỘ CHUYỂN USB-C3.1 HUB ENERGIZER HC303CV",
    "id": 260103,
    "rating_count": 13
  },
  {
    "url_thumbnail": "https://salt.tikicdn.com/cache/280x280/ts/product/41/f1/54/2c4888e69192f23fa28f9a83fcdecc9b.jpg",
    "product_count": 5,
    "price": 479000.0,
    "rating_avg": 5.0,
    "name": "BỘ CHUYỂN USB-C3.1 HUB ENERGIZER 3USB-A/1USB-C - HC304AC",
    "id": 135014,
    "rating_count": 11
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/3a2b114675c3341b001aab4739b8bf00",
    "product_count": 8,
    "price": 279000.0,
    "rating_avg": 5.0,
    "name": "BỘ CHIA CỔNG TYPE-C 1 RA 3 BASEUS L49",
    "id": 260178,
    "rating_count": 31
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/2d864e2b0619f8aa456138ae17231d82",
    "product_count": 2,
    "price": 375000.0,
    "name": "BỘ CHIA HUB USB 3.0 RA 4 CỔNG USB 3.0 UGREEN 20285",
    "id": 275351,
    "rating_count": 0
  },
  {
    "url_thumbnail": "https://cf.shopee.vn/file/27a77a5129e43c712de0ab95cb53d808",
    "product_count": 2,
    "price": 290000.0,
    "name": "Hub USB 4 Cổng Belkin F4U042BT",
    "id": 237335,
    "rating_count": 0
  },
  {
    "url_thumbnail": "https://salt.tikicdn.com/cache/280x280/ts/product/19/2d/9f/544dd94ada70fe6ad2b6d06b6dc8e1d0.jpg",
    "product_count": 5,
    "price": 600000.0,
    "rating_avg": 5.0,
    "name": "BỘ HUC CHUYỂN ĐỔI TYPE C 6 IN 1 BASEUS CAHUB-DZ0G",
    "id": 260205,
    "rating_count": 23
  }
]

const breakpoints = {
  700: {
    itemsToShow: 3.5,
  },
  1024: {
    itemsToShow: 5,
  },
}
</script>

<template>
  <div class="px-4 lg:px-0">
    <div class="text-lg font-semibold">Sản phẩm liên quan</div>
    <Carousel :items-to-show="1.5" :breakpoints="breakpoints">
      <Slide v-for="product in relatedProducts" :key="product.id">
        <div class="shadow mx-2">
          <img :src="product.url_thumbnail" alt="" class="w-56 h-56">
          <div class="lowercase">{{ product.name }}</div>
        </div>
      </Slide>
      <template #addons>
        <Navigation />
      </template>
    </Carousel>
  </div>
</template>
