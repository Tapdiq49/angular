# Siqnal sorğuları (signal queries) ilə övlad elementləri sorğulamaq

Artıq [direktivlərlə siqnallardan necə istifadə olunacağını](/tutorials/signals/8-using-signals-with-directives) öyrəndiniz, gəlin siqnal əsaslı sorğu (query) API-lərini kəşf edək. Bunlar övlad komponentlərə və direktivlərə daxil olmaq və onlarla qarşılıqlı əlaqədə olmaq üçün reaktiv bir yol təqdim edir. Həm komponentlər, həm də direktivlər sorğular həyata keçirə bilər, eyni zamanda özləri də sorğulana bilərlər. Ənənəvi ViewChild-dan fərqli olaraq, siqnal sorğuları avtomatik yenilənir və övlad komponentlərə və direktivlərə tip baxımından təhlükəsiz (type-safe) giriş imkanı verir.

Bu fəaliyyətdə siz övlad komponentlərlə proqramlı şəkildə qarşılıqlı əlaqədə olmaq üçün viewChild sorğuları əlavə edəcəksiniz.

<hr />

<docs-workflow>

<docs-step title="viewChild importunu əlavə edin">
Əvvəlcə, `app.ts` faylındakı övlad komponentlərə daxil olmaq üçün `viewChild` importunu əlavə edin.

```ts
import {Component, signal, computed, viewChild, ChangeDetectionStrategy} from '@angular/core';
```

</docs-step>

<docs-step title="viewChild sorğuları yaradın">
Övlad komponentlərə daxil olmaq üçün App komponentinə viewChild sorğuları əlavə edin.

```ts
// Övlad komponentlərə daxil olmaq üçün sorğu API-ləri
firstProduct = viewChild(ProductCard);
cartSummary = viewChild(CartSummary);
```

Bu sorğular övlad komponent instansiyalarına müraciət edən siqnallar yaradır.
</docs-step>

<docs-step title="Valideyn metodlarını implementasiya edin">
`app.ts` faylındakı övlad komponentlərin metodlarını çağırmaq üçün viewChild sorğularından istifadə edin:

```ts
showFirstProductDetails() {
  const product = this.firstProduct();
  if (product) {
    product.highlight();
  }
}

initiateCheckout() {
  const summary = this.cartSummary();
  if (summary) {
    summary.initiateCheckout();
  }
}
```

</docs-step>

<docs-step title="Qarşılıqlı əlaqələri test edin">
İdarəetmə düymələri artıq işləməlidir:

- **"Birinci Məhsulun Təfərrüatlarını Göstər"** - ProductCard üzərində `highlight()` metodunu çağırır
- **"Ödəniş Prosesinə Başla"** - CartSummary üzərində `initiateCheckout()` metodunu çağırır

ViewChild sorğularının valideyn komponentlərinə övlad davranışını necə idarə etməyə imkan verdiyini görmək üçün düymələri klikləyin.
</docs-step>

</docs-workflow>

Mükəmməl! Siz övlad komponentlərlə qarşılıqlı əlaqə üçün siqnal əsaslı sorğu API-lərindən necə istifadə olunacağını öyrəndiniz.

Növbəti dərsdə, [effect ilə siqnal dəyişikliklərinə necə reaksiya verəcəyinizi](/tutorials/signals/10-reacting-to-signal-changes-with-effect) öyrənəcəksiniz!
