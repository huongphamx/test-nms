<script lang="ts" setup>

</script>

<template>
  <div>
    <div class="py-3 md:py-4 md:border-b">
      <div class="max-w-7xl mx-auto flex px-4 lg:px-0">
        <NuxtLink to="/">
          <img
            src="https://lh3.googleusercontent.com/pw/ADCreHd5PMvwKUSbjtSRpUfeyDaazAbdXF1H0arvHtS62AyfivDEAN6hRSq-GTJ6wKiyn-9IEr63aaiNtFq6J2fP_I6VtpGAIwqAQu4B2mL64M2h2HHkPY4VhRWoDpag5VXN3Dxtwb277ZDkXPa0mnDxTTGL=w512"
            alt="logo" class="h-8 lg:h-12">
        </NuxtLink>
        <div class="hidden border rounded-full px-5 py-1 w-full max-w-xl mx-auto lg:flex items-center">
          <input type="text" placeholder="Dán link hoặc tìm sản phẩm" class="flex-1 focus:outline-none">
          <UIcon name="i-ph-magnifying-glass" />
        </div>
        <div class="hidden lg:flex items-center gap-3">
          <ModalMenu />
          <NuxtLink to="/blog">BLOG</NuxtLink>
        </div>
      </div>
    </div>
    <slot />
    <div class="border-t-4 border-orange-500 bg-gray-100">
      <div class="py-8 lg:py-16 px-4 max-w-7xl mx-auto">
        <div class="xl:grid xl:grid-cols-12 xl:gap-8">
          <div class="xl:col-span-5 xl:mr-10">
            <div class="flex flex-wrap items-center space-x-2 pb-3">
              <img class="h-10"
                src="https://lh3.googleusercontent.com/pw/ADCreHe1uaXgFtO8dlQi1fSrqmcu7OPYJYtSDgXclZin8jZ7oMkHSNc20AqAt7f3wnxrneK1VtZe0s9R7e2476DKCTes06oqHbdx41zz-o15Nf9ggs3HHqGC2K8Ym-dgGvem2sd_03jB8KlUf2MDyq4GOTH_=w256"
                alt="">
            </div>
            <p class="text-gray-500">
              <span>
                Mua Thông Minh là website, ứng dụng tìm kiếm và đánh giá hàng hóa sản phẩm online.
                Giúp bạn né Sale ảo, mua giá tốt, tin cậy và trở thành người tiêu dùng thông thái.
              </span>
              <span class="font-medium text-gray-600">MuaThongMinh.vn không bán hàng!</span>
            </p>
            <p class="mt-3 mb-2 text-gray-500">KẾT NỐI VỚI CHÚNG TÔI</p>
            <div class="flex space-x-6 pb-2">

            </div>
          </div>
          <div class="grid grid-cols-1 gap-8 xl:mt-0 xl:col-span-7 mt-12">
            <div class="md:grid md:grid-cols-2 md:gap-8">
              <div>
                <div class="text-sm font-semibold text-gray-400 tracking-wider uppercase">VỀ MUA THÔNG MINH</div>
                <ul class="mt-4 space-y-4">
                  <li>
                    <NuxtLink to="/blog">Blog</NuxtLink>
                  </li>
                  <li>
                    <NuxtLink to="/about">Giới thiệu</NuxtLink>
                  </li>
                  <li>
                    <NuxtLink to="/privacy">Chính sách bảo mật</NuxtLink>
                  </li>
                  <li>
                    <NuxtLink to="https://metric.vn" target="_blank">Metric</NuxtLink>
                  </li>
                  <li>
                    <NuxtLink to="https://diemthi.beecost.vn" target="_blank">Điểm thi</NuxtLink>
                  </li>
                </ul>
              </div>
              <div class="mt-12 md:mt-0">
                <div class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Liên hệ</div>
                <div class="mt-4 space-y-1">
                  <p class="text-base text-gray-500 font-semibold">Công ty Cổ phần Khoa học Dữ liệu</p>
                  <p class="text-base text-gray-500">Số ĐKKD: 0108677693</p>
                  <p class="text-base text-gray-500">Địa chỉ: Tầng 6 toà nhà AZ Lâm Viên, 107A Nguyễn Phong Sắc, Phường
                    Dịch Vọng Hậu, Quận Cầu Giấy, Thành phố Hà Nội, Việt Nam.</p>
                  <p class="text-base text-gray-500">Email: info@beecost.com</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <UDivider class="my-4" />
        <div class="flex flex-wrap text-gray-500 items-center justify-center my-2 text-sm">
          <span>Quốc gia & Khu vực:</span>
          <a href="https://beecost.vn" target="_self" rel="noopener" title="Việt Nam"
            class="hover:text-gray-600 px-2">Việt Nam</a>
          <a href="https://beecost.sg" target="_blank" rel="noopener" title="Singapore"
            class="hover:text-gray-600 px-2 border-l">Singapore</a>
          <a href="https://beecost.ph" target="_blank" rel="noopener" title="Philippines"
            class="hover:text-gray-600 px-2 border-l">Philippines</a>
          <a href="https://beecost.com.my" target="_blank" rel="noopener" title="Malaysia"
            class="hover:text-gray-600 px-2 border-l">Malaysia</a>
          <a href="https://beecost.co.id" target="_blank" rel="noopener" title="Indonesia"
            class="hover:text-gray-600 px-2 border-l">Indonesia</a><a href="https://beecost.tw" target="_blank"
            rel="noopener" title="Đài Loan" class="hover:text-gray-600 px-2 border-l">Đài Loan</a>
          <a href="https://beecost.com.mx" target="_blank" rel="noopener" title="Mexico"
            class="hover:text-gray-600 px-2 border-l">Mexico</a><a href="https://beecost.com.br" target="_blank"
            rel="noopener" title="Brazil" class="hover:text-gray-600 px-2 border-l">Brazil</a>
          <a href="https://thai.beecost.com" target="_blank" rel="noopener" title="Thái Lan"
            class="hover:text-gray-600 px-2 border-l">Thái Lan</a>
        </div>
      </div>
    </div>
  </div>
</template>
