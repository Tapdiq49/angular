# Formanıza validasiya əlavə edin

İstifadəçilərin düzgün məlumat daxil etmələrini təmin etmək üçün formaya validasiya əlavə etmək kritikdir. Siqnal Formaları (Signal Forms) `form()` funksiyasına ötürdüyünüz schema funksiyasında validatorlardan istifadə edir.

Bu fəaliyyətdə siz aşağıdakıları öyrənəcəksiniz:

- Daxili validatorları import etmək
- Formanız üçün schema funksiyası təyin etmək
- Xüsusi xəta mesajları ilə spesifik sahələrə validatorlar tətbiq etmək

Gəlin validasiya əlavə edək!

<hr />

<docs-workflow>

<docs-step title="Validatorları import edin">
`@angular/forms/signals`-dan `required` və `email` validatorlarını import edin:

```ts
import {form, FormField, required, email} from '@angular/forms/signals';
```

</docs-step>

<docs-step title="Formanıza schema funksiyası əlavə edin">
İkinci parametr kimi schema funksiyasını daxil etmək üçün `form()` çağırışınızı yeniləyin. Schema funksiyası hər bir sahəyə müraciət etməyə imkan verən `fieldPath` parametrini qəbul edir:

```ts
loginForm = form(this.loginModel, (fieldPath) => {
  // Validatorlar bura gələcək
});
```

</docs-step>

<docs-step title="Email sahəsinə validasiya əlavə edin">
Schema funksiyasının daxilində email sahəsi üçün validasiya əlavə edin. Həm `required()`, həm də `email()` validatorlarından istifadə edin:

```ts
loginForm = form(this.loginModel, (fieldPath) => {
  required(fieldPath.email, {message: 'Email mütləqdir'});
  email(fieldPath.email, {message: 'Düzgün email ünvanı daxil edin'});
});
```

`message` seçimi istifadəçilər üçün xüsusi xəta mesajları təmin edir.
</docs-step>

<docs-step title="Şifrə (password) sahəsinə validasiya əlavə edin">
`required()` validatorundan istifadə edərək şifrə sahəsi üçün validasiya əlavə edin:

```ts
loginForm = form(this.loginModel, (fieldPath) => {
  required(fieldPath.email, {message: 'Email mütləqdir'});
  email(fieldPath.email, {message: 'Düzgün email ünvanı daxil edin'});
  required(fieldPath.password, {message: 'Şifrə mütləqdir'});
});
```

</docs-step>

</docs-workflow>

Mükəmməl! Siz formanıza validasiya əlavə etdiniz. Validatorlar istifadəçilər forma ilə qarşılıqlı əlaqədə olduqca avtomatik işləyir. Validasiya uğursuz olduqda, sahənin vəziyyəti xətaları əks etdirəcək.

Növbəti addımda [validasiya xətalarını template-də necə göstərəcəyinizi](/tutorials/signal-forms/4-display-errors) öyrənəcəksiniz!
