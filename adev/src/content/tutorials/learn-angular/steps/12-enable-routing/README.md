# Marşrutlaşdırmaya (Routing) Baxış

Bir çox tətbiqlər üçün tətbiqin birdən çox səhifə tələb etdiyi an gəlib çatır. Bu qaçılmaz an gəldikdə, marşrutlaşdırma (routing) istifadəçilər üçün performans hekayəsinin böyük bir hissəsinə çevrilir.

QEYD: [Ətraflı bələdçidə marşrutlaşdırma](/guide/routing) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz tətbiqinizi Angular Router-dən istifadə etmək üçün necə quracağınızı və konfiqurasiya edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="app.routes.ts faylı yaradın">

`app.routes.ts` daxilində aşağıdakı dəyişiklikləri edin:

1. `@angular/router` paketindən `Routes` import edin.
2. `Routes` tipində `routes` adlı bir sabit (constant) eksport edin və dəyər olaraq `[]` təyin edin.

```ts
import {Routes} from '@angular/router';

export const routes: Routes = [];
```

</docs-step>

<docs-step title="Provider-ə marşrutlaşdırma əlavə edin">

`app.config.ts` faylında tətbiqi aşağıdakı addımlarla Angular Router üçün konfiqurasiya edin:

1. `@angular/router` paketindən `provideRouter` funksiyasını import edin.
2. `./app.routes.ts` faylından `routes` import edin.
3. `providers` massivində `routes` arqumenti ilə `provideRouter` funksiyasını çağırın.

```ts {highlight:[2,3,6]}
import {ApplicationConfig} from '@angular/core';
import {provideRouter} from '@angular/router';
import {routes} from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};
```

</docs-step>

<docs-step title="Komponentdə `RouterOutlet` import edin">

Nəhayət, tətbiqinizin Angular Router istifadə etməyə hazır olduğundan əmin olmaq üçün, tətbiqə routerin istənilən məzmunu harada göstərməsini gözlədiyinizi bildirməlisiniz. Bunu `@angular/router` kitabxanasından `RouterOutlet` direktivini istifadə edərək həyata keçirin.

`<router-outlet />` əlavə edərək `App` template-ini yeniləyin:

```angular-ts {highlight:[11]}
import {RouterOutlet} from '@angular/router';

@Component({
...
template: `
    <nav>
      <a href="/">Home</a>
      |
      <a href="/user">User</a>
    </nav>
    <router-outlet />
  `,
imports: [RouterOutlet],
})
export class App {}
```

</docs-step>

</docs-workflow>

Tətbiqiniz artıq Angular Router istifadə etmək üçün hazırdır. Yaxşı iş! 🙌

Tətbiqimiz üçün marşrutları (routes) müəyyən etmək üçün növbəti addımı öyrənməyə davam edin.
