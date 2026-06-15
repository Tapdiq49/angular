# LLM sorğuları (prompts) və AI IDE quraşdırması

Böyük dil modelləri (LLM) ilə kod yaratmaq tərtibatçılar üçün sürətlə böyüyən bir maraq sahəsidir. LLM-lər çox vaxt işlək kod yarada bilsə də, Angular kimi daim inkişaf edən çərçivələr (frameworks) üçün ardıcıl olaraq düzgün kod yaratmaq çətin ola bilər.

Qabaqcıl təlimatlar (instructions) və sorğular (prompts), domene xas detallarla müasir kod yaratmanı dəstəkləmək üçün yüksələn bir standart halına gəlir. Bu bölmə, Angular üçün daha dəqiq kod yaratmağı dəstəkləmək üçün hazırlanmış məzmun və resursları ehtiva edir.

## Xüsusi Sorğular (Custom Prompts) və Sistem Təlimatları

Aşağıdakı xüsusi, domene xas fayllardan birini istifadə edərək LLM-lərlə kod yaratma təcrübənizi inkişaf etdirin.

QEYD: Bu fayllar Angular-ın konvensiyaları ilə müasir qalmaq üçün müntəzəm olaraq yenilənəcək.

Budur LLM-lərə Angular ən yaxşı təcrübələrini (best practices) izləyən düzgün kod yaratmağa kömək edən bir sıra təlimatlar. Bu fayl, AI alətinizə sistem təlimatları kimi daxil edilə bilər və ya kontekst kimi sorğunuzla birlikdə daxil edilə bilər.

<docs-code language="md" path="packages/core/resources/best-practices.md" class="compact"/>

<a download href="/assets/context/best-practices.md" target="_blank">best-practices.md faylını yükləmək üçün bura tıklayın.</a>

## Qaydalar Faylları (Rules Files)

<a href="https://studio.firebase.google.com?utm_source=adev&utm_medium=website&utm_campaign=BUILD_WITH_AI_ANGULAR&utm_term=angular_devrel&utm_content=build_with_ai_angular_firebase_studio">Firebase Studio</a> kimi bir sıra redaktorlar, LLM-lərə kritik kontekst təqdim etmək üçün faydalı qaydalar fayllarına malikdirlər.

| Mühit/IDE            | Qaydalar Faylı                                                                                                         | Quraşdırma Təlimatları                                                                                                                                                |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Firebase Studio      | <a download href="/assets/context/airules.md" target="_blank">airules.md</a>                                           | <a href="https://firebase.google.com/docs/studio/set-up-gemini#custom-instructions">`airules.md` konfiqurasiyası</a>                                                  |
| Copilot dəstəkli IDE | <a download="copilot-instructions.md" href="/assets/context/guidelines.md" target="_blank">copilot-instructions.md</a> | <a href="https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions" target="_blank">`.github/copilot-instructions.md` konfiqurasiyası</a> |
| Cursor               | <a download href="/assets/context/angular-20.mdc" target="_blank">cursor.md</a>                                        | <a href="https://docs.cursor.com/context/rules" target="_blank">`cursorrules.md` konfiqurasiyası</a>                                                                  |
| JetBrains IDE-ləri   | <a download href="/assets/context/guidelines.md" target="_blank">guidelines.md</a>                                     | <a href="https://www.jetbrains.com/help/junie/customize-guidelines.html" target="_blank">`guidelines.md` konfiqurasiyası</a>                                          |
| VS Code              | <a download=".instructions.md" href="/assets/context/guidelines.md" target="_blank">.instructions.md</a>               | <a href="https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions" target="_blank">`.instructions.md` konfiqurasiyası</a>                |
| Windsurf             | <a download href="/assets/context/guidelines.md" target="_blank">guidelines.md</a>                                     | <a href="https://docs.windsurf.com/windsurf/cascade/memories#rules" target="_blank">`guidelines.md` konfiqurasiyası</a>                                               |

## Angular CLI MCP Server quraşdırması

Angular CLI, geliştirme mühitinizdəki AI köməkçilərinin Angular CLI ilə əlaqə qurmasına imkan verən eksperimental bir [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/) ehtiva edir.

[**Angular CLI MCP Serverinin quraşdırılmasını öyrənin**](/ai/mcp)

## `llms.txt` ilə Kontekst Təqdim Etmək

`llms.txt`, vebsaytlar üçün LLM-lərə məzmunlarını daha yaxşı başa düşmələrinə və emal etmələrinə kömək etmək üçün nəzərdə tutulmuş təklif edilmiş bir standartdır. Angular komandası, LLM-lərə və kod yaratmaq üçün LLM istifadə edən alətlərə daha müasir Angular kodu yaratmağa kömək etmək üçün bu faylın iki versiyasını hazırlamışdır.

- <a href="/llms.txt" target="_blank">llms.txt</a> — əsas fayllara və resurslara keçidlər təqdim edən indeks faylı.
- <a href="/assets/context/llms-full.txt" target="_blank">llms-full.txt</a> — Angular-ın necə işlədiyini və Angular tətbiqlərinin necə qurulacağını təsvir edən daha hərtərəfli derlenmiş resurslar dəsti.

AI-ni Angular tətbiqlərinizə necə inteqrasiya etmək barədə daha ətraflı məlumat üçün [icmalın (overview) səhifəsinə baxmağı unutmayın](/ai).

## Veb Kod Yaratma Qiymətləndirici

Angular komandası [Veb Kod Yaratma Qiymətləndiricisini (Web Codegen Scorer)](https://github.com/angular/web-codegen-scorer) hazırlamış və açıq mənbə etmişdir. Bu, AI tərəfindən yaradılan veb kodunun keyfiyyətini qiymətləndirmək üçün bir alətdir. Bu aləti Angular üçün LLM tərəfindən yaradılan kodun dəqiqliyini artırmaq üçün sorğuların tənzimlənməsi kimi AI tərəfindən yaradılan kodla bağlı sübutlara əsaslanan qərarlar qəbul etmək üçün istifadə edə bilərsiniz. Bu sorğular, AI alətiniz üçün sistem təlimatları və ya sorğunuzla birlikdə kontekst kimi daxil edilə bilər. Ayrıca, fərqli modellərin istehsal etdiyi kodun keyfiyyətini müqayisə etmək üçün bu alətdən istifadə edə və modellər və agentlər inkişaf etdikcə keyfiyyəti zamanla izləyə bilərsiniz.
