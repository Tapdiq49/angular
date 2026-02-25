# Forma göndərilməsini (submission) əlavə edin

Nəhayət, gəlin forma göndərilməsini necə idarə edəcəyimizi öyrənək. Siz forma düzgün (valid) olduqda asinxron əməliyyatları işlətmək üçün `submit()` funksiyasından necə istifadə edəcəyinizi və formada xətalar olduqda göndərmə (submit) düyməsini necə deaktiv edəcəyinizi öyrənəcəksiniz.

Bu fəaliyyətdə siz aşağıdakıları öyrənəcəksiniz:

- `submit()` funksiyasını import etmək
- Göndərmə emalçısı (submission handler) metodu yaratmaq
- Məntiqi yalnız forma düzgün olduqda işlətmək üçün `submit()` istifadə etmək
- Forma vəziyyətinə əsasən göndərmə düyməsini deaktiv etmək

Gəlin formanı tamamlayaq!

<hr />

<docs-workflow>

<docs-step title="submit funksiyasını import edin">
`@angular/forms/signals`-dan `submit` funksiyasını import edin:

```ts
import {form, FormField, required, email, submit} from '@angular/forms/signals';
```

</docs-step>

<docs-step title="onSubmit metodunu əlavə edin">
Komponent class-ınıza forma göndərilməsini idarə edən `onSubmit()` metodu əlavə edin:

```ts
onSubmit(event: Event) {
  event.preventDefault();
  submit(this.loginForm, async () => {
    const credentials = this.loginModel();
    console.log('Giriş edilir:', credentials);
    // Login məntiqinizi bura əlavə edin
  });
}
```

`submit()` funksiyası asinxron callback-inizi yalnız forma düzgün olduqda işlədir. O, həmçinin formanın göndərilmə vəziyyətini (submission state) avtomatik idarə edir.
</docs-step>

<docs-step title="Göndərmə emalçısını formaya bağlayın">
Template-inizdə `onSubmit()` metodunu formanın submit hadisəsinə (event) bağlayın:

```html
<form (submit)="onSubmit($event)"></form>
```

</docs-step>

<docs-step title="Forma yanlış olduqda düyməni deaktiv edin">
Forma yanlış (invalid) olduqda göndərmə düyməsini deaktiv olacaq şəkildə yeniləyin:

```html
<button type="submit" [disabled]="loginForm().invalid()">Giriş et</button>
```

Bu, formada validasiya xətaları olduqda göndərilmənin qarşısını alır.
</docs-step>

</docs-workflow>

Təbriklər! Siz Siqnal Formaları (Signal Forms) ilə tam bir giriş forması qurdunuz.

Nələri öyrəndiyinizi görməyə və təkmilləşdirilmiş mövzuları araşdırmağa hazırsınız? [Növbəti addımlara](/tutorials/signal-forms/6-next-steps) davam edin!
