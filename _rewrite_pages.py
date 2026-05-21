from pathlib import Path
base = Path('.')

files = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="IBYOS Design & Architecture is a Batam architecture studio creating luxury residential, commercial and interior design for Batam, Jakarta and Singapore." />
        <meta name="author" content="IBYOS Design & Architecture" />
        <title>IBYOS Design & Architecture | Batam Architecture Studio</title>
        <meta property="og:title" content="IBYOS Design & Architecture | Batam Architecture Studio" />
        <meta property="og:description" content="A premium architecture studio in Batam delivering residential architecture, commercial design and bespoke interiors for Indonesia and Singapore." />
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link active" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <p class="eyebrow mb-3">Batam Architecture Studio</p>
                        <h1 class="text-dark font-weight-bold">Designing modern architecture and interiors that feel timeless.</h1>
                        <hr class="divider" />
                    </div>
                    <div class="col-lg-8 align-self-baseline">
                        <p class="text-dark mb-5">IBYOS Design & Architecture crafts premium homes, workplaces and bespoke interiors from Batam for clients across Indonesia and Singapore. Our work is quiet, considered and built around serene spatial harmony.</p>
                        <a class="btn btn-primary btn-xl me-3" href="portfolio.html">View Projects</a>
                        <a class="btn btn-outline-primary btn-xl" href="contact.html">Start a Conversation</a>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section bg-light" id="studio-focus">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center text-center">
                    <div class="col-lg-8">
                        <p class="eyebrow mb-3">Architecture Portfolio</p>
                        <h2 class="mt-0">A premium studio for modern architecture in Batam.</h2>
                        <p class="text-muted mb-5">We partner with clients who seek refined architecture, clear spatial strategy and interiors that feel calm, functional and distinctly elegant.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 text-center mt-5">
                    <div class="col-md-4">
                        <h3 class="h5">Residential Architecture</h3>
                        <p class="text-muted">Custom homes and villa projects crafted for natural light, privacy and effortless living.</p>
                    </div>
                    <div class="col-md-4 mt-4 mt-md-0">
                        <h3 class="h5">Commercial Design</h3>
                        <p class="text-muted">Workplaces, showrooms and boutique hospitality spaces designed with brand clarity.</p>
                    </div>
                    <div class="col-md-4 mt-4 mt-md-0">
                        <h3 class="h5">Interior Architecture</h3>
                        <p class="text-muted">Curated materials, warm palettes and spatial refinement for elevated interior experiences.</p>
                    </div>
                </div>
                <div class="text-center mt-5">
                    <a class="btn btn-outline-primary btn-xl" href="services.html">Explore Services</a>
                </div>
            </div>
        </section>
        <section class="page-section" id="portfolio-preview">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center text-center">
                    <div class="col-lg-8">
                        <p class="eyebrow mb-3">Featured Work</p>
                        <h2 class="mt-0">Selected projects from our portfolio.</h2>
                        <p class="text-muted mb-5">Three recent case studies that represent our approach to luxury residential architecture, commercial showrooms and contemporary villa design.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5">
                    <div class="col-md-4 mt-4">
                        <div class="portfolio-card h-100">
                            <img class="img-fluid rounded" src="assets/img/portfolio/thumbnails/3.jpg" alt="Wellness Village architecture preview" />
                            <div class="portfolio-card-body mt-4">
                                <div class="project-category text-secondary">Residential Masterplan</div>
                                <h3 class="h5">Wellness Village</h3>
                                <p class="text-muted">A serene villa retreat designed for health, privacy and connection to landscape.</p>
                                <a class="text-primary" href="wellness-village.html">View Project</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mt-4">
                        <div class="portfolio-card h-100">
                            <img class="img-fluid rounded" src="assets/img/portfolio/thumbnails/5.jpg" alt="Yafindo Showunit preview" />
                            <div class="portfolio-card-body mt-4">
                                <div class="project-category text-secondary">Commercial Architecture</div>
                                <h3 class="h5">Yafindo Showunit</h3>
                                <p class="text-muted">A stylish showroom concept for a premium brand experience in Batam.</p>
                                <a class="text-primary" href="yafindo-showunit.html">View Project</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 mt-4">
                        <div class="portfolio-card h-100">
                            <img class="img-fluid rounded" src="assets/img/portfolio/thumbnails/6.jpg" alt="Villa Panbil preview" />
                            <div class="portfolio-card-body mt-4">
                                <div class="project-category text-secondary">Private Villa</div>
                                <h3 class="h5">Villa Panbil</h3>
                                <p class="text-muted">A refined seaside villa that balances intimate luxury with layered architecture.</p>
                                <a class="text-primary" href="villa-panbil.html">View Project</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-5">
                    <a class="btn btn-outline-primary btn-xl" href="portfolio.html">View Full Portfolio</a>
                </div>
            </div>
        </section>
        <section class="page-section bg-dark text-white text-center">
            <div class="container px-4 px-lg-5">
                <h2 class="mb-4">Looking for a studio in Batam or Singapore?</h2>
                <p class="mb-4">We deliver architecture and interior direction with a premium editorial aesthetic, grounded in site intelligence and Indonesian materials.</p>
                <a class="btn btn-light btn-xl" href="contact.html">Book a Consultation</a>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'about.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="About IBYOS Design & Architecture, a Batam architecture studio offering residential architecture, commercial architecture and interior design." />
        <meta name="author" content="IBYOS Design & Architecture" />
        <title>About | IBYOS Design & Architecture</title>
        <meta property="og:title" content="About | IBYOS Design & Architecture" />
        <meta property="og:description" content="Learn about our Batam architecture studio, our design philosophy, and our approach to luxury residential, workplace and hospitality architecture." />
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link active" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <p class="eyebrow mb-3">Architecture Studio</p>
                        <h1 class="text-dark font-weight-bold">We shape contemporary architecture with quiet confidence.</h1>
                        <hr class="divider" />
                    </div>
                    <div class="col-lg-8 align-self-baseline">
                        <p class="text-muted mb-5">IBYOS Design & Architecture is a Batam-based studio that creates premium residential, commercial and interior architecture with a calm, editorial sensibility.</p>
                        <a class="btn btn-primary btn-xl me-3" href="services.html">View Services</a>
                        <a class="btn btn-outline-primary btn-xl" href="contact.html">Contact Us</a>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section" id="about-intro">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-6">
                        <h2 class="mt-0">An Indonesian studio focused on luxury architecture and meaningful detail.</h2>
                        <p class="text-muted">We work with private clients, developers and visionary brands to design architecture that feels grounded, elegant and thoughtfully composed.</p>
                    </div>
                    <div class="col-lg-6">
                        <p class="mb-4">Our design practice blends spatial clarity, natural materials and contextual intelligence. Each project begins with a rigorous brief, then evolves through careful planning, material direction and refined spatial sequences.</p>
                        <p>Located in Batam, we serve clients in Indonesia and Singapore with architecture consultancy, concept design, interior architecture and construction guidance.</p>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section bg-light" id="approach">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-lg-8 text-center">
                        <h2 class="mt-0">A refined process rooted in craft and clarity.</h2>
                        <p class="text-muted mb-5">We shape every architecture project around the needs of clients, site conditions and the long-term life of the building. The result is work that feels timeless, composed and made to last.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5">
                    <div class="col-md-4">
                        <div class="feature-card p-4 h-100">
                            <h3 class="h5">Client collaboration</h3>
                            <p class="text-muted mb-0">We listen, clarify objectives and make the brief feel strategic, accessible and inspiring.</p>
                        </div>
                    </div>
                    <div class="col-md-4 mt-4 mt-md-0">
                        <div class="feature-card p-4 h-100">
                            <h3 class="h5">Contextual architecture</h3>
                            <p class="text-muted mb-0">Each design responds to site, climate and program while maintaining a restrained, modern aesthetic.</p>
                        </div>
                    </div>
                    <div class="col-md-4 mt-4 mt-md-0">
                        <div class="feature-card p-4 h-100">
                            <h3 class="h5">Material direction</h3>
                            <p class="text-muted mb-0">We refine finishes and details so every space feels tactile, warm and architecturally resolved.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section" id="studio-values">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-6 order-lg-2">
                        <div class="card border-0 shadow-sm p-4 bg-white">
                            <h3 class="h4">We shape ideas into calm, modern spaces.</h3>
                            <p class="text-muted">Our studio is chosen for intelligent architecture, disciplined execution and an understated approach to luxury.</p>
                            <ul class="list-unstyled text-muted mb-0">
                                <li>Batam-based architecture studio</li>
                                <li>Residential architecture and private villas</li>
                                <li>Commercial architecture and showrooms</li>
                                <li>Interior architecture and renovation design</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-6 order-lg-1">
                        <h2 class="mt-0">Architecture crafted for modern Indonesian life.</h2>
                        <p class="text-muted">From a boutique showroom in Batam to a villa by the water, our work respects context, material strength and a quiet sense of luxury.</p>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section bg-dark text-white text-center">
            <div class="container px-4 px-lg-5">
                <h2 class="mb-4">Ready to begin a design collaboration?</h2>
                <p class="mb-5">Let us help you frame what is possible for your home, work or hospitality project.</p>
                <a class="btn btn-light btn-xl" href="contact.html">Start Your Project</a>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'services.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="IBYOS Design & Architecture provides architecture services in Batam, Jakarta and Singapore for residential homes, villas, showrooms and interiors." />
        <meta name="author" content="IBYOS Design & Architecture" />
        <title>Services | IBYOS Design & Architecture</title>
        <meta property="og:title" content="Services | IBYOS Design & Architecture" />
        <meta property="og:description" content="Explore our architecture services for modern homes, commercial spaces, renovation design and interior architecture from our Batam studio." />
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link active" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <p class="eyebrow mb-3">Architectural Services</p>
                        <h1 class="text-dark font-weight-bold">Architecture, interiors and project direction with premium clarity.</h1>
                        <hr class="divider" />
                    </div>
                    <div class="col-lg-8 align-self-baseline">
                        <p class="text-muted mb-5">From bespoke home architecture to commercial showroom design and interior architecture, we support clients in Batam, Jakarta and Singapore with a thoughtful, high-end design practice.</p>
                        <a class="btn btn-primary btn-xl me-3" href="portfolio.html">View Portfolio</a>
                        <a class="btn btn-outline-primary btn-xl" href="contact.html">Book Consultation</a>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section" id="services-list">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-lg-8 text-center">
                        <h2 class="mt-0">Design services for refined architecture and interiors.</h2>
                        <p class="text-muted mb-5">Our service offering is built for clients who want modern, elegant spaces that are both expressive and exceptionally livable.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5">
                    <div class="col-md-6 col-lg-4">
                        <div class="service-card h-100">
                            <span class="service-icon">01</span>
                            <h3 class="h5">Residential Architecture</h3>
                            <p class="text-muted">Custom home design, luxury villas and connected family spaces with a calm, modern aesthetic.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mt-4 mt-md-0">
                        <div class="service-card h-100">
                            <span class="service-icon">02</span>
                            <h3 class="h5">Commercial Architecture</h3>
                            <p class="text-muted">Showrooms, hospitality and workplace environments designed for brand presence and everyday performance.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mt-4 mt-lg-0">
                        <div class="service-card h-100">
                            <span class="service-icon">03</span>
                            <h3 class="h5">Interior Architecture</h3>
                            <p class="text-muted">Material direction, lighting and spatial detailing to create cohesive, elegant interiors.</p>
                        </div>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-4">
                    <div class="col-md-6 col-lg-4">
                        <div class="service-card h-100">
                            <span class="service-icon">04</span>
                            <h3 class="h5">Renovation Design</h3>
                            <p class="text-muted">Adaptive design for existing buildings, preserving character while introducing modern clarity.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mt-4 mt-md-0">
                        <div class="service-card h-100">
                            <span class="service-icon">05</span>
                            <h3 class="h5">Design Consultation</h3>
                            <p class="text-muted">Brief development, concept refinement and strategic guidance across architecture projects.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 mt-4 mt-lg-0">
                        <div class="service-card h-100">
                            <span class="service-icon">06</span>
                            <h3 class="h5">Project Direction</h3>
                            <p class="text-muted">Coordination through construction to ensure thoughtful execution and material quality.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section bg-light" id="process">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-6">
                        <h2 class="mt-0">A considered process for ambitious architectural projects.</h2>
                        <p class="text-muted">We pair design thinking with practical delivery to create spaces that feel beautiful, intuitive and tailored to how people live and work.</p>
                    </div>
                    <div class="col-lg-6">
                        <div class="process-list">
                            <div class="process-item">
                                <strong>01</strong>
                                <div>
                                    <h3 class="h5">Discovery</h3>
                                    <p class="text-muted">We define the brief, site potential and client aspirations before design begins.</p>
                                </div>
                            </div>
                            <div class="process-item">
                                <strong>02</strong>
                                <div>
                                    <h3 class="h5">Design</h3>
                                    <p class="text-muted">Concepts are refined with spatial clarity, materials and strategic architecture decisions.</p>
                                </div>
                            </div>
                            <div class="process-item">
                                <strong>03</strong>
                                <div>
                                    <h3 class="h5">Delivery</h3>
                                    <p class="text-muted">We support execution through documentation, coordination and quality oversight.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section bg-dark text-white text-center">
            <div class="container px-4 px-lg-5">
                <h2 class="mb-4">Let’s create architecture that feels exceptional.</h2>
                <a class="btn btn-light btn-xl" href="contact.html">Book a Consultation</a>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'contact.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="Contact IBYOS Design & Architecture, a Batam architecture firm offering residential, commercial and interior design services across Indonesia and Singapore." />
        <meta name="author" content="IBYOS Design & Architecture" />
        <title>Contact | IBYOS Design & Architecture</title>
        <meta property="og:title" content="Contact | IBYOS Design & Architecture" />
        <meta property="og:description" content="Reach IBYOS Design & Architecture in Batam to discuss your next architectural project, villa, showroom or interior design brief." />
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link active" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <p class="eyebrow mb-3">Design Consultation</p>
                        <h1 class="text-dark font-weight-bold">Begin your next architecture project in Batam.</h1>
                        <hr class="divider" />
                    </div>
                    <div class="col-lg-8 align-self-baseline">
                        <p class="text-muted mb-5">Share your brief for a villa, showroom, renovation or interior architecture project and our studio will respond with a tailored design consultation.</p>
                        <a class="btn btn-primary btn-xl" href="#contact-form">Start Your Project</a>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section" id="contact-details">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-6">
                        <h2 class="mt-0">Batam-based architecture with local insight.</h2>
                        <p class="text-muted">IBYOS Design & Architecture works with clients across Batam, Jakarta and Singapore. We deliver architecture and interior direction rooted in Indonesian context and modern luxury.</p>
                        <ul class="contact-list text-muted">
                            <li><strong>Phone:</strong> +62 815-0000-0000</li>
                            <li><strong>Email:</strong> <a href="mailto:hello@ibyosdesign.com">hello@ibyosdesign.com</a></li>
                            <li><strong>Location:</strong> Batam, Indonesia</li>
                            <li><strong>Service area:</strong> Batam, Jakarta, Singapore</li>
                        </ul>
                    </div>
                    <div class="col-lg-6 mt-4 mt-lg-0">
                        <div class="card border-0 shadow-sm p-4 bg-white">
                            <h3 class="h4">What we can discuss</h3>
                            <p class="text-muted">Whether you are starting a villa, a showroom or a renovation project, we can help you define the right architecture approach, aesthetic direction and delivery strategy.</p>
                            <ul class="list-unstyled text-muted mb-0">
                                <li>Architecture consulting and concept design</li>
                                <li>Residential architecture and villa planning</li>
                                <li>Showroom and commercial architecture</li>
                                <li>Interior architecture and material direction</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="page-section bg-light" id="contact-form">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-6">
                        <div class="map-placeholder">
                            <h3>Studio in Batam</h3>
                            <p class="mb-0">IBYOS Design & Architecture<br />Batam, Indonesia</p>
                        </div>
                    </div>
                    <div class="col-lg-6 mt-4 mt-lg-0">
                        <div class="text-center mb-5">
                            <h2 class="mt-0">Tell us about your project</h2>
                            <p class="text-muted">Complete the form below and we will respond with a consultation proposal.</p>
                        </div>
                        <form id="contactForm" data-sb-form-api-token="API_TOKEN">
                            <div class="form-floating mb-3">
                                <input class="form-control" id="name" type="text" placeholder="Enter your name" data-sb-validations="required" />
                                <label for="name">Full name</label>
                                <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                            </div>
                            <div class="form-floating mb-3">
                                <input class="form-control" id="email" type="email" placeholder="name@example.com" data-sb-validations="required,email" />
                                <label for="email">Email address</label>
                                <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                                <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                            </div>
                            <div class="form-floating mb-3">
                                <input class="form-control" id="phone" type="tel" placeholder="+62 815 0000 0000" data-sb-validations="required" />
                                <label for="phone">Phone number</label>
                                <div class="invalid-feedback" data-sb-feedback="phone:required">A phone number is required.</div>
                            </div>
                            <div class="form-floating mb-3">
                                <textarea class="form-control" id="message" placeholder="Enter your project details" style="height: 12rem" data-sb-validations="required"></textarea>
                                <label for="message">Project details</label>
                                <div class="invalid-feedback" data-sb-feedback="message:required">A message is required.</div>
                            </div>
                            <div class="d-grid"><button class="btn btn-primary btn-xl disabled" id="submitButton" type="submit">Submit</button></div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'wellness-village.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="Wellness Village is a premium residential architecture case study by IBYOS Design & Architecture, designed for landscape, wellness and luxury villa living." />
        <meta property="og:title" content="Wellness Village | IBYOS Design & Architecture" />
        <meta property="og:description" content="Explore the Wellness Village case study, a villa architecture project that balances wellness, privacy and landscape-driven design." />
        <title>Wellness Village | IBYOS Design & Architecture</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead project-hero">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-end justify-content-center text-center">
                    <div class="col-lg-10">
                        <p class="eyebrow mb-3">Featured Project</p>
                        <h1 class="text-dark font-weight-bold">Wellness Village</h1>
                        <p class="text-muted mb-5">A premium residential masterplan created for wellness, landscape intimacy and understated luxury in Batam.</p>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section bg-light" id="project-overview">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-7">
                        <img class="img-fluid rounded shadow-sm" src="assets/img/portfolio/fullsize/3.jpg" alt="Wellness Village villa architecture" />
                    </div>
                    <div class="col-lg-5">
                        <h2 class="mt-0">Project overview</h2>
                        <p class="text-muted">Wellness Village is an intimate residential enclave defined by private courtyards, quiet garden rooms and a gentle balance of architecture and landscape. The project supports restorative living through careful layout, generous outdoor rooms and natural material richness.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Design challenge</h3>
                        <ul class="text-muted">
                            <li>Develop a villa community that feels private yet connected to the landscape.</li>
                            <li>Create architecture that supports wellness, cooling breezes and quiet retreat spaces.</li>
                            <li>Deliver a refined material palette suitable for coastal Batam living.</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Concept</h3>
                        <p class="text-muted">The design embraces layered volumes around central courtyards, with framed views and natural ventilation as the organizing principles. Architecture is calm and tactile, with locally inspired finishes and a warm, restrained palette.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Key features</h3>
                        <p class="text-muted">Private wellness pavilions, landscaped reflecting pools, timber-clad reception spaces and seamless indoor-outdoor transitions create a holistic experience.</p>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Impact</h3>
                        <ul class="text-muted">
                            <li>A contemporary retreat with a strong connection to garden and air.</li>
                            <li>Planned for wellbeing, low maintenance and elevated daily living.</li>
                            <li>Architecture that feels both modern and quietly luxurious.</li>
                        </ul>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-lg-12 text-center">
                        <h3 class="h5">Interested in a wellness-led architecture project?</h3>
                        <p class="text-muted mb-4">Contact our studio to discuss custom residential architecture that values landscape, privacy and modern luxury.</p>
                        <a class="btn btn-primary btn-xl" href="contact.html">Contact Us</a>
                    </div>
                </div>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'yafindo-showunit.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="Yafindo Showunit is a commercial showroom project by IBYOS Design & Architecture featuring brand-led architecture and premium interior design." />
        <meta property="og:title" content="Yafindo Showunit | IBYOS Design & Architecture" />
        <meta property="og:description" content="Discover the Yafindo Showunit case study, a refined commercial architecture project designed for Batam retail and showroom experience." />
        <title>Yafindo Showunit | IBYOS Design & Architecture</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead project-hero">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-end justify-content-center text-center">
                    <div class="col-lg-10">
                        <p class="eyebrow mb-3">Featured Project</p>
                        <h1 class="text-dark font-weight-bold">Yafindo Showunit</h1>
                        <p class="text-muted mb-5">A commercial showroom concept designed to elevate brand presence and customer experience in Batam.</p>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section bg-light" id="project-overview">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-7 order-lg-2">
                        <img class="img-fluid rounded shadow-sm" src="assets/img/portfolio/fullsize/5.jpg" alt="Yafindo Showunit interior architecture" />
                    </div>
                    <div class="col-lg-5 order-lg-1">
                        <h2 class="mt-0">Project overview</h2>
                        <p class="text-muted">Yafindo Showunit is a refined retail pavilion crafted for luxury finishes, curated product presentation and a welcoming arrival sequence. The design merges architecture and interior direction to support a premium brand story.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Design challenge</h3>
                        <ul class="text-muted">
                            <li>Design a showroom that feels polished, accessible and distinctly premium.</li>
                            <li>Support product storytelling through a calm architecture framework.</li>
                            <li>Ensure the space is flexible for seasonal display and client hospitality.</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Concept</h3>
                        <p class="text-muted">The concept combines a refined material palette with layered lighting and clear circulation. The showroom is arranged to guide visitors through display zones while preserving a sense of calm and discovery.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Key features</h3>
                        <p class="text-muted">Soft plaster walls, indirect lighting, custom display furniture and a quiet lounge area create a polished retail environment.</p>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Impact</h3>
                        <ul class="text-muted">
                            <li>Showroom architecture that honors the brand and product experience.</li>
                            <li>A welcoming retail destination optimized for Batam clientele.</li>
                            <li>Flexible display zones for future program shifts and extended merchandising.</li>
                        </ul>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-lg-12 text-center">
                        <h3 class="h5">Planning a premium commercial space?</h3>
                        <p class="text-muted mb-4">Speak with our Batam studio about showroom, retail and hospitality architecture that supports brand impact.</p>
                        <a class="btn btn-primary btn-xl" href="contact.html">Contact Us</a>
                    </div>
                </div>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
''',
    'villa-panbil.html': '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="Villa Panbil is a private villa case study by IBYOS Design & Architecture, blending contemporary architecture, coastal living and refined interior planning." />
        <meta property="og:title" content="Villa Panbil | IBYOS Design & Architecture" />
        <meta property="og:description" content="Discover Villa Panbil, a coastal villa project designed with elegant materiality, layered spatial planning and premium architecture." />
        <title>Villa Panbil | IBYOS Design & Architecture</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body id="page-top">
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">IBYOS Design & Architecture</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>
                        <li class="nav-item"><a class="nav-link" href="portfolio.html">Portfolio</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <header class="masthead project-hero">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-end justify-content-center text-center">
                    <div class="col-lg-10">
                        <p class="eyebrow mb-3">Featured Project</p>
                        <h1 class="text-dark font-weight-bold">Villa Panbil</h1>
                        <p class="text-muted mb-5">A coastal private villa that layers architecture, texture and hospitality-style spatial planning.</p>
                    </div>
                </div>
            </div>
        </header>
        <section class="page-section bg-light" id="project-overview">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 align-items-center">
                    <div class="col-lg-7">
                        <img class="img-fluid rounded shadow-sm" src="assets/img/portfolio/fullsize/6.jpg" alt="Villa Panbil coastal architecture" />
                    </div>
                    <div class="col-lg-5">
                        <h2 class="mt-0">Project overview</h2>
                        <p class="text-muted">Villa Panbil brings a coastal retreat to life with subtle luxury, generous terraces and an orientation that maximizes views and natural ventilation.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Design challenge</h3>
                        <ul class="text-muted">
                            <li>Compose a villa with strong indoor-outdoor connections and calm living zones.</li>
                            <li>Use architecture to frame coastal views while respecting privacy.</li>
                            <li>Bring warmth through refined materials and subtle detailing.</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Concept</h3>
                        <p class="text-muted">The architecture is articulated as a series of layered pavilions and terraces, with a restrained palette of stone, timber and soft plaster. Interior volumes feel open yet grounded, supporting both family life and guest hospitality.</p>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-md-6">
                        <h3 class="h5">Key features</h3>
                        <p class="text-muted">A tranquil pool court, shaded living terraces, sculptural stair volume and bespoke joinery create a luxurious yet grounded villa atmosphere.</p>
                    </div>
                    <div class="col-md-6">
                        <h3 class="h5">Impact</h3>
                        <ul class="text-muted">
                            <li>Calm and contemporary villa architecture for waterfront living.</li>
                            <li>Premium interior ambiance with a refined, tactile palette.</li>
                            <li>Architecture that reads as elegant, intimate and quietly sophisticated.</li>
                        </ul>
                    </div>
                </div>
                <div class="row gx-4 gx-lg-5 mt-5">
                    <div class="col-lg-12 text-center">
                        <h3 class="h5">Planning a private villa or coastal residence?</h3>
                        <p class="text-muted mb-4">Reach out to discuss residential architecture that balances luxury, climate and enduring design.</p>
                        <a class="btn btn-primary btn-xl" href="contact.html">Contact Us</a>
                    </div>
                </div>
            </div>
        </section>
        <footer class="bg-light py-5">
            <div class="container px-4 px-lg-5"><div class="small text-center text-muted">Copyright &copy; 2026 IBYOS Design & Architecture</div></div>
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <script src="js/scripts.js"></script>
    </body>
</html>
'''
}

for name, content in files.items():
    path = base / name
    path.write_text(content, encoding='utf-8')
    print(f'Wrote {path}')

css_path = base / 'css' / 'styles.css'
custom_css = '''
/* Custom IBYOS Design & Architecture overrides */
body {
  font-family: "Merriweather", serif;
  letter-spacing: 0.01em;
  line-height: 1.8;
}
.masthead {
  min-height: 80vh;
  padding-top: 5rem;
  padding-bottom: 5rem;
  display: flex;
  align-items: center;
  background: linear-gradient(180deg, rgba(247,241,232,0.96), rgba(233,225,211,1));
}
.project-hero {
  min-height: 60vh;
  padding-top: 6rem;
  padding-bottom: 3rem;
  background: linear-gradient(180deg, rgba(247,241,232,0.98), rgba(229,220,206,1));
}
.project-hero .eyebrow {
  color: #7b7469;
}
.service-card {
  border: 1px solid rgba(36, 32, 27, 0.08);
  background: #fff;
  border-radius: 1.25rem;
  padding: 2rem;
  box-shadow: 0 12px 28px rgba(36, 32, 27, 0.06);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.service-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 42px rgba(36, 32, 27, 0.12);
}
.service-card h3 {
  margin-top: 1rem;
}
.service-card .service-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 3rem;
  height: 3rem;
  background: rgba(79, 91, 71, 0.12);
  color: var(--bs-primary);
  font-weight: 700;
  border-radius: 999px;
  margin-bottom: 1rem;
}
.map-placeholder {
  min-height: 320px;
  background: linear-gradient(135deg, rgba(79,91,71,0.09), rgba(174,155,132,0.12));
  border: 1px solid rgba(36,32,27,0.08);
  border-radius: 1rem;
  display: grid;
  place-items: center;
  color: #4f5b47;
  text-align: center;
  padding: 2rem;
}
@media (max-width: 991.98px) {
  .masthead, .project-hero {
    padding-top: 4rem;
    padding-bottom: 4rem;
  }
  .feature-card, .service-card, .portfolio-card {
    margin-bottom: 1.5rem;
  }
}
'''
with css_path.open('a', encoding='utf-8') as f:
    f.write(custom_css)
print(f'Appended custom CSS to {css_path}')
