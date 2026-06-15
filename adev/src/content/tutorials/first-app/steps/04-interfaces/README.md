# İnterfeys yaratmaq

Bu təlimat dərsi bir interfeysin necə yaradılacağını və onun tətbiqinizin komponentinə necə daxil ediləcəyini nümayiş etdirir.

<docs-video src="https://www.youtube.com/embed/eM3zi_n7lNs?si=YkFSeUeV8Ixtz8pm"/>

## Nə öyrənəcəksiniz

- Tətbiqinizin məlumat tipi (data type) kimi istifadə edə biləcəyi yeni bir interfeysi var.
- Tətbiqinizin nümunə məlumatlarla birlikdə yeni interfeysin bir instansiyası (nüsxəsi) var.

## İnterfeyslərə konseptual baxış

[İnterfeyslər](https://www.typescriptlang.org/docs/handbook/interfaces.html) tətbiqiniz üçün xüsusi məlumat tipləridir.

Angular güclü tipli (strongly typed) proqramlaşdırma mühitində işləmək üstünlüklərindən yararlanmaq üçün TypeScript-dən istifadə edir.
Güclü tip yoxlaması tətbiqinizdəki bir elementin digərinə səhv formatlanmış məlumat göndərmə ehtimalını azaldır.
Belə tip uyğunsuzluğu xətaları TypeScript kompilyatoru tərəfindən tutulur və bir çox belə xətalar IDE-nizdə də tutula bilər.

Bu dərsdə siz tək bir yaşayış yeri haqqında məlumatları təmsil edən xüsusiyyətləri təyin etmək üçün bir interfeys yaradacaqsınız.

<docs-workflow>

<docs-step title="Yeni bir Angular interfeysi yaradın">
Bu addım tətbiqinizdə yeni bir interfeys yaradır.

IDE-nizin **Terminal** bölməsində:

1. Layihə qovluğunuzda `first-app` qovluğuna keçin.
1. `first-app` qovluğunda yeni interfeys yaratmaq üçün bu əmri işlədin:

   ```shell

   ng generate interface housinglocation

   ```

1. Tətbiqi qurmaq və `http://localhost:4200` ünvanında işə salmaq üçün `ng serve` işlədin.
1. Brauzerdə tətbiqinizi görmək üçün `http://localhost:4200` ünvanını açın.
1. Tətbiqin xətasız qurulduğunu təsdiqləyin.
   Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
   </docs-step>

<docs-step title="Yeni interfeysə xüsusiyyətlər (properties) əlavə edin">
Bu addım interfeysə tətbiqinizin yaşayış yerini təmsil etmək üçün ehtiyac duyduğu xüsusiyyətləri əlavə edir.

1.  IDE-nizin **Terminal** bölməsində, əgər artıq işləmirsə, tətbiqi qurmaq və `http://localhost:4200` ünvanında işə salmaq üçün `ng serve` əmrini başladın.
1.  IDE-nizin **Edit** (Redaktə) bölməsində `src/app/housinglocation.ts` faylını açın.
1.  `housinglocation.ts` faylında yeni interfeysinizi bu nümunəyə uyğunlaşdırmaq üçün standart məzmunu aşağıdakı kodla əvəz edin.

       <docs-code header="src/app/housinglocation.ts faylını bu koda uyğun yeniləyin" path="adev/src/content/tutorials/first-app/steps/05-inputs/src/app/housinglocation.ts" visibleLines="[1,10]" />

1.  Dəyişikliklərinizi yadda saxlayın və tətbiqin hər hansı bir xəta göstərmədiyini təsdiqləyin. Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.

Bu nöqtədə siz yaşayış yeri haqqında məlumatları, o cümlədən `id`, `name` və yerləşmə məlumatlarını təmsil edən bir interfeys təyin etdiniz.
</docs-step>

<docs-step title="Tətbiqiniz üçün bir test evi yaradın">
İnterfeysiniz var, lakin hələ ki ondan istifadə etmirsiniz.

Bu addımda siz interfeysin bir instansiyasını yaradırsınız və ona bəzi nümunə məlumatlar təyin edirsiniz.
Hələlik bu nümunə məlumatların tətbiqinizdə göründüyünü görməyəcəksiniz.
Bunun baş verməsi üçün tamamlanmalı olan daha bir neçə dərs var.

1.  IDE-nizin **Terminal** bölməsində, əgər artıq işləmirsə, tətbiqi qurmaq və `http://localhost:4200` ünvanında işə salmaq üçün `ng serve` əmrini işlədin.
1.  IDE-nizin **Edit** (Redaktə) bölməsində `src/app/home/home.ts` faylını açın.
1.  `src/app/home/home.ts` faylında mövcus `import` bəyanatlarından sonra bu import bəyanatını əlavə edin ki, `Home` komponenti yeni interfeysdən istifadə edə bilsin.

       <docs-code language="angular-ts" header="src/app/home/home.ts daxilində Home-u import edin" path="adev/src/content/tutorials/first-app/steps/05-inputs/src/app/home/home.ts" visibleLines="[3]"/>

1.  `src/app/home/home.ts` daxilində komponentdə yeni interfeysin tək bir instansiyasını yaratmaq üçün boş `export class Home {}` tərifini bu kodla əvəz edin.

       <docs-code language="angular-ts" header="src/app/home/home.ts daxilində nümunə məlumatlar əlavə edin" path="adev/src/content/tutorials/first-app/steps/05-inputs/src/app/home/home.ts" visibleLines="[22,35]"/>

1.  `home.ts` faylınızın bu nümunəyə uyğun gəldiyini təsdiqləyin.

       <docs-code language="angular-ts" header="src/app/home/home.ts" path="adev/src/content/tutorials/first-app/steps/05-inputs/src/app/home/home.ts" visibleLines="[[1,7],[9,36]]" />

    `HousingLocation` tipində `housingLocation` property-sini `Home` class-ına əlavə etməklə biz məlumatların interfeys təsvirinə uyğun gəldiyini təsdiqləyə bilirik. Əgər məlumatlar interfeys təsvirini qane etməsəydi, IDE bizə faydalı xətalar vermək üçün kifayət qədər məlumata sahib olur.

1.  Dəyişikliklərinizi yadda saxlayın və tətbiqdə xəta olmadığını təsdiqləyin. Brauzeri açın və tətbiqinizin hələ də "housing-location works!" mesajını göstərdiyini təsdiqləyin.

       <img alt="brauzer pəncərəsində homes-app-ın logo, filtr mətn giriş qutusu, axtarış düyməsi və 'housing-location works!' mesajını göstərən səhifə" src="assets/images/tutorials/first-app/homes-app-lesson-03-step-2.png">

1.  Növbəti addıma keçməzdən əvvəl hər hansı xətaları düzəldin.
    </docs-step>

</docs-workflow>

XULASƏ: Bu dərsdə siz tətbiqiniz üçün yeni bir məlumat tipi yaradan interfeys yaratdınız.
Bu yeni məlumat tipi sizə harda `HousingLocation` məlumatının tələb olunduğunu dəqiqləşdirməyə imkan verir.
Bu yeni məlumat tipi həmçinin IDE-nizə və TypeScript kompilyatoruna `HousingLocation` məlumatının tələb olunan yerdə istifadə edildiyinə əmin olmağa imkan verir.

Bu dərsdə əhatə olunmuş mövzular haqqında daha çox məlumat üçün buraya daxil olun:

<docs-pill-row>
  <docs-pill href="cli/generate/interface" title="ng generate interface"/>
  <docs-pill href="cli/generate" title="ng generate"/>
</docs-pill-row>
