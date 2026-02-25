# Angular quraşdırılmış (embedded) sənəd təlimatları

- [Təlimat faylları](#tutorial-files)
- [Təlimatların qovluq strukturu](#tutorials-directory-structure)
- [Rezerv olunmuş təlimat qovluqları](#reserved-tutorials-directories)

## Təlimat faylları {#tutorial-files}

Təlimatların məzmunu təlimat mətnindən, mənbə kodundan və konfiqurasiyadan ibarətdir.

### Məzmun: `README.md`

Təlimatın məzmunu təlimat qovluğundakı `README.md` faylında yerləşməlidir.

`learn-angular` təlimatını nümunə götürdükdə, baxın: [`src/content/tutorials/learn-angular/intro/README.md`](/src/content/tutorials/learn-angular/intro/README.md)

### Konfiqurasiya: `config.json`

Hər bir təlimat `config.json` faylı ilə müəyyən edilir və aşağıdakı seçimlərə malik ola bilər:

- `title`: təlimatın naviqasiyasında istifadə olunan təlimat başlığını müəyyən edir
- `nextTutorial`: növbəti təlimatın yolu (yalnız `intro/` addımında)
- `src`: daxili redaktorda (embedded editor) istifadə olunan təlimat mənbə kodunu müəyyən edən xarici qovluğa nisbi yol
- `answerSrc`: daxili redaktorda istifadə olunan təlimat cavabını müəyyən edən xarici qovluğa nisbi yol
- `openFiles`: redaktorda açılacaq faylların siyahısı (massiv)
- `type`: təlimatın necə təqdim olunacağını və həmin təlimat üçün hansı komponentlərin lazım olduğunu bildirir
  - `cli`: `cli` tipli təlimat yalnız məzmunu və Angular CLI ilə interaktiv terminalı ehtiva edəcək
  - `editor`: tam quraşdırılmış redaktor üçün istifadə olunur; kod redaktoru, önizləmə (preview), interaktiv terminal və proqramçı serverindən çıxışları olan konsolu ehtiva edir
  - `local`: daxili redaktoru deaktiv edir və yalnız məzmunu göstərir
  - `editor-only`: təlimat Playground və ana səhifə Playground üçün istifadə olunan xüsusi konfiqurasiyadır; məzmunu deaktiv edir və yalnız daxili redaktoru göstərir

### Mənbə kodu

Təlimatın mənbə kodu `README.md` və `config.json` istisna olmaqla, təlimat qovluğundakı hər bir faylı əhatə edir.

Təlimatın mənbə kodu [`common`](#common) layihə faylından üstündür, buna görə də bir fayl həm [`common`](#common) qovluğunda, həm də təlimat qovluğunda eyni nisbi yolla mövcuddursa, təlimat faylı [`common`](#common) faylını əvəzləyəcək (override).

## Təlimatların qovluq strukturu {#tutorials-directory-structure}

Təlimat giriş (introduction) və addımlardan (steps) ibarətdir. Həm giriş, həm də hər bir addım öz məzmununa, konfiqurasiyasına və mənbə koduna malikdir.

`learn-angular` təlimatını nümunə götürək:

### Giriş

[`src/content/tutorials/learn-angular/intro`](/src/content/tutorials/learn-angular/intro)

təlimatın girişi hissəsidir və `/tutorials/learn-angular` marşrutunda (route) yerləşəcək.

### Addımlar

[`src/content/tutorials/learn-angular/steps`](/src/content/tutorials/learn-angular/steps) təlimat addımlarını ehtiva edən qovluqdur.

Bunlar `learn-angular` təlimatından bəzi nümunələrdir:

- [`learn-angular/steps/1-components-in-angular`](/src/content/tutorials/learn-angular/steps/1-components-in-angular): Marşrut `/tutorials/learn-angular/components-in-angular` olacaq
- [`learn-angular/steps/2-updating-the-component-class`](/src/content/tutorials/learn-angular/steps/2-updating-the-component-class): Marşrut `/tutorials/learn-angular/updating-the-component-class` olacaq

Hər bir addım qovluğu bir rəqəmlə başlamalı, ardından defis, sonra isə addım yolu adı (pathname) gəlməlidir.

- Rəqəm addımı bildirir və təlimat daxilində hansı addımın əvvəlki və növbəti olacağını müəyyən edir.
- Defis bir ayırıcıdır :).
- Qovluq adından götürülən yol adı (pathname) addımın URL-ni müəyyən edir.

## Rezerv olunmuş təlimat qovluqları {#reserved-tutorials-directories}

### `common` {#common}

Ümumi (common) layihə bütün təlimatlar tərəfindən təkrar istifadə olunan tam bir Angular layihəsidir. O, bütün aslılıqları (`package.json`, `package-lock.json`), layihə konfiqurasiyasını (`tsconfig.json`, `angular.json`) və tətbiqi işə salmaq üçün əsas faylları (`index.html`, `main.ts`, `app.module.ts`) ehtiva edir.

Ümumi layihə bir neçə səbəbdən istifadə olunur:

- Təlimatlarda faylların təkrarlanmasının qarşısını almaq.
- Ümumi layihə fayllarını və aslılıqları yalnız bir dəfə sorğu etməklə tətbiqdaxili performansı optimallaşdırmaq; sonrakı sorğularda brauzer keşindən yararlanmaq.
- Bütün təlimatlar üçün tək bir `npm install` tələb etmək, beləliklə müxtəlif təlimatlar və addımlar arasında naviqasiya edərkən interaktivliyə qədər olan vaxtı (time to interactive) azaltmaq.
- Bütün təlimatlar üçün ardıcıl mühit təmin etmək.
- Hər bir təlimatın layihə quraşdırılmasına deyil, öyrədilən sahəyə aid xüsusi mənbə koduna fokuslanmasına imkan vermək.

Baxın: [`src/content/tutorials/common`](/src/content/tutorials/common)

### `playground`

Playground `/playground` ünvanındakı təlimat meydançası üçün mənbə kodunu ehtiva edir. O, hər hansı bir məzmun daxil etməməlidir.

Baxın: [`src/content/tutorials/playground`](/src/content/tutorials/playground)

### `homepage`

Homepage ana səhifə playground-u üçün mənbə kodunu ehtiva edir. O, hər hansı bir məzmun daxil etməməlidir.

Baxın: [`src/content/tutorials/homepage`](/src/content/tutorials/homepage)

## Aslılıqların yenilənməsi

Bütün təlimatların aslılıqlarını yeniləmək üçün aşağıdakı skripti işlədə bilərsiniz:

```bash
rm ./adev/src/content/tutorials/homepage/package-lock.json  ./adev/src/content/tutorials/first-app/common/package-lock.json ./adev/src/content/tutorials/learn-angular/common/package-lock.json ./adev/src/content/tutorials/playground/common/package-lock.json ./adev/src/content/tutorials/deferrable-views/common/package-lock.json

npm i --package-lock-only --prefix ./adev/src/content/tutorials/homepage
npm i --package-lock-only --prefix ./adev/src/content/tutorials/first-app/common
npm i --package-lock-only --prefix ./adev/src/content/tutorials/learn-angular/common
npm i --package-lock-only --prefix ./adev/src/content/tutorials/playground/common
npm i --package-lock-only --prefix ./adev/src/content/tutorials/deferrable-views/common
```
