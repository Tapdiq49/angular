# İnput siqnalları vasitəsilə komponentlərə məlumat ötürmək

Artıq [siqnallarla asinxron məlumatları idarə etməyi](/tutorials/signals/4-managing-async-data-with-signals) öyrəndiniz, gəlin Angular-ın siqnal bazalı `input()` API-sini araşdıraq. Bu API valideyn komponentdən övlad komponentə məlumat ötürmək üçün istifadə olunur, komponent məlumat axınını daha reaktiv və səmərəli edir. Əgər digər freymvorklardan komponent "props" anlayışı ilə tanışsınızsa, input-lar da eyni ideyadır.

Bu fəaliyyətdə siz məhsul kartı (product card) komponentinə siqnal input-ları əlavə edəcəksiniz və valideyn məlumatlarının reaktiv şəkildə aşağıya necə axdığını görəcəksiniz.

<hr />

<docs-workflow>

<docs-step title="ProductCard-a siqnal input-ları əlavə edin">
`product-card` komponentində məlumatları qəbul etmək üçün siqnal `input()` funksiyalarını əlavə edin.

```ts
// Siqnal input-ları üçün import-lar əlavə edin
import {Component, input, ChangeDetectionStrategy} from '@angular/core';

// Bu siqnal input-larını əlavə edin
name = input.required<string>();
price = input.required<number>();
available = input<boolean>(true);
```

`input.required()` mütləq təqdim edilməli olan məlumatı necə yaratdığına, susmaya görə (default) dəyəri olan `input()`-un isə seçimli (optional) olduğuna diqqət yetirin.
</docs-step>

<docs-step title="İnput-ları template-ə qoşun">
Siqnal input dəyərlərini göstərmək üçün `product-card` template-ini yeniləyin.

```angular-html
<div class="product-card">
  <h3>{{ name() }}</h3>
  <p class="price">\${{ price() }}</p>
  <p class="status">
    Status:
    @if (available()) {
      Mövcuddur
    } @else {
      Stokda yoxdur
    }
  </p>
</div>
```

İnput siqnalları template-də normal siqnallar kimi işləyir - dəyərlərinə müraciət etmək üçün onları funksiya kimi çağırın.
</docs-step>

<docs-step title="Valideyn siqnallarını övlad input-larına qoşun">
Statik dəyərlər əvəzinə dinamik siqnal dəyərlərini ötürmək üçün `app.ts` faylındakı `product-card` istifadəsini yeniləyin.

```html
<!-- Statik dəyərlərdən dəyişin: -->
<product-card name="Static Product" price="99" available="true" />

<!-- Dinamik siqnallara: -->
<product-card [name]="productName()" [price]="productPrice()" [available]="productAvailable()" />
```

Kvadrat mötərizələr `[]` cari siqnal dəyərlərini övlad komponentə ötürən property binding-ləri yaradır.
</docs-step>

<docs-step title="Reaktiv yeniləmələri test edin">
Valideyn siqnallarını yeniləmək və övlad komponentin necə avtomatik reaksiya verdiyini görmək üçün `app.ts` faylına metodlar əlavə edin.

```ts
updateProduct() {
  this.productName.set('Updated Product');
  this.productPrice.set(149);
}

toggleAvailability() {
  this.productAvailable.set(!this.productAvailable());
}
```

```html
<!-- Reaktivliyi test etmək üçün idarəetmə elementləri əlavə edin -->
<div class="controls">
  <button (click)="updateProduct()">Məhsul məlumatlarını yenilə</button>
  <button (click)="toggleAvailability()">Mövcudluğu dəyiş</button>
</div>
```

Valideyn siqnalları dəyişdikdə, övlad komponent yeni dəyərləri avtomatik qəbul edir və göstərir!
</docs-step>

</docs-workflow>

Mükəmməl! Siz siqnal input-larının necə işlədiyini öyrəndiniz:

- **Siqnal input-ları** - Valideyn komponentlərdən məlumat qəbul etmək üçün `input()` və `input.required()` istifadə edin
- **Reaktiv yeniləmələr** - Valideyn siqnal dəyərləri dəyişdikdə övlad komponentlər avtomatik yenilənir
- **Tip təhlükəsizliyi** - Siqnal input-ları tam TypeScript tip yoxlamasını təmin edir
- **Standart (default) dəyərlər** - Seçimli input-lar standart dəyərlərə malik ola bilər, məcburi input-lar isə mütləq təqdim edilməlidir

Siqnal input-ları komponent arası əlaqəni daha reaktiv edir və bir çox hallarda `OnChanges` lifecycle hook-larına ehtiyacı aradan qaldırır.

Növbəti dərsdə, [model siqnalları ilə iki tərəfli binding (two-way binding)](/tutorials/signals/6-two-way-binding-with-model-signals) haqqında öyrənəcəksiniz!
