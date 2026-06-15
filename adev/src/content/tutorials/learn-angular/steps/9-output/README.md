# Komponentin output property-ləri

Komponentlərlə işləyərkən digər komponentləri nəsə baş verdiyi barədə məlumatlandırmaq tələb oluna bilər. Ola bilsin ki, düymə kliklənib, siyahıya element əlavə edilib/silinib və ya digər mühüm yeniləmə baş verib. Bu ssenaridə komponentlər valideyn komponentlərlə əlaqə qurmalıdır.

Angular bu tip davranışı aktivləşdirmək üçün `output()` funksiyasından istifadə edir.

QEYD: [Outputs bələdçisində xüsusi event-lər](/guide/components/outputs) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz komponentlərlə əlaqə qurmaq üçün `output()` funksiyasından necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr />

Övlad komponentdən valideyn komponentə əlaqə yolunu yaratmaq üçün class property-sini inisializasiya etmək məqsədilə `output` funksiyasından istifadə edin.

```ts {header:"child.ts"}
@Component({...})
class Child {
  incrementCountEvent = output<number>();
}
```

İndi komponent valideyn komponent tərəfindən dinlənilə bilən event-lər yarada bilər. Event-ləri `emit` metodunu çağıraraq işə salın:

```ts {header:"child.ts"}
class Child {
  ...

  onClick() {
    this.count++;
    this.incrementCountEvent.emit(this.count);
  }
}
```

`emit` funksiyası `output` tərəfindən müəyyən edilmiş eyni tipdə bir event yaradacaq.

Yaxşı, indi növbə sizindir. Aşağıdakı tapşırıqları yerinə yetirərək kodu tamamlayın:

<docs-workflow>

<docs-step title="Bir `output()` property-si əlavə edin">
`child.ts` faylına `addItemEvent` adlı bir output property-si əlavə edərək onu yeniləyin; output tipini `string` olaraq təyin etdiyinizdən əmin olun.
</docs-step>

<docs-step title="`addItem` metodunu tamamlayın">
`child.ts`-də `addItem` metodunu yeniləyin; məntiq kimi aşağıdakı kodu istifadə edin:

```ts {header:"child.ts", highlight:[2]}
addItem() {
  this.addItemEvent.emit('🐢');
}
```

</docs-step>

<docs-step title="`App` template-ini yeniləyin">
`app.ts`-də template-i yeniləyərək emit olunan eventi dinləmək üçün aşağıdakı kodu əlavə edin:

```angular-html
<app-child (addItemEvent)="addItem($event)" />
```

İndi "Add Item" düyməsi hər dəfə klikləndikdə siyahıya yeni bir element əlavə edir.

</docs-step>

</docs-workflow>

Vay, bu mərhələdə siz komponentlərin əsaslarını tamamladınız - heyranedicidir 👏

Angular-ın digər möhtəşəm xüsusiyyətlərini kəşf etmək üçün öyrənməyə davam edin.
