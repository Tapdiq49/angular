# Komponentin input property-ləri

Bəzən tətbiq inkişafı zamanı komponentə məlumat göndərmək tələb olunur. Bu məlumat bir komponenti fərdiləşdirmək və ya valideyn komponentdən övlad (child) komponentə məlumat ötürmək üçün istifadə edilə bilər.

Angular `input` adlı konsepsiyadan istifadə edir. Bu, digər freymvorklardakı `props`-a bənzəyir. `input` property-si yaratmaq üçün `input()` funksiyasından istifadə edin.

QEYD: [Inputs bələdçisində input property-ləri ilə məlumatın qəbul edilməsi](/guide/components/inputs) haqqında daha çox öyrənin.

Bu fəaliyyətdə siz komponentlərə məlumat göndərmək üçün `input()` funksiyasından necə istifadə edəcəyinizi öyrənəcəksiniz.

<hr>

Bir `input` property-si yaratmaq üçün komponent class-ının property-sini inisializasiya etmək məqsədilə `input()` funksiyasını əlavə edin:

```ts {header:"user.ts"}
class User {
  occupation = input<string>();
}
```

Bir dəyəri `input` vasitəsilə ötürməyə hazır olduğunuzda, dəyərlər template-lərdə attribute sintaksisindən istifadə edilərək təyin edilə bilər. Budur bir nümunə:

```angular-ts {header:"app.ts", highlight:[3]}
@Component({
  ...
  template: `<app-user occupation="Angular Developer"></app-user>`
})
export class App {}
```

`input` funksiyası `InputSignal` qaytarır. Siz siqnalı çağıraraq dəyəri oxuya bilərsiniz.

```angular-ts {header:"user.ts"}
@Component({
  ...
  template: `<p>The user's occupation is {{occupation()}}</p>`
})
```

<docs-workflow>

<docs-step title="Bir `input()` property-si təyin edin">
`user.ts`-dəki kodu yeniləyərək `User` class-ında `name` adlı bir `input` property-si təyin edin və `string` tipini göstərin. Hələlik ilkin dəyər təyin etməyin və `input()` funksiyasını arqumentsiz çağırın. Cümlənin sonunda `name` property-sini çağırmaq və render etmək (interpolation) üçün template-i yenilədiyinizdən əmin olun.
</docs-step>

<docs-step title="`input` property-sinə dəyər ötürün">
`app.ts`-dəki kodu yeniləyərək `name` property-sinə `"Simran"` dəyərini göndərin.
<br>

Kod uğurla yeniləndikdə, tətbiq `The user's name is Simran` mesajını göstərəcək.
</docs-step>

</docs-workflow>

Bu gözəl olsa da, komponentlər arası əlaqənin yalnız bir istiqamətidir. Bəs övlad komponentdən valideyn komponentə məlumat və data göndərmək istəsəniz necə? Bunu öyrənmək üçün növbəti dərsi yoxlayın.

P.S. Əla gedirsiniz - davam edin 🎉
