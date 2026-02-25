# Naviqasiya üçün RouterLink istifadə edin

Tətbiqin hazırkı vəziyyətində, daxili bir linkə kliklədikdə bütün səhifə yenidən yüklənir. Kiçik bir tətbiqdə bu əhəmiyyətli görünməsə də, daha çox məzmunu olan böyük səhifələrdə bu, performans təsirlərinə malik ola bilər, çünki istifadəçilər resursları yenidən yükləməli və hesablamaları yenidən yerinə yetirməli olurlar.

QEYD: [Ətraflı bələdçidə tətbiqinizə marşrutların əlavə edilməsi](/guide/routing/define-routes#adding-the-router-to-your-application) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz Angular Router-dən ən səmərəli şəkildə yararlanmaq üçün `RouterLink` direktivindən necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="`RouterLink` direktivini import edin">

`app.ts` faylında `@angular/router` kitabxanasından mövcud import bəyanatına `RouterLink` direktivini əlavə edin və onu komponent dekoratorunuzun `imports` massivinə daxil edin.

```ts
...
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  imports: [RouterLink, RouterOutlet],
  ...
})
```

</docs-step>

<docs-step title="Template-ə `routerLink` əlavə edin">

`RouterLink` direktivindən istifadə etmək üçün `href` attribute-larını `routerLink` ilə əvəz edin. Template-i bu dəyişikliklə yeniləyin.

```angular-ts
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  ...
  template: `
    ...
    <a routerLink="/">Home</a>
    <a routerLink="/user">User</a>
    ...
  `,
  imports: [RouterLink, RouterOutlet],
})
```

</docs-step>

</docs-workflow>

İndi naviqasiyadakı linklərə kliklədikdə heç bir titrəmə görməməlisiniz və yalnız səhifənin öz məzmunu (yəni `router-outlet`) dəyişməlidir 🎉

Angular ilə marşrutlaşdırmanı öyrənməkdə əla iş gördünüz. Bu, `Router` API-nin hələ yalnız görünən hissəsidir, daha çox öyrənmək üçün [Angular Router Sənədlərinə](guide/routing) baxın.
