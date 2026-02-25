# Şəkillərin optimallaşdırılması

Şəkillər bir çox tətbiqlərin vacib hissəsidir və tətbiqin performans problemlərinə, o cümlədən aşağı [Core Web Vitals](https://web.dev/explore/learn-core-web-vitals) ballarına səbəb olan əsas amillərdən biri ola bilər.

Şəkillərin optimallaşdırılması mürəkkəb mövzu ola bilər, lakin Angular `NgOptimizedImage` direktivi ilə bunun böyük hissəsini sizin üçün həll edir.

QEYD: [Ətraflı bələdçidə NgOptimizedImage ilə şəkil optimallaşdırılması](/guide/image-optimization) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz şəkillərinizin səmərəli şəkildə yüklənməsini təmin etmək üçün `NgOptimizedImage` direktivindən necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="NgOptimizedImage direktivini import edin">

`NgOptimizedImage` direktivindən yararlanmaq üçün əvvəlcə onu `@angular/common` kitabxanasından import edin və komponentin `imports` massivinə əlavə edin.

```ts
import { NgOptimizedImage } from '@angular/common';

@Component({
  imports: [NgOptimizedImage],
  ...
})
```

</docs-step>

<docs-step title="src attribute-unu ngSrc ilə əvəz edin">

`NgOptimizedImage` direktivini aktivləşdirmək üçün `src` attribute-unu `ngSrc` ilə dəyişdirin. Bu həm statik şəkil mənbələri (yəni `src`), həm də dinamik şəkil mənbələri (yəni `[src]`) üçün keçərlidir.

```angular-ts {highlight:[[7],[11]]}
import { NgOptimizedImage } from '@angular/common';

@Component({
template: `     ...
    <li>
      Statik Şəkil:
      <img ngSrc="/logo.svg" alt="Angular logosu" width="32" height="32" />
    </li>
    <li>
      Dinamik Şəkil:
      <img [ngSrc]="logoUrl" [alt]="logoAlt" width="32" height="32" />
    </li>
    ...
  `,
imports: [NgOptimizedImage],
})
```

</docs-step>

<docs-step title="Width və height attribute-larını əlavə edin">

Nəzərə alın ki, yuxarıdakı kod nümunəsində hər bir şəkil həm `width`, həm də `height` attribute-larına malikdir. [Layout shift](https://web.dev/articles/cls) (maket sürüşməsi) qarşısını almaq üçün `NgOptimizedImage` direktivi hər bir şəkildə hər iki ölçü attribute-unun olmasını tələb edir.

Şəkillər üçün statik `height` və `width` göstərə bilmədiyiniz və ya istəmədiyiniz hallarda, şəklin valideyn elementini dolduran "fon şəkli" kimi davranmasını təmin etmək üçün [`fill` attribute-undan](https://web.dev/articles/cls) istifadə edə bilərsiniz:

```angular-html
// Konteyner div 'position: "relative"' üslubuna malikdir
<div class="image-container">
  <img ngSrc="www.example.com/image.png" fill />
</div>
```

QEYD: `fill` parametrli şəklin düzgün render olunması üçün onun valideyn elementi `position: "relative"`, `position: "fixed"` və ya `position: "absolute"` üslublarından birinə malik olmalıdır.

</docs-step>

<docs-step title="Vacib şəkillərə prioritet verin">

Yüklənmə performansı üçün ən vacib optimallaşdırmalardan biri səhifə yüklənərkən ekrandakı ən böyük qrafik element olan ["LCP elementi"](https://web.dev/articles/optimize-lcp) ola biləcək hər hansı bir şəklə prioritet verməkdir. Yüklənmə vaxtlarını optimallaşdırmaq üçün "hero image" və ya LCP elementi ola biləcəyini düşündüyünüz digər şəkillərə `priority` attribute-u əlavə etdiyinizdən əmin olun.

```ts
<img ngSrc="www.example.com/image.png" height="600" width="800" priority />
```

</docs-step>

<docs-step title="Könüllü: Şəkil yükləyicidən (image loader) istifadə edin">

`NgOptimizedImage` sizə direktivə şəkilləriniz üçün URL-lərin necə formatlanacağını bildirən bir [şəkil yükləyici](guide/image-optimization#configuring-an-image-loader-for-ngoptimizedimage) təyin etməyə imkan verir. Yükləyici istifadə etmək şəkillərinizi qısa, nisbi URL-lərlə təyin etməyə imkan yaradır:

```ts
providers: [provideImgixLoader('https://my.base.url/')],
```

Yekun URL 'https://my.base.url/image.png' olacaq:

```angular-html
<img ngSrc="image.png" height="600" width="800" />
```

Şəkil yükləyicilər yalnız rahatlıq üçün deyil — onlar `NgOptimizedImage`-in tam imkanlarından istifadə etməyə imkan verir. Bu optimallaşdırmalar və populyar CDN-lər üçün daxili yükləyicilər haqqında daha çox məlumatı [buradan](guide/image-optimization#configuring-an-image-loader-for-ngoptimizedimage) əldə edə bilərsiniz.

</docs-step>

</docs-workflow>

Bu direktivi iş axınınıza əlavə etməklə, şəkilləriniz artıq Angular-ın köməyi ilə ən yaxşı təcrübələrdən istifadə edərək yüklənir 🎉

Daha çox öyrənmək istəyirsinizsə, [`NgOptimizedImage` sənədlərinə](guide/image-optimization) baxın. Əla işinizi davam etdirin və növbəti bölmədə marşrutlaşdırma (routing) haqqında öyrənək.
