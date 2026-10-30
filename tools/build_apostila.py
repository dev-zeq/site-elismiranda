#!/usr/bin/env python3
"""Gera apostila/index.html a partir do conteúdo abaixo.  Uso: python3 tools/build_apostila.py"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fig(name, cap="", cls=""):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="{cls}"><img src="img/{name}.webp" alt="{html.escape(re.sub("<[^>]+>", "", cap) or name)}" loading="lazy">{c}</figure>'

def figs(*items, cls=""):
    return f'<div class="figrow {cls}">' + "".join(fig(*i) if isinstance(i, tuple) else fig(i) for i in items) + "</div>"

def note(t, kind=""):
    return f'<aside class="note {kind}">{t}</aside>'

def term(t, d):
    return f'<p><strong class="term">{t}</strong> {d}</p>'

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

PARTS = []  # (titulo_da_parte, [(id, titulo, html)])

# ───────────────────────── PARTE 1 ─────────────────────────
p1 = []
p1.append(("introducao", "Introdução", f"""
<p class="lead">Cada vez mais mulheres desejam cílios volumosos e alongados com praticidade, sem precisar usar rímel.</p>
<p>A extensão de cílios consiste na aplicação de um fio sintético sobre cada fio natural. O resultado são cílios volumosos e alongados que realçam o olhar, elevam a autoestima e, quando bem feitos, têm excelente durabilidade.</p>
<p>Desejo a você um excelente curso. Está preparada para mergulhar no mundo das extensões de cílios e elevar a autoestima de milhares de mulheres?</p>
<h3>O que é uma Lash Designer?</h3>
<p>É a profissional que se capacita em uma das técnicas de extensão de cílios e busca sempre aprimorar o conhecimento, acompanhando o que há de mais moderno e atualizado no mercado de cílios e visagismo. Deve ser detalhista e procurar ser um diferencial no mercado.</p>
<h3>Não procure atalhos</h3>
<p>Para ter sucesso na carreira de lash, não pule etapas. Esteja disposta a estudar, treinar e investir em você. Não se prenda a um único curso: busque sempre a evolução.</p>
{note("<strong>O estudo vai te levar a lugares surpreendentes.</strong>")}
"""))

p1.append(("origem", "A origem das extensões de cílios", f"""
<p>A história dos cílios fio a fio remonta ao século 20. Em <strong>1927</strong>, o maquiador <strong>Max Factor</strong> inventou os cílios postiços, e a atriz Phyllis Haver foi a primeira a usá-los. Os primeiros postiços estavam longe do ideal, mas o público ficou cativado pelo olhar dramático da atriz, e logo todas as divas de Hollywood passaram a desejá-los. Max Factor, que havia sido assistente de maquiagem artística no Teatro Bolshoi de Moscou, tornou-se estilista e maquiador de sucesso nos Estados Unidos e criou a primeira marca de maquiagem do mundo, que leva seu nome.</p>
<p>No início do século 21, os japoneses criaram um cílio artificial que reproduzia com precisão a forma e a curvatura dos cílios naturais. Dali surgiu o fio a fio como conhecemos hoje. A primeira pessoa a realizar uma extensão fio a fio foi <strong>Shu Uemura</strong>, que presenteou a Madonna com um olhar inesquecível, usando essa nova tecnologia em 2003.</p>
<h3>Postiço × fio a fio</h3>
{table(["", "Cílios postiços", "Extensão fio a fio"], [
 ["Onde é colado", "Na pálpebra", "Em cada cílio natural"],
 ["Cola", "Cola de pele", "Adesivo específico de cianoacrilato"],
 ["Duração", "Um dia", "Cerca de um mês, com manutenções"]])}
<p>O procedimento virou uma verdadeira febre entre as japonesas, porque o formato único da pálpebra asiática tornava as extensões praticamente invisíveis, permitindo fios muito mais longos. Desde então, o alongamento de cílios conquistou o mundo, com diferentes curvaturas, tamanhos, espessuras e materiais.</p>
{fig("resultado-2", "Extensão de cílios realizada no studio da Elis Miranda.")}
"""))

p1.append(("anatomia", "Anatomia do olho e importância dos cílios", f"""
<p>Em formato esférico, os olhos são protegidos pela cavidade óssea do crânio. As pálpebras dificultam a entrada de sujeira e as sobrancelhas impedem que o suor chegue ao globo ocular.</p>
{term("Esclera:", "parte branca do olho, camada fibrosa que reveste o globo ocular. Nela ficam os músculos extraoculares responsáveis pelo movimento dos olhos.")}
{term("Córnea:", "calota cristalina e transparente, contínua com a esclera. É delicada, muito sensível e cheia de terminações nervosas. Desvia a luz que chega ao olho em direção à retina. Juntas, córnea e esclera protegem as estruturas internas.")}
{term("Pupila:", "fica no centro da íris e tem abertura regulável, que permite a entrada de mais ou menos luz.")}
{term("Íris:", "parte colorida do olho. É um músculo circular que controla o tamanho da pupila: relaxa sob luz fraca (a pupila aumenta) e contrai sob luz forte (a pupila diminui), protegendo a retina.")}
{term("Retina:", "fica na parte interna do olho e envia sinais pelo nervo óptico ao cérebro, formando as imagens que vemos.")}
{term("Conjuntiva:", "lubrifica e protege contra agentes externos que possam prejudicar a visão.")}
{figs("olho-anatomia", "olho-corte")}
"""))

p1.append(("tricologia", "Tricologia dos cílios", f"""
<p>Os cílios existem para proteger os olhos: são uma barreira contra poeira e microrganismos e funcionam como sensores de alto reflexo, que fazem a pálpebra fechar antes que algo atinja o olho. São semelhantes aos cabelos, com cerca de 0,25 micrômetro de diâmetro, e por isso merecem cuidado.</p>
<p>O fio do cílio é composto por três partes:</p>
{term("Medula:", "camada central, que dá sustentação ao fio. Formada por células provenientes do córtex.")}
{term("Cutícula:", "camada externa, formada por células em escamas sobrepostas e queratinizadas, ricas em enxofre. É a barreira protetora do córtex e da medula, responsável pelo brilho e pela maciez.")}
{term("Córtex:", "segunda camada e principal do fio, considerado o “coração” do cílio: concentra a maior quantidade de proteína, além de hidrogênio e oxigênio responsáveis pela hidratação interna. É formado por células cilíndricas (a matriz), onde ficam a queratina e outras proteínas.")}
<h3>Composição química</h3>
<p>O cílio é formado por carbono, hidrogênio, nitrogênio, oxigênio e enxofre, que se unem em uma proteína chamada <strong>queratina</strong>: 65% a 95% de proteínas, mais cerca de 12% de água e 3% de lipídios.</p>
{table(["Elemento","Proporção"],[["Carbono","45%"],["Oxigênio","28%"],["Nitrogênio","15%"],["Hidrogênio","7%"],["Enxofre","5%"]])}
{figs("cilio-estrutura","cilio-camadas")}
<h3>As 3 ligações químicas do fio</h3>
{term("Pontes de hidrogênio (temporárias):", "são as mais fracas e as mais numerosas. Toda vez que molhamos o cílio, elas se desfazem e podemos dar uma nova forma ao fio ao secá-lo.")}
{term("Pontes salinas (intermediárias):", "têm cargas positivas e negativas nas cadeias polipeptídicas. São um pouco mais fortes que as de hidrogênio e se alteram quando mudamos o pH. Só voltam à estrutura normal quando o pH retorna ao natural do fio.")}
{term("Pontes dissulfeto (permanentes):", "ligações de enxofre, as mais fortes do fio, responsáveis pela estrutura permanente (liso, crespo ou encaracolado). Só são rompidas por processos químicos.")}
<p>A cor natural vem da <strong>melanina</strong>: a eumelanina dá a coloração escura e a feomelanina, a avermelhada. A presença, ausência ou mistura desses pigmentos explica a variedade de cores existentes (em pessoas albinas, o fio é amarelado por não haver melanina).</p>
<p>A pele tem papel fundamental na produção dos cílios, por isso é essencial compreender a saúde da pele e a estrutura dos pelos para obter bons resultados.</p>
<h3>Glândulas de Meibômio</h3>
<p>São glândulas sebáceas das pálpebras, localizadas nas margens, e produzem o <strong>meibo</strong>, substância gordurosa que forma uma das camadas do filme lacrimal. Ele mantém o olho lubrificado, impede que a lágrima evapore rápido e protege e nutre a superfície ocular.</p>
"""))

p1.append(("ciclo", "Ciclo de crescimento dos fios", f"""
<p>Os cílios duram em média <strong>90 a 150 dias</strong> até cair e serem substituídos. Na pálpebra superior temos cerca de <strong>160 fios</strong> por olho, distribuídos em 2 a 5 camadas (nos cantos interno e externo há menos camadas, em média 2 a 3). Todo dia surge cerca de um fio novo para substituir os que caíram, seguindo um ciclo de três fases:</p>
{table(["Fase","O que acontece","Duração"],[
 ["<strong>Anágena</strong>","Fase de crescimento","30 a 45 dias"],
 ["<strong>Catágena</strong>","Os cílios param de crescer por contenção do folículo","2 a 3 semanas"],
 ["<strong>Telógena</strong>","Repouso antes da queda","Até cerca de 7 semanas"]])}
{figs("ciclo-olho","ciclo-crescimento")}
<p>Devemos preservar os cílios em fase anágena (<em>baby lashes</em>), pois muitas vezes não suportam o peso dos fios sintéticos. Na manutenção, eles já estarão na fase ideal para receber a extensão.</p>
{note("<strong>Perdemos naturalmente de 3 a 5 fios por dia</strong>, independentemente de usar extensões. Esclareça isso para sua cliente: não se assuste se ela relatar a queda após aplicar.")}
"""))

p1.append(("saude-ocular", "Saúde ocular", f"""
<p>Os cílios vão além da estética: protegem o globo ocular como barreira física contra microrganismos e partículas e funcionam como sensores que disparam o fechamento da pálpebra quando algo se aproxima. Conhecer as principais alterações oculares ajuda você a identificar quando <strong>não</strong> atender e quando encaminhar para um médico.</p>
<h3>Conjuntivite</h3>
<p>Inflamação da membrana transparente (conjuntiva) que recobre a parte branca do olho e a face interna das pálpebras. Normalmente atinge os dois olhos e pode durar até 15 dias. As causas incluem alergias, infecções (virais, bacterianas ou fúngicas), corpo estranho e contato com substâncias químicas.</p>
{term("Alérgica:", "a mais comum, afeta em geral os dois olhos e é mais frequente em pessoas com rinite ou bronquite. Pólen, poeira e pelos de animais podem provocar. <strong>Não é contagiosa</strong> e é tratada com colírio antialérgico.")}
{term("Infecciosa:", "causada por vírus, bactérias ou fungos e <strong>altamente contagiosa</strong>. O contágio ocorre pelo contato com secreções. Previna lavando as mãos e evitando compartilhar toalhas e roupas de cama. A bacteriana produz secreção amarelada e espessa; o tratamento (colírios ou pomadas com antibiótico) deve ser feito <strong>exclusivamente por oftalmologista</strong>.")}
{term("Tóxica:", "causada pelo contato direto com agente tóxico (produtos de limpeza, tinta de cabelo, fumaça de cigarro, cloro, maquiagens, colírios). Causa lacrimejamento e vermelhidão, que costumam desaparecer em 2 a 4 dias. Na nossa profissão, ocorre quando o fume liberado pela polimerização do adesivo (cianoacrilato) atinge o olho.")}
<h3>Blefarite</h3>
<p>Inflamação das bordas das pálpebras, com escamas, crostas, vermelhidão e inchaço. Pode ser causada por infecção bacteriana ou fúngica, disfunção das glândulas meibomianas, olho seco ou parasitas (ácaros <em>Demodex</em>). Pálpebras superior e inferior podem ser afetadas, e pessoas com pele oleosa, caspa e olho seco têm maior chance de desenvolver.</p>
{fig("blefarite")}
<h3>Abrasão corneana</h3>
<p>Arranhão na superfície frontal transparente do olho (córnea). Causa dor, vermelhidão, fotofobia e sensação de corpo estranho. Em geral vem de poeira, lentes de contato ou objetos estranhos. Nas extensões, acontece quando o <strong>pad é posicionado incorretamente</strong> e se movimenta. Pequenas abrasões podem ser tratadas com colírios lubrificantes sem conservantes, mas somente um profissional habilitado pode indicar o tratamento.</p>
{fig("abrasao")}
{note("Durante o atendimento, fique atenta para que o pad não machuque os olhos da sua cliente.")}
<h3>Terçol × calázio</h3>
{table(["","Terçol","Calázio"],[
 ["Natureza","Infecção bacteriana","Inflamação (sem infecção)"],
 ["Causa","Bactérias","Obstrução do canal de saída de uma glândula sebácea"],
 ["Aspecto","“Bolinha” vermelha na borda externa da pálpebra, perto dos cílios","Caroço avermelhado na pálpebra, logo após os cílios"],
 ["Sintomas","Olhos inchados, dor, vermelhidão, calor, coceira, lacrimejamento, sensibilidade à luz","Inchaço (edema) avermelhado, mais comum em quem tem acne, seborreia ou rosácea"]])}
{figs("tercol","calazio")}
<p>Embora os sintomas sejam parecidos, exigem cuidados distintos. <strong>Somente um oftalmologista pode fazer o diagnóstico correto.</strong></p>
<h3>Demodex</h3>
<p>Ácaros são os menores animais do grupo dos aracnídeos e só são vistos ao microscópio. Duas espécies habitam as pálpebras: o <em>Demodex folliculorum</em> (base dos cílios, o que acomete cílios humanos) e o <em>Demodex brevis</em> (glândulas meibomianas). Alimentam-se de células da pele, hormônios e sebo, e estão ligados à blefarite e à meibomite. Os problemas surgem quando há falta de higienização.</p>
<p><strong>Sintomas:</strong> coceira intensa nas pálpebras, crostas na base dos cílios, olhos grudados e com secreção (principalmente pela manhã), inchaço e vermelhidão, sensibilidade à luz, ardência, perda de cílios, olho seco e sensação de areia nos olhos.</p>
{figs("demodex","demodex-olho")}
{note("Oriente sua cliente sobre a importância da higienização diária dos cílios, para evitar complicações e manter a saúde dos cílios e dos olhos.")}
"""))
PARTS.append(("Fundamentos", p1))

# ───────────────────────── PARTE 2 ─────────────────────────
p2 = []
p2.append(("biosseguranca", "Biossegurança", f"""
<p>Na estética, biossegurança é a consciência de prevenir doenças no ambiente de trabalho. Profissional e cliente ficam expostos a patógenos (hepatite B e C, herpes, gripe, tuberculose, micoses, conjuntivite, HIV, entre outros) e a produtos que exalam odores tóxicos, como o adesivo. O Brasil é o terceiro maior mercado de beleza do mundo, o que torna o cuidado ainda mais necessário.</p>
<h3>EPIs usados nas extensões de cílios</h3>
<p>São materiais de uso individual, geralmente descartáveis, que <strong>não devem ser reutilizados</strong>, nem para a mesma cliente.</p>
{ul("<strong>Luvas:</strong> em todos os procedimentos, descartadas ao final de cada um.", "<strong>Touca:</strong> evita contaminação cruzada, por microrganismos que possam estar no cabelo, entre profissional e cliente.", "<strong>Jaleco ou uniforme:</strong> sempre apresentável, evita que você se suje.", "<strong>Máscara:</strong> protege boca e nariz da profissional; descartável.", "<strong>Sapatos fechados:</strong> evitam o risco de queda de materiais e perfuração.")}
{fig("epis")}
{note("É essencial conhecer a legislação sanitária vigente para que, seguindo as boas práticas, você garanta sua saúde e a do próximo, de forma ética.")}
"""))

p2.append(("esterilizacao", "Limpeza, higienização e esterilização", f"""
<p>A limpeza e desinfecção do ambiente e dos materiais devem ser <strong>diárias</strong>. Todo estabelecimento deve respeitar a legislação sanitária vigente do seu município.</p>
{term("Limpeza:", "remoção de sujidades orgânicas e inorgânicas (óleo, gordura, sangue ou pus) com água, detergentes e ação mecânica, deixando o produto seguro para manuseio e preparado para desinfecção ou esterilização.")}
{term("Higienização / sanitização:", "conjunto de operações físicas ou químicas que reduzem a contaminação por microrganismos e proteínas tóxicas em superfícies inanimadas (instalações, equipamentos e utensílios).")}
{term("Desinfecção:", "eliminação de formas vegetativas em superfícies inanimadas, por agentes químicos e/ou físicos.")}
{term("Esterilização:", "processo que promove a completa eliminação ou destruição de todas as formas de microrganismos (vírus, bactérias, fungos, protozoários, esporos). É o único meio que garante trabalhar com segurança e prevenir contaminações.")}
<h3>O fluxo unidirecional de processamento em 7 etapas</h3>
{ol("Limpeza","Inspeção visual","Embalagem","Esterilização","Monitorização da esterilização","Registros da monitorização","Armazenamento")}
{fig("esterilizacao")}
{note("É importante elaborar um manual de rotinas e procedimentos, com rotinas escritas e padronizadas, para que nenhum requisito seja esquecido. Use os EPIs adequados em cada etapa da esterilização.")}
"""))

p2.append(("nocoes", "Noções básicas e contraindicações", f"""
<h3>Técnica clássica fio a fio</h3>
<p>Consiste na aplicação de um fio sintético para cada fio natural da cliente, com um adesivo específico. Dentro desta categoria podemos trabalhar com fio a fio, volume brasileiro (Y) e volume egípcio (W). O procedimento alonga, levanta, disfarça ou realça, além de dar volume. São aplicados em média <strong>160 fios em cada olho</strong>.</p>
<p>O tamanho, a curvatura e a espessura devem ser escolhidos conforme as características do fio natural de cada cliente, sem sobrecarregá-lo. Avalie também o formato dos olhos, das sobrancelhas e do rosto: o <strong>visagismo</strong> é essencial.</p>
<p>Neste curso também abordamos a técnica de <strong>capping</strong>, que entrega retenção e volume superiores a 30 dias, e a técnica com <strong>fans premade</strong>, que oferece volume de 3D até 16D sem que você precise montar os fans.</p>
{note("Em média, este procedimento leva cerca de <strong>2h30</strong>. Quem está começando normalmente demora mais no início.")}
<h3>Contraindicações</h3>
{ul("Cirurgias oculares: solicitar liberação médica se feitas há menos de 3 meses.", "Gestantes e lactantes: solicitar liberação médica por escrito.", "Alergia ao cianoacrilato.", "Doenças oculares ou processos inflamatórios.", "Cirurgia recente nos olhos.")}
"""))
PARTS.append(("Segurança", p2))

# ───────────────────────── PARTE 3 ─────────────────────────
p3 = []
p3.append(("fios-sinteticos", "Tipos de fios sintéticos", f"""
<p>O diferencial dos fios está na composição e no processo de fabricação. O material é o <strong>PBT</strong> (polibutileno tereftalato), um termoplástico sintético semicristalino do grupo dos poliésteres, com boa resistência química, térmica e estabilidade dimensional. A maior parte das fábricas fica na Ásia e a qualidade varia conforme o controle de produção.</p>
<h3>Seda, mink sintético, vison, cashmere e mink real</h3>
{term("Silk (seda):", "produzido para imitar a seda, é brilhante e maleável, mas <strong>não retém a curvatura</strong> por muitos dias. Geralmente é PBT puro. Em dias quentes tende a relaxar e ficar mais reto, e o brilho preto pode ficar parecido com plástico.")}
{term("Mink sintético (synthetic mink):", "o mais usado. Muito leve e macio, confortável, com preto intenso e efeito matte. Feito de uma mistura de poli/fibra, também conhecido comercialmente como vison ou cashmere.")}
<h3>Fio elipse × fio cônico</h3>
{term("Fio elipse (flat):", "base achatada, abraça maior ângulo do cílio natural, com bifurcação sutil nas pontas e melhor aderência por ter maior área de acoplagem.")}
{term("Fio cônico (classic):", "base circular, mais difícil de acoplar. É o fio exigido em campeonatos de técnica clássica.")}
{figs("flat-classic","elipse","elipse-cola")}
"""))

p3.append(("fios-tecnologicos", "Fios tecnológicos", f"""
<p>Os fios tecnológicos permitem a iniciantes aplicar extensões com muito mais volume e rapidez. Antes, isso só era possível, com segurança, pelo volume russo ou mega volume. São fabricados com <strong>Nano PBT</strong>, muito mais leve. Nesta categoria estão o fio Y, o fio W e a mais nova evolução, os fans premade.</p>
<h3>Fio W e suas variações (volume egípcio)</h3>
<p>Destacam-se pela variedade de fios presos em uma única base, com opções de <strong>3D até 10D</strong>. A aplicação segue o mesmo procedimento dos fios individuais, com resultado duradouro.</p>
{figs("fio-w","fio-w-resultado")}
<h3>Fio Y e suas variações (volume brasileiro)</h3>
<p>Possui duas variedades no mercado, que se diferenciam pela quantidade de fios presos em uma única base e de bifurcações nas pontas (4 a 6). Dá mais volume que o fio a fio e é aplicado da mesma forma.</p>
{figs("fio-y","fio-y-resultado")}
{note("<strong>Lembre-se:</strong> avalie a estrutura do fio natural da cliente para preservar a saúde. Quanto mais pontas o fio tiver, mais volume entrega, mas a base fica mais grossa e o peso aumenta.")}
"""))

p3.append(("premade", "Fans premade", f"""
<p>A mais nova evolução das extensões: fans montados manualmente, perfeitos, comercializados desde <strong>3D até 24D</strong>, de material coreano, com leveza e delicadeza. Como já vêm prontos, você aplica da mesma forma que os fios tecnológicos e entrega do volume russo ao mega volume. Encontrados nas espessuras <strong>0,03 / 0,05 / 0,07</strong>.</p>
<p>Há curvaturas tradicionais (C, D), curvaturas criativas (L, L+, M) e versões já prontas para criar o efeito <em>wisp</em>, em caixas mix e individuais, pretos e coloridos.</p>
{figs("premade-d","premade-curvas")}
<p>Para aplicar, você encontra os fans soltos ou fixados em uma fita. Para removê-los da fita sem desmontá-los, use uma pinça de boa precisão e pegue pela <strong>base</strong>.</p>
{note("Mesmo com fans prontos, a técnica é considerada clássica: você entrega volume russo ou mega volume (3D a 16D). Os fans já vêm com pouco adesivo, então atenção à quantidade na hora de acoplar.")}
"""))

p3.append(("curvaturas", "Curvaturas", f"""
<p>As curvaturas existem em grande variedade e devem ser escolhidas conforme o trabalho proposto, com atenção ao biótipo facial de cada cliente. Além das tradicionais, há as <strong>criativas</strong>, a tendência mais recente (as mais usadas hoje são L e M), para efeitos como fox e seta. Aparecem no fio a fio, nos tecnológicos e nos premades.</p>
{figs("curvas-tabela","curvas-tradicionais")}
<h3>Efeito de cada curvatura</h3>
{table(["Curvatura","Indicação e efeito"],[
 ["<strong>B</strong>","Cílios voltados para cima, para um efeito perceptível mas natural. Mais reta na base e curva suave perto da ponta. Indicada também para olhos profundos."],
 ["<strong>C</strong>","A mais popular: ideal para a maioria das clientes, sem exagero. Abre e levanta o olhar com qualquer estilo de mapping. Alonga o olhar."],
 ["<strong>CC</strong>","Abre, arredonda e levanta o olhar."],
 ["<strong>D / DD</strong>","As mais dramáticas, para um look ousado. Melhor em cílios retos ou voltados para baixo. Projetam o olhar para trás, levantam e abrem."],
 ["<strong>L</strong>","Base plana com curva acentuada, ponta voltada para frente. Ótima para cílios retos ou voltados para baixo; levanta e cria efeito gatinho com elevação no canto externo."],
 ["<strong>L+</strong>","Ideal para mapping que promove alongamento e deixa o olhar mais sensual. Evitar no mapping boneca."],
 ["<strong>LC</strong>","Projeta o olhar para frente e promove alongamento."],
 ["<strong>M</strong>","Boa para quase todas as clientes, em especial cílios retos ou caídos; projeta o olho para frente e para cima, com visual de olho de gato."]])}
{figs("curvas-criativas","curvas-efeito")}
{note("Para trabalhar com efeitos, as curvaturas mais indicadas são <strong>B, C, CC, M e L</strong>. Para usá-las corretamente, observe o crescimento natural dos cílios: ele influencia o resultado final.")}
"""))

p3.append(("diametro-comprimento", "Comprimento e diâmetro", f"""
<h3>Diâmetro</h3>
<p>É a espessura de cada fio. Os fios sintéticos têm variações e devem ser escolhidos conforme a técnica e a estrutura do fio natural. <strong>O diâmetro da extensão deve ser o mais próximo possível do diâmetro do cílio natural.</strong></p>
{table(["Técnica","Diâmetros usuais"],[
 ["Fio a fio","0,10 · 0,12 · 0,15 · 0,18 · 0,20 · 0,25"],
 ["Fio tecnológico","0,05 · 0,07 · 0,10"],
 ["Volume russo","0,05 · 0,07 (fans de 2 a 7 fios para cada fio natural)"],
 ["Mega volume","0,03 · 0,05"]])}
{figs("diametros","espessura")}
<h3>Comprimento</h3>
<p>Tamanho de cada fio sintético. No Brasil é mais comum usar de <strong>7 a 14 mm</strong>, mas avalie sempre o fio natural, evitando sobrecarregá-lo, tanto no diâmetro quanto no comprimento.</p>
{note("O comprimento da extensão não deve ultrapassar <strong>2 a 3 mm</strong> o comprimento dos cílios naturais.")}
{fig("comprimentos")}
"""))

p3.append(("mapping", "Mapping", f"""
<p>O mapeamento é altamente personalizado: não existe uma abordagem que sirva para todo mundo. Ele define o olhar desejado e a construção de um olhar único, combinando tamanhos e curvaturas conforme o formato dos olhos e as preferências da cliente. Sem ele, o trabalho não resulta em harmonia visual.</p>
<p>Para precisão, prefira mapear com a cliente de <strong>olhos abertos</strong>: peça que fixe o olhar em linha reta, marque a parte superior da pálpebra e transfira para o pad. Outra técnica é dividir os olhos em quadrantes iguais e traçar o mapeamento. Mantenha conversa constante com a cliente sobre expectativas e avalie com segurança se é possível atendê-las.</p>
<h3>Pontos de referência</h3>
{ul("Canto interno: primeiro fio", "Canto externo natural: último fio", "Início e final da íris", "Pupila")}
{fig("mapping-olho")}
<h3>O que cada região proporciona</h3>
{table(["Ponto","Região","Efeito e indicação"],[
 ["<strong>A</strong>","Canto interno (A → D1)","Perfeito para olhos afastados: aproxima o olhar pelo direcionamento dos fios."],
 ["<strong>B</strong>","Canto externo (B → D2)","Alonga, estreita e afasta o olhar. Efeito gatinho, fox, delineado, sereia."],
 ["<strong>C</strong>","Meio (início ao final da íris, D1 → D2)","Abre o olhar. Camufla olhos profundos, pálpebras caídas e olhos pequenos. Usado no mapping boneca."],
 ["<strong>D2</strong>","Final da íris (C → D2)","Mapping coringa: levanta o olhar e camufla o caimento das pálpebras. Usado no mapping esquilo."]])}
{figs("mapping-quadrantes","mapping-quadrantes-2")}
<h3>Análises principais</h3>
<p>Antes de mapear, identifique: formato dos olhos; posicionamento (distância entre os olhos); profundidade (proeminentes ou profundos); linha horizontal (ascendentes ou descendentes); e altura dos olhos e sobrancelhas.</p>
{fig("tipos-olhos", "Tipos de olhos: treine a indicação de mapping para cada um.")}
<h3>Tipos de mapping</h3>
{table(["Mapping","Efeito","Indicado para"],[
 ["Boneca","Abre o olhar","Olhos separados, pequenos ou caídos"],
 ["Esquilo","Levanta e alonga o olhar","Olhos juntos ou com caimento de pálpebras"],
 ["Coringa","Fica bom em qualquer tipo de olho","Quando houver dúvida"],
 ["Gatinho","Estreita e alonga (direcione em ângulo de 130° a 180°, a partir do meio do olho)","Olhos que pedem alongamento"]])}
{note("Quando a lash consegue fazer o mapeamento correto, ela cria sua <strong>assinatura artística</strong>: o mapeamento entrega harmonização do olhar. Você pode dominar qualquer técnica, mas se não souber escolher o mapping, seu trabalho não vai se destacar.")}
"""))

p3.append(("materiais", "Descrição de materiais", f"""
<p>Antes da lista completa (no fim da apostila), conheça a função de cada material.</p>
<h3>Pinças</h3>
<p>As <strong>retas</strong> são usadas no isolamento dos fios; as <strong>curvas</strong>, na retirada e acoplagem. Evite que caiam no chão: perdem a precisão e entortam as pontas, que são super finas.</p>
{fig("pincas")}
<h3>Higrômetro</h3>
<p>Uso essencial: é o único acessório que mostra a <strong>umidade e a temperatura</strong> do ambiente de trabalho, para o adesivo funcionar corretamente e as aplicações durarem. Deixe-o sempre próximo de onde atende.</p>
{fig("higrometro")}
<h3>Primer / Cleanser</h3>
<p>Higieniza os cílios e melhora a fixação: remove a oleosidade natural, resíduos de maquiagem e sujidades que o shampoo não retirou, além de elevar o pH do fio natural, favorecendo uma acoplagem mais rápida e eficaz.</p>
{fig("primer")}
<h3>Pad e micropore</h3>
<p>O <strong>pad</strong> tem formato anatômico e é livre de fiapos, o mais confortável para a cliente. Protege a pálpebra inferior, ajuda a isolar os cílios inferiores e dá melhor visão do campo de trabalho, além de proteger a região das pontas das pinças. O <strong>micropore</strong> auxilia no isolamento dos fios inferiores, no levantamento das pálpebras e no afastamento do canto interno dos olhos.</p>
{figs("pad-aplicacao","pad-certo-errado","micropore")}
{note("Se a cliente lacrimejar ou relatar incômodo ou ardência, <strong>pare o atendimento</strong> e verifique se pad e fitas estão na posição correta e se os olhos não estão entreabertos.")}
<h3>Nano mister</h3>
<p>Acelera a cura do adesivo, dispersando nanopartículas de água em movimentos circulares, a distância do rosto. Hoje já existem produtos que o substituem, como os finalizadores, que curam o adesivo rapidamente.</p>
{fig("nano-mister")}
<h3>Suporte para fixação dos fios</h3>
<p>Há grande variedade: de apoio na bancada ou fixados na mão. Não existe regra; escolha o que mais se adaptar. Se optar pelo de apoio, prefira os mais pesados, que dão estabilidade.</p>
{figs("paleta-fios","suporte-mao")}
<h3>Suporte para adesivo</h3>
<p>Use o que mais se adaptar e que conserve o adesivo. Quanto menos o adesivo ficar exposto, melhor a fixação: prefira recipientes com orifício.</p>
{figs("suporte-cola","jade")}
<h3>Microbrush, aplicador, escovinha e caneta</h3>
{ul("<strong>Microbrush descartável:</strong> para aplicar removedores, primer e finalizadores.", "<strong>Aplicador descartável:</strong> bastonete de fibra sintética para higienizar os cílios antes da aplicação; também serve para aplicar removedor.", "<strong>Escovinha descartável:</strong> penteia as extensões durante o procedimento e facilita o alinhamento. Uso individual; após a aplicação, ofereça à cliente para manter os cuidados.", "<strong>Caneta:</strong> de ponta fina, de preferência preta (para o mapping no pad) e branca (para marcar a pele).")}
{figs("microbrush","aplicador","escovinha","caneta")}
<h3>Espuma para limpeza e pump</h3>
<p>É o primeiro passo antes de iniciar o alongamento: higienize a região dos olhos. Comece removendo resíduos de maquiagem com água micelar e coloque uma quantidade adequada no pump para criar espuma. Existem shampoos específicos para cílios; um shampoo com <strong>pH entre 7,3 e 7,5</strong> remove impurezas com mais eficácia, mantendo os fios mais alcalinos.</p>
{figs("agua-micelar","pump","espuma")}
<h3>Removedor</h3>
<p>Remove as extensões. Há em gel e em pasta. Os de textura densa tendem a ser mais confortáveis por não escorrerem.</p>
{fig("removedor")}
<h3>Finalizadores</h3>
<p>Ao aplicar o finalizador, ele <strong>encapsula imediatamente os fumos</strong> e acelera a cura do ponto de ligação do adesivo, evitando que os olhos fiquem expostos ao processo de cura e reduzindo o risco de irritação e alergia. Também dá flexibilidade às ligações e aumenta a retenção.</p>
{ul("Sem choque de cura", "Aumenta a retenção", "Funciona com todas as colas", "Reduz irritação e desenvolvimento de processos alérgicos")}
{fig("finalizador")}
{note("Aplique o finalizador somente na ligação do adesivo com o fio natural, afastado da pele e sem excesso. Após a aplicação, ofereça à cliente para manter os cuidados.")}
"""))
PARTS.append(("Fios e materiais", p3))

# ───────────────────────── PARTE 4 ─────────────────────────
p4 = []
p4.append(("ph", "pH do fio natural", f"""
<p><strong>pH</strong> é a sigla de “potencial hidrogeniônico”: indica a quantidade de H⁺ presente em toda matéria (cabelo, pele, saliva, água...). É medido em uma escala de <strong>0 a 14</strong>.</p>
{table(["Faixa","Tipo de produto","Efeito na cutícula"],[
 ["0 a 6,9","Ácido","Cutícula fechada"],
 ["7,0","Neutro","Cutícula normal: não proporciona boa retenção, pois não está porosa"],
 ["7,1 a 14","Alcalino","Cutícula aberta"]])}
<p>O ideal é deixar o fio <strong>levemente poroso</strong>: a margem é de <strong>7,3 a 7,5</strong>, para não danificar o fio e ter excelente retenção. Nossos olhos têm pH próximo de 7,0, por isso o produto final precisa ser equilibrado para não causar irritação.</p>
{figs("ph-tabela","ph-escala")}
<h3>Como interpretar</h3>
{ul("<strong>pH ácido (1 a 6,9):</strong> o natural e recomendado para o fio fica entre 4,2 e 5,8. Um pH levemente ácido indica fio saudável.", "<strong>pH alcalino (7 a 14):</strong> precisamos do fio levemente alcalino para boa retenção, mas é ideal manter <strong>abaixo de 8</strong> para preservar o fio.", "<strong>pH neutro (7):</strong> é o do olho; não há grande prejuízo ao fio, mas também não há porosidade para boa retenção.")}
<p>É primordial que a lash conheça esta tabela: assim saberá o pH do cílio e da região dos olhos e escolherá com segurança cada produto. Se quiser higienizar e já preparar o fio, opte por shampoo com pH de <strong>7,1 a 7,5</strong>.</p>
<p>Naturalmente, o cílio saudável é ácido, mas alguns shampoos e componentes do dia a dia são alcalinos e podem afetar essa condição. Quanto mais alcalino, mais aberta a cutícula, e as substâncias penetram melhor. Um fio brilhante e forte provavelmente está no pH adequado. Já um fio com pH alcalino alto é frágil, com cutícula sempre aberta, textura áspera e desgasta mais fácil.</p>
{note("A avaliação é <strong>individual</strong>. Clientes com fios fragilizados pedem shampoo de pH mais baixo. Se precisar alcalinizar mais por causa de um fio grosso e oleoso, use shampoo de pH 7,5 (evita irritações nos olhos) e primer de pH 8,0, apenas nesses casos.")}
<h3>Desequilíbrio de pH</h3>
{table(["Possíveis causas","Detalhe"],[
 ["Características naturais de cada pessoa","Diferenças individuais na composição e no pH dos cílios"],
 ["Problemas de saúde ou uso de medicação","Condições ou tratamentos que afetam o pH"],
 ["Estilo de vida","Alimentação, hábitos de higiene e outros hábitos"],
 ["Produtos incorretos de preparo","Produtos que alteram o pH ou não são compatíveis com o fio"]])}
{table(["Problema causado","Consequência"],[
 ["A cola leva mais tempo para secar, mesmo com o ambiente adequado","Atraso na aplicação"],
 ["A cola escorrega e não adere","Menor aderência das extensões"],
 ["Desempenho inconsistente","Queda prematura"],
 ["Clientes diferentes com resultados diferentes no mesmo procedimento","Variação na durabilidade"],
 ["Em casos extremos, a cola não adere","Desprendimento precoce"]])}
"""))

p4.append(("retencao", "Retenção", f"""
<p><strong>Retenção</strong> é manter e prolongar a durabilidade das extensões, que tipicamente duram até cerca de <strong>21 dias</strong> antes de começarem a cair, pela troca de fase dos cílios naturais ou pelos cuidados da cliente. É possível ter durabilidade superior quando você domina a técnica de aplicação, usa corretamente cada produto conforme a necessidade da cliente e se baseia no pH do fio natural.</p>
<p>Como os cílios filtram impurezas, uma boa durabilidade exige higienização adequada. Para o adesivo aderir, é importante abrir suavemente a cutícula do fio, deixando-o mais poroso. Quando o pH está desequilibrado, a aderência cai e não há retenção.</p>
<h3>Os 3 princípios da retenção</h3>
{ol("Entender o pH do fio natural.", "Escolher assertivamente os produtos adequados.", "Higienizar e preparar corretamente os fios naturais.")}
<h3>Passo a passo para o sucesso na retenção</h3>
{ol("<strong>Pré-limpeza:</strong> use água micelar em um pump e faça a espuma; enxágue muito bem para remover resíduos de maquiagem. Apenas isso não prepara o fio: é preciso produtos de pH que alcalinizem os fios naturais.", "<strong>Shampoo específico para extensões:</strong> com microbrush ou lipgloss, faça movimentos de fricção sobre os fios naturais e na linha ciliar, onde há maior concentração de sujeira pelas glândulas sebáceas. Faça duas vezes. Use água filtrada ou mineral em todo o processo.", "<strong>Cleanser:</strong> produto específico para remover a oleosidade. Aplique em todos os cílios, com palito e lipgloss (ou dois lipgloss), sempre com fricção.")}
<p>Repita a limpeza de 2 a 3 vezes durante a aplicação, nos cílios que ainda vão receber a extensão: o rosto continua produzindo oleosidade. Esse preparo abre levemente a cutícula e, junto com o adesivo adequado e a acoplagem correta, entrega excelente retenção.</p>
{figs("ph-cuticula","retencao-cuticula")}
{note("Não esqueça de limpar o chicote das extensões com álcool 70% ou Cleanser, para garantir a higienização completa. Agora é só iniciar a aplicação.")}
"""))

p4.append(("adesivos", "Adesivos", f"""
<p>É um dos assuntos em que a iniciante mais tem dificuldade, porque a durabilidade depende de vários fatores. Use o higrômetro para controlar a temperatura e a umidade conforme a indicação de cada adesivo. Há inúmeras marcas, e é preciso compreender como funcionam e do que são feitos para escolher bem.</p>
<p>Os adesivos têm moléculas de <strong>cianoacrilato</strong>, que iniciam a polimerização ao contato com as moléculas de água do ar. Esse processo une as partículas da cola e a faz aderir aos cílios.</p>
<h3>Breve história</h3>
{ul("<strong>1895:</strong> o polímero é descoberto por Awers Thorpe.", "<strong>1942:</strong> desenvolvido para miras de armas, mas aderia a tudo.", "<strong>1950:</strong> nova fórmula usada em cabines de aeronaves e na sutura de ferimentos (o metil cianoacrilato causava necrose).")}
<p>É uma resina acrílica que polimeriza rapidamente na presença de água, formando cadeias longas e fortes. O cianoacrilato tem duas fases: <em>monômero</em> (líquido) e <em>polímero</em> (sólido). A passagem de uma para outra é a polimerização.</p>
<h3>Estágios da polimerização</h3>
{ul("<strong>Adesão:</strong> tempo de ação especificado em cada adesivo, que une a extensão ao cílio natural.", "<strong>Coesão:</strong> tempo após a acoplagem. Nesse momento, segure e direcione o fio para que fique alinhado e bem acoplado.", "<strong>Polimerização (cura):</strong> processo de cura do adesivo, em média 24 h.")}
<h3>Composição</h3>
<p>Varia conforme o fabricante. O <strong>cianoacrilato</strong> (80 a 90%) deve ter sempre a maior concentração.</p>
{table(["Tipo de cianoacrilato","Características"],[
 ["Metil","Altamente tóxico, <strong>uso proibido</strong>"],
 ["Etil","Secagem rápida, menos tóxico, resistente, cadeia longa"],
 ["Butil","Secagem intermediária"],
 ["Alkoxy","Cadeia longa, secagem e cura lentas, baixo odor e baixa emissão de gases, sensível à umidade, baixa toxicidade"],
 ["Metoxi / Etoxi butil","Grau médico: reduzem o risco de irritações e alergias"]])}
<p><strong>Outros componentes:</strong> estabilizantes (mantêm a molécula afastada e evitam que o adesivo endureça, mas são sensíveis à umidade); espessantes (anidrido ftálico, plastificante); PMMA (polimetil metacrilato, termoplástico que dá elasticidade e resistência); carbon black (cor do adesivo e dispersão); hidroquinona (retarda a secagem e estabiliza).</p>
{table(["Exemplo","Componentes"],[
 ["1","Ethyl cianoacrilato, ethoxyethyl cianoacrilato, PMMA, carbon black"],
 ["2","Etil cianoacrilato, alkoxy-2-cianoacrilato, PMMA"],
 ["3","Ethyl-2-cyanoacrylate, alkoxy-2-cyanoacrylate, n-butyl-2-cyanoacrylate, PMMA, carbon black"],
 ["4","Ethyl-2-cyanoacrylate, polimetil metacrilato, butyl-2-cyanoacrylate, alkoxy-2-cyanoacrylate, carbon black"]])}
<h3>Toxicidade do adesivo</h3>
<p>Está associada à estrutura molecular: quanto mais curta, maior o potencial de toxicidade. Todos os adesivos liberam vapores (a forma vaporizada dos monômeros de cianoacrilato) durante a polimerização. Em contato com olhos, nariz, garganta ou qualquer área úmida do corpo, esses fumos podem causar irritação, inchaço da pálpebra, ressecamento dos olhos e da garganta e, em casos raros, asma.</p>
{table(["Medidas de segurança"],[["Use EPIs"],["Mantenha o ambiente ventilado"],["Controle temperatura e umidade"],["Aplique a quantidade adequada de cola"],["Substitua regularmente a gota do seu adesivo"]])}
<h3>Como escolher o melhor adesivo?</h3>
<p>Escolha adesivos com pelo menos <strong>duas composições</strong> de cianoacrilato, que se tornam menos tóxicos, sempre com cadeia de <strong>grau médico</strong>, e respeite as indicações de umidade e temperatura. O principal é você dominar o que um bom adesivo precisa ter na composição.</p>
<h3>Quando substituir o adesivo?</h3>
{table(["Alteração","Descrição"],[
 ["Textura","Muito viscoso ou pegajoso"],
 ["Desempenho","Diminuição da eficácia, afetando o tempo de fixação ou a retenção"],
 ["Cor","Mesmo após agitar, não fica fluido e homogêneo"]])}
<p>Siga sempre as recomendações do fabricante para uso e armazenamento.</p>
<h3>Existe adesivo antialérgico?</h3>
<p>Não. O que existe são adesivos <strong>hipoalergênicos</strong>: de cadeia longa, com cianoacrilatos de grau médico, que são menos nocivos. Os componentes necessários para uma boa aderência são os mesmos que podem desencadear alergia, e a sensibilidade varia de pessoa para pessoa. Por isso, realize testes de sensibilidade antes da aplicação completa.</p>
<h3>Armazenamento e conservação</h3>
{ul("Mantenha na embalagem original, de preferência em recipiente que possa ser lacrado, longe de calor, umidade e luz solar.", "Agite bem antes de cada uso.", "Troque a gota a cada <strong>20 minutos</strong> ou sempre que ela ficar viscosa.", "O prazo de validade após aberto varia conforme o fabricante e o armazenamento; leia a descrição.", "Limpe o bico para evitar entupimento.")}
{note("<strong>Nunca use algodão</strong> para limpar o bico: ele reage com o adesivo e derrete, gerando combustão prejudicial à saúde.", "warn")}
{figs("cola-gota","cola-pote")}
"""))

p4.append(("temperatura-umidade", "Temperatura e umidade", f"""
<p>Umidade e temperatura são fatores essenciais para a aderência. A umidade é crucial na cura porque o adesivo reage à água:</p>
{ul("<strong>Umidade alta:</strong> o adesivo endurece mais rápido. É preciso trabalhar com agilidade; do contrário, pode curar antes da hora e causar falsa colagem, prejudicando a retenção.", "<strong>Umidade baixa:</strong> o tempo de cura se prolonga, aumentando a chance de os cílios grudarem na aplicação (os chamados <em>stickers</em>).")}
{note("Faixa ideal: <strong>20 a 24 °C</strong> de temperatura e <strong>40 a 65%</strong> de umidade.")}
<p>Selecione o adesivo conforme a temperatura e a umidade do ambiente de trabalho e adapte a agilidade ao tipo de adesivo. Mas esses não são os únicos fatores: higiene adequada, preparação minuciosa e acoplagem precisa também são fundamentais.</p>
{fig("umidade-temp")}
<h3>Soluções práticas</h3>
{table(["Umidade alta","Umidade baixa"],[
 ["Evite produtos com pH alto: eles aceleram a secagem da cola.","Aumente a umidade com um umidificador (se pequeno, coloque-o perto de você)."],
 ["Use adesivos de secagem mais lenta.","Use adesivos de secagem rápida, para evitar <em>stickers</em> e acelerar o procedimento."],
 ["Agilize o processo de acoplagem.","Use menos adesivo para acelerar a secagem."],
 ["Reduza umidade e temperatura com ar-condicionado ou desumidificador.","Evite micro gotas: com baixa umidade o adesivo fica mais líquido."],
 ["Use a gota em recipiente com menos exposição.","Aumente a temperatura do ambiente e a controle."],
 ["Trabalhe com micro gotas (microdrop).","Deixe o ambiente ventilado."]])}
"""))

p4.append(("polimerizacao", "Polimerização e cura do adesivo", f"""
<p>Ambas começam juntas, quando o fio sintético é acoplado ao natural pelo adesivo. Depois de fixado, a cura leva o adesivo do estado líquido ao sólido. O tempo varia conforme a marca e a técnica, e o tempo total de cura é de <strong>cerca de 24 horas</strong>.</p>
{ul("<strong>Início da polimerização:</strong> marca o início da fixação das extensões aos cílios naturais.", "<strong>Processo de cura:</strong> a aderência e a resistência se consolidam.", "<strong>Tempo de secagem:</strong> usualmente de 0,5 a 5 segundos, conforme a técnica e a agilidade da profissional.", "<strong>Adaptação à habilidade:</strong> iniciantes devem preferir adesivos de secagem de 2 a 3 segundos (os mais lentos). Com segurança, migre para os mais rápidos.", "<strong>Tempo total de cura:</strong> cerca de 24 h, quando a aderência alcança a máxima eficácia.")}
{fig("polimerizacao", "Polimerização: do monômero (líquido) ao polímero (sólido).")}
<p>Ao mergulhar o fio, não use adesivo em excesso: não há necessidade e pode prejudicar o trabalho, além de causar complicações e alergias. Hoje existem produtos que fazem a cura do adesivo logo após o procedimento, e a cliente <strong>pode molhar os cílios imediatamente</strong>, sem esperar 24 h.</p>
<h3>Sticker</h3>
<p>Ocorre quando uma extensão gruda na outra ou quando é aplicada em mais de um fio natural. Para evitar: não use adesivo de secagem muito lenta para o seu tempo de acoplagem; controle umidade e temperatura; e isole corretamente. Trabalhar por camadas facilita a visualização. No volume russo, invista em uma pinça de excelente precisão e evite acoplar uma ao lado da outra: aplique uma e vá alternando até preencher.</p>
{note("Stickers são prejudiciais à saúde do fio natural, pois podem arrancá-lo.", "warn")}
{fig("stickers")}
"""))

p4.append(("alergias", "Alergias e irritações", f"""
<p>A alergia é uma resposta do organismo ao contato com uma substância (o alérgeno), com reações exageradas do sistema imunológico. Surge geralmente quando o organismo está mais debilitado e varia de pessoa para pessoa. Os sintomas incluem <strong>edema (inchaço) das pálpebras, vermelhidão, coceira, secreção, lacrimejamento e sensação de corpo estranho</strong>.</p>
<p>As reações às extensões são raras, mas podem ocorrer, e o <strong>cianoacrilato</strong>, presente em todos os adesivos, é um dos componentes envolvidos. Como todo produto químico, pode se tornar irritante a qualquer momento, no primeiro contato ou quando a imunidade estiver baixa. A reação pode surgir durante a aplicação ou em até <strong>72 horas</strong>, pelo contato direto com a cola, só pelo fume ou por outros produtos usados. Quem usa extensões há anos também pode desenvolver alergia.</p>
{fig("alergia")}
<h3>Queimadura química × processo alérgico</h3>
{table(["","Queimadura química","Processo alérgico"],[
 ["O que é","Condição momentânea por contato com o fumo do adesivo, em geral porque os olhos ficaram semiabertos","Resposta do sistema imunológico"],
 ["Sintomas","Olhos vermelhos e coçando, dor e vermelhidão intensa","Olhos vermelhos, coceira (prurido), lacrimejamento, ardência, fotofobia e edema nas pálpebras"]])}
{fig("edema")}
<h3>Como minimizar o risco</h3>
{ul("Faça a aplicação correta, com toda a higienização e o distanciamento da pálpebra.", "Evite conversas durante o procedimento, para a cliente não abrir os olhos nem o pad se mover.", "Preencha sempre a <strong>ficha de anamnese</strong>.", "Se a cliente tem histórico de alergias, faça o <strong>teste de alergia um dia antes</strong>.")}
{note("<strong>NUNCA prescreva medicamento à sua cliente.</strong> Oriente sempre a procurar um médico especialista.", "warn")}
"""))
PARTS.append(("Química e retenção", p4))

# ───────────────────────── PARTE 5 ─────────────────────────
p5 = []
p5.append(("mergulho", "Forma correta de mergulhar os fios", f"""
<p>Ao colocar o fio no adesivo, não use quantidade excessiva: não há necessidade, pode prejudicar o trabalho e causar complicações e alergias.</p>
{ul("<strong>Fio a fio:</strong> mergulhe 30% da base do fio.", "<strong>Fios tecnológicos:</strong> mergulhe até a bifurcação.", "<strong>Curvaturas criativas:</strong> a base deve estar em bom contato com o fio natural; pela anatomia, exigem um pouco mais de habilidade na acoplagem.")}
{figs("mergulho","criativas-ml")}
"""))

p5.append(("isolamento", "Isolamento, acoplagem, distanciamento e direcionamento", f"""
<p>São os pilares de uma excelente aplicação e devem ser executados com excelência para o seu trabalho se destacar.</p>
<h3>Isolamento</h3>
<p>É essencial em qualquer técnica. Como os fios naturais passam por ciclos de crescimento, cada extensão deve ser aplicada individualmente, com pouco adesivo, para não grudar nos fios ao redor e não danificá-los no crescimento natural.</p>
<p>Posicione a mão com a pinça de isolamento (reta ou curva) apoiada na testa da cliente, <strong>sem pesar</strong>. Comece a isolar no sentido da raiz para a ponta, com total visibilidade do fio isolado. Se necessário, use a outra mão com a pinça de acoplagem para auxiliar. O isolamento perfeito exige muito treino.</p>
{fig("isolamento")}
<h3>Acoplagem</h3>
<p>É a aplicação do fio sintético ao natural já isolado. Pode ser feita <strong>por cima</strong>, <strong>por baixo</strong> ou, a menos usada, de lado. Segure por alguns segundos e solte. Certifique-se de que a base do fio sintético está corretamente acoplada: isso garante segurança, conforto e durabilidade.</p>
{fig("acoplagem")}
<h3>Distanciamento</h3>
<p>Respeite <strong>0,5 a 0,7 mm</strong> da pele como margem de segurança (algumas profissionais usam 0,3 mm nos cantos interno e externo). Se o adesivo tocar a pele, a chance de irritação e alergia aumenta bastante. Manter um padrão também harmoniza o alinhamento.</p>
{figs("distancia","distanciamento")}
<h3>Direcionamento</h3>
<p>Acople os fios de forma direcionada e alinhada, conforme o mapping. Se o fio da cliente for torto, faça a acoplagem com direcionamento reto, sem acompanhar o fio natural: assim o trabalho fica alinhado ao mapping.</p>
{fig("direcionamento")}
<h3>Efeitos do direcionamento</h3>
{table(["Ângulo","Efeito"],[["90°","Abertura"],["45°","Elevação"],["130°","Aproximação"],["180°","Alongamento"]])}
"""))

p5.append(("camadas", "Camadas", f"""
<p>Os cílios se organizam em camadas, em média de <strong>2 a 4</strong>, conforme a cliente. Dividir em camadas agiliza a aplicação e é fundamental para os efeitos <em>top line</em> e <em>perfect line</em>. Se feita de forma incorreta, a divisão atrapalha e causa desconforto, além de deixar os olhos expostos.</p>
<p>Use uma fita microporosa estreita, cortada de acordo com o comprimento dos olhos da cliente. Posicione-a sobre as pálpebras móveis, levante todos os cílios e use a pinça para separar delicadamente a primeira camada. Aplique <strong>uma camada por vez</strong>: ao preencher uma, solte a próxima, sequencialmente.</p>
{note("Trabalhar por camadas proporciona melhor visibilidade e facilita a fixação.")}
"""))

p5.append(("transicao", "Transição de curvaturas, top line e perfect line", f"""
<p>A transição de curvaturas permite passar de forma suave entre as diferentes curvaturas e garante um alinhamento perfeito, resultando em trabalhos <em>top line</em> ou <em>perfect line</em>. Trabalhe com no mínimo 2 camadas, faça bom preenchimento e capriche no acabamento.</p>
{table(["","Como é feito","Exemplo"],[
 ["<strong>Top line</strong>","Transição de numerações por camadas, diminuindo o tamanho de baixo para cima, <strong>com a mesma curvatura</strong>. Sem degraus.","Camada inferior 11 mm C · meio 10 mm C · superior 9 mm C"],
 ["<strong>Perfect line</strong>","Transição por camadas diminuindo a numeração <strong>e trocando a curvatura</strong>.","Inferior 11 mm D · meio 10 mm CC · superior 9 mm C"]])}
<p><strong>O que cada medida define:</strong> 9 mm: alinhamento · 10 mm: densidade · 11 mm: tamanho.</p>
{fig("top-perfect")}
"""))

p5.append(("complicacoes", "Como evitar possíveis complicações", f"""
<p>Podem ocorrer intercorrências como sensibilidade, irritação ou alergia, relacionadas desde a assepsia até os produtos usados. O adesivo ainda líquido pode ser nocivo; depois de polimerizado, é menos nocivo. Cada organismo reage de um jeito: ter usado extensões por anos não impede que a cliente desenvolva alergia.</p>
<h3>12 passos para minimizar os riscos</h3>
{ol("Higienize corretamente as mãos antes do procedimento e calce luvas descartáveis.", "Higienize adequadamente os olhos e a região próxima.", "Evite colocar o pad próximo à parte interna dos olhos (dentro da linha d'água).", "Use produtos de qualidade.", "Use fita hipoalergênica para isolar os cílios inferiores e para ajudar na visibilidade dos superiores.", "Mantenha o distanciamento adequado.", "Use a quantidade correta de adesivo, sem excesso.", "Não deixe os olhos da cliente abertos durante o procedimento.", "Evite conversas durante o procedimento; ofereça um ambiente aconchegante para ela relaxar.", "Acople corretamente os fios.", "Não use algodão na região dos olhos.", "Use o finalizador: acelera a polimerização e a cura, diminuindo o risco de irritação e alergia.")}
{note("Se a cliente tiver qualquer intercorrência que exija medicamento, <strong>nunca prescreva</strong>. Oriente a procurar um especialista.", "warn")}
"""))

p5.append(("preparacao", "Preparação, fatores externos e microdrop", f"""
<p>Antes de iniciar, preencha a <strong>ficha de avaliação</strong> e entenda o que sua cliente busca. Analise o fio natural para realizar um procedimento seguro.</p>
<p>Para as extensões durarem, os cílios naturais precisam estar <strong>100% limpos</strong>: qualquer resíduo ou oleosidade cria uma barreira entre adesivo e cílio, causando “falsa colagem” ou retenção menor. Higienize sempre os cílios e a região dos olhos antes de qualquer aplicação e enxágue em abundância. A higienização correta dos olhos previne inflamações e blefarites, e toda cliente deve higienizar diariamente após aplicar as extensões.</p>
<h3>Como controlar os fatores externos</h3>
{ul("Mantenha a sala arejada, para aumentar o nível de O₂.", "Trabalhe com adesivos de média secagem.", "Umidade entre 40 e 65% e temperatura entre 20 e 24 °C; regule o higrômetro.", "Mantenha o adesivo no pacote hermético.", "Use umidificador se a umidade estiver baixa.", "Use a técnica microdrop se a umidade estiver alta.")}
<h3>Técnica microdrop</h3>
<p>Mergulhe o fio sintético no adesivo deixando uma pequena quantidade nele, para que, ao ser acoplado em zigue-zague, se espalhe pelo fio natural. É muito útil em dias de alta umidade, pois facilita a acoplagem e evita colagens falsas.</p>
{fig("microdrop")}
"""))

p5.append(("passo-a-passo", "Passo a passo da aplicação", f"""
{ol("Escolha pelo menos quatro numerações diferentes de fios sintéticos.", "Higienize as mãos e use luvas.", "Com um pincel delicado e descartável, higienize os olhos e a região próxima com água micelar. Repita duas vezes com o shampoo específico e enxágue muito bem (no mínimo 2 vezes).", "Aplique o preparador de sua preferência.", "Posicione os pads nos cílios inferiores, sem que fiquem dentro do olho, e isole os fios inferiores com fita micropore.", "Faça a marcação do mapeamento desejado.", "Com a fita micropore, tracione a pálpebra para facilitar o isolamento. Certifique-se de que o olho da cliente esteja completamente fechado e confortável.", "Agite bem o adesivo, descarte a primeira gota e coloque uma gota no recipiente.", "Posicione as mãos: uma segura a pinça de isolamento; a outra, a pinça para pegar os fios do chicote.", "Depois de isolar, mergulhe um fio sintético no adesivo e posicione-o sobre o fio natural. Segure por alguns segundos na direção desejada.", "Repita até preencher todo o mapeamento.", "Ao finalizar, retire delicadamente as fitas e os pads.", "Aplique o finalizador e use um ventilador para ajudar a evaporar o fumo. Só então peça para a cliente abrir os olhos.", "Verifique se todos os fios estão corretamente acoplados.", "Entregue um manual com os cuidados pós-procedimento e confirme que ela entendeu.", "Ofereça o agendamento do próximo atendimento.")}
"""))

p5.append(("manutencao", "Manutenção", f"""
<p>Geralmente se faz <strong>1 aplicação e de 2 a 3 manutenções</strong>. Com o tempo, o crescimento dos fios naturais faz o mapping se perder e os resíduos de adesivo se acumulam, exigindo limpeza mais eficaz para uma nova aplicação.</p>
<p>Na manutenção, a higienização é feita como na primeira aplicação. Em geral remove-se mecanicamente os fios sintéticos que já se afastaram da raiz e reaplicam-se os que caíram, os que trocaram de fase e os que você removeu.</p>
{note("Para cobrar como manutenção, a cliente deve voltar com <strong>no mínimo 50%</strong> das extensões. Caso contrário, cobre um novo procedimento.")}
<p>Fique atenta se a cliente volta frequentemente com poucas extensões: oriente os cuidados e analise se você está falhando em algum processo.</p>
<h3>Remoção mecânica</h3>
<p>Feita com duas pinças: uma segura o fio natural e a outra remove o sintético, “como se estivesse descascando uma banana”. É a mais usada nas manutenções. Cuidado para não danificar o fio natural e <strong>evite mais de 3 manutenções mecânicas</strong>, pois, mesmo com todo o cuidado, a longo prazo podem fragilizar o fio.</p>
<h3>Remoção química</h3>
<p>Cole uma fita dupla face na pálpebra móvel da cliente e grude nela todos os fios que precisam ser removidos. Com microbrush, aplique o removedor somente na ligação com as extensões, deixe agir e remova. Geralmente é pouco usada. Depois, é só higienizar os cílios e fazer a manutenção.</p>
{figs("manutencao-1","manutencao-2")}
{note("Deixe sempre a próxima manutenção agendada: isso fideliza e evita que a cliente esqueça de marcar.")}
"""))

p5.append(("remocao", "Remoção", f"""
{ol("Aplique o removedor.", "Deixe agir conforme a indicação do fabricante.", "Faça o sistema de varredura com a pinça.", "Limpe os resíduos com cotonetes e certifique-se de que removeu tudo. Se entrarem em contato com água ou shampoo, os resíduos cristalizam e interferem na retenção.", "Depois de remover toda a extensão, limpe o restante com gazes e cotonetes e lave com shampoo <strong>2 vezes</strong>.", "Se quiser, já pode fazer uma nova aplicação.")}
{figs("remocao-1","remocao-2")}
"""))

p5.append(("pos", "Orientações pós-procedimento e lista de materiais", f"""
<h3>Orientações para a cliente</h3>
{ul("Não molhe as extensões por até 24 horas, caso não use finalizador ou seu adesivo não tenha essa tecnologia.", "Higienize os cílios diariamente.", "Não esfregue nem puxe as extensões.", "Seque os olhos com cuidado, apenas pressionando a toalha.", "Penteie delicadamente as extensões.", "Não use demaquilante oleoso ou bifásico na área dos olhos.", "Não use rímel ou curvex.", "Evite dormir em posição que amasse ou pressione os cílios.", "Evite banhos quentes e saunas.", "Sempre que chorar, suar ou mergulhar (mar ou piscina), lave os cílios com água potável.")}
<h3>Lista de materiais</h3>
<div class="checks">{"".join(f'<label><input type="checkbox"> {m}</label>' for m in ["Caixa de cílios","Higrômetro","Shampoo","Primer","Microbrush","Escova descartável","Ventilador","Frasco pump","Paleta suporte de cílios","Removedor de cílios","Pinça curva e pinça reta","Gel pads","Fita micropore","Espelho de mão","Suporte para adesivo","Luvas","Toucas","Maca","Ring light","Mocho"])}</div>
{note("<strong>Onde comprar?</strong> Compare preços para melhorar sua margem de lucro. Hoje, plataformas como Shopee e AliExpress costumam oferecer o melhor custo-benefício.")}
"""))

p5.append(("capping", "Técnica de capping e empilhamento", f"""
<p>O <strong>capping</strong> consiste em acoplar <strong>dois fios artificiais</strong> sobre o fio natural, em formato de sanduíche ou de empilhamento. Embora exista há algum tempo, ganhou destaque com as novas tecnologias de fios, entregando volume e efeitos impressionantes sem montar fans.</p>
<h3>Vantagens</h3>
{ul("Volume e densidade sem montagem de fans.", "Durabilidade das extensões superior a 30 dias.")}
<h3>Quais fios usar</h3>
<p>Fios Y, W, fio a fio cônico ou elipse, inclusive de forma híbrida (por exemplo, fio Y por baixo e fio a fio por cima). A forma mais comercializada hoje é fio Y + fio a fio.</p>
{fig("capping-fios")}
<h3>Formato sanduíche</h3>
<p>Um fio artificial é colocado na parte inferior do cílio natural e outro delicadamente por cima. A acoplagem “abraça” o fio natural e dá muito mais durabilidade. Para maior densidade, use o fio de menor numeração por cima e o de maior numeração por baixo.</p>
{fig("capping-sanduiche")}
<h3>Formato empilhamento</h3>
<p>Dois fios sintéticos são acoplados um sobre o outro no cílio natural, criando um efeito de camadas, com olhar marcante e volumoso. Podem ser acoplados por cima ou por baixo do fio natural. Há empilhamento com fios elipse e com fios tecnológicos.</p>
{fig("capping-empilhamento")}
<h3>Controle do adesivo</h3>
<p>No capping, o controle preciso do adesivo é essencial. O <strong>primeiro fio</strong> é mergulhado até a bifurcação e acoplado ao fio natural por cima; o <strong>segundo fio</strong> é imerso cerca de <strong>1/3</strong> para a devida acoplagem. Isso garante aderência e preserva o fio natural.</p>
{note("Avalie a estrutura do fio natural de cada cliente: a técnica não é indicada para todos os tipos de fio. Só realize se a estrutura for compatível.")}
<h3>Durabilidade do capping</h3>
{ol("<strong>Ciclo de vida natural dos cílios:</strong> o fio artificial fica firmemente acoplado durante o ciclo de crescimento e queda.", "<strong>Qualidade da cola:</strong> adesivos de alta qualidade, com boa cadeia de cianoacrilato, aumentam a retenção. Faça corretamente a higienização e o preparo do fio e controle umidade e temperatura.", "<strong>Alinhamento adequado:</strong> distribuição uniforme e equilibrada melhora a estética e a durabilidade.")}
<p>A durabilidade varia de pessoa para pessoa, conforme os cuidados pós-procedimento e as características individuais.</p>
<h3>Devo fazer manutenção de capping?</h3>
<p>No <strong>sanduíche</strong>, <strong>não</strong> faça manutenção: danifica os cílios naturais e não é viável financeiramente. Quando a cliente quiser trocar, faça toda a remoção de forma <strong>química</strong> e depois uma nova aplicação. No <strong>empilhamento</strong>, como o fio natural não é abraçado pelos dois fios, algumas profissionais fazem manutenção com remoção mecânica.</p>
"""))
PARTS.append(("Técnica de aplicação", p5))

# ───────────────────────── PARTE 6 ─────────────────────────
p6 = []
p6.append(("atendimento", "Atendimento: passo a passo (Master em Durabilidade)", f"""
{ol("Comece o atendimento com o preenchimento da ficha de avaliação.", "Fotografe sua cliente sentada e deitada e decida com ela qual shape será utilizado, avaliando o rosto dela.", "Higienize os olhos com a espuma, usando o pincel de aplicar gloss para esfregar os fios; enxágue com água mineral e seque levemente. Repita 2 vezes, ou mais, até o fio estar completamente limpo.", "Coloque o pad em gel abaixo dos cílios inferiores e, se necessário, cole a fita micropore por cima para isolar os fios inferiores.", "Use a fita transpore para levantar as pálpebras (<strong>cuidado para não deixar os olhos abertos</strong>).", "De acordo com o formato dos olhos, desenhe o mapping para não se perder nem errar os tamanhos.", "Isole os fios em camadas, fixando-os na pálpebra, e retire apenas a primeira camada com uma pinça.", "Isole o fio natural com a pinça reta ou semicurva e depois pegue o fio sintético.", "Molhe o fio na parte superior da cola em um movimento único, deixando o fio limpo ao tirar. Se vir uma bolinha ou pingo de cola, há excesso.", "Aplique o fio com a pinça respeitando o tempo do seu adesivo e a distância da raiz. Aplique em <strong>100% dos fios</strong> para um resultado mais bonito.", "Confira fio por fio: cole os que faltaram e desgrude os que grudaram, para evitar desconfortos.", "Use um finalizador para curar completamente a extensão, ou finalize com o nano mister e peça que a cliente aguarde 24 horas para molhar.", "Retire os micropores e os pads em gel e seque bem os fios antes de pedir para a cliente abrir os olhos.")}
{fig("resultado-3", "Resultado de extensão de cílios: volume, acabamento e alinhamento.")}
"""))

p6.append(("preco", "Preço × valor", f"""
<p>A principal objeção do cliente geralmente é o preço. Ao comunicar o valor do serviço, destaque o <strong>benefício</strong> que será obtido, em vez de só mencionar o preço.</p>
<p>Preço é o custo financeiro; <strong>valor</strong> é o benefício percebido. Imagine que eu ofereça a troca de uma nota de R$ 10 por outra de R$ 10: não é tentador. Mas se eu propuser R$ 100 em troca da mesma nota de R$ 10, a oferta fica muito atrativa.</p>
{note("Ao apresentar seu serviço, não assuste a cliente com o preço. Faça com que ela perceba que está investindo R$ 10 em algo que vale R$ 100 ou mais.")}
"""))

p6.append(("precificacao", "Como precificar seu trabalho", f"""
<p>Uma coisa é fato: a maioria de nós não aprende a cobrar corretamente. Muita gente aprende assim: “olhe o preço das concorrentes e defina o seu”. Isso <strong>não funciona</strong>, porque os custos da concorrente podem ser bem menores que os seus, e ela tem lucro cobrando aquele valor, e você talvez não.</p>
<div class="formula"><span>Custos fixos e variáveis</span> + <span>Região</span> + <span>Experiência</span> = <strong>Valor do procedimento</strong></div>
<h3>Região</h3>
<p>Pesquise os <strong>10 melhores studios</strong> da sua região e faça a média: some os valores e divida por 10.</p>
<h3>Experiência</h3>
<p>Cliente não é modelo: não atenda clientes antes de atender modelos e ter certeza do que está entregando. Assim você cobra o justo pelo que entrega. Considere também o valor que você investiu para aprender.</p>
<h3>Custos</h3>
{ul("<strong>Custo fixo:</strong> tudo o que você gasta tendo atendimento ou não (aluguel, internet, água, luz).", "<strong>Custo variável:</strong> tudo o que você gasta quando há atendimento (material, taxa de cartão, café da cliente, mimo).")}
<h3>Exemplo com valores hipotéticos</h3>
{table(["Item","Valor"],[["Custo fixo mensal","R$ 3.000"],["Custo variável por cliente","R$ 60"],["Preço médio da sua região","R$ 200"],["Meta de atendimentos","30 por mês (1 por dia)"]])}
<p>Quando ainda não temos clientes, definimos uma <strong>meta</strong> de atendimentos. Com 30 atendimentos por mês:</p>
{ul("Custo fixo por atendimento: R$ 3.000 ÷ 30 = <strong>R$ 100</strong>", "Mais o custo variável: R$ 100 + R$ 60 = <strong>R$ 160</strong> (somente custos)", "Margem de lucro: o mínimo recomendado é <strong>30%</strong>, mas você pode cobrar mais, pensando na sua experiência: R$ 160 + 30% = <strong>R$ 208</strong>")}
{note("R$ 208 é o <strong>valor mínimo</strong> que você pode cobrar com base nesses valores hipotéticos.")}
<div class="calc" id="calc">
 <h3>Calculadora de preço mínimo</h3>
 <div class="calc-grid">
  <label>Custo fixo mensal (R$)<input type="number" id="c-fixo" value="3000" min="0" step="10"></label>
  <label>Meta de atendimentos por mês<input type="number" id="c-meta" value="30" min="1" step="1"></label>
  <label>Custo variável por cliente (R$)<input type="number" id="c-var" value="60" min="0" step="1"></label>
  <label>Margem de lucro (%)<input type="number" id="c-lucro" value="30" min="0" step="1"></label>
 </div>
 <p class="calc-out">Valor mínimo por atendimento: <strong id="c-res">R$ 208,00</strong></p>
</div>
"""))
PARTS.append(("Atendimento e negócio", p6))

# ───────────────────────── MONTAGEM ─────────────────────────
toc, body, n = [], [], 0
for part, chs in PARTS:
    toc.append(f'<div class="toc-part">{part}</div>')
    body.append(f'<div class="part-label" id="parte-{re.sub("[^a-z]","",part.lower())}">{part}</div>')
    for cid, title, content in chs:
        n += 1
        toc.append(f'<a href="#{cid}" data-id="{cid}"><span class="n">{n:02d}</span>{title}</a>')
        body.append(f'<section class="chapter" id="{cid}"><header><span class="chap-n">{n:02d}</span><h2>{title}</h2></header>{content}</section>')

tpl = open(os.path.join(ROOT, "tools", "apostila_template.html"), encoding="utf-8").read()
out = tpl.replace("{{TOC}}", "\n".join(toc)).replace("{{BODY}}", "\n".join(body)).replace("{{COUNT}}", str(n))
os.makedirs(os.path.join(ROOT, "apostila"), exist_ok=True)
open(os.path.join(ROOT, "apostila", "index.html"), "w", encoding="utf-8").write(out)
print("capítulos:", n, "| bytes:", len(out))
