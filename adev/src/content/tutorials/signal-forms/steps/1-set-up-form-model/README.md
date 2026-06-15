# Forma modelini quraşdırın

Hər bir Siqnal Forması (Signal Form) bir forma məlumat modeli ilə başlayır — bu, məlumatlarınızın formasını müəyyən edən və forma məlumatlarınızı saxlayan bir siqnaldır.

Bu dərsdə siz aşağıdakıları öyrənəcəksiniz:

- Forma məlumatlarınız üçün TypeScript interfeysi təyin etmək
- Forma dəyərlərini saxlamaq üçün siqnal yaratmaq
- Siqnal Forması yaratmaq üçün `form()` funksiyasından istifadə etmək

Gəlin giriş formamızın təməlini quraq!

<hr />

<docs-workflow>

<docs-step title="LoginData interfeysini təyin edin">
Giriş forması məlumatlarınızın strukturunu müəyyən edən TypeScript interfeysi yaradın. Formanın aşağıdakı sahələri olacaq:

- `email` sahəsi (string)
- `password` sahəsi (string)
- `rememberMe` sahəsi (boolean)

```ts
interface LoginData {
  email: string;
  password: string;
  rememberMe: boolean;
}
```

Bu interfeysi `@Component` dekoratorundan yuxarı əlavə edin.
</docs-step>

<docs-step title="signal və form-u import edin">
`@angular/core`-dan `signal` funksiyasını və `@angular/forms/signals`-dan `form` funksiyasını import edin:

```ts
import {Component, signal} from '@angular/core';
import {form} from '@angular/forms/signals';
```

</docs-step>

<docs-step title="Forma model siqnalını yaradın">
Komponent class-ınızda ilkin dəyərlərlə bir `loginModel` siqnalı yaradın. Tip parametri kimi `LoginData` interfeysindən istifadə edin:

```ts
loginModel = signal<LoginData>({
  email: '',
  password: '',
  rememberMe: false,
});
```

İlkin dəyərlər mətn sahələri üçün boş string, checkbox üçün isə `false` olaraq başlayır.
</docs-step>

<docs-step title="Formanı yaradın">
İndi model siqnalınızı `form()` funksiyasına ötürərək formanı yaradın:

```ts
loginForm = form(this.loginModel);
```

`form()` funksiyası modelinizdən forma yaradır, bu da sizə sahə vəziyyətinə və validasiyaya müraciət imkanı verir.
</docs-step>

</docs-workflow>

Mükəmməl! Siz forma modelinizi quraşdırdınız. `loginModel` siqnalı forma məlumatlarınızı saxlayır, `loginForm` isə hər bir sahəyə tip təhlükəsizliyi (type safety) ilə giriş imkanı təmin edir.

Növbəti addımda [formanızı template-ə necə qoşacağınızı](/tutorials/signal-forms/2-connect-form-template) öyrənəcəksiniz!
