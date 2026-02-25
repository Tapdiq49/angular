# Tətbiqinizə HTTP rabitəsini əlavə edin

Bu təlimat HTTP və bir API-nin tətbiqinizə necə inteqrasiya olunacağını nümayiş etdirir.

Bu ana qədər tətbiqiniz məlumatları bir Angular servisindəki statik massivdən oxuyub. Növbəti addım tətbiqinizin HTTP vasitəsilə əlaqə saxlayacağı bir JSON serverindən istifadə etməkdir. HTTP sorğusu serverlə məlumatlarla işləmək təcrübəsini simulyasiya edəcək.

<docs-video src="https://www.youtube.com/embed/5K10oYJ5Y-E?si=TiuNKx_teR9baO7k"/>

VACİB: Təlimatın bu addımı üçün yerli mühitinizdən istifadə etməyi tövsiyə edirik.

## Nə öyrənəcəksiniz

Tətbiqiniz bir JSON serverindən gələn məlumatları istifadə edəcək

<docs-workflow>

<docs-step title="JSON serverini konfiqurasiya edin">
JSON Server mock REST API-lər yaratmaq üçün istifadə olunan açıq mənbəli alətdir. Siz ondan hazırda housing servisində saxlanılan yaşayış yeri məlumatlarını təqdim etmək üçün istifadə edəcəksiniz.

1. Aşağıdakı əmrdən istifadə edərək npm-dən `json-server`-i quraşdırın.

   ```bash
   npm install -g json-server
   ```

1. Layihənizin kök qovluğunda `db.json` adlı fayl yaradın. Bura `json-server` üçün məlumatları saxlayacağınız yerdir.

1. `db.json` faylını açın və aşağıdakı kodu fayla kopyalayın

   ```json
   {
     "locations": [
       {
         "id": 0,
         "name": "Acme Fresh Start Housing",
         "city": "Chicago",
         "state": "IL",
         "photo": "https://angular.dev/assets/images/tutorials/common/bernard-hermant-CLKGGwIBTaY-unsplash.jpg",
         "availableUnits": 4,
         "wifi": true,
         "laundry": true
       },
       {
         "id": 1,
         "name": "A113 Transitional Housing",
         "city": "Santa Monica",
         "state": "CA",
         "photo": "https://angular.dev/assets/images/tutorials/common/brandon-griggs-wR11KBaB86U-unsplash.jpg",
         "availableUnits": 0,
         "wifi": false,
         "laundry": true
       },
       {
         "id": 2,
         "name": "Warm Beds Housing Support",
         "city": "Juneau",
         "state": "AK",
         "photo": "https://angular.dev/assets/images/tutorials/common/i-do-nothing-but-love-lAyXdl1-Wmc-unsplash.jpg",
         "availableUnits": 1,
         "wifi": false,
         "laundry": false
       },
       {
         "id": 3,
         "name": "Homesteady Housing",
         "city": "Chicago",
         "state": "IL",
         "photo": "https://angular.dev/assets/images/tutorials/common/ian-macdonald-W8z6aiwfi1E-unsplash.jpg",
         "availableUnits": 1,
         "wifi": true,
         "laundry": false
       },
       {
         "id": 4,
         "name": "Happy Homes Group",
         "city": "Gary",
         "state": "IN",
         "photo": "https://angular.dev/assets/images/tutorials/common/krzysztof-hepner-978RAXoXnH4-unsplash.jpg",
         "availableUnits": 1,
         "wifi": true,
         "laundry": false
       },
       {
         "id": 5,
         "name": "Hopeful Apartment Group",
         "city": "Oakland",
         "state": "CA",
         "photo": "https://angular.dev/assets/images/tutorials/common/r-architecture-JvQ0Q5IkeMM-unsplash.jpg",
         "availableUnits": 2,
         "wifi": true,
         "laundry": true
       },
       {
         "id": 6,
         "name": "Seriously Safe Towns",
         "city": "Oakland",
         "state": "CA",
         "photo": "https://angular.dev/assets/images/tutorials/common/phil-hearing-IYfp2Ixe9nM-unsplash.jpg",
         "availableUnits": 5,
         "wifi": true,
         "laundry": true
       },
       {
         "id": 7,
         "name": "Hopeful Housing Solutions",
         "city": "Oakland",
         "state": "CA",
         "photo": "https://angular.dev/assets/images/tutorials/common/r-architecture-GGupkreKwxA-unsplash.jpg",
         "availableUnits": 2,
         "wifi": true,
         "laundry": true
       },
       {
         "id": 8,
         "name": "Seriously Safe Towns",
         "city": "Oakland",
         "state": "CA",
         "photo": "https://angular.dev/assets/images/tutorials/common/saru-robert-9rP3mxf8qWI-unsplash.jpg",
         "availableUnits": 10,
         "wifi": false,
         "laundry": false
       },
       {
         "id": 9,
         "name": "Capital Safe Towns",
         "city": "Portland",
         "state": "OR",
         "photo": "https://angular.dev/assets/images/tutorials/common/webaliser-_TPTXZd9mOo-unsplash.jpg",
         "availableUnits": 6,
         "wifi": true,
         "laundry": true
       }
     ]
   }
   ```

1. Bu faylı yadda saxlayın.

1. Konfiqurasiyanızı test etmək vaxtıdır. Əmr satırından (command line), layihənizin kökündə aşağıdakı əmrləri işlədin.

   ```bash
   json-server --watch db.json
   ```

1. Veb brauzerinizdə `http://localhost:3000/locations` ünvanına keçin və cavabda `db.json` faylında saxlanılan məlumatların olduğunu təsdiqləyin.

Əgər konfiqurasiyanızla bağlı hər hansı probleminiz yaranarsa, [rəsmi sənədlərdə](https://www.npmjs.com/package/json-server) daha çox təfərrüat tapa bilərsiniz.
</docs-step>

<docs-step title="Servisi yerli massiv əvəzinə veb serverdən istifadə etmək üçün yeniləyin">
Məlumat mənbəyi konfiqurasiya edildi, növbəti addım veb tətbiqinizi ona qoşulmaq və məlumatları istifadə etmək üçün yeniləməkdir.

1.  `src/app/housing.service.ts` faylında aşağıdakı dəyişiklikləri edin:

1.  Kodu `housingLocationList` property-sini, məlumatları ehtiva edən massivi və `baseUrl` property-sini silmək üçün yeniləyin.

1.  `url` adlı string property əlavə edin və onun dəyərini `'http://localhost:3000/locations'` olaraq təyin edin

    <docs-code header="housing.service.ts faylına url property-si əlavə edin" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/housing.service.ts" visibleLines="[8]"/>

    Bu kod faylın qalan hissəsində xətalara səbəb olacaq, çünki o, `housingLocationList` property-sindən asılıdır. Növbəti olaraq servis metodlarını yeniləyəcəyik.

1.  Konfiqurasiya etdiyiniz veb serverə çağırış etmək üçün `getAllHousingLocations` funksiyasını yeniləyin.

     <docs-code header="housing.service.ts daxilində getAllHousingLocations metodunu yeniləyin" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/housing.service.ts" visibleLines="[10,13]"/>

    Kod indi HTTP üzərindən **GET** sorğusu etmək üçün asinxron koddan istifadə edir.

    FAYDALI: Bu nümunə üçün kod `fetch` istifadə edir. Daha mürəkkəb istifadə halları üçün Angular tərəfindən təmin edilən `HttpClient`-dən istifadə etməyi düşünün.

1.  Konfiqurasiya etdiyiniz veb serverə çağırış etmək üçün `getHousingLocationsById` funksiyasını yeniləyin.

    FAYDALI: Nəzərə alın ki, `fetch` metodu uyğun `id` property dəyəri olan məkən üçün məlumatları _sorğulamaq (query)_ üçün yenilənib. Daha çox məlumat üçün [URL Search Parameter](https://developer.mozilla.org/en-US/docs/Web/API/URL/search) bölməsinə baxın.

     <docs-code header="housing.service.ts daxilində getHousingLocationById metodunu yeniləyin" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/housing.service.ts" visibleLines="[15,19]"/>

1.  Bütün yeniləmələr tamamlandıqdan sonra yenilənmiş servisiniz aşağıdakı koda uyğun olmalıdır.

      <docs-code header="housing.service.ts faylının son versiyası" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/housing.service.ts" visibleLines="[1,25]" />

</docs-step>

<docs-step title="Komponentləri housing servisinə asinxron çağırışlar etmək üçün yeniləyin">
Server indi HTTP sorğusundan məlumatları oxuyur, lakin servisə arxalanan komponentlərdə xətalar var, çünki onlar servisin sinxron versiyasından istifadə etmək üçün proqramlaşdırılıblar.

1.  `src/app/home/home.ts` faylında `constructor`-ı `getAllHousingLocations` metodunun yeni asinxron versiyasından istifadə etmək üçün yeniləyin. Vəziyyətimiz (state) üçün sinyallardan (signals) istifadə etmədiyimiz üçün Angular-a sinxronizasiya tələb edən bir dəyişikliyin baş verdiyini bildirməlisiniz. Bunu etmək üçün `this.changeDetectorRef.markForCheck()` metodunu çağırın.

      <docs-code header="home.ts daxilində constructor-ı yeniləyin" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/home/home.ts" visibleLines="[30,38]"/>

1.  `src/app/details/details.ts` faylında `constructor`-ı `getHousingLocationById` metodunun yeni asinxron versiyasından istifadə etmək üçün yeniləyin. Əvvəlki kimi, dəyişikliklərdən Angular-ı xəbərdar etmək üçün `this.changeDetectorRef.markForCheck()` metodunu da çağırmalısınız.

      <docs-code header="details.ts daxilində constructor-ı yeniləyin" path="adev/src/content/tutorials/first-app/steps/14-http/src-final/app/details/details.ts" visibleLines="[60,66]"/>

1.  Kodunuzu yadda saxlayın.

1.  Tətbiqi brauzerdə açın və hər hansı bir xəta olmadan işlədiyini təsdiqləyin.
    </docs-step>

</docs-workflow>

QEYD: Bu dərs `fetch` brauzer API-sinə arxalanır. Interceptor-ların dəstəyi üçün zəhmət olmasa [Http Client sənədlərinə](/guide/http) müraciət edin.

XULASƏ: Bu dərsdə siz tətbiqinizi yerli veb serverdən (`json-server`) istifadə etmək və məlumatları əldə etmək üçün asinxron servis metodlarından istifadə etmək üçün yenilədiniz.

Təbriklər! Siz bu təlimatı uğurla tamamladınız və daha mürəkkəb Angular tətbiqləri qurmaq yolunda səyahətinizə davam etməyə hazırsınız.

Əgər daha çox öyrənmək istəyirsinizsə, Angular-ın digər proqramçı [təlimatlarını (tutorials)](tutorials) və [bələdçilərini (guides)](overview) tamamlamağı düşünün.
