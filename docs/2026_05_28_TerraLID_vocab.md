---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 5
    smooth-scroll: true
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#TerraLIDvocabularies}

# **Concept scheme:** TerraLID vocabularies

Vocabulary last modified:  2026-05-28T12:58:49

subtitle: The TerraLID vocabularies include various vocabularies to ensure coherent data entries for the TerraLID metadata profile, which describes archaeometric data and the materials they are derived from with particular focus on lead isotope data. The vocabularies were compiled by the TerraLID Editors and the TerraLID Core Team and implemented in SKOS by Thomas Rose and Katrin J. Westner. This work has received funding from the German Research Foundation (DFG) through the grants KL 1259/17-1 and WI 5923/2-1 (project number: 524790825).

Namespace: 
[`http://vocab.terralid.org#conceptScheme_a0559f69`](http://vocab.terralid.org#conceptScheme_a0559f69)

**History**


- [site type](#site-type)
    - [anthropogenic site](#anthropogenic-site)
        - [built structures](#built-structures)
            - [camp](#camp)
            - [settlement](#settlement)
            - [building](#building)
                - [house](#house)
                - [military structure](#military-structure)
                - [administrative structure](#administrative-structure)
                - [communal structure](#communal-structure)
                - [religious structure](#religious-structure)
                - [agricultural structure](#agricultural-structure)
                - [workshop](#workshop)
                    - [foundry](#foundry)
                    - [smelting site](#smelting-site)
                    - [melting site](#melting-site)
                    - [non-metallurgical workshop](#non-metallurgical-workshop)
            - [infrastructure](#infrastructure)
                - [bridge](#bridge)
                - [road](#road)
        - [mine](#mine)
            - [underground mine](#underground-mine)
            - [open pit mine](#open-pit-mine)
        - [mining-related site](#mining-related-site)
            - [ore beneficiation site](#ore-beneficiation-site)
            - [mining sink-hole](#mining-sink-hole)
            - [slag dump](#slag-dump)
            - [mine dump](#mine-dump)
            - [tailing dump](#tailing-dump)
            - [mining project](#mining-project)
        - [refuse area](#refuse-area)
            - [slag dump](#slag-dump)
            - [debris dump](#debris-dump)
            - [mine dump](#mine-dump)
            - [tailing dump](#tailing-dump)
            - [midden](#midden)
        - [funerary site](#funerary-site)
            - [burial ground](#burial-ground)
            - [grave](#grave)
            - [tomb](#tomb)
            - [burial cave](#burial-cave)
        - [artefact scatter](#artefact-scatter)
        - [single find](#single-find)
        - [isolated feature](#isolated-feature)
        - [hearth](#hearth)
        - [post hole](#post-hole)
        - [pit](#pit)
        - [infilling](#infilling)
        - [storage pit](#storage-pit)
    - [geological site](#geological-site)
        - [cave](#cave)
            - [burial cave](#burial-cave)
        - [deposit](#deposit)
        - [occurrence](#occurrence)
            - [outcrop](#outcrop)
        - [field](#field)
        - [locality](#locality)
    - [unknown](#unknown)

- [assemblage](#assemblage)
    - [collection](#collection)
    - [components](#components)
    - [hoard](#hoard)
    - [item](#item)
    - [set](#set)
    - [gossan](#gossan)
    - [alteration product (hydrothermal)](#alteration-product-(hydrothermal))
    - [alteration product (supergene)](#alteration-product-(supergene))
    - [host rock](#host-rock)
    - [ore](#ore)
        - [primary ore](#primary-ore)
        - [secondary ore](#secondary-ore)
        - [alteration](#alteration)
        - [ore mineral](#ore-mineral)
            - [major mineral](#major-mineral)
            - [minor mineral](#minor-mineral)
    - [wall rock](#wall-rock)
    - [gangue](#gangue)
        - [host rock](#host-rock)

- [discovery activity](#discovery-activity)
    - [unknown](#unknown)
    - [stray find](#stray-find)
    - [borehole survey](#borehole-survey)
        - [core drilling](#core-drilling)
        - [auger drilling](#auger-drilling)
    - [metal detecting](#metal-detecting)
    - [excavation](#excavation)
        - [research excavation](#research-excavation)
        - [rescue excavation](#rescue-excavation)
        - [underwater excavation](#underwater-excavation)
    - [survey](#survey)
    - [mining](#mining)
    - [explorative mining activities](#explorative-mining-activities)
    - [ore prospection](#ore-prospection)
    - [illicit digging](#illicit-digging)

- [context type](#context-type)
    - [unknown](#unknown)
    - [undisturbed context](#undisturbed-context)
    - [disturbed context](#disturbed-context)
        - [anthropogenically disturbed](#anthropogenically-disturbed)
        - [biogenically disturbed](#biogenically-disturbed)
    - [mixed context](#mixed-context)

- [sample housing](#sample-housing)
    - [unknown](#unknown)
    - [cardboard box](#cardboard-box)
        - [acid-free cardboard box](#acid-free-cardboard-box)
        - [non acid-free cardboard box](#non-acid-free-cardboard-box)
    - [Eppendorf tube](#eppendorf-tube)
    - [glass vial](#glass-vial)
    - [PTFE/Teflon vial](#ptfe-teflon-vial)
    - [no housing](#no-housing)
    - [plastics bag](#plastics-bag)
        - [ziplock bag](#ziplock-bag)
        - [plastics fabric bag](#plastics-fabric-bag)
    - [fabric bag](#fabric-bag)
        - [cotton fabric bag](#cotton-fabric-bag)
        - [plastics fabric bag](#plastics-fabric-bag)
    - [paper bag](#paper-bag)
        - [acid-free paper bag](#acid-free-paper-bag)
        - [non acid-free paper bag](#non-acid-free-paper-bag)
    - [display case](#display-case)
        - [controlled environment display case](#controlled-environment-display-case)
        - [uncontrolled environment display case](#uncontrolled-environment-display-case)

- [object life cycle stage](#object-life-cycle-stage)
    - [storage stage](#storage-stage)
    - [restoration stage](#restoration-stage)
    - [conservation stage](#conservation-stage)
    - [finds processing stage](#finds-processing-stage)
    - [discovery stage](#discovery-stage)
    - [laboratory stage](#laboratory-stage)

- [object material](#object-material)
    - [unknown](#unknown)
    - [other](#other)
    - [sediment](#sediment)
    - [ceramic](#ceramic)
    - [pigment](#pigment)
    - [glass](#glass)
    - [metal](#metal)
        - [coin](#coin)
    - [ore (TerraLID category)](#ore-(terralid-category))

- [authenticity](#authenticity)
    - [unknown](#unknown)
    - [modern imitation](#modern-imitation)
    - [contemporary imitation](#contemporary-imitation)
    - [genuine](#genuine)

- [sample material](#sample-material)
    - [unknown](#unknown)
    - [geological material](#geological-material)
        - [gossan](#gossan)
        - [host rock](#host-rock)
        - [ore](#ore)
            - [primary ore](#primary-ore)
            - [secondary ore](#secondary-ore)
            - [alteration](#alteration)
            - [ore mineral](#ore-mineral)
                - [major mineral](#major-mineral)
                - [minor mineral](#minor-mineral)
        - [wall rock](#wall-rock)
        - [sediment](#sediment)
        - [mineral](#mineral)
        - [unaltered material](#unaltered-material)
    - [anthropogenic material](#anthropogenic-material)
        - [ceramic](#ceramic)
        - [pigment](#pigment)
        - [glass](#glass)
        - [metal](#metal)
            - [coin](#coin)
        - [alteration product (anthropogenic)](#alteration-product-(anthropogenic))
        - [unaltered material](#unaltered-material)
    - [alteration product](#alteration-product)
        - [alteration product (hydrothermal)](#alteration-product-(hydrothermal))
        - [alteration product (supergene)](#alteration-product-(supergene))
        - [alteration product (anthropogenic)](#alteration-product-(anthropogenic))
    - [bulk](#bulk)

- [sample type](#sample-type)
    - [unknown](#unknown)
    - [drill shavings](#drill-shavings)
    - [in-situ](#in-situ)
    - [powder](#powder)
    - [hand-picked](#hand-picked)
    - [mineral separate](#mineral-separate)
    - [leachate](#leachate)
    - [swabbed material](#swabbed-material)
    - [hand specimen fragments](#hand-specimen-fragments)
    - [loose material](#loose-material)
    - [cut](#cut)
    - [section](#section)
        - [polished section](#polished-section)
        - [thin section](#thin-section)

- [sampling method](#sampling-method)
    - [unknown](#unknown)
    - [drilling](#drilling)
        - [micromill](#micromill)
    - [cutting](#cutting)
    - [abrading](#abrading)
    - [ablating](#ablating)
    - [dissolution](#dissolution)
        - [swabbing](#swabbing)
        - [etching/leaching](#etching-leaching)
    - [fragment collection](#fragment-collection)
    - [crushing](#crushing)
    - [separation](#separation)
        - [magnet separation](#magnet-separation)
        - [density separation](#density-separation)
        - [hand-picking](#hand-picking)

- [sample state](#sample-state)
    - [unknown](#unknown)
    - [modified](#modified)
    - [no material left](#no-material-left)
    - [material consumed](#material-consumed)
    - [unchanged](#unchanged)

- [sample introduction](#sample-introduction)
    - [solution](#solution)
    - [laser ablation](#laser-ablation)

- [analytical method](#analytical-method)
    - [mass spectrometer](#mass-spectrometer)
        - [TIMS](#tims)
        - [ICP-MS](#icp-ms)
            - [MC-ICP-MS](#mc-icp-ms)
                - [LA-MC-ICP-MS](#la-mc-icp-ms)
                    - [fs-LA-MC-ICP-MS](#fs-la-mc-icp-ms)
                    - [ns-LA-MC-ICP-MS](#ns-la-mc-icp-ms)
            - [Q-ICP-MS](#q-icp-ms)
            - [LA-ICP-MS](#la-icp-ms)
                - [LA-MC-ICP-MS](#la-mc-icp-ms)
                    - [fs-LA-MC-ICP-MS](#fs-la-mc-icp-ms)
                    - [ns-LA-MC-ICP-MS](#ns-la-mc-icp-ms)
                - [fs-LA-ICP-MS](#fs-la-icp-ms)
                - [ns-LA-ICP-MS](#ns-la-icp-ms)
    - [atomic absorption spectroscopy](#atomic-absorption-spectroscopy)
        - [AAS (glow-discharge)](#aas-(glow-discharge))
        - [AAS (flame)](#aas-(flame))
        - [AAS (graphite furnace)](#aas-(graphite-furnace))
    - [emission spectrometry](#emission-spectrometry)
        - [OES (spark)](#oes-(spark))
        - [OES (ICP)](#oes-(icp))
        - [AES (graphite furnace)](#aes-(graphite-furnace))
        - [AES (flame)](#aes-(flame))
    - [X-ray spectrometry](#x-ray-spectrometry)
        - [ED-XRF](#ed-xrf)
            - [pXRF](#pxrf)
        - [WD-XRF](#wd-xrf)
        - [EPMA](#epma)
        - [SEM-EDS](#sem-eds)
    - [wet chemistry](#wet-chemistry)
    - [NAA](#naa)

- [mass bias correction](#mass-bias-correction)
    - [linear model](#linear-model)
    - [double-spike](#double-spike)
    - [standard-sample bracketing](#standard-sample-bracketing)
    - [power law](#power-law)
    - [exponential law](#exponential-law)

- [reference material](#reference-material)
    - [unknown](#unknown)
    - [other](#other)
    - [Tl isotope CRMs](#tl-isotope-crms)
        - [ERM-AE649](#erm-ae649)
        - [NIST SRM 997](#nist-srm-997)
    - [Pb Isotope CRMs](#pb-isotope-crms)
        - [NIST SRM 981](#nist-srm-981)
        - [NIST SRM 610](#nist-srm-610)
        - [NIST SRM 612](#nist-srm-612)
        - [NIST SRM 614](#nist-srm-614)
        - [NIST SRM 3328](#nist-srm-3328)
        - [BHVO-2](#bhvo-2)
            - [BHVO-2G](#bhvo-2g)
        - [BIR-1](#bir-1)
            - [BIR-1G](#bir-1g)
        - [BCR-2](#bcr-2)
            - [BCR-2G](#bcr-2g)
        - [ERM-3800](#erm-3800)
        - [GSD-1](#gsd-1)
            - [GSD-1G](#gsd-1g)

- [lead isotope age model](#lead-isotope-age-model)
    - [SK75](#sk75)
    - [CR75](#cr75)
    - [AJ84](#aj84)

- [analytical instrument](#analytical-instrument)
    - [other](#other)
    - [instrument manufacturer](#instrument-manufacturer)
        - [Thermo Fisher Scientific](#thermo-fisher-scientific)
            - [Neoma](#neoma)
            - [Neptune](#neptune)
            - [Neptune Plus](#neptune-plus)
            - [Triton XT](#triton-xt)
            - [Triton Plus](#triton-plus)
        - [Nu Instruments](#nu-instruments)
            - [Plasma 1700](#plasma-1700)
            - [Plasma 3](#plasma-3)
            - [Sapphire](#sapphire)
            - [Sapphire XD](#sapphire-xd)
            - [TIMS (Nu instruments)](#tims-(nu-instruments))
        - [SELMI](#selmi)
            - [MI 1201-AT](#mi-1201-at)
        - [Uralpribor](#uralpribor)
            - [MIT 350-TM](#mit-350-tm)
        - [Micromass](#micromass)
            - [Sector 54](#sector-54)
        - [Isotopx](#isotopx)
            - [Phoenix](#phoenix)
        - [GV Instruments](#gv-instruments)
            - [IsoProbe-P](#isoprobe-p)
            - [IsoProbe-T](#isoprobe-t)
        - [Finnigan MAT](#finnigan-mat)
            - [MAT 262](#mat-262)
        - [MSTech Group](#mstech-group)
            - [ZMS DF-TIMS-01](#zms-df-tims-01)
        - [Kunyuan Instrument](#kunyuan-instrument)
            - [GB-TIMS](#gb-tims)
    - [instrument model](#instrument-model)
        - [Neoma](#neoma)
        - [Neptune](#neptune)
        - [Neptune Plus](#neptune-plus)
        - [Plasma 1700](#plasma-1700)
        - [Plasma 3](#plasma-3)
        - [Sapphire](#sapphire)
        - [Sapphire XD](#sapphire-xd)
        - [IsoProbe-P](#isoprobe-p)
        - [MAT 262](#mat-262)
        - [MI 1201-AT](#mi-1201-at)
        - [MIT 350-TM](#mit-350-tm)
        - [Sector 54](#sector-54)
        - [Phoenix](#phoenix)
        - [TIMS (Nu instruments)](#tims-(nu-instruments))
        - [ZMS DF-TIMS-01](#zms-df-tims-01)
        - [Triton XT](#triton-xt)
        - [Triton Plus](#triton-plus)
        - [GB-TIMS](#gb-tims)
        - [IsoProbe-T](#isoprobe-t)
    - [instrument type](#instrument-type)
        - [MC-ICP-MS (instrument)](#mc-icp-ms-(instrument))
            - [Neoma](#neoma)
            - [Neptune](#neptune)
            - [Neptune Plus](#neptune-plus)
            - [Plasma 1700](#plasma-1700)
            - [Plasma 3](#plasma-3)
            - [Sapphire](#sapphire)
            - [Sapphire XD](#sapphire-xd)
            - [IsoProbe-P](#isoprobe-p)
        - [TIMS (instrument)](#tims-(instrument))
            - [MAT 262](#mat-262)
            - [MI 1201-AT](#mi-1201-at)
            - [MIT 350-TM](#mit-350-tm)
            - [Sector 54](#sector-54)
            - [Phoenix](#phoenix)
            - [TIMS (Nu instruments)](#tims-(nu-instruments))
            - [ZMS DF-TIMS-01](#zms-df-tims-01)
            - [Triton XT](#triton-xt)
            - [Triton Plus](#triton-plus)
            - [GB-TIMS](#gb-tims)
            - [IsoProbe-T](#isoprobe-t)

- [abundance (concentration)](#abundance-(concentration))
    - [major](#major)
    - [minor](#minor)
    - [trace](#trace)

- [alteration extent](#alteration-extent)
    - [unknown](#unknown)
    - [severe alteration](#severe-alteration)
    - [slight alteration](#slight-alteration)
    - [no alteration](#no-alteration)

- [production context](#production-context)
    - [unknown](#unknown)
    - [primary](#primary)
    - [secondary](#secondary)

- [recycling indicator](#recycling-indicator)
    - [unknown](#unknown)
    - [recycling suspected](#recycling-suspected)
    - [not recycled](#not-recycled)
    - [recycled](#recycled)

- [corrosion extent](#corrosion-extent)
    - [unknown](#unknown)
    - [severe corrosion](#severe-corrosion)
    - [moderate corrosion](#moderate-corrosion)
    - [weak corrosion](#weak-corrosion)
    - [no corrosion](#no-corrosion)

- [glass component](#glass-component)
    - [unknown](#unknown)
    - [opacifier](#opacifier)
    - [network modifier](#network-modifier)
    - [network former](#network-former)
    - [colorant](#colorant)

- [compound type](#compound-type)
    - [unknown](#unknown)
    - [mixed compound types](#mixed-compound-types)
    - [organic](#organic)
    - [inorganic](#inorganic)

- [compound origin](#compound-origin)
    - [unknown](#unknown)
    - [mixed compound origin](#mixed-compound-origin)
    - [synthetic](#synthetic)
    - [natural](#natural)

- [pigment component](#pigment-component)
    - [unknown](#unknown)
    - [various](#various)
    - [impurity](#impurity)
    - [binder](#binder)
    - [colorant](#colorant)
    - [flux](#flux)

- [alteration process](#alteration-process)
    - [unknown](#unknown)
    - [other](#other)
    - [photodegradation](#photodegradation)
    - [oxidation](#oxidation)
    - [erosion](#erosion)
    - [biodegradation](#biodegradation)
    - [darkening](#darkening)
    - [efflorescense](#efflorescense)
    - [flaking](#flaking)

- [colour system](#colour-system)
    - [eye](#eye)
    - [Munsell](#munsell)
    - [CIELAB](#cielab)

- [contributorType](#contributortype)
    - [Other (contributorType)](#other-(contributortype))
    - [WorkPackageLeader](#workpackageleader)
    - [Translator](#translator)
    - [Supervisor](#supervisor)
    - [Sponsor](#sponsor)
    - [RightsHolder](#rightsholder)
    - [ResearchGroup](#researchgroup)
    - [Researcher](#researcher)
    - [RelatedPerson](#relatedperson)
    - [RegistrationAuthority](#registrationauthority)
    - [RegistrationAgency](#registrationagency)
    - [ProjectMember](#projectmember)
    - [ProjectManager](#projectmanager)
    - [ProjectLeader](#projectleader)
    - [Producer](#producer)
    - [HostingInstitution](#hostinginstitution)
    - [Editor](#editor)
    - [Distributor](#distributor)
    - [DataManager](#datamanager)
    - [DataCurator](#datacurator)
    - [DataCollector](#datacollector)
    - [ContactPerson](#contactperson)

- [sample access](#sample-access)
    - [unknown](#unknown)
    - [accessible](#accessible)
    - [policy](#policy)
    - [inaccessible](#inaccessible)
    - [destroyed](#destroyed)
    - [lost](#lost)

- [date type](#date-type)
    - [archaeological](#archaeological)
    - [geological](#geological)

- [dating technique](#dating-technique)
    - [absolute dating](#absolute-dating)
        - [dendrochronology](#dendrochronology)
        - [lichenometry](#lichenometry)
        - [luminescence dating](#luminescence-dating)
            - [optically stimulated luminescence dating](#optically-stimulated-luminescence-dating)
            - [thermoluminescence dating](#thermoluminescence-dating)
        - [radiometric dating](#radiometric-dating)
            - [fission track dating](#fission-track-dating)
            - [potassium-argon dating](#potassium-argon-dating)
                - [argon-argon dating](#argon-argon-dating)
            - [uranium-series dating](#uranium-series-dating)
            - [radiocarbon dating](#radiocarbon-dating)
            - [uranium-lead dating](#uranium-lead-dating)
            - [rubidium-strontium dating](#rubidium-strontium-dating)
            - [lutetium-hafnium dating](#lutetium-hafnium-dating)
            - [samarium-neodymium dating](#samarium-neodymium-dating)
            - [rhenium-osmium dating](#rhenium-osmium-dating)
            - [lead-lead dating](#lead-lead-dating)
        - [rehydroxylation dating](#rehydroxylation-dating)
    - [relative dating](#relative-dating)
        - [seriation](#seriation)
        - [archaeomagnetic dating](#archaeomagnetic-dating)
        - [biostratigraphy](#biostratigraphy)
        - [tephrochronology](#tephrochronology)

- [analytical uncertainty](#analytical-uncertainty)
    - [standard error](#standard-error)
    - [standard deviation](#standard-deviation)

- [identifier](#identifier)
    - [w3id](#w3id)
    - [URN](#urn)
    - [URL](#url)
    - [UPC](#upc)
    - [SWHID](#swhid)
    - [RRID](#rrid)
    - [RAiD](#raid)
    - [PURL](#purl)
    - [PMID](#pmid)
    - [LSID](#lsid)
    - [LISSN](#lissn)
    - [ISTC](#istc)
    - [ISSN](#issn)
    - [ISBN](#isbn)
    - [IGSN](#igsn)
    - [Handle](#handle)
    - [EISSN](#eissn)
    - [EAN13](#ean13)
    - [DOI](#doi)
    - [CSTR](#cstr)
    - [bibcode](#bibcode)
    - [ArXiv](#arxiv)
    - [ARK](#ark)

- [relationType](#relationtype)
    - [HasTranslation](#hastranslation)
    - [IsTranslationOf](#istranslationof)
    - [Collects](#collects)
    - [IsCollectedBy](#iscollectedby)
    - [IsObsoletedBy](#isobsoletedby)
    - [Obsoletes](#obsoletes)
    - [Requires](#requires)
    - [IsRequiredBy](#isrequiredby)
    - [IsSourceOf](#issourceof)
    - [IsDerivedFrom](#isderivedfrom)
    - [Reviews](#reviews)
    - [IsReviewedBy](#isreviewedby)
    - [IsIdenticalTo](#isidenticalto)
    - [IsOriginalFormOf](#isoriginalformof)
    - [IsVariantFormOf](#isvariantformof)
    - [Compiles](#compiles)
    - [IsCompiledBy](#iscompiledby)
    - [Documents](#documents)
    - [IsDocumentedBy](#isdocumentedby)
    - [References](#references)
    - [IsReferencedBy](#isreferencedby)
    - [IsPublishedIn](#ispublishedin)
    - [HasPart](#haspart)
    - [IsPartOf](#ispartof)
    - [IsPreviousVersionOf](#ispreviousversionof)
    - [IsNewVersionOf](#isnewversionof)
    - [IsVersionOf](#isversionof)
    - [HasVersion](#hasversion)
    - [IsMetadataFor](#ismetadatafor)
    - [HasMetadata](#hasmetadata)
    - [IsDescribedBy](#isdescribedby)
    - [Describes](#describes)
    - [Continues](#continues)
    - [IsContinuedBy](#iscontinuedby)
    - [IsSupplementedBy](#issupplementedby)
    - [IsSupplementTo](#issupplementto)
    - [Cites](#cites)
    - [IsCitedBy](#iscitedby)

- [information source](#information-source)
    - [original](#original)
    - [calculated](#calculated)

- [lead isotope ratios](#lead-isotope-ratios)
    - [206Pb/204Pb](#206pb-204pb)
    - [207Pb/204Pb](#207pb-204pb)
    - [208Pb/204Pb](#208pb-204pb)
    - [204Pb/206Pb](#204pb-206pb)
    - [207Pb/206Pb](#207pb-206pb)
    - [208Pb/206Pb](#208pb-206pb)
    - [207Pb/208Pb](#207pb-208pb)
    - [206Pb/208Pb](#206pb-208pb)

- [resourceType](#resourcetype)
    - [Other (resourceType)](#other-(resourcetype))
    - [Workflow](#workflow)
    - [Text](#text)
    - [StudyRegistration](#studyregistration)
    - [Standard](#standard)
    - [Sound](#sound)
    - [Software](#software)
    - [Service](#service)
    - [Report](#report)
    - [Project](#project)
    - [Preprint](#preprint)
    - [PhysicalObject](#physicalobject)
    - [PeerReview](#peerreview)
    - [OutputManagementPlan](#outputmanagementplan)
    - [Model](#model)
    - [JournalArticle](#journalarticle)
    - [Journal](#journal)
    - [InteractiveResource](#interactiveresource)
    - [Instrument](#instrument)
    - [Image](#image)
    - [Event](#event)
    - [Dissertation](#dissertation)
    - [Dataset](#dataset)
    - [DataPaper](#datapaper)
    - [ConferenceProceeding](#conferenceproceeding)
    - [ConferencePaper](#conferencepaper)
    - [ComputationalNotebook](#computationalnotebook)
    - [Collection](#collection)
    - [BookChapter](#bookchapter)
    - [Book](#book)
    - [Award](#award)
    - [Audiovisual](#audiovisual)

- [registry](#registry)
    - [gazetteer](#gazetteer)
        - [WHG](#whg)
        - [TGN](#tgn)
        - [Geonames](#geonames)
        - [Pleiades](#pleiades)
        - [iDAI.gazetteer](#idai.gazetteer)
        - [PeriodO](#periodo)
    - [GND](#gnd)
    - [ORCID](#orcid)
    - [iDAI ChronOntology](#idai-chronontology)

- [unit of measurement](#unit-of-measurement)
    - [distance](#distance)
        - [m](#m)
        - [mm](#mm)
        - [cm](#cm)
        - [km](#km)
    - [mass](#mass)
        - [µg](#µg)
        - [kg](#kg)
        - [mg](#mg)
        - [g](#g)
    - [electric potential](#electric-potential)
        - [V](#v)
        - [mV](#mv)
    - [cps](#cps)
    - [time](#time)
        - [Ma](#ma)
        - [a](#a)
    - [concentration](#concentration)
        - [%](#%)
        - [at%](#at%)
        - [wt%](#wt%)
        - [µg/kg](#µg-kg)
        - [µg/g](#µg-g)
        - [oxide%](#oxide%)

- [mineral texture](#mineral-texture)
    - [intergrowth](#intergrowth)
        - [ophitic](#ophitic)
        - [intersertal](#intersertal)
        - [interstitial](#interstitial)
        - [interlocked](#interlocked)
        - [symplectitic](#symplectitic)
            - [myrmekitic](#myrmekitic)
        - [poikiloblastic](#poikiloblastic)
        - [disseminated](#disseminated)
        - [rimmed](#rimmed)
        - [amoeboid](#amoeboid)
        - [cellular (intergrowth)](#cellular-(intergrowth))
        - [atoll-like](#atoll-like)
    - [replacement](#replacement)
        - [filiform](#filiform)
        - [graphic](#graphic)
        - [cellular (replacement)](#cellular-(replacement))
        - [island-shaped](#island-shaped)
        - [boxwork](#boxwork)
        - [skeleton-shaped](#skeleton-shaped)
        - [cusp-and-caries](#cusp-and-caries)
        - [lacuna](#lacuna)
        - [lamellar](#lamellar)
        - [zonal](#zonal)
        - [atoll-like (replacement)](#atoll-like-(replacement))
        - [cement-shaped](#cement-shaped)
        - [pseudomorph](#pseudomorph)
    - [deformation-related](#deformation-related)
        - [cataclastic](#cataclastic)
        - [brecciated](#brecciated)
        - [broken](#broken)
        - [translation lamellae](#translation-lamellae)
        - [pressure twins](#pressure-twins)
        - [bending](#bending)
        - [planar alignment](#planar-alignment)

- [chemical substance](#chemical-substance)
    - [oxide](#oxide)
        - [silver oxide](#silver-oxide)
        - [silver(II) oxide](#silver(ii)-oxide)
        - [aluminium oxide](#aluminium-oxide)
        - [oxidoaluminium](#oxidoaluminium)
        - [arsenic trioxide](#arsenic-trioxide)
        - [arsenic pentoxide](#arsenic-pentoxide)
        - [gold sesquioxide](#gold-sesquioxide)
        - [diboron trioxide](#diboron-trioxide)
        - [barium oxide](#barium-oxide)
        - [beryllium oxide](#beryllium-oxide)
        - [bismuth pentoxide](#bismuth-pentoxide)
        - [dicarbon monoxide](#dicarbon-monoxide)
        - [calcium oxide](#calcium-oxide)
        - [cadmium oxide](#cadmium-oxide)
        - [cerium(IV) oxide](#cerium(iv)-oxide)
        - [dichlorine monoxide](#dichlorine-monoxide)
        - [chlorine heptoxide](#chlorine-heptoxide)
        - [chlorine dioxide](#chlorine-dioxide)
        - [carbon monoxide](#carbon-monoxide)
        - [carbon dioxide](#carbon-dioxide)
        - [carbon trioxide](#carbon-trioxide)
        - [cobalt(II) oxide](#cobalt(ii)-oxide)
        - [dichromium trioxide](#dichromium-trioxide)
        - [chromium(II) oxide](#chromium(ii)-oxide)
        - [chromium trioxide](#chromium-trioxide)
        - [copper(I) oxide](#copper(i)-oxide)
        - [copper(II) oxide](#copper(ii)-oxide)
        - [erbium(III) oxide](#erbium(iii)-oxide)
        - [iron(III) oxide](#iron(iii)-oxide)
        - [iron(II) oxide](#iron(ii)-oxide)
        - [gallium(III) oxide](#gallium(iii)-oxide)
        - [gadolinium(III) oxide](#gadolinium(iii)-oxide)
        - [germanium dioxide](#germanium-dioxide)
        - [water](#water)
        - [hafnium(IV) oxide](#hafnium(iv)-oxide)
        - [mercury(II) oxide](#mercury(ii)-oxide)
        - [holmium(III) oxide](#holmium(iii)-oxide)
        - [indium oxide](#indium-oxide)
        - [potassium oxide](#potassium-oxide)
        - [lanthanum(III) oxide](#lanthanum(iii)-oxide)
        - [lithium oxide](#lithium-oxide)
        - [lutetium(III) oxide](#lutetium(iii)-oxide)
        - [magnesium oxide](#magnesium-oxide)
        - [manganese heptoxide](#manganese-heptoxide)
        - [manganese(II) oxide](#manganese(ii)-oxide)
        - [manganese dioxide](#manganese-dioxide)
        - [molybdenum trioxide](#molybdenum-trioxide)
        - [dinitrogen trioxide](#dinitrogen-trioxide)
        - [dinitrogen tetroxide](#dinitrogen-tetroxide)
        - [dinitrogen pentoxide](#dinitrogen-pentoxide)
        - [sodium oxide](#sodium-oxide)
        - [nickel(III) oxide](#nickel(iii)-oxide)
        - [nickel(II) oxide](#nickel(ii)-oxide)
        - [nitric oxide](#nitric-oxide)
        - [nitrogen dioxide](#nitrogen-dioxide)
        - [tetraoxygen](#tetraoxygen)
        - [oxygen difluoride](#oxygen-difluoride)
        - [osmium tetroxide](#osmium-tetroxide)
        - [phosphorus pentoxide](#phosphorus-pentoxide)
        - [tetraphosphorus hexaoxide](#tetraphosphorus-hexaoxide)
        - [lead(II) oxide](#lead(ii)-oxide)
        - [lead dioxide](#lead-dioxide)
        - [palladium(II) oxide](#palladium(ii)-oxide)
        - [promethium(III) oxide](#promethium(iii)-oxide)
        - [plutonium(IV) oxide](#plutonium(iv)-oxide)
        - [rubidium oxide](#rubidium-oxide)
        - [rhenium(VII) oxide](#rhenium(vii)-oxide)
        - [rhenium trioxide](#rhenium-trioxide)
        - [rhodium(III) oxide](#rhodium(iii)-oxide)
        - [ruthenium(IV) oxide](#ruthenium(iv)-oxide)
        - [ruthenium tetroxide](#ruthenium-tetroxide)
        - [antimony trioxide](#antimony-trioxide)
        - [antimony pentoxide](#antimony-pentoxide)
        - [scandium oxide](#scandium-oxide)
        - [selenium dioxide](#selenium-dioxide)
        - [selenium trioxide](#selenium-trioxide)
        - [silicon dioxide](#silicon-dioxide)
        - [samarium(III) oxide](#samarium(iii)-oxide)
        - [tin(II) oxide](#tin(ii)-oxide)
        - [tin(IV) oxide](#tin(iv)-oxide)
        - [sulfur dioxide](#sulfur-dioxide)
        - [sulfur trioxide](#sulfur-trioxide)
        - [strontium oxide](#strontium-oxide)
        - [tantalum pentoxide](#tantalum-pentoxide)
        - [terbium(III) oxide](#terbium(iii)-oxide)
        - [tellurium dioxide](#tellurium-dioxide)
        - [tellurium trioxide](#tellurium-trioxide)
        - [thorium dioxide](#thorium-dioxide)
        - [titanium(III) oxide](#titanium(iii)-oxide)
        - [titanium dioxide](#titanium-dioxide)
        - [titanium dioxide](#titanium-dioxide)
        - [thallium(I) oxide](#thallium(i)-oxide)
        - [thallium(III) oxide](#thallium(iii)-oxide)
        - [thulium(III) oxide](#thulium(iii)-oxide)
        - [uranium dioxide](#uranium-dioxide)
        - [uranium trioxide](#uranium-trioxide)
        - [vanadium(III) oxide](#vanadium(iii)-oxide)
        - [vanadium(V) oxide](#vanadium(v)-oxide)
        - [vanadium(II) oxide](#vanadium(ii)-oxide)
        - [vanadium(IV) oxide](#vanadium(iv)-oxide)
        - [tungsten(III) oxide](#tungsten(iii)-oxide)
        - [tungsten(IV) oxide](#tungsten(iv)-oxide)
        - [tungsten trioxide](#tungsten-trioxide)
        - [xenon trioxide](#xenon-trioxide)
        - [xenon tetroxide](#xenon-tetroxide)
        - [yttrium oxide](#yttrium-oxide)
        - [ytterbium(III) oxide](#ytterbium(iii)-oxide)
        - [zinc oxide](#zinc-oxide)
        - [zirconium dioxide](#zirconium-dioxide)
        - [bismuth(III) oxide](#bismuth(iii)-oxide)
        - [chromium(IV) oxide](#chromium(iv)-oxide)
    - [chemical element](#chemical-element)
        - [hydrogène](#hydrogène)
        - [carbone](#carbone)
        - [azote](#azote)
        - [oxygène](#oxygène)
        - [phosphore](#phosphore)
        - [soufre](#soufre)
        - [sélénium](#sélénium)
        - [hélium](#hélium)
        - [lithium](#lithium)
        - [béryllium](#béryllium)
        - [sodium](#sodium)
        - [magnésium](#magnésium)
        - [potassium](#potassium)
        - [calcium](#calcium)
        - [rubidium](#rubidium)
        - [strontium](#strontium)
        - [césium](#césium)
        - [baryum](#baryum)
        - [francium](#francium)
        - [radium](#radium)
        - [bore](#bore)
        - [fluor](#fluor)
        - [néon](#néon)
        - [aluminium](#aluminium)
        - [silicium](#silicium)
        - [chlore](#chlore)
        - [argon](#argon)
        - [gallium](#gallium)
        - [germanium](#germanium)
        - [arsenic](#arsenic)
        - [brome](#brome)
        - [krypton](#krypton)
        - [indium](#indium)
        - [étain](#étain)
        - [antimoine](#antimoine)
        - [tellure](#tellure)
        - [iode](#iode)
        - [xénon](#xénon)
        - [thallium](#thallium)
        - [plomb](#plomb)
        - [bismuth](#bismuth)
        - [polonium](#polonium)
        - [astate](#astate)
        - [radon](#radon)
        - [oganesson](#oganesson)
        - [nihonium](#nihonium)
        - [flérovium](#flérovium)
        - [moscovium](#moscovium)
        - [livermorium](#livermorium)
        - [tennesse](#tennesse)
        - [scandium](#scandium)
        - [titane](#titane)
        - [vanadium](#vanadium)
        - [chrome](#chrome)
        - [manganèse](#manganèse)
        - [fer](#fer)
        - [cobalt](#cobalt)
        - [nickel](#nickel)
        - [cuivre](#cuivre)
        - [zinc](#zinc)
        - [yttrium](#yttrium)
        - [zirconium](#zirconium)
        - [niobium](#niobium)
        - [molybdène](#molybdène)
        - [technétium](#technétium)
        - [argent](#argent)
        - [cadmium](#cadmium)
        - [hafnium](#hafnium)
        - [tantale](#tantale)
        - [tungstène](#tungstène)
        - [rhénium](#rhénium)
        - [or](#or)
        - [mercure](#mercure)
        - [rutherfordium](#rutherfordium)
        - [dubnium](#dubnium)
        - [seaborgium](#seaborgium)
        - [bohrium](#bohrium)
        - [hassium](#hassium)
        - [ruthénium](#ruthénium)
        - [rhodium](#rhodium)
        - [palladium](#palladium)
        - [osmium](#osmium)
        - [iridium](#iridium)
        - [platine](#platine)
        - [meitnérium](#meitnérium)
        - [darmstadtium](#darmstadtium)
        - [roentgenium](#roentgenium)
        - [copernicium](#copernicium)
        - [lanthane](#lanthane)
        - [cérium](#cérium)
        - [praséodyme](#praséodyme)
        - [néodyme](#néodyme)
        - [prométhium](#prométhium)
        - [samarium](#samarium)
        - [europium](#europium)
        - [gadolinium](#gadolinium)
        - [terbium](#terbium)
        - [dysprosium](#dysprosium)
        - [holmium](#holmium)
        - [erbium](#erbium)
        - [thulium](#thulium)
        - [ytterbium](#ytterbium)
        - [lutécium](#lutécium)
        - [thorium](#thorium)
        - [protactinium](#protactinium)
        - [uranium](#uranium)
        - [neptunium](#neptunium)
        - [plutonium](#plutonium)
        - [américium](#américium)
        - [curium](#curium)
        - [berkélium](#berkélium)
        - [californium](#californium)
        - [einsteinium](#einsteinium)
        - [fermium](#fermium)
        - [mendélévium](#mendélévium)
        - [nobélium](#nobélium)
        - [actinium](#actinium)
        - [lawrencium](#lawrencium)

- [nuclide](#nuclide)
    - [silicon-30](#silicon-30)
    - [sulfur-33](#sulfur-33)
    - [carbon-12](#carbon-12)
    - [tungsten-184](#tungsten-184)
    - [ytterbium-168](#ytterbium-168)
    - [ytterbium-171](#ytterbium-171)
    - [ytterbium-170](#ytterbium-170)
    - [ytterbium-172](#ytterbium-172)
    - [ytterbium-173](#ytterbium-173)
    - [ytterbium-174](#ytterbium-174)
    - [ytterbium-176](#ytterbium-176)
    - [iridium-191](#iridium-191)
    - [iridium-193](#iridium-193)
    - [platinum-194](#platinum-194)
    - [platinum-192](#platinum-192)
    - [platinum-196](#platinum-196)
    - [platinum-195](#platinum-195)
    - [platinum-198](#platinum-198)
    - [lutetium-175](#lutetium-175)
    - [tin-122](#tin-122)
    - [erbium-162](#erbium-162)
    - [erbium-164](#erbium-164)
    - [erbium-168](#erbium-168)
    - [erbium-166](#erbium-166)
    - [erbium-167](#erbium-167)
    - [erbium-170](#erbium-170)
    - [samarium-150](#samarium-150)
    - [antimony-121](#antimony-121)
    - [argon-40](#argon-40)
    - [protium](#protium)
    - [holmium-165](#holmium-165)
    - [potassium-39](#potassium-39)
    - [iron-57](#iron-57)
    - [thulium-169](#thulium-169)
    - [selenium-78](#selenium-78)
    - [europium-153](#europium-153)
    - [dysprosium-156](#dysprosium-156)
    - [dysprosium-158](#dysprosium-158)
    - [dysprosium-160](#dysprosium-160)
    - [dysprosium-163](#dysprosium-163)
    - [dysprosium-164](#dysprosium-164)
    - [dysprosium-161](#dysprosium-161)
    - [dysprosium-162](#dysprosium-162)
    - [magnesium-26](#magnesium-26)
    - [molybdenum-96](#molybdenum-96)
    - [molybdenum-94](#molybdenum-94)
    - [lithium-6](#lithium-6)
    - [lithium-7](#lithium-7)
    - [carbon-13](#carbon-13)
    - [manganese-55](#manganese-55)
    - [cadmium-112](#cadmium-112)
    - [thallium-203](#thallium-203)
    - [mercury-196](#mercury-196)
    - [mercury-199](#mercury-199)
    - [mercury-198](#mercury-198)
    - [mercury-202](#mercury-202)
    - [mercury-200](#mercury-200)
    - [mercury-201](#mercury-201)
    - [mercury-204](#mercury-204)
    - [samarium-149](#samarium-149)
    - [argon-36](#argon-36)
    - [deuterium](#deuterium)
    - [gold-197](#gold-197)
    - [germanium-72](#germanium-72)
    - [vanadium-51](#vanadium-51)
    - [samarium-144](#samarium-144)
    - [krypton-83](#krypton-83)
    - [hafnium-177](#hafnium-177)
    - [hafnium-176](#hafnium-176)
    - [hafnium-179](#hafnium-179)
    - [hafnium-178](#hafnium-178)
    - [hafnium-180](#hafnium-180)
    - [chromium-53](#chromium-53)
    - [osmium-189](#osmium-189)
    - [osmium-187](#osmium-187)
    - [osmium-188](#osmium-188)
    - [osmium-190](#osmium-190)
    - [osmium-192](#osmium-192)
    - [molybdenum-98](#molybdenum-98)
    - [lead-208](#lead-208)
    - [iron-56](#iron-56)
    - [helium-4](#helium-4)
    - [sulfur-34](#sulfur-34)
    - [ruthenium-101](#ruthenium-101)
    - [xenon-128](#xenon-128)
    - [neodymium-146](#neodymium-146)
    - [tin-116](#tin-116)
    - [nitrogen-14](#nitrogen-14)
    - [tellurium-126](#tellurium-126)
    - [lead-206](#lead-206)
    - [lead-207](#lead-207)
    - [Tantalum-180](#tantalum-180)
    - [tantalum-181](#tantalum-181)
    - [thallium-205](#thallium-205)
    - [nickel-64](#nickel-64)
    - [silver-109](#silver-109)
    - [nitrogen-15](#nitrogen-15)
    - [tin-115](#tin-115)
    - [chlorine-37](#chlorine-37)
    - [strontium-87](#strontium-87)
    - [ruthenium-102](#ruthenium-102)
    - [arsenic-75](#arsenic-75)
    - [ruthenium-99](#ruthenium-99)
    - [xenon-126](#xenon-126)
    - [molybdenum-95](#molybdenum-95)
    - [tellurium-124](#tellurium-124)
    - [molybdenum-92](#molybdenum-92)
    - [tin-117](#tin-117)
    - [tungsten-182](#tungsten-182)
    - [scandium-45](#scandium-45)
    - [rhenium-185](#rhenium-185)
    - [neon-20](#neon-20)
    - [neon-22](#neon-22)
    - [palladium-104](#palladium-104)
    - [nickel-58](#nickel-58)
    - [ruthenium-100](#ruthenium-100)
    - [krypton-86](#krypton-86)
    - [molybdenum-97](#molybdenum-97)
    - [selenium-77](#selenium-77)
    - [oxygen-16](#oxygen-16)
    - [boron-10](#boron-10)
    - [selenium-76](#selenium-76)
    - [tellurium-120](#tellurium-120)
    - [palladium-105](#palladium-105)
    - [sulfur-36](#sulfur-36)
    - [copper-65](#copper-65)
    - [boron-11](#boron-11)
    - [nickel-61](#nickel-61)
    - [sulfur-32](#sulfur-32)
    - [ruthenium-96](#ruthenium-96)
    - [titanium-47](#titanium-47)
    - [neon-21](#neon-21)
    - [barium-138](#barium-138)
    - [gadolinium-155](#gadolinium-155)
    - [antimony-123](#antimony-123)
    - [neodymium-143](#neodymium-143)
    - [bromine-79](#bromine-79)
    - [tin-119](#tin-119)
    - [potassium-41](#potassium-41)
    - [germanium-70](#germanium-70)
    - [barium-136](#barium-136)
    - [indium-113](#indium-113)
    - [gallium-71](#gallium-71)
    - [palladium-106](#palladium-106)
    - [magnesium-25](#magnesium-25)
    - [neodymium-145](#neodymium-145)
    - [fluorine-19](#fluorine-19)
    - [titanium-48](#titanium-48)
    - [tellurium-125](#tellurium-125)
    - [barium-134](#barium-134)
    - [cadmium-110](#cadmium-110)
    - [rubidium-85](#rubidium-85)
    - [chlorine-35](#chlorine-35)
    - [niobium-93](#niobium-93)
    - [tin-114](#tin-114)
    - [ruthenium-98](#ruthenium-98)
    - [titanium-50](#titanium-50)
    - [gadolinium-158](#gadolinium-158)
    - [nickel-62](#nickel-62)
    - [germanium-73](#germanium-73)
    - [chromium-54](#chromium-54)
    - [palladium-110](#palladium-110)
    - [calcium-44](#calcium-44)
    - [xenon-130](#xenon-130)
    - [strontium-84](#strontium-84)
    - [praseodymium-141](#praseodymium-141)
    - [sodium-23](#sodium-23)
    - [yttrium-89](#yttrium-89)
    - [krypton-80](#krypton-80)
    - [titanium-46](#titanium-46)
    - [silicon-28](#silicon-28)
    - [titanium-49](#titanium-49)
    - [krypton-84](#krypton-84)
    - [magnesium-24](#magnesium-24)
    - [lanthanum-139](#lanthanum-139)
    - [krypton-82](#krypton-82)
    - [palladium-102](#palladium-102)
    - [terbium-159](#terbium-159)
    - [bromine-81](#bromine-81)
    - [iron-58](#iron-58)
    - [caesium-133](#caesium-133)
    - [zirconium-92](#zirconium-92)
    - [calcium-42](#calcium-42)
    - [xenon-132](#xenon-132)
    - [germanium-76](#germanium-76)
    - [selenium-74](#selenium-74)
    - [barium-130](#barium-130)
    - [zirconium-90](#zirconium-90)
    - [xenon-131](#xenon-131)
    - [samarium-154](#samarium-154)
    - [ruthenium-104](#ruthenium-104)
    - [palladium-108](#palladium-108)
    - [gadolinium-157](#gadolinium-157)
    - [strontium-86](#strontium-86)
    - [iron-54](#iron-54)
    - [germanium-74](#germanium-74)
    - [phosphorus-31](#phosphorus-31)
    - [zinc-67](#zinc-67)
    - [selenium-80](#selenium-80)
    - [samarium-152](#samarium-152)
    - [nickel-60](#nickel-60)
    - [xenon-129](#xenon-129)
    - [calcium-43](#calcium-43)
    - [argon-38](#argon-38)
    - [tin-120](#tin-120)
    - [cadmium-111](#cadmium-111)
    - [zirconium-91](#zirconium-91)
    - [gadolinium-154](#gadolinium-154)
    - [tin-118](#tin-118)
    - [beryllium-9](#beryllium-9)
    - [aluminium-27](#aluminium-27)
    - [rhodium-103](#rhodium-103)
    - [cerium-140](#cerium-140)
    - [selenium-82](#selenium-82)
    - [strontium-88](#strontium-88)
    - [tellurium-122](#tellurium-122)
    - [helium-3](#helium-3)
    - [iodine-127](#iodine-127)
    - [silver-107](#silver-107)
    - [chromium-52](#chromium-52)
    - [cobalt-59](#cobalt-59)
    - [gallium-69](#gallium-69)
    - [neodymium-148](#neodymium-148)
    - [silicon-29](#silicon-29)
    - [oxygen-17](#oxygen-17)
    - [zirconium-94](#zirconium-94)
    - [barium-137](#barium-137)
    - [copper-63](#copper-63)
    - [neodymium-142](#neodymium-142)
    - [zinc-66](#zinc-66)
    - [oxygen-18](#oxygen-18)
    - [barium-135](#barium-135)
    - [zinc-68](#zinc-68)
    - [gadolinium-156](#gadolinium-156)

- [production process](#production-process)
    - [unknown](#unknown)
    - [other](#other)
    - [absorption](#absorption)
    - [weathering](#weathering)
    - [acid reaction](#acid-reaction)
    - [leaching](#leaching)
    - [grinding](#grinding)
    - [heating](#heating)

- [pigment name](#pigment-name)
    - [bassanite](#bassanite)
    - [synthetic lead carbonate](#synthetic-lead-carbonate)
    - [lead white](#lead-white)
    - [lead carbonate hydroxide](#lead-carbonate-hydroxide)
    - [lead sulfate (other types)](#lead-sulfate-(other-types))
    - [cassiterite](#cassiterite)
    - [rutile](#rutile)
    - [zinc sulfide](#zinc-sulfide)
    - [zinc sulfate heptahydrate](#zinc-sulfate-heptahydrate)
    - [quartz](#quartz)
    - [diatomite](#diatomite)
    - [glass](#glass)
    - [pumice](#pumice)
    - [talc](#talc)
    - [palygorskite](#palygorskite)
    - [kaolinite](#kaolinite)
    - [nacrite](#nacrite)
    - [montmorillonite](#montmorillonite)
    - [nontronite](#nontronite)
    - [vermiculite group clay minerals](#vermiculite-group-clay-minerals)
    - [serpentine group clay minerals](#serpentine-group-clay-minerals)
    - [starch](#starch)
    - [red lake pigments](#red-lake-pigments)
    - [yellow lake pigments](#yellow-lake-pigments)
    - [red ochre](#red-ochre)
    - [yellow ochre](#yellow-ochre)
    - [brown ochre and burnt sienna](#brown-ochre-and-burnt-sienna)
    - [umbers and wads](#umbers-and-wads)
    - [green earths](#green-earths)
    - [feldspar minerals](#feldspar-minerals)
    - [feldspathoid minerals](#feldspathoid-minerals)
    - [mica group minerals](#mica-group-minerals)
    - [asbestiform minerals](#asbestiform-minerals)
    - [Maya blue](#maya-blue)
    - [manganese oxides](#manganese-oxides)
    - [pyrite](#pyrite)
    - [magnetite](#magnetite)
    - [bismuthinite](#bismuthinite)
    - [stibnite](#stibnite)
    - [galena](#galena)
    - [plattnerite](#plattnerite)
    - [copper(II) oxide](#copper(ii)-oxide)
    - [coal](#coal)
    - [asphalt](#asphalt)
    - [Vandyke brown](#vandyke-brown)
    - [sepia](#sepia)
    - [flame carbons](#flame-carbons)
    - [bone and yeast cokes](#bone-and-yeast-cokes)
    - [chars](#chars)
    - [graphite](#graphite)
    - [copper hexacyanoferrates](#copper-hexacyanoferrates)
    - [bismuth](#bismuth)
    - [dragon’s blood](#dragon’s-blood)
    - [turmeric](#turmeric)
    - [Indian yellow](#indian-yellow)
    - [gamboge](#gamboge)
    - [mosaic gold](#mosaic-gold)
    - [sulfur](#sulfur)
    - [cobalt yellow](#cobalt-yellow)
    - [metacinnabar](#metacinnabar)
    - [vermillion](#vermillion)
    - [cinnabar](#cinnabar)
    - [cuprite](#cuprite)
    - [red lead](#red-lead)
    - [lead chromate sulfate](#lead-chromate-sulfate)
    - [lead chromate oxide](#lead-chromate-oxide)
    - [chrome yellow](#chrome-yellow)
    - [lead tin silicon oxide](#lead-tin-silicon-oxide)
    - [lead tin oxide](#lead-tin-oxide)
    - [lead antimony zinc oxide](#lead-antimony-zinc-oxide)
    - [lead antimony tin oxide](#lead-antimony-tin-oxide)
    - [Naples yellow](#naples-yellow)
    - [litharge](#litharge)
    - [massicot](#massicot)
    - [Turner's yellow](#turner's-yellow)
    - [natrojarosite](#natrojarosite)
    - [jarosite](#jarosite)
    - [lepidocrocite](#lepidocrocite)
    - [hematite](#hematite)
    - [goethite](#goethite)
    - [pararealgar](#pararealgar)
    - [realgar](#realgar)
    - [orpiment](#orpiment)
    - [antimony(III) sulfide](#antimony(iii)-sulfide)
    - [indigo](#indigo)
    - [prussian blue](#prussian-blue)
    - [chromium phosphate hexahydrate](#chromium-phosphate-hexahydrate)
    - [chromium oxide hydrate](#chromium-oxide-hydrate)
    - [chromium(III) oxide](#chromium(iii)-oxide)
    - [glaucophane](#glaucophane)
    - [chlorite group minerals](#chlorite-group-minerals)
    - [chrysocolla](#chrysocolla)
    - [glauconite](#glauconite)
    - [celadonite](#celadonite)
    - [aerinite](#aerinite)
    - [copper citrate](#copper-citrate)
    - [gypsum](#gypsum)
    - [carbonate hydroxylapatite](#carbonate-hydroxylapatite)
    - [cerussite](#cerussite)
    - [lead chloride hydroxide](#lead-chloride-hydroxide)
    - [anglesite](#anglesite)
    - [magnesite](#magnesite)
    - [anatase](#anatase)
    - [zinc(II) oxide](#zinc(ii)-oxide)
    - [anhydrite](#anhydrite)
    - [dolomite](#dolomite)
    - [oyster shell](#oyster-shell)
    - [eggshell](#eggshell)
    - [coral](#coral)
    - [chalk](#chalk)
    - [calcium carbonate](#calcium-carbonate)
    - [aragonite](#aragonite)
    - [baryte](#baryte)
    - [barium carbonate](#barium-carbonate)
    - [arsenic(III) oxide](#arsenic(iii)-oxide)
    - [aluminium hydroxide](#aluminium-hydroxide)
    - [aluminium oxide](#aluminium-oxide)
    - [copper(II) acetate h](#copper(ii)-acetate-h)
    - [copper(II) acetate f](#copper(ii)-acetate-f)
    - [copper(II) acetate d](#copper(ii)-acetate-d)
    - [copper(II) acetate b](#copper(ii)-acetate-b)
    - [copper(II) acetate a](#copper(ii)-acetate-a)
    - [copper acetate arsenite](#copper-acetate-arsenite)
    - [copper arsenite group](#copper-arsenite-group)
    - [antlerite](#antlerite)
    - [brochantite](#brochantite)
    - [pseudomalachite](#pseudomalachite)
    - [paratacamite](#paratacamite)
    - [botallackite](#botallackite)
    - [atacamite](#atacamite)
    - [copper(II) hydroxide](#copper(ii)-hydroxide)
    - [chalconatronite](#chalconatronite)
    - [malachite](#malachite)
    - [azurite](#azurite)
    - [artificial ultramarine](#artificial-ultramarine)
    - [lazurite](#lazurite)
    - [smalt](#smalt)
    - [cobalt zinc oxide](#cobalt-zinc-oxide)
    - [cobalt tin oxide](#cobalt-tin-oxide)
    - [cobalt aluminium oxide](#cobalt-aluminium-oxide)
    - [barium manganese oxide](#barium-manganese-oxide)
    - [Egyptian green](#egyptian-green)
    - [Egyptian blue](#egyptian-blue)
    - [Han purple](#han-purple)
    - [Han blue](#han-blue)
    - [purpurite](#purpurite)
    - [synthetic manganese phosphate](#synthetic-manganese-phosphate)
    - [magnesium cobalt arsenate](#magnesium-cobalt-arsenate)
    - [lithium cobalt phosphate](#lithium-cobalt-phosphate)
    - [ammonium cobalt phosphate hydrate](#ammonium-cobalt-phosphate-hydrate)
    - [cobalt phosphate hydrate](#cobalt-phosphate-hydrate)
    - [cobalt phosphate](#cobalt-phosphate)
    - [erythrite](#erythrite)
    - [fluorite](#fluorite)
    - [vivianite](#vivianite)

**Concepts**

[]{#site-type}

##  site type
- **Definition**: Set of categories to characterise the use of a site
by humans or its geological relevance.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Concept URI:** http://vocab.terralid.org#c_cad56412

[]{#anthropogenic-site}

###  anthropogenic site
- **Definition**: The site is characterised by traces of human
activity without any further specification.
- **Child of**:
  - [`site type`](#site-type)
- **Concept URI:** http://vocab.terralid.org#c_241d96ca

[]{#built-structures}

####  built structures
- **Definition**: The parts of the environment that was constructed by
humans.
- **Child of**:
  - [`environnement bâti`](#environnement-bâti)
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300264550 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_4327d421

[]{#camp}

#####  camp
- **Definition**: A temporary settlement, usually of small size and
with non-permanent architecture.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - http://vocab.getty.edu/aat/300257104 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a4821cf4

[]{#settlement}

#####  settlement
- **Definition**: Generalised term for all types of inhabited places
permanent buildings.
- **Child of**:
  - [`built structures`](#built-structures)
- **Alternate labels:**
  - village, 
  - city, 
  - town, 
- **Matches:**
  - https://www.wikidata.org/wiki/Q486972 (exactMatch)
  - http://vocab.getty.edu/aat/300008389 (narrowMatch)
  - http://vocab.getty.edu/aat/300008372 (narrowMatch)
  - http://vocab.getty.edu/aat/300008375 (narrowMatch)
  - http://vocab.getty.edu/aat/300444153 (narrowMatch)
- **Concept URI:** http://vocab.terralid.org#c_c8fd0d05

[]{#building}

#####  building
- **Definition**: A structure built for a specific use.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - http://vocab.getty.edu/aat/300004790 (exactMatch)
  - https://www.wikidata.org/wiki/Q41176 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dcd55898

[]{#house}

######  house
- **Definition**: Building or ensemble of buildings used to provide
shelter and accommodation.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300257729 (exactMatch)
  - https://www.wikidata.org/wiki/Q3947 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_645bace2

[]{#military-structure}

######  military structure
- **Definition**: Building or ensemble of buildings used by military
forces.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300006887 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_49d89222

[]{#administrative-structure}

######  administrative structure
- **Definition**: Building or ensemble of buildings used to conduct
the management and other administrative activities of an organisation
or institution.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300007049 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0fcad077

[]{#communal-structure}

######  communal structure
- **Definition**: Building or ensemble of buildings used for communal
activities such as gatherings or cultural activities or constructed to
serve communal needs such as bathhouses.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300005120 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_98f1e2ac

[]{#religious-structure}

######  religious structure
- **Definition**: Building or ensemble of buildings used for
ceremonial and ritual activities.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1370598 (closeMatch)
  - http://vocab.getty.edu/aat/300263489 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7b246286

[]{#agricultural-structure}

######  agricultural structure
- **Definition**: Building or ensemble of buildings used in
agriculture.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300004895 (exactMatch)
  - https://www.wikidata.org/wiki/Q10480682 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f1d0e7f8

[]{#workshop}

######  workshop
- **Definition**: Building or ensemble of buildings for a specific
craft or industry.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - http://vocab.getty.edu/aat/300007733 (exactMatch)
  - https://www.wikidata.org/wiki/Q656720 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c06a2eb0

[]{#foundry}

#######  foundry
- **Definition**: Built structure used to melt and cast metal.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - http://vocab.getty.edu/aat/300266773 (closeMatch)
  - https://www.wikidata.org/wiki/Q13883136 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3d91691e

[]{#smelting-site}

#######  smelting site
- **Definition**: Built structure used to produce metal from ores.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - http://vocab.getty.edu/aat/300103997 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ba016e0c

[]{#melting-site}

#######  melting site
- **Definition**: Built structure used to prepare metals for the
production of items from it such as refining, alloying, melting of
scraps.
- **Child of**:
  - [`workshop`](#workshop)
- **Concept URI:** http://vocab.terralid.org#c_f6c15b72

[]{#non-metallurgical-workshop}

#######  non-metallurgical workshop
- **Definition**: Workshop unrelated to metallurgical activities.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - http://vocab.getty.edu/aat/300007733 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_92076176

[]{#infrastructure}

#####  infrastructure
- **Definition**: Built structure that allows the movement of goods or
people.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - http://vocab.getty.edu/aat/300386980 (exactMatch)
  - https://www.wikidata.org/wiki/Q121359 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3ae8c85b

[]{#bridge}

######  bridge
- **Definition**: Built structure that provides passage over a
depression or other structure.
- **Child of**:
  - [`infrastructure`](#infrastructure)
- **Matches:**
  - http://vocab.getty.edu/aat/300007836 (exactMatch)
  - https://www.wikidata.org/wiki/Q12280 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_11c6ca85

[]{#road}

######  road
- **Definition**: Built structure that connects locations on the
ground.
- **Child of**:
  - [`infrastructure`](#infrastructure)
- **Matches:**
  - http://vocab.getty.edu/aat/300007800 (exactMatch)
  - https://www.wikidata.org/wiki/Q34442 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3d1e781c

[]{#mine}

####  mine
- **Definition**: Place at which resources are extracted from the
earth through exacavation activities.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300000390 (exactMatch)
  - https://www.wikidata.org/wiki/Q820477 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d6f184d2

[]{#underground-mine}

#####  underground mine
- **Definition**: Place at which resources are extracted underground
from the earth through excavation activities.
- **Child of**:
  - [`mine`](#mine)
- **Matches:**
  - https://www.wikidata.org/wiki/Q4232315 (exactMatch)
  - http://vocab.getty.edu/aat/300000390 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_fa1cf9f1

[]{#open-pit-mine}

#####  open pit mine
- **Definition**: Place at which resources are extracted open-air from
the earth through excavation activities.
- **Child of**:
  - [`mine`](#mine)
- **Matches:**
  - https://www.wikidata.org/wiki/Q113681824 (exactMatch)
  - http://vocab.getty.edu/aat/300000390 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_20e4e9cd

[]{#mining-related-site}

####  mining-related site
- **Definition**: Any structure related to the operation of mines or
the processing of the mine's output.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300000388 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_0e020c21

[]{#ore-beneficiation-site}

#####  ore beneficiation site
- **Definition**: Structure used to remove economically unviable parts
of the material extracted from a mine and to sort it in preparation
for smelting.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300404101 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_df11f809

[]{#mining-sink-hole}

#####  mining sink-hole
- **Definition**: A depression in the ground caused by mining activity
(either open-air working or collapsed underground workings).
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Alternate labels:**
  - pinge
- **Concept URI:** http://vocab.terralid.org#c_5163843b

[]{#slag-dump}

#####  slag dump
- **Definition**: Area collecting discarded material from smelting
operations.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - http://vocab.getty.edu/aat/300000832 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_e652be5b

[]{#mine-dump}

#####  mine dump
- **Definition**: Area collecting discarded material from mining
activities.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Alternate labels:**
  - spoil tip, 
  - spoil pile, 
- **Matches:**
  - http://vocab.getty.edu/aat/300000821 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_143dd859

[]{#tailing-dump}

#####  tailing dump
- **Definition**: Area collecting discarded material from ore
beneficiation activities is collected.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1784525 (exactMatch)
  - http://vocab.getty.edu/aat/300000832 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_5f810e19

[]{#mining-project}

#####  mining project
- **Definition**: An informal grouping of mineral deposits commonly
used for reporting.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/project (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a790da1a

[]{#refuse-area}

####  refuse area
- **Definition**: Areas primarily used for the collection of discarded
materials.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300000824 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9bf30dd9

[]{#slag-dump}

#####  slag dump
- **Definition**: Area collecting discarded material from smelting
operations.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - http://vocab.getty.edu/aat/300000832 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_e652be5b

[]{#debris-dump}

#####  debris dump
- **Definition**: Area collecting discarded material from structures
such as buildings or furnaces.
- **Child of**:
  - [`refuse area`](#refuse-area)
- **Concept URI:** http://vocab.terralid.org#c_15466516

[]{#mine-dump}

#####  mine dump
- **Definition**: Area collecting discarded material from mining
activities.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Alternate labels:**
  - spoil tip, 
  - spoil pile, 
- **Matches:**
  - http://vocab.getty.edu/aat/300000821 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_143dd859

[]{#tailing-dump}

#####  tailing dump
- **Definition**: Area collecting discarded material from ore
beneficiation activities is collected.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1784525 (exactMatch)
  - http://vocab.getty.edu/aat/300000832 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_5f810e19

[]{#midden}

#####  midden
- **Definition**: Area collecting refuse predominantly originating
from human occupational activities.
- **Child of**:
  - [`refuse area`](#refuse-area)
- **Matches:**
  - http://vocab.getty.edu/aat/300120507 (exactMatch)
  - https://www.wikidata.org/wiki/Q1152199 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_475e1a3a

[]{#funerary-site}

####  funerary site
- **Definition**: Site primarily used to bury deceased humans,
sometimes also animals.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** http://vocab.terralid.org#c_87b21259

[]{#burial-ground}

#####  burial ground
- **Definition**: Site with burials of deceased humans, sometimes
animals.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Alternate labels:**
  - cemeteries
- **Matches:**
  - http://vocab.getty.edu/aat/300266755 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_269c18b5

[]{#grave}

#####  grave
- **Definition**: Feature dug into the earth without any constructed
structures to bury a deceased human, sometimes animal.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Matches:**
  - http://purl.org/heritagedata/schemes/eh_com/concepts/137492 (exactMatch)
  - http://purl.org/heritagedata/schemes/eh_evd/concepts/151454 (exactMatch)
  - http://vocab.getty.edu/aat/300005907 (exactMatch)
  - https://www.wikidata.org/wiki/Q173387 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_75e7f1d3

[]{#tomb}

#####  tomb
- **Definition**: Built structure (on the ground or into the ground)
dedicated to the interment of a deceased human, sometimes animal.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Matches:**
  - http://purl.org/heritagedata/schemes/eh_com/concepts/138345 (exactMatch)
  - http://vocab.getty.edu/aat/300005926 (exactMatch)
  - https://www.wikidata.org/wiki/Q381885 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2e5ac6fa

[]{#burial-cave}

#####  burial cave
- **Definition**: A natural opening in the earth used to bury deceased
humans, sometimes animals.
- **Child of**:
  - [`funerary site`](#funerary-site)
  - [`cave`](#cave)
- **Matches:**
  - http://vocab.getty.edu/aat/300387008 (exactMatch)
  - https://www.wikidata.org/wiki/Q111340496 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_00c534fa

[]{#artefact-scatter}

####  artefact scatter
- **Definition**: Site with artefacts arranged on a (previous) ground
surface.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300451777 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d2a764d2

[]{#single-find}

####  single find
- **Definition**: An isolated item, seemingly unrelated to any
structure or other traces of human activity.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** http://vocab.terralid.org#c_6d29fe63

[]{#isolated-feature}

####  isolated feature
- **Definition**: An isolated structure assumedly originating from
human activity.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** http://vocab.terralid.org#c_99186ef5

[]{#hearth}

####  hearth
- **Definition**: Remains of human activities carried out to create
and maintain a controlled fire without any dedicated architectural
remains.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - https://www.wikidata.org/wiki/Q585473 (closeMatch)
  - http://purl.org/heritagedata/schemes/eh_com/concepts/138029 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6d1e6826

[]{#post-hole}

####  post hole
- **Definition**: A hole dug to include a timber post, usually with
its packing.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://purl.org/heritagedata/schemes/eh_com/concepts/138109 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_16c0c950

[]{#pit}

####  pit
- **Definition**: A negative feature dug into the ground.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300008027 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1af01438

[]{#infilling}

####  infilling
- **Definition**: Material used to fill in a negative feature in the
ground.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300264840 (exactMatch)
  - https://www.wikidata.org/wiki/Q125275846 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_536290b6

[]{#storage-pit}

####  storage pit
- **Definition**: A pit dug in the ground to store materials.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** http://vocab.terralid.org#c_8f51e8b9

[]{#geological-site}

###  geological site
- **Definition**: The site is characterised by its geological
features.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
  - [`site type`](#site-type)
- **Matches:**
  - https://www.wikidata.org/wiki/Q10376531 (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type (narrowMatch)
- **Concept URI:** http://vocab.terralid.org#c_823bba89

[]{#cave}

####  cave
- **Definition**: A natural opening in the earth large enough for
humans to explore and sometimes also to use.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - http://vocab.getty.edu/aat/300008746 (exactMatch)
  - https://www.wikidata.org/wiki/Q35509 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1f2bd128

[]{#burial-cave}

#####  burial cave
- **Definition**: A natural opening in the earth used to bury deceased
humans, sometimes animals.
- **Child of**:
  - [`funerary site`](#funerary-site)
  - [`cave`](#cave)
- **Matches:**
  - http://vocab.getty.edu/aat/300387008 (exactMatch)
  - https://www.wikidata.org/wiki/Q111340496 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_00c534fa

[]{#deposit}

####  deposit
- **Definition**: A single body of naturally occurring and genetically
connected material with an anomalous concentration of a mineral or
rock type that has potential for human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/deposit (exactMatch)
  - https://www.wikidata.org/wiki/Q15104915 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4d90feaa

[]{#occurrence}

####  occurrence
- **Definition**: A single body of naturally occurring and genetically
connected material of any concentration that might have potential for
human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Alternate labels:**
  - mineralisation
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/occurrence (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_177cd232

[]{#outcrop}

#####  outcrop
- **Definition**: An occurrence that is accessible on the ground.
- **Child of**:
  - [`occurrence`](#occurrence)
- **Matches:**
  - https://www.wikidata.org/wiki/Q531953 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9db8b2d9

[]{#field}

####  field
- **Definition**: An area characterised by several geologically
related mineral occurrences.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/field (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4fba9c43

[]{#locality}

####  locality
- **Definition**: An area characterised by several geologically
related mineral occurrences with potential of human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Alternate labels:**
  - mining prospect
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/prospect (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b01341cd

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb


[]{#assemblage}

##  assemblage
- **Definition**: Grouping of items or specimens resulting from human
activity for archaeological materials or environmental and tectonic
processes for geological materials.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Matches:**
  - http://vocab.getty.edu/aat/300256847 (closeMatch)
  - http://vocab.getty.edu/aat/300241507 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_0fab0ef9

[]{#collection}

###  collection
- **Definition**: Accumulations of objects according to certain topics
or characteristics that do not necessarily share a common provenance.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to be used only for objects and samples with unknown archaeological context. 
- **Matches:**
  - http://vocab.getty.edu/aat/300025976 (exactMatch)
  - https://www.wikidata.org/wiki/Q2668072 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d0a53b23

[]{#components}

###  components
- **Definition**: Objects that are intended to be always used or
present in connection with other components, such as a rivet.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to identify assemblages resulting from the detachment of previously combined components which are recorded individually. 
- **Matches:**
  - http://vocab.getty.edu/aat/300241583 (exactMatch)
  - https://www.wikidata.org/wiki/Q1310239 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_665746e2

[]{#hoard}

###  hoard
- **Definition**: Group of objects that were accumulated with the aim
to be buried or hidden.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`assemblage`](#assemblage)
- **Matches:**
  - http://vocab.getty.edu/aat/300195474 (exactMatch)
  - https://www.wikidata.org/wiki/Q164099 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5f8d30a4

[]{#item}

###  item
- **Definition**: A single object.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to identify that the items does not belong to an assemblage, or that the assemblage contains only one item. 
- **Matches:**
  - http://vocab.getty.edu/aat/300404024 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5f249aa8

[]{#set}

###  set
- **Definition**: Objects purposely combined to be used as group.
- **Child of**:
  - [`Konzepte`](#konzepte)
  - [`assemblage`](#assemblage)
- **Matches:**
  - http://vocab.getty.edu/aat/300133146 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_db7df3e1

[]{#gossan}

###  gossan
- **Definition**: The outcropping, heavily weathered part of a
mineralisation.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan (exactMatch)
  - https://www.wikidata.org/wiki/Q639293 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e6cf20b1

[]{#alteration-product-(hydrothermal)}

###  alteration product (hydrothermal)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by hydrothermal solutions.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`alteration product`](#alteration-product)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_b81f7872

[]{#alteration-product-(supergene)}

###  alteration product (supergene)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by weathering.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`alteration product`](#alteration-product)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_f4468f4e

[]{#host-rock}

###  host rock
- **Definition**: The country rock or rock body in which a
mineralisation occurs.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
  - [`gangue`](#gangue)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9c0fc70d

[]{#ore}

###  ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (exactMatch)
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771 (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/raw-material-role/ore (exactMatch)
  - http://vocab.getty.edu/aat/300152583 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4dffb82b

[]{#primary-ore}

####  primary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was not altered by hydrothermal
processes or weathering.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_1823779e

[]{#secondary-ore}

####  secondary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was altered by hydrothermal
processes or weathering. The term usually refers to ore that became
enriched in the targeted elements because of alteration processes.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_adc64d1b

[]{#alteration}

####  alteration
- **Definition**: The part of the ore that is affected by natural
post-genetic processes, often including interaction with a hydrous
fluid.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/eventprocess/alteration (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_27e6e534

[]{#ore-mineral}

####  ore mineral
- **Definition**: The economically viable part of the ore.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/raw-material-role/ore (exactMatch)
  - https://www.wikidata.org/wiki/Q1969263 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_39a52896

[]{#major-mineral}

#####  major mineral
- **Definition**: An economically viable mineral dominating the ore's
mineralogical composition.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** http://vocab.terralid.org#c_6e9f3cf6

[]{#minor-mineral}

#####  minor mineral
- **Definition**: An economically viable mineral constituting a minor
part in the ore's mineralogy.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** http://vocab.terralid.org#c_42b68c9f

[]{#wall-rock}

###  wall rock
- **Definition**: The section of the host rock that was affected by
epigenetic processes resulting in the mineralisation.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_25814b64

[]{#gangue}

###  gangue
- **Definition**: The part of an ore not deemed economically
desirable.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/gangue (exactMatch)
  - https://www.wikidata.org/wiki/Q1061670 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_235c43fb

[]{#host-rock}

####  host rock
- **Definition**: The country rock or rock body in which a
mineralisation occurs.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
  - [`gangue`](#gangue)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9c0fc70d


[]{#discovery-activity}

##  discovery activity
- **Child of**:
  - [`méthodes`](#méthodes)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/147298 (relatedMatch)
  - http://purl.org/heritagedata/schemes/agl_et/concepts/147297 (relatedMatch)
- **Concept URI:** http://vocab.terralid.org#c_e95a9fbf

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#stray-find}

###  stray find
- **Definition**: The incidental discovery (and recovery) of materials
of interest.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/146344 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_84c6c6e0

[]{#borehole-survey}

###  borehole survey
- **Definition**: Drilling into the ground with the aim to collect
samples and/or to describe the stratigraphy and subsurface features of
archaeological and geological features.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145112 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_eb09b8cd

[]{#core-drilling}

####  core drilling
- **Definition**: Drilling into the ground with the aim to retrieve
the content of the borehole as a whole. The material will subsequently
be used to collect samples and/or to describe the stratigraphy and
subsurface features of archaeological and geological features.
- **Child of**:
  - [`borehole survey`](#borehole-survey)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/exploration-activity-type/core-drilling (exactMatch)
  - http://inspire.ec.europa.eu/codelist/ExplorationActivityTypeValue/coreDrilling (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_410a0d02

[]{#auger-drilling}

####  auger drilling
- **Definition**: Drilling into the ground with the aim to retrieve
the content of the borehole as loose material to retrieve samples. In
some cases, it can be used to infer stratigraphy and subsurface
features of archaeological and geological features.
- **Child of**:
  - [`borehole survey`](#borehole-survey)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/exploration-activity-type/auger-drilling (exactMatch)
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145111 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_19639bab

[]{#metal-detecting}

###  metal detecting
- **Definition**: The use of a metal detector to discover artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145147 (closeMatch)
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145148 (closeMatch)
  - https://www.wikidata.org/wiki/Q111047657 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3f471934

[]{#excavation}

###  excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an site and to retrieve samples and artefacts from
the site.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145160 (closeMatch)
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145129 (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/exploration-activity-type/excavation (exactMatch)
  - http://vocab.getty.edu/aat/300266151 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cd2a7865

[]{#research-excavation}

####  research excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to answer a specific research question by recording an site
and retrieving samples and artefacts from the site.
- **Child of**:
  - [`excavation`](#excavation)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/147305 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8eff20cd

[]{#rescue-excavation}

####  rescue excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an site under threat of destruction and to retrieve
samples and artefacts from the site under strict time constraints.
- **Child of**:
  - [`excavation`](#excavation)
- **Alternate labels:**
  - salvage excavation
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/145157 (exactMatch)
  - https://www.wikidata.org/wiki/Q101008619 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f39b79f2

[]{#underwater-excavation}

####  underwater excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an underwater site and to retrieve samples and
artefacts from the site.
- **Child of**:
  - [`excavation`](#excavation)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/163244 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6a6e0a7f

[]{#survey}

###  survey
- **Definition**: Non-intrusive fieldwork to document the extent and
layout of a site through recording the position and distribution of
specimens and artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://purl.org/heritagedata/schemes/agl_et/concepts/170654 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ae4a0583

[]{#mining}

###  mining
- **Definition**: The economic extraction of georesources from the
earth. This includes surface and underground operations.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/mining-activity (exactMatch)
  - https://www.wikidata.org/wiki/Q44497 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2758f3b1

[]{#explorative-mining-activities}

###  explorative mining activities
- **Definition**: Mining activities in preparation to establishing a
full-scale mining operation.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mine-workings-reconnaissance (closeMatch)
  - http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mining-pilot (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_77f07bb9

[]{#ore-prospection}

###  ore prospection
- **Definition**: The systematic survey on an area with the aim to
identify the presence of potentially economically viable
mineralisations.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Concept URI:** http://vocab.terralid.org#c_074a675c

[]{#illicit-digging}

###  illicit digging
- **Definition**: Uncontrolled and usually undocumented intrusive
fieldwork with the aim to collected artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Alternate labels:**
  - looting
- **Matches:**
  - https://www.wikidata.org/wiki/Q15624851 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d0e965f6


[]{#context-type}

##  context type
- **Definition**: Information about whether an (archaeological)
context includes material from a single depositional event and whether
the context is impacted by any post-depositional processes.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Concept URI:** http://vocab.terralid.org#c_ca223f0b

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#undisturbed-context}

###  undisturbed context
- **Definition**: The context represents a single depositional event
with all material coming from the same source and no interaction
happening after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Alternate labels:**
  - primary context
- **Matches:**
  - https://www.wikidata.org/wiki/Q136826284 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0541320f

[]{#disturbed-context}

###  disturbed context
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Alternate labels:**
  - secondary context
- **Matches:**
  - https://www.wikidata.org/wiki/Q136826785 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0faa6b29

[]{#anthropogenically-disturbed}

####  anthropogenically disturbed
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with humans being the
responsible agents.
- **Child of**:
  - [`disturbed context`](#disturbed-context)
- **Concept URI:** http://vocab.terralid.org#c_9408f513

[]{#biogenically-disturbed}

####  biogenically disturbed
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with non-humans being the
responsible agents (e.g. bioturbidation).
- **Child of**:
  - [`disturbed context`](#disturbed-context)
- **Concept URI:** http://vocab.terralid.org#c_1c4bfb96

[]{#mixed-context}

###  mixed context
- **Definition**: The context represents a single depositional event
with material coming from multiple sources and no interaction
happening after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Concept URI:** http://vocab.terralid.org#c_a0ae7ce8


[]{#sample-housing}

##  sample housing
- **Definition**: The material the object is stored in.
- **Child of**:
  - [`objetos móveis`](#objetos-móveis)
- **Concept URI:** http://vocab.terralid.org#c_b53eb953

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#cardboard-box}

###  cardboard box
- **Definition**: A container made of thick stiff pasteboard with
either a lid or a foldable parts on its top for closing it.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - http://vocab.getty.edu/aat/300215468 (broadMatch)
  - http://vocab.getty.edu/aat/300200342 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_1a3ca880

[]{#acid-free-cardboard-box}

####  acid-free cardboard box
- **Definition**: A cardboard box certified to be acid free.
- **Child of**:
  - [`cardboard box`](#cardboard-box)
- **Concept URI:** http://vocab.terralid.org#c_6fedae89

[]{#non-acid-free-cardboard-box}

####  non acid-free cardboard box
- **Definition**: A cardboard box not certified to be acid free.
- **Child of**:
  - [`cardboard box`](#cardboard-box)
- **Concept URI:** http://vocab.terralid.org#c_ae7c0b8c

[]{#eppendorf-tube}

###  Eppendorf tube
- **Definition**: A tube with a hinged sealing cap made of
(shatterproof) plastics.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1933961 (exactMatch)
  - http://vocab.getty.edu/aat/300198822 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_518ec832

[]{#glass-vial}

###  glass vial
- **Definition**: A vial made of glass and closed with a lid, often
made of plastics. They come in various shapes and sizes and with
various types of lids.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - http://vocab.getty.edu/aat/300198822 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_e7fdebfb

[]{#ptfe-teflon-vial}

###  PTFE/Teflon vial
- **Definition**: A vial with lid made of PTFE or Teflon.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - http://vocab.getty.edu/aat/300198822 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_3bb341cf

[]{#no-housing}

###  no housing
- **Definition**: The objects are not stored in a container, usually
because of their size and/or weight.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Concept URI:** http://vocab.terralid.org#c_0e85ae39

[]{#plastics-bag}

###  plastics bag
- **Definition**: A usually non-sealable flexible container made of
plastics.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - http://vocab.getty.edu/aat/300194509 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_f641a35c

[]{#ziplock-bag}

####  ziplock bag
- **Definition**: A re-sealable storage made of plastics, usually
polyethylene (PE).
- **Child of**:
  - [`plastics bag`](#plastics-bag)
- **Matches:**
  - http://vocab.getty.edu/aat/300194509 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_10420b12

[]{#plastics-fabric-bag}

####  plastics fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`plastics bag`](#plastics-bag)
  - [`fabric bag`](#fabric-bag)
- **Concept URI:** http://vocab.terralid.org#c_f26d0d8c

[]{#fabric-bag}

###  fabric bag
- **Definition**: A flexible container made of woven material.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - http://vocab.getty.edu/aat/300194509 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_cbbc3d94

[]{#cotton-fabric-bag}

####  cotton fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`fabric bag`](#fabric-bag)
- **Concept URI:** http://vocab.terralid.org#c_ccf5461d

[]{#plastics-fabric-bag}

####  plastics fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`plastics bag`](#plastics-bag)
  - [`fabric bag`](#fabric-bag)
- **Concept URI:** http://vocab.terralid.org#c_f26d0d8c

[]{#paper-bag}

###  paper bag
- **Definition**: A flexible container made of paper. Includes
envelopes, which are paper bags that can be seabled by some sort of
pre-applied adhesive on the closing flap.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Alternate labels:**
  - paper envelope
- **Matches:**
  - https://www.wikidata.org/wiki/Q379754 (exactMatch)
  - http://vocab.getty.edu/aat/300194509 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_850e4a23

[]{#acid-free-paper-bag}

####  acid-free paper bag
- **Definition**: A paper bag or envelope certified to be acid free.
- **Child of**:
  - [`paper bag`](#paper-bag)
- **Concept URI:** http://vocab.terralid.org#c_77b00da1

[]{#non-acid-free-paper-bag}

####  non acid-free paper bag
- **Definition**: A paper bag or envelope not certified to be acid
free.
- **Child of**:
  - [`paper bag`](#paper-bag)
- **Concept URI:** http://vocab.terralid.org#c_a1f7691a

[]{#display-case}

###  display case
- **Definition**: A cabinet with at least one transparent part
specifically designed to present objects to a visitor, e.g. in a
museum exhibition.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Alternate labels:**
  - showcase, 
  - vitrine, 
- **Matches:**
  - http://vocab.getty.edu/aat/300077356 (exactMatch)
  - https://www.wikidata.org/wiki/Q3561331 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c56bc948

[]{#controlled-environment-display-case}

####  controlled environment display case
- **Definition**: A display case equipped to control the environment
in it (e.g., temperature, humidity, chemical pollutants).
- **Child of**:
  - [`display case`](#display-case)
- **Concept URI:** http://vocab.terralid.org#c_d9a8b325

[]{#uncontrolled-environment-display-case}

####  uncontrolled environment display case
- **Definition**: A display case not equipped to control the
environment in it.
- **Child of**:
  - [`display case`](#display-case)
- **Concept URI:** http://vocab.terralid.org#c_e1c7a89c


[]{#object-life-cycle-stage}

##  object life cycle stage
- **Definition**: The different stages an object undergoes after its
collection in the field.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Concept URI:** http://vocab.terralid.org#c_6eeee275

[]{#storage-stage}

###  storage stage
- **Definition**: The object is stored in a place to keep it safe in
the long term.
- **Child of**:
  - [`human interactions`](#human-interactions)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - http://vocab.getty.edu/aat/300056390 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_20b5f585

[]{#restoration-stage}

###  restoration stage
- **Definition**: The object is brought back to its original shape as
much as possible, often with addition of missing parts.
- **Child of**:
  - [`human interactions`](#human-interactions)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - http://vocab.getty.edu/aat/300053742 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_084b00a4

[]{#conservation-stage}

###  conservation stage
- **Definition**: The object is treated in a conservation laboratory
to stop ongoing deterioation and to prepare it for long-term storage.
- **Child of**:
  - [`human interactions`](#human-interactions)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - http://vocab.getty.edu/aat/300404519 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5282dab3

[]{#finds-processing-stage}

###  finds processing stage
- **Definition**: The object undergoes limited treatment in the field
such as washing or basic convservation measures.
- **Child of**:
  - [`human interactions`](#human-interactions)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Alternate labels:**
  - in-situ conservation
- **Matches:**
  - http://vocab.getty.edu/aat/300404519 (relatedMatch)
- **Concept URI:** http://vocab.terralid.org#c_75b32326

[]{#discovery-stage}

###  discovery stage
- **Definition**: The object did not received any treatment (yet)
since its discovery.
- **Child of**:
  - [`human interactions`](#human-interactions)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - http://vocab.getty.edu/aat/300404386 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_687c5f00

[]{#laboratory-stage}

###  laboratory stage
- **Definition**: The object is under investigation in a laboratory.
- **Child of**:
  - [`environnement bâti`](#environnement-bâti)
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - http://vocab.getty.edu/aat/300007660 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_33bebd59


[]{#object-material}

##  object material
- **Definition**: The material category of TerraLID used to determine
the material-specific metadata.
- **Child of**:
  - [`materials`](#materials)
- **Concept URI:** http://vocab.terralid.org#c_9dd8c641

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#other}

###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`object material`](#object-material)
  - [`reference material`](#reference-material)
  - [`analytical instrument`](#analytical-instrument)
  - [`alteration process`](#alteration-process)
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_ebc979f8

[]{#sediment}

###  sediment
- **Definition**: The object is unconsolidated geogenic material that
was deposited by water, wind, or ice.
- **Child of**:
  - [`object material`](#object-material)
  - [`geological material`](#geological-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770 (exactMatch)
  - http://vocab.getty.edu/aat/300379424 (exactMatch)
  - https://www.wikidata.org/wiki/Q180184 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fc64d08c

[]{#ceramic}

###  ceramic
- **Definition**: The object is (predominantly) made of a nonmetallic
malleable material that was intentionally transformed at high
temperatures into a non-malleable state.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972 (exactMatch)
  - http://vocab.getty.edu/aat/300235507 (exactMatch)
  - https://www.wikidata.org/wiki/Q45621 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d7fb0caf

[]{#pigment}

###  pigment
- **Definition**: The term is used rather loosely here to describe any
material that is used for colouring another material.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Alternate labels:**
  - dye, 
  - paint, 
- **Matches:**
  - http://vocab.getty.edu/aat/300013026 (exactMatch)
  - https://www.wikidata.org/wiki/Q161179 (exactMatch)
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964 (narrowMatch)
  - http://vocab.getty.edu/aat/300013109 (narrowMatch)
- **Concept URI:** http://vocab.terralid.org#c_461a3e6b

[]{#glass}

###  glass
- **Definition**: The object is (predominantly) made of an inorganic
vitrous material based on fused silica.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774 (exactMatch)
  - https://www.wikidata.org/wiki/Q11469 (exactMatch)
  - http://vocab.getty.edu/aat/300010797 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee038e9e

[]{#metal}

###  metal
- **Definition**: The object is (predominantly) made of a metallic
material.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792 (exactMatch)
  - http://vocab.getty.edu/aat/300010900 (exactMatch)
  - https://www.wikidata.org/wiki/Q11426 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_068f3adc

[]{#coin}

####  coin
- **Definition**: A usually small, flat and round piece of metal
primarily used as medium of exchange or legal tender. It usually
follows a standardised system in weight and sometimes size and is
produced in large quantities.
- **Child of**:
  - [`objetos móveis`](#objetos-móveis)
  - [`metal`](#metal)
- **Matches:**
  - http://nomisma.org/id/coin (exactMatch)
  - http://www.wikidata.org/entity/Q41207 (exactMatch)
  - http://vocab.getty.edu/aat/300037222 (exactMatch)
  - http://d-nb.info/gnd/4040629-5 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9775890c

[]{#ore-(terralid-category)}

###  ore (TerraLID category)
- **Definition**: Geological material from which resources are
extracted, especially metals.
- **Child of**:
  - [`object material`](#object-material)
- **Other Properties:**
  - **scopeNote**: 
This entry refers specifically to the material classification in TerraLID for object-specific metadata. 
- **Concept URI:** http://vocab.terralid.org#c_dbeb733b


[]{#authenticity}

##  authenticity
- **Definition**: Whether the object is a genuine representation or an
imitation.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Matches:**
  - http://vocab.getty.edu/aat/300055848 (exactMatch)
  - https://www.wikidata.org/wiki/Q13431773 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_78d89252

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#modern-imitation}

###  modern imitation
- **Definition**: The object is a imitation of an other object that
was produced when the original object was not in use or circulation.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Matches:**
  - http://nomisma.org/id/modern_imitation (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9c8f2a35

[]{#contemporary-imitation}

###  contemporary imitation
- **Definition**: The object is a contemporary imitation of an other
object.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Matches:**
  - http://nomisma.org/id/contemporary_imitation (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1e12e502

[]{#genuine}

###  genuine
- **Definition**: The object is authentic.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Alternate labels:**
  - official, 
  - authentic, 
- **Matches:**
  - http://nomisma.org/id/official (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_149b5682


[]{#sample-material}

##  sample material
- **Definition**: The physical matter that was sampled for analysis.
- **Child of**:
  - [`materials`](#materials)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dd76eaab

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#geological-material}

###  geological material
- **Definition**: Material that was created by geological processes.
- **Child of**:
  - [`sample material`](#sample-material)
- **Concept URI:** http://vocab.terralid.org#c_888076c5

[]{#gossan}

####  gossan
- **Definition**: The outcropping, heavily weathered part of a
mineralisation.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan (exactMatch)
  - https://www.wikidata.org/wiki/Q639293 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e6cf20b1

[]{#host-rock}

####  host rock
- **Definition**: The country rock or rock body in which a
mineralisation occurs.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
  - [`gangue`](#gangue)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9c0fc70d

[]{#ore}

####  ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (exactMatch)
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771 (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/raw-material-role/ore (exactMatch)
  - http://vocab.getty.edu/aat/300152583 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4dffb82b

[]{#primary-ore}

#####  primary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was not altered by hydrothermal
processes or weathering.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_1823779e

[]{#secondary-ore}

#####  secondary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was altered by hydrothermal
processes or weathering. The term usually refers to ore that became
enriched in the targeted elements because of alteration processes.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_adc64d1b

[]{#alteration}

#####  alteration
- **Definition**: The part of the ore that is affected by natural
post-genetic processes, often including interaction with a hydrous
fluid.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (exactMatch)
  - http://resource.geosciml.org/classifier/cgi/eventprocess/alteration (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_27e6e534

[]{#ore-mineral}

#####  ore mineral
- **Definition**: The economically viable part of the ore.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/raw-material-role/ore (exactMatch)
  - https://www.wikidata.org/wiki/Q1969263 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_39a52896

[]{#major-mineral}

######  major mineral
- **Definition**: An economically viable mineral dominating the ore's
mineralogical composition.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** http://vocab.terralid.org#c_6e9f3cf6

[]{#minor-mineral}

######  minor mineral
- **Definition**: An economically viable mineral constituting a minor
part in the ore's mineralogy.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** http://vocab.terralid.org#c_42b68c9f

[]{#wall-rock}

####  wall rock
- **Definition**: The section of the host rock that was affected by
epigenetic processes resulting in the mineralisation.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_25814b64

[]{#sediment}

####  sediment
- **Definition**: The object is unconsolidated geogenic material that
was deposited by water, wind, or ice.
- **Child of**:
  - [`object material`](#object-material)
  - [`geological material`](#geological-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770 (exactMatch)
  - http://vocab.getty.edu/aat/300379424 (exactMatch)
  - https://www.wikidata.org/wiki/Q180184 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fc64d08c

[]{#mineral}

####  mineral
- **Definition**: A crystalline component of the material with a
fairly well-defined crystal structure and chemical composition.
- **Child of**:
  - [`geological material`](#geological-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23931 (exactMatch)
  - http://vocab.getty.edu/aat/300011068 (exactMatch)
  - https://www.wikidata.org/wiki/Q7946 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b5560869

[]{#unaltered-material}

####  unaltered material
- **Definition**: Anthropogenic material without any perceivable
impact from interaction prosesses with the (depositional) environment.
- **Child of**:
  - [`geological material`](#geological-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_3a384c38

[]{#anthropogenic-material}

###  anthropogenic material
- **Definition**: Material that was created by humans.
- **Child of**:
  - [`sample material`](#sample-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_62b205ba

[]{#ceramic}

####  ceramic
- **Definition**: The object is (predominantly) made of a nonmetallic
malleable material that was intentionally transformed at high
temperatures into a non-malleable state.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972 (exactMatch)
  - http://vocab.getty.edu/aat/300235507 (exactMatch)
  - https://www.wikidata.org/wiki/Q45621 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d7fb0caf

[]{#pigment}

####  pigment
- **Definition**: The term is used rather loosely here to describe any
material that is used for colouring another material.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Alternate labels:**
  - dye, 
  - paint, 
- **Matches:**
  - http://vocab.getty.edu/aat/300013026 (exactMatch)
  - https://www.wikidata.org/wiki/Q161179 (exactMatch)
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964 (narrowMatch)
  - http://vocab.getty.edu/aat/300013109 (narrowMatch)
- **Concept URI:** http://vocab.terralid.org#c_461a3e6b

[]{#glass}

####  glass
- **Definition**: The object is (predominantly) made of an inorganic
vitrous material based on fused silica.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774 (exactMatch)
  - https://www.wikidata.org/wiki/Q11469 (exactMatch)
  - http://vocab.getty.edu/aat/300010797 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee038e9e

[]{#metal}

####  metal
- **Definition**: The object is (predominantly) made of a metallic
material.
- **Child of**:
  - [`object material`](#object-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792 (exactMatch)
  - http://vocab.getty.edu/aat/300010900 (exactMatch)
  - https://www.wikidata.org/wiki/Q11426 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_068f3adc

[]{#coin}

#####  coin
- **Definition**: A usually small, flat and round piece of metal
primarily used as medium of exchange or legal tender. It usually
follows a standardised system in weight and sometimes size and is
produced in large quantities.
- **Child of**:
  - [`objetos móveis`](#objetos-móveis)
  - [`metal`](#metal)
- **Matches:**
  - http://nomisma.org/id/coin (exactMatch)
  - http://www.wikidata.org/entity/Q41207 (exactMatch)
  - http://vocab.getty.edu/aat/300037222 (exactMatch)
  - http://d-nb.info/gnd/4040629-5 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9775890c

[]{#alteration-product-(anthropogenic)}

####  alteration product (anthropogenic)
- **Definition**: Anthropogenic material that is impacted by
interaction processes with the (depositional) environment.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`alteration product`](#alteration-product)
- **Concept URI:** http://vocab.terralid.org#c_1e35bdea

[]{#unaltered-material}

####  unaltered material
- **Definition**: Anthropogenic material without any perceivable
impact from interaction prosesses with the (depositional) environment.
- **Child of**:
  - [`geological material`](#geological-material)
  - [`anthropogenic material`](#anthropogenic-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_3a384c38

[]{#alteration-product}

###  alteration product
- **Definition**: Material that was transformed by the interaction of
its pristine state with the (depositional) environment.
- **Child of**:
  - [`sample material`](#sample-material)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d5356583

[]{#alteration-product-(hydrothermal)}

####  alteration product (hydrothermal)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by hydrothermal solutions.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`alteration product`](#alteration-product)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_b81f7872

[]{#alteration-product-(supergene)}

####  alteration product (supergene)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by weathering.
- **Child of**:
  - [`materials`](#materials)
  - [`assemblage`](#assemblage)
  - [`alteration product`](#alteration-product)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_f4468f4e

[]{#alteration-product-(anthropogenic)}

####  alteration product (anthropogenic)
- **Definition**: Anthropogenic material that is impacted by
interaction processes with the (depositional) environment.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`alteration product`](#alteration-product)
- **Concept URI:** http://vocab.terralid.org#c_1e35bdea

[]{#bulk}

###  bulk
- **Definition**: A fraction of the material that represents the
average composition of the material.
- **Child of**:
  - [`sample material`](#sample-material)
- **Concept URI:** http://vocab.terralid.org#c_d339fac4


[]{#sample-type}

##  sample type
- **Definition**: The type of material obtained by sampling.
- **Child of**:
  - [`objetos móveis`](#objetos-móveis)
- **Concept URI:** http://vocab.terralid.org#c_f8762e3d

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#drill-shavings}

###  drill shavings
- **Definition**: The sample was obtained with a rotary tool and is
present in larger pieces.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://pid.geoscience.gov.au/def/voc/ga/sampletype/drill_chips_cuttings (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_bfd0ca9e

[]{#in-situ}

###  in-situ
- **Definition**: The analysis was carried out directly on the object
without collecting a separate sample.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300220837 (exactMatch)
  - https://www.wikidata.org/wiki/Q216681 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1a77d68d

[]{#powder}

###  powder
- **Definition**: A powder was obtained during sampling or sampled
material was subsequently ground to powder.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://pid.geoscience.gov.au/def/voc/ga/sampletype/powder (exactMatch)
  - http://vocab.getty.edu/aat/300014647 (exactMatch)
  - https://www.wikidata.org/wiki/Q2908004 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_153bc01e

[]{#hand-picked}

###  hand-picked
- **Definition**: A part of the object was crushed and the sample
manually separated after visual inspection of each fragment.
- **Child of**:
  - [`sample type`](#sample-type)
- **Concept URI:** http://vocab.terralid.org#c_26707627

[]{#mineral-separate}

###  mineral separate
- **Definition**: A part of the object was crushed and the sample
extracted based on its physical or chemical properties (e.g., density,
magnetic properties).
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://pid.geoscience.gov.au/def/voc/ga/sampletype/mineral_separate (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0118bbdc

[]{#leachate}

###  leachate
- **Definition**: Acids or other solvents were applied to a usually
crushed part of the object to extract the sample as solution. Usually
only done with geological material.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300053761 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_fb28d155

[]{#swabbed-material}

###  swabbed material
- **Definition**: Acids or other solvents are applied with a soft and
absorbent tool (e.g., Q-tip, sponge) on the object to extract the
sample as solution absorbed to the same tool and/or particles adhering
to it. Usually only carried out on archaeological materials.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300434176 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_07f899ac

[]{#hand-specimen-fragments}

###  hand specimen fragments
- **Definition**: The object was crushed in to pieces, which were then
taken as sample. This is usually only done with larger items of
geological origin such as rocks.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://pid.geoscience.gov.au/def/voc/ga/sampletype/crush (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d8e9f67e

[]{#loose-material}

###  loose material
- **Definition**: The object already had detached pieces, which were
collected as sample.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300117130 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d57dc599

[]{#cut}

###  cut
- **Definition**: The sample is cut from the object with e.g. a blade
or saw.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300053069 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a7cdeda3

[]{#section}

###  section
- **Definition**: A larger piece of the object is cut with the aim to
create a section of it, usually for inspection with a microscope
and/or if the object is too large to fit into the analytical
instrument's sample chamber.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300379391 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fb91df68

[]{#polished-section}

####  polished section
- **Definition**: The section is polished to an even surface.
- **Child of**:
  - [`section`](#section)
- **Matches:**
  - http://vocab.getty.edu/aat/300053867 (relatedMatch)
- **Concept URI:** http://vocab.terralid.org#c_d33a496b

[]{#thin-section}

####  thin section
- **Definition**: The section is cut and polished to a thickness that
it becomes translucent.
- **Child of**:
  - [`section`](#section)
- **Matches:**
  - http://pid.geoscience.gov.au/def/voc/ga/sampletype/polished_thin_section (exactMatch)
  - http://vocab.getty.edu/aat/300386708 (exactMatch)
  - https://www.wikidata.org/wiki/Q542715 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4365b275


[]{#sampling-method}

##  sampling method
- **Definition**: The method used to extract a sample from an object.
- **Child of**:
  - [`méthodes`](#méthodes)
- **Matches:**
  - http://vocab.getty.edu/aat/300379429 (relatedMatch)
- **Concept URI:** http://vocab.terralid.org#c_2e6c0e69

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#drilling}

###  drilling
- **Definition**: The use of a rotating tool to remove material.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300053151 (exactMatch)
  - https://www.wikidata.org/wiki/Q890886 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_961ffe7e

[]{#micromill}

####  micromill
- **Definition**: A rotary tool equipped with a camera that allows
drilling on the micrometre scale in high spatial resolution.
- **Child of**:
  - [`drilling`](#drilling)
- **Concept URI:** http://vocab.terralid.org#c_e06764b7

[]{#cutting}

###  cutting
- **Definition**: The use of a blade or saw to remove a chunk from the
sample.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300053069 (exactMatch)
  - https://www.wikidata.org/wiki/Q196751 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a5e29dda

[]{#abrading}

###  abrading
- **Definition**: The mechanical removal of material by applying
material with a rough surface and higher hardness than the object.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300053077 (closeMatch)
  - https://www.wikidata.org/wiki/Q3819233 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3cc85343

[]{#ablating}

###  ablating
- **Definition**: The removal of material with a high energy beam such
as a laser.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Alternate labels:**
  - laser ablation
- **Matches:**
  - http://vocab.getty.edu/aat/300379663 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_89610abe

[]{#dissolution}

###  dissolution
- **Definition**: The removal of material with an acid or solvent.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300380018 (exactMatch)
  - https://www.wikidata.org/wiki/Q3133701 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_959163ef

[]{#swabbing}

####  swabbing
- **Definition**: The dissolution of material with the solvent or acid
being applied with a spongy and/or absorbent tissue, usually on a
small short stick.
- **Child of**:
  - [`dissolution`](#dissolution)
- **Alternate labels:**
  - Q-tip, 
  - sponge, 
- **Matches:**
  - http://vocab.getty.edu/aat/300434176 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_15912994

[]{#etching-leaching}

####  etching/leaching
- **Definition**: The dissolution of specific parts of a material by
covering or submerging it in an acid or solvent. While etching only
affects the surface, leaching affects the entire sample.
- **Child of**:
  - [`dissolution`](#dissolution)
- **Matches:**
  - http://vocab.getty.edu/aat/300053761 (exactMatch)
  - http://vocab.getty.edu/aat/300053840 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_02b29aae

[]{#fragment-collection}

###  fragment collection
- **Definition**: The collection of material that was already detached
from the object.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300077121 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_64e8e4be

[]{#crushing}

###  crushing
- **Definition**: The fragmentation of a material by applying
mechanical force to it until it breals.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300053084 (exactMatch)
  - https://www.wikidata.org/wiki/Q2991605 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9b8c9c7e

[]{#separation}

###  separation
- **Definition**: The division of material into its components
according to the components' properties.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - http://vocab.getty.edu/aat/300053748 (exactMatch)
  - https://www.wikidata.org/wiki/Q898987 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3eae3e76

[]{#magnet-separation}

####  magnet separation
- **Definition**: The separation process is based on the material
components' magnetic properties.
- **Child of**:
  - [`separation`](#separation)
- **Matches:**
  - http://vocab.getty.edu/aat/300425051 (relatedMatch)
- **Concept URI:** http://vocab.terralid.org#c_852bd94d

[]{#density-separation}

####  density separation
- **Definition**: The separation process is based on the material
components' specific densities.
- **Child of**:
  - [`separation`](#separation)
- **Matches:**
  - http://vocab.getty.edu/aat/300427901 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_5eab7b34

[]{#hand-picking}

####  hand-picking
- **Definition**: The separation of a specific component from crushed
material by hand, usually according to its optical properties or
shape.
- **Child of**:
  - [`separation`](#separation)
- **Concept URI:** http://vocab.terralid.org#c_f3f96906


[]{#sample-state}

##  sample state
- **Definition**: The state of the sample after analysis.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Concept URI:** http://vocab.terralid.org#c_9313eed2

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#modified}

###  modified
- **Definition**: The sample was modified during analysis, e.g. by
heating or partial dissolution.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** http://vocab.terralid.org#c_b1bf2e14

[]{#no-material-left}

###  no material left
- **Definition**: The sample was completely consumed by the analysis.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** http://vocab.terralid.org#c_19d31994

[]{#material-consumed}

###  material consumed
- **Definition**: Part of the sample was consumed during analysis,
e.g. by dissolving it.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** http://vocab.terralid.org#c_27d9869d

[]{#unchanged}

###  unchanged
- **Definition**: The sample was not modified by the analysis.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** http://vocab.terralid.org#c_b4ef9d51


[]{#sample-introduction}

##  sample introduction
- **Definition**: The aggregate state in which the sample is being
analysed.
- **Child of**:
  - [`méthodes`](#méthodes)
- **Concept URI:** http://vocab.terralid.org#c_d31174dd

[]{#solution}

###  solution
- **Definition**: The sample was dissolved in liquids and the solution
is analysed.
- **Child of**:
  - [`sample introduction`](#sample-introduction)
- **Matches:**
  - https://www.wikidata.org/wiki/Q5447188 (exactMatch)
  - http://vocab.getty.edu/aat/300210311 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4301bc07

[]{#laser-ablation}

###  laser ablation
- **Definition**: The sample was ablated with a laser and the ablated
particles are analysed.
- **Child of**:
  - [`sample introduction`](#sample-introduction)
- **Matches:**
  - http://vocab.getty.edu/aat/300379663 (closeMatch)
  - https://www.wikidata.org/wiki/Q1806547 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_95cd19d8


[]{#analytical-method}

##  analytical method
- **Definition**: Procedures that operate on material samples to
produce observation results with information about the physical
properties, chemical or isotopic composition, crystallography, or
molecular structure of the sample.
- **Child of**:
  - [`méthodes`](#méthodes)
- **Other Properties:**
  - **note**: 
Definition taken from: Richard, S. M., Klöcking, M., Luzi-Helbing, M., Johansson, A., Profeta, L., Lehnert, K., Elangovan, P., Sweets, H.A., Kallas, L., Sarbas, B., Mays, J., 2024. Analytical Methods for Geochemistry and Cosmochemistry. Concept Scheme for Analysis Methods in Geo- and Cosmochemistry. Published at Research Vocabularies Australia. Version 1.4.  https://vocabs.ardc.edu.au/viewById/650, published under a CC-BY license (version number of the license not provided). 
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/analyticalmethod (exactMatch)
  - https://www.wikidata.org/wiki/Q4751159 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c1c261a2

[]{#mass-spectrometer}

###  mass spectrometer
- **Definition**: An analytical instrument in which the sample is
ionised, the ions separated and detected according to their mass-to-
charge ratio.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/massspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q180809 (exactMatch)
  - https://vocab.getty.edu/aat/300225881 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c0d215f3

[]{#tims}

####  TIMS
- **Definition**: Mass spectrometer in which the sample is placed on a
filament and ionised by heating the filament. With respect to lead
isotope analyses, mass detection by a detector array in implied.
- **Child of**:
  - [`mass spectrometer`](#mass-spectrometer)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/thermalionizationmassspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e7d3223e

[]{#icp-ms}

####  ICP-MS
- **Definition**: Mass spectrometry technique in which the sample is
introduced into an inductively coupled plasma to atomize and ionize
the sample for inlet to mass analyzer.
- **Child of**:
  - [`mass spectrometer`](#mass-spectrometer)
- **Other Properties:**
  - **note**: 
Definition taken from Richard, S. M., Klöcking, M., Luzi-Helbing, M., Johansson, A., Profeta, L., Lehnert, K., Elangovan, P., Sweets, H.A., Kallas, L., Sarbas, B., Mays, J., 2024. Analytical Methods for Geochemistry and Cosmochemistry. Concept Scheme for Analysis Methods in Geo- and Cosmochemistry. Published at Research Vocabularies Australia. Version 1.4.  https://vocabs.ardc.edu.au/viewById/650, published under a CC-BY license (version number of the license not provided). 
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmamassspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q900680 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_32908a70

[]{#mc-icp-ms}

#####  MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ionised by
an inductively coupled plasma and ions detected by an array of several
detectors.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/multicollectorinductivelycoupledplasmamassspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d0d46a2c

[]{#la-mc-icp-ms}

######  LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, ionised by an inductively coupled plasma and ions
detected by an array of several detectors.
- **Child of**:
  - [`MC-ICP-MS`](#mc-icp-ms)
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_7b1b4216

[]{#fs-la-mc-icp-ms}

#######  fs-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_e56f0531

[]{#ns-la-mc-icp-ms}

#######  ns-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_e1700c12

[]{#q-icp-ms}

#####  Q-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ionised by
an inductively coupled plasma, iones separated by mass with a
quadrupole and detected by single dectector.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/quadrupoleinductivelycoupledplasmmassspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8e269b3e

[]{#la-icp-ms}

#####  LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, introduced into an inductively coupled plasma to
atomize and ionize the sample for inlet to mass analyzer.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/laserablationinductivelycoupledplasmamassspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q108900669 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6b7986e4

[]{#la-mc-icp-ms}

######  LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, ionised by an inductively coupled plasma and ions
detected by an array of several detectors.
- **Child of**:
  - [`MC-ICP-MS`](#mc-icp-ms)
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_7b1b4216

[]{#fs-la-mc-icp-ms}

#######  fs-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_e56f0531

[]{#ns-la-mc-icp-ms}

#######  ns-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_e1700c12

[]{#fs-la-icp-ms}

######  fs-LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range,
introduced into an inductively coupled plasma to atomize and ionize
the sample for inlet to mass analyzer.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_0cd648d6

[]{#ns-la-icp-ms}

######  ns-LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range,
introduced into an inductively coupled plasma to atomize and ionize
the sample for inlet to mass analyzer.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** http://vocab.terralid.org#c_19f6f6d5

[]{#atomic-absorption-spectroscopy}

###  atomic absorption spectroscopy
- **Definition**: Analytical methods using the characteristic optical
absorption of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q655346 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d1ac5ad6

[]{#aas-(glow-discharge)}

####  AAS (glow-discharge)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by glow-
discharge.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ea3b1b8c

[]{#aas-(flame)}

####  AAS (flame)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by a flame.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d7db2dd2

[]{#aas-(graphite-furnace)}

####  AAS (graphite furnace)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by a graphite
furnace.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Alternate labels:**
  - ET-AAS
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/electrothermalabsorptionspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8d344a67

[]{#emission-spectrometry}

###  emission spectrometry
- **Definition**: Analytical methods using the characteristic optical
emission of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1651219 (exactMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/emissionspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3d79fcf3

[]{#oes-(spark)}

####  OES (spark)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Heat is induced through an electric
spark.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - https://www.wikidata.org/wiki/Q186548 (broadMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/opticalemissionspectrometry (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_3687738e

[]{#oes-(icp)}

####  OES (ICP)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Sample is heated in a inductively coupled
plasma.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Alternate labels:**
  - AES (ICP)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - https://www.wikidata.org/wiki/Q186548 (closeMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/plasmaopticalemissionspectrometry (closeMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmaopticalemissionspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q186548 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_67246a66

[]{#aes-(graphite-furnace)}

####  AES (graphite furnace)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Sample is heated in a graphite furnace.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - https://www.wikidata.org/wiki/Q186548 (closeMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/plasmaemissionspectrometry (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_0a6e5db7

[]{#aes-(flame)}

####  AES (flame)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Heat is induced by a flame.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - https://www.wikidata.org/wiki/Q186548 (closeMatch)
  - https://w3id.org/geochem/1.0/analyticalmethod/flameemissionspectrometry (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c7c72d4

[]{#x-ray-spectrometry}

###  X-ray spectrometry
- **Definition**: Analytical methods using the characteristic X-ray
spectra of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/xrayspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q901775 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f7856e7e

[]{#ed-xrf}

####  ED-XRF
- **Definition**: Determination of the chemical composition by the
energy dispersive spectroscopy of X-ray fluorescence.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q112259854 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a6a0ae84

[]{#pxrf}

#####  pXRF
- **Definition**: Determination of the chemical composition by the
energy dispersive spectroscopy of X-ray fluorescence with a handheld
instrument.
- **Child of**:
  - [`ED-XRF`](#ed-xrf)
- **Alternate labels:**
  - hhXRF
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry (broadMatch)
  - https://www.wikidata.org/wiki/Q112259854 (broadMatch)
- **Concept URI:** http://vocab.terralid.org#c_f1be908f

[]{#wd-xrf}

####  WD-XRF
- **Definition**: Determination of the chemical composition by the
wavelength dispersive spectroscopy of X-ray fluorescence.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/wavelengthdispersiveelectroninducedxrayspectrometry (closeMatch)
  - https://www.wikidata.org/wiki/Q899530 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_85bc0576

[]{#epma}

####  EPMA
- **Definition**: Determination of the chemical composition by
electron-induced wavelength dispersive X-ray spectrometry in a
microprobe.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Alternate labels:**
  - microprobe
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/quantitativeanalysiselectroninducedxrayspectrometry (exactMatch)
  - https://www.wikidata.org/wiki/Q911272 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_912285bf

[]{#sem-eds}

####  SEM-EDS
- **Definition**: Determination of the chemical composition by
electron-induced energy-dispersive X-ray spectrometry in a scanning
electron microscope.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Alternate labels:**
  - SEM-EDX
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/energydispersiveelectroninducedxrayspectrometry (closeMatch)
  - https://www.wikidata.org/wiki/Q321095 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2344bc38

[]{#wet-chemistry}

###  wet chemistry
- **Definition**: Determination of the chemical composition by
traditional chemical methods.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/wetchemistry (exactMatch)
  - https://www.wikidata.org/wiki/Q2963660 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4bf47ef2

[]{#naa}

###  NAA
- **Definition**: The determination of chemical concentrations from
the radioactivity produced by the sample material after its
irradiation with neutrons through comparison with the radioactivity
measured in standard materials of comparable sample matrix.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Alternate labels:**
  - neutron activation analysis
- **Matches:**
  - https://w3id.org/geochem/1.0/analyticalmethod/neutronactivationanalysis (exactMatch)
  - http://vocab.getty.edu/aat/300081742 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4a54f6dc


[]{#mass-bias-correction}

##  mass bias correction
- **Definition**: The mathematical model or procedure used to correct
for the fractionation of an isotope ratio during measurement.
- **Child of**:
  - [`méthodes`](#méthodes)
- **Concept URI:** http://vocab.terralid.org#c_5f1716a4

[]{#linear-model}

###  linear model
- **Definition**: A mathematical model assuming a linear relationship
between the isotope ratio of the sample and a different isotope ratio
of an internal standard added to the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** http://vocab.terralid.org#c_39d3b302

[]{#double-spike}

###  double-spike
- **Definition**: The correction of an isotope ratio's mass bias by
altering the abundance of two other isotopes of the same element
through the addition of an enriched isotopic spike
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.chemgeo.2009.05.010](https://doi.org/10.1016/j.chemgeo.2009.05.010)
- **Concept URI:** http://vocab.terralid.org#c_7b213d83

[]{#standard-sample-bracketing}

###  standard-sample bracketing
- **Definition**: The correction of an isotope ratio's mass bias in a
sample by extrapolation from measurements of the same isotope ratio in
an external standard measured before and after the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** http://vocab.terralid.org#c_725495a8

[]{#power-law}

###  power law
- **Definition**: A mathematical model assuming a power-relationship
between the isotope ratio of the sample and a different isotope ratio
of an internal standard added to the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** http://vocab.terralid.org#c_17be86eb

[]{#exponential-law}

###  exponential law
- **Definition**: A mathematical model assuming an exponential
relationship between the isotope ratio of the sample and a different
isotope ratio of an internal standard added to the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **Alternate labels:**
  - Russell model
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** http://vocab.terralid.org#c_e9b3f7f1


[]{#reference-material}

##  reference material
- **Definition**: A reference material (RM) is a material that is
sufficiently stable and homogeneous in one or more of its properties
and whose use for the calibration of measurements has been
established. A certified reference material (CRM) is characterised by
metrologically valid procedures for one or more specified properties
and is accompanied by a certificate for this characterisation.
Standard reference material" (SRM) is a trademarked term for CRMs
satisfying additional criteria specified by the United States National
Institute of Standards and Technology (NIST).
- **Child of**:
  - [`materials`](#materials)
- **Matches:**
  - https://www.wikidata.org/wiki/Q906323 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c7d45a2d

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#other}

###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`object material`](#object-material)
  - [`reference material`](#reference-material)
  - [`analytical instrument`](#analytical-instrument)
  - [`alteration process`](#alteration-process)
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_ebc979f8

[]{#tl-isotope-crms}

###  Tl isotope CRMs
- **Definition**: CRMs used for the calibration of thallium isotope
measurements.
- **Child of**:
  - [`reference material`](#reference-material)
- **Concept URI:** http://vocab.terralid.org#c_1041fd60

[]{#erm-ae649}

####  ERM-AE649
- **Definition**: Thallium isotope CRM prepared by the Joint Research
Centre Institute for Reference Materials and Measurements of the
European Commission.
- **Child of**:
  - [`Tl isotope CRMs`](#tl-isotope-crms)
- **Alternate labels:**
  - IRMM-649
- **References**:
  - [https://crm.jrc.ec.europa.eu/en/crms/ERM-AE649](https://crm.jrc.ec.europa.eu/en/crms/ERM-AE649)
- **Concept URI:** http://vocab.terralid.org#c_bf10432d

[]{#nist-srm-997}

####  NIST SRM 997
- **Definition**: Thallium isotope CRM prepared from commercially
available high purity thallium metal.
- **Child of**:
  - [`Tl isotope CRMs`](#tl-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/archives/997.pdf](https://tsapps.nist.gov/srmext/certificates/archives/997.pdf)
- **Concept URI:** http://vocab.terralid.org#c_7a5dc24d

[]{#pb-isotope-crms}

###  Pb Isotope CRMs
- **Definition**: Reference materials used for the calibration of lead
isotope measurement.
- **Child of**:
  - [`reference material`](#reference-material)
- **Concept URI:** http://vocab.terralid.org#c_cb977df5

[]{#nist-srm-981}

####  NIST SRM 981
- **Definition**: Lead isotope CRM prepared from commercially
available high purity lead metal.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/archives/981.pdf](https://tsapps.nist.gov/srmext/certificates/archives/981.pdf)
- **Concept URI:** http://vocab.terralid.org#c_8bafd421

[]{#nist-srm-610}

####  NIST SRM 610
- **Definition**: Trace element CRM prepared from synthetic glass
widely used for the measurement of lead isotope ratios with laser
ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/612.pdf](https://tsapps.nist.gov/srmext/certificates/612.pdf)
- **Concept URI:** http://vocab.terralid.org#c_bc05e76c

[]{#nist-srm-612}

####  NIST SRM 612
- **Definition**: Trace element CRM prepared from synthetic glass used
for the measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/612.pdf](https://tsapps.nist.gov/srmext/certificates/612.pdf)
- **Concept URI:** http://vocab.terralid.org#c_18a8ec86

[]{#nist-srm-614}

####  NIST SRM 614
- **Definition**: Trace element CRM prepared from synthetic glass used
for the measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/614.pdf](https://tsapps.nist.gov/srmext/certificates/614.pdf)
- **Concept URI:** http://vocab.terralid.org#c_1d25bfbf

[]{#nist-srm-3328}

####  NIST SRM 3328
- **Definition**: Lead isotope CRM prepared from NIST SRM 981, for
which it defines the delta-scale.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/3328.pdf](https://tsapps.nist.gov/srmext/certificates/3328.pdf)
- **Concept URI:** http://vocab.terralid.org#c_2fd6cc95

[]{#bhvo-2}

####  BHVO-2
- **Definition**: Reference material prepared by the USGS from the
surface layer of pahoehoe lava that overflowed from the Halemaumau
Crater in the Kilauea Caldera (Hawaii, USA).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bhvo-2-geochemical-reference-material-information-sheet](https://www.usgs.gov/media/files/bhvo-2-geochemical-reference-material-information-sheet)
- **Concept URI:** http://vocab.terralid.org#c_e2f20350

[]{#bhvo-2g}

#####  BHVO-2G
- **Definition**: Synthethic glass prepared from BHVO-2 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BHVO-2`](#bhvo-2)
- **References**:
  - [https://www.usgs.gov/media/files/bhvo-2g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bhvo-2g-microanalysis-reference-material-information-sheet)
- **Concept URI:** http://vocab.terralid.org#c_638c273b

[]{#bir-1}

####  BIR-1
- **Definition**: Reference material prepared by the USGS from
interglacial lava flows referred to as Rekjavik dolerites (Iceland).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bir-1-and-bir-1a-geochemical-reference-material-information-sheet](https://www.usgs.gov/media/files/bir-1-and-bir-1a-geochemical-reference-material-information-sheet)
- **Concept URI:** http://vocab.terralid.org#c_09290acc

[]{#bir-1g}

#####  BIR-1G
- **Definition**: Synthethic glass prepared from BIR-1 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BIR-1`](#bir-1)
- **References**:
  - [https://www.usgs.gov/media/files/bir-1g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bir-1g-microanalysis-reference-material-information-sheet)
- **Concept URI:** http://vocab.terralid.org#c_ab7e838c

[]{#bcr-2}

####  BCR-2
- **Definition**: Reference material prepared by the USGS from basalts
in the Bridal Veil Flow Quarry close to the Columbia River (Oregon,
USA).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bcr-2-geochemical-reference-material-information-sheet-0](https://www.usgs.gov/media/files/bcr-2-geochemical-reference-material-information-sheet-0)
- **Concept URI:** http://vocab.terralid.org#c_494f507e

[]{#bcr-2g}

#####  BCR-2G
- **Definition**: Synthethic glass prepared from BCR-2 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BCR-2`](#bcr-2)
- **References**:
  - [https://www.usgs.gov/media/files/bcr-2g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bcr-2g-microanalysis-reference-material-information-sheet)
- **Concept URI:** http://vocab.terralid.org#c_d365f198

[]{#erm-3800}

####  ERM-3800
- **Definition**: Lead isotope CRM prepared to provide a CRM with
sufficient isotopic homogeneity to measure differences in the isotopic
composition on the delta-scale.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://doi.org/10.1039/B821400J](https://doi.org/10.1039/B821400J)
- **Concept URI:** http://vocab.terralid.org#c_910cb973

[]{#gsd-1}

####  GSD-1
- **Definition**: Reference material prepared by the Institute of
Geophysical and Geochemical Exploration (IGGE) from a stream sediment
sample collected from a tributary flowing through biotitic granite in
Shanxi province (China).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://doi.org/10.1111/j.1751-908X.1985.tb00439.x](https://doi.org/10.1111/j.1751-908X.1985.tb00439.x)
- **Concept URI:** http://vocab.terralid.org#c_f3131ccc

[]{#gsd-1g}

#####  GSD-1G
- **Definition**: Synthethic glass prepared from GSD-1 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`GSD-1`](#gsd-1)
- **References**:
  - [https://doi.org/10.1111/j.1751-908X.2005.tb00903.x](https://doi.org/10.1111/j.1751-908X.2005.tb00903.x)
  - [https://doi.org/10.1111/j.1751-908X.2010.00114.x](https://doi.org/10.1111/j.1751-908X.2010.00114.x)
- **Concept URI:** http://vocab.terralid.org#c_f1060ba4


[]{#lead-isotope-age-model}

##  lead isotope age model
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Concept URI:** http://vocab.terralid.org#c_435c9bf2

[]{#sk75}

###  SK75
- **Definition**: The two-stage lead isotope age model according to
Stacey, J.S. and Kramers, J.D. (1975) Approximation of terrestrial
lead isotope evolution by a two-stage model. Earth and Planetary
Science Letters 26(2), pp. 207–221.
https://dx.doi.org/10.1016/0012-821X(75)90088-6
- **Child of**:
  - [`lead isotope age model`](#lead-isotope-age-model)
- **References**:
  - [https://doi.org/10.1016/0012-821X(75)90088-6](https://doi.org/10.1016/0012-821X(75)90088-6)
- **Concept URI:** http://vocab.terralid.org#c_10c030b1

[]{#cr75}

###  CR75
- **Definition**: The single-stage lead isotope age model according to
Cumming, G.L. and Richards, J.R. (1975) Ore lead isotope ratios in a
continuously changing earth. Earth and Planetary Science Letters
28(2), pp. 155–171. https://dx.doi.org/10.1016/0012-821X(75)90223-X
- **Child of**:
  - [`lead isotope age model`](#lead-isotope-age-model)
- **References**:
  - [https://doi.org/10.1016/0012-821X(75)90223-X](https://doi.org/10.1016/0012-821X(75)90223-X)
- **Concept URI:** http://vocab.terralid.org#c_b80ae0f4

[]{#aj84}

###  AJ84
- **Definition**: The two-stage lead isotope age model according to
Albarède, F. and Juteau, M. (1984) Unscrambling the lead model ages.
Geochimica et Cosmochimica Acta 48(1), pp. 207–212.
https://dx.doi.org/10.1016/0016-7037(84)90364-8
- **Child of**:
  - [`lead isotope age model`](#lead-isotope-age-model)
- **References**:
  - [https://doi.org/10.1016/0016-7037(84)90364-8](https://doi.org/10.1016/0016-7037(84)90364-8)
- **Concept URI:** http://vocab.terralid.org#c_a299bc22


[]{#analytical-instrument}

##  analytical instrument
- **Definition**: Specialized devices used to determine the chemical
or physical properties of substances, especially their composition,
qunatity, or structure.
- **Matches:**
  - https://www.wikidata.org/wiki/Q112270652 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2490c7e3

[]{#other}

###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`object material`](#object-material)
  - [`reference material`](#reference-material)
  - [`analytical instrument`](#analytical-instrument)
  - [`alteration process`](#alteration-process)
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_ebc979f8

[]{#instrument-manufacturer}

###  instrument manufacturer
- **Child of**:
  - [`groups`](#groups)
  - [`analytical instrument`](#analytical-instrument)
- **Concept URI:** http://vocab.terralid.org#c_79130afd

[]{#thermo-fisher-scientific}

####  Thermo Fisher Scientific
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_f6af165b

[]{#neoma}

#####  Neoma
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** http://vocab.terralid.org#c_b0bfa4f8

[]{#neptune}

#####  Neptune
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** http://vocab.terralid.org#c_048dcdb6

[]{#neptune-plus}

#####  Neptune Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** http://vocab.terralid.org#c_29e86132

[]{#triton-xt}

#####  Triton XT
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** http://vocab.terralid.org#c_881a6a1f

[]{#triton-plus}

#####  Triton Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** http://vocab.terralid.org#c_11b1262d

[]{#nu-instruments}

####  Nu Instruments
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_aef60277

[]{#plasma-1700}

#####  Plasma 1700
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** http://vocab.terralid.org#c_2d9b9705

[]{#plasma-3}

#####  Plasma 3
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** http://vocab.terralid.org#c_a5774803

[]{#sapphire}

#####  Sapphire
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** http://vocab.terralid.org#c_87e243c3

[]{#sapphire-xd}

#####  Sapphire XD
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** http://vocab.terralid.org#c_1d17aebe

[]{#tims-(nu-instruments)}

#####  TIMS (Nu instruments)
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** http://vocab.terralid.org#c_5a56c39c

[]{#selmi}

####  SELMI
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_17ef5068

[]{#mi-1201-at}

#####  MI 1201-AT
- **Child of**:
  - [`SELMI`](#selmi)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** http://vocab.terralid.org#c_a81ab232

[]{#uralpribor}

####  Uralpribor
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_0979c452

[]{#mit-350-tm}

#####  MIT 350-TM
- **Child of**:
  - [`Uralpribor`](#uralpribor)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** http://vocab.terralid.org#c_48c98090

[]{#micromass}

####  Micromass
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_e95a8b9d

[]{#sector-54}

#####  Sector 54
- **Child of**:
  - [`Micromass`](#micromass)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** http://vocab.terralid.org#c_00ccd58e

[]{#isotopx}

####  Isotopx
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_2b64e1c4

[]{#phoenix}

#####  Phoenix
- **Child of**:
  - [`Isotopx`](#isotopx)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** http://vocab.terralid.org#c_901bf3f2

[]{#gv-instruments}

####  GV Instruments
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_42fb87d6

[]{#isoprobe-p}

#####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** http://vocab.terralid.org#c_b04217d9

[]{#isoprobe-t}

#####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** http://vocab.terralid.org#c_35bf64c9

[]{#finnigan-mat}

####  Finnigan MAT
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_02cf051c

[]{#mat-262}

#####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** http://vocab.terralid.org#c_5339ea48

[]{#mstech-group}

####  MSTech Group
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_de754362

[]{#zms-df-tims-01}

#####  ZMS DF-TIMS-01
- **Child of**:
  - [`MSTech Group`](#mstech-group)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** http://vocab.terralid.org#c_52fa5991

[]{#kunyuan-instrument}

####  Kunyuan Instrument
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** http://vocab.terralid.org#c_f24d7f45

[]{#gb-tims}

#####  GB-TIMS
- **Child of**:
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** http://vocab.terralid.org#c_44b7c5d2

[]{#instrument-model}

###  instrument model
- **Child of**:
  - [`objetos móveis`](#objetos-móveis)
  - [`analytical instrument`](#analytical-instrument)
- **Other Properties:**
  - **note**: 
https://analyte.me/instrument/gb-tims
- **Concept URI:** http://vocab.terralid.org#c_345d9da9

[]{#neoma}

####  Neoma
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** http://vocab.terralid.org#c_b0bfa4f8

[]{#neptune}

####  Neptune
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** http://vocab.terralid.org#c_048dcdb6

[]{#neptune-plus}

####  Neptune Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** http://vocab.terralid.org#c_29e86132

[]{#plasma-1700}

####  Plasma 1700
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** http://vocab.terralid.org#c_2d9b9705

[]{#plasma-3}

####  Plasma 3
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** http://vocab.terralid.org#c_a5774803

[]{#sapphire}

####  Sapphire
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** http://vocab.terralid.org#c_87e243c3

[]{#sapphire-xd}

####  Sapphire XD
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** http://vocab.terralid.org#c_1d17aebe

[]{#isoprobe-p}

####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** http://vocab.terralid.org#c_b04217d9

[]{#mat-262}

####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** http://vocab.terralid.org#c_5339ea48

[]{#mi-1201-at}

####  MI 1201-AT
- **Child of**:
  - [`SELMI`](#selmi)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** http://vocab.terralid.org#c_a81ab232

[]{#mit-350-tm}

####  MIT 350-TM
- **Child of**:
  - [`Uralpribor`](#uralpribor)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** http://vocab.terralid.org#c_48c98090

[]{#sector-54}

####  Sector 54
- **Child of**:
  - [`Micromass`](#micromass)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** http://vocab.terralid.org#c_00ccd58e

[]{#phoenix}

####  Phoenix
- **Child of**:
  - [`Isotopx`](#isotopx)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** http://vocab.terralid.org#c_901bf3f2

[]{#tims-(nu-instruments)}

####  TIMS (Nu instruments)
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** http://vocab.terralid.org#c_5a56c39c

[]{#zms-df-tims-01}

####  ZMS DF-TIMS-01
- **Child of**:
  - [`MSTech Group`](#mstech-group)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** http://vocab.terralid.org#c_52fa5991

[]{#triton-xt}

####  Triton XT
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** http://vocab.terralid.org#c_881a6a1f

[]{#triton-plus}

####  Triton Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** http://vocab.terralid.org#c_11b1262d

[]{#gb-tims}

####  GB-TIMS
- **Child of**:
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** http://vocab.terralid.org#c_44b7c5d2

[]{#isoprobe-t}

####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** http://vocab.terralid.org#c_35bf64c9

[]{#instrument-type}

###  instrument type
- **Child of**:
  - [`analytical instrument`](#analytical-instrument)
- **Concept URI:** http://vocab.terralid.org#c_e3df0ac6

[]{#mc-icp-ms-(instrument)}

####  MC-ICP-MS (instrument)
- **Child of**:
  - [`instrument type`](#instrument-type)
- **Concept URI:** http://vocab.terralid.org#c_4c5dbb51

[]{#neoma}

#####  Neoma
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** http://vocab.terralid.org#c_b0bfa4f8

[]{#neptune}

#####  Neptune
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** http://vocab.terralid.org#c_048dcdb6

[]{#neptune-plus}

#####  Neptune Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** http://vocab.terralid.org#c_29e86132

[]{#plasma-1700}

#####  Plasma 1700
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** http://vocab.terralid.org#c_2d9b9705

[]{#plasma-3}

#####  Plasma 3
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** http://vocab.terralid.org#c_a5774803

[]{#sapphire}

#####  Sapphire
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** http://vocab.terralid.org#c_87e243c3

[]{#sapphire-xd}

#####  Sapphire XD
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** http://vocab.terralid.org#c_1d17aebe

[]{#isoprobe-p}

#####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** http://vocab.terralid.org#c_b04217d9

[]{#tims-(instrument)}

####  TIMS (instrument)
- **Child of**:
  - [`instrument type`](#instrument-type)
- **Concept URI:** http://vocab.terralid.org#c_75732fae

[]{#mat-262}

#####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** http://vocab.terralid.org#c_5339ea48

[]{#mi-1201-at}

#####  MI 1201-AT
- **Child of**:
  - [`SELMI`](#selmi)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** http://vocab.terralid.org#c_a81ab232

[]{#mit-350-tm}

#####  MIT 350-TM
- **Child of**:
  - [`Uralpribor`](#uralpribor)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** http://vocab.terralid.org#c_48c98090

[]{#sector-54}

#####  Sector 54
- **Child of**:
  - [`Micromass`](#micromass)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** http://vocab.terralid.org#c_00ccd58e

[]{#phoenix}

#####  Phoenix
- **Child of**:
  - [`Isotopx`](#isotopx)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** http://vocab.terralid.org#c_901bf3f2

[]{#tims-(nu-instruments)}

#####  TIMS (Nu instruments)
- **Child of**:
  - [`Nu Instruments`](#nu-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** http://vocab.terralid.org#c_5a56c39c

[]{#zms-df-tims-01}

#####  ZMS DF-TIMS-01
- **Child of**:
  - [`MSTech Group`](#mstech-group)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** http://vocab.terralid.org#c_52fa5991

[]{#triton-xt}

#####  Triton XT
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** http://vocab.terralid.org#c_881a6a1f

[]{#triton-plus}

#####  Triton Plus
- **Child of**:
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** http://vocab.terralid.org#c_11b1262d

[]{#gb-tims}

#####  GB-TIMS
- **Child of**:
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** http://vocab.terralid.org#c_44b7c5d2

[]{#isoprobe-t}

#####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** http://vocab.terralid.org#c_35bf64c9


[]{#abundance-(concentration)}

##  abundance (concentration)
- **Definition**: A qualitative classification for the quantity of a
compund based on its concentration.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Concept URI:** http://vocab.terralid.org#c_60b698fb

[]{#major}

###  major
- **Definition**: Compound with a concentration of more than 0.4 wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** http://vocab.terralid.org#c_0e342dcb

[]{#minor}

###  minor
- **Definition**: Compound with a concentration between 0.4 and 0.1
wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** http://vocab.terralid.org#c_e954a190

[]{#trace}

###  trace
- **Definition**: Compound with a concentration of less than 0.1 wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** http://vocab.terralid.org#c_29d78b2d


[]{#alteration-extent}

##  alteration extent
- **Definition**: The degree of the material's alteration.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Concept URI:** http://vocab.terralid.org#c_4e14cebd

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#severe-alteration}

###  severe alteration
- **Definition**: The material is altered to an extent that it is very
difficult or impossible to retrieve pristine material for analysis.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** http://vocab.terralid.org#c_a9cb8f24

[]{#slight-alteration}

###  slight alteration
- **Definition**: The material is altered but includes enough pristine
material for analyses.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** http://vocab.terralid.org#c_e935826d

[]{#no-alteration}

###  no alteration
- **Definition**: The material does not show any indication of
alteration.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** http://vocab.terralid.org#c_eb1223d0


[]{#production-context}

##  production context
- **Definition**: Classification for the type of raw materials used in
the production of the object.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Concept URI:** http://vocab.terralid.org#c_f5cb57a0

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#primary}

###  primary
- **Definition**: The material was not altered after its initial
production from raw materials.
- **Child of**:
  - [`production context`](#production-context)
- **Concept URI:** http://vocab.terralid.org#c_80dcdedf

[]{#secondary}

###  secondary
- **Definition**: The material was not directly derived from its raw
materials but represent the re-use (mixing, recycling) of materials.
- **Child of**:
  - [`production context`](#production-context)
- **Concept URI:** http://vocab.terralid.org#c_d179db0a


[]{#recycling-indicator}

##  recycling indicator
- **Definition**: Classification to indicate whether an object shows
signs of being a recycling product.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Concept URI:** http://vocab.terralid.org#c_e4626b4d

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#recycling-suspected}

###  recycling suspected
- **Definition**: Indications for a conversion of one or several
materials into the object exist but do not warrant a confirmation.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Concept URI:** http://vocab.terralid.org#c_08e80a7e

[]{#not-recycled}

###  not recycled
- **Definition**: The material is not the result of re-using other
materials.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Concept URI:** http://vocab.terralid.org#c_3a6292d6

[]{#recycled}

###  recycled
- **Definition**: One or several materials were converted into the
object.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Matches:**
  - http://resource.geosciml.org/classifier/cgi/end-use-potential/recycling (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d1e3b55d


[]{#corrosion-extent}

##  corrosion extent
- **Definition**: The degree to which a material is affected by
corrosion.
- **Concept URI:** http://vocab.terralid.org#c_3ba0ff02

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#severe-corrosion}

###  severe corrosion
- **Definition**: The material consists mostly of corrosion products
and it requires close observation to find uncorroded material.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** http://vocab.terralid.org#c_372633f8

[]{#moderate-corrosion}

###  moderate corrosion
- **Definition**: Corrosion products are widely present but uncorroded
material can still be readily found.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** http://vocab.terralid.org#c_1dba855c

[]{#weak-corrosion}

###  weak corrosion
- **Definition**: The material has only surficial or spatially very
limited corrosion.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** http://vocab.terralid.org#c_bb54a1e5

[]{#no-corrosion}

###  no corrosion
- **Definition**: The material does not show any indication of
corrosion.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** http://vocab.terralid.org#c_16a7b2ad


[]{#glass-component}

##  glass component
- **Definition**: The general ingredients creating a glass.
- **Concept URI:** http://vocab.terralid.org#c_e96ca20e

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#opacifier}

###  opacifier
- **Definition**: The component of the glass decreasing its
transparency.
- **Child of**:
  - [`glass component`](#glass-component)
- **Matches:**
  - https://www.wikidata.org/wiki/Q7095513 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6b636b3a

[]{#network-modifier}

###  network modifier
- **Definition**: The component of the glass regulating the length of
the chains build by the network former.
- **Child of**:
  - [`glass component`](#glass-component)
- **Concept URI:** http://vocab.terralid.org#c_5a103a06

[]{#network-former}

###  network former
- **Definition**: The component of the glass creating the network of
chains the glass is build of.
- **Child of**:
  - [`glass component`](#glass-component)
- **Alternate labels:**
  - silica, 
  - sand, 
- **Concept URI:** http://vocab.terralid.org#c_3e5b4e78

[]{#colorant}

###  colorant
- **Definition**: The colour-giving constituent of a pigment or glass.
- **Child of**:
  - [`glass component`](#glass-component)
  - [`pigment component`](#pigment-component)
- **Matches:**
  - https://www.wikidata.org/wiki/Q911922 (exactMatch)
  - http://vocab.getty.edu/aat/300013026 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4e57487f


[]{#compound-type}

##  compound type
- **Definition**: The chemical nature of a compound.
- **Concept URI:** http://vocab.terralid.org#c_f09f29c5

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#mixed-compound-types}

###  mixed compound types
- **Definition**: The material consists of inorganic and organic
chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300206579 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d97d70ac

[]{#organic}

###  organic
- **Definition**: The material consists of organic (i.e. carbon-based)
chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300191632 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_627d4ccf

[]{#inorganic}

###  inorganic
- **Definition**: The material consists of inorganic (i.e. not carbon-
based) chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - http://vocab.getty.edu/aat/300191633 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2211a2a4


[]{#compound-origin}

##  compound origin
- **Definition**: Information whether the compound can be found in
nature or is of articial origin.
- **Concept URI:** http://vocab.terralid.org#c_786deece

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#mixed-compound-origin}

###  mixed compound origin
- **Definition**: The material consists of natural and sythetic
compounds.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Concept URI:** http://vocab.terralid.org#c_29195cbf

[]{#synthetic}

###  synthetic
- **Definition**: The material's compounds were created by humans from
other constituents.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Alternate labels:**
  - artifical
- **Matches:**
  - http://vocab.getty.edu/aat/300218678 (closeMatch)
  - http://vocab.getty.edu/aat/300191749 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d140627e

[]{#natural}

###  natural
- **Definition**: The material's compounds occur in nature.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Matches:**
  - http://vocab.getty.edu/aat/300219527 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dc16b4b3


[]{#pigment-component}

##  pigment component
- **Definition**: The general ingredients creating a pigment.
- **Concept URI:** http://vocab.terralid.org#c_924da16f

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#various}

###  various
- **Definition**: It is not possible to differentiate between the
components of the pigment anymore.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Concept URI:** http://vocab.terralid.org#c_31227633

[]{#impurity}

###  impurity
- **Definition**: Material unintentionally included in the pigment.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - http://vocab.getty.edu/aat/300223750 (exactMatch)
  - https://www.wikidata.org/wiki/Q7216430 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e3a64656

[]{#binder}

###  binder
- **Definition**: The part of the pigment that holds the colour-giving
parts together and adheres them to the surface.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - http://vocab.getty.edu/aat/300014720 (exactMatch)
  - https://www.wikidata.org/wiki/Q863583 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_acda28e6

[]{#colorant}

###  colorant
- **Definition**: The colour-giving constituent of a pigment or glass.
- **Child of**:
  - [`glass component`](#glass-component)
  - [`pigment component`](#pigment-component)
- **Matches:**
  - https://www.wikidata.org/wiki/Q911922 (exactMatch)
  - http://vocab.getty.edu/aat/300013026 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4e57487f

[]{#flux}

###  flux
- **Definition**: Material added to another material to lower its
melting point.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - http://vocab.getty.edu/aat/300015137 (exactMatch)
  - https://www.wikidata.org/wiki/Q1134475 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c5cb1257


[]{#alteration-process}

##  alteration process
- **Definition**: The process of changing a material.
- **Matches:**
  - http://vocab.getty.edu/aat/300105442 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8469dc11

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#other}

###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`object material`](#object-material)
  - [`reference material`](#reference-material)
  - [`analytical instrument`](#analytical-instrument)
  - [`alteration process`](#alteration-process)
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_ebc979f8

[]{#photodegradation}

###  photodegradation
- **Definition**: The alteration of materials by light.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300379409 (exactMatch)
  - https://www.wikidata.org/wiki/Q1902073 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f87cfd32

[]{#oxidation}

###  oxidation
- **Definition**: The reaction of the material with oxygen.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300220235 (exactMatch)
  - https://www.wikidata.org/wiki/Q1786087 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee0c9aa1

[]{#erosion}

###  erosion
- **Definition**: The loss of material through surface processes and
its deposition elsewhere.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300054116 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dab8858f

[]{#biodegradation}

###  biodegradation
- **Definition**: The breakdown of usually organic matter by
microorganisms.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300419379 (exactMatch)
  - https://www.wikidata.org/wiki/Q696715 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_226caccd

[]{#darkening}

###  darkening
- **Definition**: The loss of the materials brightness and depth.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300379491 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3ad03b3e

[]{#efflorescense}

###  efflorescense
- **Definition**: The migration of salt to the surface of a (porous)
material.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Concept URI:** http://vocab.terralid.org#c_8855f5a4

[]{#flaking}

###  flaking
- **Definition**: The loss of adhesion of paint from its substrate
often but not necessarily in response to changes in the environment
like humidity or temperature.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q117289087 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fdeb0d6c


[]{#colour-system}

##  colour system
- **Definition**: Definition of a geometrical space or nomenclature
that represents colours.
- **Matches:**
  - http://vocab.getty.edu/aat/300311091 (exactMatch)
  - https://www.wikidata.org/wiki/Q1396457 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_49d4f3c8

[]{#eye}

###  eye
- **Definition**: The colour as perceived by a person.
- **Child of**:
  - [`colour system`](#colour-system)
- **Matches:**
  - https://www.wikidata.org/wiki/Q7364 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_63dd4d16

[]{#munsell}

###  Munsell
- **Definition**: A colour system developed by A. H. Munsell in the
early 20th century.
- **Child of**:
  - [`colour system`](#colour-system)
- **Matches:**
  - https://www.wikidata.org/wiki/Q768549 (exactMatch)
  - http://vocab.getty.edu/aat/300311089 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ffd62f45

[]{#cielab}

###  CIELAB
- **Definition**: A colour system defined by the International
Commission on Illumination, expressing colour in a three-dimensional
space with lightness (L*), red-green (A*), and blue-yellow (b*) as
axes.
- **Child of**:
  - [`colour system`](#colour-system)
- **Alternate labels:**
  - L*a*b*
- **Matches:**
  - https://www.wikidata.org/wiki/Q375414 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4f63611c


[]{#contributortype}

##  contributorType
- **Definition**: The type of contributor of the resource.
- **Child of**:
  - [`roles of individuals`](#roles-of-individuals)
- **Other Properties:**
  - **note**: 
This is a reproduction of the controlled list contributorType in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/)
- **Concept URI:** http://vocab.terralid.org#c_e4ed600b

[]{#other-(contributortype)}

###  Other (contributorType)
- **Definition**: Any person or institution making a significant
contribution to the development and/or maintenance of the resource,
but whose contribution is not adequately described by any of the other
values for contributorType.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
Could be a photographer, artist, or writer whose contribution helped to publicize the resource (as opposed to creating it), a reviewer of the resource, someone providing administrative services to the author (such as depositing updates into an online repository, analysing usage, etc.), or one of many other roles.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#other](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#other)
- **Concept URI:** http://vocab.terralid.org#c_3a208ae6

[]{#workpackageleader}

###  WorkPackageLeader
- **Definition**: A Work Package is a recognized data product, not all
of which is included in publication. The package, instead, may include
notes, discarded documents, etc. The Work Package Leader is
responsible for ensuring the comprehensive contents, versioning, and
availability of the Work Package during the development of the
resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#workpackageleader](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#workpackageleader)
- **Concept URI:** http://vocab.terralid.org#c_50da8fc6

[]{#translator}

###  Translator
- **Definition**: A person, organization, or automated system
responsible for converting the content of a resource from one language
into another, preserving its meaning and intended message.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
This contributor type should be applied to DOI metadata for a resource which has been translated from another resource.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q333634 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#translator](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#translator)
- **Concept URI:** http://vocab.terralid.org#c_79574dab

[]{#supervisor}

###  Supervisor
- **Definition**: Designated administrator over one or more
groups/teams working to produce a resource, or over one or more steps
of a development process.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#supervisor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#supervisor)
- **Concept URI:** http://vocab.terralid.org#c_2f9a64df

[]{#sponsor}

###  Sponsor
- **Definition**: Person or organisation that issued a contract or
under the auspices of which a work has been written, printed,
published, developed, etc.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
Includes organisations that provide in-kind support, through donation, provision of people or a facility or instrumentation necessary for the development of the resource, etc.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#sponsor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#sponsor)
- **Concept URI:** http://vocab.terralid.org#c_8ff2aeb0

[]{#rightsholder}

###  RightsHolder
- **Definition**: Person or institution owning or managing property
rights, including intellectual property rights over the resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#rightsholder](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#rightsholder)
- **Concept URI:** http://vocab.terralid.org#c_f18d65a2

[]{#researchgroup}

###  ResearchGroup
- **Definition**: Typically refers to a group of individuals with a
lab, department, or division that has a specifically defined focus of
activity.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
May operate at a narrower level of scope; may or may not hold less administrative responsibility than a project team.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1241025 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researchgroup](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researchgroup)
- **Concept URI:** http://vocab.terralid.org#c_57b3dd9a

[]{#researcher}

###  Researcher
- **Definition**: A person involved in analysing data or the results
of an experiment or formal study. May indicate an intern or assistant
to one of the authors who helped with research but who was not so
“key” as to be listed as an author.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
Should be a person, not an institution. Note that a person involved in the gathering of data would fall under the contributorType “DataCollector.” The researcher may find additional data online and correlate it to the data collected for the experiment or study, for example.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1650915 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researcher](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researcher)
- **Concept URI:** http://vocab.terralid.org#c_e1f2cf05

[]{#relatedperson}

###  RelatedPerson
- **Definition**: A person without a specifically defined role in the
development of the resource, but who is someone the author wishes to
recognize.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
This person could be an author’s intellectual mentor, a person providing intellectual leadership in the discipline or subject domain, etc.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#relatedperson](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#relatedperson)
- **Concept URI:** http://vocab.terralid.org#c_ad00bdad

[]{#registrationauthority}

###  RegistrationAuthority
- **Definition**: A standards-setting body from which Registration
Agencies obtain official recognition and guidance.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
The IDF serves as the Registration Authority for the International Standards Organisation (ISO) in the area/domain of Digital Object Identifiers.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#registrationauthority](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#registrationauthority)
- **Concept URI:** http://vocab.terralid.org#c_ebc3e072

[]{#registrationagency}

###  RegistrationAgency
- **Definition**: Institution/organisation officially appointed by a
Registration Authority to handle specific tasks within a defined area
of responsibility.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
DataCite is a Registration Agency for the International DOI Foundation (IDF). One of DataCite’s tasks is to assign DOI prefixes to the allocating agents who then assign the full, specific character string to data clients, provide metadata back to the DataCite registry, etc.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#registrationagency](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#registrationagency)
- **Concept URI:** http://vocab.terralid.org#c_c8f80f6c

[]{#projectmember}

###  ProjectMember
- **Definition**: Person on the membership list of a designated
project/project team.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
This vocabulary may or may not indicate the quality, quantity, or substance of the person’s involvement.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmember](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmember)
- **Concept URI:** http://vocab.terralid.org#c_c6bb8064

[]{#projectmanager}

###  ProjectManager
- **Definition**: Person officially designated as manager of a
project. Project may consist of one or many project teams and sub-
teams.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
The manager of a project normally has more administrative responsibility than actual work involvement.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q816432 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmanager](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmanager)
- **Concept URI:** http://vocab.terralid.org#c_384d11d1

[]{#projectleader}

###  ProjectLeader
- **Definition**: Person officially designated as head of project team
or sub- project team instrumental in the work necessary to development
of the resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
The Project Leader is not “removed” from the work that resulted in the resource; he or she remains intimately involved throughout the life of the particular project team.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectleader](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectleader)
- **Concept URI:** http://vocab.terralid.org#c_dd32fd29

[]{#producer}

###  Producer
- **Definition**: Typically, a person or organisation responsible for
the artistry and form of a media product.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
In the data industry, this may be a company “producing” DVDs that package data for future dissemination by a distributor.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#producer](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#producer)
- **Concept URI:** http://vocab.terralid.org#c_7250b71d

[]{#hostinginstitution}

###  HostingInstitution
- **Definition**: Typically, the organisation allowing the resource to
be available on the internet through the provision of its
hardware/software/operating support.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
This role normally falls on the University, research center or organization where the data center/data repository belongs.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#hostinginstitution](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#hostinginstitution)
- **Concept URI:** http://vocab.terralid.org#c_041e374c

[]{#editor}

###  Editor
- **Definition**: A person who oversees the details related to the
publication format of the resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
If the Editor is to be credited in place of multiple creators, the Editor’s name may be supplied as Creator, with “(Ed.)” appended to the name.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#editor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#editor)
- **Concept URI:** http://vocab.terralid.org#c_36d34fdb

[]{#distributor}

###  Distributor
- **Definition**: Institution tasked with responsibility to
generate/disseminate copies of the resource in either electronic or
print form.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
Works stored in more than one archive/repository may credit each as a distributor.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#distributor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#distributor)
- **Concept URI:** http://vocab.terralid.org#c_62875695

[]{#datamanager}

###  DataManager
- **Definition**: Person (or organisation with a staff of data
managers, such as a data centre) responsible for maintaining the
finished resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
The work done by this person or organisation ensures that the resource is periodically “refreshed” in terms of software/hardware support, is kept available or is protected from unauthorized access, is stored in accordance with industry standards, and is handled in accordance with the records management requirements applicable to it.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datamanager](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datamanager)
- **Concept URI:** http://vocab.terralid.org#c_8034b473

[]{#datacurator}

###  DataCurator
- **Definition**: Person tasked with reviewing, enhancing, cleaning,
or standardizing metadata and the associated data submitted for
storage, use, and maintenance within a data centre or repository.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
While the DataManager is concerned with digital maintenance, the DataCurator’s role encompasses quality assurance focused on content and metadata. DataCurator responsibilities include: checking completeness of the submitted dataset against the content as described by the submitter; verifying standard metadata according to the applicable system or schema; adding or verifying specialized metadata to add value and ensure access across disciplines; and determining how the metadata might map to search engines, database products, and automated feeds. Repository managers as well as data librarians working in the repository fall within this category.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datacurator](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datacurator)
- **Concept URI:** http://vocab.terralid.org#c_eed9b69e

[]{#datacollector}

###  DataCollector
- **Definition**: Person/institution responsible for finding or
gathering/collecting data under the guidelines of the author(s) or
Principal Investigator (PI).
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
May also be used when crediting survey conductors, interviewers, event or condition observers, or persons responsible for monitoring key instrument data.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datacollector](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#datacollector)
- **Concept URI:** http://vocab.terralid.org#c_f5974a2b

[]{#contactperson}

###  ContactPerson
- **Definition**: Person with knowledge of how to access,
troubleshoot, or otherwise field issues related to the resource.
- **Child of**:
  - [`contributorType`](#contributortype)
- **Other Properties:**
  - **scopeNote**: 
May also be the “Point of Contact” in an organisation that controls access to the resource, if that organisation is different from the Publisher, Distributor, and Data Manager.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#contactperson](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#contactperson)
- **Concept URI:** http://vocab.terralid.org#c_34e78a4f


[]{#sample-access}

##  sample access
- **Definition**: General information about whether objects or
materials are available for investigation.
- **Concept URI:** http://vocab.terralid.org#c_6de9e3f7

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#accessible}

###  accessible
- **Definition**: The object or material is generally accessible for
investigation.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** http://vocab.terralid.org#c_06c40941

[]{#policy}

###  policy
- **Definition**: The institution holding the object or material has a
policy regulating access to objects and materials for investigation.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** http://vocab.terralid.org#c_b1cf95c1

[]{#inaccessible}

###  inaccessible
- **Definition**: The object or material is not accessible for
investigation or analysis in general.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** http://vocab.terralid.org#c_fba4dbc9

[]{#destroyed}

###  destroyed
- **Definition**: The object or material was completely destroyed
(e.g., during analysis or in a destruction event) with records for
this event being available.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** http://vocab.terralid.org#c_5df8720f

[]{#lost}

###  lost
- **Definition**: The object or material cannot be localised any more
and its whereabouts cannot be reconstructed.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** http://vocab.terralid.org#c_6e9109c4


[]{#date-type}

##  date type
- **Definition**: Whether a date refers to an archaeological or
geological event or period.
- **Child of**:
  - [`tipos de épocas`](#tipos-de-épocas)
- **Concept URI:** http://vocab.terralid.org#c_5592fbc1

[]{#archaeological}

###  archaeological
- **Definition**: Adjective of "archaeology", which refers to the
study of the human past.
- **Child of**:
  - [`date type`](#date-type)
- **Concept URI:** http://vocab.terralid.org#c_ee0cd6f1

[]{#geological}

###  geological
- **Definition**: Adjective of "geology", which refers to the study of
the Earth's history, composition, structure, physical properties and
relevant processes.
- **Child of**:
  - [`date type`](#date-type)
- **Concept URI:** http://vocab.terralid.org#c_de82ab14


[]{#dating-technique}

##  dating technique
- **Definition**: Determining the date of an event or in time or
relatively to other other events.
- **Child of**:
  - [`méthodes`](#méthodes)
- **Matches:**
  - http://vocab.getty.edu/aat/300054714 (exactMatch)
  - https://www.wikidata.org/wiki/Q97359583 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_458c8d5b

[]{#absolute-dating}

###  absolute dating
- **Definition**: Dating technique that results dates in calendar
years.
- **Child of**:
  - [`dating technique`](#dating-technique)
- **Matches:**
  - http://vocab.getty.edu/aat/300224276 (exactMatch)
  - https://www.wikidata.org/wiki/Q332423 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_70421df0

[]{#dendrochronology}

####  dendrochronology
- **Definition**: The measurement of a sequence of tree growth rings
and their relative differences in width and the comparison of this
information to known reference curves.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300054715 (exactMatch)
  - https://www.wikidata.org/wiki/Q80205 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bf02bc84

[]{#lichenometry}

####  lichenometry
- **Definition**: The measurement of lichens' size on rock surfaces.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300380350 (exactMatch)
  - https://www.wikidata.org/wiki/Q1432441 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e71424b2

[]{#luminescence-dating}

####  luminescence dating
- **Definition**: The measurement of the released stored energy in a
material in the form of light to determine the material's age.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300266049 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_14f0b363

[]{#optically-stimulated-luminescence-dating}

#####  optically stimulated luminescence dating
- **Definition**: The measurement of the stored energy in a material
in the form of light released by exposing the material to a strong
light source (e.g. lamp or laser) to determine the material's age.
- **Child of**:
  - [`luminescence dating`](#luminescence-dating)
- **Alternate labels:**
  - OSL
- **Matches:**
  - http://vocab.getty.edu/aat/300266050 (exactMatch)
  - https://www.wikidata.org/wiki/Q4335524 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8d044281

[]{#thermoluminescence-dating}

#####  thermoluminescence dating
- **Definition**: The measurement of the stored energy in a material
in the form of light released by heating the material to determine the
material's age.
- **Child of**:
  - [`luminescence dating`](#luminescence-dating)
- **Alternate labels:**
  - TL
- **Matches:**
  - http://vocab.getty.edu/aat/300054718 (exactMatch)
  - https://www.wikidata.org/wiki/Q2727388 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8650222c

[]{#radiometric-dating}

####  radiometric dating
- **Definition**: A family of dating methods that rely on the decay of
radioactive isotopes.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Alternate labels:**
  - radioactive dating
- **Matches:**
  - http://vocab.getty.edu/aat/300081912 (exactMatch)
  - https://www.wikidata.org/wiki/Q214753 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3f00a8dc

[]{#fission-track-dating}

#####  fission track dating
- **Definition**: Determining the age of a glassy material by counting
the number of damage trails created through the radioactive decay of
uranium atoms in the material.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300081920 (exactMatch)
  - https://www.wikidata.org/wiki/Q1420956 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_44573a53

[]{#potassium-argon-dating}

#####  potassium-argon dating
- **Definition**: Determination of the age through the ratio of a
radioactive potassium isotope and the argon isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - K-Ar dating
- **Matches:**
  - http://aims.fao.org/aos/agrovoc/c_36a43475 (exactMatch)
  - http://vocab.getty.edu/aat/300081924 (exactMatch)
  - https://www.wikidata.org/wiki/Q58891020 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ade3d830

[]{#argon-argon-dating}

######  argon-argon dating
- **Definition**: A dating method superseding potassium-argon dating
by allowing age determination from a single analysis. This is achieved
by converting a controlled amount of the radioactive potassium isotope
to a not naturally occurring argon isotope by neutron irradiation.
- **Child of**:
  - [`potassium-argon dating`](#potassium-argon-dating)
- **Alternate labels:**
  - Ar-Ar dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q4789695 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_025785fd

[]{#uranium-series-dating}

#####  uranium-series dating
- **Definition**: Determination of the age by determining the extent
to which the secular equilibrium between 230Th and 234U was restored
in a material that was nominally thorium-free at the point of its
creation.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - U-series dating
- **Matches:**
  - http://vocab.getty.edu/aat/300379909 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f0e6044b

[]{#radiocarbon-dating}

#####  radiocarbon dating
- **Definition**: Determination of the age through the remaining
radioactivity of carbon 14 in biogenic materials.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Matches:**
  - http://aims.fao.org/aos/agrovoc/c_13732 (exactMatch)
  - http://vocab.getty.edu/aat/300054717 (exactMatch)
  - https://www.wikidata.org/wiki/Q173412 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4b83987e

[]{#uranium-lead-dating}

#####  uranium-lead dating
- **Definition**: Determination of the age through the two decay
series of uranium isotopes to lead isotopes.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - U-Pb dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q1930710 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_acb27762

[]{#rubidium-strontium-dating}

#####  rubidium-strontium dating
- **Definition**: Determination of the age through the ratio of a
radioactive rubidium isotope and the strontium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Rb-Sr dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q1499814 (exactMatch)
  - http://aims.fao.org/aos/agrovoc/c_570aee9a (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f21ed82d

[]{#lutetium-hafnium-dating}

#####  lutetium-hafnium dating
- **Definition**: Determination of the age through the ratio of a
radioactive lutetium isotope and the hafnium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Lu-Hf dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q48997241 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5dec7fcf

[]{#samarium-neodymium-dating}

#####  samarium-neodymium dating
- **Definition**: Determination of the age through the ratio of a
radioactive samarium isotope and the neodymium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Sm-Nd dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q7408853 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c8c1af39

[]{#rhenium-osmium-dating}

#####  rhenium-osmium dating
- **Definition**: Determination of the age through the ratio of a
radioactive rhenium isotope and the osmium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Rh-Os dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q2148046 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_eb290340

[]{#lead-lead-dating}

#####  lead-lead dating
- **Definition**: Determination of the age through the ratios of the
the lead isotopes resulting from the radioactive decay of uranium and
the stable lead isotope ratio.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Pb-Pb dating
- **Matches:**
  - https://www.wikidata.org/wiki/Q6508336 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f98943fa

[]{#rehydroxylation-dating}

####  rehydroxylation dating
- **Definition**: The measurement of the hydroxyl content in fired
clay and the determination of the related chemical kinetics to
reconstruct the date of the material.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Alternate labels:**
  - RHX
- **Matches:**
  - http://vocab.getty.edu/aat/300444022 (exactMatch)
  - https://www.wikidata.org/wiki/Q7309862 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e6861de4

[]{#relative-dating}

###  relative dating
- **Definition**: Dating technique that allows to put objects in a
sequence relative to each other that cannot be tied to calendar years.
- **Child of**:
  - [`dating technique`](#dating-technique)
- **Matches:**
  - http://vocab.getty.edu/aat/300224275 (exactMatch)
  - https://www.wikidata.org/wiki/Q265619 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_25bf9b34

[]{#seriation}

####  seriation
- **Definition**: Recording the stylistic details of a group of items
and ordering them in a sequence based defined typological features.
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300379471 (exactMatch)
  - https://www.wikidata.org/wiki/Q358095 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e2a8665e

[]{#archaeomagnetic-dating}

####  archaeomagnetic dating
- **Definition**: The measurement of the direction and intensity of
the magnetic information in materials and its comparison to known
records of fluctuations in the magnetic field of the Earth.
Archaeomagnetic dating refers to the dating of anthropogenic materials
(e.g, fired clay), while palaeomagnetic dating refers to the dating of
geogenic origin (e.g. rocks).
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Alternate labels:**
  - palaeomagnetic dating
- **Matches:**
  - http://vocab.getty.edu/aat/300226163 (exactMatch)
  - http://vocab.getty.edu/aat/300081754 (exactMatch)
  - https://www.wikidata.org/wiki/Q776437 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e1bf335f

[]{#biostratigraphy}

####  biostratigraphy
- **Definition**: The determination of the relative sequence of
sediments or rocks based on the fossils found in them.
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - https://www.wikidata.org/wiki/Q864826 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b767c559

[]{#tephrochronology}

####  tephrochronology
- **Definition**: The determination of the relative sequence of
volcanic deposits (tephra), especially through studying their
stratigraphy (tephra).
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - http://vocab.getty.edu/aat/300380317 (exactMatch)
  - https://www.wikidata.org/wiki/Q2415972 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5ef3d79f


[]{#analytical-uncertainty}

##  analytical uncertainty
- **Definition**: An expression for the statistical dispersion of a
measured value.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Alternate labels:**
  - measurement uncertainty
- **Matches:**
  - https://www.wikidata.org/wiki/Q1403517 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6ae288a3

[]{#standard-error}

###  standard error
- **Definition**: The standard error of the mean (SEM) is data item
denoting the standard deviation of the sample-mean's estimate of a
population mean. It is calculated by dividing the sample standard
deviation (i.e., the sample-based estimate of the standard deviation
of the population) by the square root of n , the size (number of
observations) of the sample. A measure of dispersion applied to means
across hypothetical repeated random samples.
- **Child of**:
  - [`analytical uncertainty`](#analytical-uncertainty)
- **Alternate labels:**
  - SE
- **Other Properties:**
  - **note**: 
The definition of this entry is taken from STATO - The Statistical Methods Ontology, published under a Creative Commons Attribution 3.0 (CC-BY 3.0) license. 
- **Matches:**
  - http://purl.obolibrary.org/obo/STATO_0000037 (exactMatch)
  - https://www.wikidata.org/wiki/Q620994 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1c8f3d46

[]{#standard-deviation}

###  standard deviation
- **Definition**: The standard deviation of a random variable,
statistical population, data set, or probability distribution is a
measure of variation which correspond to the average distance from the
mean of the data set to any given point of that dataset. It also
corresponds to the square root of its variance.
- **Child of**:
  - [`analytical uncertainty`](#analytical-uncertainty)
- **Alternate labels:**
  - SD
- **Other Properties:**
  - **note**: 
The definition of this entry are taken from STATO - The Statistical Methods Ontology, published under a Creative Commons Attribution 3.0 (CC-BY 3.0) license. 
- **Matches:**
  - http://purl.obolibrary.org/obo/STATO_0000237 (exactMatch)
  - https://www.wikidata.org/wiki/Q159375 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ed11712a


[]{#identifier}

##  identifier
- **Definition**: A string unique for a specific resource or feature.
- **Child of**:
  - [`objetos proposicionais`](#objetos-proposicionais)
- **Other Properties:**
  - **note**: 
This is a reproduction of the controlled list relatedIdentifierType in the DataCite Metadata version schema 4.7. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q853614 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c8cb9106

[]{#w3id}

###  w3id
- **Definition**: Mostly used to publish vocabularies and ontologies.
The letters ‘w3’ stand for “World Wide Web”.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Permanent identifier for Web applications
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#w3id](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#w3id)
- **Concept URI:** http://vocab.terralid.org#c_f260a576

[]{#urn}

###  URN
- **Definition**: A unique and persistent identifier of an electronic
document. The syntax is: urn:<NID>:<NSS>. The leading urn: sequence is
case-insensitive, <NID> is the namespace identifier, <NSS> is the
namespace-specific string.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Uniform Resource Name
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q76497 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#urn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#urn)
- **Concept URI:** http://vocab.terralid.org#c_efbf8c56

[]{#url}

###  URL
- **Definition**: Also known as web address, a URL is a specific
character string that constitutes a reference to a resource. The
syntax is: scheme://domain:port/path?query_string#fragment_id.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Uniform Resource Locator
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q42253 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#url](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#url)
- **Concept URI:** http://vocab.terralid.org#c_cca94dd2

[]{#upc}

###  UPC
- **Definition**: A barcode symbology used for tracking trade items in
stores. Its most common form, the UPC-A, consists of 12 numerical
digits.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Universal Product Code
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1193047 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#upc](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#upc)
- **Concept URI:** http://vocab.terralid.org#c_49ebd1fc

[]{#swhid}

###  SWHID
- **Definition**: A unique and persistent identifier for software code
artifacts commonly found in version control systems such as code files
and commits available in the Software Heritage Archive. It consists of
the mandatory identifier of the record in the Software Heritage
archive and an optional list of qualifiers to provide information
about the object’s context.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - SoftWare Hash Identifier 
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q134567344 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#swhid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#swhid)
- **Concept URI:** http://vocab.terralid.org#c_b573f515

[]{#rrid}

###  RRID
- **Definition**: A character string used to uniquely identify key
inputs to an experiment including the so-called “key biological
resources” as defined by the National Institutes of Health, and
related tools such as core facilities and databases. An RRID name is
divided into two parts, the authority and a local identifier,
separated by an underscore.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Research Resource IDentifier
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q107278278 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#rrid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#rrid)
- **Concept URI:** http://vocab.terralid.org#c_96a8c2b8

[]{#raid}

###  RAiD
- **Definition**: A unique and persistent identifier for research
projects.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Research Activity Identifier 
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#raid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#raid)
- **Concept URI:** http://vocab.terralid.org#c_b10276d1

[]{#purl}

###  PURL
- **Definition**: A PURL has three parts: (1) a protocol, (2) a
resolver address, and (3) a name.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Persistent Uniform Resource Locator
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q195305 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#purl](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#purl)
- **Concept URI:** http://vocab.terralid.org#c_ff6b1f44

[]{#pmid}

###  PMID
- **Definition**: A unique number assigned to each PubMed record.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - PubMed identifier
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q2082879 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#pmid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#pmid)
- **Concept URI:** http://vocab.terralid.org#c_491eec33

[]{#lsid}

###  LSID
- **Definition**: A unique identifier for data in the Life Science
domain. Format: urn:lsid:authority:namespace:identifier:revision.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Life Science Identifiers
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q6459954 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lsid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lsid)
- **Concept URI:** http://vocab.terralid.org#c_19665f86

[]{#lissn}

###  LISSN
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Linking ISSN
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lissn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lissn)
- **Concept URI:** http://vocab.terralid.org#c_036b6cbe

[]{#istc}

###  ISTC
- **Definition**: A unique “number” assigned to a textual work. An
ISTC consists of 16 numbers and/or letters.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - International Standard Text Code
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1666944 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#istc](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#istc)
- **Concept URI:** http://vocab.terralid.org#c_a61ff4a5

[]{#issn}

###  ISSN
- **Definition**: A unique 8-digit number used to identify a print or
electronic periodical publication.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - International Standard Serial Number
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q131276 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#issn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#issn)
- **Concept URI:** http://vocab.terralid.org#c_23aeb12c

[]{#isbn}

###  ISBN
- **Definition**: A unique numeric book identifier. There are 2
formats: a 10-digit ISBN format and a 13-digit ISBN.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - International Standard Book Number
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q33057 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#isbn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#isbn)
- **Concept URI:** http://vocab.terralid.org#c_664844dc

[]{#igsn}

###  IGSN
- **Definition**: A code that uniquely identifies samples from our
natural environment and related features-of-interest.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - International Generic Sample Number
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q17058352 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#igsn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#igsn)
- **Concept URI:** http://vocab.terralid.org#c_bb41a882

[]{#handle}

###  Handle
- **Definition**: This refers specifically to an ID in the Handle
system operated by the Corporation for National Research Initiatives
(CNRI).
- **Child of**:
  - [`identifier`](#identifier)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q3126718 (relatedMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#handle](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#handle)
- **Concept URI:** http://vocab.terralid.org#c_db36371f

[]{#eissn}

###  EISSN
- **Definition**: ISSN used to identify periodicals in electronic form
(eISSN or e-ISSN).
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Electronic International Standard Serial Number
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#eissn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#eissn)
- **Concept URI:** http://vocab.terralid.org#c_9cdedeb0

[]{#ean13}

###  EAN13
- **Definition**: A 13-digit barcoding standard that is a superset of
the original 12-digit Universal Product Code (UPC) system.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - European Article Number, 
  - International Article Number, 
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Now renamed International Article Number, but retaining the original acronym.
- **Matches:**
  - https://www.wikidata.org/wiki/Q357404 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ean13](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ean13)
- **Concept URI:** http://vocab.terralid.org#c_91caa317

[]{#doi}

###  DOI
- **Definition**: A character string used to uniquely identify an
object. A DOI name is divided into two parts, a prefix and a suffix,
separated by a slash.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Digital Object Identifier
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q25670 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#doi](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#doi)
- **Concept URI:** http://vocab.terralid.org#c_cc3c0083

[]{#cstr}

###  CSTR
- **Definition**: CSTR is an identifier based on the Chinese National
Standard GB/T 32843—2016 “Science and technology resource
identification”, providing a unique identification service for
scientific data, papers, scientific institutions, researchers,
scientific instruments, patents and other scientific and technological
resources.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Common Science and Technology Resources Identifier
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q124257084 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#cstr](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#cstr)
- **Concept URI:** http://vocab.terralid.org#c_e3b9ba37

[]{#bibcode}

###  bibcode
- **Definition**: A standardized 19-character identifier according to
the syntax yyyyjjjjjvvvvmppppa. See http://info-uri.info/registry/OAIH
andler?verb=GetRecord&metadataPrefix=reg&identifier=info:bibcode/.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Astrophysics Data System bibliographic codes
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
bibcodes can be searched via https://ui.adsabs.harvard.edu/ or resolved using https://ui.adsabs.harvard.edu/abs/<bibcode>.
- **Matches:**
  - https://www.wikidata.org/wiki/Q25754 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#bibcode](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#bibcode)
- **Concept URI:** http://vocab.terralid.org#c_58ef12c9

[]{#arxiv}

###  ArXiv
- **Definition**: arXiv.org is a repository of preprints of scientific
papers in the fields of mathematics, physics, astronomy, computer
science, quantitative biology, statistics, and quantitative finance.
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - arXiv identifier
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q118398 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#arxiv](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#arxiv)
- **Concept URI:** http://vocab.terralid.org#c_14d152fa

[]{#ark}

###  ARK
- **Definition**: A URI designed to support long-term access to
information objects. In general, ARK syntax is of the form (brackets,
[]. indicate optional elements): [http://NMA/]ark:/NAAN/Name
[Qualifier].
- **Child of**:
  - [`identifier`](#identifier)
- **Alternate labels:**
  - Archival Resource Key
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ark](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ark)
- **Concept URI:** http://vocab.terralid.org#c_9c7b1aa6


[]{#relationtype}

##  relationType
- **Definition**: Describes a relationship between the source being
regstered (A) and the related source (B).
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Other Properties:**
  - **scopeNote**: 
Within TerraLID, the related source (B) is always the entity in TerraLID. 
  - **note**: 
This is a reproduction of the controlled list relationType in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/)
- **Concept URI:** http://vocab.terralid.org#c_2c9da0f0

[]{#hastranslation}

###  HasTranslation
- **Definition**: indicates A has a translation B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
When a resource is shared in one language, then later translated to another, use “HasTranslation” to link the original resource to its translation. When a resource is released at the same time in multiple languages, use “HasTranslation” to connect the works to each other in both directions.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hastranslation](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hastranslation)
- **Concept URI:** http://vocab.terralid.org#c_42798d88

[]{#istranslationof}

###  IsTranslationOf
- **Definition**: indicates A is a translation of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
When a resource is shared in one language, then later translated to another, use “IsTranslationOf” to link the translation to the original.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#istranslationof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#istranslationof)
- **Concept URI:** http://vocab.terralid.org#c_3e9a7d5d

[]{#collects}

###  Collects
- **Definition**: indicates A collects B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used to indicate the relationship between an instrument and where it has been used to collect, measure, obtain, or observe data (as in, instrument A collects dataset B).
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#collects](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#collects)
- **Concept URI:** http://vocab.terralid.org#c_50f18eec

[]{#iscollectedby}

###  IsCollectedBy
- **Definition**: indicates A is collected by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used to indicate the relationship between a dataset and an instrument that is used to collect, measure, obtain, or observe data (as in, dataset A is IsCollectedBy instrument B).
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscollectedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscollectedby)
- **Concept URI:** http://vocab.terralid.org#c_7209d768

[]{#isobsoletedby}

###  IsObsoletedBy
- **Definition**: indicates A is replaced by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isobsoletedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isobsoletedby)
- **Concept URI:** http://vocab.terralid.org#c_b87ae52a

[]{#obsoletes}

###  Obsoletes
- **Definition**: indicates A replaces B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#obsoletes](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#obsoletes)
- **Concept URI:** http://vocab.terralid.org#c_a03285c1

[]{#requires}

###  Requires
- **Definition**: indicates A requires B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used to indicate software dependencies.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#requires](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#requires)
- **Concept URI:** http://vocab.terralid.org#c_83af8ee5

[]{#isrequiredby}

###  IsRequiredBy
- **Definition**: indicates A is required by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used to indicate software dependencies.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isrequiredby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isrequiredby)
- **Concept URI:** http://vocab.terralid.org#c_f0352501

[]{#issourceof}

###  IsSourceOf
- **Definition**: indicates A is a source upon which B is based
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
IsSourceOf is the original resource from which a derivative resource was created.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issourceof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issourceof)
- **Concept URI:** http://vocab.terralid.org#c_d7654681

[]{#isderivedfrom}

###  IsDerivedFrom
- **Definition**: indicates B is a source upon which A is based
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
IsDerivedFrom should be used for a resource that is a derivative of an original resource.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isderivedfrom](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isderivedfrom)
- **Concept URI:** http://vocab.terralid.org#c_8aa44c44

[]{#reviews}

###  Reviews
- **Definition**: indicates that A is a review of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#reviews](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#reviews)
- **Concept URI:** http://vocab.terralid.org#c_1565380d

[]{#isreviewedby}

###  IsReviewedBy
- **Definition**: indicates that A is reviewed by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreviewedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreviewedby)
- **Concept URI:** http://vocab.terralid.org#c_8941e0d4

[]{#isidenticalto}

###  IsIdenticalTo
- **Definition**: indicates that A is identical to B, for use when
there is a need to register two separate instances of the same
resource
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
IsIdenticalTo should be used for a resource that is the same as the registered resource but is saved on another location, maybe another institution.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isidenticalto](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isidenticalto)
- **Concept URI:** http://vocab.terralid.org#c_58ed789b

[]{#isoriginalformof}

###  IsOriginalFormOf
- **Definition**: indicates A is the original form of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used for different software operating systems or compiler formats, for example.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isoriginalformof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isoriginalformof)
- **Concept URI:** http://vocab.terralid.org#c_f214a28f

[]{#isvariantformof}

###  IsVariantFormOf
- **Definition**: indicates A is a variant or different form of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
Use for a different form of one thing. May be used for different software operating systems or compiler formats, for example.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isvariantformof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isvariantformof)
- **Concept URI:** http://vocab.terralid.org#c_4ccf0580

[]{#compiles}

###  Compiles
- **Definition**: indicates B is the result of a compile or creation
event using A
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used for software and text, as a compiler can be a computer program or a person.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#compiles](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#compiles)
- **Concept URI:** http://vocab.terralid.org#c_ad976a89

[]{#iscompiledby}

###  IsCompiledBy
- **Definition**: indicates B is used to compile or create A
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used to indicate either a traditional text compilation, or the compiler program used to generate executable software.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscompiledby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscompiledby)
- **Concept URI:** http://vocab.terralid.org#c_38b56cad

[]{#documents}

###  Documents
- **Definition**: indicates A is documentation about/explaining B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used for software documentation. 
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#documents](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#documents)
- **Concept URI:** http://vocab.terralid.org#c_85ea27dc

[]{#isdocumentedby}

###  IsDocumentedBy
- **Definition**: indicates B is documentation about/explaining A
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
May be used for software documentation. 
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdocumentedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdocumentedby)
- **Concept URI:** http://vocab.terralid.org#c_d85f7b3a

[]{#references}

###  References
- **Definition**: indicates B is used as a source of information for A
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#references](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#references)
- **Concept URI:** http://vocab.terralid.org#c_9e3bfeb6

[]{#isreferencedby}

###  IsReferencedBy
- **Definition**: indicates A is used as a source of information by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreferencedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreferencedby)
- **Concept URI:** http://vocab.terralid.org#c_6510b31c

[]{#ispublishedin}

###  IsPublishedIn
- **Definition**: indicates A is published inside B, but is
independent of other things published inside of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispublishedin](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispublishedin)
- **Concept URI:** http://vocab.terralid.org#c_50fb5931

[]{#haspart}

###  HasPart
- **Definition**: indicates A includes the part B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
Primarily this relation is applied to container-contained type relationships. May be used for individual software modules; note that code repository-to-version relationships should be modeled using IsVersionOf and HasVersion
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#haspart](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#haspart)
- **Concept URI:** http://vocab.terralid.org#c_99ef8f93

[]{#ispartof}

###  IsPartOf
- **Definition**: indicates A is a portion of B; may be used for
elements of a series
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
Primarily this relation is applied to container-contained type relationships. May be used for individual software modules; note that code repository-to-version relationships should be modeled using IsVersionOf and HasVersion
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispartof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispartof)
- **Concept URI:** http://vocab.terralid.org#c_43052c1f

[]{#ispreviousversionof}

###  IsPreviousVersionOf
- **Definition**: indicates A is a previous edition of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispreviousversionof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispreviousversionof)
- **Concept URI:** http://vocab.terralid.org#c_36fff7dd

[]{#isnewversionof}

###  IsNewVersionOf
- **Definition**: indicates A is a new edition of B, where the new
edition has been modified or updated
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isnewversionof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isnewversionof)
- **Concept URI:** http://vocab.terralid.org#c_5bf18e08

[]{#isversionof}

###  IsVersionOf
- **Definition**: indicates A is a version of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
The registered resource is an instance of a target resource (indicates that A is an instance of B). It may be used, e.g., to relate a specific version of a software package to its software code repository.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isversionof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isversionof)
- **Concept URI:** http://vocab.terralid.org#c_d1c5bee2

[]{#hasversion}

###  HasVersion
- **Definition**: indicates A has a version B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **scopeNote**: 
The registered resource such as a software package or code repository has a versioned instance (indicates A has the instance B). It may be used, e.g., to relate an un-versioned code repository to one of its specific software versions.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasversion](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasversion)
- **Concept URI:** http://vocab.terralid.org#c_4e153d89

[]{#ismetadatafor}

###  IsMetadataFor
- **Definition**: indicates additional metadata A for a resource B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ismetadatafor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ismetadatafor)
- **Concept URI:** http://vocab.terralid.org#c_b8eafed9

[]{#hasmetadata}

###  HasMetadata
- **Definition**: indicates resource A has additional metadata B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasmetadata](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasmetadata)
- **Concept URI:** http://vocab.terralid.org#c_f14ca7a6

[]{#isdescribedby}

###  IsDescribedBy
- **Definition**: indicates A is described by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdescribedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdescribedby)
- **Concept URI:** http://vocab.terralid.org#c_c3c2de24

[]{#describes}

###  Describes
- **Definition**: indicates A describes B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#describes](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#describes)
- **Concept URI:** http://vocab.terralid.org#c_79a5511e

[]{#continues}

###  Continues
- **Definition**: indicates A is a continuation of the work B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#continues](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#continues)
- **Concept URI:** http://vocab.terralid.org#c_ec92c2c0

[]{#iscontinuedby}

###  IsContinuedBy
- **Definition**: indicates A is continued by the work B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscontinuedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscontinuedby)
- **Concept URI:** http://vocab.terralid.org#c_33f972fe

[]{#issupplementedby}

###  IsSupplementedBy
- **Definition**: indicates that B is a supplement to A
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issupplementedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issupplementedby)
- **Concept URI:** http://vocab.terralid.org#c_7f290a34

[]{#issupplementto}

###  IsSupplementTo
- **Definition**: indicates that A is a supplement to B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issupplementto](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#issupplementto)
- **Concept URI:** http://vocab.terralid.org#c_de611488

[]{#cites}

###  Cites
- **Definition**: indicates that A includes B in a citation
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#cites](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#cites)
- **Concept URI:** http://vocab.terralid.org#c_6d01b03c

[]{#iscitedby}

###  IsCitedBy
- **Definition**: indicates that B includes A in a citation
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
  - **note**: 
Recommended for discovery.
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscitedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscitedby)
- **Concept URI:** http://vocab.terralid.org#c_bfa26094


[]{#information-source}

##  information source
- **Definition**: Identifies whether a given value was supplied by an
external agent or internally calculared.
- **Child of**:
  - [`Konzepte`](#konzepte)
- **Concept URI:** http://vocab.terralid.org#c_f3916dc0

[]{#original}

###  original
- **Definition**: The value was provided by the data supplier.
- **Child of**:
  - [`information source`](#information-source)
- **Concept URI:** http://vocab.terralid.org#c_f33b28fe

[]{#calculated}

###  calculated
- **Definition**: The value was calculated by the TerraLID system.
- **Child of**:
  - [`information source`](#information-source)
- **Concept URI:** http://vocab.terralid.org#c_16684898


[]{#lead-isotope-ratios}

##  lead isotope ratios
- **Child of**:
  - [`συμβολικά αντικείμενα`](#συμβολικά-αντικείμενα)
- **Concept URI:** http://vocab.terralid.org#c_e5dcadb1

[]{#206pb-204pb}

###  206Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_865958f1

[]{#207pb-204pb}

###  207Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_f4936f14

[]{#208pb-204pb}

###  208Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_9f519c7a

[]{#204pb-206pb}

###  204Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_f8980276

[]{#207pb-206pb}

###  207Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_9531a82a

[]{#208pb-206pb}

###  208Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_b3a0bf8c

[]{#207pb-208pb}

###  207Pb/208Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_25e00462

[]{#206pb-208pb}

###  206Pb/208Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** http://vocab.terralid.org#c_3d413d9a


[]{#resourcetype}

##  resourceType
- **Definition**: The type of a resource.
- **Child of**:
  - [`objetos proposicionais`](#objetos-proposicionais)
- **Other Properties:**
  - **note**: 
This is a reproduction of a subset of the controlled list resourceTypeGeneral in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Concept URI:** http://vocab.terralid.org#c_4f75cdd5

[]{#other-(resourcetype)}

###  Other (resourceType)
- **Definition**: Any resource not covered by other terms. If
selected, provide resource type in metadata field "additional
information".
- **Child of**:
  - [`resourceType`](#resourcetype)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#other](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#other)
- **Concept URI:** http://vocab.terralid.org#c_e4111c25

[]{#workflow}

###  Workflow
- **Definition**: A structured series of steps which can be executed
to produce a final outcome, allowing users a means to specify and
enact their work in a more reproducible manner.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q627335 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#workflow](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#workflow)
- **Concept URI:** http://vocab.terralid.org#c_eb3431d5

[]{#text}

###  Text
- **Definition**: A resource consisting primarily of words for reading
that is not covered by any other textual resource type in this list.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q234460 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#text](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#text)
- **Concept URI:** http://vocab.terralid.org#c_9fadd71a

[]{#studyregistration}

###  StudyRegistration
- **Definition**: A detailed, time-stamped description of a research
plan, often openly shared in a registry or published in a journal
before the study is conducted to lend accountability and transparency
in the hypothesis generating and testing process.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#studyregistration](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#studyregistration)
- **Concept URI:** http://vocab.terralid.org#c_d9a7c870

[]{#standard}

###  Standard
- **Definition**: Something established by authority, custom, or
general consent as a model, example, or point of reference.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#standard](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#standard)
- **Concept URI:** http://vocab.terralid.org#c_2ac847b2

[]{#sound}

###  Sound
- **Definition**: A resource primarily intended to be heard.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Alternate labels:**
  - Audio recording
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#sound](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#sound)
- **Concept URI:** http://vocab.terralid.org#c_c2b67ae7

[]{#software}

###  Software
- **Definition**: A computer program other than a computational
notebook, in either source code (text) or compiled form. Use this type
for general software components supporting scholarly research. Use the
“ComputationalNotebook” value for virtual notebooks.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Software supporting scholarly research
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q7397 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#software](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#software)
- **Concept URI:** http://vocab.terralid.org#c_b359ddc1

[]{#service}

###  Service
- **Definition**: An organized system of apparatus, appliances, staff,
etc., for supplying some function(s) required by end users.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Data management service, or long-term preservation service
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#service](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#service)
- **Concept URI:** http://vocab.terralid.org#c_40899a25

[]{#report}

###  Report
- **Definition**: A document that presents information in an organized
format for a specific audience and purpose.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q10870555 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#report](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#report)
- **Concept URI:** http://vocab.terralid.org#c_21afb462

[]{#project}

###  Project
- **Definition**: A planned endeavor or activity, frequently
collaborative, intended to achieve a particular aim using allocated
resources such as budget, time, and expertise.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
This resource type represents the project and includes research projects and studies. For a project deliverable or description of a project, use the corresponding resource type for the output—e.g., for a project report, dissertation, or study registration, use the resourceTypeGeneral “Report”, “Dissertation”, or “StudyRegistration” instead.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1172284 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#project](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#project)
- **Concept URI:** http://vocab.terralid.org#c_78ce6c50

[]{#preprint}

###  Preprint
- **Definition**: A version of a scholarly or scientific paper that
precedes formal peer review and publication in a peer-reviewed
scholarly or scientific journal.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q580922 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#preprint](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#preprint)
- **Concept URI:** http://vocab.terralid.org#c_945645e4

[]{#physicalobject}

###  PhysicalObject
- **Definition**: A physical object or substance.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Artifacts, specimens, material samples, and features-of-interest of any size. Note that digital representations of physical objects should use one of the other resourceTypeGeneral values.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q223557 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#physicalobject](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#physicalobject)
- **Concept URI:** http://vocab.terralid.org#c_1e1210c6

[]{#peerreview}

###  PeerReview
- **Definition**: Evaluation of scientific, academic, or professional
work by others working in the same field.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q215028 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#peerreview](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#peerreview)
- **Concept URI:** http://vocab.terralid.org#c_192f8727

[]{#outputmanagementplan}

###  OutputManagementPlan
- **Definition**: A formal document that outlines how research outputs
are to be handled both during a research project and after the project
is completed.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Includes data, software, and materials.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#outputmanagementplan](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#outputmanagementplan)
- **Concept URI:** http://vocab.terralid.org#c_c5e4fd1c

[]{#model}

###  Model
- **Definition**: An abstract, conceptual, graphical, mathematical or
visualization model that represents empirical objects, phenomena, or
physical processes.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Modelled descriptions of, for example, different aspects of languages or a molecular biology reaction chain
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#model](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#model)
- **Concept URI:** http://vocab.terralid.org#c_095c193d

[]{#journalarticle}

###  JournalArticle
- **Definition**: A written composition on a topic of interest, which
forms a separate part of a journal.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q13442814 (closeMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journalarticle](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journalarticle)
- **Concept URI:** http://vocab.terralid.org#c_b0ef03ef

[]{#journal}

###  Journal
- **Definition**: A scholarly publication consisting of articles that
is published regularly throughout the year.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q737498 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journal](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journal)
- **Concept URI:** http://vocab.terralid.org#c_15f86bc5

[]{#interactiveresource}

###  InteractiveResource
- **Definition**: A resource requiring interaction from the user to be
understood, executed, or experienced.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Training modules, files that require use of a viewer (e.g., Flash), or query/response portals
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#interactiveresource](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#interactiveresource)
- **Concept URI:** http://vocab.terralid.org#c_6d0e1459

[]{#instrument}

###  Instrument
- **Definition**: A device, tool or apparatus used to obtain, measure
and/or analyze data.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Note that this is meant to be the instrument instance, e.g., the individual physical device, not the digital description or design of an instrument.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#instrument](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#instrument)
- **Concept URI:** http://vocab.terralid.org#c_d40d5def

[]{#image}

###  Image
- **Definition**: A visual representation other than text.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Digitised or born digital images, drawings or photographs
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q478798 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#image](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#image)
- **Concept URI:** http://vocab.terralid.org#c_d16e61fe

[]{#event}

###  Event
- **Definition**: A non-persistent, time-based occurrence.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Descriptive information and/or content that is the basis for discovery of the purpose, location, duration, and responsible agents associated with an event such as a webcast or convention.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1656682 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#event](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#event)
- **Concept URI:** http://vocab.terralid.org#c_4229295c

[]{#dissertation}

###  Dissertation
- **Definition**: A written essay, treatise, or thesis, especially one
written by a candidate for the degree of Doctor of Philosophy.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1266946 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dissertation](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dissertation)
- **Concept URI:** http://vocab.terralid.org#c_3839e9ab

[]{#dataset}

###  Dataset
- **Definition**: Data encoded in a defined structure.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
Data file or files
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1172284 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dataset](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dataset)
- **Concept URI:** http://vocab.terralid.org#c_985fe775

[]{#datapaper}

###  DataPaper
- **Definition**: A factual and objective publication with a focused
intent to identify and describe specific data, sets of data, or data
collections to facilitate discoverability.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
A data paper describes data provenance and methodologies used in the gathering, processing, organizing, and representing the data.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q17009938 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#datapaper](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#datapaper)
- **Concept URI:** http://vocab.terralid.org#c_b3d49316

[]{#conferenceproceeding}

###  ConferenceProceeding
- **Definition**: Collection of academic papers published in the
context of an academic conference.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q1143604 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferenceproceeding](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferenceproceeding)
- **Concept URI:** http://vocab.terralid.org#c_4ec6c8f6

[]{#conferencepaper}

###  ConferencePaper
- **Definition**: Article that is written with the goal of being
accepted to a conference.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q23927052 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferencepaper](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferencepaper)
- **Concept URI:** http://vocab.terralid.org#c_afd22872

[]{#computationalnotebook}

###  ComputationalNotebook
- **Definition**: A virtual notebook environment used for literate
programming.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#computationalnotebook](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#computationalnotebook)
- **Concept URI:** http://vocab.terralid.org#c_0afde725

[]{#collection}

###  Collection
- **Definition**: An aggregation of resources, which may encompass
collections of one resourceType as well as those of mixed types. A
collection is described as a group; its parts may also be separately
described.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
A collection of samples, or various files making up a report
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#collection](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#collection)
- **Concept URI:** http://vocab.terralid.org#c_76209e5e

[]{#bookchapter}

###  BookChapter
- **Definition**: One of the main divisions of a book.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q139074677 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#bookchapter](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#bookchapter)
- **Concept URI:** http://vocab.terralid.org#c_fc66bc62

[]{#book}

###  Book
- **Definition**: A medium for recording information in the form of
writing or images, typically composed of many pages bound together and
protected by a cover.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q571 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#book](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#book)
- **Concept URI:** http://vocab.terralid.org#c_5c0c5449

[]{#award}

###  Award
- **Definition**: An umbrella term for resources provided to
individual(s) or organization(s) in support of research, academic
output, or training, such as a specific instance of funding, grant,
investment, sponsorship, scholarship, recognition, or non-monetary
materials.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q618779 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#award](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#award)
- **Concept URI:** http://vocab.terralid.org#c_a8c92376

[]{#audiovisual}

###  Audiovisual
- **Definition**: A series of visual representations imparting an
impression of motion when shown in succession. May or may not include
sound.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **scopeNote**: 
May be used for films, video, etc.
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q758901 (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#audiovisual](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#audiovisual)
- **Concept URI:** http://vocab.terralid.org#c_30709214


[]{#registry}

##  registry
- **Definition**: A registry offers authoritative information on a
defined topic.
- **Child of**:
  - [`objetos proposicionais`](#objetos-proposicionais)
- **Matches:**
  - https://www.wikidata.org/wiki/Q19386377 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_062fe0b0

[]{#gazetteer}

###  gazetteer
- **Definition**: A service publishing structured authoritative
information about a certain topic, usually locations, based on
ontological principles.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1006160 (closeMatch)
  - https://www.wikidata.org/wiki/Q81661634 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_59d96666

[]{#whg}

####  WHG
- **Definition**: The World History Gazetteer provides authoritative
data for historic and archaeological sites for the entire globe.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q130424771 (exactMatch)
- **References**:
  - [https://whgazetteer.org/](https://whgazetteer.org/)
- **Concept URI:** http://vocab.terralid.org#c_321798be

[]{#tgn}

####  TGN
- **Definition**: The Getty Thesaurus of Geographic Names is a
structured vocabulary for places important in arts and architecture.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1520117 (exactMatch)
- **References**:
  - [https://www.getty.edu/research/tools/vocabularies/tgn/index.html](https://www.getty.edu/research/tools/vocabularies/tgn/index.html)
- **Concept URI:** http://vocab.terralid.org#c_2c0d9965

[]{#geonames}

####  Geonames
- **Definition**: Geonames is a geographical database with global
coverage.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q830106 (exactMatch)
- **References**:
  - [https://www.geonames.org/](https://www.geonames.org/)
- **Concept URI:** http://vocab.terralid.org#c_c18450b7

[]{#pleiades}

####  Pleiades
- **Definition**: Pleiades is a community-built gazetteer for
archaeological and historical sites with focus on the ancient
Mediterrean and neighbouring regions.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q138510884 (exactMatch)
- **References**:
  - [https://pleiades.stoa.org/](https://pleiades.stoa.org/)
- **Concept URI:** http://vocab.terralid.org#c_81d9c666

[]{#idai.gazetteer}

####  iDAI.gazetteer
- **Definition**: The gazetteer of the German Archaeological
Institute.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q93290690 (exactMatch)
- **References**:
  - [https://gazetteer.dainst.org/app/?lang=en#!/home](https://gazetteer.dainst.org/app/?lang=en#!/home)
- **Concept URI:** http://vocab.terralid.org#c_eb965d6a

[]{#periodo}

####  PeriodO
- **Definition**: PeriodO is a gazetteer for chronological information
of archaeological, historical and art-historical periods.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - https://www.wikidata.org/wiki/Q104904881 (exactMatch)
- **References**:
  - [https://perio.do/](https://perio.do/)
- **Concept URI:** http://vocab.terralid.org#c_d012defe

[]{#gnd}

###  GND
- **Definition**: The Gemeinsame Normdatei (GND, Integrated Authority
File) of the German National Library provides authoritative data on a
wide range of topics, among them persons, corporate bodies and
geographic entities. Its main target groups are libraries who used it
for cataloguing their publication.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - https://www.wikidata.org/wiki/Q54506313 (exactMatch)
- **References**:
  - [https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html)
- **Concept URI:** http://vocab.terralid.org#c_ef46e5df

[]{#orcid}

###  ORCID
- **Definition**: The Open Researcher and Contributor ID organization
offers persistent identifiers of the same name for persons, with
researchers and scholars as their main audience.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - https://www.wikidata.org/wiki/Q51044 (exactMatch)
- **References**:
  - [https://orcid.org/](https://orcid.org/)
- **Concept URI:** http://vocab.terralid.org#c_c62b90a7

[]{#idai-chronontology}

###  iDAI ChronOntology
- **Definition**: ChronOntology is the ontology for chronological
information of the German Archaological Institute.
- **Child of**:
  - [`registry`](#registry)
- **References**:
  - [https://chronontology.dainst.org/](https://chronontology.dainst.org/)
- **Concept URI:** http://vocab.terralid.org#c_fb11b880


[]{#unit-of-measurement}

##  unit of measurement
- **Definition**: A particular quantity that was chosen as a scale for
measurements of the same dimension.
- **Child of**:
  - [`συμβολικά αντικείμενα`](#συμβολικά-αντικείμενα)
- **Matches:**
  - http://qudt.org/schema/qudt/Unit (exactMatch)
  - https://www.wikidata.org/wiki/Q47574 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ac36f033

[]{#distance}

###  distance
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q126017 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c83fe291

[]{#m}

####  m
- **Definition**: The SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - http://qudt.org/vocab/unit/M (exactMatch)
  - https://www.wikidata.org/wiki/Q11573 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_98b8d986

[]{#mm}

####  mm
- **Definition**: One thousandth of the SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - http://qudt.org/vocab/unit/MilliM (exactMatch)
  - https://www.wikidata.org/wiki/Q174789 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_50025783

[]{#cm}

####  cm
- **Definition**: One hundredth of the SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - http://qudt.org/vocab/unit/CentiM (exactMatch)
  - https://www.wikidata.org/wiki/Q174728 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4444cd3e

[]{#km}

####  km
- **Definition**: The SI unit of the distance multiplied by one
thousand.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - http://qudt.org/vocab/unit/KiloM (exactMatch)
  - https://www.wikidata.org/wiki/Q828224 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a099372d

[]{#mass}

###  mass
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q11423 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7550f509

[]{#µg}

####  µg
- **Definition**: The 0.000000001-fold of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Alternate labels:**
  - ug
- **Matches:**
  - http://qudt.org/vocab/unit/MicroGM (exactMatch)
  - https://www.wikidata.org/wiki/Q1645498 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6fc8030c

[]{#kg}

####  kg
- **Definition**: The SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - http://qudt.org/vocab/unit/KiloGM (exactMatch)
  - https://www.wikidata.org/wiki/Q11570 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3739cdc8

[]{#mg}

####  mg
- **Definition**: One milllionth thousanth of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - http://qudt.org/vocab/unit/MilliGM (exactMatch)
  - https://www.wikidata.org/wiki/Q3241121 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e5f24560

[]{#g}

####  g
- **Definition**: One thousandth of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - http://qudt.org/vocab/unit/GM (exactMatch)
  - https://www.wikidata.org/wiki/Q41803 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7ede7b9c

[]{#electric-potential}

###  electric potential
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q55451 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ded3a888

[]{#v}

####  V
- **Definition**: The SI unit of the electric potential.
- **Child of**:
  - [`electric potential`](#electric-potential)
- **Matches:**
  - http://qudt.org/vocab/unit/V (exactMatch)
  - https://www.wikidata.org/wiki/Q25250 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e16769fb

[]{#mv}

####  mV
- **Definition**: One thousandth of the SI unit of the eletric
potential.
- **Child of**:
  - [`electric potential`](#electric-potential)
- **Matches:**
  - http://qudt.org/vocab/unit/MilliV (exactMatch)
  - https://www.wikidata.org/wiki/Q2448803 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_17398a30

[]{#cps}

###  cps
- **Definition**: The number of events registered by a detector in one
second.
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q115536343 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ba8f4496

[]{#time}

###  time
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q11471 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fd424d2e

[]{#ma}

####  Ma
- **Definition**: The age on an item in millions of years, i.e.
multiples of 1000000 years.
- **Child of**:
  - [`time`](#time)
- **Matches:**
  - https://www.wikidata.org/wiki/Q20764 (exactMatch)
  - http://qudt.org/vocab/unit/MegaYR (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a39e16f9

[]{#a}

####  a
- **Definition**: The age of an item in years.
- **Child of**:
  - [`time`](#time)
- **Matches:**
  - https://www.wikidata.org/wiki/Q577 (exactMatch)
  - http://qudt.org/vocab/unit/YR (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6b05ca15

[]{#concentration}

###  concentration
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q3686031 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2f3c3933

[]{#%}

####  %
- **Definition**: The unspecified fraction of an compound as a
fraction of 100.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - https://www.wikidata.org/wiki/Q11229 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f1f818b8

[]{#at%}

####  at%
- **Definition**: The ratio of the number of atoms of one element to
the total number of atoms, expressed as percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Concept URI:** http://vocab.terralid.org#c_69a07382

[]{#wt%}

####  wt%
- **Definition**: The mass fraction of an element expressed as
percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - https://www.wikidata.org/wiki/Q110162802 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bc79dc60

[]{#µg-kg}

####  µg/kg
- **Definition**: The mass of the measurant expressed as one part per
1000000000 parts.
- **Child of**:
  - [`concentration`](#concentration)
- **Alternate labels:**
  - ppb, 
  - ng/g, 
- **Matches:**
  - http://qudt.org/vocab/unit/MicroGM-PER-KiloGM (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cb4c170e

[]{#µg-g}

####  µg/g
- **Definition**: The mass of the measurant expressed as one part per
million parts.
- **Child of**:
  - [`concentration`](#concentration)
- **Alternate labels:**
  - ppm, 
  - mg/kg, 
- **Matches:**
  - http://qudt.org/vocab/unit/MicroGM-PER-GM (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3b8ef5ef

[]{#oxide%}

####  oxide%
- **Definition**: The mass fraction of an oxide, expressed as percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - https://www.wikidata.org/wiki/Q110162802 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_815a8de3


[]{#mineral-texture}

##  mineral texture
- **Definition**: The relationship between the mineral and the matrix
and other minerals, conveying information about the mineral's
formation conditions.
- **Child of**:
  - [`υλικά μορφώματα`](#υλικά-μορφώματα)
- **Other Properties:**
  - **note**: 
The terms are mostly taken from U. Neumann (2020), Guide for the microscopical identification of ore and gangue minerals, Tübingen University Press (http://dx.doi.org/10.15496/publikation-38866). However, the definitions are original and based on various sources because the relevant literature, including the aforementioned publication, do not explicitly defines textures but provide examples for them in photomicrographs. 
- **Concept URI:** http://vocab.terralid.org#c_8441accd

[]{#intergrowth}

###  intergrowth
- **Definition**: The state of interlocking of different mineral
grains due to simultaneous crystallisation.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** http://vocab.terralid.org#c_e74b28a0

[]{#ophitic}

####  ophitic
- **Definition**: Large and often lath-shaped euhedral or subhedral
crystals are partly or fully included in much larger crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_dd1113d4

[]{#intersertal}

####  intersertal
- **Definition**: Filling of interstitial space with a glass or a
vitreous phase with small crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_cab80d83

[]{#interstitial}

####  interstitial
- **Definition**: The mineral grew in the interstitial space between
grains or structures.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_1a4f781a

[]{#interlocked}

####  interlocked
- **Definition**: Intimate intergrowth of randomly orientated mineral
grains with no gaps or cement between them.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_3e50acb7

[]{#symplectitic}

####  symplectitic
- **Definition**: The fine-grained vermicular ("worm-shaped")
intergrowth of two minerals, often indicating the breakdown of
unstable phases.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - vermicular
- **Other Properties:**
  - **scopeNote**: 
Myrmekitic as specific case of symplectitic texture. Appears to be often used synonymously at least in ore microscopy . 
- **Concept URI:** http://vocab.terralid.org#c_9e0d2c4a

[]{#myrmekitic}

#####  myrmekitic
- **Definition**: A symplectitic intergrowth of plagioclase and
vermicular quartz.
- **Child of**:
  - [`symplectitic`](#symplectitic)
- **Other Properties:**
  - **scopeNote**: 
Myrmekitic as specific case of symplectitic texture. Appears to be often used synonymously at least in ore microscopy . 
- **Concept URI:** http://vocab.terralid.org#c_5eaf970c

[]{#poikiloblastic}

####  poikiloblastic
- **Definition**: Small grains of one mineral are randomly scattered
without common orientation in larger grains of another mineral.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - poikilitic, 
  - sieve texture, 
- **Concept URI:** http://vocab.terralid.org#c_6655861f

[]{#disseminated}

####  disseminated
- **Definition**: The mineral is scattered as small grains throughout
another mineral or the matrix.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_aa5d33c3

[]{#rimmed}

####  rimmed
- **Definition**: A mineral grew in the rim of another mineral.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_436d944e

[]{#amoeboid}

####  amoeboid
- **Definition**: A mineral with irregular outlines and anhedral
crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** http://vocab.terralid.org#c_e5b6f80a

[]{#cellular-(intergrowth)}

####  cellular (intergrowth)
- **Definition**: Growth of minerals in small roughly regular-shaped
rounded aggregates that resemble the shape of biological cells. Or the
porous texture of a rock characterised by abundant openings or
cavities, which may or may not be connected.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - porous, 
  - cavernous, 
  - vesicular, 
- **Concept URI:** http://vocab.terralid.org#c_04619e43

[]{#atoll-like}

####  atoll-like
- **Definition**: The growth of a ring-shaped mineral around and
surrounded by other minerals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - core texture
- **Concept URI:** http://vocab.terralid.org#c_95b262b5

[]{#replacement}

###  replacement
- **Definition**: The growth of a new or chemically different mineral
as a reaction product of the already existing mineral.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** http://vocab.terralid.org#c_a3d375e7

[]{#filiform}

####  filiform
- **Definition**: An intergrowth of  different minerals in which the
larger crystals have a fairly regular geometric outline and
orientation, and resemble cuneiform writing or have a thread-like
appearance.
- **Child of**:
  - [`replacement`](#replacement)
- **Alternate labels:**
  - graphic texture
- **Concept URI:** http://vocab.terralid.org#c_f478f111

[]{#graphic}

####  graphic
- **Definition**: The growth of elongated rounded aggregates of
secondary minerals inside the primary mineral, often as a result of
alteration of the primary mineral.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_52eaf264

[]{#cellular-(replacement)}

####  cellular (replacement)
- **Definition**: The growth of minerals replacing the content of
cells in originally biological matter such as plants in coal.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_8c47dce3

[]{#island-shaped}

####  island-shaped
- **Definition**: The original mineral reacted from the outside,
leaving an (island-shaped) unreacted part surrounded by secondary
minerals.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_7b190793

[]{#boxwork}

####  boxwork
- **Definition**: Growth of secondary minerals in cavities and along
fracture or cleavage planes from which previously present minerals
were removed by e.g. dissolution, creating a network texture
resembling stacked boxes or honey-combs.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_d78ab7be

[]{#skeleton-shaped}

####  skeleton-shaped
- **Definition**: Relict of a skeletal crystal of one mineral enclosed
in another mineral species.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_36ca06ef

[]{#cusp-and-caries}

####  cusp-and-caries
- **Definition**: The growth of a secondary mineral from the grain
boundary into the primary minerals, resulting in a grain boundary
between both minerals with many scallop-shaped, concave embayments.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_d3b9f898

[]{#lacuna}

####  lacuna
- **Definition**: The dissolution of small areas of a mineral, often
at its rim, resulting in voids.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_bb44a01a

[]{#lamellar}

####  lamellar
- **Definition**: The oriented growth of a secondary mineral in
elongated shapes within the primary mineral, usually along cleavage
planes, crystal planes, twin boundaries or fractures.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_7fe5c1ff

[]{#zonal}

####  zonal
- **Definition**: The evenly-spaced growth of a secondary mineral
along the crystallographic orientation of the primary mineral's grain
boundary.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_7d8b3c14

[]{#atoll-like-(replacement)}

####  atoll-like (replacement)
- **Definition**: The replacement of one mineral by another with
leaving the outermost original mineral unaffected, and constituting
the "atoll".
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_dd91efb2

[]{#cement-shaped}

####  cement-shaped
- **Definition**: The growth of a dense anhedral alteration mineral in
the matrix.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** http://vocab.terralid.org#c_d375a5c9

[]{#pseudomorph}

####  pseudomorph
- **Definition**: A secondary mineral completely replacing the primary
mineral while retaining the shape of the primary mineral's grains.
- **Child of**:
  - [`replacement`](#replacement)
- **Matches:**
  - https://www.wikidata.org/wiki/Q1456639 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0571a899

[]{#deformation-related}

###  deformation-related
- **Definition**: The alteration of minerals through external
mechanical stress.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** http://vocab.terralid.org#c_88091e76

[]{#cataclastic}

####  cataclastic
- **Definition**: The fracturing of a mineral due to intense
mechanical stress.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_6783bb4e

[]{#brecciated}

####  brecciated
- **Definition**: The fragmentation of a mineral resulting in various
angular fragments
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_430fd693

[]{#broken}

####  broken
- **Definition**: The fragmentation of a mineral.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_03b13243

[]{#translation-lamellae}

####  translation lamellae
- **Definition**: The internal deformation of a mineral's crystal due
to translational forces, resulting in the re-orientation of some areas
in the crystal along crystal planes unrelated to the crystallographic
axes
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_3136dfed

[]{#pressure-twins}

####  pressure twins
- **Definition**: The internal deformation of a mineral's crystal due
to translational forces, resulting in the re-orientation of some areas
in the crystal along crystal planes along its crystallographic axes.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_7067812d

[]{#bending}

####  bending
- **Definition**: The ductile transformation of a mineral into a bent
shape (i.e., without breaking it).
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_c8069a37

[]{#planar-alignment}

####  planar alignment
- **Definition**: The transformation of elongated or layered minerals
into a (sub)parallel orientation.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** http://vocab.terralid.org#c_ed4b7838


[]{#chemical-substance}

##  chemical substance
- **Definition**: Matter of constant and unique chemical composition
with characteristic properties.
- **Child of**:
  - [`materials`](#materials)
- **Matches:**
  - https://www.wikidata.org/wiki/Q79529 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0038daae

[]{#oxide}

###  oxide
- **Definition**: Chemical substance containing oxygen and one other
chemical element.
- **Child of**:
  - [`materials`](#materials)
  - [`chemical substance`](#chemical-substance)
- **Other Properties:**
  - **scopeNote**: 
List of oxides retrieved from https://www.wikidoc.org/index.php/Oxide
- **Matches:**
  - https://www.wikidata.org/wiki/Q50690 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7014484c

[]{#silver-oxide}

####  silver oxide
- **Definition**: silver oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ag2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q407815 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6e9450ea

[]{#silver(ii)-oxide}

####  silver(II) oxide
- **Definition**: silver(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - AgO
- **Matches:**
  - https://www.wikidata.org/wiki/Q12043383 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_69c7ff92

[]{#aluminium-oxide}

####  aluminium oxide
- **Definition**: aluminium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Al2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q177342 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4b36b188

[]{#oxidoaluminium}

####  oxidoaluminium
- **Definition**: oxidoaluminium
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - AlO
- **Matches:**
  - https://www.wikidata.org/wiki/Q133767 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_87d3476d

[]{#arsenic-trioxide}

####  arsenic trioxide
- **Definition**: arsenic trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - As2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q7739 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9e1c013d

[]{#arsenic-pentoxide}

####  arsenic pentoxide
- **Definition**: arsenic pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - As2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q411256 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_11fca549

[]{#gold-sesquioxide}

####  gold sesquioxide
- **Definition**: gold sesquioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Au2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q415247 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_63057619

[]{#diboron-trioxide}

####  diboron trioxide
- **Definition**: diboron trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - B2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q411076 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ec1ff2de

[]{#barium-oxide}

####  barium oxide
- **Definition**: barium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - BaO
- **Matches:**
  - https://www.wikidata.org/wiki/Q408892 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4119401c

[]{#beryllium-oxide}

####  beryllium oxide
- **Definition**: beryllium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - BeO
- **Matches:**
  - https://www.wikidata.org/wiki/Q422714 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_981e3f6c

[]{#bismuth-pentoxide}

####  bismuth pentoxide
- **Definition**: bismuth pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Bi2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q4332804 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e9a84865

[]{#dicarbon-monoxide}

####  dicarbon monoxide
- **Definition**: Dicarbon monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - C2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q2741198 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8f4dc06f

[]{#calcium-oxide}

####  calcium oxide
- **Definition**: calcium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CaO
- **Matches:**
  - https://www.wikidata.org/wiki/Q185006 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_65421f24

[]{#cadmium-oxide}

####  cadmium oxide
- **Definition**: cadmium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CdO
- **Matches:**
  - https://www.wikidata.org/wiki/Q196661 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_43aac36b

[]{#cerium(iv)-oxide}

####  cerium(IV) oxide
- **Definition**: cerium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CeO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q411844 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_63ba3eba

[]{#dichlorine-monoxide}

####  dichlorine monoxide
- **Definition**: dichlorine monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cl2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q1154631 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cb2f4398

[]{#chlorine-heptoxide}

####  chlorine heptoxide
- **Definition**: chlorine heptoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cl2O7
- **Matches:**
  - https://www.wikidata.org/wiki/Q2301593 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_13e8632e

[]{#chlorine-dioxide}

####  chlorine dioxide
- **Definition**: chlorine dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ClO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q422080 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e6409869

[]{#carbon-monoxide}

####  carbon monoxide
- **Definition**: carbon monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO
- **Matches:**
  - https://www.wikidata.org/wiki/Q2025 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_21b7771e

[]{#carbon-dioxide}

####  carbon dioxide
- **Definition**: carbon dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q1997 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_305bca08

[]{#carbon-trioxide}

####  carbon trioxide
- **Definition**: carbon trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q27110034 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f40b7fdb

[]{#cobalt(ii)-oxide}

####  cobalt(II) oxide
- **Definition**: cobalt(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CoO
- **Matches:**
  - https://www.wikidata.org/wiki/Q411283 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6713e9e0

[]{#dichromium-trioxide}

####  dichromium trioxide
- **Definition**: dichromium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cr2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q407905 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_416e9447

[]{#chromium(ii)-oxide}

####  chromium(II) oxide
- **Definition**: chromium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO
- **Matches:**
  - https://www.wikidata.org/wiki/Q414303 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_42a32bf3

[]{#chromium-trioxide}

####  chromium trioxide
- **Definition**: chromium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q931335 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_62949c0e

[]{#copper(i)-oxide}

####  copper(I) oxide
- **Definition**: copper(I) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cu2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q407709 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dfa113ee

[]{#copper(ii)-oxide}

####  copper(II) oxide
- **Definition**: copper(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CuO
- **Matches:**
  - https://www.wikidata.org/wiki/Q421787 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2153fad4

[]{#erbium(iii)-oxide}

####  erbium(III) oxide
- **Definition**: erbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Er2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q187473 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5b76594c

[]{#iron(iii)-oxide}

####  iron(III) oxide
- **Definition**: iron(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Fe2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419170 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f64b32e0

[]{#iron(ii)-oxide}

####  iron(II) oxide
- **Definition**: iron(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - FeO
- **Matches:**
  - https://www.wikidata.org/wiki/Q196680 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2bcd7ca0

[]{#gallium(iii)-oxide}

####  gallium(III) oxide
- **Definition**: gallium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ga2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419487 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7d31fd7c

[]{#gadolinium(iii)-oxide}

####  gadolinium(III) oxide
- **Definition**: gadolinium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Gd2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419919 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9c798327

[]{#germanium-dioxide}

####  germanium dioxide
- **Definition**: germanium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - GeO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q419133 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fd57cc71

[]{#water}

####  water
- **Definition**: water
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - H2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q283 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0a346cac

[]{#hafnium(iv)-oxide}

####  hafnium(IV) oxide
- **Definition**: hafnium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - HfO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q418740 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bf5d3633

[]{#mercury(ii)-oxide}

####  mercury(II) oxide
- **Definition**: mercury(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - HgO
- **Matches:**
  - https://www.wikidata.org/wiki/Q174727 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_52244d14

[]{#holmium(iii)-oxide}

####  holmium(III) oxide
- **Definition**: holmium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ho2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q421519 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_19be4e22

[]{#indium-oxide}

####  indium oxide
- **Definition**: indium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - In2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q424955 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_909ad0f4

[]{#potassium-oxide}

####  potassium oxide
- **Definition**: potassium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - K2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q408880 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_39c30ce1

[]{#lanthanum(iii)-oxide}

####  lanthanum(III) oxide
- **Definition**: lanthanum(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - La2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q417250 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_29b91fa4

[]{#lithium-oxide}

####  lithium oxide
- **Definition**: lithium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Li2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q385662 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fdff16f4

[]{#lutetium(iii)-oxide}

####  lutetium(III) oxide
- **Definition**: lutetium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Lu2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q418048 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cca0161a

[]{#magnesium-oxide}

####  magnesium oxide
- **Definition**: magnesium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MgO
- **Matches:**
  - https://www.wikidata.org/wiki/Q214769 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4e952e50

[]{#manganese-heptoxide}

####  manganese heptoxide
- **Definition**: manganese heptoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Mn2O7
- **Matches:**
  - https://www.wikidata.org/wiki/Q27506 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_734314c6

[]{#manganese(ii)-oxide}

####  manganese(II) oxide
- **Definition**: manganese(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MnO
- **Matches:**
  - https://www.wikidata.org/wiki/Q414669 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_167c3f61

[]{#manganese-dioxide}

####  manganese dioxide
- **Definition**: manganese dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MnO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q407674 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_33f0dd4f

[]{#molybdenum-trioxide}

####  molybdenum trioxide
- **Definition**: molybdenum trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MoO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q416416 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2a4dfe8f

[]{#dinitrogen-trioxide}

####  dinitrogen trioxide
- **Definition**: dinitrogen trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q407833 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_29d3ff32

[]{#dinitrogen-tetroxide}

####  dinitrogen tetroxide
- **Definition**: dinitrogen tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O4
- **Matches:**
  - https://www.wikidata.org/wiki/Q382984 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_99b6629a

[]{#dinitrogen-pentoxide}

####  dinitrogen pentoxide
- **Definition**: dinitrogen pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q408458 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8e23fbf4

[]{#sodium-oxide}

####  sodium oxide
- **Definition**: sodium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Na2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q407467 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bfcf2bf1

[]{#nickel(iii)-oxide}

####  nickel(III) oxide
- **Definition**: nickel(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ni2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419873 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0816776a

[]{#nickel(ii)-oxide}

####  nickel(II) oxide
- **Definition**: nickel(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NiO
- **Matches:**
  - https://www.wikidata.org/wiki/Q411221 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bbf2d83f

[]{#nitric-oxide}

####  nitric oxide
- **Definition**: nitric oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NO
- **Matches:**
  - https://www.wikidata.org/wiki/Q207843 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c8b676b3

[]{#nitrogen-dioxide}

####  nitrogen dioxide
- **Definition**: nitrogen dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q207895 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_472e6ab5

[]{#tetraoxygen}

####  tetraoxygen
- **Definition**: tetraoxygen
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - O4
- **Matches:**
  - https://www.wikidata.org/wiki/Q457709 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e0df7c75

[]{#oxygen-difluoride}

####  oxygen difluoride
- **Definition**: oxygen difluoride
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - OF2
- **Matches:**
  - https://www.wikidata.org/wiki/Q411301 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ec6db833

[]{#osmium-tetroxide}

####  osmium tetroxide
- **Definition**: osmium tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - OsO4
- **Matches:**
  - https://www.wikidata.org/wiki/Q422021 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b7afbec3

[]{#phosphorus-pentoxide}

####  phosphorus pentoxide
- **Definition**: phosphorus pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - P2O5, 
  - P4O10, 
- **Matches:**
  - https://www.wikidata.org/wiki/Q369309 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6ec9fef6

[]{#tetraphosphorus-hexaoxide}

####  tetraphosphorus hexaoxide
- **Definition**: tetraphosphorus hexaoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - P4O6
- **Matches:**
  - https://www.wikidata.org/wiki/Q411876 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_abd90373

[]{#lead(ii)-oxide}

####  lead(II) oxide
- **Definition**: lead(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PbO
- **Matches:**
  - https://www.wikidata.org/wiki/Q407879 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_71d63f93

[]{#lead-dioxide}

####  lead dioxide
- **Definition**: lead dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PbO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q410749 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bcef2678

[]{#palladium(ii)-oxide}

####  palladium(II) oxide
- **Definition**: palladium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PdO
- **Matches:**
  - https://www.wikidata.org/wiki/Q421063 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_895707a7

[]{#promethium(iii)-oxide}

####  promethium(III) oxide
- **Definition**: promethium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Pm2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q421194 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f937fd73

[]{#plutonium(iv)-oxide}

####  plutonium(IV) oxide
- **Definition**: plutonium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PuO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q413258 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f1eaea78

[]{#rubidium-oxide}

####  rubidium oxide
- **Definition**: rubidium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Rb2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q425243 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_288073f5

[]{#rhenium(vii)-oxide}

####  rhenium(VII) oxide
- **Definition**: rhenium(VII) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Re2O7
- **Matches:**
  - https://www.wikidata.org/wiki/Q418325 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dd8b38a2

[]{#rhenium-trioxide}

####  rhenium trioxide
- **Definition**: rhenium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ReO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q418954 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f51699f5

[]{#rhodium(iii)-oxide}

####  rhodium(III) oxide
- **Definition**: rhodium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Rh2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q3488660 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9cad68a9

[]{#ruthenium(iv)-oxide}

####  ruthenium(IV) oxide
- **Definition**: ruthenium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - RuO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q417022 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1bd5e88e

[]{#ruthenium-tetroxide}

####  ruthenium tetroxide
- **Definition**: ruthenium tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - RuO4
- **Matches:**
  - https://www.wikidata.org/wiki/Q416759 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_96b4ede4

[]{#antimony-trioxide}

####  antimony trioxide
- **Definition**: antimony trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sb2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q409035 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e163bfbd

[]{#antimony-pentoxide}

####  antimony pentoxide
- **Definition**: antimony pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sb2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q419889 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3b73905f

[]{#scandium-oxide}

####  scandium oxide
- **Definition**: scandium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sc2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q418024 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2b783324

[]{#selenium-dioxide}

####  selenium dioxide
- **Definition**: selenium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SeO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q411386 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_175ec3f0

[]{#selenium-trioxide}

####  selenium trioxide
- **Definition**: selenium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SeO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q6070 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a9fa058d

[]{#silicon-dioxide}

####  silicon dioxide
- **Definition**: silicon dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SiO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q116269 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_32a7b3c4

[]{#samarium(iii)-oxide}

####  samarium(III) oxide
- **Definition**: samarium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sm2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q421401 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f4364919

[]{#tin(ii)-oxide}

####  tin(II) oxide
- **Definition**: tin(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SnO
- **Matches:**
  - https://www.wikidata.org/wiki/Q204980 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4276df9f

[]{#tin(iv)-oxide}

####  tin(IV) oxide
- **Definition**: tin(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SnO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q129163 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_56fa630e

[]{#sulfur-dioxide}

####  sulfur dioxide
- **Definition**: sulfur dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q5282 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f4416752

[]{#sulfur-trioxide}

####  sulfur trioxide
- **Definition**: sulfur trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q242715 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c41c55a1

[]{#strontium-oxide}

####  strontium oxide
- **Definition**: strontium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SrO
- **Matches:**
  - https://www.wikidata.org/wiki/Q418413 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_83e09194

[]{#tantalum-pentoxide}

####  tantalum pentoxide
- **Definition**: tantalum pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ta2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q425103 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_395b4a43

[]{#terbium(iii)-oxide}

####  terbium(III) oxide
- **Definition**: terbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tb2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419879 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a4a81fb8

[]{#tellurium-dioxide}

####  tellurium dioxide
- **Definition**: tellurium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TeO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q425220 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_015515bc

[]{#tellurium-trioxide}

####  tellurium trioxide
- **Definition**: tellurium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TeO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419581 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_99e07679

[]{#thorium-dioxide}

####  thorium dioxide
- **Definition**: thorium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ThO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q420634 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_65128842

[]{#titanium(iii)-oxide}

####  titanium(III) oxide
- **Definition**: titanium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ti2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q2626625 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4b5def73

[]{#titanium-dioxide}

####  titanium dioxide
- **Definition**: titanium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TiO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q193521 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bbd38114

[]{#titanium-dioxide}

####  titanium dioxide
- **Definition**: titanium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TiO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q193521 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f3eaf255

[]{#thallium(i)-oxide}

####  thallium(I) oxide
- **Definition**: thallium(I) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tl2O
- **Matches:**
  - https://www.wikidata.org/wiki/Q2983581 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_df381ea7

[]{#thallium(iii)-oxide}

####  thallium(III) oxide
- **Definition**: thallium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tl2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q419381 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_278bad09

[]{#thulium(iii)-oxide}

####  thulium(III) oxide
- **Definition**: thulium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tm2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q258759 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9421cf94

[]{#uranium-dioxide}

####  uranium dioxide
- **Definition**: uranium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - UO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q378379 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cdfad8d8

[]{#uranium-trioxide}

####  uranium trioxide
- **Definition**: uranium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - UO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q425420 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0a93f841

[]{#vanadium(iii)-oxide}

####  vanadium(III) oxide
- **Definition**: vanadium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - V2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q425350 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c8abed0

[]{#vanadium(v)-oxide}

####  vanadium(V) oxide
- **Definition**: vanadium(V) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - V2O5
- **Matches:**
  - https://www.wikidata.org/wiki/Q409173 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f832c87b

[]{#vanadium(ii)-oxide}

####  vanadium(II) oxide
- **Definition**: vanadium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - VO
- **Matches:**
  - https://www.wikidata.org/wiki/Q1966236 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e207f179

[]{#vanadium(iv)-oxide}

####  vanadium(IV) oxide
- **Definition**: vanadium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - VO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q421440 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_07ec6d7d

[]{#tungsten(iii)-oxide}

####  tungsten(III) oxide
- **Definition**: tungsten(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - W2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q379014 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_53345ff8

[]{#tungsten(iv)-oxide}

####  tungsten(IV) oxide
- **Definition**: tungsten(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - WO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q421387 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4494faac

[]{#tungsten-trioxide}

####  tungsten trioxide
- **Definition**: tungsten trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - WO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q417406 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_95ed9d33

[]{#xenon-trioxide}

####  xenon trioxide
- **Definition**: xenon trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - XeO3
- **Matches:**
  - https://www.wikidata.org/wiki/Q411169 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_244e4f2c

[]{#xenon-tetroxide}

####  xenon tetroxide
- **Definition**: xenon tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - XeO4
- **Matches:**
  - https://www.wikidata.org/wiki/Q411822 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f478024d

[]{#yttrium-oxide}

####  yttrium oxide
- **Definition**: yttrium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Y2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q414685 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1a025f99

[]{#ytterbium(iii)-oxide}

####  ytterbium(III) oxide
- **Definition**: ytterbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Yb2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q416720 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0fc5693f

[]{#zinc-oxide}

####  zinc oxide
- **Definition**: zinc oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ZnO
- **Matches:**
  - https://www.wikidata.org/wiki/Q190077 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bd12be77

[]{#zirconium-dioxide}

####  zirconium dioxide
- **Definition**: zirconium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ZrO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q36200 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b5b645cf

[]{#bismuth(iii)-oxide}

####  bismuth(III) oxide
- **Definition**: bismuth(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Bi2O3
- **Matches:**
  - https://www.wikidata.org/wiki/Q252536 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_87cca409

[]{#chromium(iv)-oxide}

####  chromium(IV) oxide
- **Definition**: chromium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO2
- **Matches:**
  - https://www.wikidata.org/wiki/Q2366389 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7d234b2a

[]{#chemical-element}

###  chemical element
- **Definition**: A species of atoms defined by its number of protons.
- **Child of**:
  - [`chemical substance`](#chemical-substance)
- **Other Properties:**
  - **note**: 
This is a reproduction of a subset of Periodic table of elements (thesaurus) by Institute for scientific and technical information (Inist) - CNRS/UPS76 and published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license at https://loterre.istex.fr/8HQ/en/ .
- **Matches:**
  - https://www.wikidata.org/wiki/Q11344 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bafa70d4

[]{#hydrogène}

####  hydrogène
* `hydrogen`
* `hidrógeno`
- **Definition**: Élément de numéro atomique 1 et de symbole H.
- **Definition**: Chemical element with atomic number 1 and symbol H.
- **Definition**: Elemento químico de número atómico 1 y símbolo H.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - H, 
  - H, 
  - H, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_24634 (closeMatch)
  - http://fr.dbpedia.org/page/Hydrogène (exactMatch)
  - http://dbpedia.org/page/Hydrogen (exactMatch)
  - http://es.dbpedia.org/page/Hidrógeno (exactMatch)
  - https://fr.wikipedia.org/wiki/Hydrogène (exactMatch)
  - https://en.wikipedia.org/wiki/Hydrogen (exactMatch)
  - https://es.wikipedia.org/wiki/Hidrógeno (exactMatch)
  - https://www.wikidata.org/wiki/Q556 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-DTLN6DML-5

[]{#carbone}

####  carbone
* `carbon`
* `carbono`
- **Definition**: Élément de numéro atomique 6 et de symbole C.
- **Definition**: Chemical element with atomic number 6 and symbol C.
- **Definition**: Elemento químico de número atómico 6 y símbolo C.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - C, 
  - C, 
  - C, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27594 (closeMatch)
  - http://fr.dbpedia.org/page/Carbone (exactMatch)
  - http://dbpedia.org/page/Carbon (exactMatch)
  - http://es.dbpedia.org/page/Carbono (exactMatch)
  - https://fr.wikipedia.org/wiki/Carbone (exactMatch)
  - https://en.wikipedia.org/wiki/Carbon (exactMatch)
  - https://es.wikipedia.org/wiki/Carbono (exactMatch)
  - https://www.wikidata.org/wiki/Q623 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GPJ5KG69-K

[]{#azote}

####  azote
* `nitrogen`
* `nitrógeno`
- **Definition**: Élément de numéro atomique 7 et de symbole N.
- **Definition**: Chemical element with atomic number 7 and symbol N.
- **Definition**: Elemento químico de número atómico 7 y símbolo N.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - N, 
  - N, 
  - N, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_25555 (closeMatch)
  - http://fr.dbpedia.org/page/Azote (exactMatch)
  - http://dbpedia.org/page/Nitrogen (exactMatch)
  - http://es.dbpedia.org/page/Nitrógeno (exactMatch)
  - https://fr.wikipedia.org/wiki/Azote (exactMatch)
  - https://en.wikipedia.org/wiki/Nitrogen (exactMatch)
  - https://es.wikipedia.org/wiki/Nitrógeno (exactMatch)
  - https://www.wikidata.org/wiki/Q627 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FMW7R7GT-H

[]{#oxygène}

####  oxygène
* `oxygen`
* `oxígeno`
- **Definition**: Élément de numéro atomique 8 et de symbole O.
- **Definition**: Chemical element with atomic number 8 and symbol O.
- **Definition**: Elemento químico de número atómico 8 y símbolo O.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - O, 
  - O, 
  - O, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_25805 (closeMatch)
  - http://fr.dbpedia.org/page/Oxygène (exactMatch)
  - http://dbpedia.org/page/Oxygen (exactMatch)
  - http://es.dbpedia.org/page/Oxígeno (exactMatch)
  - https://fr.wikipedia.org/wiki/Oxygène (exactMatch)
  - https://en.wikipedia.org/wiki/Oxygen (exactMatch)
  - https://es.wikipedia.org/wiki/Oxígeno (exactMatch)
  - https://www.wikidata.org/wiki/Q629 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-RX5D8P7R-1

[]{#phosphore}

####  phosphore
* `phosphorus`
* `fósforo`
- **Definition**: Élément de numéro atomique 15 et de symbole P.
- **Definition**: Chemical element with atomic number 15 and symbol P.
- **Definition**: Elemento químico de número atómico 15 y símbolo P.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - P, 
  - P, 
  - P, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28659 (closeMatch)
  - http://fr.dbpedia.org/page/Phosphore (exactMatch)
  - http://dbpedia.org/page/Phosphorus (exactMatch)
  - http://es.dbpedia.org/page/Fósforo (exactMatch)
  - https://fr.wikipedia.org/wiki/Phosphore (exactMatch)
  - https://en.wikipedia.org/wiki/Phosphorus (exactMatch)
  - https://es.wikipedia.org/wiki/Fósforo (exactMatch)
  - https://www.wikidata.org/wiki/Q674 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-VC1M1XR4-F

[]{#soufre}

####  soufre
* `sulfur`
* `azufre`
- **Definition**: Élément de numéro atomique 16 et de symbole S.
- **Definition**: Chemical element with atomic number 16 and symbol S.
- **Definition**: Elemento químico de número atómico 16 y símbolo S.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - S, 
  - S, 
  - S, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_26833 (closeMatch)
  - http://fr.dbpedia.org/page/Soufre (exactMatch)
  - http://dbpedia.org/page/Sulfur (exactMatch)
  - http://es.dbpedia.org/page/Azufre (exactMatch)
  - https://fr.wikipedia.org/wiki/Soufre (exactMatch)
  - https://en.wikipedia.org/wiki/Sulfur (exactMatch)
  - https://es.wikipedia.org/wiki/Azufre (exactMatch)
  - https://www.wikidata.org/wiki/Q682 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NK1JKPQC-4

[]{#sélénium}

####  sélénium
* `selenium`
* `selenio`
- **Definition**: Élément de numéro atomique 34 et de symbole Se.
- **Definition**: Chemical element with atomic number 34 and symbol
Se.
- **Definition**: Elemento químico de número atómico 34 y símbolo Se.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Se, 
  - Se, 
  - Se, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27568 (closeMatch)
  - http://fr.dbpedia.org/page/Sélénium (exactMatch)
  - http://dbpedia.org/page/Selenium (exactMatch)
  - http://es.dbpedia.org/page/Selenio (exactMatch)
  - https://fr.wikipedia.org/wiki/Sélénium (exactMatch)
  - https://en.wikipedia.org/wiki/Selenium (exactMatch)
  - https://es.wikipedia.org/wiki/Selenio (exactMatch)
  - https://www.wikidata.org/wiki/Q876 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-SSFNCHSK-B

[]{#hélium}

####  hélium
* `helium`
* `helio`
- **Definition**: Élément de numéro atomique 2 et de symbole He.
- **Definition**: Chemical element with atomic number 2 and symbol He.
- **Definition**: Elemento químico de número atómico 2 y símbolo He.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - He, 
  - He, 
  - He, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30217 (closeMatch)
  - http://fr.dbpedia.org/page/Hélium (exactMatch)
  - http://dbpedia.org/page/Helium (exactMatch)
  - http://es.dbpedia.org/page/Helio (exactMatch)
  - https://fr.wikipedia.org/wiki/Hélium (exactMatch)
  - https://en.wikipedia.org/wiki/Helium (exactMatch)
  - https://es.wikipedia.org/wiki/Helio (exactMatch)
  - https://www.wikidata.org/wiki/Q560 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-J65QLDDJ-T

[]{#lithium}

####  lithium
* `lithium`
* `litio`
- **Definition**: Élément de numéro atomique 3 et de symbole Li.
- **Definition**: Chemical element with atomic number 3 and symbol Li.
- **Definition**: Elemento químico de número atómico 3 y símbolo Li.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Li, 
  - Li, 
  - Li, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30145 (closeMatch)
  - http://fr.dbpedia.org/page/Lithium (exactMatch)
  - http://dbpedia.org/page/Lithium (exactMatch)
  - http://es.dbpedia.org/page/Litio (exactMatch)
  - https://fr.wikipedia.org/wiki/Lithium (exactMatch)
  - https://en.wikipedia.org/wiki/Lithium (exactMatch)
  - https://es.wikipedia.org/wiki/Litio (exactMatch)
  - https://www.wikidata.org/wiki/Q568 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NVMP6P5B-4

[]{#béryllium}

####  béryllium
* `beryllium`
* `berilio`
- **Definition**: Élément de numéro atomique 4 et de symbole Be.
- **Definition**: Chemical element with atomic number 4 and symbol Be.
- **Definition**: Elemento químico de número atómico 4 y símbolo Be.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Be, 
  - Be, 
  - Be, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30501 (closeMatch)
  - http://fr.dbpedia.org/page/Béryllium (exactMatch)
  - http://dbpedia.org/page/Beryllium (exactMatch)
  - http://es.dbpedia.org/page/Berilio (exactMatch)
  - https://fr.wikipedia.org/wiki/Béryllium (exactMatch)
  - https://en.wikipedia.org/wiki/Beryllium (exactMatch)
  - https://es.wikipedia.org/wiki/Berilio (exactMatch)
  - https://www.wikidata.org/wiki/Q569 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-J7L957H4-S

[]{#sodium}

####  sodium
* `sodium`
* `sodio`
- **Definition**: Élément de numéro atomique 11 et de symbole Na.
- **Definition**: Chemical element with atomic number 11 and symbol
Na.
- **Definition**: Elemento químico de número atómico 11 y símbolo Na.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Na, 
  - Na, 
  - Na, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_26708 (closeMatch)
  - http://fr.dbpedia.org/page/Sodium (exactMatch)
  - http://dbpedia.org/page/Sodium (exactMatch)
  - http://es.dbpedia.org/page/Sodio (exactMatch)
  - https://fr.wikipedia.org/wiki/Sodium (exactMatch)
  - https://en.wikipedia.org/wiki/Sodium (exactMatch)
  - https://es.wikipedia.org/wiki/Sodio (exactMatch)
  - https://www.wikidata.org/wiki/Q658 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-D9J9ZG62-C

[]{#magnésium}

####  magnésium
* `magnesium`
* `magnesio`
- **Definition**: Élément de numéro atomique 12 et de symbole Mg.
- **Definition**: Chemical element with atomic number 12 and symbol
Mg.
- **Definition**: Elemento químico de número atómico 12 y símbolo Mg.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Mg, 
  - Mg, 
  - Mg, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_25107 (closeMatch)
  - http://fr.dbpedia.org/page/Magnésium (exactMatch)
  - http://dbpedia.org/page/Magnesium (exactMatch)
  - http://es.dbpedia.org/page/Magnesio (exactMatch)
  - https://fr.wikipedia.org/wiki/Magnésium (exactMatch)
  - https://en.wikipedia.org/wiki/Magnesium (exactMatch)
  - https://es.wikipedia.org/wiki/Magnesio (exactMatch)
  - https://www.wikidata.org/wiki/Q660 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-S4R6VJD9-W

[]{#potassium}

####  potassium
* `potassium`
* `potasio`
- **Definition**: Élément de numéro atomique 19 et de symbole K.
- **Definition**: Chemical element with atomic number 19 and symbol K.
- **Definition**: Elemento químico de número atómico 19 y símbolo K.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - K, 
  - K, 
  - K, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_26216 (closeMatch)
  - http://fr.dbpedia.org/page/Potassium (exactMatch)
  - http://dbpedia.org/page/Potassium (exactMatch)
  - http://es.dbpedia.org/page/Potasio (exactMatch)
  - https://fr.wikipedia.org/wiki/Potassium (exactMatch)
  - https://en.wikipedia.org/wiki/Potassium (exactMatch)
  - https://es.wikipedia.org/wiki/Potasio (exactMatch)
  - https://www.wikidata.org/wiki/Q703 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-LGJQJQQ9-N

[]{#calcium}

####  calcium
* `calcium`
* `calcio`
- **Definition**: Élément de numéro atomique 20 et de symbole Ca.
- **Definition**: Chemical element with atomic number 20 and symbol
Ca.
- **Definition**: Elemento químico de número atómico 20 y símbolo Ca.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ca, 
  - Ca, 
  - Ca, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_22984 (closeMatch)
  - http://fr.dbpedia.org/page/Calcium (exactMatch)
  - http://dbpedia.org/page/Calcium (exactMatch)
  - http://es.dbpedia.org/page/Calcio (exactMatch)
  - https://fr.wikipedia.org/wiki/Calcium (exactMatch)
  - https://en.wikipedia.org/wiki/Calcium (exactMatch)
  - https://es.wikipedia.org/wiki/Calcio (exactMatch)
  - https://www.wikidata.org/wiki/Q706 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-SX8VX34H-4

[]{#rubidium}

####  rubidium
* `rubidium`
* `rubidio`
- **Definition**: Élément de numéro atomique 37 et de symbole Rb.
- **Definition**: Chemical element with atomic number 37 and symbol
Rb.
- **Definition**: Elemento químico de número atómico 37 y símbolo Rb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Rb, 
  - Rb, 
  - Rb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33322 (closeMatch)
  - http://fr.dbpedia.org/page/Rubidium (exactMatch)
  - http://dbpedia.org/page/Rubidium (exactMatch)
  - http://es.dbpedia.org/page/Rubidio (exactMatch)
  - https://fr.wikipedia.org/wiki/Rubidium (exactMatch)
  - https://en.wikipedia.org/wiki/Rubidium (exactMatch)
  - https://es.wikipedia.org/wiki/Rubidio (exactMatch)
  - https://www.wikidata.org/wiki/Q895 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-M32L945D-3

[]{#strontium}

####  strontium
* `strontium`
* `estroncio`
- **Definition**: Élément de numéro atomique 38 et de symbole Sr.
- **Definition**: Chemical element with atomic number 38 and symbol
Sr.
- **Definition**: Elemento químico de número atómico 38 y símbolo Sr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sr, 
  - Sr, 
  - Sr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33324 (closeMatch)
  - http://fr.dbpedia.org/page/Strontium (exactMatch)
  - http://dbpedia.org/page/Strontium (exactMatch)
  - http://es.dbpedia.org/page/Estroncio (exactMatch)
  - https://fr.wikipedia.org/wiki/Strontium (exactMatch)
  - https://en.wikipedia.org/wiki/Strontium (exactMatch)
  - https://es.wikipedia.org/wiki/Estroncio (exactMatch)
  - https://www.wikidata.org/wiki/Q938 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GL3J8X2V-F

[]{#césium}

####  césium
* `caesium`
* `cesio`
- **Definition**: Élément de numéro atomique 55 et de symbole Cs.
- **Definition**: Chemical element with atomic number 55 and symbol
Cs.
- **Definition**: Elemento químico de número atómico 55 y símbolo Cs.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cs, 
  - Cs, 
  - cesium, 
  - Cs, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30514 (closeMatch)
  - http://fr.dbpedia.org/page/Césium (exactMatch)
  - http://dbpedia.org/page/Cesium (exactMatch)
  - http://es.dbpedia.org/page/Cesio (exactMatch)
  - https://fr.wikipedia.org/wiki/Césium (exactMatch)
  - https://en.wikipedia.org/wiki/Cesium (exactMatch)
  - https://es.wikipedia.org/wiki/Cesio (exactMatch)
  - https://www.wikidata.org/wiki/Q1108 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-MQQTJBS0-W

[]{#baryum}

####  baryum
* `barium`
* `bario`
- **Definition**: Élément de numéro atomique 56 et de symbole Ba.
- **Definition**: Chemical element with atomic number 56 and symbol
Ba.
- **Definition**: Elemento químico de número atómico 56 y símbolo Ba.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ba, 
  - Ba, 
  - Ba, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_32594 (closeMatch)
  - http://fr.dbpedia.org/page/Baryum (exactMatch)
  - http://dbpedia.org/page/Barium (exactMatch)
  - http://es.dbpedia.org/page/Bario (exactMatch)
  - https://fr.wikipedia.org/wiki/Baryum (exactMatch)
  - https://en.wikipedia.org/wiki/Barium (exactMatch)
  - https://es.wikipedia.org/wiki/Bario (exactMatch)
  - https://www.wikidata.org/wiki/Q1112 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-P1S60994-X

[]{#francium}

####  francium
* `francium`
* `francio`
- **Definition**: Élément de numéro atomique 87 et de symbole Fr.
- **Definition**: Chemical element with atomic number 87 and symbol
Fr.
- **Definition**: Elemento químico de número atómico 87 y símbolo Fr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Fr, 
  - Fr, 
  - Fr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33323 (closeMatch)
  - http://fr.dbpedia.org/page/Francium (exactMatch)
  - http://dbpedia.org/page/Francium (exactMatch)
  - http://es.dbpedia.org/page/Francio (exactMatch)
  - https://fr.wikipedia.org/wiki/Francium (exactMatch)
  - https://en.wikipedia.org/wiki/Francium (exactMatch)
  - https://es.wikipedia.org/wiki/Francio (exactMatch)
  - https://www.wikidata.org/wiki/Q671 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BMW5TDQD-V

[]{#radium}

####  radium
* `radium`
* `radio`
- **Definition**: Élément de numéro atomique 88 et de symbole Ra.
- **Definition**: Chemical element with atomic number 88 and symbol
Ra.
- **Definition**: Elemento químico de número atómico 88 y símbolo Ra.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ra, 
  - Ra, 
  - Ra, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33325 (closeMatch)
  - http://fr.dbpedia.org/page/Radium (exactMatch)
  - http://dbpedia.org/page/Radium (exactMatch)
  - http://es.dbpedia.org/page/Radio (exactMatch)
  - https://fr.wikipedia.org/wiki/Radium (exactMatch)
  - https://en.wikipedia.org/wiki/Radium (exactMatch)
  - https://es.wikipedia.org/wiki/Radio (exactMatch)
  - https://www.wikidata.org/wiki/Q1128 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GXFQ6HV4-P

[]{#bore}

####  bore
* `boron`
* `boro`
- **Definition**: Élément de numéro atomique 5 et de symbole B.
- **Definition**: Chemical element with atomic number 5 and symbol B.
- **Definition**: Elemento químico de número atómico 5 y símbolo B.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - B, 
  - B, 
  - B, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27560 (closeMatch)
  - http://fr.dbpedia.org/page/Bore (exactMatch)
  - http://dbpedia.org/page/Boron (exactMatch)
  - http://es.dbpedia.org/page/Boro (exactMatch)
  - https://fr.wikipedia.org/wiki/Bore (exactMatch)
  - https://en.wikipedia.org/wiki/Boron (exactMatch)
  - https://es.wikipedia.org/wiki/Boro (exactMatch)
  - https://www.wikidata.org/wiki/Q618 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BJJWZT6G-K

[]{#fluor}

####  fluor
* `fluorine`
* `fluor`
- **Definition**: Élément de numéro atomique 9 et de symbole F.
- **Definition**: Chemical element with atomic number 9 and symbol F.
- **Definition**: Elemento químico de número atómico 9 y símbolo F.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - F, 
  - F, 
  - F, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_24061 (closeMatch)
  - http://fr.dbpedia.org/page/Fluor (exactMatch)
  - http://dbpedia.org/page/Fluorine (exactMatch)
  - http://es.dbpedia.org/page/Fluor (exactMatch)
  - https://fr.wikipedia.org/wiki/Fluor (exactMatch)
  - https://en.wikipedia.org/wiki/Fluorine (exactMatch)
  - https://es.wikipedia.org/wiki/Fluor (exactMatch)
  - https://www.wikidata.org/wiki/Q650 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-XNB95WRM-4

[]{#néon}

####  néon
* `neon`
* `neón`
- **Definition**: Élément de numéro atomique 10 et de symbole Ne.
- **Definition**: Chemical element with atomic number 10 and symbol
Ne.
- **Definition**: Elemento químico de número atómico 10 y símbolo Ne.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ne, 
  - Ne, 
  - Ne, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33310 (closeMatch)
  - http://fr.dbpedia.org/page/Néon (exactMatch)
  - http://dbpedia.org/page/Neon (exactMatch)
  - http://es.dbpedia.org/page/Neón (exactMatch)
  - https://fr.wikipedia.org/wiki/Néon (exactMatch)
  - https://en.wikipedia.org/wiki/Neon (exactMatch)
  - https://es.wikipedia.org/wiki/Neón (exactMatch)
  - https://www.wikidata.org/wiki/Q654 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-QT7P52MZ-9

[]{#aluminium}

####  aluminium
* `aluminium`
* `aluminio`
- **Definition**: Élément de numéro atomique 13 et de symbole Al.
- **Definition**: Chemical element with atomic number 13 and symbol
Al.
- **Definition**: Elemento químico de número atómico 13 y símbolo Al.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Al, 
  - Al, 
  - aluminum, 
  - Al, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28984 (closeMatch)
  - http://fr.dbpedia.org/page/Aluminium (exactMatch)
  - http://dbpedia.org/page/Aluminium (exactMatch)
  - http://es.dbpedia.org/page/Aluminio (exactMatch)
  - https://fr.wikipedia.org/wiki/Aluminium (exactMatch)
  - https://en.wikipedia.org/wiki/Aluminium (exactMatch)
  - https://es.wikipedia.org/wiki/Aluminio (exactMatch)
  - https://www.wikidata.org/wiki/Q663 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-X55C5RJ1-N

[]{#silicium}

####  silicium
* `silicon`
* `silicio`
- **Definition**: Élément de numéro atomique 14 et de symbole Si.
- **Definition**: Chemical element with atomic number 14 and symbol
Si.
- **Definition**: Elemento químico de número atómico 14 y símbolo Si.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Si, 
  - Si, 
  - Si, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27573 (closeMatch)
  - http://fr.dbpedia.org/page/Silicium (exactMatch)
  - http://dbpedia.org/page/Silicon (exactMatch)
  - http://es.dbpedia.org/page/Silicio (exactMatch)
  - https://fr.wikipedia.org/wiki/Silicium (exactMatch)
  - https://en.wikipedia.org/wiki/Silicon (exactMatch)
  - https://es.wikipedia.org/wiki/Silicio (exactMatch)
  - https://www.wikidata.org/wiki/Q670 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-Q69H14CX-1

[]{#chlore}

####  chlore
* `chlorine`
* `cloro`
- **Definition**: Élément de numéro atomique 17 et de symbole Cl.
- **Definition**: Chemical element with atomic number 17 and symbol
Cl.
- **Definition**: Elemento químico de número atómico 17 y símbolo Cl.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cl, 
  - Cl, 
  - Cl, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_23116 (closeMatch)
  - http://fr.dbpedia.org/page/Chlore (exactMatch)
  - http://dbpedia.org/page/Chlorine (exactMatch)
  - http://es.dbpedia.org/page/Cloro (exactMatch)
  - https://fr.wikipedia.org/wiki/Chlore (exactMatch)
  - https://en.wikipedia.org/wiki/Chlorine (exactMatch)
  - https://es.wikipedia.org/wiki/Cloro (exactMatch)
  - https://www.wikidata.org/wiki/Q688 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-HKV44ZNF-C

[]{#argon}

####  argon
* `argon`
* `argón`
- **Definition**: Élément de numéro atomique 18 et de symbole Ar.
- **Definition**: Chemical element with atomic number 18 and symbol
Ar.
- **Definition**: Elemento químico de número atómico 18 y símbolo Ar.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ar, 
  - Ar, 
  - Ar, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33311 (closeMatch)
  - http://fr.dbpedia.org/page/Argon (exactMatch)
  - http://dbpedia.org/page/Argon (exactMatch)
  - http://es.dbpedia.org/page/Argón (exactMatch)
  - https://fr.wikipedia.org/wiki/Argon (exactMatch)
  - https://en.wikipedia.org/wiki/Argon (exactMatch)
  - https://es.wikipedia.org/wiki/Argón (exactMatch)
  - https://www.wikidata.org/wiki/Q696 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-XZG1JMS2-0

[]{#gallium}

####  gallium
* `gallium`
* `galio`
- **Definition**: Élément de numéro atomique 31 et de symbole Ga.
- **Definition**: Chemical element with atomic number 31 and symbol
Ga.
- **Definition**: Elemento químico de número atómico 31 y símbolo Ga.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ga, 
  - Ga, 
  - Ga, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33326 (closeMatch)
  - http://fr.dbpedia.org/page/Gallium (exactMatch)
  - http://dbpedia.org/page/Gallium (exactMatch)
  - http://es.dbpedia.org/page/Galio (exactMatch)
  - https://fr.wikipedia.org/wiki/Gallium (exactMatch)
  - https://en.wikipedia.org/wiki/Gallium (exactMatch)
  - https://es.wikipedia.org/wiki/Galio (exactMatch)
  - https://www.wikidata.org/wiki/Q861 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-M1Q18DX1-K

[]{#germanium}

####  germanium
* `germanium`
* `germanio`
- **Definition**: Élément de numéro atomique 32 et de symbole Ge.
- **Definition**: Chemical element with atomic number 32 and symbol
Ge.
- **Definition**: Elemento químico de número atómico 32 y símbolo Ge.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ge, 
  - Ge, 
  - Ge, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30441 (closeMatch)
  - http://fr.dbpedia.org/page/Germanium (exactMatch)
  - http://dbpedia.org/page/Germanium (exactMatch)
  - http://es.dbpedia.org/page/Germanio (exactMatch)
  - https://fr.wikipedia.org/wiki/Germanium (exactMatch)
  - https://en.wikipedia.org/wiki/Germanium (exactMatch)
  - https://es.wikipedia.org/wiki/Germanio (exactMatch)
  - https://www.wikidata.org/wiki/Q867 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BP5PPHC4-5

[]{#arsenic}

####  arsenic
* `arsenic`
* `arsénico`
- **Definition**: Élément de numéro atomique 33 et de symbole As.
- **Definition**: Chemical element with atomic number 33 and symbol
As.
- **Definition**: Elemento químico de número atómico 33 y símbolo As.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - As, 
  - As, 
  - As, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27563 (closeMatch)
  - http://fr.dbpedia.org/page/Arsenic (exactMatch)
  - http://dbpedia.org/page/Arsenic (exactMatch)
  - http://es.dbpedia.org/page/Arsénico (exactMatch)
  - https://fr.wikipedia.org/wiki/Arsenic (exactMatch)
  - https://en.wikipedia.org/wiki/Arsenic (exactMatch)
  - https://es.wikipedia.org/wiki/Arsénico (exactMatch)
  - https://www.wikidata.org/wiki/Q871 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-B31MNC3P-0

[]{#brome}

####  brome
* `bromine`
* `bromo`
- **Definition**: Élément de numéro atomique 35 et de symbole Br.
- **Definition**: Chemical element with atomic number 35 and symbol
Br.
- **Definition**: Elemento químico de número atómico 35 y símbolo Br.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Br, 
  - Br, 
  - Br, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_22927 (closeMatch)
  - http://fr.dbpedia.org/page/Brome (exactMatch)
  - http://dbpedia.org/page/Bromine (exactMatch)
  - http://es.dbpedia.org/page/Bromo (exactMatch)
  - https://fr.wikipedia.org/wiki/Brome (exactMatch)
  - https://en.wikipedia.org/wiki/Bromine (exactMatch)
  - https://es.wikipedia.org/wiki/Bromo (exactMatch)
  - https://www.wikidata.org/wiki/Q879 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-JKQD0SHX-7

[]{#krypton}

####  krypton
* `krypton`
* `kriptón`
- **Definition**: Élément de numéro atomique 36 et de symbole Kr.
- **Definition**: Chemical element with atomic number 36 and symbol
Kr.
- **Definition**: Elemento químico de número atómico 36 y símbolo Kr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Kr, 
  - Kr, 
  - Kr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33312 (closeMatch)
  - http://fr.dbpedia.org/page/Krypton (exactMatch)
  - http://dbpedia.org/page/Krypton (exactMatch)
  - http://es.dbpedia.org/page/Kriptón (exactMatch)
  - https://fr.wikipedia.org/wiki/Krypton (exactMatch)
  - https://en.wikipedia.org/wiki/Krypton (exactMatch)
  - https://es.wikipedia.org/wiki/Kriptón (exactMatch)
  - https://www.wikidata.org/wiki/Q888 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-H4KTFDCX-D

[]{#indium}

####  indium
* `indium`
* `indio`
- **Definition**: Élément de numéro atomique 49 et de symbole In.
- **Definition**: Chemical element with atomic number 49 and symbol
In.
- **Definition**: Elemento químico de número atómico 49 y símbolo In.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - In, 
  - In, 
  - In, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30430 (closeMatch)
  - http://fr.dbpedia.org/page/Indium (exactMatch)
  - http://dbpedia.org/page/Indium (exactMatch)
  - http://es.dbpedia.org/page/Indio (exactMatch)
  - https://fr.wikipedia.org/wiki/Indium (exactMatch)
  - https://en.wikipedia.org/wiki/Indium (exactMatch)
  - https://es.wikipedia.org/wiki/Indio (exactMatch)
  - https://www.wikidata.org/wiki/Q1094 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BRKZVG3H-8

[]{#étain}

####  étain
* `tin`
* `estaño`
- **Definition**: Élément de numéro atomique 50 et de symbole Sn.
- **Definition**: Chemical element with atomic number 50 and symbol
Sn.
- **Definition**: Elemento químico de número atómico 50 y símbolo Sn.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sn, 
  - Sn, 
  - Sn, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27007 (closeMatch)
  - http://es.dbpedia.org/page/Zinc (exactMatch)
  - http://fr.dbpedia.org/page/étain (exactMatch)
  - http://dbpedia.org/page/Tin (exactMatch)
  - https://fr.wikipedia.org/wiki/Étain (exactMatch)
  - https://en.wikipedia.org/wiki/Tin (exactMatch)
  - https://es.wikipedia.org/wiki/ (exactMatch)
  - https://www.wikidata.org/wiki/Q1096 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZK5FBL3T-Z

[]{#antimoine}

####  antimoine
* `antimony`
* `antimonio`
- **Definition**: Élément de numéro atomique 51 et de symbole Sb.
- **Definition**: Chemical element with atomic number 51 and symbol
Sb.
- **Definition**: Elemento químico de número atómico 51 y símbolo Sb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sb, 
  - Sb, 
  - Sb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30513 (closeMatch)
  - http://fr.dbpedia.org/page/Antimoine (exactMatch)
  - http://dbpedia.org/page/Antimony (exactMatch)
  - http://es.dbpedia.org/page/Antimonio (exactMatch)
  - https://fr.wikipedia.org/wiki/Antimoine (exactMatch)
  - https://en.wikipedia.org/wiki/Antimony (exactMatch)
  - https://es.wikipedia.org/wiki/Antimonio (exactMatch)
  - https://www.wikidata.org/wiki/Q1099 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-LGWKM8TW-9

[]{#tellure}

####  tellure
* `tellurium`
* `teluro`
- **Definition**: Élément de numéro atomique 52 et de symbole Te.
- **Definition**: Chemical element with atomic number 52 and symbol
Te.
- **Definition**: Elemento químico de número atómico 52 y símbolo Te.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Te, 
  - Te, 
  - Te, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30452 (closeMatch)
  - http://fr.dbpedia.org/page/Tellure (exactMatch)
  - http://dbpedia.org/page/Tellurium (exactMatch)
  - http://es.dbpedia.org/page/Teluro (exactMatch)
  - https://fr.wikipedia.org/wiki/Tellure (exactMatch)
  - https://en.wikipedia.org/wiki/Tellurium (exactMatch)
  - https://es.wikipedia.org/wiki/Teluro (exactMatch)
  - https://www.wikidata.org/wiki/Q1100 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-SNW71HFC-W

[]{#iode}

####  iode
* `iodine`
* `iodo`
- **Definition**: Élément de numéro atomique 53 et de symbole I.
- **Definition**: Chemical element with atomic number 53 and symbol I.
- **Definition**: Elemento químico de número atómico 53 y símbolo I.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - I, 
  - I, 
  - I, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_24859 (closeMatch)
  - http://fr.dbpedia.org/page/Iode (exactMatch)
  - http://dbpedia.org/page/Iodine (exactMatch)
  - http://es.dbpedia.org/page/Iodo (exactMatch)
  - https://fr.wikipedia.org/wiki/Iode (exactMatch)
  - https://en.wikipedia.org/wiki/Iodine (exactMatch)
  - https://es.wikipedia.org/wiki/Iodo (exactMatch)
  - https://www.wikidata.org/wiki/Q1103 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-W76CCWHW-C

[]{#xénon}

####  xénon
* `xenon`
* `xenón`
- **Definition**: Élément de numéro atomique 54 et de symbole Xe.
- **Definition**: Chemical element with atomic number 54 and symbol
Xe.
- **Definition**: Elemento químico de número atómico 54 y símbolo Xe.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Xe, 
  - Xe, 
  - Xe, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_32305 (closeMatch)
  - http://fr.dbpedia.org/page/Xénon (exactMatch)
  - http://dbpedia.org/page/Xenon (exactMatch)
  - http://es.dbpedia.org/page/Xenón (exactMatch)
  - https://fr.wikipedia.org/wiki/Xénon (exactMatch)
  - https://en.wikipedia.org/wiki/Xenon (exactMatch)
  - https://es.wikipedia.org/wiki/Xenón (exactMatch)
  - https://www.wikidata.org/wiki/Q1106 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-DT73NB0V-F

[]{#thallium}

####  thallium
* `thallium`
* `talio`
- **Definition**: Élément de numéro atomique 81 et de symbole Tl.
- **Definition**: Chemical element with atomic number 81 and symbol
Tl.
- **Definition**: Elemento químico de número atómico 81 y símbolo Tl.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Tl, 
  - Tl, 
  - Tl, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30440 (closeMatch)
  - http://fr.dbpedia.org/page/Thallium (exactMatch)
  - http://dbpedia.org/page/Thallium (exactMatch)
  - http://es.dbpedia.org/page/Talio (exactMatch)
  - https://fr.wikipedia.org/wiki/Thallium (exactMatch)
  - https://en.wikipedia.org/wiki/Thallium (exactMatch)
  - https://es.wikipedia.org/wiki/Talio (exactMatch)
  - https://www.wikidata.org/wiki/Q932 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-D9N33PC7-J

[]{#plomb}

####  plomb
* `lead`
* `plomo`
- **Definition**: Élément de numéro atomique 82 et de symbole Pb.
- **Definition**: Chemical element with atomic number 82 and symbol
Pb.
- **Definition**: Elemento químico de número atómico 82 y símbolo Pb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pb, 
  - Pb, 
  - Pb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_25016 (closeMatch)
  - http://fr.dbpedia.org/page/Plomb (exactMatch)
  - http://dbpedia.org/page/Lead (exactMatch)
  - http://es.dbpedia.org/page/Plomo (exactMatch)
  - https://fr.wikipedia.org/wiki/Plomb (exactMatch)
  - https://en.wikipedia.org/wiki/Lead (exactMatch)
  - https://es.wikipedia.org/wiki/Plomo (exactMatch)
  - https://www.wikidata.org/wiki/Q708 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NRPKN8GG-H

[]{#bismuth}

####  bismuth
* `bismuth`
* `bismuto`
- **Definition**: Élément de numéro atomique 83 et de symbole Bi.
- **Definition**: Chemical element with atomic number 83 and symbol
Bi.
- **Definition**: Elemento químico de número atómico 83 y símbolo Bi.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Bi, 
  - Bi, 
  - Bi, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33301 (closeMatch)
  - http://fr.dbpedia.org/page/Bismuth (exactMatch)
  - http://dbpedia.org/page/Bismuth (exactMatch)
  - http://es.dbpedia.org/page/Bismuto (exactMatch)
  - https://fr.wikipedia.org/wiki/Bismuth (exactMatch)
  - https://en.wikipedia.org/wiki/Bismuth (exactMatch)
  - https://es.wikipedia.org/wiki/Bismuto (exactMatch)
  - https://www.wikidata.org/wiki/Q942 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-SLTRM919-5

[]{#polonium}

####  polonium
* `polonium`
* `polonio`
- **Definition**: Élément de numéro atomique 84 et de symbole Po.
- **Definition**: Chemical element with atomic number 84 and symbol
Po.
- **Definition**: Elemento químico de número atómico 84 y símbolo Po.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Po, 
  - Po, 
  - Po, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33313 (closeMatch)
  - http://fr.dbpedia.org/page/Polonium (exactMatch)
  - http://dbpedia.org/page/Polonium (exactMatch)
  - http://es.dbpedia.org/page/Polonio (exactMatch)
  - https://fr.wikipedia.org/wiki/Polonium (exactMatch)
  - https://en.wikipedia.org/wiki/Polonium (exactMatch)
  - https://es.wikipedia.org/wiki/Polonio (exactMatch)
  - https://www.wikidata.org/wiki/Q979 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-HJN40QPV-B

[]{#astate}

####  astate
* `astatine`
* `astato`
- **Definition**: Élément de numéro atomique 85 et de symbole At.
- **Definition**: Chemical element with atomic number 85 and symbol
At.
- **Definition**: Elemento químico de número atómico 85 y símbolo At.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - At, 
  - At, 
  - At, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30415 (closeMatch)
  - http://fr.dbpedia.org/page/Astate (exactMatch)
  - http://dbpedia.org/page/Astatine (exactMatch)
  - http://es.dbpedia.org/page/Astato (exactMatch)
  - https://fr.wikipedia.org/wiki/Astate (exactMatch)
  - https://en.wikipedia.org/wiki/Astatine (exactMatch)
  - https://es.wikipedia.org/wiki/Astato (exactMatch)
  - https://www.wikidata.org/wiki/Q999 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-VDGS91T8-X

[]{#radon}

####  radon
* `radon`
* `radón`
- **Definition**: Élément de numéro atomique 86 et de symbole Rn.
- **Definition**: Chemical element with atomic number 86 and symbol
Rn.
- **Definition**: Elemento químico de número atómico 86 y símbolo Rn.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Rn, 
  - Rn, 
  - Rn, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33314 (closeMatch)
  - http://fr.dbpedia.org/page/Radon (exactMatch)
  - http://dbpedia.org/page/Radon (exactMatch)
  - http://es.dbpedia.org/page/Radón (exactMatch)
  - https://fr.wikipedia.org/wiki/Radon (exactMatch)
  - https://en.wikipedia.org/wiki/Radon (exactMatch)
  - https://es.wikipedia.org/wiki/Radón (exactMatch)
  - https://www.wikidata.org/wiki/Q1133 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-XZ6ZCBNG-K

[]{#oganesson}

####  oganesson
* `oganesson`
* `oganesón`
- **Definition**: Élément de numéro atomique 118 et de symbole Og. Son
nom provisoire était : ununoctium (symbole : Uuo).
- **Definition**: Chemical element with atomic number 118 and symbol
Og. Its provisional name was : ununoctium (symbol : Uuo).
- **Definition**: Elemento químico de número atómico 118 y símbolo Og.
Su nombre provisional era : ununoctio (símbolo : Uuo).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Og, 
  - élément 118, 
  - Uuo, 
  - ununoctium, 
  - Og, 
  - element 118, 
  - Uuo, 
  - ununoctium, 
  - Og, 
  - elemento 118, 
  - Uuo, 
  - ununoctio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - Chemical and physical properties of superheavy elements, B. Fricke. J. McMinn, 1976, Naturwissenschaften vol.63, page 162 - 170, https://doi.org/10.1007/BFb0116498, 
- **Matches:**
  - http://fr.dbpedia.org/page/Ununoctium (exactMatch)
  - http://dbpedia.org/page/Oganesson (exactMatch)
  - http://es.dbpedia.org/page/Ununoctio (exactMatch)
  - https://fr.wikipedia.org/wiki/Oganesson (exactMatch)
  - https://en.wikipedia.org/wiki/Oganesson (exactMatch)
  - https://es.wikipedia.org/wiki/Oganesón (exactMatch)
  - https://www.wikidata.org/wiki/Q1307 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-KWXVTS75-K

[]{#nihonium}

####  nihonium
* `nihonium`
* `nihonio`
- **Definition**: Élément de numéro atomique 113 et de symbole Nh. Son
nom provisoire était : ununtrium (symbole : Uut).
- **Definition**: Chemical element with atomic number 113 and symbol
Nh. Its provisional name was : ununtrium (symbol : Uut).
- **Definition**: Elemento químico de número atómico 113 y símbolo Nh.
Su nombre provisional era : ununtrio (símbolo : Uut).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Nh, 
  - élément 113, 
  - Uut, 
  - ununtrium, 
  - Nh, 
  - element 113, 
  - Uut, 
  - ununtrium, 
  - Nh, 
  - elemento 113, 
  - Uut, 
  - ununtrio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - Chemical and physical properties of superheavy elements, B. Fricke. J. McMinn, 1976, Naturwissenschaften vol.63, page 162 - 170, https://doi.org/10.1007/BFb0116498 , 
- **Matches:**
  - http://fr.dbpedia.org/page/Nihonium (exactMatch)
  - http://dbpedia.org/page/Nihonium (exactMatch)
  - http://es.dbpedia.org/page/Ununtrio (exactMatch)
  - https://fr.wikipedia.org/wiki/Nihonium (exactMatch)
  - https://en.wikipedia.org/wiki/Nihonium (exactMatch)
  - https://es.wikipedia.org/wiki/Nihonio (exactMatch)
  - https://www.wikidata.org/wiki/Q1301 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZRNFG3MB-8

[]{#flérovium}

####  flérovium
* `flerovium`
* `flerovio`
- **Definition**: Élément de numéro atomique 114 et de symbole Fl. Son
nom provisoire était : ununquadium (symbole : Uuq).
- **Definition**: Chemical element with atomic number 114 and symbol
Fl. Its provisional name was : ununquadium (symbol : Uuq).
- **Definition**: Elemento químico de número atómico 114 y símbolo Fl.
Su nombre provisional era : ununquadio (símbolo : Uuq).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Fl, 
  - élément 114, 
  - Uuq, 
  - ununquadium, 
  - Fl, 
  - element 114, 
  - Uuq, 
  - ununquadium, 
  - Fl, 
  - elemento 114, 
  - Uuq, 
  - ununquadio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - Chemical and physical properties of superheavy elements, B. Fricke. J. McMinn, 1976, Naturwissenschaften vol.63, page 162 - 170, https://doi.org/10.1007/BFb0116498 , 
- **Matches:**
  - http://fr.dbpedia.org/page/Flérovium (exactMatch)
  - http://dbpedia.org/page/Flerovium (exactMatch)
  - http://es.dbpedia.org/page/Flerovio (exactMatch)
  - https://fr.wikipedia.org/wiki/Flérovium (exactMatch)
  - https://en.wikipedia.org/wiki/Flerovium (exactMatch)
  - https://es.wikipedia.org/wiki/Flerovio (exactMatch)
  - https://www.wikidata.org/wiki/Q1302 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-QBFMJL2M-1

[]{#moscovium}

####  moscovium
* `moscovium`
* `moscovio`
- **Definition**: Élément de numéro atomique 115 et de symbole Mc. Son
nom provisoire était : ununpentium (symbole : Uup).
- **Definition**: Chemical element with atomic number 115 and symbol
Mc. Its provisional name was : ununpentium (symbol : Uup).
- **Definition**: Elemento químico de número atómico 115 y símbolo Mc.
Su nombre provisional era : ununpentio (símbolo : Uup).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Mc, 
  - élément 115, 
  - Uup, 
  - ununpentium, 
  - Mc, 
  - element 115, 
  - Uup, 
  - ununpentium, 
  - Mc, 
  - elemento 115, 
  - Uup, 
  - ununpentio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - Chemical and physical properties of superheavy elements, B. Fricke. J. McMinn, 1976, Naturwissenschaften vol.63, page 162 - 170, https://doi.org/10.1007/BFb0116498 , 
- **Matches:**
  - http://fr.dbpedia.org/page/Ununpentium (exactMatch)
  - http://dbpedia.org/page/Moscovium (exactMatch)
  - http://es.dbpedia.org/page/Ununpentio (exactMatch)
  - https://fr.wikipedia.org/wiki/Moscovium (exactMatch)
  - https://en.wikipedia.org/wiki/Moscovium (exactMatch)
  - https://es.wikipedia.org/wiki/Moscovio (exactMatch)
  - https://www.wikidata.org/wiki/Q1303 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-C7CWB1D9-L

[]{#livermorium}

####  livermorium
* `livermorium`
* `livermorio`
- **Definition**: Élément de numéro atomique 116 et de symbole Lv. Son
nom provisoire était : ununhexium (symbole : Uuh).
- **Definition**: Chemical element with atomic number 116 and symbol
Lv. Its provisional name was : ununhexium (symbol : Uuh).
- **Definition**: Elemento químico de número atómico 116 y símbolo Lv.
Su nombre provisional era : ununhexio (símbolo : Uuh).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Lv, 
  - élément 116, 
  - Uuh, 
  - ununhexium, 
  - Lv, 
  - element 116, 
  - Uuh, 
  - ununhexium, 
  - Lv, 
  - elemento 116, 
  - Uuh, 
  - ununhexio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - , 
- **Matches:**
  - http://fr.dbpedia.org/page/Livermorium (exactMatch)
  - http://dbpedia.org/page/Livermorium (exactMatch)
  - http://es.dbpedia.org/page/Livermorio (exactMatch)
  - https://fr.wikipedia.org/wiki/Livermorium (exactMatch)
  - https://en.wikipedia.org/wiki/Livermorium (exactMatch)
  - https://es.wikipedia.org/wiki/Livermorio (exactMatch)
  - https://www.wikidata.org/wiki/Q1304 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-J01HKKLW-8

[]{#tennesse}

####  tennesse
* `tennessine`
* `téneso`
- **Definition**: Élément de numéro atomique 117 et de symbole Ts. Son
nom provisoire était : ununseptium (symbole : Uus).
- **Definition**: Chemical element with atomic number 117 and symbol
Ts. Its provisional name was : ununseptium (symbol : Uus).
- **Definition**: Elemento químico de número atómico 117 y símbolo Ts.
Su nombre provisional era : ununseptio (símbolo : Uus).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ts, 
  - élément 117, 
  - Uus, 
  - ununseptium, 
  - Ts, 
  - element 117, 
  - Uus, 
  - ununseptium, 
  - Ts, 
  - elemento 117, 
  - Uus, 
  - ununseptio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - , 
  - Chemical and physical properties of superheavy elements, B. Fricke. J. McMinn, 1976, Naturwissenschaften vol.63, page 162 - 170, https://doi.org/10.1007/BFb0116498 , 
- **Matches:**
  - http://fr.dbpedia.org/page/Ununseptium (exactMatch)
  - http://dbpedia.org/page/Tennessine (exactMatch)
  - http://es.dbpedia.org/page/Ununseptio (exactMatch)
  - https://fr.wikipedia.org/wiki/Tennesse (exactMatch)
  - https://en.wikipedia.org/wiki/Tennessine (exactMatch)
  - https://es.wikipedia.org/wiki/Téneso (exactMatch)
  - https://www.wikidata.org/wiki/Q1306 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-T6JMQV2K-7

[]{#scandium}

####  scandium
* `scandium`
* `escandio`
- **Definition**: Élément de numéro atomique 21 et de symbole Sc.
- **Definition**: Chemical element with atomic number 21 and symbol
Sc.
- **Definition**: Elemento químico de número atómico 21 y símbolo Sc.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sc, 
  - Sc, 
  - Sc, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33330 (closeMatch)
  - http://fr.dbpedia.org/page/Scandium (exactMatch)
  - http://dbpedia.org/page/Scandium (exactMatch)
  - http://es.dbpedia.org/page/Escandio (exactMatch)
  - https://fr.wikipedia.org/wiki/Scandium (exactMatch)
  - https://en.wikipedia.org/wiki/Scandium (exactMatch)
  - https://es.wikipedia.org/wiki/Escandio (exactMatch)
  - https://www.wikidata.org/wiki/Q713 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NHX11FWH-N

[]{#titane}

####  titane
* `titanium`
* `titanio`
- **Definition**: Élément de numéro atomique 22 et de symbole Ti.
- **Definition**: Chemical element with atomic number 22 and symbol
Ti.
- **Definition**: Elemento químico de número atómico 22 y símbolo Ti.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ti, 
  - Ti, 
  - Ti, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33341 (closeMatch)
  - http://fr.dbpedia.org/page/Titane (exactMatch)
  - http://dbpedia.org/page/Titanium (exactMatch)
  - http://es.dbpedia.org/page/Titanio (exactMatch)
  - https://fr.wikipedia.org/wiki/Titane (exactMatch)
  - https://en.wikipedia.org/wiki/Titanium (exactMatch)
  - https://es.wikipedia.org/wiki/Titanio (exactMatch)
  - https://www.wikidata.org/wiki/Q716 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-B46N74X6-Z

[]{#vanadium}

####  vanadium
* `vanadium`
* `vanadio`
- **Definition**: Élément de numéro atomique 23 et de symbole V.
- **Definition**: Chemical element with atomic number 23 and symbol V.
- **Definition**: Elemento químico de número atómico 23 y símbolo V.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - V, 
  - V, 
  - V, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27698 (closeMatch)
  - http://fr.dbpedia.org/page/Vanadium (exactMatch)
  - http://dbpedia.org/page/Vanadium (exactMatch)
  - http://es.dbpedia.org/page/Vanadio (exactMatch)
  - https://fr.wikipedia.org/wiki/Vanadium (exactMatch)
  - https://en.wikipedia.org/wiki/Vanadium (exactMatch)
  - https://es.wikipedia.org/wiki/Vanadio (exactMatch)
  - https://www.wikidata.org/wiki/Q722 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-XZ20HJNX-W

[]{#chrome}

####  chrome
* `chromium`
* `cromo`
- **Definition**: Élément de numéro atomique 24 et de symbole Cr.
- **Definition**: Chemical element with atomic number 24 and symbol
Cr.
- **Definition**: Elemento químico de número atómico 24 y símbolo Cr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cr, 
  - Cr, 
  - Cr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28073 (closeMatch)
  - http://fr.dbpedia.org/page/Chrome (exactMatch)
  - http://dbpedia.org/page/Chromium (exactMatch)
  - http://es.dbpedia.org/page/Cromo (exactMatch)
  - https://fr.wikipedia.org/wiki/Chrome (exactMatch)
  - https://en.wikipedia.org/wiki/Chromium (exactMatch)
  - https://es.wikipedia.org/wiki/Cromo (exactMatch)
  - https://www.wikidata.org/wiki/Q725 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-W2MFT88M-C

[]{#manganèse}

####  manganèse
* `manganese`
* `manganeso`
- **Definition**: Élément de numéro atomique 25 et de symbole Mn.
- **Definition**: Chemical element with atomic number 25 and symbol
Mn.
- **Definition**: Elemento químico de número atómico 25 y símbolo Mn.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Mn, 
  - Mn, 
  - Mn, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_18291 (closeMatch)
  - http://fr.dbpedia.org/page/Manganèse (exactMatch)
  - http://dbpedia.org/page/Manganese (exactMatch)
  - http://es.dbpedia.org/page/Manganeso (exactMatch)
  - https://fr.wikipedia.org/wiki/Manganèse (exactMatch)
  - https://en.wikipedia.org/wiki/Manganese (exactMatch)
  - https://es.wikipedia.org/wiki/Manganeso (exactMatch)
  - https://www.wikidata.org/wiki/Q731 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZHXJ4D8T-H

[]{#fer}

####  fer
* `iron`
* `hierro`
- **Definition**: Élément de numéro atomique 26 et de symbole Fe.
- **Definition**: Chemical element with atomic number 26 and symbol
Fe.
- **Definition**: Elemento químico de número atómico 26 y símbolo Fe.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Fe, 
  - Fe, 
  - Fe, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_18248 (closeMatch)
  - http://fr.dbpedia.org/page/Fer (exactMatch)
  - http://dbpedia.org/page/Iron (exactMatch)
  - http://es.dbpedia.org/page/Hierro (exactMatch)
  - https://fr.wikipedia.org/wiki/Fer (exactMatch)
  - https://en.wikipedia.org/wiki/Iron (exactMatch)
  - https://es.wikipedia.org/wiki/Hierro (exactMatch)
  - https://www.wikidata.org/wiki/Q677 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NQ0K580N-5

[]{#cobalt}

####  cobalt
* `cobalt`
* `cobalto`
- **Definition**: Élément de numéro atomique 27 et de symbole Co.
- **Definition**: Chemical element with atomic number 27 and symbol
Co.
- **Definition**: Elemento químico de número atómico 27 y símbolo Co.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Co, 
  - Co, 
  - Co, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27638 (closeMatch)
  - http://fr.dbpedia.org/page/Cobalt (exactMatch)
  - http://dbpedia.org/page/Cobalt (exactMatch)
  - http://es.dbpedia.org/page/Cobalto (exactMatch)
  - https://fr.wikipedia.org/wiki/Cobalt (exactMatch)
  - https://en.wikipedia.org/wiki/Cobalt (exactMatch)
  - https://es.wikipedia.org/wiki/Cobalto (exactMatch)
  - https://www.wikidata.org/wiki/Q740 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BVR52VXN-F

[]{#nickel}

####  nickel
* `nickel`
* `niquel`
- **Definition**: Élément de numéro atomique 28 et de symbole Ni.
- **Definition**: Chemical element with atomic number 28 and symbol
Ni.
- **Definition**: Elemento químico de número atómico 28 y símbolo Ni.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ni, 
  - Ni, 
  - Ni, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28112 (closeMatch)
  - http://fr.dbpedia.org/page/Nickel (exactMatch)
  - http://dbpedia.org/page/Nickel (exactMatch)
  - http://es.dbpedia.org/page/Niquel (exactMatch)
  - https://fr.wikipedia.org/wiki/Nickel (exactMatch)
  - https://en.wikipedia.org/wiki/Nickel (exactMatch)
  - https://es.wikipedia.org/wiki/Niquel (exactMatch)
  - https://www.wikidata.org/wiki/Q744 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FDQVX1R1-D

[]{#cuivre}

####  cuivre
* `copper`
* `cobre`
- **Definition**: Élément de numéro atomique 29 et de symbole Cu.
- **Definition**: Chemical element with atomic number 29 and symbol
Cu.
- **Definition**: Elemento químico de número atómico 29 y símbolo Cu.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cu, 
  - Cu, 
  - Cu, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28694 (closeMatch)
  - http://fr.dbpedia.org/page/Cuivre (exactMatch)
  - http://dbpedia.org/page/Copper (exactMatch)
  - http://es.dbpedia.org/page/Cobre (exactMatch)
  - https://fr.wikipedia.org/wiki/Cuivre (exactMatch)
  - https://en.wikipedia.org/wiki/Copper (exactMatch)
  - https://es.wikipedia.org/wiki/Cobre (exactMatch)
  - https://www.wikidata.org/wiki/Q753 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-G3VCNX8B-6

[]{#zinc}

####  zinc
* `zinc`
* `zinc`
- **Definition**: Élément de numéro atomique 30 et de symbole Zn.
- **Definition**: Chemical element with atomic number 30 and symbol
Zn.
- **Definition**: Elemento químico de número atómico 30 y símbolo Zn.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Zn, 
  - Zn, 
  - Zn, 
  - cinc, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27363 (closeMatch)
  - http://fr.dbpedia.org/page/Zinc (exactMatch)
  - http://dbpedia.org/page/Zinc (exactMatch)
  - http://es.dbpedia.org/page/Zinc (exactMatch)
  - https://fr.wikipedia.org/wiki/Zinc (exactMatch)
  - https://en.wikipedia.org/wiki/Zinc (exactMatch)
  - https://es.wikipedia.org/wiki/Zinc (exactMatch)
  - https://www.wikidata.org/wiki/Q758 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZH5RPRR9-D

[]{#yttrium}

####  yttrium
* `yttrium`
* `ytrio`
- **Definition**: Élément de numéro atomique 39 et de symbole Y.
- **Definition**: Chemical element with atomic number 39 and symbol Y.
- **Definition**: Elemento químico de número atómico 39 y símbolo Y.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Y, 
  - Y, 
  - Y, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33331 (closeMatch)
  - http://fr.dbpedia.org/page/Yttrium (exactMatch)
  - http://dbpedia.org/page/Yttrium (exactMatch)
  - http://es.dbpedia.org/page/Ytrio (exactMatch)
  - https://fr.wikipedia.org/wiki/Yttrium (exactMatch)
  - https://en.wikipedia.org/wiki/Yttrium (exactMatch)
  - https://es.wikipedia.org/wiki/Ytrio (exactMatch)
  - https://www.wikidata.org/wiki/Q941 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CJJ7GLMV-8

[]{#zirconium}

####  zirconium
* `zirconium`
* `zirconio`
- **Definition**: Élément de numéro atomique 40 et de symbole Zr.
- **Definition**: Chemical element with atomic number 40 and symbol
Zr.
- **Definition**: Elemento químico de número atómico 40 y símbolo Zr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Zr, 
  - Zr, 
  - Zr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33342 (closeMatch)
  - http://fr.dbpedia.org/page/Zirconium (exactMatch)
  - http://dbpedia.org/page/Zirconium (exactMatch)
  - http://es.dbpedia.org/page/Zirconio (exactMatch)
  - https://fr.wikipedia.org/wiki/Zirconium (exactMatch)
  - https://en.wikipedia.org/wiki/Zirconium (exactMatch)
  - https://es.wikipedia.org/wiki/Zirconio (exactMatch)
  - https://www.wikidata.org/wiki/Q1038 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NCV4MKFK-N

[]{#niobium}

####  niobium
* `niobium`
* `niobio`
- **Definition**: Élément de numéro atomique 41 et de symbole Nb.
- **Definition**: Chemical element with atomic number 41 and symbol
Nb.
- **Definition**: Elemento químico de número atómico 41 y símbolo Nb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Nb, 
  - Nb, 
  - Nb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33344 (closeMatch)
  - http://fr.dbpedia.org/page/Niobium (exactMatch)
  - http://dbpedia.org/page/Niobium (exactMatch)
  - http://es.dbpedia.org/page/Niobio (exactMatch)
  - https://fr.wikipedia.org/wiki/Niobium (exactMatch)
  - https://en.wikipedia.org/wiki/Niobium (exactMatch)
  - https://es.wikipedia.org/wiki/Niobio (exactMatch)
  - https://www.wikidata.org/wiki/Q1046 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-M9473W1P-9

[]{#molybdène}

####  molybdène
* `molybdenum`
* `molibdeno`
- **Definition**: Élément de numéro atomique 42 et de symbole Mo.
- **Definition**: Chemical element with atomic number 42 and symbol
Mo.
- **Definition**: Elemento químico de número atómico 42 y símbolo Mo.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Mo, 
  - Mo, 
  - Mo, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_28685 (closeMatch)
  - http://fr.dbpedia.org/page/Molybdène (exactMatch)
  - http://dbpedia.org/page/Molybdenum (exactMatch)
  - http://es.dbpedia.org/page/Molibdeno (exactMatch)
  - https://fr.wikipedia.org/wiki/Molybdène (exactMatch)
  - https://en.wikipedia.org/wiki/Molybdenum (exactMatch)
  - https://es.wikipedia.org/wiki/Molibdeno (exactMatch)
  - https://www.wikidata.org/wiki/Q1053 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-KZJDHQWD-3

[]{#technétium}

####  technétium
* `technetium`
* `tecnecio`
- **Definition**: Élément de numéro atomique 43 et de symbole Tc.
- **Definition**: Chemical element with atomic number 43 and symbol
Tc.
- **Definition**: Elemento químico de número atómico 43 y símbolo Tc.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Tc, 
  - Tc, 
  - Tc, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33353 (closeMatch)
  - http://fr.dbpedia.org/page/Technétium (exactMatch)
  - http://dbpedia.org/page/Technetium (exactMatch)
  - http://es.dbpedia.org/page/Tecnecio (exactMatch)
  - https://fr.wikipedia.org/wiki/Technétium (exactMatch)
  - https://en.wikipedia.org/wiki/Technetium (exactMatch)
  - https://es.wikipedia.org/wiki/Tecnecio (exactMatch)
  - https://www.wikidata.org/wiki/Q1054 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-KS62JGFZ-8

[]{#argent}

####  argent
* `silver`
* `plata`
- **Definition**: Élément de numéro atomique 47 et de symbole Ag.
- **Definition**: Chemical element with atomic number 47 and symbol
Ag.
- **Definition**: Elemento químico de número atómico 47 y símbolo Ag.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ag, 
  - Ag, 
  - Ag, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30512 (closeMatch)
  - http://fr.dbpedia.org/page/Argent (exactMatch)
  - http://dbpedia.org/page/Silver (exactMatch)
  - http://es.dbpedia.org/page/Plata (exactMatch)
  - https://fr.wikipedia.org/wiki/Argent (exactMatch)
  - https://en.wikipedia.org/wiki/Silver (exactMatch)
  - https://es.wikipedia.org/wiki/Plata (exactMatch)
  - https://www.wikidata.org/wiki/Q1090 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-MBPSKJ5K-B

[]{#cadmium}

####  cadmium
* `cadmium`
* `cadmio`
- **Definition**: Élément de numéro atomique 48 et de symbole Cd.
- **Definition**: Chemical element with atomic number 48 and symbol
Cd.
- **Definition**: Elemento químico de número atómico 48 y símbolo Cd.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cd, 
  - Cd, 
  - Cd, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_22977 (closeMatch)
  - http://fr.dbpedia.org/page/Cadmium (exactMatch)
  - http://dbpedia.org/page/Cadmium (exactMatch)
  - http://es.dbpedia.org/page/Cadmio (exactMatch)
  - https://fr.wikipedia.org/wiki/Cadmium (exactMatch)
  - https://en.wikipedia.org/wiki/Cadmium (exactMatch)
  - https://es.wikipedia.org/wiki/Cadmio (exactMatch)
  - https://www.wikidata.org/wiki/Q1091 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-R5TL4FBV-J

[]{#hafnium}

####  hafnium
* `hafnium`
* `hafnio`
- **Definition**: Élément de numéro atomique 72 et de symbole Hf.
- **Definition**: Chemical element with atomic number 72 and symbol
Hf.
- **Definition**: Elemento químico de número atómico 72 y símbolo Hf.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Hf, 
  - Hf, 
  - Hf, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33343 (closeMatch)
  - http://fr.dbpedia.org/page/Hafnium (exactMatch)
  - http://dbpedia.org/page/Hafnium (exactMatch)
  - http://es.dbpedia.org/page/Hafnio (exactMatch)
  - https://fr.wikipedia.org/wiki/Hafnium (exactMatch)
  - https://en.wikipedia.org/wiki/Hafnium (exactMatch)
  - https://es.wikipedia.org/wiki/Hafnio (exactMatch)
  - https://www.wikidata.org/wiki/Q1119 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-RFB6RBQG-4

[]{#tantale}

####  tantale
* `tantalum`
* `tantalio`
- **Definition**: Élément de numéro atomique 73 et de symbole Ta.
- **Definition**: Chemical element with atomic number 73 and symbol
Ta.
- **Definition**: Elemento químico de número atómico 73 y símbolo Ta.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ta, 
  - Ta, 
  - Ta, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33348 (closeMatch)
  - http://fr.dbpedia.org/page/Tantale (exactMatch)
  - http://dbpedia.org/page/Tantalum (exactMatch)
  - http://es.dbpedia.org/page/Tantalio (exactMatch)
  - https://fr.wikipedia.org/wiki/Tantale_(chimie) (exactMatch)
  - https://en.wikipedia.org/wiki/Tantalum (exactMatch)
  - https://es.wikipedia.org/wiki/Tantalio (exactMatch)
  - https://www.wikidata.org/wiki/Q1123 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-L44RTF4W-7

[]{#tungstène}

####  tungstène
* `tungsten`
* `wolframio`
- **Definition**: Élément de numéro atomique 74 et de symbole W.
- **Definition**: Chemical element with atomic number 74 and symbol W.
- **Definition**: Elemento químico de número atómico 74 y símbolo W.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - W, 
  - W, 
  - W, 
  - volframio, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27998 (closeMatch)
  - http://fr.dbpedia.org/page/Tungstène (exactMatch)
  - http://dbpedia.org/page/Tungsten (exactMatch)
  - http://es.dbpedia.org/page/Wolframio (exactMatch)
  - https://fr.wikipedia.org/wiki/Tungstène (exactMatch)
  - https://en.wikipedia.org/wiki/Tungsten (exactMatch)
  - https://es.wikipedia.org/wiki/Wolframio (exactMatch)
  - https://www.wikidata.org/wiki/Q743 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-B030NV4K-M

[]{#rhénium}

####  rhénium
* `rhenium`
* `renio`
- **Definition**: Élément de numéro atomique 75 et de symbole Re.
- **Definition**: Chemical element with atomic number 75 and symbol
Re.
- **Definition**: Elemento químico de número atómico 75 y símbolo Re.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Re, 
  - Re, 
  - Re, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33354 (closeMatch)
  - http://fr.dbpedia.org/page/Rhénium (exactMatch)
  - http://dbpedia.org/page/Rhenium (exactMatch)
  - http://es.dbpedia.org/page/Renio (exactMatch)
  - https://fr.wikipedia.org/wiki/Rhénium (exactMatch)
  - https://en.wikipedia.org/wiki/Rhenium (exactMatch)
  - https://es.wikipedia.org/wiki/Renio (exactMatch)
  - https://www.wikidata.org/wiki/Q737 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-X7V8KNMP-X

[]{#or}

####  or
* `gold`
* `oro`
- **Definition**: Élément de numéro atomique 79 et de symbole Au.
- **Definition**: Chemical element with atomic number 79 and symbol
Au.
- **Definition**: Elemento químico de número atómico 79 y símbolo Au.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Au, 
  - Au, 
  - Au, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_29287 (closeMatch)
  - http://fr.dbpedia.org/page/Or (exactMatch)
  - http://dbpedia.org/page/Gold (exactMatch)
  - http://es.dbpedia.org/page/Oro (exactMatch)
  - https://fr.wikipedia.org/wiki/Or (exactMatch)
  - https://en.wikipedia.org/wiki/Gold (exactMatch)
  - https://es.wikipedia.org/wiki/Oro (exactMatch)
  - https://www.wikidata.org/wiki/Q897 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-HD8QM9KB-M

[]{#mercure}

####  mercure
* `mercury`
* `mercurio`
- **Definition**: Élément de numéro atomique 80 et de symbole Hg.
- **Definition**: Chemical element with atomic number 80 and symbol
Hg.
- **Definition**: Elemento químico de número atómico 80 y símbolo Hg.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Hg, 
  - Hg, 
  - Hg, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_25195 (closeMatch)
  - http://fr.dbpedia.org/page/Mercure_(chimie) (exactMatch)
  - http://dbpedia.org/page/Mercury_(element) (exactMatch)
  - http://es.dbpedia.org/page/Mercurio_(elemento) (exactMatch)
  - https://fr.wikipedia.org/wiki/Mercure_(chimie) (exactMatch)
  - https://en.wikipedia.org/wiki/Mercury_(element) (exactMatch)
  - https://es.wikipedia.org/wiki/Mercurio_(elemento) (exactMatch)
  - https://www.wikidata.org/wiki/Q925 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-H9J0KWB5-L

[]{#rutherfordium}

####  rutherfordium
* `rutherfordium`
* `rutherfordio`
- **Definition**: Élément de numéro atomique 104 et de symbole Rf. Son
nom provisoire était : unnilquadium (symbole : Unq).
- **Definition**: Chemical element with atomic number 104 and symbol
Rf. Its provisional name was : unnilquadium (symbol : Unq).
- **Definition**: Elemento químico de número atómico 104 y símbolo Rf.
Su nombre provisional era : unnilquadio (símbolo : Unq).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Rf, 
  - élément 104, 
  - Unq, 
  - unnilquadium, 
  - Rf, 
  - element 104, 
  - Unq, 
  - unnilquadium, 
  - Rf, 
  - elemento 104, 
  - Unq, 
  - unnilquadio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - The Chemistry of the actinide and transactinide elements, fourth edition, Volumes 1–6, 2010, chapitre 14, p. 1652-1752, Transactinide Elements and Future Elements,Darleane C. Hoffman, Diana M. Lee, and Valeria Pershina, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33346 (closeMatch)
  - http://fr.dbpedia.org/page/Rutherfordium (exactMatch)
  - http://dbpedia.org/page/Rutherfordium (exactMatch)
  - http://es.dbpedia.org/page/Rutherfordio (exactMatch)
  - https://fr.wikipedia.org/wiki/Rutherfordium (exactMatch)
  - https://en.wikipedia.org/wiki/Rutherfordium (exactMatch)
  - https://es.wikipedia.org/wiki/Rutherfordio (exactMatch)
  - https://www.wikidata.org/wiki/Q1226 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-K0ZD3V17-V

[]{#dubnium}

####  dubnium
* `dubnium`
* `dubnio`
- **Definition**: Élément de numéro atomique 105 et de symbole Db. Son
nom provisoire était : unnilpentium (symbole : Unp).
- **Definition**: Chemical element with atomic number 105 and symbol
Db. Its provisional name was : unnilpentium (symbol : Unp).
- **Definition**: Elemento químico de número atómico 105 y símbolo Db.
Su nombre provisional era : unnilpentio (símbolo : Unp).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Db, 
  - élément 105, 
  - Unp, 
  - unnilpentium, 
  - Db, 
  - element 105, 
  - Unp, 
  - unnilpentium, 
  - Db, 
  - elemento 105, 
  - Unp, 
  - unnilpentio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33349 (closeMatch)
  - http://fr.dbpedia.org/page/Dubnium (exactMatch)
  - http://dbpedia.org/page/Dubnium (exactMatch)
  - http://es.dbpedia.org/page/Dubnio (exactMatch)
  - https://fr.wikipedia.org/wiki/Dubnium (exactMatch)
  - https://en.wikipedia.org/wiki/Dubnium (exactMatch)
  - https://es.wikipedia.org/wiki/Dubnio (exactMatch)
  - https://www.wikidata.org/wiki/Q1232 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CBJQP8XN-J

[]{#seaborgium}

####  seaborgium
* `seaborgium`
* `seaborgio`
- **Definition**: Élément de numéro atomique 106 et de symbole Sg. Son
nom provisoire était : unnilhexium (symbole : Unh).
- **Definition**: Chemical element with atomic number 106 and symbol
Sg. Its provisional name was : unnilhexium (symbol : Unh).
- **Definition**: Elemento químico de número atómico 106 y símbolo Sg.
Su nombre provisional era : unnilhexio (símbolo : Unh).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sg, 
  - élément 106, 
  - Unh, 
  - unnilhexium, 
  - Sg, 
  - element 106, 
  - Unh, 
  - unnilhexium, 
  - Sg, 
  - elemento 106, 
  - Unh, 
  - unnilhexio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33351 (closeMatch)
  - http://fr.dbpedia.org/page/Seaborgium (exactMatch)
  - http://dbpedia.org/page/Seaborgium (exactMatch)
  - http://es.dbpedia.org/page/Seaborgio (exactMatch)
  - https://fr.wikipedia.org/wiki/Seaborgium (exactMatch)
  - https://en.wikipedia.org/wiki/Seaborgium (exactMatch)
  - https://es.wikipedia.org/wiki/Seaborgio (exactMatch)
  - https://www.wikidata.org/wiki/Q1234 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FWTB5L0N-T

[]{#bohrium}

####  bohrium
* `bohrium`
* `bohrio`
- **Definition**: Élément de numéro atomique 107 et de symbole Bh. Son
nom provisoire était : unnilseptium (symbole : Uns).
- **Definition**: Chemical element with atomic number 107 and symbol
Bh. Its provisional name was : unnilseptium (symbol : Uns).
- **Definition**: Elemento químico de número atómico 107 y símbolo Bh.
Su nombre provisional era : unnilseptio (símbolo : Uns).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Bh, 
  - élément 107, 
  - Uns, 
  - unnilseptium, 
  - Bh, 
  - element 107, 
  - Uns, 
  - unnilseptium, 
  - Bh, 
  - elemento 107, 
  - Uns, 
  - unnilseptio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33355 (closeMatch)
  - http://fr.dbpedia.org/page/Bohrium (exactMatch)
  - http://dbpedia.org/page/Bohrium (exactMatch)
  - http://es.dbpedia.org/page/Bohrio (exactMatch)
  - https://fr.wikipedia.org/wiki/Bohrium (exactMatch)
  - https://en.wikipedia.org/wiki/Bohrium (exactMatch)
  - https://es.wikipedia.org/wiki/Bohrio (exactMatch)
  - https://www.wikidata.org/wiki/Q1249 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZXTR1209-C

[]{#hassium}

####  hassium
* `hassium`
* `hassio`
- **Definition**: Élément de numéro atomique 108 et de symbole Hs. Son
nom provisoire était : unniloctium (symbole : Uno).
- **Definition**: Chemical element with atomic number 108 and symbol
Hs. Its provisional name was : unniloctium (symbol : Uno).
- **Definition**: Elemento químico de número atómico 108 y símbolo Hs.
Su nombre provisional era : unniloctio (símbolo : Uno).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Hs, 
  - élément 108, 
  - Uno, 
  - unniloctium, 
  - Hs, 
  - element 108, 
  - Uno, 
  - unniloctium, 
  - Hs, 
  - elemento 108, 
  - Uno, 
  - unniloctio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33357 (closeMatch)
  - http://fr.dbpedia.org/page/Hassium (exactMatch)
  - http://dbpedia.org/page/Hassium (exactMatch)
  - http://es.dbpedia.org/page/Hassio (exactMatch)
  - https://fr.wikipedia.org/wiki/Hassium (exactMatch)
  - https://en.wikipedia.org/wiki/Hassium (exactMatch)
  - https://es.wikipedia.org/wiki/Hassio (exactMatch)
  - https://www.wikidata.org/wiki/Q1252 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-JPS5NPG3-L

[]{#ruthénium}

####  ruthénium
* `ruthenium`
* `rutenio`
- **Definition**: Élément de numéro atomique 44 et de symbole Ru.
- **Definition**: Chemical element with atomic number 44 and symbol
Ru.
- **Definition**: Elemento químico de número atómico 44 y símbolo Ru.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ru, 
  - Ru, 
  - Ru, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30682 (closeMatch)
  - http://fr.dbpedia.org/page/Ruthénium (exactMatch)
  - http://dbpedia.org/page/Ruthenium (exactMatch)
  - http://es.dbpedia.org/page/Rutenio (exactMatch)
  - https://fr.wikipedia.org/wiki/Ruthénium (exactMatch)
  - https://en.wikipedia.org/wiki/Ruthenium (exactMatch)
  - https://es.wikipedia.org/wiki/Rutenio (exactMatch)
  - https://www.wikidata.org/wiki/Q1086 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-R6LMKQKX-5

[]{#rhodium}

####  rhodium
* `rhodium`
* `rodio`
- **Definition**: Élément de numéro atomique 45 et de symbole Rh.
- **Definition**: Chemical element with atomic number 45 and symbol
Rh.
- **Definition**: Elemento químico de número atómico 45 y símbolo Rh.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Rh, 
  - Rh, 
  - Rh, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33359 (closeMatch)
  - http://fr.dbpedia.org/page/Rhodium (exactMatch)
  - http://dbpedia.org/page/Rhodium (exactMatch)
  - http://es.dbpedia.org/page/Rodio (exactMatch)
  - https://fr.wikipedia.org/wiki/Rhodium (exactMatch)
  - https://en.wikipedia.org/wiki/Rhodium (exactMatch)
  - https://es.wikipedia.org/wiki/Rodio (exactMatch)
  - https://www.wikidata.org/wiki/Q1087 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FKKNQWB0-B

[]{#palladium}

####  palladium
* `palladium`
* `paladio`
- **Definition**: Élément de numéro atomique 46 et de symbole Pd.
- **Definition**: Chemical element with atomic number 46 and symbol
Pd.
- **Definition**: Elemento químico de número atómico 46 y símbolo Pd.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pd, 
  - Pd, 
  - Pd, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33363 (closeMatch)
  - http://fr.dbpedia.org/page/Palladium (exactMatch)
  - http://dbpedia.org/page/Palladium (exactMatch)
  - http://es.dbpedia.org/page/Paladio (exactMatch)
  - https://fr.wikipedia.org/wiki/Palladium (exactMatch)
  - https://en.wikipedia.org/wiki/Palladium (exactMatch)
  - https://es.wikipedia.org/wiki/Paladio (exactMatch)
  - https://www.wikidata.org/wiki/Q1089 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GKH9PL2W-2

[]{#osmium}

####  osmium
* `osmium`
* `osmio`
- **Definition**: Élément de numéro atomique 76 et de symbole Os.
- **Definition**: Chemical element with atomic number 76 and symbol
Os.
- **Definition**: Elemento químico de número atómico 76 y símbolo Os.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Os, 
  - Os, 
  - Os, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_30687 (closeMatch)
  - http://fr.dbpedia.org/page/Osmium (exactMatch)
  - http://dbpedia.org/page/Osmium (exactMatch)
  - http://es.dbpedia.org/page/Osmio (exactMatch)
  - https://fr.wikipedia.org/wiki/Osmium (exactMatch)
  - https://en.wikipedia.org/wiki/Osmium (exactMatch)
  - https://es.wikipedia.org/wiki/Osmio (exactMatch)
  - https://www.wikidata.org/wiki/Q751 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-V9RXLN1J-0

[]{#iridium}

####  iridium
* `iridium`
* `iridio`
- **Definition**: Élément de numéro atomique 77 et de symbole Ir.
- **Definition**: Chemical element with atomic number 77 and symbol
Ir.
- **Definition**: Elemento químico de número atómico 77 y símbolo Ir.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ir, 
  - Ir, 
  - Ir, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33360 (closeMatch)
  - http://fr.dbpedia.org/page/Iridium (exactMatch)
  - http://dbpedia.org/page/Iridium (exactMatch)
  - http://es.dbpedia.org/page/Iridio (exactMatch)
  - https://fr.wikipedia.org/wiki/Iridium (exactMatch)
  - https://en.wikipedia.org/wiki/Iridium (exactMatch)
  - https://es.wikipedia.org/wiki/Iridio (exactMatch)
  - https://www.wikidata.org/wiki/Q877 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-WK9PDRSF-D

[]{#platine}

####  platine
* `platinum`
* `platino`
- **Definition**: Élément de numéro atomique 78 et de symbole Pt.
- **Definition**: Chemical element with atomic number 78 and symbol
Pt.
- **Definition**: Elemento químico de número atómico 78 y símbolo Pt.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pt, 
  - Pt, 
  - Pt, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33364 (closeMatch)
  - http://fr.dbpedia.org/page/Platine (exactMatch)
  - http://dbpedia.org/page/Platinum (exactMatch)
  - http://es.dbpedia.org/page/Platino (exactMatch)
  - https://fr.wikipedia.org/wiki/Platine (exactMatch)
  - https://en.wikipedia.org/wiki/Platinum (exactMatch)
  - https://es.wikipedia.org/wiki/Platino (exactMatch)
  - https://www.wikidata.org/wiki/Q880 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-HCSZZCGN-4

[]{#meitnérium}

####  meitnérium
* `meitnerium`
* `meitnerio`
- **Definition**: Élément de numéro atomique 109 et de symbole Mt. Son
nom provisoire était : unnilennium (symbole : Une).
- **Definition**: Chemical element with atomic number 109 and symbol
Mt. Its provisional name was : unnilennium (symbol : Une).
- **Definition**: Elemento químico de número atómico 109 y símbolo Mt.
Su nombre provisional era : unnilennio (símbolo : Une).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Mt, 
  - meitnerium, 
  - élément 109, 
  - Une, 
  - unnilennium, 
  - Mt, 
  - element 109, 
  - Une, 
  - unnilennium, 
  - Mt, 
  - elemento 109, 
  - Une, 
  - unnilennio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33361 (closeMatch)
  - http://fr.dbpedia.org/page/Meitnerium (exactMatch)
  - http://dbpedia.org/page/Meitnerium (exactMatch)
  - http://es.dbpedia.org/page/Meitnerio (exactMatch)
  - https://fr.wikipedia.org/wiki/Meitnerium (exactMatch)
  - https://en.wikipedia.org/wiki/Meitnerium (exactMatch)
  - https://es.wikipedia.org/wiki/Meitnerio (exactMatch)
  - https://www.wikidata.org/wiki/Q1258 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CSZNWMQ3-R

[]{#darmstadtium}

####  darmstadtium
* `darmstadtium`
* `darmstadio`
- **Definition**: Élément de numéro atomique 110 et de symbole Ds. Son
nom provisoire était : ununnilium (symbole : Uun).
- **Definition**: Chemical element with atomic number 110 and symbol
Ds. Its provisional name was : ununnilium (symbol : Uun).
- **Definition**: Elemento químico de número atómico 110 y símbolo Ds.
Su nombre provisional era : ununnilio (símbolo : Uun).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ds, 
  - élément 110, 
  - Uun, 
  - ununnilium, 
  - Ds, 
  - element 110, 
  - Uun, 
  - ununnilium, 
  - Ds, 
  - elemento 110, 
  - Uun, 
  - ununnilio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33367 (closeMatch)
  - http://fr.dbpedia.org/page/Darmstadium (exactMatch)
  - http://dbpedia.org/page/Darmstadium (exactMatch)
  - http://es.dbpedia.org/page/Darmstadio (exactMatch)
  - https://fr.wikipedia.org/wiki/Darmstadtium (exactMatch)
  - https://en.wikipedia.org/wiki/Darmstadtium (exactMatch)
  - https://es.wikipedia.org/wiki/Darmstadio (exactMatch)
  - https://www.wikidata.org/wiki/Q1266 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-J7MRT66Z-G

[]{#roentgenium}

####  roentgenium
* `roentgenium`
* `roentgenio`
- **Definition**: Élément de numéro atomique 111 et de symbole Rg. Son
nom provisoire était : unununium (symbole : Uuu).
- **Definition**: Chemical element with atomic number 111 and symbol
Rg. Its provisional name was : unununium (symbol : Uuu).
- **Definition**: Elemento químico de número atómico 111 y símbolo Rg.
Su nombre provisional era : unununio (símbolo : Uuu).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Rg, 
  - élément 111, 
  - Uuu, 
  - roentgénium, 
  - röntgenium, 
  - rœntgénium, 
  - unununium, 
  - Rg, 
  - element 111, 
  - Uuu, 
  - unununium, 
  - Rg, 
  - elemento 111, 
  - Uuu, 
  - unununio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33368 (closeMatch)
  - http://fr.dbpedia.org/page/Roentgenium (exactMatch)
  - http://dbpedia.org/page/Roentgenium (exactMatch)
  - http://es.dbpedia.org/page/Roentgenio (exactMatch)
  - https://fr.wikipedia.org/wiki/Roentgenium (exactMatch)
  - https://en.wikipedia.org/wiki/Roentgenium (exactMatch)
  - https://es.wikipedia.org/wiki/Roentgenio (exactMatch)
  - https://www.wikidata.org/wiki/Q1272 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NMPSS1D3-1

[]{#copernicium}

####  copernicium
* `copernicium`
* `copernicio`
- **Definition**: Élément de numéro atomique 112 et de symbole Cn. Son
nom provisoire était : ununbium (symbole : Uub).
- **Definition**: Chemical element with atomic number 112 and symbol
Cn. Its provisional name was : ununbium (symbol : Uub).
- **Definition**: Elemento químico de número atómico 112 y símbolo Cn.
Su nombre provisional era : ununbio (símbolo : Uub).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cn, 
  - élément 112, 
  - Uub, 
  - ununbium, 
  - Cn, 
  - element 112, 
  - Uub, 
  - ununbium, 
  - Cn, 
  - elemento 112, 
  - Uub, 
  - ununbio, 
- **Source:**
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33517 (closeMatch)
  - http://fr.dbpedia.org/page/Copernicium (exactMatch)
  - http://dbpedia.org/page/Copernicium (exactMatch)
  - http://es.dbpedia.org/page/Copernicio (exactMatch)
  - https://fr.wikipedia.org/wiki/Copernicium (exactMatch)
  - https://en.wikipedia.org/wiki/Copernicium (exactMatch)
  - https://es.wikipedia.org/wiki/Copernicio (exactMatch)
  - https://www.wikidata.org/wiki/Q1278 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-R2FD9FPX-8

[]{#lanthane}

####  lanthane
* `lanthanum`
* `lantano`
- **Definition**: Élément de numéro atomique 57 et de symbole La.
- **Definition**: Chemical element with atomic number 57 and symbol
La.
- **Definition**: Elemento químico de número atómico 57 y símbolo La.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - La, 
  - La, 
  - La, 
- **Source:**
  - The group 3 dilemma by Philip Ball, 21 April 2017, https://www.chemistryworld.com/opinion/the-group-3-dilemma/3007080.article, 
  - www.iupac.org/project/2015-039-2-200, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33336 (closeMatch)
  - http://fr.dbpedia.org/page/Lanthane (exactMatch)
  - http://dbpedia.org/page/Lanthanum (exactMatch)
  - http://es.dbpedia.org/page/Lantano (exactMatch)
  - https://fr.wikipedia.org/wiki/Lanthane (exactMatch)
  - https://en.wikipedia.org/wiki/Lanthanum (exactMatch)
  - https://es.wikipedia.org/wiki/Lantano (exactMatch)
  - https://www.wikidata.org/wiki/Q1801 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GLQBRH9P-Q

[]{#cérium}

####  cérium
* `cerium`
* `cerio`
- **Definition**: Élément de numéro atomique 58 et de symbole Ce.
- **Definition**: Chemical element with atomic number 58 and symbol
Ce.
- **Definition**: Elemento químico de número atómico 58 y símbolo Ce.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ce, 
  - Ce, 
  - Ce, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33369 (closeMatch)
  - http://fr.dbpedia.org/page/Cérium (exactMatch)
  - http://dbpedia.org/page/Cerium (exactMatch)
  - http://es.dbpedia.org/page/Cerio (exactMatch)
  - https://fr.wikipedia.org/wiki/Cérium (exactMatch)
  - https://en.wikipedia.org/wiki/Cerium (exactMatch)
  - https://es.wikipedia.org/wiki/Cerio (exactMatch)
  - https://www.wikidata.org/wiki/Q1385 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-Z426CQXF-G

[]{#praséodyme}

####  praséodyme
* `praseodymium`
* `praseodimio`
- **Definition**: Élément de numéro atomique 59 et de symbole Pr.
- **Definition**: Chemical element with atomic number 59 and symbol
Pr.
- **Definition**: Elemento químico de número atómico 59 y símbolo Pr.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pr, 
  - Pr, 
  - Pr, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33370 (closeMatch)
  - http://fr.dbpedia.org/page/Praséodyme (exactMatch)
  - http://dbpedia.org/page/Praseodymium (exactMatch)
  - http://es.dbpedia.org/page/Praseodimio (exactMatch)
  - https://fr.wikipedia.org/wiki/Praséodyme (exactMatch)
  - https://en.wikipedia.org/wiki/Praseodymium (exactMatch)
  - https://es.wikipedia.org/wiki/Praseodimio (exactMatch)
  - https://www.wikidata.org/wiki/Q1386 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FNF2KRP1-X

[]{#néodyme}

####  néodyme
* `neodymium`
* `neodimio`
- **Definition**: Élément de numéro atomique 60 et de symbole Nd.
- **Definition**: Chemical element with atomic number 60 and symbol
Nd.
- **Definition**: Elemento químico de número atómico 60 y símbolo Nd.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Nd, 
  - Nd, 
  - Nd, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33372 (closeMatch)
  - http://fr.dbpedia.org/page/Néodyme (exactMatch)
  - http://dbpedia.org/page/Neodymium (exactMatch)
  - http://es.dbpedia.org/page/Neodimio (exactMatch)
  - https://fr.wikipedia.org/wiki/Néodyme (exactMatch)
  - https://en.wikipedia.org/wiki/Neodymium (exactMatch)
  - https://es.wikipedia.org/wiki/Neodimio (exactMatch)
  - https://www.wikidata.org/wiki/Q1388 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-Z5HSKR9D-Q

[]{#prométhium}

####  prométhium
* `promethium`
* `promecio`
- **Definition**: Élément de numéro atomique 61 et de symbole Pm.
- **Definition**: Chemical element with atomic number 61 and symbol
Pm.
- **Definition**: Elemento químico de número atómico 61 y símbolo Pm.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pm, 
  - Pm, 
  - Pm, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33373 (closeMatch)
  - http://fr.dbpedia.org/page/Prométhium (exactMatch)
  - http://dbpedia.org/page/Promethium (exactMatch)
  - http://es.dbpedia.org/page/Promecio (exactMatch)
  - https://fr.wikipedia.org/wiki/Prométhium (exactMatch)
  - https://en.wikipedia.org/wiki/Promethium (exactMatch)
  - https://es.wikipedia.org/wiki/Promecio (exactMatch)
  - https://www.wikidata.org/wiki/Q1809 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CV59QX8B-L

[]{#samarium}

####  samarium
* `samarium`
* `samario`
- **Definition**: Élément de numéro atomique 62 et de symbole Sm.
- **Definition**: Chemical element with atomic number 62 and symbol
Sm.
- **Definition**: Elemento químico de número atómico 62 y símbolo Sm.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Sm, 
  - Sm, 
  - Sm, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33374 (closeMatch)
  - http://fr.dbpedia.org/page/Samarium (exactMatch)
  - http://dbpedia.org/page/Samarium (exactMatch)
  - http://es.dbpedia.org/page/Samario (exactMatch)
  - https://fr.wikipedia.org/wiki/Samarium (exactMatch)
  - https://en.wikipedia.org/wiki/Samarium (exactMatch)
  - https://es.wikipedia.org/wiki/Samario (exactMatch)
  - https://www.wikidata.org/wiki/Q1819 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-JTHN5WMQ-W

[]{#europium}

####  europium
* `europium`
* `europio`
- **Definition**: Élément de numéro atomique 63 et de symbole Eu.
- **Definition**: Chemical element with atomic number 63 and symbol
Eu.
- **Definition**: Elemento químico de número atómico 63 y símbolo Eu.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Eu, 
  - Eu, 
  - Eu, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_32999 (closeMatch)
  - http://fr.dbpedia.org/page/Europium (exactMatch)
  - http://dbpedia.org/page/Europium (exactMatch)
  - http://es.dbpedia.org/page/Europio (exactMatch)
  - https://fr.wikipedia.org/wiki/Europium (exactMatch)
  - https://en.wikipedia.org/wiki/Europium (exactMatch)
  - https://es.wikipedia.org/wiki/Europio (exactMatch)
  - https://www.wikidata.org/wiki/Q1396 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-P1D55JLQ-Q

[]{#gadolinium}

####  gadolinium
* `gadolinium`
* `gadolinio`
- **Definition**: Élément de numéro atomique 64 et de symbole Gd.
- **Definition**: Chemical element with atomic number 64 and symbol
Gd.
- **Definition**: Elemento químico de número atómico 64 y símbolo Gd.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Gd, 
  - Gd, 
  - Gd, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33375 (closeMatch)
  - http://fr.dbpedia.org/page/Gadolinium (exactMatch)
  - http://dbpedia.org/page/Gadolinium (exactMatch)
  - http://es.dbpedia.org/page/Gadolinio (exactMatch)
  - https://fr.wikipedia.org/wiki/Gadolinium (exactMatch)
  - https://en.wikipedia.org/wiki/Gadolinium (exactMatch)
  - https://es.wikipedia.org/wiki/Gadolinio (exactMatch)
  - https://www.wikidata.org/wiki/Q1832 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-Q4V6R5PS-J

[]{#terbium}

####  terbium
* `terbium`
* `terbio`
- **Definition**: Élément de numéro atomique 65 et de symbole Tb.
- **Definition**: Chemical element with atomic number 65 and symbol
Tb.
- **Definition**: Elemento químico de número atómico 65 y símbolo Tb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Tb, 
  - Tb, 
  - Tb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33376 (closeMatch)
  - http://fr.dbpedia.org/page/Terbium (exactMatch)
  - http://dbpedia.org/page/Terbium (exactMatch)
  - http://es.dbpedia.org/page/Terbio (exactMatch)
  - https://fr.wikipedia.org/wiki/Terbium (exactMatch)
  - https://en.wikipedia.org/wiki/Terbium (exactMatch)
  - https://es.wikipedia.org/wiki/Terbio (exactMatch)
  - https://www.wikidata.org/wiki/Q1838 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-RMXJ8T8X-M

[]{#dysprosium}

####  dysprosium
* `dysprosium`
* `disprosio`
- **Definition**: Élément de numéro atomique 66 et de symbole Dy.
- **Definition**: Chemical element with atomic number 66 and symbol
Dy.
- **Definition**: Elemento químico de número atómico 66 y símbolo Dy.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Dy, 
  - Dy, 
  - Dy, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33377 (closeMatch)
  - http://fr.dbpedia.org/page/Dysprosium (exactMatch)
  - http://dbpedia.org/page/Dysprosium (exactMatch)
  - http://es.dbpedia.org/page/Disprosio (exactMatch)
  - https://fr.wikipedia.org/wiki/Dysprosium (exactMatch)
  - https://en.wikipedia.org/wiki/Dysprosium (exactMatch)
  - https://es.wikipedia.org/wiki/Disprosio (exactMatch)
  - https://www.wikidata.org/wiki/Q1843 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GSHRX5GS-Z

[]{#holmium}

####  holmium
* `holmium`
* `holmio`
- **Definition**: Élément de numéro atomique 67 et de symbole Ho.
- **Definition**: Chemical element with atomic number 67 and symbol
Ho.
- **Definition**: Elemento químico de número atómico 67 y símbolo Ho.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ho, 
  - Ho, 
  - Ho, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33378 (closeMatch)
  - http://fr.dbpedia.org/page/Holmium (exactMatch)
  - http://dbpedia.org/page/Holmium (exactMatch)
  - http://es.dbpedia.org/page/Holmio (exactMatch)
  - https://fr.wikipedia.org/wiki/Holmium (exactMatch)
  - https://en.wikipedia.org/wiki/Holmium (exactMatch)
  - https://es.wikipedia.org/wiki/Holmio (exactMatch)
  - https://www.wikidata.org/wiki/Q1846 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-X7XM14L0-W

[]{#erbium}

####  erbium
* `erbium`
* `erbio`
- **Definition**: Élément de numéro atomique 68 et de symbole Er.
- **Definition**: Chemical element with atomic number 68 and symbol
Er.
- **Definition**: Elemento químico de número atómico 68 y símbolo Er.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Er, 
  - Er, 
  - Er, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33379 (closeMatch)
  - http://fr.dbpedia.org/page/Erbium (exactMatch)
  - http://dbpedia.org/page/Erbium (exactMatch)
  - http://es.dbpedia.org/page/Erbio (exactMatch)
  - https://fr.wikipedia.org/wiki/Erbium (exactMatch)
  - https://en.wikipedia.org/wiki/Erbium (exactMatch)
  - https://es.wikipedia.org/wiki/Erbio (exactMatch)
  - https://www.wikidata.org/wiki/Q1849 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-F9BT8LGW-R

[]{#thulium}

####  thulium
* `thulium`
* `tulio`
- **Definition**: Élément de numéro atomique 69 et de symbole Tm.
- **Definition**: Chemical element with atomic number 69 and symbol
Tm.
- **Definition**: Elemento químico de número atómico 69 y símbolo Tm.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Tm, 
  - Tm, 
  - Tm, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33380 (closeMatch)
  - http://fr.dbpedia.org/page/Thulium (exactMatch)
  - http://dbpedia.org/page/Thulium (exactMatch)
  - http://es.dbpedia.org/page/Tulio (exactMatch)
  - https://fr.wikipedia.org/wiki/Thulium (exactMatch)
  - https://en.wikipedia.org/wiki/Thulium (exactMatch)
  - https://es.wikipedia.org/wiki/Tulio (exactMatch)
  - https://www.wikidata.org/wiki/Q1853 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-QR0ZMLT2-8

[]{#ytterbium}

####  ytterbium
* `ytterbium`
* `yterbio`
- **Definition**: Élément de numéro atomique 70 et de symbole Yb.
- **Definition**: Chemical element with atomic number 70 and symbol
Yb.
- **Definition**: Elemento químico de número atómico 70 y símbolo Yb.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Yb, 
  - Yb, 
  - Yb, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33381 (closeMatch)
  - http://fr.dbpedia.org/page/Ytterbium (exactMatch)
  - http://dbpedia.org/page/Ytterbium (exactMatch)
  - http://es.dbpedia.org/page/Yterbio (exactMatch)
  - https://fr.wikipedia.org/wiki/Ytterbium (exactMatch)
  - https://en.wikipedia.org/wiki/Ytterbium (exactMatch)
  - https://es.wikipedia.org/wiki/Yterbio (exactMatch)
  - https://www.wikidata.org/wiki/Q1855 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NFCKRP8Z-J

[]{#lutécium}

####  lutécium
* `lutetium`
* `lutecio`
- **Definition**: Élément de numéro atomique 71 et de symbole Lu.
- **Definition**: Chemical element with atomic number 71 and symbol
Lu.
- **Definition**: Elemento químico de número atómico 71 y símbolo Lu.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Lu, 
  - lutétium, 
  - Lu, 
  - Lu, 
- **Source:**
  - The group 3 dilemma by Philip Ball, 21 April 2017, https://www.chemistryworld.com/opinion/the-group-3-dilemma/3007080.article, 
  - www.iupac.org/project/2015-039-2-200, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33382 (closeMatch)
  - http://fr.dbpedia.org/page/Lutécium (exactMatch)
  - http://dbpedia.org/page/Lutetium (exactMatch)
  - http://es.dbpedia.org/page/Lutecio (exactMatch)
  - https://fr.wikipedia.org/wiki/Lutécium (exactMatch)
  - https://en.wikipedia.org/wiki/Lutetium (exactMatch)
  - https://es.wikipedia.org/wiki/Lutecio (exactMatch)
  - https://www.wikidata.org/wiki/Q1857 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-BZFLDL73-0

[]{#thorium}

####  thorium
* `thorium`
* `torio`
- **Definition**: Élément de numéro atomique 90 et de symbole Th.
- **Definition**: Chemical element with atomic number 90 and symbol
Th.
- **Definition**: Elemento químico de número atómico 90 y símbolo Th.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Th, 
  - Th, 
  - Th, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33385 (closeMatch)
  - http://fr.dbpedia.org/page/Thorium (exactMatch)
  - http://dbpedia.org/page/Thorium (exactMatch)
  - http://es.dbpedia.org/page/Torio (exactMatch)
  - https://fr.wikipedia.org/wiki/Thorium (exactMatch)
  - https://en.wikipedia.org/wiki/Thorium (exactMatch)
  - https://es.wikipedia.org/wiki/Torio (exactMatch)
  - https://www.wikidata.org/wiki/Q1115 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-ZJ4ZVTV9-3

[]{#protactinium}

####  protactinium
* `protactinium`
* `protactinio`
- **Definition**: Élément de numéro atomique 91 et de symbole Pa.
- **Definition**: Chemical element with atomic number 91 and symbol
Pa.
- **Definition**: Elemento químico de número atómico 91 y símbolo Pa.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pa, 
  - Pa, 
  - Pa, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33386 (closeMatch)
  - http://fr.dbpedia.org/page/Protactinium (exactMatch)
  - http://dbpedia.org/page/Protactinium (exactMatch)
  - http://es.dbpedia.org/page/Protactinio (exactMatch)
  - https://fr.wikipedia.org/wiki/Protactinium (exactMatch)
  - https://en.wikipedia.org/wiki/Protactinium (exactMatch)
  - https://es.wikipedia.org/wiki/Protactinio (exactMatch)
  - https://www.wikidata.org/wiki/Q1109 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-LKF0484D-F

[]{#uranium}

####  uranium
* `uranium`
* `uranio`
- **Definition**: Élément de numéro atomique 92 et de symbole U.
- **Definition**: Chemical element with atomic number 92 and symbol U.
- **Definition**: Elemento químico de número atómico 92 y símbolo U.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - U, 
  - U, 
  - U, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_27214 (closeMatch)
  - http://fr.dbpedia.org/page/Uranium (exactMatch)
  - http://dbpedia.org/page/Uranium (exactMatch)
  - http://es.dbpedia.org/page/Uranio (exactMatch)
  - https://fr.wikipedia.org/wiki/Uranium (exactMatch)
  - https://en.wikipedia.org/wiki/Uranium (exactMatch)
  - https://es.wikipedia.org/wiki/Uranio (exactMatch)
  - https://www.wikidata.org/wiki/Q1098 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CXXQX7D7-P

[]{#neptunium}

####  neptunium
* `neptunium`
* `neptunio`
- **Definition**: Élément de numéro atomique 93 et de symbole Np.
- **Definition**: Chemical element with atomic number 93 and symbol
Np.
- **Definition**: Elemento químico de número atómico 93 y símbolo Np.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Np, 
  - élément 93, 
  - Np, 
  - element 93, 
  - Np, 
  - elemento 93, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33387 (closeMatch)
  - http://fr.dbpedia.org/page/Neptunium (exactMatch)
  - http://dbpedia.org/page/Neptunium (exactMatch)
  - http://es.dbpedia.org/page/Neptunio (exactMatch)
  - https://fr.wikipedia.org/wiki/Neptunium (exactMatch)
  - https://en.wikipedia.org/wiki/Neptunium (exactMatch)
  - https://es.wikipedia.org/wiki/Neptunio (exactMatch)
  - https://www.wikidata.org/wiki/Q1105 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-WQGJPGN3-N

[]{#plutonium}

####  plutonium
* `plutonium`
* `plutonio`
- **Definition**: Élément de numéro atomique 94 et de symbole Pu.
- **Definition**: Chemical element with atomic number 94 and symbol
Pu.
- **Definition**: Elemento químico de número atómico 94 y símbolo Pu.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Pu, 
  - élément 94, 
  - Pu, 
  - element 94, 
  - Pu, 
  - elemento 94, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33388 (closeMatch)
  - http://fr.dbpedia.org/page/Plutonium (exactMatch)
  - http://dbpedia.org/page/Plutonium (exactMatch)
  - http://es.dbpedia.org/page/Plutonio (exactMatch)
  - https://fr.wikipedia.org/wiki/Plutonium (exactMatch)
  - https://en.wikipedia.org/wiki/Plutonium (exactMatch)
  - https://es.wikipedia.org/wiki/Plutonio (exactMatch)
  - https://www.wikidata.org/wiki/Q1102 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-GJDFZ77K-V

[]{#américium}

####  américium
* `americium`
* `americio`
- **Definition**: Élément de numéro atomique 95 et de symbole Am.
- **Definition**: Chemical element with atomic number 95 and symbol
Am.
- **Definition**: Elemento químico de número atómico 95 y símbolo Am.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Am, 
  - élément 95, 
  - Am, 
  - element 95, 
  - Am, 
  - elemento 95, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33389 (closeMatch)
  - http://fr.dbpedia.org/page/Américium (exactMatch)
  - http://dbpedia.org/page/Americium (exactMatch)
  - http://es.dbpedia.org/page/Americio (exactMatch)
  - https://fr.wikipedia.org/wiki/Américium (exactMatch)
  - https://en.wikipedia.org/wiki/Americium (exactMatch)
  - https://es.wikipedia.org/wiki/Americio (exactMatch)
  - https://www.wikidata.org/wiki/Q1872 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-R5MG15L7-3

[]{#curium}

####  curium
* `curium`
* `curio`
- **Definition**: Élément de numéro atomique 96 et de symbole Cm.
- **Definition**: Chemical element with atomic number 96 and symbol
Cm.
- **Definition**: Elemento químico de número atómico 96 y símbolo Cm.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cm, 
  - élément 96, 
  - Cm, 
  - element 96, 
  - Cm, 
  - elemento 96, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33390 (closeMatch)
  - http://fr.dbpedia.org/page/Curium (exactMatch)
  - http://dbpedia.org/page/Curium (exactMatch)
  - http://es.dbpedia.org/page/Curio (exactMatch)
  - https://fr.wikipedia.org/wiki/Curium (exactMatch)
  - https://en.wikipedia.org/wiki/Curium (exactMatch)
  - https://es.wikipedia.org/wiki/Curio (exactMatch)
  - https://www.wikidata.org/wiki/Q1876 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-K0MXFJV4-P

[]{#berkélium}

####  berkélium
* `berkelium`
* `berkelio`
- **Definition**: Élément de numéro atomique 97 et de symbole Bk.
- **Definition**: Chemical element with atomic number 97 and symbol
Bk.
- **Definition**: Elemento químico de número atómico 97 y símbolo Bk.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Bk, 
  - élément 97, 
  - Bk, 
  - element 97, 
  - Bk, 
  - elemento 97, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33391 (closeMatch)
  - http://fr.dbpedia.org/page/Berkélium (exactMatch)
  - http://dbpedia.org/page/Berkelium (exactMatch)
  - http://es.dbpedia.org/page/Berkelio (exactMatch)
  - https://fr.wikipedia.org/wiki/Berkélium (exactMatch)
  - https://en.wikipedia.org/wiki/Berkelium (exactMatch)
  - https://es.wikipedia.org/wiki/Berkelio (exactMatch)
  - https://www.wikidata.org/wiki/Q1882 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-J1C32XNL-H

[]{#californium}

####  californium
* `californium`
* `californio`
- **Definition**: Élément de numéro atomique 98 et de symbole Cf.
- **Definition**: Chemical element with atomic number 98 and symbol
Cf.
- **Definition**: Elemento químico de número atómico 98 y símbolo Cf.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Cf, 
  - élément 98, 
  - Cf, 
  - element 98, 
  - Cf, 
  - elemento 98, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33392 (closeMatch)
  - http://fr.dbpedia.org/page/Californium (exactMatch)
  - http://dbpedia.org/page/Californium (exactMatch)
  - http://es.dbpedia.org/page/Californio (exactMatch)
  - https://fr.wikipedia.org/wiki/Californium (exactMatch)
  - https://en.wikipedia.org/wiki/Californium (exactMatch)
  - https://es.wikipedia.org/wiki/Californio (exactMatch)
  - https://www.wikidata.org/wiki/Q1888 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-CDTG8KJ0-0

[]{#einsteinium}

####  einsteinium
* `einsteinium`
* `einstenio`
- **Definition**: Élément de numéro atomique 99 et de symbole Es.
- **Definition**: Chemical element with atomic number 99 and symbol
Es.
- **Definition**: Elemento químico de número atómico 99 y símbolo Es.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Es, 
  - élément 99, 
  - Es, 
  - element 99, 
  - Es, 
  - elemento 99, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33393 (closeMatch)
  - http://fr.dbpedia.org/page/Einsteinium (exactMatch)
  - http://dbpedia.org/page/Einsteinium (exactMatch)
  - http://es.dbpedia.org/page/Einstenio (exactMatch)
  - https://fr.wikipedia.org/wiki/Einsteinium (exactMatch)
  - https://en.wikipedia.org/wiki/Einsteinium (exactMatch)
  - https://es.wikipedia.org/wiki/Einstenio (exactMatch)
  - https://www.wikidata.org/wiki/Q1892 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-V5VQHGWX-S

[]{#fermium}

####  fermium
* `fermium`
* `fermio`
- **Definition**: Élément de numéro atomique 100 et de symbole Fm.
- **Definition**: Chemical element with atomic number 100 and symbol
Fm.
- **Definition**: Elemento químico de número atómico 100 y símbolo Fm.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Fm, 
  - élément 100, 
  - Fm, 
  - element 100, 
  - Fm, 
  - elemento 100, 
- **Source:**
  - Bonding and the electronic structure of the actinide metals, Jean-MarcFournier (1976), Journal of Physics and Chemistry of Solids, Volume 37, Issue 2, 1976, Pages 235-244, https://doi.org/10.1016/0022-3697(76)90167-0
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33394 (closeMatch)
  - http://fr.dbpedia.org/page/Fermium (exactMatch)
  - http://dbpedia.org/page/Fermium (exactMatch)
  - http://es.dbpedia.org/page/Fermio (exactMatch)
  - https://fr.wikipedia.org/wiki/Fermium (exactMatch)
  - https://en.wikipedia.org/wiki/Fermium (exactMatch)
  - https://es.wikipedia.org/wiki/Fermio (exactMatch)
  - https://www.wikidata.org/wiki/Q1896 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-FPGD9SBX-X

[]{#mendélévium}

####  mendélévium
* `mendelevium`
* `mendelevio`
- **Definition**: Élément de numéro atomique 101 et de symbole Md. Son
nom provisoire était : unnilunium (symbole : Unu).
- **Definition**: Chemical element with atomic number 101 and symbol
Md. Its provisional name was : unnilunium (symbol : Unu).
- **Definition**: Elemento químico de número atómico 101 y símbolo Md.
Su nombre provisional era : unnilunio (símbolo : Unu).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Md, 
  - élément 101, 
  - Unu, 
  - unnilunium, 
  - Md, 
  - element 101, 
  - Unu, 
  - unnilunium, 
  - Md, 
  - elemento 101, 
  - Unu, 
  - unnilunio, 
- **Source:**
  - Bonding and the electronic structure of the actinide metals, Jean-MarcFournier (1976), Journal of Physics and Chemistry of Solids, Volume 37, Issue 2, 1976, Pages 235-244, https://doi.org/10.1016/0022-3697(76)90167-0, 
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33395 (closeMatch)
  - http://fr.dbpedia.org/page/Mendélévium (exactMatch)
  - http://dbpedia.org/page/Mendelevium (exactMatch)
  - http://es.dbpedia.org/page/Mendelevio (exactMatch)
  - https://fr.wikipedia.org/wiki/Mendélévium (exactMatch)
  - https://en.wikipedia.org/wiki/Mendelevium (exactMatch)
  - https://es.wikipedia.org/wiki/Mendelevio (exactMatch)
  - https://www.wikidata.org/wiki/Q1898 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-NQR2DXN3-R

[]{#nobélium}

####  nobélium
* `nobelium`
* `nobelio`
- **Definition**: Élément de numéro atomique 102 et de symbole No. Son
nom provisoire était : unnilbium (symbole : Unb).
- **Definition**: Chemical element with atomic number 102 and symbol
No. Its provisional name was : unnilbium (symbol : Unb).
- **Definition**: Elemento químico de número atómico 102 y símbolo No.
Su nombre provisional era : unnilbio (símbolo : Unb).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - No, 
  - élément 102, 
  - Unb, 
  - unnilbium, 
  - No, 
  - element 102, 
  - Unb, 
  - unnilbium, 
  - No, 
  - elemento 102, 
  - Unb, 
  - unnilbio, 
- **Source:**
  - Bonding and the electronic structure of the actinide metals, Jean-MarcFournier (1976), Journal of Physics and Chemistry of Solids, Volume 37, Issue 2, 1976, Pages 235-244, https://doi.org/10.1016/0022-3697(76)90167-0, 
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33396 (closeMatch)
  - http://fr.dbpedia.org/page/Nobélium (exactMatch)
  - http://dbpedia.org/page/Nobelium (exactMatch)
  - http://es.dbpedia.org/page/Nobelio (exactMatch)
  - https://fr.wikipedia.org/wiki/Nobélium (exactMatch)
  - https://en.wikipedia.org/wiki/Nobelium (exactMatch)
  - https://es.wikipedia.org/wiki/Nobelio (exactMatch)
  - https://www.wikidata.org/wiki/Q1901 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-JZ85JL0V-4

[]{#actinium}

####  actinium
* `actinium`
* `actinio`
- **Definition**: Élément de numéro atomique 89 et de symbole Ac.
- **Definition**: Chemical element with atomic number 89 and symbol
Ac.
- **Definition**: Elemento químico de número atómico 89 y símbolo Ac.
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Ac, 
  - Ac, 
  - Ac, 
- **Source:**
  - The group 3 dilemma by Philip Ball, 21 April 2017, https://www.chemistryworld.com/opinion/the-group-3-dilemma/3007080.article, 
  - www.iupac.org/project/2015-039-2-200, 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33337 (closeMatch)
  - http://fr.dbpedia.org/page/Actinium (exactMatch)
  - http://dbpedia.org/page/Actinium (exactMatch)
  - http://es.dbpedia.org/page/Actinio (exactMatch)
  - https://fr.wikipedia.org/wiki/Actinium (exactMatch)
  - https://en.wikipedia.org/wiki/Actinium (exactMatch)
  - https://es.wikipedia.org/wiki/Actinio (exactMatch)
  - https://www.wikidata.org/wiki/Q1121 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-MQ7K65FT-R

[]{#lawrencium}

####  lawrencium
* `lawrencium`
* `lawrencio`
- **Definition**: Élément de numéro atomique 103 et de symbole Lr. Son
nom provisoire était : unniltrium (symbole : Unt).
- **Definition**: Chemical element with atomic number 103 and symbol
Lr. Its provisional name was : unniltrium (symbol : Unt).
- **Definition**: Elemento químico de número atómico 103 y símbolo Lr.
Su nombre provisional era : unniltrio (símbolo : Unt).
- **Child of**:
  - [`chemical element`](#chemical-element)
- **Alternate labels:**
  - Lr, 
  - élément 103, 
  - Unt, 
  - unniltrium, 
  - Lr, 
  - element 103, 
  - Unt, 
  - unniltrium, 
  - Lr, 
  - elemento 103, 
  - Unt, 
  - unniltrio, 
- **Source:**
  - The group 3 dilemma by Philip Ball, 21 April 2017, https://www.chemistryworld.com/opinion/the-group-3-dilemma/3007080.article, 
  - www.iupac.org/project/2015-039-2-200, 
  - Bonding and the electronic structure of the actinide metals, Jean-MarcFournier (1976), Journal of Physics and Chemistry of Solids, Volume 37, Issue 2, 1976, Pages 235-244, https://doi.org/10.1016/0022-3697(76)90167-0, 
  - Nomenclature of Inorganic chemistry IUPAC recommendations 2005, page 47, Systematic nomenclature and symbols for new elements, https://old.iupac.org/publications/books/rbook/Red_Book_2005.pdf, 
  - , 
- **Matches:**
  - http://purl.obolibrary.org/obo/CHEBI_33397 (closeMatch)
  - http://fr.dbpedia.org/page/Lawrencium (exactMatch)
  - http://dbpedia.org/page/Lawrencium (exactMatch)
  - http://es.dbpedia.org/page/Lawrencio (exactMatch)
  - https://fr.wikipedia.org/wiki/Lawrencium (exactMatch)
  - https://en.wikipedia.org/wiki/Lawrencium (exactMatch)
  - https://es.wikipedia.org/wiki/Lawrencio (exactMatch)
  - https://www.wikidata.org/wiki/Q1905 (exactMatch)
- **Concept URI:** http://data.loterre.fr/ark:/67375/8HQ-R2S5FRSJ-L


[]{#nuclide}

##  nuclide
- **Definition**: Atom that is characterised by its number of protons
and number of neutrons.
- **Child of**:
  - [`materials`](#materials)
- **Alternate labels:**
  - isotope
- **Other Properties:**
  - **scopeNote**: 
Only naturally occurring nuclides were included. While it was aimed to include all stable nuclides, only some radioactive nuclides are included. 
- **Matches:**
  - https://www.wikidata.org/wiki/Q108149 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5264a37a

[]{#silicon-30}

###  silicon-30
- **Definition**: Isotope of silicon with mass 30
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 30Si, 
  - Si-30, 
- **Matches:**
  - http://www.wikidata.org/entity/Q14338840 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_36dbfd1e

[]{#sulfur-33}

###  sulfur-33
- **Definition**: Isotope of sulphur with mass 33
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 33S, 
  - S-33, 
  - sulphur-33, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2055815 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b1284fee

[]{#carbon-12}

###  carbon-12
- **Definition**: Isotope of carbon with mass 12
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 12C, 
  - C-12, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1058364 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4a430372

[]{#tungsten-184}

###  tungsten-184
- **Definition**: Isotope of tungsten with mass 184
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 184W, 
  - W-184, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882868 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e62451fc

[]{#ytterbium-168}

###  ytterbium-168
- **Definition**: Isotope of ytterbium with mass 168
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 168Yb, 
  - Yb-168, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882562 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5b0e584b

[]{#ytterbium-171}

###  ytterbium-171
- **Definition**: Isotope of ytterbium with mass 171
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 171Yb, 
  - Yb-171, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882567 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d5b4a5a4

[]{#ytterbium-170}

###  ytterbium-170
- **Definition**: Isotope of ytterbium with mass 170
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 170Yb, 
  - Yb-170, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882565 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee470414

[]{#ytterbium-172}

###  ytterbium-172
- **Definition**: Isotope of ytterbium with mass 172
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 172Yb, 
  - Yb-172, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882570 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0f86af5e

[]{#ytterbium-173}

###  ytterbium-173
- **Definition**: Isotope of ytterbium with mass 173
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 173Yb, 
  - Yb-173, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882571 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a16ae7d6

[]{#ytterbium-174}

###  ytterbium-174
- **Definition**: Isotope of ytterbium with mass 174
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 174Yb, 
  - Yb-174, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882575 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b77a42f1

[]{#ytterbium-176}

###  ytterbium-176
- **Definition**: Isotope of ytterbium with mass 176
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 176Yb, 
  - Yb-176, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882579 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_71f01f48

[]{#iridium-191}

###  iridium-191
- **Definition**: Isotope of iridium with mass 191
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 191Ir, 
  - Ir-191, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883039 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f16172eb

[]{#iridium-193}

###  iridium-193
- **Definition**: Isotope of iridium with mass 193
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 193Ir, 
  - Ir-193, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883045 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d944f289

[]{#platinum-194}

###  platinum-194
- **Definition**: Isotope of platinum with mass 194
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 194Pt, 
  - Pt-194, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883099 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_78c0a330

[]{#platinum-192}

###  platinum-192
- **Definition**: Isotope of platinum with mass 192
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 192Pt, 
  - Pt-192, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883096 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4f25c598

[]{#platinum-196}

###  platinum-196
- **Definition**: Isotope of platinum with mass 196
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 196Pt, 
  - Pt-196, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883102 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dae04b1d

[]{#platinum-195}

###  platinum-195
- **Definition**: Isotope of platinum with mass 195
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 195Pt, 
  - Pt-195, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883100 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2b5475d8

[]{#platinum-198}

###  platinum-198
- **Definition**: Isotope of platinum with mass 198
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 198Pt, 
  - Pt-198, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883105 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_767bd948

[]{#lutetium-175}

###  lutetium-175
- **Definition**: Isotope of lutetium with mass 175
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 175Lu, 
  - Lu-175, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882652 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_97e1697a

[]{#tin-122}

###  tin-122
- **Definition**: Isotope of tin with mass 122
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 122Sn, 
  - Sn-122, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1895278 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_11fc95e5

[]{#erbium-162}

###  erbium-162
- **Definition**: Isotope of erbium with mass 162
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 162Er, 
  - Er-162, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874939 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_758aff67

[]{#erbium-164}

###  erbium-164
- **Definition**: Isotope of erbium with mass 164
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 164Er, 
  - Er-164, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874941 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d9b4651e

[]{#erbium-168}

###  erbium-168
- **Definition**: Isotope of erbium with mass 168
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 168Er, 
  - Er-168, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874946 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d95ddf57

[]{#erbium-166}

###  erbium-166
- **Definition**: Isotope of erbium with mass 166
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 166Er, 
  - Er-166, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874944 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_541ff9d6

[]{#erbium-167}

###  erbium-167
- **Definition**: Isotope of erbium with mass 167
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 167Er, 
  - Er-167, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874945 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_11bbb681

[]{#erbium-170}

###  erbium-170
- **Definition**: Isotope of erbium with mass 170
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 170Er, 
  - Er-170, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15874948 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_78ffaee2

[]{#samarium-150}

###  samarium-150
- **Definition**: Isotope of samarium with mass 150
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 150Sm, 
  - Sm-150, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1905822 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b5cd561e

[]{#antimony-121}

###  antimony-121
- **Definition**: Isotope of antimony with mass 121
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 121Sb, 
  - Sb-121, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1856817 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e3c8b27e

[]{#argon-40}

###  argon-40
- **Definition**: Isotope of argon with mass 40
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 40Ar, 
  - Ar-40, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1929004 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_93f3727f

[]{#protium}

###  protium
- **Definition**: Isotope of hydrogen with 0 neutrons with mass 1
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - H-1, 
  - 1H, 
- **Matches:**
  - http://www.wikidata.org/entity/Q12830437 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_921309ce

[]{#holmium-165}

###  holmium-165
- **Definition**: Isotope of holmium with mass 165
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 165Ho, 
  - Ho-165, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15876412 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5dc5a57f

[]{#potassium-39}

###  potassium-39
- **Definition**: Isotope of potassium with mass 39
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - K-39, 
  - 39K, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2023226 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_035a8f5a

[]{#iron-57}

###  iron-57
- **Definition**: Isotope of iron with mass 57
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 57Fe, 
  - Fe-57, 
- **Matches:**
  - http://www.wikidata.org/entity/Q14744877 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5a20b188

[]{#thulium-169}

###  thulium-169
- **Definition**: Isotope of thulium with mass 169
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 169Tm, 
  - Tm-169, 
- **Matches:**
  - http://www.wikidata.org/entity/Q15882884 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8e971c30

[]{#selenium-78}

###  selenium-78
- **Definition**: Isotope of selenium with mass 78
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 78Se, 
  - Se-78, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1890759 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_45408129

[]{#europium-153}

###  europium-153
- **Definition**: Isotope of europium with mass 153
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 153Eu, 
  - Eu-153, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2027407 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8c348a7c

[]{#dysprosium-156}

###  dysprosium-156
- **Definition**: Isotope of dysprosium with mass 156
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 156Dy, 
  - Dy-156, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574970 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_525c36e1

[]{#dysprosium-158}

###  dysprosium-158
- **Definition**: Isotope of dysprosium with mass 158
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 158Dy, 
  - Dy-158, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574971 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_28d13e35

[]{#dysprosium-160}

###  dysprosium-160
- **Definition**: Isotope of dysprosium with mass 160
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 160Dy, 
  - Dy-160, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574974 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f49d9fa4

[]{#dysprosium-163}

###  dysprosium-163
- **Definition**: Isotope of dysprosium with mass 163
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 163Dy, 
  - Dy-163, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574978 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_77e047aa

[]{#dysprosium-164}

###  dysprosium-164
- **Definition**: Isotope of dysprosium with mass 164
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 164Dy, 
  - Dy-164, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574979 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7f4d8aa8

[]{#dysprosium-161}

###  dysprosium-161
- **Definition**: Isotope of dysprosium with mass 161
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 161Dy, 
  - Dy-161, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574976 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a8bf2c4f

[]{#dysprosium-162}

###  dysprosium-162
- **Definition**: Isotope of dysprosium with mass 162
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 162Dy, 
  - Dy-162, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13574977 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6334fb78

[]{#magnesium-26}

###  magnesium-26
- **Definition**: Isotope of magnesium with mass 26
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 26Mg, 
  - Mg-26, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13808814 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4ff16f3e

[]{#molybdenum-96}

###  molybdenum-96
- **Definition**: Isotope of molybdenum with mass 96
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 96Mo, 
  - Mo-96, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1928853 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c0aebc6

[]{#molybdenum-94}

###  molybdenum-94
- **Definition**: Isotope of molybdenum with mass 94
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 94Mo, 
  - Mo-94, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13860694 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1bf33c5e

[]{#lithium-6}

###  lithium-6
- **Definition**: Isotope of lithium with mass 6
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 6Li, 
  - Li-6, 
- **Matches:**
  - http://www.wikidata.org/entity/Q10322200 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cb89bf3a

[]{#lithium-7}

###  lithium-7
- **Definition**: Isotope of lithium with mass 7
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 7Li, 
  - Li-7, 
- **Matches:**
  - http://www.wikidata.org/entity/Q10322201 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d3787f38

[]{#carbon-13}

###  carbon-13
- **Definition**: Isotope of carbon with mass 13
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - C-13, 
  - 13C, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1770822 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_54fc7af8

[]{#manganese-55}

###  manganese-55
- **Definition**: Isotope of manganese with mass 55
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 55Mn, 
  - Mn-55, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13811964 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dce98965

[]{#cadmium-112}

###  cadmium-112
- **Definition**: Isotope of cadmium with mass 112
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 112Cd, 
  - Cd-112, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2040848 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3f768b80

[]{#thallium-203}

###  thallium-203
- **Definition**: Isotope of thallium with mass 203
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 203Tl, 
  - Tl-203, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883327 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_21a82c22

[]{#mercury-196}

###  mercury-196
- **Definition**: Isotope of mercury with mass 196
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 196Hg, 
  - Hg-196, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883230 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9bd85a6a

[]{#mercury-199}

###  mercury-199
- **Definition**: Isotope of mercury with mass 199
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 199Hg, 
  - Hg-199, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883234 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8425e6e1

[]{#mercury-198}

###  mercury-198
- **Definition**: Isotope of mercury with mass 198
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 198Hg, 
  - Hg-198, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883233 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_449e5c74

[]{#mercury-202}

###  mercury-202
- **Definition**: Isotope of mercury with mass 202
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 202Hg, 
  - Hg-202, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883239 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2d205d68

[]{#mercury-200}

###  mercury-200
- **Definition**: Isotope of mercury with mass 200
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 200Hg, 
  - Hg-200, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883236 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c4ce97bd

[]{#mercury-201}

###  mercury-201
- **Definition**: Isotope of mercury with mass 201
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 201Hg, 
  - Hg-201, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883237 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6708f55a

[]{#mercury-204}

###  mercury-204
- **Definition**: Isotope of mercury with mass 204
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 204Hg, 
  - Hg-204, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883242 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2e435946

[]{#samarium-149}

###  samarium-149
- **Definition**: Isotope of samarium with mass 149
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 149Sm, 
  - Sm-149, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1915454 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f2f53cac

[]{#argon-36}

###  argon-36
- **Definition**: Isotope of argon with mass 36
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 36Ar, 
  - Ar-36, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2019992 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_634a9fef

[]{#deuterium}

###  deuterium
- **Definition**: Isotope of hydrogen with 1 neutron with mass 2
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - D, 
  - 2H, 
  - H-2, 
- **Matches:**
  - http://www.wikidata.org/entity/Q102296 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bfc6c4ac

[]{#gold-197}

###  gold-197
- **Definition**: Isotope of gold with mass 197
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 197Au, 
  - Au-197, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883174 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_edfee844

[]{#germanium-72}

###  germanium-72
- **Definition**: Isotope of germanium with mass 72
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 72Ge, 
  - Ge-72, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2035731 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d7e15bbf

[]{#vanadium-51}

###  vanadium-51
- **Definition**: Isotope of vanadium with mass 51
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - V-51, 
  - 51V, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1931262 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_94107e51

[]{#samarium-144}

###  samarium-144
- **Definition**: Isotope of samarium with mass 144
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 144Sm, 
  - Sm-144, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1862339 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dc9fee51

[]{#krypton-83}

###  krypton-83
- **Definition**: Isotope of krypton with mass 83
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 83Kr, 
  - Kr-83, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1921298 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_80a6e9f7

[]{#hafnium-177}

###  hafnium-177
- **Definition**: Isotope of hafnium with mass 177
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 177Hf, 
  - Hf-177, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18087014 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9e098a70

[]{#hafnium-176}

###  hafnium-176
- **Definition**: Isotope of hafnium with mass 176
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 176Hf, 
  - Hf-176, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18087012 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_eae30078

[]{#hafnium-179}

###  hafnium-179
- **Definition**: Isotope of hafnium with mass 179
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 179Hf, 
  - Hf-179, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18087018 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4d844f64

[]{#hafnium-178}

###  hafnium-178
- **Definition**: Isotope of hafnium with mass 178
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 178Hf, 
  - Hf-178, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18087016 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_33551bf0

[]{#hafnium-180}

###  hafnium-180
- **Definition**: Isotope of hafnium with mass 180
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 180Hf, 
  - Hf-180, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18087020 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9069a811

[]{#chromium-53}

###  chromium-53
- **Definition**: Isotope of chromium with mass 53
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 53Cr, 
  - Cr-53, 
- **Matches:**
  - http://www.wikidata.org/entity/Q13466446 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fca9776e

[]{#osmium-189}

###  osmium-189
- **Definition**: Isotope of osmium with mass 189
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 189Os, 
  - Os-189, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882975 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_04af303a

[]{#osmium-187}

###  osmium-187
- **Definition**: Isotope of osmium with mass 187
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 187Os, 
  - Os-187, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882972 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_16395128

[]{#osmium-188}

###  osmium-188
- **Definition**: Isotope of osmium with mass 188
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 188Os, 
  - Os-188, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882973 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7dbbec2a

[]{#osmium-190}

###  osmium-190
- **Definition**: Isotope of osmium with mass 190
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 190Os, 
  - Os-190, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882977 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_107d2645

[]{#osmium-192}

###  osmium-192
- **Definition**: Isotope of osmium with mass 192
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 192Os, 
  - Os-192, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882981 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5aae9881

[]{#molybdenum-98}

###  molybdenum-98
- **Definition**: Isotope of molybdenum with mass 98
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 98Mo, 
  - Mo-98, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2019439 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9cbf34cf

[]{#lead-208}

###  lead-208
- **Definition**: Isotope of lead with mass 208
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 208Pb, 
  - Pb-208, 
- **Matches:**
  - http://www.wikidata.org/entity/Q16670466 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f6d5d4ed

[]{#iron-56}

###  iron-56
- **Definition**: Isotope of iron with mass 56
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 56Fe, 
  - Fe-56, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1052454 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9e898635

[]{#helium-4}

###  helium-4
- **Definition**: Isotope of helium with mass 4
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 4He, 
  - He-4, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1151346 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3a1f8662

[]{#sulfur-34}

###  sulfur-34
- **Definition**: Isotope of sulfur with mass 34
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 34S, 
  - S-34, 
  - sulphur-34, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1880449 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9ba40373

[]{#ruthenium-101}

###  ruthenium-101
- **Definition**: Isotope of ruthenium with mass 101
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 101Ru, 
  - Ru-101, 
- **Matches:**
  - http://www.wikidata.org/entity/Q14292039 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e3bb1d50

[]{#xenon-128}

###  xenon-128
- **Definition**: Isotope of xenon with mass 128
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 128Xe, 
  - Xe-128, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1953543 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d0b13e13

[]{#neodymium-146}

###  neodymium-146
- **Definition**: Isotope of neodymium with mass 146
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 146Nd, 
  - Nd-146, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1880887 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3c8b21b2

[]{#tin-116}

###  tin-116
- **Definition**: Isotope of tin with mass 116
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 116Sn, 
  - Sn-116, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1995851 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_334b1987

[]{#nitrogen-14}

###  nitrogen-14
- **Definition**: Isotope of nitrogen with mass 14
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - N-14, 
  - 14N, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1138479 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_07c719c5

[]{#tellurium-126}

###  tellurium-126
- **Definition**: Isotope of tellurium with mass 126
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 126Te, 
  - Te-126, 
- **Matches:**
  - http://www.wikidata.org/entity/Q14467249 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_969eafbf

[]{#lead-206}

###  lead-206
- **Definition**: Isotope of lead with mass 206
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 206Pb, 
  - Pb-206, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883438 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ef8584a1

[]{#lead-207}

###  lead-207
- **Definition**: Isotope of lead with mass 207
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 207Pb, 
  - Pb-207, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883443 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bc8d9e4d

[]{#tantalum-180}

###  Tantalum-180
- **Definition**: Isotope of tantalum with mass 180
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 180Ta, 
  - Ta-180, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882796 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cbc3ed4d

[]{#tantalum-181}

###  tantalum-181
- **Definition**: Isotope of tantalum with mass 181
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 181Ta, 
  - Ta-181, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882801 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ab630ac0

[]{#thallium-205}

###  thallium-205
- **Definition**: Isotope of thallium with mass 205
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 205Tl, 
  - Tl-205, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18883334 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1931aa2b

[]{#nickel-64}

###  nickel-64
- **Definition**: Isotope of nickel with mass 64
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 64Ni, 
  - Ni-64, 
- **Matches:**
  - http://www.wikidata.org/entity/Q5459468 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a0a50681

[]{#silver-109}

###  silver-109
- **Definition**: Isotope of silver with mass 109
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 109Ag, 
  - Ag-109, 
- **Matches:**
  - http://www.wikidata.org/entity/Q5518299 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c053857

[]{#nitrogen-15}

###  nitrogen-15
- **Definition**: Isotope of nitrogen with mass 15
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 15N, 
  - N-15, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3271953 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_125a4865

[]{#tin-115}

###  tin-115
- **Definition**: Isotope of tin with mass 115
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 115Sn, 
  - Sn-115, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3039718 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ab1de480

[]{#chlorine-37}

###  chlorine-37
- **Definition**: Isotope of chlorine with mass 37
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 37Cl, 
  - Cl-37, 
- **Matches:**
  - http://www.wikidata.org/entity/Q5102949 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_de66e623

[]{#strontium-87}

###  strontium-87
- **Definition**: Isotope of strontium with mass 87
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 87Sr, 
  - Sr-87, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4300037 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_81d0af6d

[]{#ruthenium-102}

###  ruthenium-102
- **Definition**: Isotope of ruthenium with mass 102
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 102Ru, 
  - Ru-102, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3221068 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2dd4c061

[]{#arsenic-75}

###  arsenic-75
- **Definition**: Isotope of arsenic with mass 75
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 75As, 
  - As-75, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4942137 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7a39fb20

[]{#ruthenium-99}

###  ruthenium-99
- **Definition**: Isotope of ruthenium with mass 99
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 99Ru, 
  - Ru-99, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3190653 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d79ce101

[]{#xenon-126}

###  xenon-126
- **Definition**: Isotope of xenon with mass 126
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 126Xe, 
  - Xe-126, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3134801 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1c0470f4

[]{#molybdenum-95}

###  molybdenum-95
- **Definition**: Isotope of molybdenum with mass 95
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 95Mo, 
  - Mo-95, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3355387 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_24416eb2

[]{#tellurium-124}

###  tellurium-124
- **Definition**: Isotope of tellurium with mass 124
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 124Te, 
  - Te-124, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4993070 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_13a011a4

[]{#molybdenum-92}

###  molybdenum-92
- **Definition**: Isotope of molybdenum with mass 92
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 92Mo, 
  - Mo-92, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4499982 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7e6f913e

[]{#tin-117}

###  tin-117
- **Definition**: Isotope of tin with mass 117
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 117Sn, 
  - Sn-117, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4970255 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ad3cdb0f

[]{#tungsten-182}

###  tungsten-182
- **Definition**: Isotope of tungsten with mass 182
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 182W, 
  - W-182, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882864 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6d51b4ba

[]{#scandium-45}

###  scandium-45
- **Definition**: Isotope of scandium with mass 45
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 45Sc, 
  - Sc-45, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1975917 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7f5e3dac

[]{#rhenium-185}

###  rhenium-185
- **Definition**: Isotope of rhenium with mass 185
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 185Re, 
  - Re-185, 
- **Matches:**
  - http://www.wikidata.org/entity/Q18882926 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4c5b0564

[]{#neon-20}

###  neon-20
- **Definition**: Isotope of neon with mass 20
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 20Ne, 
  - Ne-20, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1956685 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bcf548a3

[]{#neon-22}

###  neon-22
- **Definition**: Isotope of neon with mass 22
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 22Ne, 
  - Ne-22, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2021125 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_99093f03

[]{#palladium-104}

###  palladium-104
- **Definition**: Isotope of palladium with mass 104
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 104Pd, 
  - Pd-104, 
- **Matches:**
  - http://www.wikidata.org/entity/Q1978569 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9a582b93

[]{#nickel-58}

###  nickel-58
- **Definition**: Isotope of nickel with mass 58
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 58Ni, 
  - Ni-58, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2424204 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d721ab60

[]{#ruthenium-100}

###  ruthenium-100
- **Definition**: Isotope of ruthenium with mass 100
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 100Ru, 
  - Ru-100, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2511176 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_67749cc6

[]{#krypton-86}

###  krypton-86
- **Definition**: Isotope of krypton with mass 86
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 86Kr, 
  - Kr-86, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2195058 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_17ac3728

[]{#molybdenum-97}

###  molybdenum-97
- **Definition**: Isotope of molybdenum with mass 97
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 97Mo, 
  - Mo-97, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2690215 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee504e86

[]{#selenium-77}

###  selenium-77
- **Definition**: Isotope of selenium with mass 77
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 77Se, 
  - Se-77, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2433972 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_79948193

[]{#oxygen-16}

###  oxygen-16
- **Definition**: Isotope of oxygen with mass 16
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 16O, 
  - O-16, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2309203 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_57a4ad83

[]{#boron-10}

###  boron-10
- **Definition**: Isotope of boron with mass 10
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - B-10, 
  - 10B, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2437314 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6562bc02

[]{#selenium-76}

###  selenium-76
- **Definition**: Isotope of selenium with mass 76
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 76Se, 
  - Se-76, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2533598 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e4d0a232

[]{#tellurium-120}

###  tellurium-120
- **Definition**: Isotope of tellurium with mass 120
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 120Te, 
  - Te-120, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2538285 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_19df9c97

[]{#palladium-105}

###  palladium-105
- **Definition**: Isotope of palladium with mass 105
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 105Pd, 
  - Pd-105, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2692839 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b9836a69

[]{#sulfur-36}

###  sulfur-36
- **Definition**: Isotope of sulphur with mass 36
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 36S, 
  - S-36, 
  - sulphur-36, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2881932 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bf26bf88

[]{#copper-65}

###  copper-65
- **Definition**: Isotope of copper with mass 65
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 65Cu, 
  - Cu-65, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2557191 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9516cfd3

[]{#boron-11}

###  boron-11
- **Definition**: Isotope of boron with mass 11
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - B-11, 
  - 11B, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2659502 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_14290b2e

[]{#nickel-61}

###  nickel-61
- **Definition**: Isotope of nickel with mass 61
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 61Ni, 
  - Ni-61, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2468639 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7363d301

[]{#sulfur-32}

###  sulfur-32
- **Definition**: Isotope of sulphur with mass 32
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - S-32, 
  - 32S, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2375775 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_97fe135a

[]{#ruthenium-96}

###  ruthenium-96
- **Definition**: Isotope of ruthenium with mass 96
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 96Ru, 
  - Ru-96, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2251024 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_badf250e

[]{#titanium-47}

###  titanium-47
- **Definition**: Isotope of titanium with mass 47
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 47Ti, 
  - Ti-47, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2484855 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a3d8b8b4

[]{#neon-21}

###  neon-21
- **Definition**: Isotope of neon with mass 21
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 21Ne, 
  - Ne-21, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2862844 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_56164ad8

[]{#barium-138}

###  barium-138
- **Definition**: Isotope of barium with mass 138
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 138Ba, 
  - Ba-138, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2409784 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_478c47fa

[]{#gadolinium-155}

###  gadolinium-155
- **Definition**: Isotope of gadolinium with mass 155
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 155Gd, 
  - Gd-155, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2972794 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_be2ddeb7

[]{#antimony-123}

###  antimony-123
- **Definition**: Isotope of antimony with mass 123
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 123Sb, 
  - Sb-123, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2297512 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cd03b20f

[]{#neodymium-143}

###  neodymium-143
- **Definition**: Isotope of neodymium with mass 143
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 143Nd, 
  - Nd-143, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2064444 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_204ffd92

[]{#bromine-79}

###  bromine-79
- **Definition**: Isotope of bromine with mass 79
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 79Br, 
  - Br-79, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2311128 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3bc6fb7b

[]{#tin-119}

###  tin-119
- **Definition**: Isotope of tin with mass 119
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 119Sn, 
  - Sn-119, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2140731 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_8f7ae05e

[]{#potassium-41}

###  potassium-41
- **Definition**: Isotope of potassium with mass 41
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - K-41, 
  - 41K, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2956910 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b54d2b45

[]{#germanium-70}

###  germanium-70
- **Definition**: Isotope of germanium with mass 70
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 70Ge, 
  - Ge-70, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2674362 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a53bc3c5

[]{#barium-136}

###  barium-136
- **Definition**: Isotope of barium with mass 136
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 136Ba, 
  - Ba-136, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2449314 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dd1bd88d

[]{#indium-113}

###  indium-113
- **Definition**: Isotope of indium with mass 113
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 113In, 
  - In-113, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2322760 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cbd4ebe9

[]{#gallium-71}

###  gallium-71
- **Definition**: Isotope of gallium with mass 71
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 71Ga, 
  - Ga-71, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2311889 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f45079c8

[]{#palladium-106}

###  palladium-106
- **Definition**: Isotope of palladium with mass 106
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 106Pd, 
  - Pd-106, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2541204 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_63bcd4be

[]{#magnesium-25}

###  magnesium-25
- **Definition**: Isotope of magnesium with mass 25
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 25Mg, 
  - Mg-25, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2796325 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1d718f7e

[]{#neodymium-145}

###  neodymium-145
- **Definition**: Isotope of neodymium with mass 145
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 145Nd, 
  - Nd-145, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2198672 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_09489d52

[]{#fluorine-19}

###  fluorine-19
- **Definition**: Isotope of fluorine with mass 19
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - F-19, 
  - 19F, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2257946 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b05b6ea8

[]{#titanium-48}

###  titanium-48
- **Definition**: Isotope of titanium with mass 48
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 48Ti, 
  - Ti-48, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2467450 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_01d0f1ce

[]{#tellurium-125}

###  tellurium-125
- **Definition**: Isotope of tellurium with mass 125
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 125Te, 
  - Te-125, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2480123 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b60f79de

[]{#barium-134}

###  barium-134
- **Definition**: Isotope of barium with mass 134
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 134Ba, 
  - Ba-134, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2538685 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f3e7c5c2

[]{#cadmium-110}

###  cadmium-110
- **Definition**: Isotope of cadmium with mass 110
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 110Cd, 
  - Cd-110, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2549993 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6fdabf24

[]{#rubidium-85}

###  rubidium-85
- **Definition**: Isotope of rubidium with mass 85
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 85Rb, 
  - Rb-85, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2171949 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a1037c56

[]{#chlorine-35}

###  chlorine-35
- **Definition**: Isotope of chlorine with mass 35
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 35Cl, 
  - Cl-35, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2783861 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_37007611

[]{#niobium-93}

###  niobium-93
- **Definition**: Isotope of niobium with mass 93
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 93Nb, 
  - Nb-93, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2319025 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4314df1f

[]{#tin-114}

###  tin-114
- **Definition**: Isotope of tin with mass 114
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 114Sn, 
  - Sn-114, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2191216 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_aa3c7724

[]{#ruthenium-98}

###  ruthenium-98
- **Definition**: Isotope of ruthenium with mass 98
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 98Ru, 
  - Ru-98, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2476375 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_02cd39b8

[]{#titanium-50}

###  titanium-50
- **Definition**: Isotope of titanium with mass 50
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 50Ti, 
  - Ti-50, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2269284 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a4c7629b

[]{#gadolinium-158}

###  gadolinium-158
- **Definition**: Isotope of gadolinium with mass 158
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 158Gd, 
  - Gd-158, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2237256 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0fcf74f2

[]{#nickel-62}

###  nickel-62
- **Definition**: Isotope of nickel with mass 62
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 62Ni, 
  - Ni-62, 
- **Matches:**
  - http://www.wikidata.org/entity/Q284149 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cecc8f83

[]{#germanium-73}

###  germanium-73
- **Definition**: Isotope of germanium with mass 73
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 73Ge, 
  - Ge-73, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2437511 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_edb8fb3e

[]{#chromium-54}

###  chromium-54
- **Definition**: Isotope of chromium with mass 54
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 54Cr, 
  - Cr-54, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2239560 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_220f23dc

[]{#palladium-110}

###  palladium-110
- **Definition**: Isotope of palladium with mass 110
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 110Pd, 
  - Pd-110, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2890340 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cbf072fd

[]{#calcium-44}

###  calcium-44
- **Definition**: Isotope of calcium with mass 44
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 44Ca, 
  - Ca-44, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3027367 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b495ff08

[]{#xenon-130}

###  xenon-130
- **Definition**: Isotope of xenon with mass 130
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 130Xe, 
  - Xe-130, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2622312 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_86c5d1ff

[]{#strontium-84}

###  strontium-84
- **Definition**: Isotope of strontium with mass 84
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 84Sr, 
  - Sr-84, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2226267 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a92206d6

[]{#praseodymium-141}

###  praseodymium-141
- **Definition**: Isotope of praseodymium with mass 141
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 141Pr, 
  - Pr-141, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2496517 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_89205aa5

[]{#sodium-23}

###  sodium-23
- **Definition**: Isotope of sodium with mass 23
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 23Na, 
  - Na-23, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2265714 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_64153bb9

[]{#yttrium-89}

###  yttrium-89
- **Definition**: Isotope of yttrium with mass 89
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 89Y, 
  - Y-89, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2581836 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6e5177e2

[]{#krypton-80}

###  krypton-80
- **Definition**: Isotope of krypton with mass 80
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 80Kr, 
  - Kr-80, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2071481 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2fedcdf0

[]{#titanium-46}

###  titanium-46
- **Definition**: Isotope of titanium with mass 46
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 46Ti, 
  - Ti-46, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2694202 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7fad80a2

[]{#silicon-28}

###  silicon-28
- **Definition**: Isotope of silicon with mass 28
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 28Si, 
  - Si-28, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2236831 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_718e4614

[]{#titanium-49}

###  titanium-49
- **Definition**: Isotope of titanium with mass 49
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 49Ti, 
  - Ti-49, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2482282 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_246c1972

[]{#krypton-84}

###  krypton-84
- **Definition**: Isotope of aluminium with mass 84
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 84Kr, 
  - Kr-84, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2163590 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_c3037190

[]{#magnesium-24}

###  magnesium-24
- **Definition**: Isotope of magnesium with mass 24
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 24Mg, 
  - Mg-24, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2096096 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4669d0d6

[]{#lanthanum-139}

###  lanthanum-139
- **Definition**: Isotope of lanthanum with mass 139
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 139La, 
  - La-139, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2424900 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2a8d2d0b

[]{#krypton-82}

###  krypton-82
- **Definition**: Isotope of krypton with mass 82
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 82Kr, 
  - Kr-82, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2558547 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_059f31a1

[]{#palladium-102}

###  palladium-102
- **Definition**: Isotope of palladium with mass 102
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 102Pd, 
  - Pd-102, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2177150 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b0c56b41

[]{#terbium-159}

###  terbium-159
- **Definition**: Isotope of terbium with mass 159
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 159Tb, 
  - Tb-159, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2554426 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f4c7203f

[]{#bromine-81}

###  bromine-81
- **Definition**: Isotope of bromine with mass 81
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 81Br, 
  - Br-81, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2342633 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0442fdbb

[]{#iron-58}

###  iron-58
- **Definition**: Isotope of iron with mass 58
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 58Fe, 
  - Fe-58, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2704780 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_191eb426

[]{#caesium-133}

###  caesium-133
- **Definition**: Isotope of caesium with mass 133
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 133Cs, 
  - Cs-133, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2327948 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2d6e603e

[]{#zirconium-92}

###  zirconium-92
- **Definition**: Isotope of zirconium with mass 92
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 92Zr, 
  - Zr-92, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2706395 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_9e42ffdb

[]{#calcium-42}

###  calcium-42
- **Definition**: Isotope of calcium with mass 42
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 42Ca, 
  - Ca-42, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2728105 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_75e2c4b9

[]{#xenon-132}

###  xenon-132
- **Definition**: Isotope of xenon with mass 132
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 132Xe, 
  - Xe-132, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2125594 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0180033a

[]{#germanium-76}

###  germanium-76
- **Definition**: Isotope of germanium with mass 76
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 76Ge, 
  - Ge-76, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2190009 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_834c5313

[]{#selenium-74}

###  selenium-74
- **Definition**: Isotope of selenium with mass 74
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 74Se, 
  - Se-74, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2806682 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0777fed8

[]{#barium-130}

###  barium-130
- **Definition**: Isotope of barium with mass 130
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 130Ba, 
  - Ba-130, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2574790 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ebf7d20a

[]{#zirconium-90}

###  zirconium-90
- **Definition**: Isotope of zirconium with mass 90
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 90Zr, 
  - Zr-90, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2090546 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_40f5aec8

[]{#xenon-131}

###  xenon-131
- **Definition**: Isotope of xenon with mass 131
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 131Xe, 
  - Xe-131, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2501965 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d1256d1b

[]{#samarium-154}

###  samarium-154
- **Definition**: Isotope of samarium with mass 154
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 154Sm, 
  - Sm-154, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2402263 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_130a9e88

[]{#ruthenium-104}

###  ruthenium-104
- **Definition**: Isotope of ruthenium with mass 104
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 104Ru, 
  - Ru-104, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2705828 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_111f7fe3

[]{#palladium-108}

###  palladium-108
- **Definition**: Isotope of palladium with mass 108
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 108Pd, 
  - Pd-108, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2611037 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b7efcb48

[]{#gadolinium-157}

###  gadolinium-157
- **Definition**: Isotope of gadolinium with mass 157
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 157Gd, 
  - Gd-157, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2226266 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_010322ff

[]{#strontium-86}

###  strontium-86
- **Definition**: Isotope of strontium with mass 86
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 86Sr, 
  - Sr-86, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2267980 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_668a66e9

[]{#iron-54}

###  iron-54
- **Definition**: Isotope of iron with mass 54
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 54Fe, 
  - Fe-54, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2696892 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3d11ce8b

[]{#germanium-74}

###  germanium-74
- **Definition**: Isotope of germanium with mass 74
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 74Ge, 
  - Ge-74, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2531608 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_bfb2f06d

[]{#phosphorus-31}

###  phosphorus-31
- **Definition**: Isotope of phosphorus with mass 31
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - P-31, 
  - 31P, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2459552 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0bb6a74b

[]{#zinc-67}

###  zinc-67
- **Definition**: Isotope of zinc with mass 67
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 67Zn, 
  - Zn-67, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2423143 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5134414b

[]{#selenium-80}

###  selenium-80
- **Definition**: Isotope of selenium with mass 80
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 80Se, 
  - Se-80, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2387529 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_48eeee1c

[]{#samarium-152}

###  samarium-152
- **Definition**: Isotope of samarium with mass 152
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 152Sm, 
  - Sm-152, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2288129 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1bb0d387

[]{#nickel-60}

###  nickel-60
- **Definition**: Isotope of nickel with mass 60
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 60Ni, 
  - Ni-60, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2103496 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d71d09a1

[]{#xenon-129}

###  xenon-129
- **Definition**: Isotope of xenon with mass 129
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 129Xe, 
  - Xe-129, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2388818 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_252ecb30

[]{#calcium-43}

###  calcium-43
- **Definition**: Isotope of calcium with mass 43
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 43Ca, 
  - Ca-43, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2103298 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_db747aa1

[]{#argon-38}

###  argon-38
- **Definition**: Isotope of argon with mass 38
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 38Ar, 
  - Ar-38, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2801372 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4c2e56ad

[]{#tin-120}

###  tin-120
- **Definition**: Isotope of tin with mass 120
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 120Sn, 
  - Sn-120, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2347800 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_0ccb3401

[]{#cadmium-111}

###  cadmium-111
- **Definition**: Isotope of cadmium with mass 111
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 111Cd, 
  - Cd-111, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2437333 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e37552a3

[]{#zirconium-91}

###  zirconium-91
- **Definition**: Isotope of zirconium with mass 91
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 91Zr, 
  - Zr-91, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2328556 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_21d6e5be

[]{#gadolinium-154}

###  gadolinium-154
- **Definition**: Isotope of gadolinium with mass 154
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 154Gd, 
  - Gd-154, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2175390 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6be62267

[]{#tin-118}

###  tin-118
- **Definition**: Isotope of tin with mass 118
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 118Sn, 
  - Sn-118, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2122600 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a6746e4c

[]{#beryllium-9}

###  beryllium-9
- **Definition**: Isotope of beryllium with mass 9
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 9Be, 
  - Be-9, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3010030 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_84430359

[]{#aluminium-27}

###  aluminium-27
- **Definition**: Isotope of aluminium with mass 27
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 27Al, 
  - Al-27, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2225512 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a9212ed3

[]{#rhodium-103}

###  rhodium-103
- **Definition**: Isotope of rhodium with mass 103
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 103Rh, 
  - Rh-103, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2672056 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a274048b

[]{#cerium-140}

###  cerium-140
- **Definition**: Isotope of cerium with mass 140
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 140Ce, 
  - Ce-140, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2646578 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_aec1e5c8

[]{#selenium-82}

###  selenium-82
- **Definition**: Isotope of selenium with mass 82
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 82Se, 
  - Se-82, 
- **Matches:**
  - http://www.wikidata.org/entity/Q2290353 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3cdb41fa

[]{#strontium-88}

###  strontium-88
- **Definition**: Isotope of strontium with mass 88
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 88Sr, 
  - Sr-88, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3355112 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_4b9b91b6

[]{#tellurium-122}

###  tellurium-122
- **Definition**: Isotope of tellurium with mass 122
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 122Te, 
  - Te-122, 
- **Matches:**
  - http://www.wikidata.org/entity/Q5315292 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_6de2e4f0

[]{#helium-3}

###  helium-3
- **Definition**: Isotope of helium with mass 3
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 3He, 
  - He-3, 
- **Matches:**
  - http://www.wikidata.org/entity/Q533498 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_17f13010

[]{#iodine-127}

###  iodine-127
- **Definition**: Isotope of iodine with mass 127
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 127I, 
  - I-127, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3069233 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d5f54116

[]{#silver-107}

###  silver-107
- **Definition**: Isotope of silver with mass 107
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 107Ag, 
  - Ag-107, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3204948 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_fac64e23

[]{#chromium-52}

###  chromium-52
- **Definition**: Isotope of chromium with mass 52
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 52Cr, 
  - Cr-52, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4469260 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_cf33d726

[]{#cobalt-59}

###  cobalt-59
- **Definition**: Isotope of cobalt with mass 59
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 59Co, 
  - Co-59, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4350852 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_565bd3cd

[]{#gallium-69}

###  gallium-69
- **Definition**: Isotope of gallium with mass 69
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 69Ga, 
  - Ga-69, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4738844 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d9877e77

[]{#neodymium-148}

###  neodymium-148
- **Definition**: Isotope of neodymium with mass 148
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 148Nd, 
  - Nd-148, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4990557 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_7dfdbf8b

[]{#silicon-29}

###  silicon-29
- **Definition**: Isotope of silicon with mass 29
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 29Si, 
  - Si-29, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3410389 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_d86e5206

[]{#oxygen-17}

###  oxygen-17
- **Definition**: Isotope of oxygen with mass 17
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 17O, 
  - O-17, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3359113 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_265f3fdc

[]{#zirconium-94}

###  zirconium-94
- **Definition**: Isotope of zirconium with mass 94
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 94Zr, 
  - Zr-94, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4808461 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_1c1e8e64

[]{#barium-137}

###  barium-137
- **Definition**: Isotope of barium with mass 137
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 137Ba, 
  - Ba-137, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4734760 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_e0619307

[]{#copper-63}

###  copper-63
- **Definition**: Isotope of copper with mass 63
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 63Cu, 
  - Cu-63, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3031418 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_dc42718a

[]{#neodymium-142}

###  neodymium-142
- **Definition**: Isotope of neodymium with mass 142
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 142Nd, 
  - Nd-142, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3193312 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_ba468a55

[]{#zinc-66}

###  zinc-66
- **Definition**: Isotope of zinc with mass 66
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 66Zn, 
  - Zn-66, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4046116 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_45767302

[]{#oxygen-18}

###  oxygen-18
- **Definition**: Isotope of oxygen with mass 18
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 18O, 
  - O-18, 
- **Matches:**
  - http://www.wikidata.org/entity/Q662269 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b248ae80

[]{#barium-135}

###  barium-135
- **Definition**: Isotope of barium with mass 135
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 135Ba, 
  - Ba-135, 
- **Matches:**
  - http://www.wikidata.org/entity/Q3192465 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_b1146739

[]{#zinc-68}

###  zinc-68
- **Definition**: Isotope of zinc with mass 68
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - Zn-68, 
  - 68Zn, 
- **Matches:**
  - http://www.wikidata.org/entity/Q8072263 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_255b0315

[]{#gadolinium-156}

###  gadolinium-156
- **Definition**: Isotope of gadolinium with mass 156
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 156Gd, 
  - Gd-156, 
- **Matches:**
  - http://www.wikidata.org/entity/Q4505367 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_2ce9bcc9


[]{#production-process}

##  production process
- **Definition**: The process by which a material was modified as part
of the production process.
- **Matches:**
  - https://www.wikidata.org/wiki/Q1408286 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_25f0249a

[]{#unknown}

###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`site type`](#site-type)
  - [`discovery activity`](#discovery-activity)
  - [`context type`](#context-type)
  - [`sample housing`](#sample-housing)
  - [`object material`](#object-material)
  - [`authenticity`](#authenticity)
  - [`sample material`](#sample-material)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`sample state`](#sample-state)
  - [`reference material`](#reference-material)
  - [`alteration extent`](#alteration-extent)
  - [`production context`](#production-context)
  - [`recycling indicator`](#recycling-indicator)
  - [`corrosion extent`](#corrosion-extent)
  - [`glass component`](#glass-component)
  - [`compound type`](#compound-type)
  - [`compound origin`](#compound-origin)
  - [`pigment component`](#pigment-component)
  - [`alteration process`](#alteration-process)
  - [`sample access`](#sample-access)
  - [`production process`](#production-process)
- **Matches:**
  - https://www.wikidata.org/wiki/Q24238356 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_3e4fdfbb

[]{#other}

###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`object material`](#object-material)
  - [`reference material`](#reference-material)
  - [`analytical instrument`](#analytical-instrument)
  - [`alteration process`](#alteration-process)
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_ebc979f8

[]{#absorption}

###  absorption
- **Definition**: The material is exposed to another material from
which a specific compound or the entire material gets dissolved into
the material.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300053004 (exactMatch)
  - https://www.wikidata.org/wiki/Q332828 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_31f5fc72

[]{#weathering}

###  weathering
- **Definition**: The material was exposed to react with its
environment and meteoric water.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300226583 (closeMatch)
  - http://vocab.getty.edu/aat/300054115 (exactMatch)
  - https://www.wikidata.org/wiki/Q179177 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_f37a4790

[]{#acid-reaction}

###  acid reaction
- **Definition**: The partial or complete dissolution of all parts of
a material when exposed to acids.
- **Child of**:
  - [`production process`](#production-process)
- **Concept URI:** http://vocab.terralid.org#c_6237ab6b

[]{#leaching}

###  leaching
- **Definition**: The dissolution of specific parts of a material by
covering or submerging it in a solution such as an acid, solvent, or
water.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300053761 (exactMatch)
  - https://www.wikidata.org/wiki/Q1483184 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_5916e942

[]{#grinding}

###  grinding
- **Definition**: The material was mechanically reduced to smaller
particles by applying friction.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300053090 (exactMatch)
  - https://www.wikidata.org/wiki/Q26882416 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_a1b2b905

[]{#heating}

###  heating
- **Definition**: The material was exposed to high temperatures.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - http://vocab.getty.edu/aat/300053885 (exactMatch)
  - https://www.wikidata.org/wiki/Q4311765 (exactMatch)
- **Concept URI:** http://vocab.terralid.org#c_22488ba9


[]{#pigment-name}

##  pigment name
- **Other Properties:**
  - **note**: 
This vocabulary is based on the pigments listed in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_38acd1d1

[]{#bassanite}

###  bassanite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.xH2O, where x ~ 0.5-0.8.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium sulfate, 
  - CaSO4.xH2O, where x ~ 0.5-0.8, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q408259 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_727afc46

[]{#synthetic-lead-carbonate}

###  synthetic lead carbonate
- **Definition**: A Pb-based inorganic and synthetic pigment with the
chemical formula PbCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q411260 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a9faa87b

[]{#lead-white}

###  lead white
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula 2PbCO3.Pb(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - lead carbonate hydroxide, 
  - 2PbCO3.Pb(OH)2, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q116470614 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_34bc82ee

[]{#lead-carbonate-hydroxide}

###  lead carbonate hydroxide
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula Pb10(CO3)6O(OH)6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - plumbonacrite type, 
  - Pb10(CO3)6O(OH)6, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q4338141 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0d5c40fd

[]{#lead-sulfate-(other-types)}

###  lead sulfate (other types)
- **Definition**: A Pb-based inorganic and natural pigment made of
lead sulfides other than PbSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_5d066542

[]{#cassiterite}

###  cassiterite
- **Definition**: A Sn-based inorganic and natural pigment with the
chemical formula SnO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SnO2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q191222 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a2fb615f

[]{#rutile}

###  rutile
- **Definition**: A Ti-based inorganic and natural pigment with the
chemical formula TiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - TiO2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q320603 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_523cbfab

[]{#zinc-sulfide}

###  zinc sulfide
- **Definition**: A Zn-based inorganic and natural pigment with the
chemical formula ZnS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ZnS
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q204952 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_03a70634

[]{#zinc-sulfate-heptahydrate}

###  zinc sulfate heptahydrate
- **Definition**: A Zn-based inorganic and natural pigment with the
chemical formula ZnSO4.7H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ZnSO4.7H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q27114864 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8027db1a

[]{#quartz}

###  quartz
- **Definition**: A Si-based inorganic and natural pigment with the
chemical formula SiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q43010 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a1cb5378

[]{#diatomite}

###  diatomite
- **Definition**: A Si-based inorganic and natural pigment made of
amorphous SiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2(am)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3706845 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e83576ca

[]{#glass}

###  glass
- **Definition**: A Si-based inorganic and natural pigment made of
mixture of amorphous SiO2 and other phases.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2(am) with other included phases
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q11469 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c095a984

[]{#pumice}

###  pumice
- **Definition**: A Si-based inorganic and natural pigment made of
mixture of amorphous SiO2 and other phases.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2(am) with other included phases
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q25931026 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_5af4a831

[]{#talc}

###  talc
- **Definition**: A Mg-Si-based inorganic and natural pigment with the
chemical formula Mg3Si4O10(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Mg3Si4O10(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q134583 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_08bba0d7

[]{#palygorskite}

###  palygorskite
- **Definition**: A Mg-Al-Si based inorganic and natural clay mineral
pigment from the palygorskite group with the chemical formula
(Mg,Al)2Si4O10(OH).4H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (Mg,Al)2Si4O10(OH).4H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q414065 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c81f28a

[]{#kaolinite}

###  kaolinite
- **Definition**: A Al-Si-based inorganic and natural clay mineral
pigment from the kaolinite group with the chemical formula
Al2Si2O5(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2Si2O5(OH)4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q20406255 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a34b704f

[]{#nacrite}

###  nacrite
- **Definition**: A Al-Si-based inorganic and natural clay mineral
pigment from the kaolinite group with the chemical formula
Al2Si2O5(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2Si2O5(OH)4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q418903 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_39f96274

[]{#montmorillonite}

###  montmorillonite
- **Definition**: A Mg-Al-Si based inorganic and natural clay mineral
pigment from the smectite group with the chemical formula
(Na,Ca)0.3(Al,Mg)2Si4O10(OH)2.nH2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (Na,Ca)0.3(Al,Mg)2Si4O10(OH)2.nH2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q422131 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_488d8f86

[]{#nontronite}

###  nontronite
- **Definition**: A Fe-Al-Si based inorganic and natural clay mineral
pigment from the smectite group with the chemical formula
Na0.3Fe3+2(Si,Al)4O10(OH)2.nH2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Na0.3Fe3+2(Si,Al)4O10(OH)2.nH2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q420274 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2cd83a62

[]{#vermiculite-group-clay-minerals}

###  vermiculite group clay minerals
- **Definition**: A Fe-Al-Si based inorganic and natural clay mineral
pigments from the vermiculite group with the chemical formula
(Mg,Fe2+,Al)3(Al,Si)4O10(OH)2.4H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (Mg,Fe2+,Al)3(Al,Si)4O10(OH)2.4H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q194358 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a24984db

[]{#serpentine-group-clay-minerals}

###  serpentine group clay minerals
- **Definition**: Complex inorganic and natural clay mineral pigments
from the serpentinite group.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q335249 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_9591f687

[]{#starch}

###  starch
- **Definition**: A Complex inorganic and natural pigment made of a
complex based on C6H10O5.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - C6H10O5-based complex
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q41534 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e5e5a283

[]{#red-lake-pigments}

###  red lake pigments
- **Definition**: A Metal-organic-complex inorganic and natural
pigment with a complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_87413a8f

[]{#yellow-lake-pigments}

###  yellow lake pigments
- **Definition**: A Metal-organic-complex inorganic and natural
pigment with a complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_7380fd9d

[]{#red-ochre}

###  red ochre
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1054292 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_64214b59

[]{#yellow-ochre}

###  yellow ochre
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3348755 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_813e37ee

[]{#brown-ochre-and-burnt-sienna}

###  brown ochre and burnt sienna
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q110645329 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_b3250fc4

[]{#umbers-and-wads}

###  umbers and wads
- **Definition**: A Fe-Mn-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q901731 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_1546d26c

[]{#green-earths}

###  green earths
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1552133 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e2f4e9bd

[]{#feldspar-minerals}

###  feldspar minerals
- **Definition**: A group of inorganic and natural pigments.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q170258 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_b9f1d4d2

[]{#feldspathoid-minerals}

###  feldspathoid minerals
- **Definition**: A group of inorganic and natural pigment.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1006122 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_86f42d6e

[]{#mica-group-minerals}

###  mica group minerals
- **Definition**: A group of inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q114675 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_5c078f15

[]{#asbestiform-minerals}

###  asbestiform minerals
- **Definition**: A group of inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q4803674 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ab399c01

[]{#maya-blue}

###  Maya blue
- **Definition**: A Complex synthetic pigment based on an indigo-
paligorskite complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - indigo-paligorskite complex
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q901499 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_159b6705

[]{#manganese-oxides}

###  manganese oxides
- **Definition**: A Mn-based inorganic and natural pigment made of
various manganese oxides.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q110921543 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d1315130

[]{#pyrite}

###  pyrite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula FeS2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - FeS2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q50769 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8c5cddc6

[]{#magnetite}

###  magnetite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula Fe2+Fe3+2O4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Fe2+Fe3+2O4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q181395 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2bd15e2a

[]{#bismuthinite}

###  bismuthinite
- **Definition**: A Bi-based inorganic and natural pigment with the
chemical formula Bi2S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Bi2S3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q419292 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ffbcca13

[]{#stibnite}

###  stibnite
- **Definition**: A Sb-based inorganic and natural pigment with the
chemical formula Sb2S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Sb2S3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q421831 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_7a2bfe0e

[]{#galena}

###  galena
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula PbS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbS
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q37559 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_3f1a6b61

[]{#plattnerite}

###  plattnerite
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula PbO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbO2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2738313 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e9ae944d

[]{#copper(ii)-oxide}

###  copper(II) oxide
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula CuO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CuO, 
  - tenorite type and tenorite, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q421787 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ce78bc60

[]{#coal}

###  coal
- **Definition**: An organic and natural pigment based on a chemical
complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - anthracite and cannel types
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q24489 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_976245b6

[]{#asphalt}

###  asphalt
- **Definition**: An inorganic and natural pigment based on a chemical
complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q167510 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_68d45411

[]{#vandyke-brown}

###  Vandyke brown
- **Definition**: An organic and natural pigment based on a chemical
complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Van Dyke brown
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3518638 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6973d71d

[]{#sepia}

###  sepia
- **Definition**: A C-Organic-based inorganic and natural pigment
based on a chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - bister
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q774061 (closeMatch)
  - https://www.wikidata.org/wiki/Q767608 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_5156c6e4

[]{#flame-carbons}

###  flame carbons
- **Definition**: A C-based inorganic and synthetic pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - carbon-based black
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_eb4c525f

[]{#bone-and-yeast-cokes}

###  bone and yeast cokes
- **Definition**: A C-based inorganic and synthetic pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - carbon-based black
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_d10be7f5

[]{#chars}

###  chars
- **Definition**: A C-based inorganic and natural pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - carbon-based black
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_e7d6bfa2

[]{#graphite}

###  graphite
- **Definition**: A C-based inorganic pigment with the chemical
formula C.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - C
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q5309 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_28a6feab

[]{#copper-hexacyanoferrates}

###  copper hexacyanoferrates
- **Definition**: A Cu-Fe-based inorganic and synthetic pigment with
the chemical formula CuK2Fe(CN)6 or Cu2Fe(CN)6.xH2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2Fe(CN)6.xH2O, 
  - CuK2Fe(CN)6, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_0dc73827

[]{#bismuth}

###  bismuth
- **Definition**: A Bi-based inorganic and natural pigment with the
chemical formula Bi.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Bi
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q942 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_abd27d33

[]{#dragon’s-blood}

###  dragon’s blood
- **Definition**: An organic and natural pigment made of dracorubin,
dracorhodin or derivatives.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - dracorubin, dracorhodin and derivatives
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q421877 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a8e7855c

[]{#turmeric}

###  turmeric
- **Definition**: An organic and natural pigment made of curcumin and
derivatives.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - curcumin and derivatives
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q20730193 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_70e78128

[]{#indian-yellow}

###  Indian yellow
- **Definition**: An organic and natural pigment made of Ca and Mg
euxanthates.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Ca, Mg euxanthates
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q55611196 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_60f19008

[]{#gamboge}

###  gamboge
- **Definition**: An organic and natural pigment made of gambogic acid
or its derivatives.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - gambogic acid and derivatives
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q909115 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_caa85d4c

[]{#mosaic-gold}

###  mosaic gold
- **Definition**: A Sn-based inorganic and synthetic pigment with the
chemical formula SnS2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Tin(IV) sulfide, 
  - SnS2, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q693323 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_00240e2a

[]{#sulfur}

###  sulfur
- **Definition**: A S-based inorganic and natural pigment with the
chemical formula S(am) and S8.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - S(am) and S8
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q682 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_272d1738

[]{#cobalt-yellow}

###  cobalt yellow
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula K3-xNax[Co(NO2)6].nH2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (K, Na) hexanitrocobalt(III), 
  - K3-xNax[Co(NO2)6].nH2O, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q4134928 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_dbdef691

[]{#metacinnabar}

###  metacinnabar
- **Definition**: A Hg-based inorganic and natural pigment with the
chemical formula β-HgS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - β-HgS
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q415961 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_7de3a131

[]{#vermillion}

###  vermillion
- **Definition**: A Hg-based inorganic and synthetic pigment with the
chemical formula α-HgS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - synthetic mercury(II) sulfide, 
  - α-HgS, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q104614 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_1291f4c0

[]{#cinnabar}

###  cinnabar
- **Definition**: A Hg-based inorganic and natural pigment with the
chemical formula α-HgS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - α-HgS, 
  - mercury(II) sulfide, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q104614 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d0ab0694

[]{#cuprite}

###  cuprite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2O, 
  - copper(I) oxide, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q407335 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_84df1f14

[]{#red-lead}

###  red lead
- **Definition**: A Pb-based inorganic pigment with the chemical
formula Pb2+2Pb4+O4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Minium, 
  - lead(II, IV) oxide, 
  - Pb2+2Pb4+O4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q17141476 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_287b8eaf

[]{#lead-chromate-sulfate}

###  lead chromate sulfate
- **Definition**: A Pb-Cr-based inorganic pigment with the chemical
formula PbCrO4.xPbSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbCrO4.xPbSO4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_bad809ea

[]{#lead-chromate-oxide}

###  lead chromate oxide
- **Definition**: A Pb-Cr-based inorganic pigment with the chemical
formula Pb2(CrO4)O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - phoenicochroite, 
  - Pb2(CrO4)O, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2738147 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_86d5c260

[]{#chrome-yellow}

###  chrome yellow
- **Definition**: A Pb-Cr-based inorganic pigment with the chemical
formula PbCrO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Lead chromate, 
  - crocoite, 
  - PbCrO4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q422903 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_76870482

[]{#lead-tin-silicon-oxide}

###  lead tin silicon oxide
- **Definition**: A Pb-Sn-based inorganic and synthetic pigment with
the chemical formula Pb(Six,Sn1-x)O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - lead tin yellow type II, 
  - Pb(Six,Sn1-x)O3, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q125731333 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_01593656

[]{#lead-tin-oxide}

###  lead tin oxide
- **Definition**: A Pb-Sn-based inorganic and synthetic pigment with
the chemical formula Pb2SnO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - lead tin yellow, 
  - Pb2SnO4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q883704 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_7d971fe0

[]{#lead-antimony-zinc-oxide}

###  lead antimony zinc oxide
- **Definition**: A Pb-Sb-based inorganic and synthetic pigment with
the chemical formula ~Pb2(Sb,Zn)2O7.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ~Pb2(Sb,Zn)2O7
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_1d78709c

[]{#lead-antimony-tin-oxide}

###  lead antimony tin oxide
- **Definition**: A Pb-Sb-based inorganic and synthetic pigment with
the chemical formula ~Pb2(Sb,Sn)2O7.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ~Pb2(Sb,Sn)2O7
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_e6963953

[]{#naples-yellow}

###  Naples yellow
- **Definition**: A Pb-based inorganic and synthetic pigment with the
chemical formula Pb2Sb2O7.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Lead antimony oxide, 
  - Pb2Sb2O7, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q899295 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0a295fe8

[]{#litharge}

###  litharge
- **Definition**: A Pb-based inorganic pigment with the chemical
formula α-PbO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - α-PbO
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2362697 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f8a16acc

[]{#massicot}

###  massicot
- **Definition**: A Pb-based inorganic pigment with the chemical
formula β-PbO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - β-PbO
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3297608 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8cc93dc4

[]{#turner's-yellow}

###  Turner's yellow
- **Definition**: A Pb-based inorganic and synthetic pigment with the
chemical formula PbCl2.5-7PbO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Lead oxychloride, 
  - C.I. Pigment Yellow 30 , 
  - PbCl2.5-7PbO, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q133256795 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_acadfc5a

[]{#natrojarosite}

###  natrojarosite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula NaFe3(SO4)2(OH)6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - NaFe3(SO4)2(OH)6
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1069438 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c858e62d

[]{#jarosite}

###  jarosite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula KFe3(SO4)2(OH)6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - KFe3(SO4)2(OH)6
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q411168 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_aadde1cf

[]{#lepidocrocite}

###  lepidocrocite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula γ-FeOOH.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - γ-FeOOH
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q410583 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2048807b

[]{#hematite}

###  hematite
- **Definition**: A Fe-based inorganic pigment with the chemical
formula α-Fe2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - α-Fe2O3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q103223 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_7ee5ce6a

[]{#goethite}

###  goethite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula α-FeOOH.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - α-FeOOH
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q189703 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d7955b2c

[]{#pararealgar}

###  pararealgar
- **Definition**: An As-based inorganic and natural pigment with the
chemical formula As4S4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As4S4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1058825 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_5d1e4ab8

[]{#realgar}

###  realgar
- **Definition**: An As-based inorganic and natural pigment with the
chemical formula As4S4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As4S4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q109746 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2c36600a

[]{#orpiment}

###  orpiment
- **Definition**: An As-based inorganic and natural pigment with the
chemical formula As2S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As2S3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83020604 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0874360a

[]{#antimony(iii)-sulfide}

###  antimony(III) sulfide
- **Definition**: A Sb-based inorganic pigment with the chemical
formula Sb2S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Sb2S3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q409041 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8810667b

[]{#indigo}

###  indigo
- **Definition**: An organic and natural pigment with the chemical
formula C16H10N2O2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - C16H10N2O2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q422662 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_fc6e3616

[]{#prussian-blue}

###  prussian blue
- **Definition**: A Fe-based inorganic and synthetic pigment with the
chemical formula Fe4[Fe(CN)6]3.xH2O where x = 14-16 (and
substitutions).
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - hexacyanoferrate(II) compounds, 
  - Fe4[Fe(CN)6]3.xH2O where x = 14-16 (and substitutions), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q421894 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_afeb342a

[]{#chromium-phosphate-hexahydrate}

###  chromium phosphate hexahydrate
- **Definition**: A Cr-based inorganic and natural pigment with the
chemical formula CrPO4.6H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CrPO4.6H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_112626eb

[]{#chromium-oxide-hydrate}

###  chromium oxide hydrate
- **Definition**: A Cr-based inorganic and synthetic pigment with the
chemical formula Cr2O3.2H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - viridian, 
  - Cr2O3.2H2O, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q6163776 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c845ef5

[]{#chromium(iii)-oxide}

###  chromium(III) oxide
- **Definition**: A Cr-based inorganic and synthetic pigment with the
chemical formula Cr2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cr2O3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q407905 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6052da16

[]{#glaucophane}

###  glaucophane
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula Na2(Mg,Fe2+)3Al2Si8O22(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Na2(Mg,Fe2+)3Al2Si8O22(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q413272 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_8fff9159

[]{#chlorite-group-minerals}

###  chlorite group minerals
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula [e.g.: Clinochlore, (Mg,Fe2+)5Al(Si3Al)O10(OH)8].
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - [e.g.: Clinochlore, (Mg,Fe2+)5Al(Si3Al)O10(OH)8]
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q427254 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_30be1f40

[]{#chrysocolla}

###  chrysocolla
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula (Cu,Al)2H2Si2O5(OH)4.xH2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (Cu,Al)2H2Si2O5(OH)4.xH2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q22907242 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_2f6f42e6

[]{#glauconite}

###  glauconite
- **Definition**: A Fe-based inorganic and natural pigment of the
illite clay mineral group with the chemical formula
(K,Na)(Fe3+,Al,Mg)2(Si,Al)4O10(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (K,Na)(Fe3+,Al,Mg)2(Si,Al)4O10(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1552133 (closeMatch)
  - https://www.wikidata.org/wiki/Q423034 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_377e324e

[]{#celadonite}

###  celadonite
- **Definition**: A Fe-based inorganic and natural pigment of the
illite clay mineral group with the chemical formula
K(Mg,Fe2+)(Fe3+,Al)Si4O10(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - K(Mg,Fe2+)(Fe3+,Al)Si4O10(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1552133 (closeMatch)
  - https://www.wikidata.org/wiki/Q425142 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_77bedf08

[]{#aerinite}

###  aerinite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula Ca4(Al,Fe3+,Mg,Fe2+)10Si12O36(CO3).12H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Ca4(Al,Fe3+,Mg,Fe2+)10Si12O36(CO3).12H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q381133 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_27446acf

[]{#copper-citrate}

###  copper citrate
- **Definition**: A Cu-based synthetic pigment with the chemical
formula Cu4[HOC(CH2COO)2(COO)]2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu4[HOC(CH2COO)2(COO)]2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1291820 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c8a0b38f

[]{#gypsum}

###  gypsum
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.2H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium sulfate, 
  - CaSO4.2H2O, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q82658 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_959fe0ea

[]{#carbonate-hydroxylapatite}

###  carbonate hydroxylapatite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula Ca5(PO4,CO3)3(OH).
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Ca5(PO4,CO3)3(OH)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_0f9765a8

[]{#cerussite}

###  cerussite
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula PbCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q409122 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_7971c791

[]{#lead-chloride-hydroxide}

###  lead chloride hydroxide
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula Pb(OH)2.PbCl2, Pb2Cl(O,OH)2-x (where x ~ 0.325) and
others.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Pb(OH)2.PbCl2, Pb2Cl(O,OH)2-x (where x ~ 0.325) and others
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_d5dcb6d8

[]{#anglesite}

###  anglesite
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula PbSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Lead(II) sulfate, 
  - PbSO4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q156526 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_5219129d

[]{#magnesite}

###  magnesite
- **Definition**: A Mg-based inorganic and natural pigment with the
chemical formula MgCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - MgCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q425450 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_bb46e184

[]{#anatase}

###  anatase
- **Definition**: A Ti-based inorganic and natural pigment with the
chemical formula TiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - TiO2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q413357 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a24e7815

[]{#zinc(ii)-oxide}

###  zinc(II) oxide
- **Definition**: A Zn-based inorganic and natural pigment with the
chemical formula ZnO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ZnO
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q190077 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_73cbee47

[]{#anhydrite}

###  anhydrite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium sulfate, 
  - CaSO4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q105439 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_acf85f04

[]{#dolomite}

###  dolomite
- **Definition**: A Ca-Mg-based inorganic and natural pigment with the
chemical formula CaMg(CO3)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaMg(CO3)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q167741 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_9a35c6da

[]{#oyster-shell}

###  oyster shell
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q110619733 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f7844dc4

[]{#eggshell}

###  eggshell
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2731253 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_23185837

[]{#coral}

###  coral
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q171446 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_4a82a3e9

[]{#chalk}

###  chalk
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q183670 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_4b6f93ce

[]{#calcium-carbonate}

###  calcium carbonate
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q23767 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e570ba6a

[]{#aragonite}

###  aragonite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium carbonate, 
  - CaCO3, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q82003566 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6d5cf070

[]{#baryte}

###  baryte
- **Definition**: A Ba-based inorganic and natural pigment with the
chemical formula BaSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Barium sulfate, 
  - BaSO4, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q309038 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_a83e8eaa

[]{#barium-carbonate}

###  barium carbonate
- **Definition**: A Ba-based inorganic and natural pigment with the
chemical formula BaCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - BaCO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q409224 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_9267b7f6

[]{#arsenic(iii)-oxide}

###  arsenic(III) oxide
- **Definition**: A As-based inorganic and natural pigment with the
chemical formula As2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As2O3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q7739 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_00694ff3

[]{#aluminium-hydroxide}

###  aluminium hydroxide
- **Definition**: An Al-based inorganic and natural pigment with the
chemical formula Al(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al(OH)3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q407125 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_1940d870

[]{#aluminium-oxide}

###  aluminium oxide
- **Definition**: An Al-based inorganic and natural pigment with the
chemical formula Al2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2O3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q177342 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ca798b6c

[]{#copper(ii)-acetate-h}

###  copper(II) acetate h
- **Definition**: A Cu-based synthetic pigment with the chemical
formula Cu(CH3COO)2.[Cu(OH)2]4.3H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu(CH3COO)2.[Cu(OH)2]4.3H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83528898 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_1ae29fc6

[]{#copper(ii)-acetate-f}

###  copper(II) acetate f
- **Definition**: A Cu-based synthetic pigment with the chemical
formula Cu(CH3COO)2.H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu(CH3COO)2.H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83528898 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_3cbb9a04

[]{#copper(ii)-acetate-d}

###  copper(II) acetate d
- **Definition**: A Cu-based synthetic pigment with the chemical
formula Cu(CH3COO)2.[Cu(OH)2]3.2H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu(CH3COO)2.[Cu(OH)2]3.2H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83528898 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0e32d3f0

[]{#copper(ii)-acetate-b}

###  copper(II) acetate b
- **Definition**: A Cu-based synthetic pigment with the chemical
formula Cu(CH3COO)2.Cu(OH)2.5H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu(CH3COO)2.Cu(OH)2.5H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83528898 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d27d8cdd

[]{#copper(ii)-acetate-a}

###  copper(II) acetate a
- **Definition**: A Cu-based synthetic pigment with the chemical
formula [Cu(CH3COO)2]2.Cu(OH)2.5H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - [Cu(CH3COO)2]2.Cu(OH)2.5H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q83528898 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_d50a0c1c

[]{#copper-acetate-arsenite}

###  copper acetate arsenite
- **Definition**: A Cu-As-based synthetic pigment with the chemical
formula Cu4(CH3COO)2(AsO2)6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu4(CH3COO)2(AsO2)6
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_2a1c5fe3

[]{#copper-arsenite-group}

###  copper arsenite group
- **Definition**: A group of Cu-As-based synthetic pigments.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q23636739 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c29fdc48

[]{#antlerite}

###  antlerite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu3(SO4)(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu3(SO4)(OH)4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q417254 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_eb9c523c

[]{#brochantite}

###  brochantite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu4(SO4)(OH)6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - copper sulfate hydrate, 
  - Cu4(SO4)(OH)6, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q411036 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_b5df1234

[]{#pseudomalachite}

###  pseudomalachite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu5(PO4)2(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu5(PO4)2(OH)4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2479376 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_c7ff0c22

[]{#paratacamite}

###  paratacamite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2Cl(OH)3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q1057152 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e71b2ebb

[]{#botallackite}

###  botallackite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2Cl(OH)3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q2739239 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_0a8e15d2

[]{#atacamite}

###  atacamite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - copper chloride hydroxide, 
  - Cu2Cl(OH)3, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q409775 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f252764f

[]{#copper(ii)-hydroxide}

###  copper(II) hydroxide
- **Definition**: A Cu-based inorganic and synthetic pigment with the
chemical formula Cu(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q186357 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6ef22ba7

[]{#chalconatronite}

###  chalconatronite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Na2Cu(CO3)2.3H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Na2Cu(CO3)2.3H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3665757 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ee47568f

[]{#malachite}

###  malachite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2CO3(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - copper carbonate hydroxide, 
  - Cu2CO3(OH)2, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q408815 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_cd222c05

[]{#azurite}

###  azurite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu3(CO3)2(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - copper carbonate hydroxide, 
  - Cu3(CO3)2(OH)2, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q4161307 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f3c28be9

[]{#artificial-ultramarine}

###  artificial ultramarine
- **Definition**: A S-based inorganic and synthetic pigment with the
chemical formula Na7Al6Si6O24S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Na7Al6Si6O24S3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q17990717 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6e53b6bc

[]{#lazurite}

###  lazurite
- **Definition**: A S-based inorganic and natural pigment with the
chemical formula (Na,Ca)8[(Al,Si)12O24](S,SO4).
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - (Na,Ca)8[(Al,Si)12O24](S,SO4)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q10914750 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f420149c

[]{#smalt}

###  smalt
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula SiO2(vit)Cox.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2(vit)Cox
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q107387254 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_94c83a39

[]{#cobalt-zinc-oxide}

###  cobalt zinc oxide
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula CoZnO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CoZnO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_73305a8a

[]{#cobalt-tin-oxide}

###  cobalt tin oxide
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula CoSnO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CoSnO3
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_54df3c30

[]{#cobalt-aluminium-oxide}

###  cobalt aluminium oxide
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula CoAl2O4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CoAl2O4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q4063718 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_e4becf48

[]{#barium-manganese-oxide}

###  barium manganese oxide
- **Definition**: A Mn-based inorganic and synthetic pigment with the
chemical formula BaMnO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - BaMnO4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q82900287 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_b57c07a6

[]{#egyptian-green}

###  Egyptian green
- **Definition**: A Cu-based inorganic and synthetic pigment with the
chemical formula (Ca,Cu)3Si3O9.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - cupro-wollastonite, 
  - (Ca,Cu)3Si3O9, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q133807926 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_485b59c0

[]{#egyptian-blue}

###  Egyptian blue
- **Definition**: A Cu-based inorganic and synthetic pigment with the
chemical formula CaCuSi4O10.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium copper silicate, 
  - cuprorivaite, 
  - CaCuSi4O10, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q253181 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_318b6d40

[]{#han-purple}

###  Han purple
- **Definition**: A Cu-based inorganic and synthetic pigment with the
chemical formula BaCuSi2O6.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - barium copper silerythicate, 
  - BaCuSi2O6, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q5646726 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ccccde03

[]{#han-blue}

###  Han blue
- **Definition**: A Cu-based inorganic and synthetic pigment with the
chemical formula BaCuSi4O10.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - barium copper silicate, 
  - BaCuSi4O10, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q5646726 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_699e5788

[]{#purpurite}

###  purpurite
- **Definition**: A Mn-based inorganic and natural pigment with the
chemical formula MnPO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - MnPO4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q333827 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_ad522ba1

[]{#synthetic-manganese-phosphate}

###  synthetic manganese phosphate
- **Definition**: A Mn-based inorganic and synthetic pigment with the
chemical formula MnPO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - MnPO4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_6b2692af

[]{#magnesium-cobalt-arsenate}

###  magnesium cobalt arsenate
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula Mg2Co(AsO4)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Mg2Co(AsO4)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_7903d63d

[]{#lithium-cobalt-phosphate}

###  lithium cobalt phosphate
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula LiCoPO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - LiCoPO4
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q82525114 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_16d6b816

[]{#ammonium-cobalt-phosphate-hydrate}

###  ammonium cobalt phosphate hydrate
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula CoNH4PO4.H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CoNH4PO4.H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_ab4883bd

[]{#cobalt-phosphate-hydrate}

###  cobalt phosphate hydrate
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula Co3(PO4)2.8H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Co3(PO4)2.8H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** http://vocab.terralid.org#c_f649fe61

[]{#cobalt-phosphate}

###  cobalt phosphate
- **Definition**: A Co-based inorganic and synthetic pigment with the
chemical formula Co3(PO4)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Co3(PO4)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q15634038 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_df972a0a

[]{#erythrite}

###  erythrite
- **Definition**: A Co-based inorganic and natural pigment with the
chemical formula Co3(AsO4)2.8H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - cobalt ochre, 
  - Co3(AsO4)2.8H2O, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q131611792 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_6c9467ff

[]{#fluorite}

###  fluorite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaF.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - calcium fluorite, 
  - CaF, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q413374 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f70ed0af

[]{#vivianite}

###  vivianite
- **Definition**: A Fe-based inorganic and natural pigment with the
chemical formula Fe3(PO4)2.8H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Fe3(PO4)2.8H2O
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - https://www.wikidata.org/wiki/Q3777850 (closeMatch)
- **Concept URI:** http://vocab.terralid.org#c_f5569e8c


