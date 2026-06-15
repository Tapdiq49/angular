# Töhfə Qaydaları (Contributing Guidelines)

Angular-ın rəsmi sənədlərinin Azərbaycan dilinə tərcüməsi layihəsinə maraq göstərdiyiniz və töhfə vermək istədiyiniz üçün təşəkkür edirik!

Bu layihənin əsas məqsədi Angular texnologiyasını Azərbaycan dilli tərtibatçılar (developerlər) üçün daha əlçatan etmək və öyrənmə prosesini asanlaşdırmaqdır. Bu layihə tamamilə icma tərəfindən idarə olunur və istənilən töhfə, istər kiçik bir hərf səhvinin düzəldilməsi, istərsə də bütöv bir məqalənin tərcüməsi bizim üçün çox dəyərlidir.

Aşağıdakı təlimatlar sizə bu prosesdə necə iştirak edə biləcəyinizi daha aydın şəkildə izah edəcək.

## 🛠 Nədən Başlamalı?

Əgər tərcüməyə haradan başlayacağınızı bilmirsinizsə:

1. **İssue-ları yoxlayın:** GitHub repozitoriyasında açıq olan [Issues](https://github.com/angular/angular/issues) bölməsinə nəzər yetirin. Çox güman ki, "help wanted" və ya "translation" etiketi ilə qeyd olunmuş mövzular tapacaqsınız.
2. **Səhifə seçin:** Sənədlər `adev/src/content/` qovluğunda Markdown (`.md`) formatında saxlanılır. Hələ tərcümə olunmamış və ya yenilənməyə ehtiyacı olan istənilən faylı seçə bilərsiniz.

## Töhfə Növləri

Siz layihəyə bir neçə fərqli yolla kömək edə bilərsiniz:

- **Yeni Səhifələrin Tərcüməsi:** İngilis dilində olan orijinal sənədlərin Azərbaycan dilinə tərcümə edilməsi.
- **Mövcud Tərcümələrin Təkmilləşdirilməsi:** Tərcümə edilmiş mətnlərin daha səlis və qrammatik cəhətdən doğru hala gətirilməsi.
- **Xətaların Düzəldilməsi:** Orfoqrafik səhvlər, işləməyən linklər (broken links) və ya səhv formatlanmış Markdown strukturlarının bərpası.
- **Rəy Bildirmək (Review):** Digər istifadəçilərin açdığı Pull Request-ləri (PR) yoxlamaq və onlara rəy vermək.

## İş Prosesi (Workflow)

Tərcümələrinizi və ya düzəlişlərinizi layihəyə əlavə etmək üçün standart GitHub iş prosesindən istifadə edirik:

1. **Fork edin:** Bu repozitoriyanı öz GitHub hesabınıza fork edin.
2. **Klonlayın:** Fork etdiyiniz repozitoriyanı öz kompyuterinizə klonlayın.
   ```bash
   git clone https://github.com/SIZIN_ISTIFADECHI_ADINIZ/angular.git
   ```
3. **Yeni Şaxə (Branch) Yaradın:** Hər bir tərcümə və ya düzəliş üçün yeni və izahlı bir şaxə yaradın.
   ```bash
   git checkout -b docs-az-components-translation
   ```
4. **Dəyişiklikləri Edin:** Seçdiyiniz `.md` fayllarını redaktə edin.
5. **Commit Edin:** Dəyişikliklərinizi mənası aydın olan bir mesajla commit edin.
   ```bash
   git commit -m "docs(az): təlimat səhifəsi tərcümə edildi"
   ```
6. **Push Edin və PR Açın:** Şaxəni GitHub-a göndərin (push) və orijinal repozitoriyaya bir Pull Request (PR) açın.

## Tərcümə Qaydaları və Standartları

Tərcümələrin hər kəs üçün anlaşılan və peşəkar olması üçün aşağıdakı qaydalara riayət etməyinizi xahiş edirik:

### Nələri TƏRCÜMƏ ETMƏLİ?

- Adi mətnləri, paraqrafları, siyahıları.
- Səhifə və bölmə başlıqlarını (Headers).
- Şəkillərin `alt` mətnlərini.

### Nələri TƏRCÜMƏ ETMƏMƏLİ?

- **Kod Blokları:** Kod daxilindəki dəyişənləri, funksiya adlarını və s. olduğu kimi saxlayın (yalnız kod şərhlərini (comments) tərcümə edə bilərsiniz).
- **Fayl yolları və URL-lər:** Linkləri və fayl adlarını qətiyyən dəyişdirməyin.
- **Xüsusi Terminlər:** Bəzi proqramlaşdırma terminlərini (məsələn: _Component, Directive, Pipe, Service, Framework, API_) orijinalda olduğu kimi saxlamaq məsləhətdir, çünki bu sözlər Azərbaycan dilindəki texniki leksikonda da bu şəkildə istifadə olunur.
- **Xüsusi Blok İşıqlandırıcıları:** Markdown fayllarındakı xüsusi bildiriş açar sözlərini İngiliscə saxlayın: `NOTE`, `TIP`, `IMPORTANT`, `HELPFUL`, `WARNING`.

### Üslub və Ton

- Tərcümələrdə rəsmi, lakin aydın və anlaşıqlı bir üslubdan istifadə edin.
- Cümlələri həddindən artıq uzatmamağa və birbaşa tərcümə (sözbəsöz) etməməyə çalışın. Mənanın düzgün çatdırılması daha vacibdir.
- Tərcümədə digər sənədlərlə uyğunluğu (consistency) qorumağa diqqət edin.

## Suallarınız Var?

Əgər hər hansı bir məqamla bağlı tərəddüdünüz varsa və ya nəyisə dəqiqləşdirmək istəyirsinizsə, GitHub üzərindən bir **Issue** aça və ya açdığınız Pull Request daxilində şərh yaza bilərsiniz. Layihənin digər iştirakçıları sizə böyük məmnuniyyətlə kömək edəcəklər.
