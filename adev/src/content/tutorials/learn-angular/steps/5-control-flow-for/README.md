# Komponentlərdə Control Flow - `@for`

Veb tətbiqlər qurarkən tez-tez bəzi kodları müəyyən sayda təkrarlamaq lazım olur - məsələn, adlar massivi verildikdə, hər bir adı bir `<p>` teqi daxilində göstərmək istəyə bilərsiniz.

QEYD: [Essentials bələdçisində control flow](/essentials/templates#if-və-for-ilə-control-flow) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz template-də elementləri təkrarlamaq üçün `@for`-dan necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr/>

Template-də elementlərin təkrarlanmasını təmin edən sintaksis `@for`-dur.

Budur, komponent daxilində `@for` sintaksisinin istifadəsinə dair bir nümunə:

```angular-ts
@Component({
  ...
  template: `
    @for (os of operatingSystems; track os.id) {
      {{ os.name }}
    }
  `,
})
export class App {
  operatingSystems = [{id: 'win', name: 'Windows'}, {id: 'osx', name: 'MacOS'}, {id: 'linux', name: 'Linux'}];
}
```

Diqqət edilməli iki məqam:

- `for` ifadəsinin əvvəlində `@` prefiksi var, çünki bu, [Angular template syntax](guide/templates) adlanan xüsusi sintaksis növüdür.
- v16 və daha köhnə versiyalardan istifadə edən tətbiqlər üçün [Angular documentation for NgFor](guide/directives/structural-directives) bölməsinə baxın.

<docs-workflow>

<docs-step title="`users` property-sini əlavə edin">
`App` class-ına istifadəçiləri və onların adlarını ehtiva edən `users` adlı property əlavə edin.

```ts
[
  {id: 0, name: 'Sarah'},
  {id: 1, name: 'Amy'},
  {id: 2, name: 'Rachel'},
  {id: 3, name: 'Jessica'},
  {id: 4, name: 'Poornima'},
];
```

</docs-step>

<docs-step title="Template-i yeniləyin">
`@for` template sintaksisindən istifadə edərək hər bir istifadəçi adını `p` elementi daxilində göstərmək üçün template-i yeniləyin.

```angular-html
@for (user of users; track user.id) {
  <p>{{ user.name }}</p>
}
```

QEYD: `track` istifadəsi mütləqdir, siz `id` və ya başqa bir unikal identifikator istifadə edə bilərsiniz.

</docs-step>

</docs-workflow>

Bu tip funksionallıq control flow adlanır. Növbəti mərhələdə komponentləri necə fərdiləşdirəcəyinizi və onlarla necə əlaqə quracağınızı öyrənəcəksiniz - yeri gəlmişkən, indiyə qədər əla iş görürsünüz.
