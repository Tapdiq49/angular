# Validasiya xətalarını göstərin

Artıq formanı validasiya edə bildiyinizə görə, validasiya xətalarını istifadəçilərə göstərmək vacibdir.

Bu fəaliyyətdə siz aşağıdakıları öyrənəcəksiniz:

- Validasiya siqnalları ilə sahə vəziyyətinə müraciət etmək
- Xətaları şərti olaraq göstərmək üçün `@if` istifadə etmək
- `@for` ilə xətalar üzərində dövr (loop) qurmaq
- Xətaları yalnız istifadəçi qarşılıqlı əlaqəsindən sonra göstərmək

Gəlin validasiya rəyini (feedback) göstərək!

<hr />

<docs-workflow>

<docs-step title="Email sahəsi üçün xəta göstəricisi əlavə edin">
Email girişinin aşağısında şərti xəta göstəricisi əlavə edin. Bu, yalnız sahə həm yanlış (invalid), həm də toxunulmuş (touched) olduqda xətaları göstərəcək:

```angular-html
<label>
  Email
  <input type="email" [formField]="loginForm.email" />
</label>
@if (loginForm.email().invalid() && loginForm.email().touched()) {
  <div class="error">
    @for (error of loginForm.email().errors(); track error.kind) {
      <span>{{ error.message }}</span>
    }
  </div>
}
```

`loginForm.email()` çağırışı sahənin vəziyyət siqnalına daxil olur. `invalid()` metodu validasiya uğursuz olduqda `true`, `touched()` metodu istifadəçi sahə ilə qarşılıqlı əlaqədə olduqdan sonra `true` qaytarır və `errors()` xüsusi mesajları ilə validasiya xətaları massivini təmin edir.
</docs-step>

<docs-step title="Şifrə (password) sahəsi üçün xəta göstəricisi əlavə edin">
Şifrə girişinin aşağısında şifrə xətaları üçün eyni növü əlavə edin:

```angular-html
<label>
  Şifrə
  <input type="password" [formField]="loginForm.password" />
</label>
@if (loginForm.password().invalid() && loginForm.password().touched()) {
  <div class="error">
    @for (error of loginForm.password().errors(); track error.kind) {
      <span>{{ error.message }}</span>
    }
  </div>
}
```

</docs-step>

</docs-workflow>

Mükəmməl! Siz formanıza xəta göstəricisi əlavə etdiniz. Xətalar yalnız istifadəçilər bir sahə ilə qarşılıqlı əlaqədə olduqdan sonra görünür və bezdirici olmadan faydalı rəy təmin edir.

Növbəti addımda [forma göndərilməsini (submission) necə idarə edəcəyinizi](/tutorials/signal-forms/5-add-submission) öyrənəcəksiniz!
