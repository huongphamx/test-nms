from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_category_list():
    return {
  "status": "success",
  "data": {
    "categories": [
      {
        "category_base_id": "1__100017",
        "slug": "thoi-trang-nu",
        "name": "Thời Trang Nữ",
        "url_thumbnail": "https://cf.shopee.vn/file/75ea42f9eca124e9cb3cde744c060e4d",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100108",
            "slug": "ao-len",
            "name": "Áo len",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100103",
            "slug": "quan-jeans",
            "name": "Quần jeans",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100105",
            "slug": "vay-cuoi",
            "name": "Váy cưới",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100115",
            "slug": "do-hoa-trang",
            "name": "Đồ hóa trang",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100116",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100104",
            "slug": "dam",
            "name": "Đầm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100102",
            "slug": "vay",
            "name": "Váy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100099",
            "slug": "ao",
            "name": "Áo",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100100",
            "slug": "quan",
            "name": "Quần",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100101",
            "slug": "quan-dui",
            "name": "Quần đùi",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100106",
            "slug": "do-lien-than",
            "name": "Đồ liền thân",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100107",
            "slug": "ao-khoac",
            "name": "Áo khoác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100109",
            "slug": "hoodie-va-ao-ni",
            "name": "Hoodie và Áo nỉ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100110",
            "slug": "bo",
            "name": "Bộ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100111",
            "slug": "do-lot",
            "name": "Đồ lót",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100112",
            "slug": "do-ngu",
            "name": "Đồ ngủ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100113",
            "slug": "do-bau",
            "name": "Đồ Bầu",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100114",
            "slug": "do-truyen-thong",
            "name": "Đồ truyền thống",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100117",
            "slug": "vai",
            "name": "Vải",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          },
          {
            "category_base_id": "1__100118",
            "slug": "vo-tat",
            "name": "Vớ/ Tất",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100017",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100012",
        "slug": "giay-dep-nam",
        "name": "Giày Dép Nam",
        "url_thumbnail": "https://cf.shopee.vn/file/74ca517e1fa74dc4d974e5d03c3139de",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100067",
            "slug": "giay-oxfords-giay-buoc-day",
            "name": "Giày Oxfords & Giày buộc dây",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100064",
            "slug": "giay-the-thao-sneakers",
            "name": "Giày thể thao/ Sneakers",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100065",
            "slug": "giay-suc",
            "name": "Giày sục",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100070",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100066",
            "slug": "giay-tay-luoi",
            "name": "Giày tây lười",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100063",
            "slug": "bot",
            "name": "Bốt",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100068",
            "slug": "xang-dan-dep",
            "name": "Xăng-đan & Dép",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          },
          {
            "category_base_id": "1__100069",
            "slug": "phu-kien-giay-dep",
            "name": "Phụ kiện giày dép",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100012",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100533",
        "slug": "tui-vi-nam",
        "name": "Túi Ví Nam",
        "url_thumbnail": "https://cf.shopee.vn/file/18fd9d878ad946db2f1bf4e33760c86f",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100566",
            "slug": "tui-tote",
            "name": "Túi tote",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100567",
            "slug": "cap-xach-cong-so",
            "name": "Cặp xách công sở",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100568",
            "slug": "vi-cam-tay",
            "name": "Ví cầm tay",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100564",
            "slug": "ba-lo",
            "name": "Ba lô",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100570",
            "slug": "tui-deo-cheo",
            "name": "Túi đeo chéo",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100569",
            "slug": "tui-deo-hong-tui-deo-nguc",
            "name": "Túi đeo hông & Túi đeo ngực",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100565",
            "slug": "cap-laptop",
            "name": "Cặp laptop",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100571",
            "slug": "bop-vi",
            "name": "Bóp/ Ví",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          },
          {
            "category_base_id": "1__100572",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100533",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100630",
        "slug": "sac-dep",
        "name": "Sắc Đẹp",
        "url_thumbnail": "https://cf.shopee.vn/file/c765998fda99b2be9eb6e348df29af28",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100666",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100665",
            "slug": "bo-san-pham-lam-dep",
            "name": "Bộ sản phẩm làm đẹp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100661",
            "slug": "nuoc-hoa",
            "name": "Nước hoa",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100658",
            "slug": "cham-soc-tay-chan-mong",
            "name": "Chăm sóc tay, chân & móng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100659",
            "slug": "cham-soc-toc",
            "name": "Chăm sóc tóc",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100660",
            "slug": "cham-soc-nam-gioi",
            "name": "Chăm sóc nam giới",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100662",
            "slug": "trang-diem",
            "name": "Trang điểm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100663",
            "slug": "dung-cu-lam-dep",
            "name": "Dụng cụ làm đẹp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__100664",
            "slug": "cham-soc-da-mat",
            "name": "Chăm sóc da mặt",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          },
          {
            "category_base_id": "1__102002",
            "slug": "tam-cham-soc-co-the",
            "name": "Tắm & chăm sóc cơ thể",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100630",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100631",
        "slug": "cham-soc-thu-cung",
        "name": "Chăm Sóc Thú Cưng",
        "url_thumbnail": "https://cf.shopee.vn/file/cdf21b1bf4bfff257efe29054ecea1ec",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100673",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100667",
            "slug": "thuc-an-cho-thu-cung",
            "name": "Thức ăn cho thú cưng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100668",
            "slug": "phu-kien-cho-thu-cung",
            "name": "Phụ kiện cho thú cưng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100669",
            "slug": "ve-sinh-cho-thu-cung",
            "name": "Vệ sinh cho thú cưng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100670",
            "slug": "lam-dep-cho-thu-cung",
            "name": "Làm đẹp cho thú cưng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100671",
            "slug": "quan-ao-phu-kien",
            "name": "Quần áo & phụ kiện",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          },
          {
            "category_base_id": "1__100672",
            "slug": "cham-soc-suc-khoe",
            "name": "Chăm sóc sức khỏe",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100631",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100633",
        "slug": "thoi-trang-tre-em-tre-so-sinh",
        "name": "Thời trang trẻ em & trẻ sơ sinh",
        "url_thumbnail": "https://cf.shopee.vn/file/4540f87aa3cbe99db739f9e8dd2cdaf0",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100694",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100688",
            "slug": "bao-tay-tre-em-tat",
            "name": "Bao tay trẻ em & Tất",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100687",
            "slug": "quan-ao-tre-em",
            "name": "Quần áo trẻ em",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100689",
            "slug": "phu-kien-tre-em-tre-so-sinh",
            "name": "Phụ kiện trẻ em & trẻ sơ sinh",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100690",
            "slug": "quan-ao-be-trai",
            "name": "Quần áo bé trai",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100691",
            "slug": "quan-ao-be-gai",
            "name": "Quần áo bé gái",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100692",
            "slug": "giay-be-trai",
            "name": "Giày bé trai",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          },
          {
            "category_base_id": "1__100693",
            "slug": "giay-be-gai",
            "name": "Giày bé gái",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100633",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100632",
        "slug": "me-be",
        "name": "Mẹ & Bé",
        "url_thumbnail": "https://cf.shopee.vn/file/099edde1ab31df35bc255912bab54a5e",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100686",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100685",
            "slug": "bo-goi-qua-tang",
            "name": "Bộ & Gói quà tặng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100674",
            "slug": "do-dung-du-lich-cho-be",
            "name": "Đồ dùng du lịch cho bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100675",
            "slug": "do-dung-an-dam-cho-be",
            "name": "Đồ dùng ăn dặm cho bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100676",
            "slug": "phu-kien-cho-me",
            "name": "Phụ kiện cho mẹ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100677",
            "slug": "cham-soc-suc-khoe-me",
            "name": "Chăm sóc sức khỏe mẹ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100678",
            "slug": "do-dung-phong-tam-cham-soc-co-the-be",
            "name": "Đồ dùng phòng tắm & Chăm sóc cơ thể bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100679",
            "slug": "do-dung-phong-ngu-cho-be",
            "name": "Đồ dùng phòng ngủ cho bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100680",
            "slug": "an-toan-cho-be",
            "name": "An toàn cho bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100681",
            "slug": "sua-cong-thuc-thuc-pham-cho-be",
            "name": "Sữa công thức & Thực phẩm cho bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100682",
            "slug": "cham-soc-suc-khoe-be",
            "name": "Chăm sóc sức khỏe bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100683",
            "slug": "ta-bo-em-be",
            "name": "Tã & bô em bé",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          },
          {
            "category_base_id": "1__100684",
            "slug": "do-choi",
            "name": "Đồ chơi",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100632",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100637",
        "slug": "the-thao-da-ngoai",
        "name": "Thể Thao & Dã Ngoại",
        "url_thumbnail": "https://cf.shopee.vn/file/6cb7e633f8b63757463b676bd19a50e4",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100729",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100637",
            "relative_path": None
          },
          {
            "category_base_id": "1__100725",
            "slug": "dung-cu-the-thao-da-ngoai",
            "name": "Dụng Cụ Thể Thao & Dã Ngoại",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100637",
            "relative_path": None
          },
          {
            "category_base_id": "1__100726",
            "slug": "giay-the-thao",
            "name": "Giày Thể Thao",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100637",
            "relative_path": None
          },
          {
            "category_base_id": "1__100727",
            "slug": "thoi-trang-the-thao-da-ngoai",
            "name": "Thời Trang Thể Thao & Dã Ngoại",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100637",
            "relative_path": None
          },
          {
            "category_base_id": "1__100728",
            "slug": "phu-kien-the-thao-da-ngoai",
            "name": "Phụ Kiện Thể Thao & Dã Ngoại",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100637",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100636",
        "slug": "nha-cua-doi-song",
        "name": "Nhà cửa & Đời sống",
        "url_thumbnail": "https://cf.shopee.vn/file/24b194a695ea59d384768b7b471d563f",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100723",
            "slug": "do-tho-cung-do-phong-thuy",
            "name": "Đồ thờ cúng, đồ phong thủy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100712",
            "slug": "tui-lam-am",
            "name": "Túi làm ấm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100719",
            "slug": "den",
            "name": "Đèn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100724",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100708",
            "slug": "chat-khu-mui-lam-thom-nha",
            "name": "Chất khử mùi, làm thơm nhà",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100709",
            "slug": "do-dung-phong-tam",
            "name": "Đồ dùng phòng tắm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100710",
            "slug": "chan-ga-goi-nem",
            "name": "Chăn ga gối nệm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100711",
            "slug": "trang-tri-nha-cua",
            "name": "Trang trí nhà cửa",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100713",
            "slug": "noi-that",
            "name": "Nội thất",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100714",
            "slug": "lam-vuon",
            "name": "Làm vườn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100715",
            "slug": "dung-cu-thiet-bi-tien-ich",
            "name": "Dụng cụ & Thiết bị tiện ích",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100716",
            "slug": "dung-cu-cham-soc-nha-cua",
            "name": "Dụng cụ chăm sóc nhà cửa",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100717",
            "slug": "dung-cu-nha-bep",
            "name": "Dụng cụ nhà bếp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100718",
            "slug": "bo-do-ban-an",
            "name": "Bộ đồ bàn ăn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100720",
            "slug": "bao-ho-gia-dinh",
            "name": "Bảo hộ gia đình",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100721",
            "slug": "sap-xep-nha-cua",
            "name": "Sắp xếp nhà cửa",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          },
          {
            "category_base_id": "1__100722",
            "slug": "trang-tri-tiec-tung",
            "name": "Trang trí tiệc tùng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100636",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100641",
        "slug": "mo-to-xe-may",
        "name": "Mô tô, xe máy",
        "url_thumbnail": "https://cf.shopee.vn/file/3fb459e3449905545701b418e8220334",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100758",
            "slug": "mu-bao-hiem-phu-kien",
            "name": "Mũ bảo hiểm & Phụ kiện",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100641",
            "relative_path": None
          },
          {
            "category_base_id": "1__100755",
            "slug": "mo-to-xe-may",
            "name": "Mô tô, xe máy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100641",
            "relative_path": None
          },
          {
            "category_base_id": "1__100759",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100641",
            "relative_path": None
          },
          {
            "category_base_id": "1__100756",
            "slug": "phu-kien-xe-may",
            "name": "Phụ kiện xe máy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100641",
            "relative_path": None
          },
          {
            "category_base_id": "1__100757",
            "slug": "phu-tung-xe-may",
            "name": "Phụ tùng xe máy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100641",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100644",
        "slug": "may-tinh-laptop",
        "name": "Máy tính & Laptop",
        "url_thumbnail": "https://cf.shopee.vn/file/c3f3edfaa9f6dafc4825b77d8449999d",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__101943",
            "slug": "phu-kien-may-tinh-khac",
            "name": "Phụ Kiện Máy Tính Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101933",
            "slug": "man-hinh",
            "name": "Màn Hình",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101937",
            "slug": "phan-mem",
            "name": "Phần Mềm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101942",
            "slug": "laptop",
            "name": "Laptop",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101932",
            "slug": "may-tinh-ban",
            "name": "Máy Tính Bàn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101934",
            "slug": "linh-kien-may-tinh",
            "name": "Linh Kiện Máy Tính",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101935",
            "slug": "thiet-bi-luu-tru",
            "name": "Thiết Bị Lưu Trữ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101936",
            "slug": "thiet-bi-mang",
            "name": "Thiết Bị Mạng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101938",
            "slug": "thiet-bi-van-phong",
            "name": "Thiết Bị Văn Phòng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101939",
            "slug": "may-in-may-scan",
            "name": "Máy In & Máy Scan",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101940",
            "slug": "phu-kien-may-tinh",
            "name": "Phụ Kiện Máy Tính",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          },
          {
            "category_base_id": "1__101941",
            "slug": "chuot-ban-phim",
            "name": "Chuột & Bàn Phím",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100644",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100643",
        "slug": "sach-tap-chi",
        "name": "Sách & Tạp Chí",
        "url_thumbnail": "https://cf.shopee.vn/file/36013311815c55d303b0e6c62d6a8139",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100779",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100643",
            "relative_path": None
          },
          {
            "category_base_id": "1__100776",
            "slug": "tap-chi-bao-giay",
            "name": "Tạp Chí & Báo Giấy",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100643",
            "relative_path": None
          },
          {
            "category_base_id": "1__100777",
            "slug": "sach",
            "name": "Sách",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100643",
            "relative_path": None
          },
          {
            "category_base_id": "1__100778",
            "slug": "e-books",
            "name": "E-Books",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100643",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100001",
        "slug": "suc-khoe",
        "name": "Sức Khỏe",
        "url_thumbnail": "https://cf.shopee.vn/file/bf87b50b463f646bb7fb8a1a606d9ed2",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100008",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100001",
            "relative_path": None
          },
          {
            "category_base_id": "1__100002",
            "slug": "thuc-pham-chuc-nang",
            "name": "Thực phẩm chức năng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100001",
            "relative_path": None
          },
          {
            "category_base_id": "1__100018",
            "slug": "vat-tu-y-te",
            "name": "Vật tư y tế",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100001",
            "relative_path": None
          },
          {
            "category_base_id": "1__100019",
            "slug": "cham-soc-ca-nhan",
            "name": "Chăm sóc cá nhân",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100001",
            "relative_path": None
          },
          {
            "category_base_id": "1__100020",
            "slug": "ho-tro-tinh-duc",
            "name": "Hỗ trợ tình dục",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100001",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100642",
        "slug": "voucher-dich-vu",
        "name": "Voucher & Dịch vụ",
        "url_thumbnail": "https://cf.shopee.vn/file/b0f78c3136d2d78d49af71dd1c3f38c1",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100767",
            "slug": "khoa-hoc",
            "name": "Khóa học",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100775",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100760",
            "slug": "su-kien-giai-tri",
            "name": "Sự kiện & Giải trí",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100761",
            "slug": "nha-hang-an-uong",
            "name": "Nhà hàng & Ăn uống",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100762",
            "slug": "mua-sam",
            "name": "Mua sắm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100764",
            "slug": "dich-vu-khac",
            "name": "Dịch vụ khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100765",
            "slug": "suc-khoe-lam-dep",
            "name": "Sức khỏe & Làm đẹp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100766",
            "slug": "goi-xe",
            "name": "Gọi xe",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100768",
            "slug": "nap-tien-tai-khoan",
            "name": "Nạp tiền tài khoản",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100769",
            "slug": "du-lich-khach-san",
            "name": "Du lịch & Khách sạn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100770",
            "slug": "tien-dien-tu",
            "name": "Tiền điện tử",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100771",
            "slug": "bat-dong-san",
            "name": "Bất động sản",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100772",
            "slug": "the-game",
            "name": "Thẻ game",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100773",
            "slug": "streaming",
            "name": "Streaming",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100774",
            "slug": "ma-qua-tang-shopee",
            "name": "Mã quà tặng Shopee",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          },
          {
            "category_base_id": "1__100763",
            "slug": "thanh-toan-hoa-don",
            "name": "Thanh toán hóa đơn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100642",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100010",
        "slug": "thiet-bi-dien-gia-dung",
        "name": "Thiết Bị Điện Gia Dụng",
        "url_thumbnail": "https://cf.shopee.vn/file/7abfbfee3c4844652b4a8245e473d857",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100046",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100043",
            "slug": "pin",
            "name": "Pin",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100045",
            "slug": "thiet-bi-dieu-khien-tu-xa",
            "name": "Thiết bị điều khiển từ xa",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100037",
            "slug": "may-chieu-phu-kien",
            "name": "Máy chiếu & Phụ kiện",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100038",
            "slug": "thiet-bi-dien-gia-dung-nho",
            "name": "Thiết bị điện gia dụng nhỏ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100039",
            "slug": "thiet-bi-dien-gia-dung-lon",
            "name": "Thiết bị điện gia dụng lớn",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100040",
            "slug": "tivi-phu-kien",
            "name": "Tivi & Phụ kiện",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100041",
            "slug": "do-gia-dung-nha-bep",
            "name": "Đồ gia dụng nhà bếp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100042",
            "slug": "mach-dien-phu-tung",
            "name": "Mạch điện & Phụ tùng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          },
          {
            "category_base_id": "1__100044",
            "slug": "thuoc-la-dien-tu",
            "name": "Thuốc lá điện tử",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100010",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100534",
        "slug": "dong-ho",
        "name": "Đồng Hồ",
        "url_thumbnail": "https://cf.shopee.vn/file/86c294aae72ca1db5f541790f7796260",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100577",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100534",
            "relative_path": None
          },
          {
            "category_base_id": "1__100575",
            "slug": "bo-dong-ho-dong-ho-cap",
            "name": "Bộ đồng hồ & Đồng hồ cặp",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100534",
            "relative_path": None
          },
          {
            "category_base_id": "1__100574",
            "slug": "dong-ho-nam",
            "name": "Đồng hồ nam",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100534",
            "relative_path": None
          },
          {
            "category_base_id": "1__100573",
            "slug": "dong-ho-nu",
            "name": "Đồng hồ nữ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100534",
            "relative_path": None
          },
          {
            "category_base_id": "1__100576",
            "slug": "phu-kien-dong-ho",
            "name": "Phụ kiện đồng hồ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100534",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100011",
        "slug": "thoi-trang-nam",
        "name": "Thời Trang Nam",
        "url_thumbnail": "https://cf.shopee.vn/file/687f3967b7c2fe6a134a2c11894eea4b",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100061",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100056",
            "slug": "do-ngu",
            "name": "Đồ ngủ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100062",
            "slug": "vo-tat",
            "name": "Vớ/ Tất",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100060",
            "slug": "trang-phuc-nganh-nghe",
            "name": "Trang phục ngành nghề",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100059",
            "slug": "do-hoa-trang",
            "name": "Đồ hóa trang",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100047",
            "slug": "quan-jean",
            "name": "Quần jean",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100057",
            "slug": "bo",
            "name": "Bộ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100053",
            "slug": "quan-dui",
            "name": "Quần đùi",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100049",
            "slug": "ao-len",
            "name": "Áo len",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100048",
            "slug": "hoodie-ao-ni",
            "name": "Hoodie & Áo nỉ",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100050",
            "slug": "ao-khoac",
            "name": "Áo khoác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100051",
            "slug": "com-le",
            "name": "Com lê",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100052",
            "slug": "quan-dai",
            "name": "Quần dài",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100054",
            "slug": "ao",
            "name": "Áo",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100055",
            "slug": "do-lot",
            "name": "Đồ lót",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          },
          {
            "category_base_id": "1__100058",
            "slug": "trang-phuc-truyen-thong",
            "name": "Trang phục truyền thống",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100011",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100016",
        "slug": "tui-vi-nu",
        "name": "Túi Ví Nữ",
        "url_thumbnail": "https://cf.shopee.vn/file/fa6ada2555e8e51f369718bbc92ccc52",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100098",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100091",
            "slug": "vi-du-tiec-vi-cam-tay",
            "name": "Ví dự tiệc & Ví cầm tay",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100095",
            "slug": "tui-deo-cheo-tui-deo-vai",
            "name": "Túi đeo chéo & Túi đeo vai",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100092",
            "slug": "tui-deo-hong-tui-deo-nguc",
            "name": "Túi đeo hông & Túi đeo ngực",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100093",
            "slug": "tui-tote",
            "name": "Túi tote",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100089",
            "slug": "ba-lo",
            "name": "Ba lô",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100094",
            "slug": "tui-quai-xach",
            "name": "Túi quai xách",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100090",
            "slug": "cap-laptop",
            "name": "Cặp laptop",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100096",
            "slug": "vi",
            "name": "Ví",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          },
          {
            "category_base_id": "1__100097",
            "slug": "phu-kien-tui",
            "name": "Phụ kiện túi",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100016",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100532",
        "slug": "giay-dep-nu",
        "name": "Giày Dép Nữ",
        "url_thumbnail": "https://cf.shopee.vn/file/48630b7c76a7b62bc070c9e227097847",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100560",
            "slug": "giay-de-xuong",
            "name": "Giày đế xuồng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100557",
            "slug": "giay-the-thao-sneaker",
            "name": "Giày thể thao/ sneaker",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100559",
            "slug": "giay-cao-got",
            "name": "Giày cao gót",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100563",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100556",
            "slug": "bot",
            "name": "Bốt",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100558",
            "slug": "giay-de-bang",
            "name": "Giày đế bằng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100561",
            "slug": "xang-dan-va-dep",
            "name": "Xăng-đan và dép",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          },
          {
            "category_base_id": "1__100562",
            "slug": "phu-kien-cham-soc-giay",
            "name": "Phụ kiện & chăm sóc giày",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100532",
            "relative_path": None
          }
        ]
      },
      {
        "category_base_id": "1__100013",
        "slug": "dien-thoai-phu-kien",
        "name": "Điện Thoại & Phụ Kiện",
        "url_thumbnail": "https://cf.shopee.vn/file/31234a27876fb89cd522d7e3db1ba5ca",
        "cat_level": 0,
        "parent_category_id": None,
        "relative_path": None,
        "childs": [
          {
            "category_base_id": "1__100072",
            "slug": "may-tinh-bang",
            "name": "Máy tính bảng",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100077",
            "slug": "khac",
            "name": "Khác",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100076",
            "slug": "bo-dam",
            "name": "Bộ đàm",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100071",
            "slug": "the-sim",
            "name": "Thẻ sim",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100073",
            "slug": "dien-thoai",
            "name": "Điện thoại",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100074",
            "slug": "thiet-bi-deo-thong-minh",
            "name": "Thiết bị đeo thông minh",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          },
          {
            "category_base_id": "1__100075",
            "slug": "phu-kien",
            "name": "Phụ kiện",
            "url_thumbnail": "https://i.imgur.com/LZZhAkE.png",
            "cat_level": 1,
            "parent_category_id": "1__100013",
            "relative_path": None
          }
        ]
      }
    ]
  }
}