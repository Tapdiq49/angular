# Formanızı template-ə qoşun

İndi `[formField]` direktivindən istifadə edərək formanı template-ə qoşmalısınız. Bu, forma modelinizlə giriş (input) elementləri arasında iki tərəfli məlumat binding-i (two-way data binding) yaradır.

Bu dərsdə siz aşağıdakıları öyrənəcəksiniz:

- `FormField` direktivini import etmək
- Forma sahələrini girişlərə bağlamaq üçün `[formField]` direktivindən istifadə etmək
- Mətn girişlərini və checkbox-ları formanıza qoşmaq
- Template-də forma sahə dəyərlərini göstərmək

Gəlin template-i qoşaq!

<hr />

<docs-workflow>

<docs-step title="FormField direktivini import edin">
`@angular/forms/signals`-dan `FormField` direktivini import edin və onu komponentinizin imports massivinə əlavə edin:

```ts
import { form, FormField } from '@angular/forms/signals';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.css',
  imports: [FormField],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
```

</docs-step>

<docs-step title="Email sahəsini bağlayın">
Template-inizdə email girişinə `[formField]` direktivini əlavə edin:

```html
<input type="email" [formField]="loginForm.email" />
```

`loginForm.email` ifadəsi formanızdakı email sahəsinə müraciət edir.
</docs-step>

<docs-step title="Şifrə (password) sahəsini bağlayın">
Şifrə girişinə `[formField]` direktivini əlavə edin:

```html
<input type="password" [formField]="loginForm.password" />
```

</docs-step>

<docs-step title="Checkbox sahəsini bağlayın">
Checkbox girişinə `[formField]` direktivini əlavə edin:

```html
<input type="checkbox" [formField]="loginForm.rememberMe" />
```

</docs-step>

<docs-step title="Forma dəyərlərini göstərin">
Formanın aşağısında cari forma dəyərlərini göstərmək üçün debug (sazlama) bölməsi var. `.value()` istifadə edərək hər bir sahə dəyərini göstərin:

```angular-html
<p>Email: {{ loginForm.email().value() }}</p>
<p>Şifrə: {{ loginForm.password().value() ? '••••••••' : '(boşdur)' }}</p>
<p>Məni xatırla: {{ loginForm.rememberMe().value() ? 'Bəli' : 'Xeyr' }}</p>
```

Forma sahə dəyərləri siqnallardır, beləliklə göstərilən dəyərlər siz yazdıqca avtomatik yenilənir.
</docs-step>

</docs-workflow>

Əla iş! Siz formanızı template-ə qoşdunuz və forma dəyərlərini göstərdiniz. `[formField]` direktivi iki tərəfli məlumat binding-ini avtomatik idarə edir — siz yazdıqca `loginModel` siqnalı yenilənir və göstərilən dəyərlər dərhal yenilənir.

Növbəti addımda [formanıza validasiyanı necə əlavə edəcəyinizi](/tutorials/signal-forms/3-add-validation) öyrənəcəksiniz!
