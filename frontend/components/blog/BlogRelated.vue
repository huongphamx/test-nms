<script lang="ts" setup>
interface RelatedBlog {
  url_thumbnail: string
  category_id: number
  lst_category_base_id: string[]
  lst_keyword: string[]
  id: number
  title: string
  excerpt: string
  published_at: string
  slug: string
}

const relatedBlogList: RelatedBlog[] = [
  {
    "url_thumbnail": "https:\/\/static.beecost.vn\/upload\/uploads\/2020\/03\/1584424796.6228461..jpe",
    "category_id": 8691,
    "lst_category_base_id": [
      "1__100644",
      "3__1846",
      "4__2901"
    ],
    "lst_keyword": [
      "laptop",
      "pin laptop",
      "pin laptop giá rẻ"
    ],
    "id": 835482,
    "title": "Có nên mua và sử dụng pin laptop giá rẻ không ? [CHUYÊN GIA TƯ VẤN]",
    "excerpt": "Giá một chiếc pin laptop mới sẽ là không hề rẻ chút nào đối với những học sinh, sinh viên. Cho nên, không ít sinh viên nghĩ tới phương án sử dụng các loại pin laptop giá rẻ để tiết kiệm chi phí. Tuy nhiên, việc sử dụng loại pin giá rẻ này có thực sự tốt, nên hay không nên?\n",
    "published_at": "2021-07-13T09:52:56.941000",
    "slug": "pin-laptop-gia-re"
  },
  {
    "url_thumbnail": "https:\/\/static.beecost.vn\/upload\/uploads\/2020\/03\/1584427223.9663014..jpe",
    "category_id": 7372,
    "lst_category_base_id": [
      "1__100644",
      "3__1846",
      "4__2901"
    ],
    "lst_keyword": [
      "quạt tản gió"
    ],
    "id": 839702,
    "title": "Quạt tản gió là gì? Ưu nhược điểm của quạt tản gió",
    "excerpt": "Được sử dụng phổ biến, thế nhưng khi nhắc tới “quạt tản gió” đa số mọi người lại không hề biết chúng là gì? Bài viết này BeeCost sẽ giúp bạn hiểu hơn về khái niệm quạt tản gió cũng như những ưu và nhược điểm của chúng.\n",
    "published_at": "2021-07-13T09:52:56.941000",
    "slug": "quat-tan-gio-la-gi-uu-nhuoc-diem-cua-quat-tan-gio"
  },
  {
    "url_thumbnail": "https:\/\/static.beecost.vn\/upload\/uploads\/2020\/03\/1584427774.4921753..jpe",
    "category_id": 7401,
    "lst_category_base_id": [
      "1__100644",
      "3__1846",
      "4__2901"
    ],
    "lst_keyword": [
      "pin"
    ],
    "id": 840620,
    "title": "Hướng dẫn kiểm tra độ chai pin khi mua laptop cũ",
    "excerpt": "Ngoài cấu hình máy, màn hình, vỏ máy… thì pin laptop cũng được khá nhiều người quan tâm khi mua laptop cũ. Chính vì vậy BeeCost sẽ hướng dẫn kiểm tra độ chai pin khi mua laptop cũ để chọn được những chiếc laptop có pin chai ít nhất.\n",
    "published_at": "2021-07-13T09:52:56.941000",
    "slug": "huong-dan-kiem-tra-do-chai-pin-khi-mua-laptop-cu"
  }
]
</script>

<template>
  <div class="flex flex-nowrap overflow-auto scrollbar-hide space-x-2 lg:space-x-4 mr-4 lg:mr-0">
    <BlogRelatedCard v-for="blog in relatedBlogList" :key="blog.id" :blog="blog" />
  </div>
</template>
