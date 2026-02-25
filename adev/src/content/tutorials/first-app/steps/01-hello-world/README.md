# Salam dünya

Bu ilk dərs, bu təlimatdakı hər bir dərsin tam bir Angular tətbiqi qurmaq üçün yeni funksiyalar əlavə etdiyi başlanğıc nöqtəsi rolunu oynayır. Bu dərsdə biz tətbiqi məşhur "Hello World" (Salam Dünya) mətnini göstərmək üçün yeniləyəcəyik.

<docs-video src="https://www.youtube.com/embed/UnOwDuliqZA?si=uML-cDRbrxmYdD_9"/>

## Nə öyrənəcəksiniz

Bu dərsdən sonra yenilənmiş tətbiqiniz sizin və IDE-nizin bir Angular tətbiqi yaratmağa başlamağa hazır olduğunuzu təsdiqləyir.

QEYD: Əgər daxili redaktorla işləyirsinizsə, [dördüncü addıma](#hello-world-yaradın) keçin.
Brauzer playground-unda işləyərkən tətbiqi işə salmaq üçün `ng serve` etməyə ehtiyac yoxdur. `ng generate` kimi digər əmrlər sağınızdakı konsol pəncərəsində yerinə yetirilə bilər.

<docs-workflow>

<docs-step title="Standart tətbiqi yükləyin">
Kod redaktorunun yuxarı sağ hissəsindəki "Download" (Yüklə) ikonuna klikləməklə başlayın. Bu, bu təlimatın mənbə kodunu ehtiva edən `.zip` faylı yükləyəcək. Bunu yerli Terminal və IDE-nizdə açın, sonra standart tətbiqi test etməyə keçin.

Təlimatın istənilən addımında həmin addımın mənbə kodunu yükləmək və oradan başlamaq üçün bu ikonuna klikləyə bilərsiniz.
</docs-step>

<docs-step title="Standart tətbiqi test edin">
Bu addımda, standart başlanğıc tətbiqini yüklədikdən sonra onu qurursunuz.
Bu, inkişaf mühitinizin təlimatı davam etdirmək üçün lazım olan hər şeyə malik olduğunu təsdiqləyir.

IDE-nizin **Terminal** bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.
1. Tətbiqi işlətmək üçün lazım olan aslılıqları quraşdırmaq üçün bu əmri işlədin.

   ```shell
   npm install
   ```

1. Standart tətbiqi qurmaq və serverdə işə salmaq üçün bu əmri işlədin.

   ```shell
   ng serve
   ```

   Tətbiq xətasız qurulmalıdır.

1. İnkişaf etdirdiyiniz kompüterdə veb brauzerdə `http://localhost:4200` ünvanını açın.
1. Standart veb saytın brauzerdə göründüyünü təsdiqləyin.
1. Növbəti addımları tamamlayarkən `ng serve` əmrini işlək vəziyyətdə saxlaya bilərsiniz.
   </docs-step>

<docs-step title="Layihədəki faylları nəzərdən keçirin">
Bu addımda siz standart bir Angular tətbiqini təşkil edən fayllarla tanış olursunuz.

IDE-nizin **Explorer** (Fayl araşdırıcısı) bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.
1. Bu faylları görmək üçün `src` qovluğunu açın.
   1. Fayl araşdırıcısında Angular tətbiq fayllarını (`/src`) tapın.
      1. `index.html` tətbiqin ən üst səviyyəli HTML template-idir.
      1. `styles.css` tətbiqin ən üst səviyyəli üslub cədvəlidir (style sheet).
      1. `main.ts` tətbiqin işə başladığı yerdir.
      1. `favicon.ico` hər hansı bir veb saytda olduğu kimi tətbiqin ikonudur.
   1. Fayl araşdırıcısında Angular tətbiqinin komponent fayllarını (`/app`) tapın.
      1. `app.ts` `app-root` komponentini təsvir edən mənbə faylıdır.
         Bu, tətbiqdəki ən üst səviyyəli Angular komponentidir. Komponent bir Angular tətbiqinin əsas quruluş blokudur.
         Komponent təsvirinə komponentin kodu, HTML template-i və üslubları daxildir ki, bunlar bu faylda və ya ayrı-ayrı fayllarda təsvir oluna bilər.

         Bu tətbiqdə üslublar ayrı bir faylda, komponentin kodu və HTML template-i isə bu faylda yerləşir.

      1. `app.css` bu komponent üçün üslub cədvəlidir.
      1. Yeni komponentlər bu qovluğa əlavə edilir.

   1. Fayl araşdırıcısında tətbiq tərəfindən istifadə edilən şəkilləri ehtiva edən şəkil qovluğunu (`/assets`) tapın.
   1. Fayl araşdırıcısında Angular tətbiqinin qurulması və işləməsi üçün lazım olan, lakin normal olaraq qarşılıqlı əlaqədə olmadığınız faylları və qovluqları tapın.
      1. `.angular` Angular tətbiqini qurmaq üçün lazım olan fayllara malikdir.
      1. `.e2e` tətbiqi test etmək üçün istifadə olunan fayllara malikdir.
      1. `.node_modules` tətbiqin istifadə etdiyi node.js paketlərinə malikdir.
      1. `angular.json` Angular tətbiqini tətbiq qurma alətlərinə təsvir edir.
      1. `package.json` tamamlanmış tətbiqi işlətmək üçün `npm` (node package manager) tərəfindən istifadə olunur.
      1. `tsconfig.*` tətbiqin konfiqurasiyasını TypeScript kompilyatoruna təsvir edən fayllardır.

Bir Angular tətbiqi layihəsini təşkil edən faylları nəzərdən keçirdikdən sonra növbəti addıma keçin.
</docs-step>

<docs-step title="`Hello World` yaradın">
Bu addımda siz göstərilən məzmunu dəyişdirmək üçün Angular layihə fayllarını yeniləyirsiniz.

IDE-nizdə:

1. `first-app/src/index.html` faylını açın.
   QEYD: Bu və növbəti addım yalnız yerli mühitiniz üçündür!

1. `index.html` faylında tətbiqin başlığını yeniləmək üçün `<title>` elementini bu kodla əvəz edin.

   <docs-code header="src/index.html daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/02-Home/src/index.html" visibleLines="[5]"/>

   Sonra `index.html` faylına etdiyiniz dəyişiklikləri yadda saxlayın.

1. Növbəti olaraq `first-app/src/app/app.ts` faylını açın.
1. `app.ts` faylında `@Component` tərifində tətbiq komponentindəki mətni dəyişdirmək üçün `template` sətrini bu kodla əvəz edin.

   <docs-code language="angular-ts" header="src/app/app.ts daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/02-Home/src/app/app.ts" visibleLines="[6,8]"/>

1. `app.ts` faylında `App` class-ı tərifində komponent başlığını dəyişdirmək üçün `title` sətrini bu kodla əvəz edin.

   <docs-code header="src/app/app.ts daxilində əvəzləyin" path="adev/src/content/tutorials/first-app/steps/02-Home/src/app/app.ts" visibleLines="[11,13]"/>

   Sonra `app.ts` faylına etdiyiniz dəyişiklikləri yadda saxlayın.

1. Əgər 1-ci addımdakı `ng serve` əmrini dayandırmısınızsa, IDE-nizin **Terminal** pəncərəsində yenidən `ng serve` işlədin.
1. Brauzerinizi açın və `localhost:4200` ünvanına keçin və tətbiqin xətasız qurulduğunu, başlıqda _Homes_, tətbiqinizin gövdəsində isə _Hello world_ göründüyünü təsdiqləyin:
   <img alt="brauzer pəncərəsində 'Hello World' mətnini göstərən səhifə" src="assets/images/tutorials/first-app/homes-app-lesson-01-browser.png">
   </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz standart Angular tətbiqini _Hello world_ göstərmək üçün yenilədiniz.
Proses zamanı tətbiqinizi sınaq üçün yerli olaraq serverdə işlətmək üçün `ng serve` əmri haqqında öyrəndiniz.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="guide/components" title="Angular Komponentləri"/>
  <docs-pill href="tools/cli" title="Angular CLI ilə tətbiqlərin yaradılması"/>
</docs-pill-row>
