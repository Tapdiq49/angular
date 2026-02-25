# Direktivlərlə siqnallardan istifadə etmək

Artıq [servislərlə siqnallardan istifadə etməyi](/tutorials/signals/7-using-signals-with-services) öyrəndiniz, gəlin direktivlərin siqnallardan necə istifadə etdiyini araşdıraq. **Yaxşı xəbər budur ki: siqnallar direktivlərdə tamamilə komponentlərdə olduğu kimi işləyir!** Əsas fərq odur ki, direktivlərin template-ləri olmadığı üçün siz siqnallardan əsasən host elementini reaktiv şəkildə yeniləmək üçün host binding-lərində (host bindings) istifadə edəcəksiniz.

Bu fəaliyyətdə siz siqnalların direktivlərdə necə reaktiv davranış yaratdığını nümayiş etdirən işıqlandırma (highlight) direktivi quracaqsınız.

<hr />

<docs-workflow>

<docs-step title="Siqnalları komponentdəki kimi qurun">
Siqnal funksiyalarını import edin və reaktiv vəziyyətinizi yaradın. Bu, komponentlərdə olduğu kimi eyni şəkildə işləyir:

```ts
import {Directive, input, signal, computed} from '@angular/core';

@Directive({
  selector: '[highlight]',
})
export class HighlightDirective {
  // Siqnal input-ları - komponentlərdəki kimi!
  color = input<string>('yellow');
  intensity = input<number>(0.3);

  // Daxili vəziyyət (state) - komponentlərdəki kimi!
  private isHovered = signal(false);

  // Computed siqnallar - komponentlərdəki kimi!
  backgroundStyle = computed(() => {
    const baseColor = this.color();
    const alpha = this.isHovered() ? this.intensity() : this.intensity() * 0.5;

    const colorMap: Record<string, string> = {
      'yellow': `rgba(255, 255, 0, ${alpha})`,
      'blue': `rgba(0, 100, 255, ${alpha})`,
      'green': `rgba(0, 200, 0, ${alpha})`,
      'red': `rgba(255, 0, 0, ${alpha})`,
    };

    return colorMap[baseColor] || colorMap['yellow'];
  });
}
```

Bunun komponent naxışları ilə eyni olduğuna diqqət yetirin — tək fərq bizim `@Component` yerinə `@Directive` daxilində olmağımızdır.
</docs-step>

<docs-step title="Siqnalları host binding-lərində istifadə edin">
Direktivlərin template-ləri olmadığı üçün siz host elementini reaktiv şəkildə yeniləmək üçün siqnallardan **host binding-lərində** istifadə edəcəksiniz. `host` konfiqurasiyasını və hadisə emalçılarını (event handlers) əlavə edin:

```ts
@Directive({
  selector: '[highlight]',
  host: {
    '[style.backgroundColor]': 'backgroundStyle()',
    '(mouseenter)': 'onMouseEnter()',
    '(mouseleave)': 'onMouseLeave()',
  },
})
export class HighlightDirective {
  // ... əvvəlki addımdakı siqnallar ...

  onMouseEnter() {
    this.isHovered.set(true);
  }

  onMouseLeave() {
    this.isHovered.set(false);
  }
}
```

Host binding-ləri siqnallar dəyişdikdə avtomatik olaraq yenidən qiymətləndirilir — eynilə komponentlərdəki template binding-ləri kimi! `isHovered` dəyişdikdə, `backgroundStyle` computed siqnalı yenidən hesablanır və host binding elementin stilini yeniləyir.
</docs-step>

<docs-step title="Direktivi template-inizdə istifadə edin">
Reaktiv direktivi nümayiş etdirmək üçün app template-ini yeniləyin:

```angular-html
template: `
<div>
  <h1>Siqnallı Direktiv</h1>

  <div highlight color="yellow" [intensity]="0.2">Üstümə gəl - Sarı highlight</div>

  <div highlight color="blue" [intensity]="0.4">Üstümə gəl - Mavi highlight</div>

  <div highlight color="green" [intensity]="0.6">Üstümə gəl - Yaşıl highlight</div>
</div>
`,
```

Direktiv siqnal input-larına əsasən reaktiv işıqlandırmanı avtomatik tətbiq edir!
</docs-step>

</docs-workflow>

Mükəmməl! Siz siqnalların direktivlərlə necə işlədiyini gördünüz. Bu dərsin bəzi əsas nəticələri:

- **Siqnallar universaldır** - Bütün siqnal API-ləri (`input()`, `signal()`, `computed()`, `effect()`) həm direktivlərdə, həm də komponentlərdə eyni şəkildə işləyir
- **Host binding-ləri əsas istifadə sahəsidir** - Direktivlərin template-ləri olmadığı üçün host elementini reaktiv şəkildə dəyişdirmək üçün siqnalları host binding-lərində istifadə edirsiniz
- **Eyni reaktiv naxışlar** - Siqnal yeniləmələri komponent template-lərində olduğu kimi computed siqnalların və host binding-lərin avtomatik yenidən qiymətləndirilməsini tətikləyir

Növbəti dərsdə, [siqnal sorğuları (signal queries) ilə övlad elementləri necə sorğulayacağınızı](/tutorials/signals/9-query-child-elements-with-signal-queries) öyrənəcəksiniz!
