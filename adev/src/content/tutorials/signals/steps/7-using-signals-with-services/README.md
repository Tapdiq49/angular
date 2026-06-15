# Servislərlə siqnallardan istifadə etmək

Artıq [model siqnalları ilə iki tərəfli binding-i](/tutorials/signals/6-two-way-binding-with-model-signals) öyrəndiniz, gəlin siqnallardan Angular servisləri ilə necə istifadə olunacağını araşdıraq. Servislər reaktiv vəziyyəti bir neçə komponent arasında paylaşmaq üçün mükəmməldir və siqnallar avtomatik dəyişiklik aşkarlanması (change detection) və təmiz reaktiv naxışlar (patterns) təmin edərək bunu daha da güclü edir.

Bu fəaliyyətdə siz səbət (cart) göstəricisi komponentinin vəziyyət dəyişikliklərinə avtomatik reaksiya verməsinə imkan verən siqnallı bir səbət store-u yaratmağı öyrənəcəksiniz.

<hr />

<docs-workflow>

<docs-step title="Səbət store siqnallarını əlavə edin">
`cart-store.ts` faylında səbət vəziyyətini reaktiv etmək üçün readonly və computed siqnallar əlavə edin.

```ts
// Computed importunu əlavə edin
import {Injectable, signal, computed} from '@angular/core';

// Sonra class-a bu siqnalları əlavə edin:

// Readonly siqnallar
readonly cartItems = this.items.asReadonly();

// Computed siqnallar
readonly totalQuantity = computed(() => {
  return this.items().reduce((sum, item) => sum + item.quantity, 0);
});

readonly totalPrice = computed(() => {
  return this.items().reduce((sum, item) => sum + item.price * item.quantity, 0);
});
```

Bu siqnallar komponentlərin reaktiv şəkildə səbət məlumatlarına və hesablanmış cəmlərə daxil olmasına imkan verir. `asReadonly()` metodu xarici kodun səbət elementlərini birbaşa dəyişdirməsinin qarşısını alır, `computed()` isə mənbə siqnalı dəyişdikdə avtomatik yenilənən törəmə vəziyyətlər yaradır.
</docs-step>

<docs-step title="Miqdar yeniləmə metodlarını tamamlayın">
`cart-display.ts` faylındakı səbət sərgi komponenti artıq template-də səbət store siqnallarından istifadə edir. Səbət elementlərini dəyişdirmək üçün miqdar yeniləmə metodlarını tamamlayın:

```ts
increaseQuantity(id: string) {
  const items = this.cartStore.cartItems();
  const currentItem = items.find((item) => item.id === id);
  if (currentItem) {
    this.cartStore.updateQuantity(id, currentItem.quantity + 1);
  }
}

decreaseQuantity(id: string) {
  const items = this.cartStore.cartItems();
  const currentItem = items.find((item) => item.id === id);
  if (currentItem && currentItem.quantity > 1) {
    this.cartStore.updateQuantity(id, currentItem.quantity - 1);
  }
}
```

Bu metodlar `cartItems()` istifadə edərək cari səbət vəziyyətini oxuyur və store metodları vasitəsilə miqdarları yeniləyir. Siqnallar dəyişdikdə UI avtomatik yenilənir!
</docs-step>

<docs-step title="Əsas app komponentini yeniləyin">
Səbət servisindən istifadə etmək və səbət komponentini göstərmək üçün `app.ts` faylındakı əsas komponenti yeniləyin.

```angular-ts
import {Component, inject} from '@angular/core';
import {CartStore} from './cart-store';
import {CartDisplay} from './cart-display';

@Component({
  selector: 'app-root',
  imports: [CartDisplay],
  template: `
    <div class="shopping-app">
      <header>
        <h1>Servislərlə Siqnalların Demosu</h1>
        <div class="cart-badge">
          Səbət: {{ cartStore.totalQuantity() }} element (\${{ cartStore.totalPrice() }})
        </div>
      </header>

      <main>
        <cart-display />
      </main>
    </div>
  `,
  styleUrl: './app.css',
})
export class App {
  cartStore = inject(CartStore);
}
```

</docs-step>

</docs-workflow>

Mükəmməl! Siz artıq siqnallardan servislərlə necə istifadə edəcəyinizi öyrəndiniz. Yadda saxlanmalı əsas konsepsiyalar:

- **Servis səviyyəli siqnallar**: Servislər reaktiv vəziyyəti idarə etmək üçün siqnallardan istifadə edə bilər
- **Aslılıq inyeksiyası (Dependency injection)**: Komponentlərdə siqnallı servislərə daxil olmaq üçün `inject()` istifadə edin
- **Servislərdə computed siqnallar**: Avtomatik yenilənən törəmə vəziyyətlər yaradın
- **Readonly siqnallar**: Xarici mutasiyaların qarşısını almaq üçün siqnalların yalnız oxunabilir versiyalarını təqdim edin

Növbəti dərsdə, [direktivlərlə siqnallardan istifadə etməyi](/tutorials/signals/8-using-signals-with-directives) öyrənəcəksiniz!
