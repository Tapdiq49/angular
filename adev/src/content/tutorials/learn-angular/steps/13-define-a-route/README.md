# Marşrut (Route) Müəyyən Edin

İndi tətbiqi Angular Router istifadə etmək üçün qurduğunuzdan sonra, marşrutları (routes) müəyyən etməlisiniz.

QEYD: [Ətraflı bələdçidə əsas marşrutun müəyyən edilməsi](/guide/routing/define-routes) haqqında daha çox öyrənin.

Bu fəaliyyətdə tətbiqinizə marşrutları necə əlavə edəcəyinizi və konfiqurasiya edəcəyinizi öyrənəcəksiniz.

<hr>

<docs-workflow>

<docs-step title="`app.routes.ts` faylında marşrut müəyyən edin">

Tətbiqinizdə göstəriləcək iki səhifə var: (1) Ana səhifə (Home) və (2) İstifadəçi səhifəsi (User).

Marşrut müəyyən etmək üçün `app.routes.ts`-dəki `routes` massivinə aşağıdakıları daxil edən bir marşrut obyekti əlavə edin:

- Marşrutun yolu - `path` (hansı ki, avtomatik olaraq kök yoldan başlayır (yəni `/`))
- Marşrutun göstərməsini istədiyiniz komponent - `component`

```ts
import {Routes} from '@angular/router';
import {Home} from './home/home';

export const routes: Routes = [
  {
    path: '',
    component: Home,
  },
];
```

Yuxarıdakı kod `Home` komponentinin marşrut kimi necə əlavə edilə biləcəyinə dair bir nümunədir. İndi playground-da `User` ilə birlikdə bunu həyata keçirin.

`User` üçün yol (path) kimi `'user'` istifadə edin.

</docs-step>

<docs-step title="Marşrut tərifinə başlıq (title) əlavə edin">

Marşrutları düzgün müəyyən etməklə yanaşı, Angular Router hər bir marşruta `title` property-si əlavə etməklə istifadəçilər naviqasiya etdikdə səhifə başlığını təyin etməyə imkan verir.

`app.routes.ts` faylında standart marşruta (`path: ''`) və `user` marşrutuna `title` property-sini əlavə edin. Budur bir nümunə:

```ts {highlight:[7]}
import {Routes} from '@angular/router';
import {Home} from './home/home';

export const routes: Routes = [
  {
    path: '',
    title: 'App Home Page',
    component: Home,
  },
];
```

</docs-step>

</docs-workflow>

Bu fəaliyyətdə siz Angular tətbiqinizdə marşrutları müəyyən etməyi və konfiqurasiya etməyi öyrəndiniz. Yaxşı iş. 🙌

Tətbiqinizdə marşrutlaşdırmanı tam aktivləşdirmək üçün səyahət demək olar ki, tamamlanıb, davam edin.
