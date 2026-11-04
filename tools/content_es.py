"""Spanish content. ES maps each English page path to its Spanish URL and copy.
Reviews stay in their original language: they are verbatim quotes."""

_SP = "¿Atienden en español?"
_SP_A = "Sí. Atendemos en español y en inglés."
_C = "¿Cuánto cuesta"

ES = {}

ES["upholstery"] = dict(
  path="es/tapiceria", service="Tapicería y retapizado de muebles", crumb="Tapicería",
  title="Tapicería de Muebles en Miami | Tapicero y Retapizado | MIAN",
  desc="Tapicería de muebles en Miami: tu tapicero para retapizar sofás, seccionales, sillas de comedor, cabeceros y antigüedades. Recogida gratis y cotización gratis en 24 horas. (786) 348-8650.",
  eyebrow="Tapicería · Miami-Dade",
  h1="Tapicería de Muebles en Miami",
  lede="Conserva el sofá, la silla o el cabecero que te gusta: tu tapicero en Miami lo reconstruye con espuma y tela nuevas en nuestro taller. Recogida gratis, cotización gratis en 24 horas y atención en español.",
  hero_alt="Sofá capitoné con orejas retapizándose en el taller de MIAN en Miami",
  body="""
<h2>Retapizado que le devuelve la vida a un buen mueble</h2>
<p>Una estructura bien hecha dura décadas más que su tela. Retapizar conserva esa estructura y cambia todo lo que se desgasta: la tela, la espuma y el relleno y, cuando hace falta, los resortes y las cinchas. El resultado es un mueble que encaja con tu espacio y tu gusto, listo para durar muchos años más.</p>
<p>Cada pieza se mide, se corta y se cose en nuestro propio taller en 1 NW 62nd St, Miami. Hablas directamente con quienes hacen el trabajo, desde la primera foto hasta la entrega.</p>
<h2>¿Dónde tapizar muebles en Miami?</h2>
<p>Si buscas un tapicero cerca de ti, quieres un taller local que vea la pieza. El nuestro está en 1 NW 62nd St, y hacemos el tapizado de muebles con recogida a domicilio gratis en todo Miami-Dade, desde <a href="/es/zonas/hialeah/">Hialeah</a> y <a href="/es/zonas/north-miami/">North Miami</a> hasta <a href="/es/zonas/kendall/">Kendall</a> y <a href="/es/zonas/miami-beach/">Miami Beach</a>.</p>
<h3>Qué tapizamos</h3>
<ul>
  <li><a href="/es/tapiceria/tapizar-sofa-miami/"><b>Sofás y seccionales</b></a>, incluso modulares y de gran tamaño</li>
  <li><a href="/es/tapiceria/tapizar-sillas-miami/"><b>Sillas de comedor</b></a>, una sola o el juego completo</li>
  <li><a href="/es/tapiceria/cabeceros-tapizados-miami/"><b>Cabeceros y camas</b></a>: capitoné, acanalados o lisos</li>
  <li><a href="/es/tapiceria/tapiceria-cuero-miami/"><b>Sofás y sillas de cuero</b></a></li>
  <li><b>Butacas, sillones de orejas y settees</b></li>
  <li><b>Antigüedades y piezas vintage</b> que vale la pena conservar</li>
  <li><b>Otomanas y bancos</b>, y <a href="/es/tapiceria/cojines-a-medida-miami/"><b>cojines a medida</b></a> de interior y exterior</li>
</ul>
<h3>Telas para los hogares de Miami</h3>
<p>Te ayudamos a elegir según el uso de la pieza: telas de alto rendimiento para niños y mascotas, textiles para exterior que aguantan patios y sol, y lino, terciopelo, bouclé u opciones tipo cuero para la sala. Llevamos los muestrarios a tu casa para que veas cada tela con tu propia luz.</p>
""",
  steps=[("Envía una foto", "Manda por texto o WhatsApp una foto de la pieza. Recibes tu cotización gratis en 24 horas."),
         ("Medimos y eliges", "Medimos y llevamos muestras de tela para que elijas en casa."),
         ("Recogida gratis", "Recogemos la pieza y la reconstruimos en nuestro taller de Miami."),
         ("Entrega", "Tu mueble regresa terminado y listo para usar.")],
  gallery_alt=["Butaca de bouclé con estructura de madera oscura, retapizada por completo",
               "Sillas de comedor retapizadas en tela gris texturizada en Miami",
               "Sofá de terciopelo azul tapizado en el taller de MIAN"],
  faq=[("¿Vale la pena retapizar un sofá en vez de comprar uno nuevo?",
        "Si la estructura está sólida, algo común en muebles antiguos y bien hechos, retapizar suele darte una pieza más resistente que una nueva por el mismo precio, y en la tela exacta que quieres. Si la estructura está rota o mal hecha, te lo decimos con honestidad."),
       (_C+" retapizar un mueble en Miami?",
        "Depende del tamaño de la pieza, de la tela y de cuánto trabajo de espuma o resortes necesite. Envíanos una foto por texto o WhatsApp y te mandamos una cotización gratis en 24 horas."),
       ("¿Cuánto tarda el retapizado?",
        "Depende de la pieza y de la disponibilidad de la tela; te damos una fecha junto con la cotización. Un cliente reciente tuvo su sofá listo dos semanas después de nuestra primera visita."),
       ("¿Hacen tapizado de muebles a domicilio?",
        "Recogemos a domicilio gratis en todo Miami-Dade, tapizamos la pieza en nuestro taller y te la entregamos terminada."),
       ("¿Reparan muebles?",
        "Reparamos lo que va debajo de la tela: espuma, resortes y cinchas. Envía una foto del daño y te decimos qué necesita la pieza."),
       ("¿Van a medir y a mostrar telas?",
        "Sí. Medimos la pieza y llevamos muestras para que elijas la tela en casa."),
       (_SP, "Sí. Atendemos en español y en inglés, desde la cotización hasta la entrega.")],
)

ES["drapery"] = dict(
  path="es/cortinas", service="Cortinas a medida", crumb="Cortinas",
  title="Cortinas a Medida en Miami | Euro y Pinch Pleat | MIAN",
  desc="Cortinas a medida en Miami: euro pleat, pinch pleat, visillos, blackout y exteriores, medidas e instaladas por nosotros. Cotización gratis en 24 horas.",
  eyebrow="Cortinas · Miami-Dade",
  h1="Cortinas a Medida en Miami",
  lede="Cortinas euro pleat y pinch pleat, visillos y blackout cosidos en nuestro taller de Miami, para ventanas altas, puertas corredizas y patios cubiertos. Las medimos y las instalamos nosotros. Cotización gratis en 24 horas.",
  hero_alt="Cortina marfil hecha a medida en una ventana alta en arco en Miami",
  body="""
<h2>Cortinas hechas para tus ventanas, no para un catálogo</h2>
<p>Las cortinas ya hechas casi nunca le quedan a las ventanas de Miami: ventanales altos, ventanas en arco, puertas corredizas y aberturas anchas de patio. Medimos cada abertura y cosemos la cortina a medida en nuestro propio taller, para que caiga recta, llegue al piso como quieres y cierre bien.</p>
<p>Hablas directamente con las personas que miden, cosen e instalan tus cortinas, en español o en inglés, desde la primera foto hasta el día de la instalación.</p>

<h2>Estilos de cortinas que hacemos</h2>
<p>El cabezal, es decir, la forma en que se recoge la tela arriba, define el aspecto de la cortina más que cualquier otra cosa. Estos son los estilos que más hacemos en hogares de Miami.</p>
<h3>Cortinas euro pleat</h3>
<p>Los euro pleats se recogen y se fijan justo en el borde superior, de modo que cada pliegue se abre en ondas suaves y parejas. El resultado es entallado pero relajado, y va muy bien en espacios contemporáneos, condominios y ventanales de piso a techo. <a href="/es/cortinas/cortinas-euro-pleat-miami/">Conoce las cortinas euro pleat</a>.</p>
<h3>Cortinas pinch pleat y plisadas</h3>
<p>Los pinch pleats clásicos se cosen unas pulgadas por debajo del borde superior, y dan pliegues definidos y una caída más llena. Funcionan bien en ambientes tradicionales y de transición, comedores, habitaciones y ventanales de sala. <a href="/es/cortinas/cortinas-pinch-pleat-miami/">Conoce las cortinas pinch pleat</a>.</p>
<h3>Visillos</h3>
<p>Los visillos suavizan el resplandor y dan privacidad de día sin bloquear la luz, algo ideal para ventanas de edificios altos y puertas corredizas. Se pueden combinar con una cortina forrada o blackout en un segundo riel para tener control total.</p>
<h3>Cortinas blackout y forradas</h3>
<p>El forro blackout oscurece habitaciones y salas de cine. Un forro estándar protege la tela del sol de Miami, mejora la privacidad y le da más cuerpo a la caída. <a href="/es/cortinas/cortinas-blackout-miami/">Conoce las cortinas blackout</a>.</p>
<h3>Cortinas para exterior</h3>
<p>Para patios cubiertos, terrazas y balcones cosemos cortinas en telas para exterior que aguantan el sol y la humedad, muchas veces junto con <a href="/es/tapiceria/">cojines de exterior retapizados</a> en una tela que combina. <a href="/es/cortinas/cortinas-exteriores-miami/">Conoce las cortinas para exterior</a>.</p>

<h2>Telas y forros para la luz de Miami</h2>
<p>La luz, el calor y la humedad importan aquí. Te ayudamos a elegir para cada espacio:</p>
<ul>
  <li><b>Visillos</b> para suavizar el resplandor sin oscurecer el espacio</li>
  <li><b>Cortinas forradas</b> que protegen la tela y dan privacidad en espacios soleados</li>
  <li><b>Forro blackout</b> para habitaciones, cuartos de bebé y salas de cine</li>
  <li><b>Textiles para exterior</b> en patios, terrazas y zonas húmedas</li>
  <li><b>Cojines y almohadones</b> cosidos en la misma tela de tus cortinas</li>
</ul>
<p>Llevamos muestras a tu casa para que compares cada opción con tus ventanas, paredes y muebles antes de cortar nada.</p>

<h2>Cortinas a medida en todo Miami</h2>
<p>Medimos, confeccionamos e instalamos cortinas en todo Miami-Dade:</p>
<ul>
  <li><a href="/es/zonas/brickell/"><b>Brickell</b></a>: visillos y blackout para ventanales de piso a techo en edificios altos</li>
  <li><a href="/es/zonas/miami-beach/"><b>Miami Beach</b></a>: cortinas forradas para espacios con mucho sol y cortinas de exterior para terrazas</li>
  <li><a href="/es/zonas/coral-gables/"><b>Coral Gables</b></a>: cortinas forradas para ventanales de sala</li>
  <li><a href="/es/zonas/kendall/"><b>Kendall</b></a>: cortinas a medida para habitaciones y salas</li>
  <li><a href="/es/zonas/doral/"><b>Doral</b></a>: cortinas blackout para habitaciones</li>
  <li><a href="/es/zonas/north-miami/"><b>North Miami</b></a>: muy cerca de nuestro taller en 1 NW 62nd St</li>
</ul>
<p>¿Vas a renovar algo más que las ventanas? También hacemos <a href="/es/tapiceria/">tapicería y retapizado de muebles</a>, y <a href="/es/comercial/">cortinas y asientos para restaurantes, hoteles y espacios de eventos</a>.</p>
""",
  steps=[("Envía una foto", "Comparte fotos de las ventanas. Recibes tu cotización gratis en 24 horas."),
         ("Medimos", "Medimos cada abertura y te ayudamos a elegir tela, forro y cabezal."),
         ("Hecha a medida", "Tu cortina se corta y se cose en nuestro taller de Miami."),
         ("Instalada", "Colgamos tus cortinas, hechas a la medida de tus ventanas.")],
  gallery_alt=["Cortina plisada enmarcando una ventana alta en un hogar de Miami",
               "Cortinas de exterior y asientos retapizados en un patio de Miami",
               "Cortina marfil en una ventana en arco"],
  faq=[(_C+"n las cortinas a medida en Miami?",
        "Depende del tamaño de la ventana, la tela, el forro y el estilo de cabezal. Envíanos fotos de tus ventanas y te mandamos una cotización gratis en 24 horas."),
       ("¿Qué diferencia hay entre euro pleat y pinch pleat?",
        "Los euro pleats se fijan en el borde superior y se abren en ondas suaves, con un aspecto más limpio y contemporáneo. Los pinch pleats se cosen unas pulgadas más abajo y dan pliegues más definidos y un aspecto más tradicional."),
       ("¿Miden e instalan las cortinas?",
        "Sí. Medimos cada abertura para coser la cortina a medida y la instalamos en tu casa."),
       ("¿Mis cortinas deben llevar forro?",
        "En Miami, por lo general sí en espacios soleados: el forro protege la tela de la decoloración y mejora la privacidad. Los visillos son la excepción, cuando quieres que pase la luz."),
       ("¿Hacen cortinas blackout?",
        "Sí. La cortina con forro blackout funciona muy bien en habitaciones y salas de cine."),
       ("¿Hacen cortinas para exterior?",
        "Sí, en telas para exterior para patios cubiertos y terrazas."),
       ("¿Pueden hacer cojines que combinen con mis cortinas?",
        "Sí. Cosemos cojines y almohadones en la misma tela de tus cortinas."),
       ("¿Qué zonas atienden?",
        "Todo Miami-Dade, incluidos Brickell, Miami Beach, Coral Gables, Kendall, Doral y North Miami."),
       (_SP, _SP_A)],
)

_FORRO = ("¿Miden e instalan?", "Sí. Medimos cada abertura, cosemos las cortinas a medida en nuestro taller de Miami y las instalamos en tu casa.")

ES["drapery/euro-pleat-drapes-miami"] = dict(
  path="es/cortinas/cortinas-euro-pleat-miami", service="Cortinas euro pleat a medida",
  parent=("Cortinas", "/drapery/"), crumb="Cortinas Euro Pleat",
  title="Cortinas Euro Pleat en Miami | A Medida e Instaladas | MIAN",
  desc="Cortinas euro pleat en Miami, cosidas a medida en nuestro taller e instaladas por nosotros. Visillo, forradas o blackout. Cotización gratis en 24 horas.",
  eyebrow="Cortinas · Euro pleat",
  h1="Cortinas Euro Pleat en Miami, a Medida",
  lede="Cortinas euro pleat entalladas para condominios, ventanas altas y puertas corredizas: las medimos, las cosemos en nuestro taller de Miami y las instalamos. Cotización gratis en 24 horas.",
  hero_alt="Cortinas plisadas a medida enmarcando una ventana alta en un hogar de Miami",
  body="""
<h2>Qué es una cortina euro pleat</h2>
<p>El euro pleat, también llamado pliegue fijado arriba, recoge la tela en pequeños grupos de pliegues y los fija justo en el borde superior. Debajo de ese punto, cada pliegue se abre libremente en ondas suaves y parejas hasta el piso. Queda entallado, pero más ligero que un pinch pleat clásico.</p>
<p>Ese equilibrio explica por qué es uno de los estilos más pedidos en Miami: se ve limpio y moderno en ventanales de piso a techo, y a la vez suave y bien terminado en una habitación o una sala.</p>

<h2>Dónde funcionan mejor</h2>
<ul>
  <li><b>Condominios y edificios altos</b>: paños largos que enmarcan la vista sin verse pesados</li>
  <li><b>Puertas corredizas</b>: paños que se recogen ordenados a un lado</li>
  <li><b>Salas contemporáneas y de transición</b> donde buscas líneas limpias</li>
  <li><b>Habitaciones</b>, con forro blackout para dormir mejor</li>
  <li><b>Ventanas altas y de doble altura</b>, donde un cabezal simple deja protagonismo a la tela</li>
</ul>

<h2>Visillo, forrada o blackout</h2>
<p>El cabezal define el aspecto; la tela y el forro deciden cómo funciona la cortina. El sol de Miami es fuerte, así que te ayudamos a elegir para cada espacio:</p>
<ul>
  <li><b>Visillos euro pleat</b> que suavizan el resplandor y dan privacidad de día</li>
  <li><b>Cortinas euro pleat forradas</b> que protegen la tela y dan más cuerpo a los pliegues</li>
  <li><b>Euro pleat con forro blackout</b> para habitaciones, cuartos de bebé y salas de cine</li>
  <li><b>Visillo y cortina forrada</b> en dos rieles, para controlar la luz de la mañana a la noche</li>
</ul>
<p>Llevamos muestras a tu casa para que compares telas con tus ventanas, paredes y muebles antes de cortar nada.</p>

<h2>Hechas en nuestro taller de Miami, instaladas por nosotros</h2>
<p>Cada abertura se mide por separado y la cortina se corta y se cose a medida en nuestro taller en 1 NW 62nd St, Miami. Eso hace que los pliegues caigan parejos y que el ruedo quede como quieres. Después las instalamos nosotros mismos.</p>
<p>¿No sabes si el euro pleat es el cabezal indicado? Compáralo con las <a href="/es/cortinas/cortinas-pinch-pleat-miami/">cortinas pinch pleat</a> o mira todos los estilos en <a href="/es/cortinas/">cortinas a medida en Miami</a>.</p>
""",
  steps=[("Envía una foto", "Comparte fotos de las ventanas. Recibes tu cotización gratis en 24 horas."),
         ("Medimos", "Medimos cada abertura y llevamos muestras de tela y forro."),
         ("Hecha a medida", "Tus cortinas euro pleat se cortan y se cosen en nuestro taller de Miami."),
         ("Instalada", "Colgamos las cortinas y revisamos el ajuste.")],
  gallery_alt=["Cortina plisada enmarcando una ventana alta en Miami",
               "Cortina marfil a medida en una ventana en arco",
               "Cortinas de exterior en un patio cubierto de Miami"],
  faq=[("¿Qué es una cortina euro pleat?",
        "Una cortina cuyos pliegues se fijan solo en el borde superior, de modo que abajo se abren libremente. Se ve entallada, pero más suave y contemporánea que una pinch pleat."),
       ("¿Qué diferencia hay entre euro pleat y pinch pleat?",
        "Los euro pleats se fijan en el borde superior y se abren en ondas suaves. Los pinch pleats se cosen unas pulgadas más abajo y dan pliegues más definidos y un aspecto más tradicional."),
       ("¿Las cortinas euro pleat pueden ser blackout?",
        "Sí. Podemos ponerles forro blackout para habitaciones y salas de cine, o un forro estándar para espacios soleados."),
       (_C+"n las cortinas euro pleat a medida en Miami?",
        "Depende del tamaño de la ventana, la tela y el forro. Envíanos fotos y te mandamos una cotización gratis en 24 horas."),
       _FORRO, (_SP, _SP_A)],
)

ES["drapery/pinch-pleat-drapes-miami"] = dict(
  path="es/cortinas/cortinas-pinch-pleat-miami", service="Cortinas pinch pleat a medida",
  parent=("Cortinas", "/drapery/"), crumb="Cortinas Pinch Pleat",
  title="Cortinas Pinch Pleat en Miami | A Medida e Instaladas | MIAN",
  desc="Cortinas pinch pleat en Miami, cosidas a medida en nuestro taller e instaladas por nosotros. Forradas, blackout o visillo. Cotización gratis en 24 horas.",
  eyebrow="Cortinas · Pinch pleat",
  h1="Cortinas Pinch Pleat en Miami, a Medida",
  lede="Cortinas pinch pleat clásicas, con pliegues definidos y estructurados: las medimos, las cosemos en nuestro taller de Miami y las instalamos. Cotización gratis en 24 horas.",
  hero_alt="Cortina plisada marfil a medida en una ventana alta en arco en Miami",
  body="""
<h2>Qué es una cortina pinch pleat</h2>
<p>El pinch pleat recoge la tela en grupos de pliegues y los cose unas pulgadas por debajo del borde superior, con un cabezal reforzado encima. Como el pliegue queda sujeto en ese primer tramo, arranca definido y estructurado y cae en ondas profundas y llenas.</p>
<p>Es una opción que no pasa de moda: se ve formal en un comedor, refinada en una habitación y con presencia en un ventanal de sala.</p>

<h2>Dónde funcionan mejor</h2>
<ul>
  <li><b>Salas tradicionales y de transición</b>: paños llenos y entallados que enmarcan ventanales</li>
  <li><b>Comedores</b>, donde los pliegues estructurados dan un acabado más formal</li>
  <li><b>Habitaciones</b>, con forro blackout para dormir mejor</li>
  <li><b>Ventanas altas y en arco</b> que piden una caída más llena</li>
  <li><b>Hoteles y espacios de eventos</b>: mira nuestro trabajo <a href="/es/comercial/">comercial</a></li>
</ul>

<h2>Forrada, blackout o visillo</h2>
<p>Los pinch pleats mantienen mejor su forma cuando la tela tiene cuerpo, por eso casi todas las que hacemos van forradas. Con la luz de Miami, te ayudamos a elegir para cada espacio:</p>
<ul>
  <li><b>Pinch pleat forrada</b>: protege la tela, da privacidad y ayuda a mantener los pliegues</li>
  <li><b>Pinch pleat con forro blackout</b> para habitaciones, cuartos de bebé y salas de cine</li>
  <li><b>Visillo pinch pleat</b>, una versión más ligera que igual filtra el resplandor</li>
  <li><b>Cojines y almohadones</b> en la misma tela de tus cortinas</li>
</ul>
<p>Llevamos muestras de tela y forro a tu casa para que veas cada opción con tus ventanas, paredes y muebles antes de cortar nada.</p>

<h2>Hechas en nuestro taller de Miami, instaladas por nosotros</h2>
<p>Cada ventana se mide por separado y las cortinas se cortan y se cosen a medida en nuestro taller en 1 NW 62nd St, Miami, para que los pliegues queden bien repartidos en todo el ancho y el ruedo termine donde quieres. Luego las instalamos nosotros mismos.</p>
<p>¿Prefieres un cabezal más suave y contemporáneo? Compara con las <a href="/es/cortinas/cortinas-euro-pleat-miami/">cortinas euro pleat</a> o mira todos los estilos en <a href="/es/cortinas/">cortinas a medida en Miami</a>.</p>
""",
  steps=[("Envía una foto", "Comparte fotos de las ventanas. Recibes tu cotización gratis en 24 horas."),
         ("Medimos", "Medimos cada abertura y llevamos muestras de tela y forro."),
         ("Hecha a medida", "Tus cortinas pinch pleat se cortan y se cosen en nuestro taller de Miami."),
         ("Instalada", "Colgamos las cortinas y revisamos el ajuste.")],
  gallery_alt=["Cortina plisada marfil en una ventana en arco en Miami",
               "Cortina plisada enmarcando una ventana alta en Miami",
               "Tapicería y textiles para un restaurante de Miami"],
  faq=[("¿Qué es una cortina pinch pleat?",
        "Una cortina cuyos pliegues se cosen unas pulgadas por debajo del borde superior, con ondas definidas y un aspecto más lleno y tradicional."),
       ("¿Pinch pleat o euro pleat: cuál elijo?",
        "Los pinch pleats van bien en ambientes tradicionales y de transición y dan una caída más formal. Los euro pleats se fijan solo arriba, con ondas más suaves y un aspecto contemporáneo. Llevamos muestras para que decidas en casa."),
       ("¿Las cortinas pinch pleat pueden ser blackout?",
        "Sí. Podemos ponerles forro blackout para habitaciones y salas de cine, o un forro estándar para espacios soleados."),
       (_C+"n las cortinas pinch pleat a medida en Miami?",
        "Depende del tamaño de la ventana, la tela y el forro. Envíanos fotos y te mandamos una cotización gratis en 24 horas."),
       _FORRO, (_SP, _SP_A)],
)

ES["commercial"] = dict(
  path="es/comercial", service="Tapicería comercial", crumb="Tapicería Comercial",
  title="Tapicería Comercial en Miami | Restaurantes y Hoteles | MIAN",
  desc="Tapicería comercial en Miami-Dade: banquetas y booths de restaurante, sillas, asientos de hotel y oficina, y cojines náuticos. Telas contract. Cotización gratis en 24 horas.",
  eyebrow="Comercial · Miami-Dade",
  h1="Tapicería Comercial en Miami: Restaurantes, Hoteles y Oficinas",
  lede="Tapizamos banquetas, booths, sillas de comedor y asientos de lounge con telas de grado contract y espuma resistente, hechos en nuestro taller de Miami. Cotización gratis en 24 horas.",
  hero_alt="Banqueta de restaurante y sillas de cuero tapizadas para un local de Miami",
  body="""
<h2>Asientos hechos para el uso diario intenso</h2>
<p>Los asientos de un restaurante u hotel reciben en un mes más desgaste que un sofá de casa en un año. Los reconstruimos con telas de grado contract y espuma resistente para que mantengan la forma y se limpien fácil, y los hacemos en nuestro propio taller de Miami, así que tratas directamente con quienes hacen el trabajo.</p>
<h3>Qué tapizamos para negocios</h3>
<ul>
  <li><b>Banquetas y booths de restaurante</b></li>
  <li><b>Sillas de comedor y de bar</b>, en juegos iguales</li>
  <li><b>Asientos de lounge y lobby</b> para hoteles y oficinas</li>
  <li><b>Cabeceros y textiles</b> para hotelería</li>
  <li><b>Cojines náuticos y de exterior</b> para yates y terrazas</li>
  <li><b>Cortinas a medida</b> para comedores y espacios de eventos</li>
</ul>
<h3>Trabajamos según tu negocio</h3>
<p>Dinos tu horario y planificamos la recogida y la entrega para que tu local pase el menor tiempo posible sin sus asientos. Recibes una cotización por escrito y una fecha antes de empezar.</p>
""",
  steps=[("Envía fotos", "Fotos y un conteo aproximado de piezas. Cotización gratis en 24 horas."),
         ("Visita al local", "Medimos en el sitio y te ayudamos a elegir telas de grado contract."),
         ("Taller", "Todo se reconstruye en nuestro taller de Miami."),
         ("Entrega", "Las piezas regresan en la fecha acordada, listas para el servicio.")],
  gallery_alt=["Banqueta de restaurante tapizada en cuero marrón en Miami",
               "Cojines de exterior a rayas azul marino para un yate en una marina de Miami",
               "Juego de sillas de comedor tapizadas"],
  faq=[("¿Con qué tipo de negocios trabajan?",
        "Restaurantes, hoteles, oficinas y embarcaciones en todo Miami-Dade: cualquier lugar con asientos de uso intenso."),
       ("¿Usan telas de grado contract?",
        "Sí. Para asientos comerciales recomendamos telas de grado contract y de alto rendimiento, con espuma resistente."),
       ("¿Pueden trabajar según nuestro horario?",
        "Dinos tu horario y planificamos la recogida y la entrega según él."),
       ("¿Cómo pido una cotización?",
        "Envía fotos y un número aproximado de piezas por texto, WhatsApp o el formulario. Recibes una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

ES["upholstery/sofa-reupholstery-miami"] = dict(
  path="es/tapiceria/tapizar-sofa-miami", service="Retapizado de sofás y seccionales",
  parent=("Tapicería", "/upholstery/"), crumb="Tapizar Sofás",
  title="Tapizar Sofá en Miami | Retapizar Sofás y Seccionales | MIAN",
  desc="Tapizar o forrar tu sofá en Miami: tela nueva, espuma nueva y la misma estructura. Medimos en casa, recogida gratis y cotización en 24 horas.",
  eyebrow="Tapicería · Sofás",
  h1="Tapizar Sofás en Miami",
  lede="Tela y espuma nuevas para el sofá o seccional que ya tienes, reconstruido en nuestro taller de Miami. Medimos en tu casa, recogemos gratis y cotizamos en 24 horas.",
  hero_alt="Sofá de terciopelo azul tapizado en el taller de MIAN en Miami",
  body="""
<h2>Cuándo vale la pena retapizar un sofá</h2>
<p>Si la estructura está sólida y el sofá le queda bien a tu espacio, retapizar suele ser la mejor decisión. Presiona los brazos y el respaldo: una buena estructura se siente firme y no se balancea. Los asientos hundidos, los cojines aplastados y la tela gastada tienen arreglo. Si la estructura está rota o mal hecha, te diremos que lo cambies.</p>
<h2>Qué cambia en tu sofá</h2>
<ul>
  <li><b>Tela</b>: se retira y se cambia por la que elijas</li>
  <li><b>Espuma del asiento</b>: se reemplaza para que los cojines recuperen forma y comodidad</li>
  <li><b>Resortes y cinchas</b>: se reparan donde hayan cedido</li>
  <li><b>Detalles</b>: vivos, botones, faldas y estilo de cojín pueden quedarse o cambiar</li>
</ul>
<h2>¿Cuánto cuesta tapizar un sofá?</h2>
<p>El precio depende de cuatro cosas: el tamaño del sofá, la cantidad de tela, la tela que elijas y si la espuma, los resortes o las cinchas necesitan trabajo. No publicamos un precio fijo porque dos sofás del mismo tamaño pueden necesitar trabajos muy distintos. Envía una foto y recibes una cotización gratis por escrito en 24 horas.</p>
<h2>Seccionales y sofás grandes</h2>
<p>Los seccionales y sofás modulares se construyen por piezas, así que medimos y cotizamos cada sección. Esto importa en los condominios de Miami, donde reemplazar un sofá grande no siempre es fácil: retapizar conserva un mueble que ya cabe en tu ascensor y en tu sala. Dinos las reglas de entrega de tu edificio y planificamos la recogida según ellas.</p>
<h2>Telas para tu forma de vivir</h2>
<p>Las telas de alto rendimiento aguantan niños, mascotas y uso diario. El terciopelo y el bouclé van bien en una sala más tranquila. Llevamos muestras a tu casa para que las compares con tu propia luz. Mira todos nuestros <a href="/es/tapiceria/">servicios de tapicería</a> o lee sobre cómo <a href="/es/tapiceria/tapizar-sillas-miami/">tapizar sillas</a>.</p>
""",
  steps=[("Envía una foto", "Manda una foto del sofá. Recibes tu cotización gratis en 24 horas."),
         ("Medimos y eliges", "Medimos en tu casa y llevamos muestras de tela."),
         ("Recogida gratis", "Recogemos el sofá y lo reconstruimos en nuestro taller de Miami."),
         ("Entrega", "Tu sofá regresa con tela y espuma nuevas.")],
  gallery_alt=["Sofá de terciopelo azul tapizado en Miami",
               "Seccional gris con otomana en una sala frente al mar en Miami",
               "Settee capitoné retapizándose en el taller"],
  faq=[(_C+" tapizar un sofá en Miami?",
        "Depende del tamaño del sofá, la tela y cuánto trabajo de espuma o resortes necesite. Envía una foto por texto o WhatsApp y te mandamos una cotización gratis en 24 horas."),
       ("¿Cuánto tarda tapizar un sofá?",
        "Depende del sofá y de la disponibilidad de la tela; te damos una fecha con la cotización. Un cliente reciente tuvo su sofá listo dos semanas después de nuestra primera visita."),
       ("¿Pueden retapizar un seccional?",
        "Sí. Medimos y cotizamos cada sección, incluso las piezas modulares."),
       ("¿Cambian la espuma?",
        "Sí. La espuma nueva es lo que recupera un sofá cansado, y la incluimos en la cotización cuando hace falta."),
       ("¿Recogen el sofá?",
        "Sí. La recogida es gratis en todo Miami-Dade y te entregamos el sofá terminado."),
       (_SP, _SP_A)],
)

ES["upholstery/chair-reupholstery-miami"] = dict(
  path="es/tapiceria/tapizar-sillas-miami", service="Retapizado de sillas",
  parent=("Tapicería", "/upholstery/"), crumb="Tapizar Sillas",
  title="Tapizar Sillas de Comedor en Miami | Tapizado de Sillas | MIAN",
  desc="Tapizado de sillas en Miami: sillas de comedor, butacas, sillones de orejas y piezas vintage, una sola o el juego completo. Recogida gratis y cotización en 24 horas.",
  eyebrow="Tapicería · Sillas",
  h1="Tapizar Sillas de Comedor en Miami",
  lede="Sillas de comedor, butacas, sillones de orejas y piezas vintage, una sola o el juego completo, reconstruidas en nuestro taller de Miami. Recogida gratis y cotización gratis en 24 horas.",
  hero_alt="Butaca de bouclé con estructura de madera oscura retapizada en Miami",
  body="""
<h2>Sillas que tapizamos</h2>
<ul>
  <li><b>Sillas de comedor</b>: solo el asiento, o asiento y respaldo, una silla o el juego completo</li>
  <li><b>Butacas y sillas decorativas</b>, también en bouclé, terciopelo y lino</li>
  <li><b>Sillones de orejas y sillas capitoné</b>, con botones y capitoné reconstruidos</li>
  <li><b>Sillas vintage y mid-century</b>: la estructura se queda; el relleno y la tela son nuevos</li>
  <li><b>Sillas de oficina y escritorio</b> con asiento tapizado</li>
</ul>
<h2>Juegos de sillas de comedor</h2>
<p>Un juego tiene que quedar igual, así que cortamos todas las sillas de la misma tela y reconstruimos los asientos con la misma firmeza. Si solo quieres cambiar la tela, un asiento desmontable es el trabajo más simple. Las sillas con respaldo tapizado llevan más tiempo, y la cotización lo refleja. Envía una foto clara del frente y otra de atrás, y dinos cuántas sillas tienes.</p>
<h2>¿Cuánto cuesta tapizar una silla?</h2>
<p>Un asiento desmontable de comedor es el trabajo más simple. Una silla con respaldo tapizado o un sillón de orejas lleva más tela y más horas, y la cotización lo refleja. Envía una foto de la silla y dinos cuántas tienes: recibes una cotización gratis en 24 horas.</p>
<h2>Sillas vintage que vale la pena conservar</h2>
<p>Las sillas antiguas suelen tener mejores estructuras que las nuevas. Retiramos el relleno viejo, revisamos las uniones y reconstruimos el asiento con espuma nueva antes de poner la tela. Un cliente, después de que retapizáramos un cabecero Bernhardt, nos trajo dos sillas vintage.</p>
<p>¿Buscas algo más grande? Mira cómo <a href="/es/tapiceria/tapizar-sofa-miami/">tapizar sofás</a>. Para sillas de restaurante, mira la <a href="/es/comercial/tapiceria-restaurantes-miami/">tapicería para restaurantes</a>.</p>
""",
  steps=[("Envía fotos", "Frente y parte de atrás de una silla, y cuántas tienes."),
         ("Eliges la tela", "Llevamos muestras y te ayudamos a elegir según el uso."),
         ("Recogida gratis", "Recogemos las sillas y las reconstruimos en el taller."),
         ("Entrega", "Tus sillas regresan iguales y listas para usar.")],
  gallery_alt=["Sillas de comedor retapizadas en tela gris texturizada en Miami",
               "Butaca de bouclé retapizada en Miami",
               "Asiento capitoné en el taller de MIAN"],
  faq=[(_C+" tapizar una silla de comedor?",
        "Depende de si es solo el asiento o asiento y respaldo, y de la tela. Envía una foto y el número de sillas y te mandamos una cotización gratis en 24 horas."),
       ("¿Pueden tapizar solo los asientos?",
        "Sí. Es un trabajo común en sillas de comedor."),
       ("¿Aceptan una sola silla?",
        "Sí, una silla o el juego completo."),
       ("¿Restauran sillas vintage?",
        "Sí. Retiramos el relleno viejo y reconstruimos el asiento con espuma y tela nuevas sobre la estructura original."),
       (_SP, _SP_A)],
)

ES["upholstery/headboard-upholstery-miami"] = dict(
  path="es/tapiceria/cabeceros-tapizados-miami", service="Cabeceros tapizados",
  parent=("Tapicería", "/upholstery/"), crumb="Cabeceros Tapizados",
  title="Cabeceros Tapizados en Miami | A Medida y Retapizado | MIAN",
  desc="Cabeceros tapizados a medida y retapizado de cabeceros en Miami: capitoné, acanalados o lisos, a la medida de tu cama. Cotización gratis en 24 horas.",
  eyebrow="Tapicería · Cabeceros",
  h1="Cabeceros Tapizados en Miami",
  lede="Retapizamos el cabecero que ya tienes o hacemos uno nuevo a la medida de tu cama y tu pared, en nuestro taller de Miami. Capitoné, acanalado o liso. Cotización gratis en 24 horas.",
  hero_alt="Tapizado capitoné con botones en el taller de MIAN en Miami",
  body="""
<h2>Retapizarlo o hacer uno nuevo</h2>
<p>Si te gusta la forma de tu cabecero (o espaldar), podemos quitarle la tela y retapizarlo, incluso en una cama de diseñador. Retapizamos un cabecero Bernhardt que, en palabras del cliente, "was not an easy job". Si quieres algo que todavía no existe, construimos un cabecero a medida según el ancho de tu cama y la altura de tu pared.</p>
<h2>Estilos que hacemos</h2>
<ul>
  <li><b>Capitoné con botones</b>: clásico y formal</li>
  <li><b>Acanalado</b>: paneles verticales para un aspecto entallado y moderno</li>
  <li><b>Panel liso</b>: líneas limpias con vivos o tachuelas en el borde</li>
  <li><b>Paneles de pared</b> más anchos que la cama</li>
</ul>
<h2>Telas para la habitación</h2>
<p>El cabecero recibe el contacto del cabello y la piel, así que conviene una tela fácil de limpiar. Las mezclas de terciopelo de alto rendimiento y de lino funcionan muy bien, y podemos combinar la tela con tus <a href="/es/cortinas/cortinas-blackout-miami/">cortinas blackout</a> o las cortinas de la habitación. Llevamos muestras para que las veas en el espacio.</p>
<p>Mira todos nuestros <a href="/es/tapiceria/">servicios de tapicería</a>.</p>
""",
  steps=[("Envía una foto", "Tu cabecero, o la medida de la pared y la cama si es nuevo."),
         ("Diseño", "Definimos tamaño, estilo y tela con muestras en casa."),
         ("Taller", "Se construye o se retapiza en nuestro taller de Miami."),
         ("Entrega", "Tu cabecero llega listo para tu cama.")],
  gallery_alt=["Tapizado capitoné en el taller", "Detalle de tapizado en bouclé", "Tapizado en terciopelo de MIAN en Miami"],
  faq=[("¿Pueden retapizar un cabecero que ya tengo?",
        "Sí. Le quitamos la tela y lo retapizamos, incluso si es una pieza de diseñador."),
       ("¿Hacen cabeceros a medida?",
        "Sí. Lo construimos según el ancho de tu cama y la altura que quieras."),
       (_C+" un cabecero tapizado?",
        "Depende del tamaño, el estilo y la tela. Envía una foto o la medida de tu cama y te mandamos una cotización gratis en 24 horas."),
       ("¿La tela puede combinar con mis cortinas?",
        "Sí. Podemos usar la misma tela de tus cortinas o cojines."),
       (_SP, _SP_A)],
)

ES["drapery/blackout-curtains-miami"] = dict(
  path="es/cortinas/cortinas-blackout-miami", service="Cortinas blackout a medida",
  parent=("Cortinas", "/drapery/"), crumb="Cortinas Blackout",
  title="Cortinas Blackout en Miami | Hechas a Medida | MIAN",
  desc="Cortinas blackout a medida en Miami, cosidas e instaladas por nosotros, para habitaciones, cuartos de bebé y salas de cine. Cotización gratis en 24 horas.",
  eyebrow="Cortinas · Blackout",
  h1="Cortinas Blackout a Medida en Miami",
  lede="Cortinas blackout hechas a medida para habitaciones, cuartos de bebé y salas de cine, cosidas en nuestro taller de Miami e instaladas por nosotros. Cotización gratis en 24 horas.",
  hero_alt="Cortina plisada forrada en una ventana alta de un hogar de Miami",
  body="""
<h2>Por qué la medida importa en una cortina blackout</h2>
<p>El forro bloquea la luz, pero el ajuste decide qué tan oscuro queda el espacio. La luz entra por los lados, por arriba y por el piso. Un paño ya hecho deja esas rendijas. Medimos cada ventana y hacemos la cortina para que sobrepase el marco, que es lo que deja una habitación de Miami realmente oscura a las 7 de la mañana.</p>
<h2>Dónde funcionan mejor</h2>
<ul>
  <li><b>Habitaciones</b>, sobre todo las que dan al este y las de edificios altos</li>
  <li><b>Cuartos de bebé</b>: las siestas de día necesitan oscuridad</li>
  <li><b>Salas de cine</b>: sin reflejos en la pantalla</li>
  <li><b>Habitaciones de quienes trabajan de noche</b> y duermen de día</li>
</ul>
<h2>Blackout sin un aspecto pesado</h2>
<p>El forro blackout va detrás de la tela que elijas, así que el espacio conserva su estilo. Funciona con cabezales <a href="/es/cortinas/cortinas-euro-pleat-miami/">euro pleat</a> y <a href="/es/cortinas/cortinas-pinch-pleat-miami/">pinch pleat</a>. Para controlar la luz todo el día, podemos sumar un visillo en un segundo riel: de día tienes luz y privacidad, y de noche cierras el blackout.</p>
<p>El forro también ayuda a que la tela dure, porque la protege del sol de Miami. Mira todos los estilos en <a href="/es/cortinas/">cortinas a medida en Miami</a>.</p>
""",
  steps=[("Envía una foto", "Fotos de las ventanas. Cotización gratis en 24 horas."),
         ("Medimos", "Medimos cada abertura y llevamos muestras de tela."),
         ("Hecha a medida", "Tus cortinas se cosen con forro blackout en nuestro taller."),
         ("Instalada", "Las colgamos y revisamos que no entre luz.")],
  gallery_alt=["Cortina plisada en una ventana alta en Miami", "Cortina a medida en una ventana en arco", "Cortinas a medida en un hogar de Miami"],
  faq=[("¿Las cortinas blackout dejan el espacio totalmente oscuro?",
        "El forro bloquea la luz que le llega. Qué tan oscuro queda depende del ajuste alrededor de la ventana, por eso medimos cada abertura y hacemos la cortina para que sobrepase el marco."),
       ("¿Puedo elegir mi tela y agregar blackout?",
        "Sí. El forro blackout va detrás de la tela que elijas."),
       ("¿Se puede combinar blackout con visillos?",
        "Sí, en dos rieles: el visillo de día y la cortina blackout de noche."),
       (_C+"n las cortinas blackout a medida en Miami?",
        "Depende del tamaño de la ventana, la tela y el cabezal. Envía fotos y te mandamos una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

ES["drapery/outdoor-curtains-miami"] = dict(
  path="es/cortinas/cortinas-exteriores-miami", service="Cortinas para exterior a medida",
  parent=("Cortinas", "/drapery/"), crumb="Cortinas para Exterior",
  title="Cortinas para Exterior en Miami | Patios y Terrazas | MIAN",
  desc="Cortinas para exterior a medida en Miami para patios cubiertos, terrazas y cabañas, en telas para exterior. Cotización gratis en 24 horas. (786) 348-8650.",
  eyebrow="Cortinas · Exterior",
  h1="Cortinas para Exterior en Miami",
  lede="Cortinas a medida para patios cubiertos, terrazas y cabañas, en telas para exterior que aguantan el sol y la humedad de Miami. Cotización gratis en 24 horas.",
  hero_alt="Cortinas de exterior y cojines a medida en un patio cubierto de Miami",
  body="""
<h2>Cortinas de exterior para el clima de Miami</h2>
<p>Las telas normales de cortina se decoloran y retienen humedad al aire libre. Cosemos las cortinas de exterior en textiles elegidos para el sol y la humedad, para que un patio cubierto tenga sombra y privacidad todo el año.</p>
<h2>Qué le aportan a un patio</h2>
<ul>
  <li><b>Sombra</b>: bloquean el sol bajo de la tarde en la zona de asientos</li>
  <li><b>Privacidad</b>: separan la terraza de los vecinos o de la calle</li>
  <li><b>Definición</b>: enmarcan un arco o una galería como una sala al aire libre, con alzapaños cuando están abiertas</li>
</ul>
<h2>Medidas para tu abertura</h2>
<p>Los patios casi nunca tienen medidas estándar. Medimos cada abertura, incluida la altura del riel al piso y la inclinación del suelo. Los alzapaños mantienen los paños ordenados los días de viento. El patio de nuestras fotos tiene paños hasta el piso que enmarcan el arco, con alzapaños en el mismo estampado de los cojines.</p>
<h2>Combina los cojines</h2>
<p>También hacemos los asientos: cojines y almohadones de exterior en una tela que combina, cosidos en el mismo taller. Para embarcaciones y marinas, mira la <a href="/es/comercial/tapiceria-nautica-miami/">tapicería náutica</a>. Para interiores, mira <a href="/es/cortinas/">cortinas a medida en Miami</a>.</p>
""",
  steps=[("Envía una foto", "Fotos del patio o la terraza. Cotización gratis en 24 horas."),
         ("Medimos", "Medimos cada abertura y llevamos muestras de telas para exterior."),
         ("Hecha a medida", "Tus paños se cosen en nuestro taller de Miami."),
         ("Instalada", "Colgamos las cortinas y ajustamos los alzapaños.")],
  gallery_alt=["Cortinas de exterior en un patio cubierto de Miami", "Cojines de exterior en tela a rayas azul marino", "Cortina a medida en Miami"],
  faq=[("¿Qué tela usan para cortinas de exterior?",
        "Textiles para exterior elegidos para el sol y la humedad. Llevamos muestras para que los veas en tu espacio."),
       ("¿Hacen cortinas para patios cubiertos?",
        "Sí, para patios cubiertos, terrazas y cabañas."),
       ("¿Pueden hacer cojines que combinen?",
        "Sí. Cosemos cojines y almohadones de exterior en una tela que combina."),
       (_C+"n las cortinas para exterior?",
        "Depende del tamaño de las aberturas y de la tela. Envía fotos y te mandamos una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

ES["commercial/restaurant-upholstery-miami"] = dict(
  path="es/comercial/tapiceria-restaurantes-miami", service="Tapicería para restaurantes",
  parent=("Comercial", "/commercial/"), crumb="Tapicería para Restaurantes",
  title="Tapicería para Restaurantes en Miami | Booths | MIAN",
  desc="Tapicería para restaurantes en Miami: booths, banquetas y sillas en telas de grado contract con espuma resistente, hechos en nuestro taller. Cotización gratis en 24 horas.",
  eyebrow="Comercial · Restaurantes",
  h1="Tapicería para Restaurantes en Miami",
  lede="Booths, banquetas y sillas de comedor reconstruidos con telas de grado contract y espuma resistente, en nuestro taller de Miami. Cotización gratis en 24 horas.",
  hero_alt="Banqueta de restaurante y sillas de cuero tapizadas para un local de Miami",
  body="""
<h2>Qué tapizamos para restaurantes</h2>
<ul>
  <li><b>Booths y banquetas</b>: asientos de pared, de uno o dos lados</li>
  <li><b>Sillas de comedor</b>: juegos iguales, solo asientos o sillas completas</li>
  <li><b>Taburetes de bar</b> y asientos de barra</li>
  <li><b>Zonas de lounge y de espera</b></li>
</ul>
<h2>Hecho para el servicio, no para una vitrina</h2>
<p>Los asientos de un restaurante reciben derrames, productos de limpieza y cientos de comensales. Usamos telas de grado contract y espuma resistente para que el asiento mantenga la forma y se limpie fácil. Las roturas y costuras abiertas se ven peor de lo que son: por lo general un booth se puede reconstruir sobre su estructura sin reemplazarlo.</p>
<h2>Planificado según tu servicio</h2>
<p>Dinos tu horario y tus días más flojos, y planificamos la recogida y la entrega según ellos. Recibes una cotización por escrito y una fecha antes de empezar.</p>
<h2>Cómo pedir una cotización</h2>
<p>Envía fotos de los asientos, un conteo o largo aproximado de los booths y tus tiempos. Vamos a medir y te ayudamos a elegir la tela. Hoteles, oficinas y embarcaciones están en nuestra página de <a href="/es/comercial/">tapicería comercial</a>, y también hacemos <a href="/es/cortinas/">cortinas para comedores</a>.</p>
""",
  steps=[("Envía fotos", "Fotos de los asientos y un conteo aproximado. Cotización gratis en 24 horas."),
         ("Visita al local", "Medimos en el sitio y llevamos telas de grado contract."),
         ("Taller", "Los asientos se reconstruyen en nuestro taller de Miami."),
         ("Entrega", "Las piezas regresan en la fecha acordada, listas para el servicio.")],
  gallery_alt=["Banqueta de restaurante en cuero marrón en Miami", "Juego de sillas de comedor tapizadas", "Asiento capitoné en el taller de MIAN"],
  faq=[("¿Retapizan booths de restaurante?",
        "Sí, booths y banquetas, por lo general sobre su estructura actual."),
       ("¿Qué tela recomiendan para restaurantes?",
        "Telas de grado contract fáciles de limpiar, con espuma resistente."),
       ("¿Pueden trabajar según nuestro horario?",
        "Sí. Dinos tu horario y planificamos la recogida y la entrega según él."),
       ("¿Cómo pido una cotización?",
        "Envía fotos y un conteo aproximado por texto, WhatsApp o el formulario. Recibes una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

ES["commercial/marine-upholstery-miami"] = dict(
  path="es/comercial/tapiceria-nautica-miami", service="Tapicería náutica",
  parent=("Comercial", "/commercial/"), crumb="Tapicería Náutica",
  title="Tapicería Náutica en Miami | Cojines para Yates | MIAN",
  desc="Tapicería náutica en Miami: cojines y asientos para yates y embarcaciones en telas para exterior, cosidos en nuestro taller. Cotización gratis en 24 horas.",
  eyebrow="Comercial · Náutica",
  h1="Tapicería Náutica en Miami",
  lede="Cojines y asientos a medida para yates y embarcaciones en telas para exterior, cosidos en nuestro taller de Miami. Cotización gratis en 24 horas.",
  hero_alt="Cojines a rayas azul marino hechos para un yate en una marina de Miami",
  body="""
<h2>Qué hacemos para embarcaciones</h2>
<ul>
  <li><b>Cojines de cubierta y cockpit</b>: asientos, respaldos y colchonetas de sol</li>
  <li><b>Asientos de flybridge</b></li>
  <li><b>Asientos de salón</b> y colchonetas de camarote</li>
  <li><b>Almohadones y bolsters</b> en una tela que combina</li>
</ul>
<h2>Hecho para el sol y la brisa salada</h2>
<p>Los cojines de un barco viven con sol, salitre y humedad, así que trabajamos con textiles para exterior y cortamos cada cojín según la forma del asiento. El juego a rayas azul marino y blanco de nuestras fotos se hizo para un yate en Miami.</p>
<h2>Reemplazar lo que ya tienes</h2>
<p>La forma más simple de empezar es con tus cojines actuales: los usamos como patrón para que el juego nuevo calce en las mismas bases. Si quieres un aspecto nuevo, te ayudamos a elegir la tela y los vivos.</p>
<h2>Cómo pedir una cotización</h2>
<p>Envía fotos de los asientos y dinos dónde está atracada la embarcación. También hacemos <a href="/es/cortinas/cortinas-exteriores-miami/">cortinas para exterior</a> para terrazas frente al agua. Mira toda nuestra <a href="/es/comercial/">tapicería comercial</a>.</p>
""",
  steps=[("Envía fotos", "Fotos de los asientos y dónde está el barco. Cotización gratis en 24 horas."),
         ("Medimos", "Sacamos patrones de tus cojines y llevamos muestras de tela."),
         ("Taller", "Tus cojines se cortan y se cosen en nuestro taller de Miami."),
         ("Entrega", "El juego nuevo llega listo para colocar.")],
  gallery_alt=["Cojines a rayas azul marino para un yate en una marina de Miami", "Cojines y cortinas de exterior en Miami", "Trabajo de tapicería en el taller de MIAN"],
  faq=[("¿Hacen cojines para yates y embarcaciones?",
        "Sí: de cubierta, cockpit, flybridge e interior."),
       ("¿Qué tela usan en embarcaciones?",
        "Textiles para exterior elegidos para el sol y la humedad. Llevamos muestras."),
       ("¿Pueden copiar mis cojines actuales?",
        "Sí. Los usamos como patrón para que el juego nuevo calce."),
       (_C+" la tapicería náutica?",
        "Depende del número de cojines, su forma y la tela. Envía fotos y te mandamos una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

ES["upholstery/leather-reupholstery-miami"] = dict(
  path="es/tapiceria/tapiceria-cuero-miami", service="Tapicería y retapizado en cuero",
  parent=("Tapicería", "/upholstery/"), crumb="Tapicería en Cuero",
  title="Tapicería en Cuero en Miami | Sofás y Sillas | MIAN",
  desc="Tapicería en cuero en Miami: retapizamos sofás y sillas de cuero en nuestro taller. Recogida gratis y cotización gratis en 24 horas. Atendemos en español.",
  eyebrow="Tapicería · Cuero",
  h1="Tapicería en Cuero en Miami",
  lede="¿Cuero agrietado, pelado o gastado sobre una estructura que sigue buena? Retapizamos sofás, sillas y booths de cuero en nuestro taller de Miami. Recogida gratis y cotización gratis en 24 horas.",
  hero_alt="Banqueta de restaurante y sillas de cuero tapizadas para un local de Miami",
  body="""
<h2>Retapizar un sofá o una silla de cuero</h2>
<p>El cuero se desgasta distinto a la tela. Los cojines del asiento y los brazos se agrietan y se pelan primero, mientras la estructura casi siempre sigue sólida. Por eso un sofá de cuero gastado suele ser un buen candidato para retapizar: la estructura se queda, y el forro y la espuma son nuevos.</p>
<h2>En qué trabajamos</h2>
<ul>
  <li><b>Sofás de cuero</b>, incluidos cojines de asiento que perdieron la forma</li>
  <li><b>Sillas de cuero</b>: de comedor, butacas y sillas de escritorio</li>
  <li><b>Booths y banquetas</b> para <a href="/es/comercial/tapiceria-restaurantes-miami/">restaurantes</a></li>
</ul>
<h2>¿Reparar o retapizar?</h2>
<p>A veces solo una sección está gastada. Otras veces toda la pieza necesita forro nuevo para que combine. Envía una foto del daño y de la pieza completa, y te decimos qué conviene antes de que gastes algo.</p>
<h2>Cuero o material tipo cuero</h2>
<p>Te ayudamos a elegir según el uso de la pieza. Un material tipo cuero puede ser una opción práctica para uso intenso, y llevamos muestras para que las compares en tu espacio. Mira todos nuestros <a href="/es/tapiceria/">servicios de tapicería</a> o lee cómo <a href="/es/tapiceria/tapizar-sofa-miami/">tapizar sofás</a>.</p>
""",
  steps=[("Envía una foto", "El daño y la pieza completa. Recibes tu cotización gratis en 24 horas."),
         ("Eliges el material", "Llevamos muestras y te ayudamos a elegir según el uso."),
         ("Recogida gratis", "Recogemos la pieza y la reconstruimos en nuestro taller de Miami."),
         ("Entrega", "Tu pieza regresa terminada y lista para usar.")],
  gallery_alt=["Banqueta de restaurante en cuero marrón en Miami", "Sillas de comedor tapizadas en Miami", "Settee capitoné en el taller de MIAN"],
  faq=[("¿Pueden retapizar un sofá de cuero?",
        "Sí. Si la estructura está sólida, cambiamos el forro y la espuma que necesite. Envía una foto y te confirmamos."),
       ("¿Reparan sillas de cuero?",
        "Envía una foto del daño. Te decimos si se puede rehacer la sección gastada o si conviene retapizar toda la silla."),
       (_C+" la tapicería en cuero?",
        "Depende del tamaño de la pieza, el material y el trabajo de espuma. Envía una foto y recibes una cotización gratis en 24 horas."),
       ("¿Recogen la pieza?", "Sí. La recogida es gratis en todo Miami-Dade."),
       (_SP, _SP_A)],
)

ES["upholstery/custom-cushions-miami"] = dict(
  path="es/tapiceria/cojines-a-medida-miami", service="Cojines a medida",
  parent=("Tapicería", "/upholstery/"), crumb="Cojines a Medida",
  title="Cojines a Medida en Miami | Patio y Exterior | MIAN",
  desc="Cojines a medida en Miami: cojines de reemplazo para patio, exterior y tumbonas de piscina, cosidos en nuestro taller. Cotización gratis en 24 horas.",
  eyebrow="Tapicería · Cojines",
  h1="Cojines a Medida y de Reemplazo en Miami",
  lede="Cojines de reemplazo para muebles de patio, sofás de exterior, tumbonas y asientos de interior, cortados a la medida de tu estructura y cosidos en nuestro taller de Miami. Cotización gratis en 24 horas.",
  hero_alt="Cojines de exterior a rayas azul marino cosidos por MIAN en Miami",
  body="""
<h2>Cojines hechos para tus muebles</h2>
<p>Los muebles de patio suelen durar más que sus cojines, y los de repuesto ya hechos casi nunca calzan. Usamos tu cojín viejo o tu estructura como patrón para que el nuevo quede bien en el mismo asiento.</p>
<h2>Qué hacemos</h2>
<ul>
  <li><b>Cojines para sofás y sillas de patio</b></li>
  <li><b>Cojines para tumbonas de piscina</b></li>
  <li><b>Cojines de asiento y de banco</b> para interior</li>
  <li><b>Fundas de cojín</b> cuando la espuma sigue buena</li>
  <li><b>Almohadones</b> en una tela que combina</li>
</ul>
<h2>Tela de exterior para el clima de Miami</h2>
<p>El sol y la humedad castigan los cojines aquí. Cosemos los cojines de exterior en textiles para exterior y llevamos muestras para que los veas en tu patio. Si la espuma quedó aplastada, también la cambiamos.</p>
<h2>Cambiar la funda o todo el cojín</h2>
<p>Si la espuma aún mantiene la forma, puede que solo necesites una funda nueva. Envía una foto y las medidas y te decimos. Las embarcaciones tienen su propia página: <a href="/es/comercial/tapiceria-nautica-miami/">tapicería náutica</a>. Para combinar el patio, mira las <a href="/es/cortinas/cortinas-exteriores-miami/">cortinas para exterior</a>.</p>
""",
  steps=[("Envía una foto", "Los cojines y sus medidas. Cotización gratis en 24 horas."),
         ("Eliges la tela", "Llevamos muestras de telas de exterior e interior."),
         ("Taller", "Tus cojines se cortan y se cosen en nuestro taller de Miami."),
         ("Entrega", "El juego nuevo regresa listo para usar.")],
  gallery_alt=["Cojines a medida a rayas azul marino en Miami", "Cojines y cortinas a medida en un patio cubierto de Miami", "Sala en Miami con sofá retapizado y cojines"],
  faq=[("¿Hacen cojines de reemplazo para muebles de patio?",
        "Sí. Usamos tu cojín viejo o tu estructura como patrón para que el nuevo calce."),
       ("¿Hacen cojines en tela de exterior?",
        "Sí, en textiles para exterior. Llevamos muestras a tu casa."),
       ("¿Pueden cambiar solo las fundas?",
        "Sí, si la espuma aún mantiene la forma. Envía una foto y te decimos."),
       (_C+"n los cojines a medida?",
        "Depende del número de cojines, su tamaño y la tela. Envía una foto y las medidas y recibes una cotización gratis en 24 horas."),
       (_SP, _SP_A)],
)

AREA_ES = {
  "coral-gables": ("Las casas de Coral Gables están llenas de muebles que vale la pena conservar: piezas familiares, antigüedades y sofás bien hechos que solo necesitan tela nueva. Retapizar te deja conservar la estructura y la historia mientras actualizas el aspecto para tu espacio.",
    "Lo más pedido aquí: retapizar antigüedades y sillas heredadas, juegos de comedor y cortinas forradas para ventanales de sala."),
  "doral": ("Doral combina casas familiares y oficinas. En casa, eso suele significar sofás y sillas de comedor con telas que aguanten niños y mascotas; en los negocios, asientos resistentes para oficinas y restaurantes.",
    "Lo más pedido aquí: sofás y sillas con telas de alto rendimiento, asientos para oficinas y restaurantes, y cortinas blackout para habitaciones."),
  "brickell": ("Los condominios de Brickell tienen ventanales de piso a techo y un sol fuerte por la tarde. Los visillos y las cortinas forradas a medida suavizan el resplandor y protegen los muebles, mientras los seccionales y sofás modulares recuperan su vida con espuma y tela nuevas.",
    "Lo más pedido aquí: visillos y cortinas blackout para ventanas de edificios altos, retapizado de seccionales y cojines a medida para balcones. Avísanos las reglas de entrega de tu edificio y planificamos según ellas."),
  "miami-beach": ("El salitre, el sol y la humedad castigan las telas en Miami Beach. Los textiles para exterior y de alto rendimiento duran mucho más en terrazas, balcones y embarcaciones, y las cortinas forradas evitan que se decoloren los espacios con mucho sol.",
    "Lo más pedido aquí: cojines de exterior y náuticos, cortinas para terrazas y asientos para hoteles y restaurantes."),
  "kendall": ("En las casas familiares de Kendall, cada sofá y silla de comedor se usa a diario. Retapizar con una tela de alto rendimiento devuelve asientos cómodos y fáciles de limpiar sin cambiar muebles que ya te gustan.",
    "Lo más pedido aquí: sofás y seccionales de sala familiar, juegos completos de sillas de comedor y cortinas a medida para habitaciones y salas."),
  "hialeah": ("Los hogares de Hialeah conservan sus muebles por años, y un buen sofá o juego de comedor casi siempre vale la pena reconstruirlo. Nuestro tapicero recoge gratis en Hialeah, reconstruye la pieza en el taller de Miami y te la devuelve terminada.",
    "Lo más pedido aquí: tapicería de muebles para sofás y sillas de comedor, retapizado en cuero y cojines de patio de reemplazo."),
  "north-miami": ("North Miami está cerca de nuestro taller en 1 NW 62nd St, lo que facilita mucho la recogida y la entrega. Las piezas vintage y mid-century son comunes aquí y muchas veces vale más retapizarlas que reemplazarlas.",
    "Lo más pedido aquí: retapizado de sillas vintage y mid-century, sofás y cortinas a medida."),
}

def area_es(slug, name):
    p1, p2 = AREA_ES[slug]
    return dict(
      path=f"es/zonas/{slug}", service="Tapicería y cortinas a medida", crumb=name,
      title=f"Tapicería en {name}, FL | Tapicero de Muebles | MIAN",
      desc=f"Tapicería, retapizado de muebles y cortinas a medida en {name}, FL. Recogida gratis y cotización gratis en 24 horas. Atención en español. (786) 348-8650.",
      eyebrow=f"Servimos {name}",
      h1=f"Tapicería de Muebles en {name}",
      lede=f"Retapizado, tapicería a medida y cortinas para hogares y negocios en {name}. Recogida gratis y cotización gratis en 24 horas.",
      hero_alt=f"Mueble tapizado por MIAN House &amp; Decor para un cliente en {name}",
      body=f"""
<h2>Tapicería y cortinas en {name}</h2>
<p>{p1}</p>
<p>{p2}</p>
<h3>Servicios en {name}</h3>
<ul>
  <li><a href="/es/tapiceria/"><b>Tapicería y retapizado de muebles</b></a>: sofás, seccionales, sillas de comedor, cabeceros y antigüedades</li>
  <li><a href="/es/cortinas/"><b>Cortinas a medida</b></a>: cortinas plisadas, visillos, blackout y de exterior</li>
  <li><a href="/es/comercial/"><b>Tapicería comercial</b></a>: restaurantes, hoteles, oficinas y embarcaciones</li>
</ul>
<p>Todo se hace en nuestro taller en 1 NW 62nd St, Miami. La recogida es gratis y recibes una cotización por escrito en 24 horas después de enviarnos una foto.</p>
""",
      faq=[(f"¿Recogen muebles en {name}?", f"Sí. La recogida es gratis en {name} y en todo Miami-Dade."),
           ("¿Cómo pido una cotización?", "Envía una foto de la pieza por texto, WhatsApp o el formulario. Recibes una cotización gratis en 24 horas."),
           (_SP, _SP_A)],
    )

# Exact-string swaps applied to shared chrome, the home page and the thank-you page.
# Longest strings are applied first. Anything left in English is a bug: see the audit in the build.
PAIRS = [
  ('<html lang="en">', '<html lang="es">'),
  ('en_US', 'es_US'),
  ('Skip to content', 'Saltar al contenido'),
  ('aria-label="MIAN House &amp; Decor — home"', 'aria-label="MIAN House &amp; Decor, inicio"'),
  ('>Home<', '>Inicio<'), ('>Services<', '>Servicios<'), ('>About us<', '>Nosotros<'), ('>Contact<', '>Contacto<'),
  ('>Free Quote<', '>Cotización gratis<'), ('Free Quote', 'Cotización gratis'),
  ('Miami · Residential &amp; Commercial', 'Miami · Residencial y comercial'),
  ('Custom Upholstery &amp; Reupholstery in Miami', 'Tapicería y Tapizado de Muebles en Miami'),
  ('From reupholstery to custom furniture, curtains and cushions — we deliver fast, precise solutions shaped around your needs. <strong>Hablamos español.</strong>',
   'Del retapizado a los muebles a medida, cortinas y cojines: soluciones rápidas y precisas, hechas según lo que necesitas. <strong>Atendemos en español.</strong>'),
  ('Text us — fastest reply', 'Escríbenos: respuesta rápida'),
  ('Text us', 'Escríbenos'),
  (' · 12 Google reviews', ' · 12 reseñas en Google'),
  ('<b>10+ years</b> in Miami-Dade', '<b>Más de 10 años</b> en Miami-Dade'),
  ('<b>Free quote</b> in 24h', '<b>Cotización gratis</b> en 24 h'),
  ('<b>Free pickup</b> in Miami-Dade', '<b>Recogida gratis</b> en Miami-Dade'),
  ('Upholstery &amp; Drapery <span class="hl">Services</span> in Miami', 'Tapicería y <span class="hl">cortinas</span> en Miami'),
  ('We work with curtains, cushions, custom furniture and upholstery — shaping pieces and spaces through attentive listening and precise execution.',
   'Trabajamos con cortinas, cojines, muebles a medida y tapicería, y damos forma a piezas y espacios escuchando con atención y ejecutando con precisión.'),
  ('<h3>Curtains</h3>', '<h3>Cortinas</h3>'),
  ('Made-to-measure drapery, sheers and blackouts — measured and installed by us.', 'Cortinas a medida, visillos y blackout, medidos e instalados por nosotros.'),
  ('<h3>Upholstery Fabrics</h3>', '<h3>Telas de tapicería</h3>'),
  ('Performance, outdoor, linen and contract-grade textiles — advised, not guessed.', 'Telas de alto rendimiento, de exterior, lino y grado contract, con asesoría y sin adivinar.'),
  ('<h3>Custom Furniture</h3>', '<h3>Muebles a medida</h3>'),
  ('Custom pieces built to your dimensions, from a single chair to a full room.', 'Piezas hechas a tus medidas, desde una silla hasta un espacio completo.'),
  ('<h3>Reupholstery</h3>', '<h3>Retapizado</h3>'),
  ('New fabric and new foam on the frame you already love — brought back to life.', 'Tela y espuma nuevas sobre la estructura que ya te gusta: de vuelta a la vida.'),
  ('Our specialties', 'Nuestras especialidades'),
  ('Recent Upholstery <span class="hl">Work</span> in Miami', 'Trabajos recientes de <span class="hl">tapicería</span> en Miami'),
  ('Recent <span class="hl">work</span>', 'Trabajos <span class="hl">recientes</span>'),
  ('<figcaption>Curtains</figcaption>', '<figcaption>Cortinas</figcaption>'),
  ('<figcaption>Furniture</figcaption>', '<figcaption>Muebles</figcaption>'),
  ('<figcaption>Commercial</figcaption>', '<figcaption>Comercial</figcaption>'),
  ('alt="Made-to-measure ivory drapery on a tall arched window in Miami"', 'alt="Cortina marfil a medida en una ventana alta en arco en Miami"'),
  ('alt="Custom grey sectional and ottoman in an oceanfront Miami living room"', 'alt="Seccional gris con otomana en una sala frente al mar en Miami"'),
  ('alt="Restaurant banquette and leather chairs upholstered for a Miami venue"', 'alt="Banqueta de restaurante y sillas de cuero tapizadas en Miami"'),
  ('alt="Miami living room with a reupholstered sofa and cushions by MIAN House &amp; Decor"', 'alt="Sala en Miami con sofá retapizado y cojines de MIAN House &amp; Decor"'),
  ('alt="Mercedes Ruiz cutting fabric in the MIAN workshop in Miami"', 'alt="Mercedes Ruiz cortando tela en el taller de MIAN en Miami"'),
  ('What Miami <span class="hl">says</span>', 'Lo que dice <span class="hl">Miami</span>'),
  ('4.7 out of 5 from 12 reviews on Google.', '4.7 de 5 en 12 reseñas de Google. Las reseñas se muestran en su idioma original.'),
  ('aria-label="5 out of 5 stars"', 'aria-label="5 de 5 estrellas"'),
  ('Google review · a month ago', 'Reseña de Google'), ('Google review · 4 months ago', 'Reseña de Google'), ('Google review · 8 months ago', 'Reseña de Google'),
  ('Google review', 'Reseña de Google'),
  ('Read all reviews on Google', 'Leer todas las reseñas en Google'),
  ('<span>our</span>', '<span>nuestra</span>'),
  ('<h3>MISSION</h3>', '<h3>MISIÓN</h3>'), ('<h3>VISION</h3>', '<h3>VISIÓN</h3>'), ('<h3>PURPOSE</h3>', '<h3>PROPÓSITO</h3>'),
  ('MIAN focuses on understanding, advising and executing <b>quickly</b>. We <b>customize</b> precisely, turning complex requirements into clear, tailored <b>results</b>, paying close <b>attention to detail</b>.',
   'MIAN se enfoca en entender, asesorar y ejecutar <b>con rapidez</b>. <b>Personalizamos</b> con precisión y convertimos requerimientos complejos en <b>resultados</b> claros y a la medida, con mucha <b>atención al detalle</b>.'),
  ("MIAN will become a leading solution for <b>high-end projects</b>; offering <b>express services</b> and tailoring our work to our client's needs through a deep <b>understanding</b> of their lifestyle and business.",
   'MIAN será una solución líder para <b>proyectos de alto nivel</b>, con <b>servicios exprés</b> y un trabajo adaptado a cada cliente gracias a un profundo <b>entendimiento</b> de su estilo de vida y su negocio.'),
  ('MIAN turns every request into a <b>lasting solution</b>. Custom designs, products and spaces <b>crafted around your needs</b>.',
   'MIAN convierte cada solicitud en una <b>solución duradera</b>. Diseños, productos y espacios a medida, <b>creados según tus necesidades</b>.'),
  ('Our <span class="hl">Values</span>', 'Nuestros <span class="hl">valores</span>'),
  ('<h4>Client Insight</h4>', '<h4>Conocer al cliente</h4>'),
  ("We start by listening. We take time to understand each client's needs, lifestyle and context before giving any suggestion.",
   'Empezamos escuchando. Nos tomamos el tiempo de entender las necesidades, el estilo de vida y el contexto de cada cliente antes de sugerir algo.'),
  ('<h4>Agility</h4>', '<h4>Agilidad</h4>'),
  ('We respond quickly, adjust with ease and keep projects flowing, always standing behind the quality of the work we deliver.',
   'Respondemos rápido, nos ajustamos con facilidad y mantenemos los proyectos en marcha, siempre respaldando la calidad de lo que entregamos.'),
  ('<h4>Craftsmanship</h4>', '<h4>Oficio</h4>'),
  ('We care about how things are made. From upholstery to finishing, we ensure precise execution and long-lasting quality.',
   'Nos importa cómo se hacen las cosas. De la tapicería a los acabados, aseguramos una ejecución precisa y una calidad duradera.'),
  ('<h4>Efficiency</h4>', '<h4>Eficiencia</h4>'),
  ('We look for intelligent ways to achieve impact: clear processes, organized workflows and minimal friction for the client.',
   'Buscamos formas inteligentes de lograr impacto: procesos claros, flujos organizados y el mínimo de fricción para el cliente.'),
  ('<p class="eyebrow">About us</p>', '<p class="eyebrow">Nosotros</p>'),
  ('Who are <em>we?</em>', '¿Quiénes <em>somos?</em>'),
  ('We work with curtains, cushions, custom furniture and upholstery — shaping pieces and spaces through attentive listening, precise execution and fast, reliable service.',
   'Trabajamos con cortinas, cojines, muebles a medida y tapicería, y damos forma a piezas y espacios escuchando con atención, ejecutando con precisión y con un servicio rápido y confiable.'),
  ('From reupholstery to fully crafted furniture, we approach every project with care, transforming complex requests into clear, tailored results that feel right, last over time and truly support the way our clients live and work.',
   'Del retapizado a los muebles hechos por completo, abordamos cada proyecto con cuidado y convertimos solicitudes complejas en resultados claros y a la medida, que se sienten bien, duran en el tiempo y acompañan de verdad la forma en que nuestros clientes viven y trabajan.'),
  ('<span>Creative Director</span>', '<span>Directora creativa</span>'),
  ('Serving Miami-Dade:', 'Servimos Miami-Dade:'), (' &amp; more.', ' y más.'),
  ('<small>Workshop · by appointment</small>', '<small>Taller · con cita previa</small>'),
  ('<small>Call or WhatsApp</small>', '<small>Llamada o WhatsApp</small>'),
  ('<small>Email</small>', '<small>Correo</small>'),
  ('<small>Hours</small>', '<small>Horario</small>'),
  ('Mon–Fri 8 AM–8 PM · Sat 10 AM–3 PM', 'Lun–vie 8 AM–8 PM · Sáb 10 AM–3 PM'),
  ('Mon–Fri 8 AM–8 PM<br>Sat 10 AM–3 PM · Sun closed', 'Lun–vie 8 AM–8 PM<br>Sáb 10 AM–3 PM · Dom cerrado'),
  ('Do you need an <em>Express Service?</em>', '¿Necesitas un <em>servicio exprés?</em>'),
  ("Let us know how we can help you make this happen. Send a photo on WhatsApp and we'll usually price it the same day.",
   'Cuéntanos cómo podemos ayudarte a lograrlo. Envía una foto por WhatsApp y normalmente te damos el precio el mismo día.'),
  ('Message us on WhatsApp', 'Escríbenos por WhatsApp'),
  ('<p class="eyebrow">Contact</p>', '<p class="eyebrow">Contacto</p>'),
  ('Get your free quote in 24 hours.', 'Recibe tu cotización gratis en 24 horas.'),
  ('Tell us what you need reupholstered, built or measured. We reply within one business day.', 'Cuéntanos qué necesitas retapizar, construir o medir. Respondemos en un día hábil.'),
  ('Call (786) 348-8650', 'Llama al (786) 348-8650'),
  ('Request a quote', 'Pide una cotización'),
  ('Free · No obligation · Reply within 24 hours', 'Gratis · Sin compromiso · Respuesta en 24 horas'),
  ('<label for="f-name">Name</label>', '<label for="f-name">Nombre</label>'),
  ('<label for="f-phone">Phone</label>', '<label for="f-phone">Teléfono</label>'),
  ('<label for="f-email">Email</label>', '<label for="f-email">Correo</label>'),
  ('What do you need?', '¿Qué necesitas?'),
  ('<option>Curtains</option>', '<option>Cortinas</option>'), ('<option>Fabrics</option>', '<option>Telas</option>'),
  ('<option>Custom furniture</option>', '<option>Muebles a medida</option>'), ('<option>Reupholstery</option>', '<option>Retapizado</option>'),
  ('<option>Cushions</option>', '<option>Cojines</option>'), ('<option>Commercial project</option>', '<option>Proyecto comercial</option>'),
  ('<option>Something else</option>', '<option>Otra cosa</option>'),
  ('Comment or message', 'Comentario o mensaje'),
  ('placeholder="Your name"', 'placeholder="Tu nombre"'), ('placeholder="you@email.com"', 'placeholder="tu@correo.com"'),
  ('Tell us about the piece — type of furniture, fabric idea, measurements…', 'Cuéntanos de la pieza: tipo de mueble, idea de tela, medidas…'),
  ('Send my request', 'Enviar mi solicitud'),
  ('Goes straight to our inbox. We reply within 24 hours.', 'Llega directo a nuestro correo. Respondemos en 24 horas.'),
  ('Residential &amp; Commercial', 'Residencial y comercial'),
  ('Custom furniture, reupholstery, cushions and curtains for homes and businesses across Miami-Dade.', 'Muebles a medida, retapizado, cojines y cortinas para hogares y negocios en todo Miami-Dade.'),
  ('<h4>Services</h4>', '<h4>Servicios</h4>'),
  ('Upholstery &amp; Reupholstery', 'Tapicería y retapizado'), ('Custom Drapery &amp; Curtains', 'Cortinas a medida'),
  ('Custom Drapery', 'Cortinas a medida'), ('Commercial Upholstery', 'Tapicería comercial'),
  ('>Free quote<', '>Cotización gratis<'),
  ('From needs to solutions. · Hablamos español', 'From needs to solutions. · Atendemos en español'),
  ('>Call</a>', '>Llamar</a>'), ('Call</a>', 'Llamar</a>'),
  ('Quote\n  </a>', 'Cotizar\n  </a>'),
  ('aria-label="Quick contact"', 'aria-label="Contacto rápido"'),
  ('aria-label="Call us"', 'aria-label="Llámanos"'), ('aria-label="Email us"', 'aria-label="Escríbenos un correo"'),
  ('aria-label="Text us"', 'aria-label="Escríbenos"'), ('aria-label="Menu"', 'aria-label="Menú"'),
  ('Hi%20MIAN%20House%20%26%20Decor%2C%20I%27d%20like%20a%20free%20quote.', 'Hola%20MIAN%20House%20%26%20Decor%2C%20quisiera%20una%20cotizaci%C3%B3n%20gratis.'),
  ('Hi%20MIAN%20House%20%26%20Decor%2C%20I%20need%20an%20express%20service.', 'Hola%20MIAN%20House%20%26%20Decor%2C%20necesito%20un%20servicio%20expr%C3%A9s.'),
  ('Hi%20MIAN%20House%20%26%20Decor%2C%20I%20just%20sent%20a%20quote%20request.', 'Hola%20MIAN%20House%20%26%20Decor%2C%20acabo%20de%20pedir%20una%20cotizaci%C3%B3n.'),
  ("'Hi MIAN House & Decor, I would like a free quote.'", "'Hola MIAN House & Decor, quisiera una cotización gratis.'"),
  ("'Name: '", "'Nombre: '"), ("'Phone: '", "'Teléfono: '"), ("'Email: '", "'Correo: '"), ("'Service: '", "'Servicio: '"), ("'Details: '", "'Detalles: '"),
  ('Please add your name and phone so we can reply.', 'Agrega tu nombre y teléfono para poder responderte.'),
  ('Sending your request…', 'Enviando tu solicitud…'), ('Sending…', 'Enviando…'), ('Request sent ✓', 'Solicitud enviada ✓'),
  ('We could not send that. ', 'No pudimos enviarlo. '), ('Send it on WhatsApp', 'Envíalo por WhatsApp'), (' or call (786) 348-8650.', ' o llama al (786) 348-8650.'),
  ('/thanks.html?via=', '/es/gracias/?via='), ('https://mianhousedecor.com/thanks.html', 'https://mianhousedecor.com/es/gracias/'),
  # landing-page chrome
  ('How it <span class="hl">works</span>', 'Cómo <span class="hl">funciona</span>'),
  ('Frequently asked <span class="hl">questions</span>', 'Preguntas <span class="hl">frecuentes</span>'),
  ('More from MIAN', 'Más de MIAN'),
  ('Get your free quote <em>in 24 hours</em>', 'Recibe tu cotización gratis <em>en 24 horas</em>'),
  ('Send a photo of the piece or the windows — we reply within one business day. Se habla español.', 'Envía una foto de la pieza o de las ventanas: respondemos en un día hábil. Atendemos en español.'),
  ('>Quote form<', '>Formulario<'),
  ('aria-label="Breadcrumb"', 'aria-label="Ruta de navegación"'),
  ('"name": "Home"', '"name": "Inicio"'), ('"name": "Areas"', '"name": "Zonas"'), ('>Areas<', '>Zonas<'),
  ('"item": "https://mianhousedecor.com/"', '"item": "https://mianhousedecor.com/es/"'),
  ('"item": "https://mianhousedecor.com/#about"', '"item": "https://mianhousedecor.com/es/#about"'),
  ('"Miami-Dade County"', '"Condado de Miami-Dade"'),
  # thank-you page
  ('Thank you — MIAN House &amp; Decor', 'Gracias — MIAN House &amp; Decor'),
  ('Thank you — we got it.', 'Gracias, ya lo recibimos.'),
  ("We'll get back to you within 24 hours — usually the same day.", 'Te respondemos en 24 horas, normalmente el mismo día.'),
  ('Want a faster quote? Send us a photo of the piece and its measurements.', '¿Quieres una cotización más rápida? Envíanos una foto de la pieza y sus medidas.'),
  ('Back to the site', 'Volver al sitio'),
]

HOME_META = [
  ('<title>Custom Upholstery North Miami &amp; Miami | Free Quote | MIAN</title>', '<title>Tapicería en Miami | Tapicero de Muebles y Cortinas | MIAN</title>'),
  ('content="Custom Upholstery North Miami &amp; Miami | Free Quote | MIAN"', 'content="Tapicería en Miami | Tapicero de Muebles y Cortinas | MIAN"'),
  ('<link rel="canonical" href="https://mianhousedecor.com/">', '<link rel="canonical" href="https://mianhousedecor.com/es/">'),
  ('<meta property="og:url" content="https://mianhousedecor.com/">', '<meta property="og:url" content="https://mianhousedecor.com/es/">'),
  ('"url": "https://mianhousedecor.com/"', '"url": "https://mianhousedecor.com/es/"'),
  ('"description": "Reupholstery, custom furniture, curtains and cushions for residential and commercial spaces in Miami. Free quote in 24 hours. Hablamos español."', '"description": "Retapizado, muebles a medida, cortinas y cojines para espacios residenciales y comerciales en Miami. Cotización gratis en 24 horas. Atendemos en español."'),
]
HOME_META += [
  ('"name": "Services"', '"name": "Servicios"'), ('"name": "Curtains"', '"name": "Cortinas"'), ('"name": "Fabrics"', '"name": "Telas"'),
  ('"name": "Custom furniture"', '"name": "Muebles a medida"'), ('"name": "Reupholstery"', '"name": "Retapizado"'),
  ('"description": "Made-to-measure drapery, sheers and blackouts."', '"description": "Cortinas a medida, visillos y blackout."'),
  ('"description": "Performance, outdoor, linen and contract-grade textiles."', '"description": "Telas de alto rendimiento, de exterior, lino y grado contract."'),
  ('"description": "Custom pieces built to your dimensions."', '"description": "Piezas hechas a tus medidas."'),
  ('"description": "New fabric and new foam on your existing frame."', '"description": "Tela y espuma nuevas sobre tu estructura."'),
]
HOME_DESC = "Tapicería de muebles en Miami: tu tapicero para tapizar sofás y sillas, más cortinas a medida y cojines. Recogida gratis y cotización gratis en 24 horas. Atendemos en español."
