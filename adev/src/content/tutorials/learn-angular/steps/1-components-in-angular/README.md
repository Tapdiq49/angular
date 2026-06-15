# Angular-da Komponentlər

Komponentlər hər hansı bir Angular tətbiqinin təməl quruluş bloklarıdır. Hər bir komponent üç hissədən ibarətdir:

- TypeScript class-ı
- HTML template-i
- CSS üslubları

QEYD: [Essentials bələdçisində komponentlər](/essentials/components) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz bir komponentin template-ini və üslublarını necə yeniləməyi öyrənəcəksiniz.

<hr />

Bu, Angular ilə başlamaq üçün əla fürsətdir.

<docs-workflow>

<docs-step title="Komponent template-ini yeniləyin">
`Hello Universe` mətnini göstərmək üçün `template` property-sini yeniləyin:

```ts
template: `
  Hello Universe
`,
```

HTML template-ini dəyişdikdə, önizləmə (preview) sizin mesajınızla yeniləndi. Gəlin bir addım daha irəli gedək: mətnin rəngini dəyişək.
</docs-step>

<docs-step title="Komponent üslublarını yeniləyin">
Styles dəyərini yeniləyin və `color` property-sini `blue`-dan `#a144eb`-ə dəyişin.

```ts
styles: `
  :host {
    color: #a144eb;
  }
`,
```

Önizləməyə baxdıqda mətnin rənginin dəyişdiyini görəcəksiniz.
</docs-step>

</docs-workflow>

Angular-da brauzer tərəfindən dəstəklənən bütün CSS və HTML imkanlarından istifadə edə bilərsiniz. İstəsəniz, template və üslublarınızı ayrıca fayllarda da saxlaya bilərsiniz.
