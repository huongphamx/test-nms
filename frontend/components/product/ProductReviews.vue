<script lang="ts" setup>
import type { Review } from '@/types'

const reviews: Review[] = [
  {
    "review_base_id": "1__6445871458",
    "product_base_id": "1__5382617241__227642622",
    "platform_id": 1,
    "title": null,
    "content": "Sp tốt \nMua lúc 8g tối 9g nhận được luôn\nShop dịch vụ tốt\nMình dùng type c qua monitor 4k đường hdmi  i",
    "rating": 5,
    "images": [
      "https://cf.shopee.vn/file/77bd432952a494ecf86d3b7992f2e515",
      "https://cf.shopee.vn/file/1fa4aba5bdbd00aae40a1ffa5e6b8bc5",
      "https://cf.shopee.vn/file/fd9f55f1aa284cf8f0ad6660a39fa9f8",
      "https://cf.shopee.vn/file/bc4cf053e366300af40b15b4212c2a33",
      "https://play-tx.vod.shopee.com/c3/98934353/103/AmM1gYMAEE=mRvMhSgEGLsxH.jpg"
    ],
    "comments": null,
    "created_at_platform": 1635631356,
    "user_username": "annatrinh2001",
    "user_url_image": "https://cf.shopee.vn/file/3958d01eeaaf632ee0bb594590303a22"
  },
  {
    "review_base_id": "1__6449115499",
    "product_base_id": "1__5382617241__227642622",
    "platform_id": 1,
    "title": null,
    "content": "Khá là ngon nhưng thỉnh thoảng cổng mạng bị đứt, mình nghĩ là do bị nóng quá, mình dùng 3 cổng USB + HDMI + LAN, liên tục tầm 10 mấy tiếng thì tự nhiên mất LAN, rút ra để nguội tý, restart máy lại thì bình thường",
    "rating": 5,
    "images": null,
    "comments": [
      {
        "comment": "Dạ, cảm ơn anh đã mua hàng tại shop.\nAnh thử kiểm tra lại các thiết bị mình sử dụng có dùng nhiều điện không nhé. Các thiết bị ngoại vi kết nối vào cần nhận dữ liệu và điện năng đồng thời, một số thiết bị như ổ cứng... sẽ cần nhiều điện để hoạt động thì phải bổ sung nguồn rời ạ.",
        "created_at": 1635748516
      }
    ],
    "created_at_platform": 1635681737,
    "user_username": "ltnghia678",
    "user_url_image": "https://cf.shopee.vn/file/8cf409d63f4d1341939596054a0187aa"
  }
]
</script>

<template>
  <div>
    <ProductReviewsRow v-for="review in reviews" :key="review.review_base_id" :review="review" class="first:pt-0" />
  </div>
</template>
