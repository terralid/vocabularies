---
title: "TerraLID Vocabulary"
comment: |
  WARNING: This file is generated. Any edits will be lost!
execute:
  echo: false
---

[]{#TerraLIDvocabularies}


Vocabulary last modified:  2026-06-13T01:06:16

The TerraLID vocabularies include various vocabularies to ensure coherent data entries for the TerraLID metadata profile, which describes archaeometric data and the materials they are derived from with particular focus on lead isotope data. The vocabularies were compiled by the TerraLID Editors and the TerraLID Core Team and implemented in SKOS by Thomas Rose and Katrin J. Westner. This work has received funding from the German Research Foundation (DFG) through the grants KL 1259/17-1 and WI 5923/2-1 (project number: 524790825).
  The TerraLID vocabularies include various vocabularies to ensure coherent data entries for the TerraLID metadata profile, which describes archaeometric data and the materials they are derived from with particular focus on lead isotope data. The vocabularies were compiled by the TerraLID Editors and the TerraLID Core Team and implemented in SKOS by Thomas Rose and Katrin J. Westner. This work has received funding from the German Research Foundation (DFG) through the grants KL 1259/17-1 and WI 5923/2-1 (project number: 524790825).

Namespace: 
[`http://vocab.terralid.org#conceptScheme_a0559f69`](http://vocab.terralid.org#conceptScheme_a0559f69)

**History**


- [abundance (concentration)](#abundance-(concentration))
    - [major](#major)
    - [minor](#minor)
    - [trace](#trace)

- [alteration extent](#alteration-extent)
    - [no alteration](#no-alteration)
    - [severe alteration](#severe-alteration)
    - [slight alteration](#slight-alteration)
    - [unknown](#unknown)

- [alteration process](#alteration-process)
    - [biodegradation](#biodegradation)
    - [darkening](#darkening)
    - [efflorescense](#efflorescense)
    - [erosion](#erosion)
    - [flaking](#flaking)
    - [other](#other)
    - [oxidation](#oxidation)
    - [photodegradation](#photodegradation)
    - [unknown](#unknown)

- [analytical instrument](#analytical-instrument)
    - [instrument manufacturer](#instrument-manufacturer)
        - [Finnigan MAT](#finnigan-mat)
            - [MAT 262](#mat-262)
        - [GV Instruments](#gv-instruments)
            - [IsoProbe-P](#isoprobe-p)
            - [IsoProbe-T](#isoprobe-t)
        - [Isotopx](#isotopx)
            - [Phoenix](#phoenix)
        - [Kunyuan Instrument](#kunyuan-instrument)
            - [GB-TIMS](#gb-tims)
        - [Micromass](#micromass)
            - [Sector 54](#sector-54)
        - [MSTech Group](#mstech-group)
            - [ZMS DF-TIMS-01](#zms-df-tims-01)
        - [Nu Instruments](#nu-instruments)
            - [Plasma 1700](#plasma-1700)
            - [Plasma 3](#plasma-3)
            - [Sapphire](#sapphire)
            - [Sapphire XD](#sapphire-xd)
            - [TIMS (Nu instruments)](#tims-(nu-instruments))
        - [SELMI](#selmi)
            - [MI 1201-AT](#mi-1201-at)
        - [Thermo Fisher Scientific](#thermo-fisher-scientific)
            - [Neoma](#neoma)
            - [Neptune](#neptune)
            - [Neptune Plus](#neptune-plus)
            - [Triton Plus](#triton-plus)
            - [Triton XT](#triton-xt)
        - [Uralpribor](#uralpribor)
            - [MIT 350-TM](#mit-350-tm)
    - [instrument model](#instrument-model)
        - [GB-TIMS](#gb-tims)
        - [IsoProbe-P](#isoprobe-p)
        - [IsoProbe-T](#isoprobe-t)
        - [MAT 262](#mat-262)
        - [MI 1201-AT](#mi-1201-at)
        - [MIT 350-TM](#mit-350-tm)
        - [Neoma](#neoma)
        - [Neptune](#neptune)
        - [Neptune Plus](#neptune-plus)
        - [Phoenix](#phoenix)
        - [Plasma 1700](#plasma-1700)
        - [Plasma 3](#plasma-3)
        - [Sapphire](#sapphire)
        - [Sapphire XD](#sapphire-xd)
        - [Sector 54](#sector-54)
        - [TIMS (Nu instruments)](#tims-(nu-instruments))
        - [Triton Plus](#triton-plus)
        - [Triton XT](#triton-xt)
        - [ZMS DF-TIMS-01](#zms-df-tims-01)
    - [instrument type](#instrument-type)
        - [MC-ICP-MS (instrument)](#mc-icp-ms-(instrument))
            - [IsoProbe-P](#isoprobe-p)
            - [Neoma](#neoma)
            - [Neptune](#neptune)
            - [Neptune Plus](#neptune-plus)
            - [Plasma 1700](#plasma-1700)
            - [Plasma 3](#plasma-3)
            - [Sapphire](#sapphire)
            - [Sapphire XD](#sapphire-xd)
        - [TIMS (instrument)](#tims-(instrument))
            - [GB-TIMS](#gb-tims)
            - [IsoProbe-T](#isoprobe-t)
            - [MAT 262](#mat-262)
            - [MI 1201-AT](#mi-1201-at)
            - [MIT 350-TM](#mit-350-tm)
            - [Phoenix](#phoenix)
            - [Sector 54](#sector-54)
            - [TIMS (Nu instruments)](#tims-(nu-instruments))
            - [Triton Plus](#triton-plus)
            - [Triton XT](#triton-xt)
            - [ZMS DF-TIMS-01](#zms-df-tims-01)
    - [other](#other)

- [analytical method](#analytical-method)
    - [atomic absorption spectroscopy](#atomic-absorption-spectroscopy)
        - [AAS (flame)](#aas-(flame))
        - [AAS (glow-discharge)](#aas-(glow-discharge))
        - [AAS (graphite furnace)](#aas-(graphite-furnace))
    - [emission spectrometry](#emission-spectrometry)
        - [AES (flame)](#aes-(flame))
        - [AES (graphite furnace)](#aes-(graphite-furnace))
        - [OES (ICP)](#oes-(icp))
        - [OES (spark)](#oes-(spark))
    - [mass spectrometer](#mass-spectrometer)
        - [ICP-MS](#icp-ms)
            - [LA-ICP-MS](#la-icp-ms)
                - [fs-LA-ICP-MS](#fs-la-icp-ms)
                - [LA-MC-ICP-MS](#la-mc-icp-ms)
                    - [fs-LA-MC-ICP-MS](#fs-la-mc-icp-ms)
                    - [ns-LA-MC-ICP-MS](#ns-la-mc-icp-ms)
                - [ns-LA-ICP-MS](#ns-la-icp-ms)
            - [MC-ICP-MS](#mc-icp-ms)
                - [LA-MC-ICP-MS](#la-mc-icp-ms)
                    - [fs-LA-MC-ICP-MS](#fs-la-mc-icp-ms)
                    - [ns-LA-MC-ICP-MS](#ns-la-mc-icp-ms)
            - [Q-ICP-MS](#q-icp-ms)
        - [TIMS](#tims)
    - [NAA](#naa)
    - [wet chemistry](#wet-chemistry)
    - [X-ray spectrometry](#x-ray-spectrometry)
        - [ED-XRF](#ed-xrf)
            - [pXRF](#pxrf)
        - [EPMA](#epma)
        - [SEM-EDS](#sem-eds)
        - [WD-XRF](#wd-xrf)

- [analytical uncertainty](#analytical-uncertainty)
    - [standard deviation](#standard-deviation)
    - [standard error](#standard-error)

- [assemblage](#assemblage)
    - [alteration product (hydrothermal)](#alteration-product-(hydrothermal))
    - [alteration product (supergene)](#alteration-product-(supergene))
    - [collection](#collection)
    - [components](#components)
    - [gangue](#gangue)
    - [gossan](#gossan)
    - [hoard](#hoard)
    - [host rock](#host-rock)
    - [item](#item)
    - [ore](#ore)
        - [alteration](#alteration)
        - [ore mineral](#ore-mineral)
            - [major mineral](#major-mineral)
            - [minor mineral](#minor-mineral)
        - [primary ore](#primary-ore)
        - [secondary ore](#secondary-ore)
    - [set](#set)
    - [wall rock](#wall-rock)

- [authenticity](#authenticity)
    - [contemporary imitation](#contemporary-imitation)
    - [genuine](#genuine)
    - [modern imitation](#modern-imitation)
    - [unknown](#unknown)

- [colour system](#colour-system)
    - [CIELAB](#cielab)
    - [eye](#eye)
    - [Munsell](#munsell)

- [compound origin](#compound-origin)
    - [mixed compound origin](#mixed-compound-origin)
    - [natural](#natural)
    - [synthetic](#synthetic)
    - [unknown](#unknown)

- [compound type](#compound-type)
    - [inorganic](#inorganic)
    - [mixed compound types](#mixed-compound-types)
    - [organic](#organic)
    - [unknown](#unknown)

- [context type](#context-type)
    - [disturbed context](#disturbed-context)
        - [anthropogenically disturbed](#anthropogenically-disturbed)
        - [biogenically disturbed](#biogenically-disturbed)
    - [mixed context](#mixed-context)
    - [undisturbed context](#undisturbed-context)
    - [unknown](#unknown)

- [contributorType](#contributortype)
    - [ContactPerson](#contactperson)
    - [DataCollector](#datacollector)
    - [DataCurator](#datacurator)
    - [DataManager](#datamanager)
    - [Distributor](#distributor)
    - [Editor](#editor)
    - [HostingInstitution](#hostinginstitution)
    - [Other (contributorType)](#other-(contributortype))
    - [Producer](#producer)
    - [ProjectLeader](#projectleader)
    - [ProjectManager](#projectmanager)
    - [ProjectMember](#projectmember)
    - [RegistrationAgency](#registrationagency)
    - [RegistrationAuthority](#registrationauthority)
    - [RelatedPerson](#relatedperson)
    - [Researcher](#researcher)
    - [ResearchGroup](#researchgroup)
    - [RightsHolder](#rightsholder)
    - [Sponsor](#sponsor)
    - [Supervisor](#supervisor)
    - [Translator](#translator)
    - [WorkPackageLeader](#workpackageleader)

- [corrosion extent](#corrosion-extent)
    - [moderate corrosion](#moderate-corrosion)
    - [no corrosion](#no-corrosion)
    - [severe corrosion](#severe-corrosion)
    - [unknown](#unknown)
    - [weak corrosion](#weak-corrosion)

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
            - [lead-lead dating](#lead-lead-dating)
            - [lutetium-hafnium dating](#lutetium-hafnium-dating)
            - [potassium-argon dating](#potassium-argon-dating)
                - [argon-argon dating](#argon-argon-dating)
            - [radiocarbon dating](#radiocarbon-dating)
            - [rhenium-osmium dating](#rhenium-osmium-dating)
            - [rubidium-strontium dating](#rubidium-strontium-dating)
            - [samarium-neodymium dating](#samarium-neodymium-dating)
            - [uranium-lead dating](#uranium-lead-dating)
            - [uranium-series dating](#uranium-series-dating)
        - [rehydroxylation dating](#rehydroxylation-dating)
    - [relative dating](#relative-dating)
        - [archaeomagnetic dating](#archaeomagnetic-dating)
        - [biostratigraphy](#biostratigraphy)
        - [seriation](#seriation)
        - [tephrochronology](#tephrochronology)

- [discovery activity](#discovery-activity)
    - [borehole survey](#borehole-survey)
        - [auger drilling](#auger-drilling)
        - [core drilling](#core-drilling)
    - [excavation](#excavation)
        - [rescue excavation](#rescue-excavation)
        - [research excavation](#research-excavation)
        - [underwater excavation](#underwater-excavation)
    - [explorative mining activities](#explorative-mining-activities)
    - [illicit digging](#illicit-digging)
    - [metal detecting](#metal-detecting)
    - [mining](#mining)
    - [ore prospection](#ore-prospection)
    - [stray find](#stray-find)
    - [survey](#survey)
    - [unknown](#unknown)

- [glass component](#glass-component)
    - [colorant](#colorant)
    - [network former](#network-former)
    - [network modifier](#network-modifier)
    - [opacifier](#opacifier)
    - [unknown](#unknown)

- [identifier](#identifier)
    - [ARK](#ark)
    - [ArXiv](#arxiv)
    - [bibcode](#bibcode)
    - [CSTR](#cstr)
    - [DOI](#doi)
    - [EAN13](#ean13)
    - [EISSN](#eissn)
    - [Handle](#handle)
    - [IGSN](#igsn)
    - [ISBN](#isbn)
    - [ISSN](#issn)
    - [ISTC](#istc)
    - [LISSN](#lissn)
    - [LSID](#lsid)
    - [PMID](#pmid)
    - [PURL](#purl)
    - [RAiD](#raid)
    - [RRID](#rrid)
    - [SWHID](#swhid)
    - [UPC](#upc)
    - [URL](#url)
    - [URN](#urn)
    - [w3id](#w3id)

- [information source](#information-source)
    - [calculated](#calculated)
    - [original](#original)

- [lead isotope age model](#lead-isotope-age-model)
    - [AJ84](#aj84)
    - [CR75](#cr75)
    - [SK75](#sk75)

- [lead isotope ratios](#lead-isotope-ratios)
    - [204Pb/206Pb](#204pb-206pb)
    - [206Pb/204Pb](#206pb-204pb)
    - [206Pb/208Pb](#206pb-208pb)
    - [207Pb/204Pb](#207pb-204pb)
    - [207Pb/206Pb](#207pb-206pb)
    - [207Pb/208Pb](#207pb-208pb)
    - [208Pb/204Pb](#208pb-204pb)
    - [208Pb/206Pb](#208pb-206pb)

- [mass bias correction](#mass-bias-correction)
    - [double-spike](#double-spike)
    - [exponential law](#exponential-law)
    - [linear model](#linear-model)
    - [power law](#power-law)
    - [standard-sample bracketing](#standard-sample-bracketing)

- [mineral texture](#mineral-texture)
    - [deformation-related](#deformation-related)
        - [bending](#bending)
        - [brecciated](#brecciated)
        - [broken](#broken)
        - [cataclastic](#cataclastic)
        - [planar alignment](#planar-alignment)
        - [pressure twins](#pressure-twins)
        - [translation lamellae](#translation-lamellae)
    - [intergrowth](#intergrowth)
        - [amoeboid](#amoeboid)
        - [atoll-like](#atoll-like)
        - [cellular (intergrowth)](#cellular-(intergrowth))
        - [disseminated](#disseminated)
        - [interlocked](#interlocked)
        - [intersertal](#intersertal)
        - [interstitial](#interstitial)
        - [ophitic](#ophitic)
        - [poikiloblastic](#poikiloblastic)
        - [rimmed](#rimmed)
        - [symplectitic](#symplectitic)
            - [myrmekitic](#myrmekitic)
    - [replacement](#replacement)
        - [atoll-like (replacement)](#atoll-like-(replacement))
        - [boxwork](#boxwork)
        - [cellular (replacement)](#cellular-(replacement))
        - [cement-shaped](#cement-shaped)
        - [cusp-and-caries](#cusp-and-caries)
        - [filiform](#filiform)
        - [graphic](#graphic)
        - [island-shaped](#island-shaped)
        - [lacuna](#lacuna)
        - [lamellar](#lamellar)
        - [pseudomorph](#pseudomorph)
        - [skeleton-shaped](#skeleton-shaped)
        - [zonal](#zonal)

- [nuclide](#nuclide)
    - [aluminium-27](#aluminium-27)
    - [antimony-121](#antimony-121)
    - [antimony-123](#antimony-123)
    - [argon-36](#argon-36)
    - [argon-38](#argon-38)
    - [argon-40](#argon-40)
    - [arsenic-75](#arsenic-75)
    - [barium-130](#barium-130)
    - [barium-134](#barium-134)
    - [barium-135](#barium-135)
    - [barium-136](#barium-136)
    - [barium-137](#barium-137)
    - [barium-138](#barium-138)
    - [beryllium-9](#beryllium-9)
    - [boron-10](#boron-10)
    - [boron-11](#boron-11)
    - [bromine-79](#bromine-79)
    - [bromine-81](#bromine-81)
    - [cadmium-110](#cadmium-110)
    - [cadmium-111](#cadmium-111)
    - [cadmium-112](#cadmium-112)
    - [caesium-133](#caesium-133)
    - [calcium-42](#calcium-42)
    - [calcium-43](#calcium-43)
    - [calcium-44](#calcium-44)
    - [carbon-12](#carbon-12)
    - [carbon-13](#carbon-13)
    - [cerium-140](#cerium-140)
    - [chlorine-35](#chlorine-35)
    - [chlorine-37](#chlorine-37)
    - [chromium-52](#chromium-52)
    - [chromium-53](#chromium-53)
    - [chromium-54](#chromium-54)
    - [cobalt-59](#cobalt-59)
    - [copper-63](#copper-63)
    - [copper-65](#copper-65)
    - [deuterium](#deuterium)
    - [dysprosium-156](#dysprosium-156)
    - [dysprosium-158](#dysprosium-158)
    - [dysprosium-160](#dysprosium-160)
    - [dysprosium-161](#dysprosium-161)
    - [dysprosium-162](#dysprosium-162)
    - [dysprosium-163](#dysprosium-163)
    - [dysprosium-164](#dysprosium-164)
    - [erbium-162](#erbium-162)
    - [erbium-164](#erbium-164)
    - [erbium-166](#erbium-166)
    - [erbium-167](#erbium-167)
    - [erbium-168](#erbium-168)
    - [erbium-170](#erbium-170)
    - [europium-153](#europium-153)
    - [fluorine-19](#fluorine-19)
    - [gadolinium-154](#gadolinium-154)
    - [gadolinium-155](#gadolinium-155)
    - [gadolinium-156](#gadolinium-156)
    - [gadolinium-157](#gadolinium-157)
    - [gadolinium-158](#gadolinium-158)
    - [gallium-69](#gallium-69)
    - [gallium-71](#gallium-71)
    - [germanium-70](#germanium-70)
    - [germanium-72](#germanium-72)
    - [germanium-73](#germanium-73)
    - [germanium-74](#germanium-74)
    - [germanium-76](#germanium-76)
    - [gold-197](#gold-197)
    - [hafnium-176](#hafnium-176)
    - [hafnium-177](#hafnium-177)
    - [hafnium-178](#hafnium-178)
    - [hafnium-179](#hafnium-179)
    - [hafnium-180](#hafnium-180)
    - [helium-3](#helium-3)
    - [helium-4](#helium-4)
    - [holmium-165](#holmium-165)
    - [indium-113](#indium-113)
    - [iodine-127](#iodine-127)
    - [iridium-191](#iridium-191)
    - [iridium-193](#iridium-193)
    - [iron-54](#iron-54)
    - [iron-56](#iron-56)
    - [iron-57](#iron-57)
    - [iron-58](#iron-58)
    - [krypton-80](#krypton-80)
    - [krypton-82](#krypton-82)
    - [krypton-83](#krypton-83)
    - [krypton-84](#krypton-84)
    - [krypton-86](#krypton-86)
    - [lanthanum-139](#lanthanum-139)
    - [lead-206](#lead-206)
    - [lead-207](#lead-207)
    - [lead-208](#lead-208)
    - [lithium-6](#lithium-6)
    - [lithium-7](#lithium-7)
    - [lutetium-175](#lutetium-175)
    - [magnesium-24](#magnesium-24)
    - [magnesium-25](#magnesium-25)
    - [magnesium-26](#magnesium-26)
    - [manganese-55](#manganese-55)
    - [mercury-196](#mercury-196)
    - [mercury-198](#mercury-198)
    - [mercury-199](#mercury-199)
    - [mercury-200](#mercury-200)
    - [mercury-201](#mercury-201)
    - [mercury-202](#mercury-202)
    - [mercury-204](#mercury-204)
    - [molybdenum-92](#molybdenum-92)
    - [molybdenum-94](#molybdenum-94)
    - [molybdenum-95](#molybdenum-95)
    - [molybdenum-96](#molybdenum-96)
    - [molybdenum-97](#molybdenum-97)
    - [molybdenum-98](#molybdenum-98)
    - [neodymium-142](#neodymium-142)
    - [neodymium-143](#neodymium-143)
    - [neodymium-145](#neodymium-145)
    - [neodymium-146](#neodymium-146)
    - [neodymium-148](#neodymium-148)
    - [neon-20](#neon-20)
    - [neon-21](#neon-21)
    - [neon-22](#neon-22)
    - [nickel-58](#nickel-58)
    - [nickel-60](#nickel-60)
    - [nickel-61](#nickel-61)
    - [nickel-62](#nickel-62)
    - [nickel-64](#nickel-64)
    - [niobium-93](#niobium-93)
    - [nitrogen-14](#nitrogen-14)
    - [nitrogen-15](#nitrogen-15)
    - [osmium-187](#osmium-187)
    - [osmium-188](#osmium-188)
    - [osmium-189](#osmium-189)
    - [osmium-190](#osmium-190)
    - [osmium-192](#osmium-192)
    - [oxygen-16](#oxygen-16)
    - [oxygen-17](#oxygen-17)
    - [oxygen-18](#oxygen-18)
    - [palladium-102](#palladium-102)
    - [palladium-104](#palladium-104)
    - [palladium-105](#palladium-105)
    - [palladium-106](#palladium-106)
    - [palladium-108](#palladium-108)
    - [palladium-110](#palladium-110)
    - [phosphorus-31](#phosphorus-31)
    - [platinum-192](#platinum-192)
    - [platinum-194](#platinum-194)
    - [platinum-195](#platinum-195)
    - [platinum-196](#platinum-196)
    - [platinum-198](#platinum-198)
    - [potassium-39](#potassium-39)
    - [potassium-41](#potassium-41)
    - [praseodymium-141](#praseodymium-141)
    - [protium](#protium)
    - [rhenium-185](#rhenium-185)
    - [rhodium-103](#rhodium-103)
    - [rubidium-85](#rubidium-85)
    - [ruthenium-100](#ruthenium-100)
    - [ruthenium-101](#ruthenium-101)
    - [ruthenium-102](#ruthenium-102)
    - [ruthenium-104](#ruthenium-104)
    - [ruthenium-96](#ruthenium-96)
    - [ruthenium-98](#ruthenium-98)
    - [ruthenium-99](#ruthenium-99)
    - [samarium-144](#samarium-144)
    - [samarium-149](#samarium-149)
    - [samarium-150](#samarium-150)
    - [samarium-152](#samarium-152)
    - [samarium-154](#samarium-154)
    - [scandium-45](#scandium-45)
    - [selenium-74](#selenium-74)
    - [selenium-76](#selenium-76)
    - [selenium-77](#selenium-77)
    - [selenium-78](#selenium-78)
    - [selenium-80](#selenium-80)
    - [selenium-82](#selenium-82)
    - [silicon-28](#silicon-28)
    - [silicon-29](#silicon-29)
    - [silicon-30](#silicon-30)
    - [silver-107](#silver-107)
    - [silver-109](#silver-109)
    - [sodium-23](#sodium-23)
    - [strontium-84](#strontium-84)
    - [strontium-86](#strontium-86)
    - [strontium-87](#strontium-87)
    - [strontium-88](#strontium-88)
    - [sulfur-32](#sulfur-32)
    - [sulfur-33](#sulfur-33)
    - [sulfur-34](#sulfur-34)
    - [sulfur-36](#sulfur-36)
    - [Tantalum-180](#tantalum-180)
    - [tantalum-181](#tantalum-181)
    - [tellurium-120](#tellurium-120)
    - [tellurium-122](#tellurium-122)
    - [tellurium-124](#tellurium-124)
    - [tellurium-125](#tellurium-125)
    - [tellurium-126](#tellurium-126)
    - [terbium-159](#terbium-159)
    - [thallium-203](#thallium-203)
    - [thallium-205](#thallium-205)
    - [thulium-169](#thulium-169)
    - [tin-114](#tin-114)
    - [tin-115](#tin-115)
    - [tin-116](#tin-116)
    - [tin-117](#tin-117)
    - [tin-118](#tin-118)
    - [tin-119](#tin-119)
    - [tin-120](#tin-120)
    - [tin-122](#tin-122)
    - [titanium-46](#titanium-46)
    - [titanium-47](#titanium-47)
    - [titanium-48](#titanium-48)
    - [titanium-49](#titanium-49)
    - [titanium-50](#titanium-50)
    - [tungsten-182](#tungsten-182)
    - [tungsten-184](#tungsten-184)
    - [vanadium-51](#vanadium-51)
    - [xenon-126](#xenon-126)
    - [xenon-128](#xenon-128)
    - [xenon-129](#xenon-129)
    - [xenon-130](#xenon-130)
    - [xenon-131](#xenon-131)
    - [xenon-132](#xenon-132)
    - [ytterbium-168](#ytterbium-168)
    - [ytterbium-170](#ytterbium-170)
    - [ytterbium-171](#ytterbium-171)
    - [ytterbium-172](#ytterbium-172)
    - [ytterbium-173](#ytterbium-173)
    - [ytterbium-174](#ytterbium-174)
    - [ytterbium-176](#ytterbium-176)
    - [yttrium-89](#yttrium-89)
    - [zinc-66](#zinc-66)
    - [zinc-67](#zinc-67)
    - [zinc-68](#zinc-68)
    - [zirconium-90](#zirconium-90)
    - [zirconium-91](#zirconium-91)
    - [zirconium-92](#zirconium-92)
    - [zirconium-94](#zirconium-94)

- [object life cycle stage](#object-life-cycle-stage)
    - [conservation stage](#conservation-stage)
    - [discovery stage](#discovery-stage)
    - [finds processing stage](#finds-processing-stage)
    - [laboratory stage](#laboratory-stage)
    - [restoration stage](#restoration-stage)
    - [storage stage](#storage-stage)

- [object material](#object-material)
    - [ceramic](#ceramic)
    - [glass](#glass)
    - [metal](#metal)
        - [coin](#coin)
    - [ore (TerraLID category)](#ore-(terralid-category))
    - [other](#other)
    - [pigment](#pigment)
    - [sediment](#sediment)
    - [unknown](#unknown)

- [oxide](#oxide)
    - [aluminium oxide](#aluminium-oxide)
    - [antimony pentoxide](#antimony-pentoxide)
    - [antimony trioxide](#antimony-trioxide)
    - [arsenic pentoxide](#arsenic-pentoxide)
    - [arsenic trioxide](#arsenic-trioxide)
    - [barium oxide](#barium-oxide)
    - [beryllium oxide](#beryllium-oxide)
    - [bismuth pentoxide](#bismuth-pentoxide)
    - [bismuth(III) oxide](#bismuth(iii)-oxide)
    - [cadmium oxide](#cadmium-oxide)
    - [calcium oxide](#calcium-oxide)
    - [carbon dioxide](#carbon-dioxide)
    - [carbon monoxide](#carbon-monoxide)
    - [carbon trioxide](#carbon-trioxide)
    - [cerium(IV) oxide](#cerium(iv)-oxide)
    - [chlorine dioxide](#chlorine-dioxide)
    - [chlorine heptoxide](#chlorine-heptoxide)
    - [chromium trioxide](#chromium-trioxide)
    - [chromium(II) oxide](#chromium(ii)-oxide)
    - [chromium(IV) oxide](#chromium(iv)-oxide)
    - [cobalt(II) oxide](#cobalt(ii)-oxide)
    - [copper(I) oxide](#copper(i)-oxide)
    - [copper(II) oxide](#copper(ii)-oxide)
    - [diboron trioxide](#diboron-trioxide)
    - [dicarbon monoxide](#dicarbon-monoxide)
    - [dichlorine monoxide](#dichlorine-monoxide)
    - [dichromium trioxide](#dichromium-trioxide)
    - [dinitrogen pentoxide](#dinitrogen-pentoxide)
    - [dinitrogen tetroxide](#dinitrogen-tetroxide)
    - [dinitrogen trioxide](#dinitrogen-trioxide)
    - [erbium(III) oxide](#erbium(iii)-oxide)
    - [gadolinium(III) oxide](#gadolinium(iii)-oxide)
    - [gallium(III) oxide](#gallium(iii)-oxide)
    - [germanium dioxide](#germanium-dioxide)
    - [gold sesquioxide](#gold-sesquioxide)
    - [hafnium(IV) oxide](#hafnium(iv)-oxide)
    - [holmium(III) oxide](#holmium(iii)-oxide)
    - [indium oxide](#indium-oxide)
    - [iron(II) oxide](#iron(ii)-oxide)
    - [iron(III) oxide](#iron(iii)-oxide)
    - [lanthanum(III) oxide](#lanthanum(iii)-oxide)
    - [lead dioxide](#lead-dioxide)
    - [lead(II) oxide](#lead(ii)-oxide)
    - [lithium oxide](#lithium-oxide)
    - [lutetium(III) oxide](#lutetium(iii)-oxide)
    - [magnesium oxide](#magnesium-oxide)
    - [manganese dioxide](#manganese-dioxide)
    - [manganese heptoxide](#manganese-heptoxide)
    - [manganese(II) oxide](#manganese(ii)-oxide)
    - [mercury(II) oxide](#mercury(ii)-oxide)
    - [molybdenum trioxide](#molybdenum-trioxide)
    - [nickel(II) oxide](#nickel(ii)-oxide)
    - [nickel(III) oxide](#nickel(iii)-oxide)
    - [nitric oxide](#nitric-oxide)
    - [nitrogen dioxide](#nitrogen-dioxide)
    - [osmium tetroxide](#osmium-tetroxide)
    - [oxidoaluminium](#oxidoaluminium)
    - [oxygen difluoride](#oxygen-difluoride)
    - [palladium(II) oxide](#palladium(ii)-oxide)
    - [phosphorus pentoxide](#phosphorus-pentoxide)
    - [plutonium(IV) oxide](#plutonium(iv)-oxide)
    - [potassium oxide](#potassium-oxide)
    - [promethium(III) oxide](#promethium(iii)-oxide)
    - [rhenium trioxide](#rhenium-trioxide)
    - [rhenium(VII) oxide](#rhenium(vii)-oxide)
    - [rhodium(III) oxide](#rhodium(iii)-oxide)
    - [rubidium oxide](#rubidium-oxide)
    - [ruthenium tetroxide](#ruthenium-tetroxide)
    - [ruthenium(IV) oxide](#ruthenium(iv)-oxide)
    - [samarium(III) oxide](#samarium(iii)-oxide)
    - [scandium oxide](#scandium-oxide)
    - [selenium dioxide](#selenium-dioxide)
    - [selenium trioxide](#selenium-trioxide)
    - [silicon dioxide](#silicon-dioxide)
    - [silver oxide](#silver-oxide)
    - [silver(II) oxide](#silver(ii)-oxide)
    - [sodium oxide](#sodium-oxide)
    - [strontium oxide](#strontium-oxide)
    - [sulfur dioxide](#sulfur-dioxide)
    - [sulfur trioxide](#sulfur-trioxide)
    - [tantalum pentoxide](#tantalum-pentoxide)
    - [tellurium dioxide](#tellurium-dioxide)
    - [tellurium trioxide](#tellurium-trioxide)
    - [terbium(III) oxide](#terbium(iii)-oxide)
    - [tetraoxygen](#tetraoxygen)
    - [tetraphosphorus hexaoxide](#tetraphosphorus-hexaoxide)
    - [thallium(I) oxide](#thallium(i)-oxide)
    - [thallium(III) oxide](#thallium(iii)-oxide)
    - [thorium dioxide](#thorium-dioxide)
    - [thulium(III) oxide](#thulium(iii)-oxide)
    - [tin(II) oxide](#tin(ii)-oxide)
    - [tin(IV) oxide](#tin(iv)-oxide)
    - [titanium dioxide](#titanium-dioxide)
    - [titanium(III) oxide](#titanium(iii)-oxide)
    - [tungsten trioxide](#tungsten-trioxide)
    - [tungsten(III) oxide](#tungsten(iii)-oxide)
    - [tungsten(IV) oxide](#tungsten(iv)-oxide)
    - [uranium dioxide](#uranium-dioxide)
    - [uranium trioxide](#uranium-trioxide)
    - [vanadium(II) oxide](#vanadium(ii)-oxide)
    - [vanadium(III) oxide](#vanadium(iii)-oxide)
    - [vanadium(IV) oxide](#vanadium(iv)-oxide)
    - [vanadium(V) oxide](#vanadium(v)-oxide)
    - [water](#water)
    - [xenon tetroxide](#xenon-tetroxide)
    - [xenon trioxide](#xenon-trioxide)
    - [ytterbium(III) oxide](#ytterbium(iii)-oxide)
    - [yttrium oxide](#yttrium-oxide)
    - [zinc oxide](#zinc-oxide)
    - [zirconium dioxide](#zirconium-dioxide)

- [pigment component](#pigment-component)
    - [binder](#binder)
    - [colorant](#colorant)
    - [flux](#flux)
    - [impurity](#impurity)
    - [unknown](#unknown)
    - [various](#various)

- [pigment name](#pigment-name)
    - [aerinite](#aerinite)
    - [aluminium hydroxide](#aluminium-hydroxide)
    - [aluminium oxide (pigment)](#aluminium-oxide-(pigment))
    - [ammonium cobalt phosphate hydrate](#ammonium-cobalt-phosphate-hydrate)
    - [anatase](#anatase)
    - [anglesite](#anglesite)
    - [anhydrite](#anhydrite)
    - [antimony(III) sulfide](#antimony(iii)-sulfide)
    - [antlerite](#antlerite)
    - [arsenic(III) oxide](#arsenic(iii)-oxide)
    - [artificial ultramarine](#artificial-ultramarine)
    - [asbestiform minerals](#asbestiform-minerals)
    - [asphalt](#asphalt)
    - [atacamite](#atacamite)
    - [azurite](#azurite)
    - [barium carbonate](#barium-carbonate)
    - [barium manganese oxide](#barium-manganese-oxide)
    - [baryte](#baryte)
    - [bassanite](#bassanite)
    - [bismuth](#bismuth)
    - [bismuthinite](#bismuthinite)
    - [bone and yeast cokes](#bone-and-yeast-cokes)
    - [botallackite](#botallackite)
    - [brochantite](#brochantite)
    - [brown ochre and burnt sienna](#brown-ochre-and-burnt-sienna)
    - [calcium carbonate](#calcium-carbonate)
        - [aragonite](#aragonite)
        - [chalk](#chalk)
        - [coral](#coral)
        - [eggshell](#eggshell)
        - [oyster shell](#oyster-shell)
    - [carbonate hydroxylapatite](#carbonate-hydroxylapatite)
    - [cassiterite](#cassiterite)
    - [celadonite](#celadonite)
    - [cerussite](#cerussite)
    - [chalconatronite](#chalconatronite)
    - [chars](#chars)
    - [chlorite group minerals](#chlorite-group-minerals)
    - [chrome yellow](#chrome-yellow)
    - [chromium oxide hydrate](#chromium-oxide-hydrate)
    - [chromium phosphate hexahydrate](#chromium-phosphate-hexahydrate)
    - [chromium(III) oxide](#chromium(iii)-oxide)
    - [chrysocolla](#chrysocolla)
    - [cinnabar](#cinnabar)
    - [coal](#coal)
    - [cobalt aluminium oxide](#cobalt-aluminium-oxide)
    - [cobalt phosphate](#cobalt-phosphate)
    - [cobalt phosphate hydrate](#cobalt-phosphate-hydrate)
    - [cobalt tin oxide](#cobalt-tin-oxide)
    - [cobalt yellow](#cobalt-yellow)
    - [cobalt zinc oxide](#cobalt-zinc-oxide)
    - [copper acetate arsenite](#copper-acetate-arsenite)
    - [copper arsenite group](#copper-arsenite-group)
    - [copper citrate](#copper-citrate)
    - [copper hexacyanoferrates](#copper-hexacyanoferrates)
    - [copper(II) acetate a](#copper(ii)-acetate-a)
    - [copper(II) acetate b](#copper(ii)-acetate-b)
    - [copper(II) acetate d](#copper(ii)-acetate-d)
    - [copper(II) acetate f](#copper(ii)-acetate-f)
    - [copper(II) acetate h](#copper(ii)-acetate-h)
    - [copper(II) hydroxide](#copper(ii)-hydroxide)
    - [copper(II) oxide (pigment)](#copper(ii)-oxide-(pigment))
    - [cuprite](#cuprite)
    - [diatomite](#diatomite)
    - [dolomite](#dolomite)
    - [dragon’s blood](#dragon’s-blood)
    - [Egyptian blue](#egyptian-blue)
    - [Egyptian green](#egyptian-green)
    - [erythrite](#erythrite)
    - [feldspar minerals](#feldspar-minerals)
    - [feldspathoid minerals](#feldspathoid-minerals)
    - [flame carbons](#flame-carbons)
    - [fluorite](#fluorite)
    - [galena](#galena)
    - [gamboge](#gamboge)
    - [glass (pigment)](#glass-(pigment))
    - [glauconite](#glauconite)
    - [glaucophane](#glaucophane)
    - [goethite](#goethite)
    - [graphite](#graphite)
    - [green earths](#green-earths)
    - [gypsum](#gypsum)
    - [Han blue](#han-blue)
    - [Han purple](#han-purple)
    - [hematite](#hematite)
    - [Indian yellow](#indian-yellow)
    - [indigo](#indigo)
    - [jarosite](#jarosite)
    - [kaolinite](#kaolinite)
    - [lazurite](#lazurite)
    - [lead antimony tin oxide](#lead-antimony-tin-oxide)
    - [lead antimony zinc oxide](#lead-antimony-zinc-oxide)
    - [lead carbonate hydroxide](#lead-carbonate-hydroxide)
    - [lead chloride hydroxide](#lead-chloride-hydroxide)
    - [lead chromate oxide](#lead-chromate-oxide)
    - [lead chromate sulfate](#lead-chromate-sulfate)
    - [lead sulfate (other types)](#lead-sulfate-(other-types))
    - [lead tin oxide](#lead-tin-oxide)
    - [lead tin silicon oxide](#lead-tin-silicon-oxide)
    - [lead white](#lead-white)
    - [lepidocrocite](#lepidocrocite)
    - [litharge](#litharge)
    - [lithium cobalt phosphate](#lithium-cobalt-phosphate)
    - [magnesite](#magnesite)
    - [magnesium cobalt arsenate](#magnesium-cobalt-arsenate)
    - [magnetite](#magnetite)
    - [malachite](#malachite)
    - [manganese oxides](#manganese-oxides)
    - [massicot](#massicot)
    - [Maya blue](#maya-blue)
    - [metacinnabar](#metacinnabar)
    - [mica group minerals](#mica-group-minerals)
    - [montmorillonite](#montmorillonite)
    - [mosaic gold](#mosaic-gold)
    - [nacrite](#nacrite)
    - [Naples yellow](#naples-yellow)
    - [natrojarosite](#natrojarosite)
    - [nontronite](#nontronite)
    - [orpiment](#orpiment)
    - [palygorskite](#palygorskite)
    - [pararealgar](#pararealgar)
    - [paratacamite](#paratacamite)
    - [plattnerite](#plattnerite)
    - [prussian blue](#prussian-blue)
    - [pseudomalachite](#pseudomalachite)
    - [pumice](#pumice)
    - [purpurite](#purpurite)
    - [pyrite](#pyrite)
    - [quartz](#quartz)
    - [realgar](#realgar)
    - [red lake pigments](#red-lake-pigments)
    - [red lead](#red-lead)
    - [red ochre](#red-ochre)
    - [rutile](#rutile)
    - [sepia](#sepia)
    - [serpentine group clay minerals](#serpentine-group-clay-minerals)
    - [smalt](#smalt)
    - [starch](#starch)
    - [stibnite](#stibnite)
    - [sulfur](#sulfur)
    - [synthetic lead carbonate](#synthetic-lead-carbonate)
    - [synthetic manganese phosphate](#synthetic-manganese-phosphate)
    - [talc](#talc)
    - [turmeric](#turmeric)
    - [Turner's yellow](#turner's-yellow)
    - [umbers and wads](#umbers-and-wads)
    - [Vandyke brown](#vandyke-brown)
    - [vermiculite group clay minerals](#vermiculite-group-clay-minerals)
    - [vermillion](#vermillion)
    - [vivianite](#vivianite)
    - [yellow lake pigments](#yellow-lake-pigments)
    - [yellow ochre](#yellow-ochre)
    - [zinc sulfate heptahydrate](#zinc-sulfate-heptahydrate)
    - [zinc sulfide](#zinc-sulfide)
    - [zinc(II) oxide](#zinc(ii)-oxide)

- [production context](#production-context)
    - [primary](#primary)
    - [secondary](#secondary)
    - [unknown](#unknown)

- [production process](#production-process)
    - [absorption](#absorption)
    - [acid reaction](#acid-reaction)
    - [grinding](#grinding)
    - [heating](#heating)
    - [leaching](#leaching)
    - [other](#other)
    - [unknown](#unknown)
    - [weathering](#weathering)

- [recycling indicator](#recycling-indicator)
    - [not recycled](#not-recycled)
    - [recycled](#recycled)
    - [recycling suspected](#recycling-suspected)
    - [unknown](#unknown)

- [reference material](#reference-material)
    - [other](#other)
    - [Pb Isotope CRMs](#pb-isotope-crms)
        - [BCR-2](#bcr-2)
            - [BCR-2G](#bcr-2g)
        - [BHVO-2](#bhvo-2)
            - [BHVO-2G](#bhvo-2g)
        - [BIR-1](#bir-1)
            - [BIR-1G](#bir-1g)
        - [ERM-3800](#erm-3800)
        - [GSD-1](#gsd-1)
            - [GSD-1G](#gsd-1g)
        - [NIST SRM 3328](#nist-srm-3328)
        - [NIST SRM 610](#nist-srm-610)
        - [NIST SRM 612](#nist-srm-612)
        - [NIST SRM 614](#nist-srm-614)
        - [NIST SRM 981](#nist-srm-981)
    - [Tl isotope CRMs](#tl-isotope-crms)
        - [ERM-AE649](#erm-ae649)
        - [NIST SRM 997](#nist-srm-997)
    - [unknown](#unknown)

- [registry](#registry)
    - [gazetteer](#gazetteer)
        - [Geonames](#geonames)
        - [iDAI.gazetteer](#idai.gazetteer)
        - [PeriodO](#periodo)
        - [Pleiades](#pleiades)
        - [TGN](#tgn)
        - [WHG](#whg)
    - [GND](#gnd)
    - [iDAI ChronOntology](#idai-chronontology)
    - [ORCID](#orcid)

- [relationType](#relationtype)
    - [Cites](#cites)
    - [Collects](#collects)
    - [Compiles](#compiles)
    - [Continues](#continues)
    - [Describes](#describes)
    - [Documents](#documents)
    - [HasMetadata](#hasmetadata)
    - [HasPart](#haspart)
    - [HasTranslation](#hastranslation)
    - [HasVersion](#hasversion)
    - [IsCitedBy](#iscitedby)
    - [IsCollectedBy](#iscollectedby)
    - [IsCompiledBy](#iscompiledby)
    - [IsContinuedBy](#iscontinuedby)
    - [IsDerivedFrom](#isderivedfrom)
    - [IsDescribedBy](#isdescribedby)
    - [IsDocumentedBy](#isdocumentedby)
    - [IsIdenticalTo](#isidenticalto)
    - [IsMetadataFor](#ismetadatafor)
    - [IsNewVersionOf](#isnewversionof)
    - [IsObsoletedBy](#isobsoletedby)
    - [IsOriginalFormOf](#isoriginalformof)
    - [IsPartOf](#ispartof)
    - [IsPreviousVersionOf](#ispreviousversionof)
    - [IsPublishedIn](#ispublishedin)
    - [IsReferencedBy](#isreferencedby)
    - [IsRequiredBy](#isrequiredby)
    - [IsReviewedBy](#isreviewedby)
    - [IsSourceOf](#issourceof)
    - [IsSupplementedBy](#issupplementedby)
    - [IsSupplementTo](#issupplementto)
    - [IsTranslationOf](#istranslationof)
    - [IsVariantFormOf](#isvariantformof)
    - [IsVersionOf](#isversionof)
    - [Obsoletes](#obsoletes)
    - [References](#references)
    - [Requires](#requires)
    - [Reviews](#reviews)

- [resourceType](#resourcetype)
    - [Audiovisual](#audiovisual)
    - [Award](#award)
    - [Book](#book)
    - [BookChapter](#bookchapter)
    - [Collection (ResourceType)](#collection-(resourcetype))
    - [ComputationalNotebook](#computationalnotebook)
    - [ConferencePaper](#conferencepaper)
    - [ConferenceProceeding](#conferenceproceeding)
    - [DataPaper](#datapaper)
    - [Dataset](#dataset)
    - [Dissertation](#dissertation)
    - [Event](#event)
    - [Image](#image)
    - [Instrument](#instrument)
    - [InteractiveResource](#interactiveresource)
    - [Journal](#journal)
    - [JournalArticle](#journalarticle)
    - [Model](#model)
    - [Other (resourceType)](#other-(resourcetype))
    - [OutputManagementPlan](#outputmanagementplan)
    - [PeerReview](#peerreview)
    - [PhysicalObject](#physicalobject)
    - [Preprint](#preprint)
    - [Project](#project)
    - [Report](#report)
    - [Service](#service)
    - [Software](#software)
    - [Sound](#sound)
    - [Standard](#standard)
    - [StudyRegistration](#studyregistration)
    - [Text](#text)
    - [Workflow](#workflow)

- [sample access](#sample-access)
    - [accessible](#accessible)
    - [destroyed](#destroyed)
    - [inaccessible](#inaccessible)
    - [lost](#lost)
    - [policy](#policy)
    - [unknown](#unknown)

- [sample housing](#sample-housing)
    - [cardboard box](#cardboard-box)
        - [acid-free cardboard box](#acid-free-cardboard-box)
        - [non acid-free cardboard box](#non-acid-free-cardboard-box)
    - [display case](#display-case)
        - [controlled environment display case](#controlled-environment-display-case)
        - [uncontrolled environment display case](#uncontrolled-environment-display-case)
    - [Eppendorf tube](#eppendorf-tube)
    - [fabric bag](#fabric-bag)
        - [cotton fabric bag](#cotton-fabric-bag)
        - [plastics fabric bag](#plastics-fabric-bag)
    - [glass vial](#glass-vial)
    - [no housing](#no-housing)
    - [paper bag](#paper-bag)
        - [acid-free paper bag](#acid-free-paper-bag)
        - [non acid-free paper bag](#non-acid-free-paper-bag)
    - [plastics bag](#plastics-bag)
        - [plastics fabric bag](#plastics-fabric-bag)
        - [ziplock bag](#ziplock-bag)
    - [PTFE/Teflon vial](#ptfe-teflon-vial)
    - [unknown](#unknown)

- [sample introduction](#sample-introduction)
    - [laser ablation](#laser-ablation)
    - [solution](#solution)

- [sample material](#sample-material)
    - [alteration product](#alteration-product)
        - [alteration product (anthropogenic)](#alteration-product-(anthropogenic))
        - [alteration product (hydrothermal)](#alteration-product-(hydrothermal))
        - [alteration product (supergene)](#alteration-product-(supergene))
    - [anthropogenic material](#anthropogenic-material)
        - [alteration product (anthropogenic)](#alteration-product-(anthropogenic))
        - [ceramic](#ceramic)
        - [glass](#glass)
        - [metal](#metal)
            - [coin](#coin)
        - [pigment](#pigment)
        - [unaltered material](#unaltered-material)
    - [bulk](#bulk)
    - [geological material](#geological-material)
        - [gossan](#gossan)
        - [host rock](#host-rock)
        - [mineral](#mineral)
        - [ore](#ore)
            - [alteration](#alteration)
            - [ore mineral](#ore-mineral)
                - [major mineral](#major-mineral)
                - [minor mineral](#minor-mineral)
            - [primary ore](#primary-ore)
            - [secondary ore](#secondary-ore)
        - [sediment](#sediment)
        - [unaltered material](#unaltered-material)
        - [wall rock](#wall-rock)
    - [unknown](#unknown)

- [sample state](#sample-state)
    - [material consumed](#material-consumed)
    - [modified](#modified)
    - [no material left](#no-material-left)
    - [unchanged](#unchanged)
    - [unknown](#unknown)

- [sample type](#sample-type)
    - [cut](#cut)
    - [drill shavings](#drill-shavings)
    - [hand specimen fragments](#hand-specimen-fragments)
    - [hand-picked](#hand-picked)
    - [in-situ](#in-situ)
    - [leachate](#leachate)
    - [loose material](#loose-material)
    - [mineral separate](#mineral-separate)
    - [powder](#powder)
    - [section](#section)
        - [polished section](#polished-section)
        - [thin section](#thin-section)
    - [swabbed material](#swabbed-material)
    - [unknown](#unknown)

- [sampling method](#sampling-method)
    - [ablating](#ablating)
    - [abrading](#abrading)
    - [crushing](#crushing)
    - [cutting](#cutting)
    - [dissolution](#dissolution)
        - [etching/leaching](#etching-leaching)
        - [swabbing](#swabbing)
    - [drilling](#drilling)
        - [micromill](#micromill)
    - [fragment collection](#fragment-collection)
    - [separation](#separation)
        - [density separation](#density-separation)
        - [hand-picking](#hand-picking)
        - [magnet separation](#magnet-separation)
    - [unknown](#unknown)

- [site type](#site-type)
    - [anthropogenic site](#anthropogenic-site)
        - [artefact scatter](#artefact-scatter)
        - [built structures](#built-structures)
            - [building](#building)
                - [administrative structure](#administrative-structure)
                - [agricultural structure](#agricultural-structure)
                - [communal structure](#communal-structure)
                - [house](#house)
                - [military structure](#military-structure)
                - [religious structure](#religious-structure)
                - [workshop](#workshop)
                    - [foundry](#foundry)
                    - [melting site](#melting-site)
                    - [non-metallurgical workshop](#non-metallurgical-workshop)
                    - [smelting site](#smelting-site)
            - [camp](#camp)
            - [infrastructure](#infrastructure)
                - [bridge](#bridge)
                - [road](#road)
            - [settlement](#settlement)
        - [funerary site](#funerary-site)
            - [burial cave](#burial-cave)
            - [burial ground](#burial-ground)
            - [grave](#grave)
            - [tomb](#tomb)
        - [hearth](#hearth)
        - [infilling](#infilling)
        - [isolated feature](#isolated-feature)
        - [mine](#mine)
            - [open pit mine](#open-pit-mine)
            - [underground mine](#underground-mine)
        - [mining-related site](#mining-related-site)
            - [mine dump](#mine-dump)
            - [mining project](#mining-project)
            - [mining sink-hole](#mining-sink-hole)
            - [ore beneficiation site](#ore-beneficiation-site)
            - [slag dump](#slag-dump)
            - [tailing dump](#tailing-dump)
        - [pit](#pit)
        - [post hole](#post-hole)
        - [refuse area](#refuse-area)
            - [debris dump](#debris-dump)
            - [midden](#midden)
            - [mine dump](#mine-dump)
            - [slag dump](#slag-dump)
            - [tailing dump](#tailing-dump)
        - [single find](#single-find)
        - [storage pit](#storage-pit)
    - [geological site](#geological-site)
        - [cave](#cave)
            - [burial cave](#burial-cave)
        - [deposit](#deposit)
        - [field](#field)
        - [locality](#locality)
        - [occurrence](#occurrence)
            - [outcrop](#outcrop)
    - [unknown](#unknown)

- [unit of measurement](#unit-of-measurement)
    - [concentration](#concentration)
        - [%](#%)
        - [at%](#at%)
        - [oxide%](#oxide%)
        - [wt%](#wt%)
        - [µg/g](#µg-g)
        - [µg/kg](#µg-kg)
    - [cps](#cps)
    - [distance](#distance)
        - [cm](#cm)
        - [km](#km)
        - [m](#m)
        - [mm](#mm)
    - [electric potential](#electric-potential)
        - [mV](#mv)
        - [V](#v)
    - [mass](#mass)
        - [g](#g)
        - [kg](#kg)
        - [mg](#mg)
        - [µg](#µg)
    - [time](#time)
        - [a](#a)
        - [Ma](#ma)

**Concepts**


##  abundance (concentration)
- **Definition**: A qualitative classification for the quantity of a
compund based on its concentration.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_60b698fb">http://vocab.terralid.org#c_60b698fb</a>


###  major
- **Definition**: Compound with a concentration of more than 0.4 wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0e342dcb">http://vocab.terralid.org#c_0e342dcb</a>


###  minor
- **Definition**: Compound with a concentration between 0.4 and 0.1
wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e954a190">http://vocab.terralid.org#c_e954a190</a>


###  trace
- **Definition**: Compound with a concentration of less than 0.1 wt%.
- **Child of**:
  - [`abundance (concentration)`](#abundance-(concentration))
- **References**:
  - [https://doi.org/10.1007/978-3-319-39193-9_255-1](https://doi.org/10.1007/978-3-319-39193-9_255-1)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29d78b2d">http://vocab.terralid.org#c_29d78b2d</a>



##  alteration extent
- **Definition**: The degree of the material's alteration.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4e14cebd">http://vocab.terralid.org#c_4e14cebd</a>


###  no alteration
- **Definition**: The material does not show any indication of
alteration.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb1223d0">http://vocab.terralid.org#c_eb1223d0</a>


###  severe alteration
- **Definition**: The material is altered to an extent that it is very
difficult or impossible to retrieve pristine material for analysis.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a9cb8f24">http://vocab.terralid.org#c_a9cb8f24</a>


###  slight alteration
- **Definition**: The material is altered but includes enough pristine
material for analyses.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e935826d">http://vocab.terralid.org#c_e935826d</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  alteration process
- **Definition**: The process of changing a material.
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300105442">http://vocab.getty.edu/aat/300105442</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8469dc11">http://vocab.terralid.org#c_8469dc11</a>


###  biodegradation
- **Definition**: The breakdown of usually organic matter by
microorganisms.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300419379">http://vocab.getty.edu/aat/300419379</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q696715">https://www.wikidata.org/wiki/Q696715</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_226caccd">http://vocab.terralid.org#c_226caccd</a>


###  darkening
- **Definition**: The loss of the materials brightness and depth.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379491">http://vocab.getty.edu/aat/300379491</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3ad03b3e">http://vocab.terralid.org#c_3ad03b3e</a>


###  efflorescense
- **Definition**: The migration of salt to the surface of a (porous)
material.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8855f5a4">http://vocab.terralid.org#c_8855f5a4</a>


###  erosion
- **Definition**: The loss of material through surface processes and
its deposition elsewhere.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300054116">http://vocab.getty.edu/aat/300054116</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dab8858f">http://vocab.terralid.org#c_dab8858f</a>


###  flaking
- **Definition**: The loss of adhesion of paint from its substrate
often but not necessarily in response to changes in the environment
like humidity or temperature.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q117289087">https://www.wikidata.org/wiki/Q117289087</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fdeb0d6c">http://vocab.terralid.org#c_fdeb0d6c</a>


###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`alteration process`](#alteration-process)
  - [`analytical instrument`](#analytical-instrument)
  - [`object material`](#object-material)
  - [`production process`](#production-process)
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc979f8">http://vocab.terralid.org#c_ebc979f8</a>


###  oxidation
- **Definition**: The reaction of the material with oxygen.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300220235">http://vocab.getty.edu/aat/300220235</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1786087">https://www.wikidata.org/wiki/Q1786087</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee0c9aa1">http://vocab.terralid.org#c_ee0c9aa1</a>


###  photodegradation
- **Definition**: The alteration of materials by light.
- **Child of**:
  - [`alteration process`](#alteration-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379409">http://vocab.getty.edu/aat/300379409</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1902073">https://www.wikidata.org/wiki/Q1902073</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f87cfd32">http://vocab.terralid.org#c_f87cfd32</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  analytical instrument
- **Definition**: Specialized devices used to determine the chemical
or physical properties of substances, especially their composition,
qunatity, or structure.
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q112270652">https://www.wikidata.org/wiki/Q112270652</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2490c7e3">http://vocab.terralid.org#c_2490c7e3</a>


###  instrument manufacturer
- **Child of**:
  - [`analytical instrument`](#analytical-instrument)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/0000075">https://vocabs.dariah.eu/bbt/Concept/0000075</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_79130afd">http://vocab.terralid.org#c_79130afd</a>


####  Finnigan MAT
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_02cf051c">http://vocab.terralid.org#c_02cf051c</a>


#####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5339ea48">http://vocab.terralid.org#c_5339ea48</a>


####  GV Instruments
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_42fb87d6">http://vocab.terralid.org#c_42fb87d6</a>


#####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b04217d9">http://vocab.terralid.org#c_b04217d9</a>


#####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** <a href="http://vocab.terralid.org#c_35bf64c9">http://vocab.terralid.org#c_35bf64c9</a>


####  Isotopx
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2b64e1c4">http://vocab.terralid.org#c_2b64e1c4</a>


#####  Phoenix
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Isotopx`](#isotopx)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** <a href="http://vocab.terralid.org#c_901bf3f2">http://vocab.terralid.org#c_901bf3f2</a>


####  Kunyuan Instrument
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f24d7f45">http://vocab.terralid.org#c_f24d7f45</a>


#####  GB-TIMS
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_44b7c5d2">http://vocab.terralid.org#c_44b7c5d2</a>


####  Micromass
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e95a8b9d">http://vocab.terralid.org#c_e95a8b9d</a>


#####  Sector 54
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Micromass`](#micromass)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00ccd58e">http://vocab.terralid.org#c_00ccd58e</a>


####  MSTech Group
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_de754362">http://vocab.terralid.org#c_de754362</a>


#####  ZMS DF-TIMS-01
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MSTech Group`](#mstech-group)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** <a href="http://vocab.terralid.org#c_52fa5991">http://vocab.terralid.org#c_52fa5991</a>


####  Nu Instruments
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_aef60277">http://vocab.terralid.org#c_aef60277</a>


#####  Plasma 1700
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2d9b9705">http://vocab.terralid.org#c_2d9b9705</a>


#####  Plasma 3
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a5774803">http://vocab.terralid.org#c_a5774803</a>


#####  Sapphire
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87e243c3">http://vocab.terralid.org#c_87e243c3</a>


#####  Sapphire XD
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d17aebe">http://vocab.terralid.org#c_1d17aebe</a>


#####  TIMS (Nu instruments)
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Nu Instruments`](#nu-instruments)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5a56c39c">http://vocab.terralid.org#c_5a56c39c</a>


####  SELMI
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_17ef5068">http://vocab.terralid.org#c_17ef5068</a>


#####  MI 1201-AT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`SELMI`](#selmi)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a81ab232">http://vocab.terralid.org#c_a81ab232</a>


####  Thermo Fisher Scientific
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f6af165b">http://vocab.terralid.org#c_f6af165b</a>


#####  Neoma
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b0bfa4f8">http://vocab.terralid.org#c_b0bfa4f8</a>


#####  Neptune
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** <a href="http://vocab.terralid.org#c_048dcdb6">http://vocab.terralid.org#c_048dcdb6</a>


#####  Neptune Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29e86132">http://vocab.terralid.org#c_29e86132</a>


#####  Triton Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11b1262d">http://vocab.terralid.org#c_11b1262d</a>


#####  Triton XT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** <a href="http://vocab.terralid.org#c_881a6a1f">http://vocab.terralid.org#c_881a6a1f</a>


####  Uralpribor
- **Child of**:
  - [`instrument manufacturer`](#instrument-manufacturer)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0979c452">http://vocab.terralid.org#c_0979c452</a>


#####  MIT 350-TM
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
  - [`Uralpribor`](#uralpribor)
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** <a href="http://vocab.terralid.org#c_48c98090">http://vocab.terralid.org#c_48c98090</a>


###  instrument model
- **Child of**:
  - [`analytical instrument`](#analytical-instrument)
- **Other Properties:**
  - **note**: 
https://analyte.me/instrument/gb-tims
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000017">https://vocabs.dariah.eu/bbt/Concept/000017</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_345d9da9">http://vocab.terralid.org#c_345d9da9</a>


####  GB-TIMS
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_44b7c5d2">http://vocab.terralid.org#c_44b7c5d2</a>


####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b04217d9">http://vocab.terralid.org#c_b04217d9</a>


####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** <a href="http://vocab.terralid.org#c_35bf64c9">http://vocab.terralid.org#c_35bf64c9</a>


####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5339ea48">http://vocab.terralid.org#c_5339ea48</a>


####  MI 1201-AT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`SELMI`](#selmi)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a81ab232">http://vocab.terralid.org#c_a81ab232</a>


####  MIT 350-TM
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
  - [`Uralpribor`](#uralpribor)
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** <a href="http://vocab.terralid.org#c_48c98090">http://vocab.terralid.org#c_48c98090</a>


####  Neoma
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b0bfa4f8">http://vocab.terralid.org#c_b0bfa4f8</a>


####  Neptune
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** <a href="http://vocab.terralid.org#c_048dcdb6">http://vocab.terralid.org#c_048dcdb6</a>


####  Neptune Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29e86132">http://vocab.terralid.org#c_29e86132</a>


####  Phoenix
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Isotopx`](#isotopx)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** <a href="http://vocab.terralid.org#c_901bf3f2">http://vocab.terralid.org#c_901bf3f2</a>


####  Plasma 1700
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2d9b9705">http://vocab.terralid.org#c_2d9b9705</a>


####  Plasma 3
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a5774803">http://vocab.terralid.org#c_a5774803</a>


####  Sapphire
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87e243c3">http://vocab.terralid.org#c_87e243c3</a>


####  Sapphire XD
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d17aebe">http://vocab.terralid.org#c_1d17aebe</a>


####  Sector 54
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Micromass`](#micromass)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00ccd58e">http://vocab.terralid.org#c_00ccd58e</a>


####  TIMS (Nu instruments)
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Nu Instruments`](#nu-instruments)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5a56c39c">http://vocab.terralid.org#c_5a56c39c</a>


####  Triton Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11b1262d">http://vocab.terralid.org#c_11b1262d</a>


####  Triton XT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** <a href="http://vocab.terralid.org#c_881a6a1f">http://vocab.terralid.org#c_881a6a1f</a>


####  ZMS DF-TIMS-01
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MSTech Group`](#mstech-group)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** <a href="http://vocab.terralid.org#c_52fa5991">http://vocab.terralid.org#c_52fa5991</a>


###  instrument type
- **Child of**:
  - [`analytical instrument`](#analytical-instrument)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e3df0ac6">http://vocab.terralid.org#c_e3df0ac6</a>


####  MC-ICP-MS (instrument)
- **Child of**:
  - [`instrument type`](#instrument-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4c5dbb51">http://vocab.terralid.org#c_4c5dbb51</a>


#####  IsoProbe-P
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-p](https://analyte.me/instrument/isoprobe-p)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b04217d9">http://vocab.terralid.org#c_b04217d9</a>


#####  Neoma
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neoma](https://analyte.me/instrument/neoma)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b0bfa4f8">http://vocab.terralid.org#c_b0bfa4f8</a>


#####  Neptune
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128](https://speciation.net/Database/Instruments/Thermo-Scientific/NEPTUNE-;i128)
- **Concept URI:** <a href="http://vocab.terralid.org#c_048dcdb6">http://vocab.terralid.org#c_048dcdb6</a>


#####  Neptune Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
- **References**:
  - [https://analyte.me/instrument/neptune-plus](https://analyte.me/instrument/neptune-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29e86132">http://vocab.terralid.org#c_29e86132</a>


#####  Plasma 1700
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-1700](https://analyte.me/instrument/plasma-1700)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2d9b9705">http://vocab.terralid.org#c_2d9b9705</a>


#####  Plasma 3
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/plasma-3](https://analyte.me/instrument/plasma-3)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a5774803">http://vocab.terralid.org#c_a5774803</a>


#####  Sapphire
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire](https://analyte.me/instrument/sapphire)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87e243c3">http://vocab.terralid.org#c_87e243c3</a>


#####  Sapphire XD
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MC-ICP-MS (instrument)`](#mc-icp-ms-(instrument))
  - [`Nu Instruments`](#nu-instruments)
- **References**:
  - [https://analyte.me/instrument/sapphire-xd](https://analyte.me/instrument/sapphire-xd)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d17aebe">http://vocab.terralid.org#c_1d17aebe</a>


####  TIMS (instrument)
- **Child of**:
  - [`instrument type`](#instrument-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_75732fae">http://vocab.terralid.org#c_75732fae</a>


#####  GB-TIMS
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Kunyuan Instrument`](#kunyuan-instrument)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/gb-tims](https://analyte.me/instrument/gb-tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_44b7c5d2">http://vocab.terralid.org#c_44b7c5d2</a>


#####  IsoProbe-T
- **Child of**:
  - [`GV Instruments`](#gv-instruments)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/isoprobe-t](https://analyte.me/instrument/isoprobe-t)
- **Concept URI:** <a href="http://vocab.terralid.org#c_35bf64c9">http://vocab.terralid.org#c_35bf64c9</a>


#####  MAT 262
- **Child of**:
  - [`Finnigan MAT`](#finnigan-mat)
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mat-262](https://analyte.me/instrument/mat-262)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5339ea48">http://vocab.terralid.org#c_5339ea48</a>


#####  MI 1201-AT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`SELMI`](#selmi)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/mi-1201-at](https://analyte.me/instrument/mi-1201-at)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a81ab232">http://vocab.terralid.org#c_a81ab232</a>


#####  MIT 350-TM
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`TIMS (instrument)`](#tims-(instrument))
  - [`Uralpribor`](#uralpribor)
- **References**:
  - [https://analyte.me/instrument/mti-350-tm](https://analyte.me/instrument/mti-350-tm)
- **Concept URI:** <a href="http://vocab.terralid.org#c_48c98090">http://vocab.terralid.org#c_48c98090</a>


#####  Phoenix
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Isotopx`](#isotopx)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/phoenix](https://analyte.me/instrument/phoenix)
- **Concept URI:** <a href="http://vocab.terralid.org#c_901bf3f2">http://vocab.terralid.org#c_901bf3f2</a>


#####  Sector 54
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Micromass`](#micromass)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/sector-54](https://analyte.me/instrument/sector-54)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00ccd58e">http://vocab.terralid.org#c_00ccd58e</a>


#####  TIMS (Nu instruments)
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Nu Instruments`](#nu-instruments)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/tims](https://analyte.me/instrument/tims)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5a56c39c">http://vocab.terralid.org#c_5a56c39c</a>


#####  Triton Plus
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-plus](https://analyte.me/instrument/triton-plus)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11b1262d">http://vocab.terralid.org#c_11b1262d</a>


#####  Triton XT
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`Thermo Fisher Scientific`](#thermo-fisher-scientific)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/triton-xt](https://analyte.me/instrument/triton-xt)
- **Concept URI:** <a href="http://vocab.terralid.org#c_881a6a1f">http://vocab.terralid.org#c_881a6a1f</a>


#####  ZMS DF-TIMS-01
- **Child of**:
  - [`instrument model`](#instrument-model)
  - [`MSTech Group`](#mstech-group)
  - [`TIMS (instrument)`](#tims-(instrument))
- **References**:
  - [https://analyte.me/instrument/zms-df-tims-01](https://analyte.me/instrument/zms-df-tims-01)
- **Concept URI:** <a href="http://vocab.terralid.org#c_52fa5991">http://vocab.terralid.org#c_52fa5991</a>


###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`alteration process`](#alteration-process)
  - [`analytical instrument`](#analytical-instrument)
  - [`object material`](#object-material)
  - [`production process`](#production-process)
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc979f8">http://vocab.terralid.org#c_ebc979f8</a>



##  analytical method
- **Definition**: Procedures that operate on material samples to
produce observation results with information about the physical
properties, chemical or isotopic composition, crystallography, or
molecular structure of the sample.
- **Other Properties:**
  - **note**: 
Definition taken from: Richard, S. M., Klöcking, M., Luzi-Helbing, M., Johansson, A., Profeta, L., Lehnert, K., Elangovan, P., Sweets, H.A., Kallas, L., Sarbas, B., Mays, J., 2024. Analytical Methods for Geochemistry and Cosmochemistry. Concept Scheme for Analysis Methods in Geo- and Cosmochemistry. Published at Research Vocabularies Australia. Version 1.4.  https://vocabs.ardc.edu.au/viewById/650, published under a CC-BY license (version number of the license not provided). 
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/analyticalmethod">https://w3id.org/geochem/1.0/analyticalmethod/analyticalmethod</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q4751159">https://www.wikidata.org/wiki/Q4751159</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c1c261a2">http://vocab.terralid.org#c_c1c261a2</a>


###  atomic absorption spectroscopy
- **Definition**: Analytical methods using the characteristic optical
absorption of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q655346">https://www.wikidata.org/wiki/Q655346</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d1ac5ad6">http://vocab.terralid.org#c_d1ac5ad6</a>


####  AAS (flame)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by a flame.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7db2dd2">http://vocab.terralid.org#c_d7db2dd2</a>


####  AAS (glow-discharge)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by glow-
discharge.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/atomicabsorptionspectrometry</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ea3b1b8c">http://vocab.terralid.org#c_ea3b1b8c</a>


####  AAS (graphite furnace)
- **Definition**: Determination of the chemical composition by the
optical absorption of a heated samples. Heat is induced by a graphite
furnace.
- **Child of**:
  - [`atomic absorption spectroscopy`](#atomic-absorption-spectroscopy)
- **Alternate labels:**
  - ET-AAS
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/electrothermalabsorptionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/electrothermalabsorptionspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8d344a67">http://vocab.terralid.org#c_8d344a67</a>


###  emission spectrometry
- **Definition**: Analytical methods using the characteristic optical
emission of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1651219">https://www.wikidata.org/wiki/Q1651219</a> (exactMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/emissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/emissionspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3d79fcf3">http://vocab.terralid.org#c_3d79fcf3</a>


####  AES (flame)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Heat is induced by a flame.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q186548">https://www.wikidata.org/wiki/Q186548</a> (closeMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/flameemissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/flameemissionspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c7c72d4">http://vocab.terralid.org#c_6c7c72d4</a>


####  AES (graphite furnace)
- **Definition**: Determination of the chemical composition by optimal
emission of a heated sample. Sample is heated in a graphite furnace.
- **Child of**:
  - [`emission spectrometry`](#emission-spectrometry)
- **Other Properties:**
  - **scopeNote**: 
The only difference between OES and AES seems to be the simultaneous vs. sequential analysis of elements (https://www.drawellanalytical.com/spectrophotometer/inductively-coupled-plasma-emission-spectrometericp-aes-icp-oes/).
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q186548">https://www.wikidata.org/wiki/Q186548</a> (closeMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/plasmaemissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/plasmaemissionspectrometry</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0a6e5db7">http://vocab.terralid.org#c_0a6e5db7</a>


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
  - <a href="https://www.wikidata.org/wiki/Q186548">https://www.wikidata.org/wiki/Q186548</a> (closeMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/plasmaopticalemissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/plasmaopticalemissionspectrometry</a> (closeMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmaopticalemissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmaopticalemissionspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q186548">https://www.wikidata.org/wiki/Q186548</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_67246a66">http://vocab.terralid.org#c_67246a66</a>


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
  - <a href="https://www.wikidata.org/wiki/Q186548">https://www.wikidata.org/wiki/Q186548</a> (broadMatch)
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/opticalemissionspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/opticalemissionspectrometry</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3687738e">http://vocab.terralid.org#c_3687738e</a>


###  mass spectrometer
- **Definition**: An analytical instrument in which the sample is
ionised, the ions separated and detected according to their mass-to-
charge ratio.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/massspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/massspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q180809">https://www.wikidata.org/wiki/Q180809</a> (exactMatch)
  - <a href="https://vocab.getty.edu/aat/300225881">https://vocab.getty.edu/aat/300225881</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c0d215f3">http://vocab.terralid.org#c_c0d215f3</a>


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
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmamassspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/inductivelycoupledplasmamassspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q900680">https://www.wikidata.org/wiki/Q900680</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_32908a70">http://vocab.terralid.org#c_32908a70</a>


#####  LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, introduced into an inductively coupled plasma to
atomize and ionize the sample for inlet to mass analyzer.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/laserablationinductivelycoupledplasmamassspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/laserablationinductivelycoupledplasmamassspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q108900669">https://www.wikidata.org/wiki/Q108900669</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6b7986e4">http://vocab.terralid.org#c_6b7986e4</a>


######  fs-LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range,
introduced into an inductively coupled plasma to atomize and ionize
the sample for inlet to mass analyzer.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0cd648d6">http://vocab.terralid.org#c_0cd648d6</a>


######  LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, ionised by an inductively coupled plasma and ions
detected by an array of several detectors.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
  - [`MC-ICP-MS`](#mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7b1b4216">http://vocab.terralid.org#c_7b1b4216</a>


#######  fs-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e56f0531">http://vocab.terralid.org#c_e56f0531</a>


#######  ns-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e1700c12">http://vocab.terralid.org#c_e1700c12</a>


######  ns-LA-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range,
introduced into an inductively coupled plasma to atomize and ionize
the sample for inlet to mass analyzer.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19f6f6d5">http://vocab.terralid.org#c_19f6f6d5</a>


#####  MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ionised by
an inductively coupled plasma and ions detected by an array of several
detectors.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/multicollectorinductivelycoupledplasmamassspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/multicollectorinductivelycoupledplasmamassspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d0d46a2c">http://vocab.terralid.org#c_d0d46a2c</a>


######  LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam, ionised by an inductively coupled plasma and ions
detected by an array of several detectors.
- **Child of**:
  - [`LA-ICP-MS`](#la-icp-ms)
  - [`MC-ICP-MS`](#mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7b1b4216">http://vocab.terralid.org#c_7b1b4216</a>


#######  fs-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the femtosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e56f0531">http://vocab.terralid.org#c_e56f0531</a>


#######  ns-LA-MC-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ablated
with a laser beam with laser pulses in the nanosecond range, ionised
by an inductively coupled plasma and ions detected by an array of
several detectors.
- **Child of**:
  - [`LA-MC-ICP-MS`](#la-mc-icp-ms)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e1700c12">http://vocab.terralid.org#c_e1700c12</a>


#####  Q-ICP-MS
- **Definition**: Mass spectrometer in which the sample is ionised by
an inductively coupled plasma, iones separated by mass with a
quadrupole and detected by single dectector.
- **Child of**:
  - [`ICP-MS`](#icp-ms)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/quadrupoleinductivelycoupledplasmmassspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/quadrupoleinductivelycoupledplasmmassspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8e269b3e">http://vocab.terralid.org#c_8e269b3e</a>


####  TIMS
- **Definition**: Mass spectrometer in which the sample is placed on a
filament and ionised by heating the filament. With respect to lead
isotope analyses, mass detection by a detector array in implied.
- **Child of**:
  - [`mass spectrometer`](#mass-spectrometer)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/thermalionizationmassspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/thermalionizationmassspectrometry</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e7d3223e">http://vocab.terralid.org#c_e7d3223e</a>


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
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/neutronactivationanalysis">https://w3id.org/geochem/1.0/analyticalmethod/neutronactivationanalysis</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300081742">http://vocab.getty.edu/aat/300081742</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4a54f6dc">http://vocab.terralid.org#c_4a54f6dc</a>


###  wet chemistry
- **Definition**: Determination of the chemical composition by
traditional chemical methods.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/wetchemistry">https://w3id.org/geochem/1.0/analyticalmethod/wetchemistry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2963660">https://www.wikidata.org/wiki/Q2963660</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4bf47ef2">http://vocab.terralid.org#c_4bf47ef2</a>


###  X-ray spectrometry
- **Definition**: Analytical methods using the characteristic X-ray
spectra of chemical elements for identification and quantification.
- **Child of**:
  - [`analytical method`](#analytical-method)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/xrayspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/xrayspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q901775">https://www.wikidata.org/wiki/Q901775</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f7856e7e">http://vocab.terralid.org#c_f7856e7e</a>


####  ED-XRF
- **Definition**: Determination of the chemical composition by the
energy dispersive spectroscopy of X-ray fluorescence.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry">https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q112259854">https://www.wikidata.org/wiki/Q112259854</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a6a0ae84">http://vocab.terralid.org#c_a6a0ae84</a>


#####  pXRF
- **Definition**: Determination of the chemical composition by the
energy dispersive spectroscopy of X-ray fluorescence with a handheld
instrument.
- **Child of**:
  - [`ED-XRF`](#ed-xrf)
- **Alternate labels:**
  - hhXRF
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry">https://w3id.org/geochem/1.0/analyticalmethod/energydispersivexrayfluorescencespectrometry</a> (broadMatch)
  - <a href="https://www.wikidata.org/wiki/Q112259854">https://www.wikidata.org/wiki/Q112259854</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f1be908f">http://vocab.terralid.org#c_f1be908f</a>


####  EPMA
- **Definition**: Determination of the chemical composition by
electron-induced wavelength dispersive X-ray spectrometry in a
microprobe.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Alternate labels:**
  - microprobe
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/quantitativeanalysiselectroninducedxrayspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/quantitativeanalysiselectroninducedxrayspectrometry</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q911272">https://www.wikidata.org/wiki/Q911272</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_912285bf">http://vocab.terralid.org#c_912285bf</a>


####  SEM-EDS
- **Definition**: Determination of the chemical composition by
electron-induced energy-dispersive X-ray spectrometry in a scanning
electron microscope.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Alternate labels:**
  - SEM-EDX
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/energydispersiveelectroninducedxrayspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/energydispersiveelectroninducedxrayspectrometry</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q321095">https://www.wikidata.org/wiki/Q321095</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2344bc38">http://vocab.terralid.org#c_2344bc38</a>


####  WD-XRF
- **Definition**: Determination of the chemical composition by the
wavelength dispersive spectroscopy of X-ray fluorescence.
- **Child of**:
  - [`X-ray spectrometry`](#x-ray-spectrometry)
- **Matches:**
  - <a href="https://w3id.org/geochem/1.0/analyticalmethod/wavelengthdispersiveelectroninducedxrayspectrometry">https://w3id.org/geochem/1.0/analyticalmethod/wavelengthdispersiveelectroninducedxrayspectrometry</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q899530">https://www.wikidata.org/wiki/Q899530</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_85bc0576">http://vocab.terralid.org#c_85bc0576</a>



##  analytical uncertainty
- **Definition**: An expression for the statistical dispersion of a
measured value.
- **Alternate labels:**
  - measurement uncertainty
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1403517">https://www.wikidata.org/wiki/Q1403517</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6ae288a3">http://vocab.terralid.org#c_6ae288a3</a>


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
  - <a href="http://purl.obolibrary.org/obo/STATO_0000237">http://purl.obolibrary.org/obo/STATO_0000237</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q159375">https://www.wikidata.org/wiki/Q159375</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ed11712a">http://vocab.terralid.org#c_ed11712a</a>


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
  - <a href="http://purl.obolibrary.org/obo/STATO_0000037">http://purl.obolibrary.org/obo/STATO_0000037</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q620994">https://www.wikidata.org/wiki/Q620994</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1c8f3d46">http://vocab.terralid.org#c_1c8f3d46</a>



##  assemblage
- **Definition**: Grouping of items or specimens resulting from human
activity for archaeological materials or environmental and tectonic
processes for geological materials.
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300256847">http://vocab.getty.edu/aat/300256847</a> (closeMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
  - <a href="http://vocab.getty.edu/aat/300241507">http://vocab.getty.edu/aat/300241507</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0fab0ef9">http://vocab.terralid.org#c_0fab0ef9</a>


###  alteration product (hydrothermal)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by hydrothermal solutions.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b81f7872">http://vocab.terralid.org#c_b81f7872</a>


###  alteration product (supergene)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by weathering.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4468f4e">http://vocab.terralid.org#c_f4468f4e</a>


###  collection
- **Definition**: Accumulations of objects according to certain topics
or characteristics that do not necessarily share a common provenance.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to be used only for objects and samples with unknown archaeological context. 
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300025976">http://vocab.getty.edu/aat/300025976</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2668072">https://www.wikidata.org/wiki/Q2668072</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d0a53b23">http://vocab.terralid.org#c_d0a53b23</a>


###  components
- **Definition**: Objects that are intended to be always used or
present in connection with other components, such as a rivet.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to identify assemblages resulting from the detachment of previously combined components which are recorded individually. 
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300241583">http://vocab.getty.edu/aat/300241583</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1310239">https://www.wikidata.org/wiki/Q1310239</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_665746e2">http://vocab.terralid.org#c_665746e2</a>


###  gangue
- **Definition**: The part of an ore not deemed economically
desirable.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/gangue">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/gangue</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1061670">https://www.wikidata.org/wiki/Q1061670</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_235c43fb">http://vocab.terralid.org#c_235c43fb</a>


###  gossan
- **Definition**: The outcropping, heavily weathered part of a
mineralisation.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan">http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q639293">https://www.wikidata.org/wiki/Q639293</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e6cf20b1">http://vocab.terralid.org#c_e6cf20b1</a>


###  hoard
- **Definition**: Group of objects that were accumulated with the aim
to be buried or hidden.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300195474">http://vocab.getty.edu/aat/300195474</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q164099">https://www.wikidata.org/wiki/Q164099</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5f8d30a4">http://vocab.terralid.org#c_5f8d30a4</a>


###  host rock
- **Definition**: The country rock or rock body in which a
mineralisation occurs.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9c0fc70d">http://vocab.terralid.org#c_9c0fc70d</a>


###  item
- **Definition**: A single object.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Other Properties:**
  - **scopeNote**: 
Intended to identify that the items does not belong to an assemblage, or that the assemblage contains only one item. 
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300404024">http://vocab.getty.edu/aat/300404024</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5f249aa8">http://vocab.terralid.org#c_5f249aa8</a>


###  ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (exactMatch)
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771</a> (exactMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/raw-material-role/ore">http://resource.geosciml.org/classifier/cgi/raw-material-role/ore</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300152583">http://vocab.getty.edu/aat/300152583</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4dffb82b">http://vocab.terralid.org#c_4dffb82b</a>


####  alteration
- **Definition**: The part of the ore that is affected by natural
post-genetic processes, often including interaction with a hydrous
fluid.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (exactMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/eventprocess/alteration">http://resource.geosciml.org/classifier/cgi/eventprocess/alteration</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_27e6e534">http://vocab.terralid.org#c_27e6e534</a>


####  ore mineral
- **Definition**: The economically viable part of the ore.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/raw-material-role/ore">http://resource.geosciml.org/classifier/cgi/raw-material-role/ore</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1969263">https://www.wikidata.org/wiki/Q1969263</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_39a52896">http://vocab.terralid.org#c_39a52896</a>


#####  major mineral
- **Definition**: An economically viable mineral dominating the ore's
mineralogical composition.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e9f3cf6">http://vocab.terralid.org#c_6e9f3cf6</a>


#####  minor mineral
- **Definition**: An economically viable mineral constituting a minor
part in the ore's mineralogy.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** <a href="http://vocab.terralid.org#c_42b68c9f">http://vocab.terralid.org#c_42b68c9f</a>


####  primary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was not altered by hydrothermal
processes or weathering.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1823779e">http://vocab.terralid.org#c_1823779e</a>


####  secondary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was altered by hydrothermal
processes or weathering. The term usually refers to ore that became
enriched in the targeted elements because of alteration processes.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_adc64d1b">http://vocab.terralid.org#c_adc64d1b</a>


###  set
- **Definition**: Objects purposely combined to be used as group.
- **Child of**:
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300133146">http://vocab.getty.edu/aat/300133146</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_db7df3e1">http://vocab.terralid.org#c_db7df3e1</a>


###  wall rock
- **Definition**: The section of the host rock that was affected by
epigenetic processes resulting in the mineralisation.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_25814b64">http://vocab.terralid.org#c_25814b64</a>



##  authenticity
- **Definition**: Whether the object is a genuine representation or an
imitation.
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300055848">http://vocab.getty.edu/aat/300055848</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q13431773">https://www.wikidata.org/wiki/Q13431773</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_78d89252">http://vocab.terralid.org#c_78d89252</a>


###  contemporary imitation
- **Definition**: The object is a contemporary imitation of an other
object.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Matches:**
  - <a href="http://nomisma.org/id/contemporary_imitation">http://nomisma.org/id/contemporary_imitation</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1e12e502">http://vocab.terralid.org#c_1e12e502</a>


###  genuine
- **Definition**: The object is authentic.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Alternate labels:**
  - official, 
  - authentic, 
- **Matches:**
  - <a href="http://nomisma.org/id/official">http://nomisma.org/id/official</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_149b5682">http://vocab.terralid.org#c_149b5682</a>


###  modern imitation
- **Definition**: The object is a imitation of an other object that
was produced when the original object was not in use or circulation.
- **Child of**:
  - [`authenticity`](#authenticity)
- **Matches:**
  - <a href="http://nomisma.org/id/modern_imitation">http://nomisma.org/id/modern_imitation</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9c8f2a35">http://vocab.terralid.org#c_9c8f2a35</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  colour system
- **Definition**: Definition of a geometrical space or nomenclature
that represents colours.
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300311091">http://vocab.getty.edu/aat/300311091</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1396457">https://www.wikidata.org/wiki/Q1396457</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_49d4f3c8">http://vocab.terralid.org#c_49d4f3c8</a>


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
  - <a href="https://www.wikidata.org/wiki/Q375414">https://www.wikidata.org/wiki/Q375414</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4f63611c">http://vocab.terralid.org#c_4f63611c</a>


###  eye
- **Definition**: The colour as perceived by a person.
- **Child of**:
  - [`colour system`](#colour-system)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q7364">https://www.wikidata.org/wiki/Q7364</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_63dd4d16">http://vocab.terralid.org#c_63dd4d16</a>


###  Munsell
- **Definition**: A colour system developed by A. H. Munsell in the
early 20th century.
- **Child of**:
  - [`colour system`](#colour-system)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q768549">https://www.wikidata.org/wiki/Q768549</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300311089">http://vocab.getty.edu/aat/300311089</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ffd62f45">http://vocab.terralid.org#c_ffd62f45</a>



##  compound origin
- **Definition**: Information whether the compound can be found in
nature or is of articial origin.
- **Concept URI:** <a href="http://vocab.terralid.org#c_786deece">http://vocab.terralid.org#c_786deece</a>


###  mixed compound origin
- **Definition**: The material consists of natural and sythetic
compounds.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29195cbf">http://vocab.terralid.org#c_29195cbf</a>


###  natural
- **Definition**: The material's compounds occur in nature.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300219527">http://vocab.getty.edu/aat/300219527</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dc16b4b3">http://vocab.terralid.org#c_dc16b4b3</a>


###  synthetic
- **Definition**: The material's compounds were created by humans from
other constituents.
- **Child of**:
  - [`compound origin`](#compound-origin)
- **Alternate labels:**
  - artifical
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300218678">http://vocab.getty.edu/aat/300218678</a> (closeMatch)
  - <a href="http://vocab.getty.edu/aat/300191749">http://vocab.getty.edu/aat/300191749</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d140627e">http://vocab.terralid.org#c_d140627e</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  compound type
- **Definition**: The chemical nature of a compound.
- **Concept URI:** <a href="http://vocab.terralid.org#c_f09f29c5">http://vocab.terralid.org#c_f09f29c5</a>


###  inorganic
- **Definition**: The material consists of inorganic (i.e. not carbon-
based) chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300191633">http://vocab.getty.edu/aat/300191633</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2211a2a4">http://vocab.terralid.org#c_2211a2a4</a>


###  mixed compound types
- **Definition**: The material consists of inorganic and organic
chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300206579">http://vocab.getty.edu/aat/300206579</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d97d70ac">http://vocab.terralid.org#c_d97d70ac</a>


###  organic
- **Definition**: The material consists of organic (i.e. carbon-based)
chemical compounds.
- **Child of**:
  - [`compound type`](#compound-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300191632">http://vocab.getty.edu/aat/300191632</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_627d4ccf">http://vocab.terralid.org#c_627d4ccf</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  context type
- **Definition**: Information about whether an (archaeological)
context includes material from a single depositional event and whether
the context is impacted by any post-depositional processes.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ca223f0b">http://vocab.terralid.org#c_ca223f0b</a>


###  disturbed context
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Alternate labels:**
  - secondary context
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q136826785">https://www.wikidata.org/wiki/Q136826785</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0faa6b29">http://vocab.terralid.org#c_0faa6b29</a>


####  anthropogenically disturbed
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with humans being the
responsible agents.
- **Child of**:
  - [`disturbed context`](#disturbed-context)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9408f513">http://vocab.terralid.org#c_9408f513</a>


####  biogenically disturbed
- **Definition**: The material in the context represents multiple
depositional events or it was interacted with non-humans being the
responsible agents (e.g. bioturbidation).
- **Child of**:
  - [`disturbed context`](#disturbed-context)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1c4bfb96">http://vocab.terralid.org#c_1c4bfb96</a>


###  mixed context
- **Definition**: The context represents a single depositional event
with material coming from multiple sources and no interaction
happening after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a0ae7ce8">http://vocab.terralid.org#c_a0ae7ce8</a>


###  undisturbed context
- **Definition**: The context represents a single depositional event
with all material coming from the same source and no interaction
happening after its deposition.
- **Child of**:
  - [`context type`](#context-type)
- **Alternate labels:**
  - primary context
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q136826284">https://www.wikidata.org/wiki/Q136826284</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0541320f">http://vocab.terralid.org#c_0541320f</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  contributorType
- **Definition**: The type of contributor of the resource.
- **Other Properties:**
  - **note**: 
This is a reproduction of the controlled list contributorType in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/0000074">https://vocabs.dariah.eu/bbt/Concept/0000074</a> (broadMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e4ed600b">http://vocab.terralid.org#c_e4ed600b</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_34e78a4f">http://vocab.terralid.org#c_34e78a4f</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f5974a2b">http://vocab.terralid.org#c_f5974a2b</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_eed9b69e">http://vocab.terralid.org#c_eed9b69e</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_8034b473">http://vocab.terralid.org#c_8034b473</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_62875695">http://vocab.terralid.org#c_62875695</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_36d34fdb">http://vocab.terralid.org#c_36d34fdb</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_041e374c">http://vocab.terralid.org#c_041e374c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_3a208ae6">http://vocab.terralid.org#c_3a208ae6</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_7250b71d">http://vocab.terralid.org#c_7250b71d</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd32fd29">http://vocab.terralid.org#c_dd32fd29</a>


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
  - <a href="https://www.wikidata.org/wiki/Q816432">https://www.wikidata.org/wiki/Q816432</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmanager](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#projectmanager)
- **Concept URI:** <a href="http://vocab.terralid.org#c_384d11d1">http://vocab.terralid.org#c_384d11d1</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_c6bb8064">http://vocab.terralid.org#c_c6bb8064</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8f80f6c">http://vocab.terralid.org#c_c8f80f6c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc3e072">http://vocab.terralid.org#c_ebc3e072</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_ad00bdad">http://vocab.terralid.org#c_ad00bdad</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1650915">https://www.wikidata.org/wiki/Q1650915</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researcher](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researcher)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e1f2cf05">http://vocab.terralid.org#c_e1f2cf05</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1241025">https://www.wikidata.org/wiki/Q1241025</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researchgroup](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#researchgroup)
- **Concept URI:** <a href="http://vocab.terralid.org#c_57b3dd9a">http://vocab.terralid.org#c_57b3dd9a</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f18d65a2">http://vocab.terralid.org#c_f18d65a2</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_8ff2aeb0">http://vocab.terralid.org#c_8ff2aeb0</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_2f9a64df">http://vocab.terralid.org#c_2f9a64df</a>


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
  - <a href="https://www.wikidata.org/wiki/Q333634">https://www.wikidata.org/wiki/Q333634</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#translator](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/contributorType/#translator)
- **Concept URI:** <a href="http://vocab.terralid.org#c_79574dab">http://vocab.terralid.org#c_79574dab</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_50da8fc6">http://vocab.terralid.org#c_50da8fc6</a>



##  corrosion extent
- **Definition**: The degree to which a material is affected by
corrosion.
- **Concept URI:** <a href="http://vocab.terralid.org#c_3ba0ff02">http://vocab.terralid.org#c_3ba0ff02</a>


###  moderate corrosion
- **Definition**: Corrosion products are widely present but uncorroded
material can still be readily found.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1dba855c">http://vocab.terralid.org#c_1dba855c</a>


###  no corrosion
- **Definition**: The material does not show any indication of
corrosion.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_16a7b2ad">http://vocab.terralid.org#c_16a7b2ad</a>


###  severe corrosion
- **Definition**: The material consists mostly of corrosion products
and it requires close observation to find uncorroded material.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_372633f8">http://vocab.terralid.org#c_372633f8</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>


###  weak corrosion
- **Definition**: The material has only surficial or spatially very
limited corrosion.
- **Child of**:
  - [`corrosion extent`](#corrosion-extent)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bb54a1e5">http://vocab.terralid.org#c_bb54a1e5</a>



##  date type
- **Definition**: Whether a date refers to an archaeological or
geological event or period.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000005">https://vocabs.dariah.eu/bbt/Concept/000005</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5592fbc1">http://vocab.terralid.org#c_5592fbc1</a>


###  archaeological
- **Definition**: Adjective of "archaeology", which refers to the
study of the human past.
- **Child of**:
  - [`date type`](#date-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee0cd6f1">http://vocab.terralid.org#c_ee0cd6f1</a>


###  geological
- **Definition**: Adjective of "geology", which refers to the study of
the Earth's history, composition, structure, physical properties and
relevant processes.
- **Child of**:
  - [`date type`](#date-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_de82ab14">http://vocab.terralid.org#c_de82ab14</a>



##  dating technique
- **Definition**: Determining the date of an event or in time or
relatively to other other events.
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300054714">http://vocab.getty.edu/aat/300054714</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q97359583">https://www.wikidata.org/wiki/Q97359583</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_458c8d5b">http://vocab.terralid.org#c_458c8d5b</a>


###  absolute dating
- **Definition**: Dating technique that results dates in calendar
years.
- **Child of**:
  - [`dating technique`](#dating-technique)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300224276">http://vocab.getty.edu/aat/300224276</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q332423">https://www.wikidata.org/wiki/Q332423</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_70421df0">http://vocab.terralid.org#c_70421df0</a>


####  dendrochronology
- **Definition**: The measurement of a sequence of tree growth rings
and their relative differences in width and the comparison of this
information to known reference curves.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300054715">http://vocab.getty.edu/aat/300054715</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q80205">https://www.wikidata.org/wiki/Q80205</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bf02bc84">http://vocab.terralid.org#c_bf02bc84</a>


####  lichenometry
- **Definition**: The measurement of lichens' size on rock surfaces.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300380350">http://vocab.getty.edu/aat/300380350</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1432441">https://www.wikidata.org/wiki/Q1432441</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e71424b2">http://vocab.terralid.org#c_e71424b2</a>


####  luminescence dating
- **Definition**: The measurement of the released stored energy in a
material in the form of light to determine the material's age.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300266049">http://vocab.getty.edu/aat/300266049</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_14f0b363">http://vocab.terralid.org#c_14f0b363</a>


#####  optically stimulated luminescence dating
- **Definition**: The measurement of the stored energy in a material
in the form of light released by exposing the material to a strong
light source (e.g. lamp or laser) to determine the material's age.
- **Child of**:
  - [`luminescence dating`](#luminescence-dating)
- **Alternate labels:**
  - OSL
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300266050">http://vocab.getty.edu/aat/300266050</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q4335524">https://www.wikidata.org/wiki/Q4335524</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8d044281">http://vocab.terralid.org#c_8d044281</a>


#####  thermoluminescence dating
- **Definition**: The measurement of the stored energy in a material
in the form of light released by heating the material to determine the
material's age.
- **Child of**:
  - [`luminescence dating`](#luminescence-dating)
- **Alternate labels:**
  - TL
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300054718">http://vocab.getty.edu/aat/300054718</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2727388">https://www.wikidata.org/wiki/Q2727388</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8650222c">http://vocab.terralid.org#c_8650222c</a>


####  radiometric dating
- **Definition**: A family of dating methods that rely on the decay of
radioactive isotopes.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Alternate labels:**
  - radioactive dating
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300081912">http://vocab.getty.edu/aat/300081912</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q214753">https://www.wikidata.org/wiki/Q214753</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3f00a8dc">http://vocab.terralid.org#c_3f00a8dc</a>


#####  fission track dating
- **Definition**: Determining the age of a glassy material by counting
the number of damage trails created through the radioactive decay of
uranium atoms in the material.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300081920">http://vocab.getty.edu/aat/300081920</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1420956">https://www.wikidata.org/wiki/Q1420956</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_44573a53">http://vocab.terralid.org#c_44573a53</a>


#####  lead-lead dating
- **Definition**: Determination of the age through the ratios of the
the lead isotopes resulting from the radioactive decay of uranium and
the stable lead isotope ratio.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Pb-Pb dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q6508336">https://www.wikidata.org/wiki/Q6508336</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f98943fa">http://vocab.terralid.org#c_f98943fa</a>


#####  lutetium-hafnium dating
- **Definition**: Determination of the age through the ratio of a
radioactive lutetium isotope and the hafnium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Lu-Hf dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q48997241">https://www.wikidata.org/wiki/Q48997241</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5dec7fcf">http://vocab.terralid.org#c_5dec7fcf</a>


#####  potassium-argon dating
- **Definition**: Determination of the age through the ratio of a
radioactive potassium isotope and the argon isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - K-Ar dating
- **Matches:**
  - <a href="http://aims.fao.org/aos/agrovoc/c_36a43475">http://aims.fao.org/aos/agrovoc/c_36a43475</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300081924">http://vocab.getty.edu/aat/300081924</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q58891020">https://www.wikidata.org/wiki/Q58891020</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ade3d830">http://vocab.terralid.org#c_ade3d830</a>


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
  - <a href="https://www.wikidata.org/wiki/Q4789695">https://www.wikidata.org/wiki/Q4789695</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_025785fd">http://vocab.terralid.org#c_025785fd</a>


#####  radiocarbon dating
- **Definition**: Determination of the age through the remaining
radioactivity of carbon 14 in biogenic materials.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Matches:**
  - <a href="http://aims.fao.org/aos/agrovoc/c_13732">http://aims.fao.org/aos/agrovoc/c_13732</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300054717">http://vocab.getty.edu/aat/300054717</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q173412">https://www.wikidata.org/wiki/Q173412</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4b83987e">http://vocab.terralid.org#c_4b83987e</a>


#####  rhenium-osmium dating
- **Definition**: Determination of the age through the ratio of a
radioactive rhenium isotope and the osmium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Rh-Os dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2148046">https://www.wikidata.org/wiki/Q2148046</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb290340">http://vocab.terralid.org#c_eb290340</a>


#####  rubidium-strontium dating
- **Definition**: Determination of the age through the ratio of a
radioactive rubidium isotope and the strontium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Rb-Sr dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1499814">https://www.wikidata.org/wiki/Q1499814</a> (exactMatch)
  - <a href="http://aims.fao.org/aos/agrovoc/c_570aee9a">http://aims.fao.org/aos/agrovoc/c_570aee9a</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f21ed82d">http://vocab.terralid.org#c_f21ed82d</a>


#####  samarium-neodymium dating
- **Definition**: Determination of the age through the ratio of a
radioactive samarium isotope and the neodymium isotope it decays into.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - Sm-Nd dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q7408853">https://www.wikidata.org/wiki/Q7408853</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8c1af39">http://vocab.terralid.org#c_c8c1af39</a>


#####  uranium-lead dating
- **Definition**: Determination of the age through the two decay
series of uranium isotopes to lead isotopes.
- **Child of**:
  - [`radiometric dating`](#radiometric-dating)
- **Alternate labels:**
  - U-Pb dating
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1930710">https://www.wikidata.org/wiki/Q1930710</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_acb27762">http://vocab.terralid.org#c_acb27762</a>


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
  - <a href="http://vocab.getty.edu/aat/300379909">http://vocab.getty.edu/aat/300379909</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f0e6044b">http://vocab.terralid.org#c_f0e6044b</a>


####  rehydroxylation dating
- **Definition**: The measurement of the hydroxyl content in fired
clay and the determination of the related chemical kinetics to
reconstruct the date of the material.
- **Child of**:
  - [`absolute dating`](#absolute-dating)
- **Alternate labels:**
  - RHX
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300444022">http://vocab.getty.edu/aat/300444022</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q7309862">https://www.wikidata.org/wiki/Q7309862</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e6861de4">http://vocab.terralid.org#c_e6861de4</a>


###  relative dating
- **Definition**: Dating technique that allows to put objects in a
sequence relative to each other that cannot be tied to calendar years.
- **Child of**:
  - [`dating technique`](#dating-technique)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300224275">http://vocab.getty.edu/aat/300224275</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q265619">https://www.wikidata.org/wiki/Q265619</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_25bf9b34">http://vocab.terralid.org#c_25bf9b34</a>


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
  - <a href="http://vocab.getty.edu/aat/300226163">http://vocab.getty.edu/aat/300226163</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300081754">http://vocab.getty.edu/aat/300081754</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q776437">https://www.wikidata.org/wiki/Q776437</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e1bf335f">http://vocab.terralid.org#c_e1bf335f</a>


####  biostratigraphy
- **Definition**: The determination of the relative sequence of
sediments or rocks based on the fossils found in them.
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q864826">https://www.wikidata.org/wiki/Q864826</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b767c559">http://vocab.terralid.org#c_b767c559</a>


####  seriation
- **Definition**: Recording the stylistic details of a group of items
and ordering them in a sequence based defined typological features.
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379471">http://vocab.getty.edu/aat/300379471</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q358095">https://www.wikidata.org/wiki/Q358095</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e2a8665e">http://vocab.terralid.org#c_e2a8665e</a>


####  tephrochronology
- **Definition**: The determination of the relative sequence of
volcanic deposits (tephra), especially through studying their
stratigraphy (tephra).
- **Child of**:
  - [`relative dating`](#relative-dating)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300380317">http://vocab.getty.edu/aat/300380317</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2415972">https://www.wikidata.org/wiki/Q2415972</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5ef3d79f">http://vocab.terralid.org#c_5ef3d79f</a>



##  discovery activity
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/147298">http://purl.org/heritagedata/schemes/agl_et/concepts/147298</a> (relatedMatch)
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/147297">http://purl.org/heritagedata/schemes/agl_et/concepts/147297</a> (relatedMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e95a9fbf">http://vocab.terralid.org#c_e95a9fbf</a>


###  borehole survey
- **Definition**: Drilling into the ground with the aim to collect
samples and/or to describe the stratigraphy and subsurface features of
archaeological and geological features.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145112">http://purl.org/heritagedata/schemes/agl_et/concepts/145112</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb09b8cd">http://vocab.terralid.org#c_eb09b8cd</a>


####  auger drilling
- **Definition**: Drilling into the ground with the aim to retrieve
the content of the borehole as loose material to retrieve samples. In
some cases, it can be used to infer stratigraphy and subsurface
features of archaeological and geological features.
- **Child of**:
  - [`borehole survey`](#borehole-survey)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/exploration-activity-type/auger-drilling">http://resource.geosciml.org/classifier/cgi/exploration-activity-type/auger-drilling</a> (exactMatch)
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145111">http://purl.org/heritagedata/schemes/agl_et/concepts/145111</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19639bab">http://vocab.terralid.org#c_19639bab</a>


####  core drilling
- **Definition**: Drilling into the ground with the aim to retrieve
the content of the borehole as a whole. The material will subsequently
be used to collect samples and/or to describe the stratigraphy and
subsurface features of archaeological and geological features.
- **Child of**:
  - [`borehole survey`](#borehole-survey)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/exploration-activity-type/core-drilling">http://resource.geosciml.org/classifier/cgi/exploration-activity-type/core-drilling</a> (exactMatch)
  - <a href="http://inspire.ec.europa.eu/codelist/ExplorationActivityTypeValue/coreDrilling">http://inspire.ec.europa.eu/codelist/ExplorationActivityTypeValue/coreDrilling</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_410a0d02">http://vocab.terralid.org#c_410a0d02</a>


###  excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an site and to retrieve samples and artefacts from
the site.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145160">http://purl.org/heritagedata/schemes/agl_et/concepts/145160</a> (closeMatch)
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145129">http://purl.org/heritagedata/schemes/agl_et/concepts/145129</a> (exactMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/exploration-activity-type/excavation">http://resource.geosciml.org/classifier/cgi/exploration-activity-type/excavation</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300266151">http://vocab.getty.edu/aat/300266151</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cd2a7865">http://vocab.terralid.org#c_cd2a7865</a>


####  rescue excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an site under threat of destruction and to retrieve
samples and artefacts from the site under strict time constraints.
- **Child of**:
  - [`excavation`](#excavation)
- **Alternate labels:**
  - salvage excavation
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145157">http://purl.org/heritagedata/schemes/agl_et/concepts/145157</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q101008619">https://www.wikidata.org/wiki/Q101008619</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f39b79f2">http://vocab.terralid.org#c_f39b79f2</a>


####  research excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to answer a specific research question by recording an site
and retrieving samples and artefacts from the site.
- **Child of**:
  - [`excavation`](#excavation)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/147305">http://purl.org/heritagedata/schemes/agl_et/concepts/147305</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8eff20cd">http://vocab.terralid.org#c_8eff20cd</a>


####  underwater excavation
- **Definition**: Controlled and documented intrusive fieldwork with
the aim to record an underwater site and to retrieve samples and
artefacts from the site.
- **Child of**:
  - [`excavation`](#excavation)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/163244">http://purl.org/heritagedata/schemes/agl_et/concepts/163244</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6a6e0a7f">http://vocab.terralid.org#c_6a6e0a7f</a>


###  explorative mining activities
- **Definition**: Mining activities in preparation to establishing a
full-scale mining operation.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mine-workings-reconnaissance">http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mine-workings-reconnaissance</a> (closeMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mining-pilot">http://resource.geosciml.org/classifier/cgi/exploration-activity-type/mining-pilot</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_77f07bb9">http://vocab.terralid.org#c_77f07bb9</a>


###  illicit digging
- **Definition**: Uncontrolled and usually undocumented intrusive
fieldwork with the aim to collected artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Alternate labels:**
  - looting
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q15624851">https://www.wikidata.org/wiki/Q15624851</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d0e965f6">http://vocab.terralid.org#c_d0e965f6</a>


###  metal detecting
- **Definition**: The use of a metal detector to discover artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145147">http://purl.org/heritagedata/schemes/agl_et/concepts/145147</a> (closeMatch)
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/145148">http://purl.org/heritagedata/schemes/agl_et/concepts/145148</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q111047657">https://www.wikidata.org/wiki/Q111047657</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3f471934">http://vocab.terralid.org#c_3f471934</a>


###  mining
- **Definition**: The economic extraction of georesources from the
earth. This includes surface and underground operations.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mining-activity">http://resource.geosciml.org/classifier/cgi/mining-activity</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q44497">https://www.wikidata.org/wiki/Q44497</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2758f3b1">http://vocab.terralid.org#c_2758f3b1</a>


###  ore prospection
- **Definition**: The systematic survey on an area with the aim to
identify the presence of potentially economically viable
mineralisations.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Concept URI:** <a href="http://vocab.terralid.org#c_074a675c">http://vocab.terralid.org#c_074a675c</a>


###  stray find
- **Definition**: The incidental discovery (and recovery) of materials
of interest.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/146344">http://purl.org/heritagedata/schemes/agl_et/concepts/146344</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_84c6c6e0">http://vocab.terralid.org#c_84c6c6e0</a>


###  survey
- **Definition**: Non-intrusive fieldwork to document the extent and
layout of a site through recording the position and distribution of
specimens and artefacts.
- **Child of**:
  - [`discovery activity`](#discovery-activity)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/agl_et/concepts/170654">http://purl.org/heritagedata/schemes/agl_et/concepts/170654</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ae4a0583">http://vocab.terralid.org#c_ae4a0583</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  glass component
- **Definition**: The general ingredients creating a glass.
- **Concept URI:** <a href="http://vocab.terralid.org#c_e96ca20e">http://vocab.terralid.org#c_e96ca20e</a>


###  colorant
- **Definition**: The colour-giving constituent of a pigment or glass.
- **Child of**:
  - [`glass component`](#glass-component)
  - [`pigment component`](#pigment-component)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q911922">https://www.wikidata.org/wiki/Q911922</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300013026">http://vocab.getty.edu/aat/300013026</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4e57487f">http://vocab.terralid.org#c_4e57487f</a>


###  network former
- **Definition**: The component of the glass creating the network of
chains the glass is build of.
- **Child of**:
  - [`glass component`](#glass-component)
- **Alternate labels:**
  - silica, 
  - sand, 
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e5b4e78">http://vocab.terralid.org#c_3e5b4e78</a>


###  network modifier
- **Definition**: The component of the glass regulating the length of
the chains build by the network former.
- **Child of**:
  - [`glass component`](#glass-component)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5a103a06">http://vocab.terralid.org#c_5a103a06</a>


###  opacifier
- **Definition**: The component of the glass decreasing its
transparency.
- **Child of**:
  - [`glass component`](#glass-component)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q7095513">https://www.wikidata.org/wiki/Q7095513</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6b636b3a">http://vocab.terralid.org#c_6b636b3a</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  identifier
- **Definition**: A string unique for a specific resource or feature.
- **Other Properties:**
  - **note**: 
This is a reproduction of the controlled list relatedIdentifierType in the DataCite Metadata version schema 4.7. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q853614">https://www.wikidata.org/wiki/Q853614</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000022">https://vocabs.dariah.eu/bbt/Concept/000022</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8cb9106">http://vocab.terralid.org#c_c8cb9106</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_9c7b1aa6">http://vocab.terralid.org#c_9c7b1aa6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q118398">https://www.wikidata.org/wiki/Q118398</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#arxiv](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#arxiv)
- **Concept URI:** <a href="http://vocab.terralid.org#c_14d152fa">http://vocab.terralid.org#c_14d152fa</a>


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
  - <a href="https://www.wikidata.org/wiki/Q25754">https://www.wikidata.org/wiki/Q25754</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#bibcode](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#bibcode)
- **Concept URI:** <a href="http://vocab.terralid.org#c_58ef12c9">http://vocab.terralid.org#c_58ef12c9</a>


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
  - <a href="https://www.wikidata.org/wiki/Q124257084">https://www.wikidata.org/wiki/Q124257084</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#cstr](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#cstr)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e3b9ba37">http://vocab.terralid.org#c_e3b9ba37</a>


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
  - <a href="https://www.wikidata.org/wiki/Q25670">https://www.wikidata.org/wiki/Q25670</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#doi](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#doi)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cc3c0083">http://vocab.terralid.org#c_cc3c0083</a>


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
  - <a href="https://www.wikidata.org/wiki/Q357404">https://www.wikidata.org/wiki/Q357404</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ean13](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#ean13)
- **Concept URI:** <a href="http://vocab.terralid.org#c_91caa317">http://vocab.terralid.org#c_91caa317</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_9cdedeb0">http://vocab.terralid.org#c_9cdedeb0</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3126718">https://www.wikidata.org/wiki/Q3126718</a> (relatedMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#handle](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#handle)
- **Concept URI:** <a href="http://vocab.terralid.org#c_db36371f">http://vocab.terralid.org#c_db36371f</a>


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
  - <a href="https://www.wikidata.org/wiki/Q17058352">https://www.wikidata.org/wiki/Q17058352</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#igsn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#igsn)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bb41a882">http://vocab.terralid.org#c_bb41a882</a>


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
  - <a href="https://www.wikidata.org/wiki/Q33057">https://www.wikidata.org/wiki/Q33057</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#isbn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#isbn)
- **Concept URI:** <a href="http://vocab.terralid.org#c_664844dc">http://vocab.terralid.org#c_664844dc</a>


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
  - <a href="https://www.wikidata.org/wiki/Q131276">https://www.wikidata.org/wiki/Q131276</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#issn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#issn)
- **Concept URI:** <a href="http://vocab.terralid.org#c_23aeb12c">http://vocab.terralid.org#c_23aeb12c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1666944">https://www.wikidata.org/wiki/Q1666944</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#istc](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#istc)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a61ff4a5">http://vocab.terralid.org#c_a61ff4a5</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_036b6cbe">http://vocab.terralid.org#c_036b6cbe</a>


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
  - <a href="https://www.wikidata.org/wiki/Q6459954">https://www.wikidata.org/wiki/Q6459954</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lsid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#lsid)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19665f86">http://vocab.terralid.org#c_19665f86</a>


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
  - <a href="https://www.wikidata.org/wiki/Q2082879">https://www.wikidata.org/wiki/Q2082879</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#pmid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#pmid)
- **Concept URI:** <a href="http://vocab.terralid.org#c_491eec33">http://vocab.terralid.org#c_491eec33</a>


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
  - <a href="https://www.wikidata.org/wiki/Q195305">https://www.wikidata.org/wiki/Q195305</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#purl](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#purl)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ff6b1f44">http://vocab.terralid.org#c_ff6b1f44</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_b10276d1">http://vocab.terralid.org#c_b10276d1</a>


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
  - <a href="https://www.wikidata.org/wiki/Q107278278">https://www.wikidata.org/wiki/Q107278278</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#rrid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#rrid)
- **Concept URI:** <a href="http://vocab.terralid.org#c_96a8c2b8">http://vocab.terralid.org#c_96a8c2b8</a>


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
  - <a href="https://www.wikidata.org/wiki/Q134567344">https://www.wikidata.org/wiki/Q134567344</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#swhid](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#swhid)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b573f515">http://vocab.terralid.org#c_b573f515</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1193047">https://www.wikidata.org/wiki/Q1193047</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#upc](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#upc)
- **Concept URI:** <a href="http://vocab.terralid.org#c_49ebd1fc">http://vocab.terralid.org#c_49ebd1fc</a>


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
  - <a href="https://www.wikidata.org/wiki/Q42253">https://www.wikidata.org/wiki/Q42253</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#url](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#url)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cca94dd2">http://vocab.terralid.org#c_cca94dd2</a>


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
  - <a href="https://www.wikidata.org/wiki/Q76497">https://www.wikidata.org/wiki/Q76497</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#urn](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relatedIdentifierType/#urn)
- **Concept URI:** <a href="http://vocab.terralid.org#c_efbf8c56">http://vocab.terralid.org#c_efbf8c56</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f260a576">http://vocab.terralid.org#c_f260a576</a>



##  information source
- **Definition**: Identifies whether a given value was supplied by an
external agent or internally calculared.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f3916dc0">http://vocab.terralid.org#c_f3916dc0</a>


###  calculated
- **Definition**: The value was calculated by the TerraLID system.
- **Child of**:
  - [`information source`](#information-source)
- **Concept URI:** <a href="http://vocab.terralid.org#c_16684898">http://vocab.terralid.org#c_16684898</a>


###  original
- **Definition**: The value was provided by the data supplier.
- **Child of**:
  - [`information source`](#information-source)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f33b28fe">http://vocab.terralid.org#c_f33b28fe</a>



##  lead isotope age model
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_435c9bf2">http://vocab.terralid.org#c_435c9bf2</a>


###  AJ84
- **Definition**: The two-stage lead isotope age model according to
Albarède, F. and Juteau, M. (1984) Unscrambling the lead model ages.
Geochimica et Cosmochimica Acta 48(1), pp. 207–212.
https://dx.doi.org/10.1016/0016-7037(84)90364-8
- **Child of**:
  - [`lead isotope age model`](#lead-isotope-age-model)
- **References**:
  - [https://doi.org/10.1016/0016-7037(84)90364-8](https://doi.org/10.1016/0016-7037(84)90364-8)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a299bc22">http://vocab.terralid.org#c_a299bc22</a>


###  CR75
- **Definition**: The single-stage lead isotope age model according to
Cumming, G.L. and Richards, J.R. (1975) Ore lead isotope ratios in a
continuously changing earth. Earth and Planetary Science Letters
28(2), pp. 155–171. https://dx.doi.org/10.1016/0012-821X(75)90223-X
- **Child of**:
  - [`lead isotope age model`](#lead-isotope-age-model)
- **References**:
  - [https://doi.org/10.1016/0012-821X(75)90223-X](https://doi.org/10.1016/0012-821X(75)90223-X)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b80ae0f4">http://vocab.terralid.org#c_b80ae0f4</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_10c030b1">http://vocab.terralid.org#c_10c030b1</a>



##  lead isotope ratios
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000021">https://vocabs.dariah.eu/bbt/Concept/000021</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e5dcadb1">http://vocab.terralid.org#c_e5dcadb1</a>


###  204Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f8980276">http://vocab.terralid.org#c_f8980276</a>


###  206Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_865958f1">http://vocab.terralid.org#c_865958f1</a>


###  206Pb/208Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3d413d9a">http://vocab.terralid.org#c_3d413d9a</a>


###  207Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4936f14">http://vocab.terralid.org#c_f4936f14</a>


###  207Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9531a82a">http://vocab.terralid.org#c_9531a82a</a>


###  207Pb/208Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_25e00462">http://vocab.terralid.org#c_25e00462</a>


###  208Pb/204Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9f519c7a">http://vocab.terralid.org#c_9f519c7a</a>


###  208Pb/206Pb
- **Child of**:
  - [`lead isotope ratios`](#lead-isotope-ratios)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b3a0bf8c">http://vocab.terralid.org#c_b3a0bf8c</a>



##  mass bias correction
- **Definition**: The mathematical model or procedure used to correct
for the fractionation of an isotope ratio during measurement.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5f1716a4">http://vocab.terralid.org#c_5f1716a4</a>


###  double-spike
- **Definition**: The correction of an isotope ratio's mass bias by
altering the abundance of two other isotopes of the same element
through the addition of an enriched isotopic spike
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.chemgeo.2009.05.010](https://doi.org/10.1016/j.chemgeo.2009.05.010)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7b213d83">http://vocab.terralid.org#c_7b213d83</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_e9b3f7f1">http://vocab.terralid.org#c_e9b3f7f1</a>


###  linear model
- **Definition**: A mathematical model assuming a linear relationship
between the isotope ratio of the sample and a different isotope ratio
of an internal standard added to the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** <a href="http://vocab.terralid.org#c_39d3b302">http://vocab.terralid.org#c_39d3b302</a>


###  power law
- **Definition**: A mathematical model assuming a power-relationship
between the isotope ratio of the sample and a different isotope ratio
of an internal standard added to the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** <a href="http://vocab.terralid.org#c_17be86eb">http://vocab.terralid.org#c_17be86eb</a>


###  standard-sample bracketing
- **Definition**: The correction of an isotope ratio's mass bias in a
sample by extrapolation from measurements of the same isotope ratio in
an external standard measured before and after the sample.
- **Child of**:
  - [`mass bias correction`](#mass-bias-correction)
- **References**:
  - [https://doi.org/10.1016/j.gca.2003.11.024](https://doi.org/10.1016/j.gca.2003.11.024)
- **Concept URI:** <a href="http://vocab.terralid.org#c_725495a8">http://vocab.terralid.org#c_725495a8</a>



##  mineral texture
- **Definition**: The relationship between the mineral and the matrix
and other minerals, conveying information about the mineral's
formation conditions.
- **Other Properties:**
  - **note**: 
The terms are mostly taken from U. Neumann (2020), Guide for the microscopical identification of ore and gangue minerals, Tübingen University Press (http://dx.doi.org/10.15496/publikation-38866). However, the definitions are original and based on various sources because the relevant literature, including the aforementioned publication, do not explicitly defines textures but provide examples for them in photomicrographs. 
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8441accd">http://vocab.terralid.org#c_8441accd</a>


###  deformation-related
- **Definition**: The alteration of minerals through external
mechanical stress.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** <a href="http://vocab.terralid.org#c_88091e76">http://vocab.terralid.org#c_88091e76</a>


####  bending
- **Definition**: The ductile transformation of a mineral into a bent
shape (i.e., without breaking it).
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8069a37">http://vocab.terralid.org#c_c8069a37</a>


####  brecciated
- **Definition**: The fragmentation of a mineral resulting in various
angular fragments
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_430fd693">http://vocab.terralid.org#c_430fd693</a>


####  broken
- **Definition**: The fragmentation of a mineral.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_03b13243">http://vocab.terralid.org#c_03b13243</a>


####  cataclastic
- **Definition**: The fracturing of a mineral due to intense
mechanical stress.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6783bb4e">http://vocab.terralid.org#c_6783bb4e</a>


####  planar alignment
- **Definition**: The transformation of elongated or layered minerals
into a (sub)parallel orientation.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ed4b7838">http://vocab.terralid.org#c_ed4b7838</a>


####  pressure twins
- **Definition**: The internal deformation of a mineral's crystal due
to translational forces, resulting in the re-orientation of some areas
in the crystal along crystal planes along its crystallographic axes.
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7067812d">http://vocab.terralid.org#c_7067812d</a>


####  translation lamellae
- **Definition**: The internal deformation of a mineral's crystal due
to translational forces, resulting in the re-orientation of some areas
in the crystal along crystal planes unrelated to the crystallographic
axes
- **Child of**:
  - [`deformation-related`](#deformation-related)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3136dfed">http://vocab.terralid.org#c_3136dfed</a>


###  intergrowth
- **Definition**: The state of interlocking of different mineral
grains due to simultaneous crystallisation.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e74b28a0">http://vocab.terralid.org#c_e74b28a0</a>


####  amoeboid
- **Definition**: A mineral with irregular outlines and anhedral
crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e5b6f80a">http://vocab.terralid.org#c_e5b6f80a</a>


####  atoll-like
- **Definition**: The growth of a ring-shaped mineral around and
surrounded by other minerals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - core texture
- **Concept URI:** <a href="http://vocab.terralid.org#c_95b262b5">http://vocab.terralid.org#c_95b262b5</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_04619e43">http://vocab.terralid.org#c_04619e43</a>


####  disseminated
- **Definition**: The mineral is scattered as small grains throughout
another mineral or the matrix.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_aa5d33c3">http://vocab.terralid.org#c_aa5d33c3</a>


####  interlocked
- **Definition**: Intimate intergrowth of randomly orientated mineral
grains with no gaps or cement between them.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e50acb7">http://vocab.terralid.org#c_3e50acb7</a>


####  intersertal
- **Definition**: Filling of interstitial space with a glass or a
vitreous phase with small crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cab80d83">http://vocab.terralid.org#c_cab80d83</a>


####  interstitial
- **Definition**: The mineral grew in the interstitial space between
grains or structures.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1a4f781a">http://vocab.terralid.org#c_1a4f781a</a>


####  ophitic
- **Definition**: Large and often lath-shaped euhedral or subhedral
crystals are partly or fully included in much larger crystals.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd1113d4">http://vocab.terralid.org#c_dd1113d4</a>


####  poikiloblastic
- **Definition**: Small grains of one mineral are randomly scattered
without common orientation in larger grains of another mineral.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Alternate labels:**
  - poikilitic, 
  - sieve texture, 
- **Concept URI:** <a href="http://vocab.terralid.org#c_6655861f">http://vocab.terralid.org#c_6655861f</a>


####  rimmed
- **Definition**: A mineral grew in the rim of another mineral.
- **Child of**:
  - [`intergrowth`](#intergrowth)
- **Concept URI:** <a href="http://vocab.terralid.org#c_436d944e">http://vocab.terralid.org#c_436d944e</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e0d2c4a">http://vocab.terralid.org#c_9e0d2c4a</a>


#####  myrmekitic
- **Definition**: A symplectitic intergrowth of plagioclase and
vermicular quartz.
- **Child of**:
  - [`symplectitic`](#symplectitic)
- **Other Properties:**
  - **scopeNote**: 
Myrmekitic as specific case of symplectitic texture. Appears to be often used synonymously at least in ore microscopy . 
- **Concept URI:** <a href="http://vocab.terralid.org#c_5eaf970c">http://vocab.terralid.org#c_5eaf970c</a>


###  replacement
- **Definition**: The growth of a new or chemically different mineral
as a reaction product of the already existing mineral.
- **Child of**:
  - [`mineral texture`](#mineral-texture)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a3d375e7">http://vocab.terralid.org#c_a3d375e7</a>


####  atoll-like (replacement)
- **Definition**: The replacement of one mineral by another with
leaving the outermost original mineral unaffected, and constituting
the "atoll".
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd91efb2">http://vocab.terralid.org#c_dd91efb2</a>


####  boxwork
- **Definition**: Growth of secondary minerals in cavities and along
fracture or cleavage planes from which previously present minerals
were removed by e.g. dissolution, creating a network texture
resembling stacked boxes or honey-combs.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d78ab7be">http://vocab.terralid.org#c_d78ab7be</a>


####  cellular (replacement)
- **Definition**: The growth of minerals replacing the content of
cells in originally biological matter such as plants in coal.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8c47dce3">http://vocab.terralid.org#c_8c47dce3</a>


####  cement-shaped
- **Definition**: The growth of a dense anhedral alteration mineral in
the matrix.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d375a5c9">http://vocab.terralid.org#c_d375a5c9</a>


####  cusp-and-caries
- **Definition**: The growth of a secondary mineral from the grain
boundary into the primary minerals, resulting in a grain boundary
between both minerals with many scallop-shaped, concave embayments.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d3b9f898">http://vocab.terralid.org#c_d3b9f898</a>


####  filiform
- **Definition**: An intergrowth of  different minerals in which the
larger crystals have a fairly regular geometric outline and
orientation, and resemble cuneiform writing or have a thread-like
appearance.
- **Child of**:
  - [`replacement`](#replacement)
- **Alternate labels:**
  - graphic texture
- **Concept URI:** <a href="http://vocab.terralid.org#c_f478f111">http://vocab.terralid.org#c_f478f111</a>


####  graphic
- **Definition**: The growth of elongated rounded aggregates of
secondary minerals inside the primary mineral, often as a result of
alteration of the primary mineral.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_52eaf264">http://vocab.terralid.org#c_52eaf264</a>


####  island-shaped
- **Definition**: The original mineral reacted from the outside,
leaving an (island-shaped) unreacted part surrounded by secondary
minerals.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7b190793">http://vocab.terralid.org#c_7b190793</a>


####  lacuna
- **Definition**: The dissolution of small areas of a mineral, often
at its rim, resulting in voids.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bb44a01a">http://vocab.terralid.org#c_bb44a01a</a>


####  lamellar
- **Definition**: The oriented growth of a secondary mineral in
elongated shapes within the primary mineral, usually along cleavage
planes, crystal planes, twin boundaries or fractures.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7fe5c1ff">http://vocab.terralid.org#c_7fe5c1ff</a>


####  pseudomorph
- **Definition**: A secondary mineral completely replacing the primary
mineral while retaining the shape of the primary mineral's grains.
- **Child of**:
  - [`replacement`](#replacement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1456639">https://www.wikidata.org/wiki/Q1456639</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0571a899">http://vocab.terralid.org#c_0571a899</a>


####  skeleton-shaped
- **Definition**: Relict of a skeletal crystal of one mineral enclosed
in another mineral species.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_36ca06ef">http://vocab.terralid.org#c_36ca06ef</a>


####  zonal
- **Definition**: The evenly-spaced growth of a secondary mineral
along the crystallographic orientation of the primary mineral's grain
boundary.
- **Child of**:
  - [`replacement`](#replacement)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7d8b3c14">http://vocab.terralid.org#c_7d8b3c14</a>



##  nuclide
- **Definition**: Atom that is characterised by its number of protons
and number of neutrons.
- **Alternate labels:**
  - isotope
- **Other Properties:**
  - **scopeNote**: 
Only naturally occurring nuclides were included. While it was aimed to include all stable nuclides, only some radioactive nuclides are included. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q108149">https://www.wikidata.org/wiki/Q108149</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5264a37a">http://vocab.terralid.org#c_5264a37a</a>


###  aluminium-27
- **Definition**: Isotope of aluminium with mass 27
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 27Al, 
  - Al-27, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2225512">http://www.wikidata.org/entity/Q2225512</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a9212ed3">http://vocab.terralid.org#c_a9212ed3</a>


###  antimony-121
- **Definition**: Isotope of antimony with mass 121
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 121Sb, 
  - Sb-121, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1856817">http://www.wikidata.org/entity/Q1856817</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e3c8b27e">http://vocab.terralid.org#c_e3c8b27e</a>


###  antimony-123
- **Definition**: Isotope of antimony with mass 123
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 123Sb, 
  - Sb-123, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2297512">http://www.wikidata.org/entity/Q2297512</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cd03b20f">http://vocab.terralid.org#c_cd03b20f</a>


###  argon-36
- **Definition**: Isotope of argon with mass 36
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 36Ar, 
  - Ar-36, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2019992">http://www.wikidata.org/entity/Q2019992</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_634a9fef">http://vocab.terralid.org#c_634a9fef</a>


###  argon-38
- **Definition**: Isotope of argon with mass 38
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 38Ar, 
  - Ar-38, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2801372">http://www.wikidata.org/entity/Q2801372</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4c2e56ad">http://vocab.terralid.org#c_4c2e56ad</a>


###  argon-40
- **Definition**: Isotope of argon with mass 40
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 40Ar, 
  - Ar-40, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1929004">http://www.wikidata.org/entity/Q1929004</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_93f3727f">http://vocab.terralid.org#c_93f3727f</a>


###  arsenic-75
- **Definition**: Isotope of arsenic with mass 75
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 75As, 
  - As-75, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4942137">http://www.wikidata.org/entity/Q4942137</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7a39fb20">http://vocab.terralid.org#c_7a39fb20</a>


###  barium-130
- **Definition**: Isotope of barium with mass 130
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 130Ba, 
  - Ba-130, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2574790">http://www.wikidata.org/entity/Q2574790</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebf7d20a">http://vocab.terralid.org#c_ebf7d20a</a>


###  barium-134
- **Definition**: Isotope of barium with mass 134
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 134Ba, 
  - Ba-134, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2538685">http://www.wikidata.org/entity/Q2538685</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f3e7c5c2">http://vocab.terralid.org#c_f3e7c5c2</a>


###  barium-135
- **Definition**: Isotope of barium with mass 135
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 135Ba, 
  - Ba-135, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3192465">http://www.wikidata.org/entity/Q3192465</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b1146739">http://vocab.terralid.org#c_b1146739</a>


###  barium-136
- **Definition**: Isotope of barium with mass 136
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 136Ba, 
  - Ba-136, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2449314">http://www.wikidata.org/entity/Q2449314</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd1bd88d">http://vocab.terralid.org#c_dd1bd88d</a>


###  barium-137
- **Definition**: Isotope of barium with mass 137
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 137Ba, 
  - Ba-137, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4734760">http://www.wikidata.org/entity/Q4734760</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e0619307">http://vocab.terralid.org#c_e0619307</a>


###  barium-138
- **Definition**: Isotope of barium with mass 138
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 138Ba, 
  - Ba-138, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2409784">http://www.wikidata.org/entity/Q2409784</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_478c47fa">http://vocab.terralid.org#c_478c47fa</a>


###  beryllium-9
- **Definition**: Isotope of beryllium with mass 9
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 9Be, 
  - Be-9, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3010030">http://www.wikidata.org/entity/Q3010030</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_84430359">http://vocab.terralid.org#c_84430359</a>


###  boron-10
- **Definition**: Isotope of boron with mass 10
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - B-10, 
  - 10B, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2437314">http://www.wikidata.org/entity/Q2437314</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6562bc02">http://vocab.terralid.org#c_6562bc02</a>


###  boron-11
- **Definition**: Isotope of boron with mass 11
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - B-11, 
  - 11B, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2659502">http://www.wikidata.org/entity/Q2659502</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_14290b2e">http://vocab.terralid.org#c_14290b2e</a>


###  bromine-79
- **Definition**: Isotope of bromine with mass 79
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 79Br, 
  - Br-79, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2311128">http://www.wikidata.org/entity/Q2311128</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3bc6fb7b">http://vocab.terralid.org#c_3bc6fb7b</a>


###  bromine-81
- **Definition**: Isotope of bromine with mass 81
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 81Br, 
  - Br-81, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2342633">http://www.wikidata.org/entity/Q2342633</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0442fdbb">http://vocab.terralid.org#c_0442fdbb</a>


###  cadmium-110
- **Definition**: Isotope of cadmium with mass 110
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 110Cd, 
  - Cd-110, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2549993">http://www.wikidata.org/entity/Q2549993</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6fdabf24">http://vocab.terralid.org#c_6fdabf24</a>


###  cadmium-111
- **Definition**: Isotope of cadmium with mass 111
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 111Cd, 
  - Cd-111, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2437333">http://www.wikidata.org/entity/Q2437333</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e37552a3">http://vocab.terralid.org#c_e37552a3</a>


###  cadmium-112
- **Definition**: Isotope of cadmium with mass 112
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 112Cd, 
  - Cd-112, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2040848">http://www.wikidata.org/entity/Q2040848</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3f768b80">http://vocab.terralid.org#c_3f768b80</a>


###  caesium-133
- **Definition**: Isotope of caesium with mass 133
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 133Cs, 
  - Cs-133, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2327948">http://www.wikidata.org/entity/Q2327948</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2d6e603e">http://vocab.terralid.org#c_2d6e603e</a>


###  calcium-42
- **Definition**: Isotope of calcium with mass 42
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 42Ca, 
  - Ca-42, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2728105">http://www.wikidata.org/entity/Q2728105</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_75e2c4b9">http://vocab.terralid.org#c_75e2c4b9</a>


###  calcium-43
- **Definition**: Isotope of calcium with mass 43
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 43Ca, 
  - Ca-43, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2103298">http://www.wikidata.org/entity/Q2103298</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_db747aa1">http://vocab.terralid.org#c_db747aa1</a>


###  calcium-44
- **Definition**: Isotope of calcium with mass 44
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 44Ca, 
  - Ca-44, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3027367">http://www.wikidata.org/entity/Q3027367</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b495ff08">http://vocab.terralid.org#c_b495ff08</a>


###  carbon-12
- **Definition**: Isotope of carbon with mass 12
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 12C, 
  - C-12, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1058364">http://www.wikidata.org/entity/Q1058364</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4a430372">http://vocab.terralid.org#c_4a430372</a>


###  carbon-13
- **Definition**: Isotope of carbon with mass 13
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - C-13, 
  - 13C, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1770822">http://www.wikidata.org/entity/Q1770822</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_54fc7af8">http://vocab.terralid.org#c_54fc7af8</a>


###  cerium-140
- **Definition**: Isotope of cerium with mass 140
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 140Ce, 
  - Ce-140, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2646578">http://www.wikidata.org/entity/Q2646578</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_aec1e5c8">http://vocab.terralid.org#c_aec1e5c8</a>


###  chlorine-35
- **Definition**: Isotope of chlorine with mass 35
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 35Cl, 
  - Cl-35, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2783861">http://www.wikidata.org/entity/Q2783861</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_37007611">http://vocab.terralid.org#c_37007611</a>


###  chlorine-37
- **Definition**: Isotope of chlorine with mass 37
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 37Cl, 
  - Cl-37, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q5102949">http://www.wikidata.org/entity/Q5102949</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_de66e623">http://vocab.terralid.org#c_de66e623</a>


###  chromium-52
- **Definition**: Isotope of chromium with mass 52
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 52Cr, 
  - Cr-52, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4469260">http://www.wikidata.org/entity/Q4469260</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cf33d726">http://vocab.terralid.org#c_cf33d726</a>


###  chromium-53
- **Definition**: Isotope of chromium with mass 53
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 53Cr, 
  - Cr-53, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13466446">http://www.wikidata.org/entity/Q13466446</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fca9776e">http://vocab.terralid.org#c_fca9776e</a>


###  chromium-54
- **Definition**: Isotope of chromium with mass 54
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 54Cr, 
  - Cr-54, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2239560">http://www.wikidata.org/entity/Q2239560</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_220f23dc">http://vocab.terralid.org#c_220f23dc</a>


###  cobalt-59
- **Definition**: Isotope of cobalt with mass 59
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 59Co, 
  - Co-59, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4350852">http://www.wikidata.org/entity/Q4350852</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_565bd3cd">http://vocab.terralid.org#c_565bd3cd</a>


###  copper-63
- **Definition**: Isotope of copper with mass 63
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 63Cu, 
  - Cu-63, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3031418">http://www.wikidata.org/entity/Q3031418</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dc42718a">http://vocab.terralid.org#c_dc42718a</a>


###  copper-65
- **Definition**: Isotope of copper with mass 65
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 65Cu, 
  - Cu-65, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2557191">http://www.wikidata.org/entity/Q2557191</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9516cfd3">http://vocab.terralid.org#c_9516cfd3</a>


###  deuterium
- **Definition**: Isotope of hydrogen with 1 neutron with mass 2
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - D, 
  - 2H, 
  - H-2, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q102296">http://www.wikidata.org/entity/Q102296</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bfc6c4ac">http://vocab.terralid.org#c_bfc6c4ac</a>


###  dysprosium-156
- **Definition**: Isotope of dysprosium with mass 156
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 156Dy, 
  - Dy-156, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574970">http://www.wikidata.org/entity/Q13574970</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_525c36e1">http://vocab.terralid.org#c_525c36e1</a>


###  dysprosium-158
- **Definition**: Isotope of dysprosium with mass 158
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 158Dy, 
  - Dy-158, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574971">http://www.wikidata.org/entity/Q13574971</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_28d13e35">http://vocab.terralid.org#c_28d13e35</a>


###  dysprosium-160
- **Definition**: Isotope of dysprosium with mass 160
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 160Dy, 
  - Dy-160, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574974">http://www.wikidata.org/entity/Q13574974</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f49d9fa4">http://vocab.terralid.org#c_f49d9fa4</a>


###  dysprosium-161
- **Definition**: Isotope of dysprosium with mass 161
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 161Dy, 
  - Dy-161, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574976">http://www.wikidata.org/entity/Q13574976</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a8bf2c4f">http://vocab.terralid.org#c_a8bf2c4f</a>


###  dysprosium-162
- **Definition**: Isotope of dysprosium with mass 162
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 162Dy, 
  - Dy-162, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574977">http://www.wikidata.org/entity/Q13574977</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6334fb78">http://vocab.terralid.org#c_6334fb78</a>


###  dysprosium-163
- **Definition**: Isotope of dysprosium with mass 163
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 163Dy, 
  - Dy-163, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574978">http://www.wikidata.org/entity/Q13574978</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_77e047aa">http://vocab.terralid.org#c_77e047aa</a>


###  dysprosium-164
- **Definition**: Isotope of dysprosium with mass 164
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 164Dy, 
  - Dy-164, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13574979">http://www.wikidata.org/entity/Q13574979</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7f4d8aa8">http://vocab.terralid.org#c_7f4d8aa8</a>


###  erbium-162
- **Definition**: Isotope of erbium with mass 162
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 162Er, 
  - Er-162, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874939">http://www.wikidata.org/entity/Q15874939</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_758aff67">http://vocab.terralid.org#c_758aff67</a>


###  erbium-164
- **Definition**: Isotope of erbium with mass 164
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 164Er, 
  - Er-164, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874941">http://www.wikidata.org/entity/Q15874941</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d9b4651e">http://vocab.terralid.org#c_d9b4651e</a>


###  erbium-166
- **Definition**: Isotope of erbium with mass 166
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 166Er, 
  - Er-166, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874944">http://www.wikidata.org/entity/Q15874944</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_541ff9d6">http://vocab.terralid.org#c_541ff9d6</a>


###  erbium-167
- **Definition**: Isotope of erbium with mass 167
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 167Er, 
  - Er-167, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874945">http://www.wikidata.org/entity/Q15874945</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11bbb681">http://vocab.terralid.org#c_11bbb681</a>


###  erbium-168
- **Definition**: Isotope of erbium with mass 168
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 168Er, 
  - Er-168, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874946">http://www.wikidata.org/entity/Q15874946</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d95ddf57">http://vocab.terralid.org#c_d95ddf57</a>


###  erbium-170
- **Definition**: Isotope of erbium with mass 170
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 170Er, 
  - Er-170, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15874948">http://www.wikidata.org/entity/Q15874948</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_78ffaee2">http://vocab.terralid.org#c_78ffaee2</a>


###  europium-153
- **Definition**: Isotope of europium with mass 153
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 153Eu, 
  - Eu-153, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2027407">http://www.wikidata.org/entity/Q2027407</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8c348a7c">http://vocab.terralid.org#c_8c348a7c</a>


###  fluorine-19
- **Definition**: Isotope of fluorine with mass 19
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - F-19, 
  - 19F, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2257946">http://www.wikidata.org/entity/Q2257946</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b05b6ea8">http://vocab.terralid.org#c_b05b6ea8</a>


###  gadolinium-154
- **Definition**: Isotope of gadolinium with mass 154
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 154Gd, 
  - Gd-154, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2175390">http://www.wikidata.org/entity/Q2175390</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6be62267">http://vocab.terralid.org#c_6be62267</a>


###  gadolinium-155
- **Definition**: Isotope of gadolinium with mass 155
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 155Gd, 
  - Gd-155, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2972794">http://www.wikidata.org/entity/Q2972794</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_be2ddeb7">http://vocab.terralid.org#c_be2ddeb7</a>


###  gadolinium-156
- **Definition**: Isotope of gadolinium with mass 156
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 156Gd, 
  - Gd-156, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4505367">http://www.wikidata.org/entity/Q4505367</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2ce9bcc9">http://vocab.terralid.org#c_2ce9bcc9</a>


###  gadolinium-157
- **Definition**: Isotope of gadolinium with mass 157
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 157Gd, 
  - Gd-157, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2226266">http://www.wikidata.org/entity/Q2226266</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_010322ff">http://vocab.terralid.org#c_010322ff</a>


###  gadolinium-158
- **Definition**: Isotope of gadolinium with mass 158
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 158Gd, 
  - Gd-158, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2237256">http://www.wikidata.org/entity/Q2237256</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0fcf74f2">http://vocab.terralid.org#c_0fcf74f2</a>


###  gallium-69
- **Definition**: Isotope of gallium with mass 69
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 69Ga, 
  - Ga-69, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4738844">http://www.wikidata.org/entity/Q4738844</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d9877e77">http://vocab.terralid.org#c_d9877e77</a>


###  gallium-71
- **Definition**: Isotope of gallium with mass 71
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 71Ga, 
  - Ga-71, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2311889">http://www.wikidata.org/entity/Q2311889</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f45079c8">http://vocab.terralid.org#c_f45079c8</a>


###  germanium-70
- **Definition**: Isotope of germanium with mass 70
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 70Ge, 
  - Ge-70, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2674362">http://www.wikidata.org/entity/Q2674362</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a53bc3c5">http://vocab.terralid.org#c_a53bc3c5</a>


###  germanium-72
- **Definition**: Isotope of germanium with mass 72
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 72Ge, 
  - Ge-72, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2035731">http://www.wikidata.org/entity/Q2035731</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7e15bbf">http://vocab.terralid.org#c_d7e15bbf</a>


###  germanium-73
- **Definition**: Isotope of germanium with mass 73
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 73Ge, 
  - Ge-73, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2437511">http://www.wikidata.org/entity/Q2437511</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_edb8fb3e">http://vocab.terralid.org#c_edb8fb3e</a>


###  germanium-74
- **Definition**: Isotope of germanium with mass 74
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 74Ge, 
  - Ge-74, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2531608">http://www.wikidata.org/entity/Q2531608</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bfb2f06d">http://vocab.terralid.org#c_bfb2f06d</a>


###  germanium-76
- **Definition**: Isotope of germanium with mass 76
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 76Ge, 
  - Ge-76, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2190009">http://www.wikidata.org/entity/Q2190009</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_834c5313">http://vocab.terralid.org#c_834c5313</a>


###  gold-197
- **Definition**: Isotope of gold with mass 197
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 197Au, 
  - Au-197, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883174">http://www.wikidata.org/entity/Q18883174</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_edfee844">http://vocab.terralid.org#c_edfee844</a>


###  hafnium-176
- **Definition**: Isotope of hafnium with mass 176
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 176Hf, 
  - Hf-176, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18087012">http://www.wikidata.org/entity/Q18087012</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eae30078">http://vocab.terralid.org#c_eae30078</a>


###  hafnium-177
- **Definition**: Isotope of hafnium with mass 177
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 177Hf, 
  - Hf-177, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18087014">http://www.wikidata.org/entity/Q18087014</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e098a70">http://vocab.terralid.org#c_9e098a70</a>


###  hafnium-178
- **Definition**: Isotope of hafnium with mass 178
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 178Hf, 
  - Hf-178, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18087016">http://www.wikidata.org/entity/Q18087016</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_33551bf0">http://vocab.terralid.org#c_33551bf0</a>


###  hafnium-179
- **Definition**: Isotope of hafnium with mass 179
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 179Hf, 
  - Hf-179, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18087018">http://www.wikidata.org/entity/Q18087018</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4d844f64">http://vocab.terralid.org#c_4d844f64</a>


###  hafnium-180
- **Definition**: Isotope of hafnium with mass 180
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 180Hf, 
  - Hf-180, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18087020">http://www.wikidata.org/entity/Q18087020</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9069a811">http://vocab.terralid.org#c_9069a811</a>


###  helium-3
- **Definition**: Isotope of helium with mass 3
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 3He, 
  - He-3, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q533498">http://www.wikidata.org/entity/Q533498</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_17f13010">http://vocab.terralid.org#c_17f13010</a>


###  helium-4
- **Definition**: Isotope of helium with mass 4
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 4He, 
  - He-4, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1151346">http://www.wikidata.org/entity/Q1151346</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3a1f8662">http://vocab.terralid.org#c_3a1f8662</a>


###  holmium-165
- **Definition**: Isotope of holmium with mass 165
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 165Ho, 
  - Ho-165, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15876412">http://www.wikidata.org/entity/Q15876412</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5dc5a57f">http://vocab.terralid.org#c_5dc5a57f</a>


###  indium-113
- **Definition**: Isotope of indium with mass 113
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 113In, 
  - In-113, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2322760">http://www.wikidata.org/entity/Q2322760</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cbd4ebe9">http://vocab.terralid.org#c_cbd4ebe9</a>


###  iodine-127
- **Definition**: Isotope of iodine with mass 127
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 127I, 
  - I-127, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3069233">http://www.wikidata.org/entity/Q3069233</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d5f54116">http://vocab.terralid.org#c_d5f54116</a>


###  iridium-191
- **Definition**: Isotope of iridium with mass 191
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 191Ir, 
  - Ir-191, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883039">http://www.wikidata.org/entity/Q18883039</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f16172eb">http://vocab.terralid.org#c_f16172eb</a>


###  iridium-193
- **Definition**: Isotope of iridium with mass 193
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 193Ir, 
  - Ir-193, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883045">http://www.wikidata.org/entity/Q18883045</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d944f289">http://vocab.terralid.org#c_d944f289</a>


###  iron-54
- **Definition**: Isotope of iron with mass 54
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 54Fe, 
  - Fe-54, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2696892">http://www.wikidata.org/entity/Q2696892</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3d11ce8b">http://vocab.terralid.org#c_3d11ce8b</a>


###  iron-56
- **Definition**: Isotope of iron with mass 56
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 56Fe, 
  - Fe-56, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1052454">http://www.wikidata.org/entity/Q1052454</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e898635">http://vocab.terralid.org#c_9e898635</a>


###  iron-57
- **Definition**: Isotope of iron with mass 57
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 57Fe, 
  - Fe-57, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q14744877">http://www.wikidata.org/entity/Q14744877</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5a20b188">http://vocab.terralid.org#c_5a20b188</a>


###  iron-58
- **Definition**: Isotope of iron with mass 58
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 58Fe, 
  - Fe-58, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2704780">http://www.wikidata.org/entity/Q2704780</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_191eb426">http://vocab.terralid.org#c_191eb426</a>


###  krypton-80
- **Definition**: Isotope of krypton with mass 80
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 80Kr, 
  - Kr-80, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2071481">http://www.wikidata.org/entity/Q2071481</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2fedcdf0">http://vocab.terralid.org#c_2fedcdf0</a>


###  krypton-82
- **Definition**: Isotope of krypton with mass 82
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 82Kr, 
  - Kr-82, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2558547">http://www.wikidata.org/entity/Q2558547</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_059f31a1">http://vocab.terralid.org#c_059f31a1</a>


###  krypton-83
- **Definition**: Isotope of krypton with mass 83
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 83Kr, 
  - Kr-83, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1921298">http://www.wikidata.org/entity/Q1921298</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_80a6e9f7">http://vocab.terralid.org#c_80a6e9f7</a>


###  krypton-84
- **Definition**: Isotope of aluminium with mass 84
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 84Kr, 
  - Kr-84, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2163590">http://www.wikidata.org/entity/Q2163590</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c3037190">http://vocab.terralid.org#c_c3037190</a>


###  krypton-86
- **Definition**: Isotope of krypton with mass 86
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 86Kr, 
  - Kr-86, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2195058">http://www.wikidata.org/entity/Q2195058</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_17ac3728">http://vocab.terralid.org#c_17ac3728</a>


###  lanthanum-139
- **Definition**: Isotope of lanthanum with mass 139
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 139La, 
  - La-139, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2424900">http://www.wikidata.org/entity/Q2424900</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2a8d2d0b">http://vocab.terralid.org#c_2a8d2d0b</a>


###  lead-206
- **Definition**: Isotope of lead with mass 206
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 206Pb, 
  - Pb-206, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883438">http://www.wikidata.org/entity/Q18883438</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ef8584a1">http://vocab.terralid.org#c_ef8584a1</a>


###  lead-207
- **Definition**: Isotope of lead with mass 207
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 207Pb, 
  - Pb-207, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883443">http://www.wikidata.org/entity/Q18883443</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bc8d9e4d">http://vocab.terralid.org#c_bc8d9e4d</a>


###  lead-208
- **Definition**: Isotope of lead with mass 208
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 208Pb, 
  - Pb-208, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q16670466">http://www.wikidata.org/entity/Q16670466</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f6d5d4ed">http://vocab.terralid.org#c_f6d5d4ed</a>


###  lithium-6
- **Definition**: Isotope of lithium with mass 6
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 6Li, 
  - Li-6, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q10322200">http://www.wikidata.org/entity/Q10322200</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cb89bf3a">http://vocab.terralid.org#c_cb89bf3a</a>


###  lithium-7
- **Definition**: Isotope of lithium with mass 7
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 7Li, 
  - Li-7, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q10322201">http://www.wikidata.org/entity/Q10322201</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d3787f38">http://vocab.terralid.org#c_d3787f38</a>


###  lutetium-175
- **Definition**: Isotope of lutetium with mass 175
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 175Lu, 
  - Lu-175, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882652">http://www.wikidata.org/entity/Q18882652</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_97e1697a">http://vocab.terralid.org#c_97e1697a</a>


###  magnesium-24
- **Definition**: Isotope of magnesium with mass 24
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 24Mg, 
  - Mg-24, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2096096">http://www.wikidata.org/entity/Q2096096</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4669d0d6">http://vocab.terralid.org#c_4669d0d6</a>


###  magnesium-25
- **Definition**: Isotope of magnesium with mass 25
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 25Mg, 
  - Mg-25, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2796325">http://www.wikidata.org/entity/Q2796325</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d718f7e">http://vocab.terralid.org#c_1d718f7e</a>


###  magnesium-26
- **Definition**: Isotope of magnesium with mass 26
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 26Mg, 
  - Mg-26, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13808814">http://www.wikidata.org/entity/Q13808814</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4ff16f3e">http://vocab.terralid.org#c_4ff16f3e</a>


###  manganese-55
- **Definition**: Isotope of manganese with mass 55
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 55Mn, 
  - Mn-55, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13811964">http://www.wikidata.org/entity/Q13811964</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dce98965">http://vocab.terralid.org#c_dce98965</a>


###  mercury-196
- **Definition**: Isotope of mercury with mass 196
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 196Hg, 
  - Hg-196, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883230">http://www.wikidata.org/entity/Q18883230</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9bd85a6a">http://vocab.terralid.org#c_9bd85a6a</a>


###  mercury-198
- **Definition**: Isotope of mercury with mass 198
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 198Hg, 
  - Hg-198, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883233">http://www.wikidata.org/entity/Q18883233</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_449e5c74">http://vocab.terralid.org#c_449e5c74</a>


###  mercury-199
- **Definition**: Isotope of mercury with mass 199
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 199Hg, 
  - Hg-199, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883234">http://www.wikidata.org/entity/Q18883234</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8425e6e1">http://vocab.terralid.org#c_8425e6e1</a>


###  mercury-200
- **Definition**: Isotope of mercury with mass 200
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 200Hg, 
  - Hg-200, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883236">http://www.wikidata.org/entity/Q18883236</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c4ce97bd">http://vocab.terralid.org#c_c4ce97bd</a>


###  mercury-201
- **Definition**: Isotope of mercury with mass 201
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 201Hg, 
  - Hg-201, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883237">http://www.wikidata.org/entity/Q18883237</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6708f55a">http://vocab.terralid.org#c_6708f55a</a>


###  mercury-202
- **Definition**: Isotope of mercury with mass 202
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 202Hg, 
  - Hg-202, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883239">http://www.wikidata.org/entity/Q18883239</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2d205d68">http://vocab.terralid.org#c_2d205d68</a>


###  mercury-204
- **Definition**: Isotope of mercury with mass 204
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 204Hg, 
  - Hg-204, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883242">http://www.wikidata.org/entity/Q18883242</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2e435946">http://vocab.terralid.org#c_2e435946</a>


###  molybdenum-92
- **Definition**: Isotope of molybdenum with mass 92
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 92Mo, 
  - Mo-92, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4499982">http://www.wikidata.org/entity/Q4499982</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7e6f913e">http://vocab.terralid.org#c_7e6f913e</a>


###  molybdenum-94
- **Definition**: Isotope of molybdenum with mass 94
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 94Mo, 
  - Mo-94, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q13860694">http://www.wikidata.org/entity/Q13860694</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1bf33c5e">http://vocab.terralid.org#c_1bf33c5e</a>


###  molybdenum-95
- **Definition**: Isotope of molybdenum with mass 95
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 95Mo, 
  - Mo-95, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3355387">http://www.wikidata.org/entity/Q3355387</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_24416eb2">http://vocab.terralid.org#c_24416eb2</a>


###  molybdenum-96
- **Definition**: Isotope of molybdenum with mass 96
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 96Mo, 
  - Mo-96, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1928853">http://www.wikidata.org/entity/Q1928853</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c0aebc6">http://vocab.terralid.org#c_6c0aebc6</a>


###  molybdenum-97
- **Definition**: Isotope of molybdenum with mass 97
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 97Mo, 
  - Mo-97, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2690215">http://www.wikidata.org/entity/Q2690215</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee504e86">http://vocab.terralid.org#c_ee504e86</a>


###  molybdenum-98
- **Definition**: Isotope of molybdenum with mass 98
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 98Mo, 
  - Mo-98, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2019439">http://www.wikidata.org/entity/Q2019439</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9cbf34cf">http://vocab.terralid.org#c_9cbf34cf</a>


###  neodymium-142
- **Definition**: Isotope of neodymium with mass 142
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 142Nd, 
  - Nd-142, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3193312">http://www.wikidata.org/entity/Q3193312</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ba468a55">http://vocab.terralid.org#c_ba468a55</a>


###  neodymium-143
- **Definition**: Isotope of neodymium with mass 143
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 143Nd, 
  - Nd-143, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2064444">http://www.wikidata.org/entity/Q2064444</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_204ffd92">http://vocab.terralid.org#c_204ffd92</a>


###  neodymium-145
- **Definition**: Isotope of neodymium with mass 145
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 145Nd, 
  - Nd-145, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2198672">http://www.wikidata.org/entity/Q2198672</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_09489d52">http://vocab.terralid.org#c_09489d52</a>


###  neodymium-146
- **Definition**: Isotope of neodymium with mass 146
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 146Nd, 
  - Nd-146, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1880887">http://www.wikidata.org/entity/Q1880887</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3c8b21b2">http://vocab.terralid.org#c_3c8b21b2</a>


###  neodymium-148
- **Definition**: Isotope of neodymium with mass 148
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 148Nd, 
  - Nd-148, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4990557">http://www.wikidata.org/entity/Q4990557</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7dfdbf8b">http://vocab.terralid.org#c_7dfdbf8b</a>


###  neon-20
- **Definition**: Isotope of neon with mass 20
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 20Ne, 
  - Ne-20, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1956685">http://www.wikidata.org/entity/Q1956685</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bcf548a3">http://vocab.terralid.org#c_bcf548a3</a>


###  neon-21
- **Definition**: Isotope of neon with mass 21
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 21Ne, 
  - Ne-21, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2862844">http://www.wikidata.org/entity/Q2862844</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_56164ad8">http://vocab.terralid.org#c_56164ad8</a>


###  neon-22
- **Definition**: Isotope of neon with mass 22
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 22Ne, 
  - Ne-22, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2021125">http://www.wikidata.org/entity/Q2021125</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_99093f03">http://vocab.terralid.org#c_99093f03</a>


###  nickel-58
- **Definition**: Isotope of nickel with mass 58
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 58Ni, 
  - Ni-58, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2424204">http://www.wikidata.org/entity/Q2424204</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d721ab60">http://vocab.terralid.org#c_d721ab60</a>


###  nickel-60
- **Definition**: Isotope of nickel with mass 60
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 60Ni, 
  - Ni-60, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2103496">http://www.wikidata.org/entity/Q2103496</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d71d09a1">http://vocab.terralid.org#c_d71d09a1</a>


###  nickel-61
- **Definition**: Isotope of nickel with mass 61
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 61Ni, 
  - Ni-61, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2468639">http://www.wikidata.org/entity/Q2468639</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7363d301">http://vocab.terralid.org#c_7363d301</a>


###  nickel-62
- **Definition**: Isotope of nickel with mass 62
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 62Ni, 
  - Ni-62, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q284149">http://www.wikidata.org/entity/Q284149</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cecc8f83">http://vocab.terralid.org#c_cecc8f83</a>


###  nickel-64
- **Definition**: Isotope of nickel with mass 64
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 64Ni, 
  - Ni-64, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q5459468">http://www.wikidata.org/entity/Q5459468</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a0a50681">http://vocab.terralid.org#c_a0a50681</a>


###  niobium-93
- **Definition**: Isotope of niobium with mass 93
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 93Nb, 
  - Nb-93, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2319025">http://www.wikidata.org/entity/Q2319025</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4314df1f">http://vocab.terralid.org#c_4314df1f</a>


###  nitrogen-14
- **Definition**: Isotope of nitrogen with mass 14
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - N-14, 
  - 14N, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1138479">http://www.wikidata.org/entity/Q1138479</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_07c719c5">http://vocab.terralid.org#c_07c719c5</a>


###  nitrogen-15
- **Definition**: Isotope of nitrogen with mass 15
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 15N, 
  - N-15, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3271953">http://www.wikidata.org/entity/Q3271953</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_125a4865">http://vocab.terralid.org#c_125a4865</a>


###  osmium-187
- **Definition**: Isotope of osmium with mass 187
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 187Os, 
  - Os-187, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882972">http://www.wikidata.org/entity/Q18882972</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_16395128">http://vocab.terralid.org#c_16395128</a>


###  osmium-188
- **Definition**: Isotope of osmium with mass 188
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 188Os, 
  - Os-188, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882973">http://www.wikidata.org/entity/Q18882973</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7dbbec2a">http://vocab.terralid.org#c_7dbbec2a</a>


###  osmium-189
- **Definition**: Isotope of osmium with mass 189
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 189Os, 
  - Os-189, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882975">http://www.wikidata.org/entity/Q18882975</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_04af303a">http://vocab.terralid.org#c_04af303a</a>


###  osmium-190
- **Definition**: Isotope of osmium with mass 190
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 190Os, 
  - Os-190, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882977">http://www.wikidata.org/entity/Q18882977</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_107d2645">http://vocab.terralid.org#c_107d2645</a>


###  osmium-192
- **Definition**: Isotope of osmium with mass 192
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 192Os, 
  - Os-192, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882981">http://www.wikidata.org/entity/Q18882981</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5aae9881">http://vocab.terralid.org#c_5aae9881</a>


###  oxygen-16
- **Definition**: Isotope of oxygen with mass 16
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 16O, 
  - O-16, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2309203">http://www.wikidata.org/entity/Q2309203</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_57a4ad83">http://vocab.terralid.org#c_57a4ad83</a>


###  oxygen-17
- **Definition**: Isotope of oxygen with mass 17
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 17O, 
  - O-17, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3359113">http://www.wikidata.org/entity/Q3359113</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_265f3fdc">http://vocab.terralid.org#c_265f3fdc</a>


###  oxygen-18
- **Definition**: Isotope of oxygen with mass 18
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 18O, 
  - O-18, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q662269">http://www.wikidata.org/entity/Q662269</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b248ae80">http://vocab.terralid.org#c_b248ae80</a>


###  palladium-102
- **Definition**: Isotope of palladium with mass 102
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 102Pd, 
  - Pd-102, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2177150">http://www.wikidata.org/entity/Q2177150</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b0c56b41">http://vocab.terralid.org#c_b0c56b41</a>


###  palladium-104
- **Definition**: Isotope of palladium with mass 104
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 104Pd, 
  - Pd-104, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1978569">http://www.wikidata.org/entity/Q1978569</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9a582b93">http://vocab.terralid.org#c_9a582b93</a>


###  palladium-105
- **Definition**: Isotope of palladium with mass 105
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 105Pd, 
  - Pd-105, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2692839">http://www.wikidata.org/entity/Q2692839</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b9836a69">http://vocab.terralid.org#c_b9836a69</a>


###  palladium-106
- **Definition**: Isotope of palladium with mass 106
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 106Pd, 
  - Pd-106, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2541204">http://www.wikidata.org/entity/Q2541204</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_63bcd4be">http://vocab.terralid.org#c_63bcd4be</a>


###  palladium-108
- **Definition**: Isotope of palladium with mass 108
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 108Pd, 
  - Pd-108, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2611037">http://www.wikidata.org/entity/Q2611037</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b7efcb48">http://vocab.terralid.org#c_b7efcb48</a>


###  palladium-110
- **Definition**: Isotope of palladium with mass 110
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 110Pd, 
  - Pd-110, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2890340">http://www.wikidata.org/entity/Q2890340</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cbf072fd">http://vocab.terralid.org#c_cbf072fd</a>


###  phosphorus-31
- **Definition**: Isotope of phosphorus with mass 31
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - P-31, 
  - 31P, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2459552">http://www.wikidata.org/entity/Q2459552</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0bb6a74b">http://vocab.terralid.org#c_0bb6a74b</a>


###  platinum-192
- **Definition**: Isotope of platinum with mass 192
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 192Pt, 
  - Pt-192, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883096">http://www.wikidata.org/entity/Q18883096</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4f25c598">http://vocab.terralid.org#c_4f25c598</a>


###  platinum-194
- **Definition**: Isotope of platinum with mass 194
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 194Pt, 
  - Pt-194, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883099">http://www.wikidata.org/entity/Q18883099</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_78c0a330">http://vocab.terralid.org#c_78c0a330</a>


###  platinum-195
- **Definition**: Isotope of platinum with mass 195
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 195Pt, 
  - Pt-195, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883100">http://www.wikidata.org/entity/Q18883100</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2b5475d8">http://vocab.terralid.org#c_2b5475d8</a>


###  platinum-196
- **Definition**: Isotope of platinum with mass 196
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 196Pt, 
  - Pt-196, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883102">http://www.wikidata.org/entity/Q18883102</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dae04b1d">http://vocab.terralid.org#c_dae04b1d</a>


###  platinum-198
- **Definition**: Isotope of platinum with mass 198
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 198Pt, 
  - Pt-198, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883105">http://www.wikidata.org/entity/Q18883105</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_767bd948">http://vocab.terralid.org#c_767bd948</a>


###  potassium-39
- **Definition**: Isotope of potassium with mass 39
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - K-39, 
  - 39K, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2023226">http://www.wikidata.org/entity/Q2023226</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_035a8f5a">http://vocab.terralid.org#c_035a8f5a</a>


###  potassium-41
- **Definition**: Isotope of potassium with mass 41
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - K-41, 
  - 41K, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2956910">http://www.wikidata.org/entity/Q2956910</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b54d2b45">http://vocab.terralid.org#c_b54d2b45</a>


###  praseodymium-141
- **Definition**: Isotope of praseodymium with mass 141
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 141Pr, 
  - Pr-141, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2496517">http://www.wikidata.org/entity/Q2496517</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_89205aa5">http://vocab.terralid.org#c_89205aa5</a>


###  protium
- **Definition**: Isotope of hydrogen with 0 neutrons with mass 1
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - H-1, 
  - 1H, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q12830437">http://www.wikidata.org/entity/Q12830437</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_921309ce">http://vocab.terralid.org#c_921309ce</a>


###  rhenium-185
- **Definition**: Isotope of rhenium with mass 185
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 185Re, 
  - Re-185, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882926">http://www.wikidata.org/entity/Q18882926</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4c5b0564">http://vocab.terralid.org#c_4c5b0564</a>


###  rhodium-103
- **Definition**: Isotope of rhodium with mass 103
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 103Rh, 
  - Rh-103, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2672056">http://www.wikidata.org/entity/Q2672056</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a274048b">http://vocab.terralid.org#c_a274048b</a>


###  rubidium-85
- **Definition**: Isotope of rubidium with mass 85
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 85Rb, 
  - Rb-85, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2171949">http://www.wikidata.org/entity/Q2171949</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a1037c56">http://vocab.terralid.org#c_a1037c56</a>


###  ruthenium-100
- **Definition**: Isotope of ruthenium with mass 100
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 100Ru, 
  - Ru-100, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2511176">http://www.wikidata.org/entity/Q2511176</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_67749cc6">http://vocab.terralid.org#c_67749cc6</a>


###  ruthenium-101
- **Definition**: Isotope of ruthenium with mass 101
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 101Ru, 
  - Ru-101, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q14292039">http://www.wikidata.org/entity/Q14292039</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e3bb1d50">http://vocab.terralid.org#c_e3bb1d50</a>


###  ruthenium-102
- **Definition**: Isotope of ruthenium with mass 102
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 102Ru, 
  - Ru-102, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3221068">http://www.wikidata.org/entity/Q3221068</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2dd4c061">http://vocab.terralid.org#c_2dd4c061</a>


###  ruthenium-104
- **Definition**: Isotope of ruthenium with mass 104
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 104Ru, 
  - Ru-104, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2705828">http://www.wikidata.org/entity/Q2705828</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_111f7fe3">http://vocab.terralid.org#c_111f7fe3</a>


###  ruthenium-96
- **Definition**: Isotope of ruthenium with mass 96
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 96Ru, 
  - Ru-96, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2251024">http://www.wikidata.org/entity/Q2251024</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_badf250e">http://vocab.terralid.org#c_badf250e</a>


###  ruthenium-98
- **Definition**: Isotope of ruthenium with mass 98
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 98Ru, 
  - Ru-98, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2476375">http://www.wikidata.org/entity/Q2476375</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_02cd39b8">http://vocab.terralid.org#c_02cd39b8</a>


###  ruthenium-99
- **Definition**: Isotope of ruthenium with mass 99
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 99Ru, 
  - Ru-99, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3190653">http://www.wikidata.org/entity/Q3190653</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d79ce101">http://vocab.terralid.org#c_d79ce101</a>


###  samarium-144
- **Definition**: Isotope of samarium with mass 144
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 144Sm, 
  - Sm-144, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1862339">http://www.wikidata.org/entity/Q1862339</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dc9fee51">http://vocab.terralid.org#c_dc9fee51</a>


###  samarium-149
- **Definition**: Isotope of samarium with mass 149
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 149Sm, 
  - Sm-149, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1915454">http://www.wikidata.org/entity/Q1915454</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f2f53cac">http://vocab.terralid.org#c_f2f53cac</a>


###  samarium-150
- **Definition**: Isotope of samarium with mass 150
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 150Sm, 
  - Sm-150, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1905822">http://www.wikidata.org/entity/Q1905822</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b5cd561e">http://vocab.terralid.org#c_b5cd561e</a>


###  samarium-152
- **Definition**: Isotope of samarium with mass 152
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 152Sm, 
  - Sm-152, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2288129">http://www.wikidata.org/entity/Q2288129</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1bb0d387">http://vocab.terralid.org#c_1bb0d387</a>


###  samarium-154
- **Definition**: Isotope of samarium with mass 154
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 154Sm, 
  - Sm-154, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2402263">http://www.wikidata.org/entity/Q2402263</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_130a9e88">http://vocab.terralid.org#c_130a9e88</a>


###  scandium-45
- **Definition**: Isotope of scandium with mass 45
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 45Sc, 
  - Sc-45, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1975917">http://www.wikidata.org/entity/Q1975917</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7f5e3dac">http://vocab.terralid.org#c_7f5e3dac</a>


###  selenium-74
- **Definition**: Isotope of selenium with mass 74
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 74Se, 
  - Se-74, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2806682">http://www.wikidata.org/entity/Q2806682</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0777fed8">http://vocab.terralid.org#c_0777fed8</a>


###  selenium-76
- **Definition**: Isotope of selenium with mass 76
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 76Se, 
  - Se-76, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2533598">http://www.wikidata.org/entity/Q2533598</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e4d0a232">http://vocab.terralid.org#c_e4d0a232</a>


###  selenium-77
- **Definition**: Isotope of selenium with mass 77
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 77Se, 
  - Se-77, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2433972">http://www.wikidata.org/entity/Q2433972</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_79948193">http://vocab.terralid.org#c_79948193</a>


###  selenium-78
- **Definition**: Isotope of selenium with mass 78
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 78Se, 
  - Se-78, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1890759">http://www.wikidata.org/entity/Q1890759</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_45408129">http://vocab.terralid.org#c_45408129</a>


###  selenium-80
- **Definition**: Isotope of selenium with mass 80
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 80Se, 
  - Se-80, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2387529">http://www.wikidata.org/entity/Q2387529</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_48eeee1c">http://vocab.terralid.org#c_48eeee1c</a>


###  selenium-82
- **Definition**: Isotope of selenium with mass 82
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 82Se, 
  - Se-82, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2290353">http://www.wikidata.org/entity/Q2290353</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3cdb41fa">http://vocab.terralid.org#c_3cdb41fa</a>


###  silicon-28
- **Definition**: Isotope of silicon with mass 28
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 28Si, 
  - Si-28, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2236831">http://www.wikidata.org/entity/Q2236831</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_718e4614">http://vocab.terralid.org#c_718e4614</a>


###  silicon-29
- **Definition**: Isotope of silicon with mass 29
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 29Si, 
  - Si-29, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3410389">http://www.wikidata.org/entity/Q3410389</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d86e5206">http://vocab.terralid.org#c_d86e5206</a>


###  silicon-30
- **Definition**: Isotope of silicon with mass 30
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 30Si, 
  - Si-30, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q14338840">http://www.wikidata.org/entity/Q14338840</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_36dbfd1e">http://vocab.terralid.org#c_36dbfd1e</a>


###  silver-107
- **Definition**: Isotope of silver with mass 107
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 107Ag, 
  - Ag-107, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3204948">http://www.wikidata.org/entity/Q3204948</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fac64e23">http://vocab.terralid.org#c_fac64e23</a>


###  silver-109
- **Definition**: Isotope of silver with mass 109
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 109Ag, 
  - Ag-109, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q5518299">http://www.wikidata.org/entity/Q5518299</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c053857">http://vocab.terralid.org#c_6c053857</a>


###  sodium-23
- **Definition**: Isotope of sodium with mass 23
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 23Na, 
  - Na-23, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2265714">http://www.wikidata.org/entity/Q2265714</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_64153bb9">http://vocab.terralid.org#c_64153bb9</a>


###  strontium-84
- **Definition**: Isotope of strontium with mass 84
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 84Sr, 
  - Sr-84, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2226267">http://www.wikidata.org/entity/Q2226267</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a92206d6">http://vocab.terralid.org#c_a92206d6</a>


###  strontium-86
- **Definition**: Isotope of strontium with mass 86
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 86Sr, 
  - Sr-86, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2267980">http://www.wikidata.org/entity/Q2267980</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_668a66e9">http://vocab.terralid.org#c_668a66e9</a>


###  strontium-87
- **Definition**: Isotope of strontium with mass 87
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 87Sr, 
  - Sr-87, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4300037">http://www.wikidata.org/entity/Q4300037</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_81d0af6d">http://vocab.terralid.org#c_81d0af6d</a>


###  strontium-88
- **Definition**: Isotope of strontium with mass 88
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 88Sr, 
  - Sr-88, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3355112">http://www.wikidata.org/entity/Q3355112</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4b9b91b6">http://vocab.terralid.org#c_4b9b91b6</a>


###  sulfur-32
- **Definition**: Isotope of sulphur with mass 32
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - S-32, 
  - 32S, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2375775">http://www.wikidata.org/entity/Q2375775</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_97fe135a">http://vocab.terralid.org#c_97fe135a</a>


###  sulfur-33
- **Definition**: Isotope of sulphur with mass 33
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 33S, 
  - S-33, 
  - sulphur-33, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2055815">http://www.wikidata.org/entity/Q2055815</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b1284fee">http://vocab.terralid.org#c_b1284fee</a>


###  sulfur-34
- **Definition**: Isotope of sulfur with mass 34
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 34S, 
  - S-34, 
  - sulphur-34, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1880449">http://www.wikidata.org/entity/Q1880449</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9ba40373">http://vocab.terralid.org#c_9ba40373</a>


###  sulfur-36
- **Definition**: Isotope of sulphur with mass 36
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 36S, 
  - S-36, 
  - sulphur-36, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2881932">http://www.wikidata.org/entity/Q2881932</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bf26bf88">http://vocab.terralid.org#c_bf26bf88</a>


###  Tantalum-180
- **Definition**: Isotope of tantalum with mass 180
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 180Ta, 
  - Ta-180, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882796">http://www.wikidata.org/entity/Q18882796</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cbc3ed4d">http://vocab.terralid.org#c_cbc3ed4d</a>


###  tantalum-181
- **Definition**: Isotope of tantalum with mass 181
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 181Ta, 
  - Ta-181, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882801">http://www.wikidata.org/entity/Q18882801</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ab630ac0">http://vocab.terralid.org#c_ab630ac0</a>


###  tellurium-120
- **Definition**: Isotope of tellurium with mass 120
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 120Te, 
  - Te-120, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2538285">http://www.wikidata.org/entity/Q2538285</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19df9c97">http://vocab.terralid.org#c_19df9c97</a>


###  tellurium-122
- **Definition**: Isotope of tellurium with mass 122
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 122Te, 
  - Te-122, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q5315292">http://www.wikidata.org/entity/Q5315292</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6de2e4f0">http://vocab.terralid.org#c_6de2e4f0</a>


###  tellurium-124
- **Definition**: Isotope of tellurium with mass 124
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 124Te, 
  - Te-124, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4993070">http://www.wikidata.org/entity/Q4993070</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_13a011a4">http://vocab.terralid.org#c_13a011a4</a>


###  tellurium-125
- **Definition**: Isotope of tellurium with mass 125
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 125Te, 
  - Te-125, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2480123">http://www.wikidata.org/entity/Q2480123</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b60f79de">http://vocab.terralid.org#c_b60f79de</a>


###  tellurium-126
- **Definition**: Isotope of tellurium with mass 126
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 126Te, 
  - Te-126, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q14467249">http://www.wikidata.org/entity/Q14467249</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_969eafbf">http://vocab.terralid.org#c_969eafbf</a>


###  terbium-159
- **Definition**: Isotope of terbium with mass 159
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 159Tb, 
  - Tb-159, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2554426">http://www.wikidata.org/entity/Q2554426</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4c7203f">http://vocab.terralid.org#c_f4c7203f</a>


###  thallium-203
- **Definition**: Isotope of thallium with mass 203
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 203Tl, 
  - Tl-203, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883327">http://www.wikidata.org/entity/Q18883327</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_21a82c22">http://vocab.terralid.org#c_21a82c22</a>


###  thallium-205
- **Definition**: Isotope of thallium with mass 205
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 205Tl, 
  - Tl-205, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18883334">http://www.wikidata.org/entity/Q18883334</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1931aa2b">http://vocab.terralid.org#c_1931aa2b</a>


###  thulium-169
- **Definition**: Isotope of thulium with mass 169
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 169Tm, 
  - Tm-169, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q15882884">http://www.wikidata.org/entity/Q15882884</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8e971c30">http://vocab.terralid.org#c_8e971c30</a>


###  tin-114
- **Definition**: Isotope of tin with mass 114
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 114Sn, 
  - Sn-114, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2191216">http://www.wikidata.org/entity/Q2191216</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_aa3c7724">http://vocab.terralid.org#c_aa3c7724</a>


###  tin-115
- **Definition**: Isotope of tin with mass 115
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 115Sn, 
  - Sn-115, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3039718">http://www.wikidata.org/entity/Q3039718</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ab1de480">http://vocab.terralid.org#c_ab1de480</a>


###  tin-116
- **Definition**: Isotope of tin with mass 116
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 116Sn, 
  - Sn-116, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1995851">http://www.wikidata.org/entity/Q1995851</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_334b1987">http://vocab.terralid.org#c_334b1987</a>


###  tin-117
- **Definition**: Isotope of tin with mass 117
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 117Sn, 
  - Sn-117, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4970255">http://www.wikidata.org/entity/Q4970255</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ad3cdb0f">http://vocab.terralid.org#c_ad3cdb0f</a>


###  tin-118
- **Definition**: Isotope of tin with mass 118
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 118Sn, 
  - Sn-118, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2122600">http://www.wikidata.org/entity/Q2122600</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a6746e4c">http://vocab.terralid.org#c_a6746e4c</a>


###  tin-119
- **Definition**: Isotope of tin with mass 119
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 119Sn, 
  - Sn-119, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2140731">http://www.wikidata.org/entity/Q2140731</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8f7ae05e">http://vocab.terralid.org#c_8f7ae05e</a>


###  tin-120
- **Definition**: Isotope of tin with mass 120
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 120Sn, 
  - Sn-120, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2347800">http://www.wikidata.org/entity/Q2347800</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0ccb3401">http://vocab.terralid.org#c_0ccb3401</a>


###  tin-122
- **Definition**: Isotope of tin with mass 122
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 122Sn, 
  - Sn-122, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1895278">http://www.wikidata.org/entity/Q1895278</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11fc95e5">http://vocab.terralid.org#c_11fc95e5</a>


###  titanium-46
- **Definition**: Isotope of titanium with mass 46
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 46Ti, 
  - Ti-46, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2694202">http://www.wikidata.org/entity/Q2694202</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7fad80a2">http://vocab.terralid.org#c_7fad80a2</a>


###  titanium-47
- **Definition**: Isotope of titanium with mass 47
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 47Ti, 
  - Ti-47, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2484855">http://www.wikidata.org/entity/Q2484855</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a3d8b8b4">http://vocab.terralid.org#c_a3d8b8b4</a>


###  titanium-48
- **Definition**: Isotope of titanium with mass 48
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 48Ti, 
  - Ti-48, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2467450">http://www.wikidata.org/entity/Q2467450</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_01d0f1ce">http://vocab.terralid.org#c_01d0f1ce</a>


###  titanium-49
- **Definition**: Isotope of titanium with mass 49
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 49Ti, 
  - Ti-49, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2482282">http://www.wikidata.org/entity/Q2482282</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_246c1972">http://vocab.terralid.org#c_246c1972</a>


###  titanium-50
- **Definition**: Isotope of titanium with mass 50
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 50Ti, 
  - Ti-50, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2269284">http://www.wikidata.org/entity/Q2269284</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a4c7629b">http://vocab.terralid.org#c_a4c7629b</a>


###  tungsten-182
- **Definition**: Isotope of tungsten with mass 182
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 182W, 
  - W-182, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882864">http://www.wikidata.org/entity/Q18882864</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d51b4ba">http://vocab.terralid.org#c_6d51b4ba</a>


###  tungsten-184
- **Definition**: Isotope of tungsten with mass 184
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 184W, 
  - W-184, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882868">http://www.wikidata.org/entity/Q18882868</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e62451fc">http://vocab.terralid.org#c_e62451fc</a>


###  vanadium-51
- **Definition**: Isotope of vanadium with mass 51
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - V-51, 
  - 51V, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1931262">http://www.wikidata.org/entity/Q1931262</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_94107e51">http://vocab.terralid.org#c_94107e51</a>


###  xenon-126
- **Definition**: Isotope of xenon with mass 126
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 126Xe, 
  - Xe-126, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q3134801">http://www.wikidata.org/entity/Q3134801</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1c0470f4">http://vocab.terralid.org#c_1c0470f4</a>


###  xenon-128
- **Definition**: Isotope of xenon with mass 128
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 128Xe, 
  - Xe-128, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q1953543">http://www.wikidata.org/entity/Q1953543</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d0b13e13">http://vocab.terralid.org#c_d0b13e13</a>


###  xenon-129
- **Definition**: Isotope of xenon with mass 129
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 129Xe, 
  - Xe-129, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2388818">http://www.wikidata.org/entity/Q2388818</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_252ecb30">http://vocab.terralid.org#c_252ecb30</a>


###  xenon-130
- **Definition**: Isotope of xenon with mass 130
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 130Xe, 
  - Xe-130, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2622312">http://www.wikidata.org/entity/Q2622312</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_86c5d1ff">http://vocab.terralid.org#c_86c5d1ff</a>


###  xenon-131
- **Definition**: Isotope of xenon with mass 131
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 131Xe, 
  - Xe-131, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2501965">http://www.wikidata.org/entity/Q2501965</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d1256d1b">http://vocab.terralid.org#c_d1256d1b</a>


###  xenon-132
- **Definition**: Isotope of xenon with mass 132
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 132Xe, 
  - Xe-132, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2125594">http://www.wikidata.org/entity/Q2125594</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0180033a">http://vocab.terralid.org#c_0180033a</a>


###  ytterbium-168
- **Definition**: Isotope of ytterbium with mass 168
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 168Yb, 
  - Yb-168, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882562">http://www.wikidata.org/entity/Q18882562</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5b0e584b">http://vocab.terralid.org#c_5b0e584b</a>


###  ytterbium-170
- **Definition**: Isotope of ytterbium with mass 170
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 170Yb, 
  - Yb-170, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882565">http://www.wikidata.org/entity/Q18882565</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee470414">http://vocab.terralid.org#c_ee470414</a>


###  ytterbium-171
- **Definition**: Isotope of ytterbium with mass 171
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 171Yb, 
  - Yb-171, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882567">http://www.wikidata.org/entity/Q18882567</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d5b4a5a4">http://vocab.terralid.org#c_d5b4a5a4</a>


###  ytterbium-172
- **Definition**: Isotope of ytterbium with mass 172
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 172Yb, 
  - Yb-172, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882570">http://www.wikidata.org/entity/Q18882570</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0f86af5e">http://vocab.terralid.org#c_0f86af5e</a>


###  ytterbium-173
- **Definition**: Isotope of ytterbium with mass 173
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 173Yb, 
  - Yb-173, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882571">http://www.wikidata.org/entity/Q18882571</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a16ae7d6">http://vocab.terralid.org#c_a16ae7d6</a>


###  ytterbium-174
- **Definition**: Isotope of ytterbium with mass 174
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 174Yb, 
  - Yb-174, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882575">http://www.wikidata.org/entity/Q18882575</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b77a42f1">http://vocab.terralid.org#c_b77a42f1</a>


###  ytterbium-176
- **Definition**: Isotope of ytterbium with mass 176
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 176Yb, 
  - Yb-176, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q18882579">http://www.wikidata.org/entity/Q18882579</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_71f01f48">http://vocab.terralid.org#c_71f01f48</a>


###  yttrium-89
- **Definition**: Isotope of yttrium with mass 89
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 89Y, 
  - Y-89, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2581836">http://www.wikidata.org/entity/Q2581836</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e5177e2">http://vocab.terralid.org#c_6e5177e2</a>


###  zinc-66
- **Definition**: Isotope of zinc with mass 66
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 66Zn, 
  - Zn-66, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4046116">http://www.wikidata.org/entity/Q4046116</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_45767302">http://vocab.terralid.org#c_45767302</a>


###  zinc-67
- **Definition**: Isotope of zinc with mass 67
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 67Zn, 
  - Zn-67, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2423143">http://www.wikidata.org/entity/Q2423143</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5134414b">http://vocab.terralid.org#c_5134414b</a>


###  zinc-68
- **Definition**: Isotope of zinc with mass 68
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - Zn-68, 
  - 68Zn, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q8072263">http://www.wikidata.org/entity/Q8072263</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_255b0315">http://vocab.terralid.org#c_255b0315</a>


###  zirconium-90
- **Definition**: Isotope of zirconium with mass 90
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 90Zr, 
  - Zr-90, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2090546">http://www.wikidata.org/entity/Q2090546</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_40f5aec8">http://vocab.terralid.org#c_40f5aec8</a>


###  zirconium-91
- **Definition**: Isotope of zirconium with mass 91
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 91Zr, 
  - Zr-91, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2328556">http://www.wikidata.org/entity/Q2328556</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_21d6e5be">http://vocab.terralid.org#c_21d6e5be</a>


###  zirconium-92
- **Definition**: Isotope of zirconium with mass 92
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 92Zr, 
  - Zr-92, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q2706395">http://www.wikidata.org/entity/Q2706395</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e42ffdb">http://vocab.terralid.org#c_9e42ffdb</a>


###  zirconium-94
- **Definition**: Isotope of zirconium with mass 94
- **Child of**:
  - [`nuclide`](#nuclide)
- **Alternate labels:**
  - 94Zr, 
  - Zr-94, 
- **Matches:**
  - <a href="http://www.wikidata.org/entity/Q4808461">http://www.wikidata.org/entity/Q4808461</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1c1e8e64">http://vocab.terralid.org#c_1c1e8e64</a>



##  object life cycle stage
- **Definition**: The different stages an object undergoes after its
collection in the field.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6eeee275">http://vocab.terralid.org#c_6eeee275</a>


###  conservation stage
- **Definition**: The object is treated in a conservation laboratory
to stop ongoing deterioation and to prepare it for long-term storage.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300404519">http://vocab.getty.edu/aat/300404519</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000011">https://vocabs.dariah.eu/bbt/Concept/000011</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5282dab3">http://vocab.terralid.org#c_5282dab3</a>


###  discovery stage
- **Definition**: The object did not received any treatment (yet)
since its discovery.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300404386">http://vocab.getty.edu/aat/300404386</a> (closeMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000011">https://vocabs.dariah.eu/bbt/Concept/000011</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_687c5f00">http://vocab.terralid.org#c_687c5f00</a>


###  finds processing stage
- **Definition**: The object undergoes limited treatment in the field
such as washing or basic convservation measures.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Alternate labels:**
  - in-situ conservation
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000011">https://vocabs.dariah.eu/bbt/Concept/000011</a> (broadMatch)
  - <a href="http://vocab.getty.edu/aat/300404519">http://vocab.getty.edu/aat/300404519</a> (relatedMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_75b32326">http://vocab.terralid.org#c_75b32326</a>


###  laboratory stage
- **Definition**: The object is under investigation in a laboratory.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007660">http://vocab.getty.edu/aat/300007660</a> (closeMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000018">https://vocabs.dariah.eu/bbt/Concept/000018</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_33bebd59">http://vocab.terralid.org#c_33bebd59</a>


###  restoration stage
- **Definition**: The object is brought back to its original shape as
much as possible, often with addition of missing parts.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053742">http://vocab.getty.edu/aat/300053742</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000011">https://vocabs.dariah.eu/bbt/Concept/000011</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_084b00a4">http://vocab.terralid.org#c_084b00a4</a>


###  storage stage
- **Definition**: The object is stored in a place to keep it safe in
the long term.
- **Child of**:
  - [`object life cycle stage`](#object-life-cycle-stage)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300056390">http://vocab.getty.edu/aat/300056390</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000011">https://vocabs.dariah.eu/bbt/Concept/000011</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_20b5f585">http://vocab.terralid.org#c_20b5f585</a>



##  object material
- **Definition**: The material category of TerraLID used to determine
the material-specific metadata.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9dd8c641">http://vocab.terralid.org#c_9dd8c641</a>


###  ceramic
- **Definition**: The object is (predominantly) made of a nonmetallic
malleable material that was intentionally transformed at high
temperatures into a non-malleable state.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300235507">http://vocab.getty.edu/aat/300235507</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q45621">https://www.wikidata.org/wiki/Q45621</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7fb0caf">http://vocab.terralid.org#c_d7fb0caf</a>


###  glass
- **Definition**: The object is (predominantly) made of an inorganic
vitrous material based on fused silica.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11469">https://www.wikidata.org/wiki/Q11469</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300010797">http://vocab.getty.edu/aat/300010797</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee038e9e">http://vocab.terralid.org#c_ee038e9e</a>


###  metal
- **Definition**: The object is (predominantly) made of a metallic
material.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300010900">http://vocab.getty.edu/aat/300010900</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11426">https://www.wikidata.org/wiki/Q11426</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_068f3adc">http://vocab.terralid.org#c_068f3adc</a>


####  coin
- **Definition**: A usually small, flat and round piece of metal
primarily used as medium of exchange or legal tender. It usually
follows a standardised system in weight and sometimes size and is
produced in large quantities.
- **Child of**:
  - [`metal`](#metal)
- **Matches:**
  - <a href="http://nomisma.org/id/coin">http://nomisma.org/id/coin</a> (exactMatch)
  - <a href="http://www.wikidata.org/entity/Q41207">http://www.wikidata.org/entity/Q41207</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300037222">http://vocab.getty.edu/aat/300037222</a> (exactMatch)
  - <a href="http://d-nb.info/gnd/4040629-5">http://d-nb.info/gnd/4040629-5</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000017">https://vocabs.dariah.eu/bbt/Concept/000017</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9775890c">http://vocab.terralid.org#c_9775890c</a>


###  ore (TerraLID category)
- **Definition**: Geological material from which resources are
extracted, especially metals.
- **Child of**:
  - [`object material`](#object-material)
- **Other Properties:**
  - **scopeNote**: 
This entry refers specifically to the material classification in TerraLID for object-specific metadata. 
- **Concept URI:** <a href="http://vocab.terralid.org#c_dbeb733b">http://vocab.terralid.org#c_dbeb733b</a>


###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`alteration process`](#alteration-process)
  - [`analytical instrument`](#analytical-instrument)
  - [`object material`](#object-material)
  - [`production process`](#production-process)
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc979f8">http://vocab.terralid.org#c_ebc979f8</a>


###  pigment
- **Definition**: The term is used rather loosely here to describe any
material that is used for colouring another material.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Alternate labels:**
  - dye, 
  - paint, 
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300013026">http://vocab.getty.edu/aat/300013026</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q161179">https://www.wikidata.org/wiki/Q161179</a> (exactMatch)
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964</a> (narrowMatch)
  - <a href="http://vocab.getty.edu/aat/300013109">http://vocab.getty.edu/aat/300013109</a> (narrowMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_461a3e6b">http://vocab.terralid.org#c_461a3e6b</a>


###  sediment
- **Definition**: The object is unconsolidated geogenic material that
was deposited by water, wind, or ice.
- **Child of**:
  - [`geological material`](#geological-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300379424">http://vocab.getty.edu/aat/300379424</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q180184">https://www.wikidata.org/wiki/Q180184</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fc64d08c">http://vocab.terralid.org#c_fc64d08c</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  oxide
- **Definition**: Chemical substance containing oxygen and one other
chemical element.
- **Other Properties:**
  - **scopeNote**: 
List of oxides retrieved from https://www.wikidoc.org/index.php/Oxide
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q50690">https://www.wikidata.org/wiki/Q50690</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7014484c">http://vocab.terralid.org#c_7014484c</a>


###  aluminium oxide
- **Definition**: aluminium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Al2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q177342">https://www.wikidata.org/wiki/Q177342</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4b36b188">http://vocab.terralid.org#c_4b36b188</a>


###  antimony pentoxide
- **Definition**: antimony pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sb2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419889">https://www.wikidata.org/wiki/Q419889</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3b73905f">http://vocab.terralid.org#c_3b73905f</a>


###  antimony trioxide
- **Definition**: antimony trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sb2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q409035">https://www.wikidata.org/wiki/Q409035</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e163bfbd">http://vocab.terralid.org#c_e163bfbd</a>


###  arsenic pentoxide
- **Definition**: arsenic pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - As2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411256">https://www.wikidata.org/wiki/Q411256</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11fca549">http://vocab.terralid.org#c_11fca549</a>


###  arsenic trioxide
- **Definition**: arsenic trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - As2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q7739">https://www.wikidata.org/wiki/Q7739</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e1c013d">http://vocab.terralid.org#c_9e1c013d</a>


###  barium oxide
- **Definition**: barium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - BaO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q408892">https://www.wikidata.org/wiki/Q408892</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4119401c">http://vocab.terralid.org#c_4119401c</a>


###  beryllium oxide
- **Definition**: beryllium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - BeO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q422714">https://www.wikidata.org/wiki/Q422714</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_981e3f6c">http://vocab.terralid.org#c_981e3f6c</a>


###  bismuth pentoxide
- **Definition**: bismuth pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Bi2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q4332804">https://www.wikidata.org/wiki/Q4332804</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e9a84865">http://vocab.terralid.org#c_e9a84865</a>


###  bismuth(III) oxide
- **Definition**: bismuth(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Bi2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q252536">https://www.wikidata.org/wiki/Q252536</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87cca409">http://vocab.terralid.org#c_87cca409</a>


###  cadmium oxide
- **Definition**: cadmium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CdO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q196661">https://www.wikidata.org/wiki/Q196661</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_43aac36b">http://vocab.terralid.org#c_43aac36b</a>


###  calcium oxide
- **Definition**: calcium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CaO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q185006">https://www.wikidata.org/wiki/Q185006</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_65421f24">http://vocab.terralid.org#c_65421f24</a>


###  carbon dioxide
- **Definition**: carbon dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1997">https://www.wikidata.org/wiki/Q1997</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_305bca08">http://vocab.terralid.org#c_305bca08</a>


###  carbon monoxide
- **Definition**: carbon monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2025">https://www.wikidata.org/wiki/Q2025</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_21b7771e">http://vocab.terralid.org#c_21b7771e</a>


###  carbon trioxide
- **Definition**: carbon trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q27110034">https://www.wikidata.org/wiki/Q27110034</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f40b7fdb">http://vocab.terralid.org#c_f40b7fdb</a>


###  cerium(IV) oxide
- **Definition**: cerium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CeO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411844">https://www.wikidata.org/wiki/Q411844</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_63ba3eba">http://vocab.terralid.org#c_63ba3eba</a>


###  chlorine dioxide
- **Definition**: chlorine dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ClO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q422080">https://www.wikidata.org/wiki/Q422080</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e6409869">http://vocab.terralid.org#c_e6409869</a>


###  chlorine heptoxide
- **Definition**: chlorine heptoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cl2O7
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2301593">https://www.wikidata.org/wiki/Q2301593</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_13e8632e">http://vocab.terralid.org#c_13e8632e</a>


###  chromium trioxide
- **Definition**: chromium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q931335">https://www.wikidata.org/wiki/Q931335</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_62949c0e">http://vocab.terralid.org#c_62949c0e</a>


###  chromium(II) oxide
- **Definition**: chromium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q414303">https://www.wikidata.org/wiki/Q414303</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_42a32bf3">http://vocab.terralid.org#c_42a32bf3</a>


###  chromium(IV) oxide
- **Definition**: chromium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CrO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2366389">https://www.wikidata.org/wiki/Q2366389</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7d234b2a">http://vocab.terralid.org#c_7d234b2a</a>


###  cobalt(II) oxide
- **Definition**: cobalt(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CoO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411283">https://www.wikidata.org/wiki/Q411283</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6713e9e0">http://vocab.terralid.org#c_6713e9e0</a>


###  copper(I) oxide
- **Definition**: copper(I) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cu2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407709">https://www.wikidata.org/wiki/Q407709</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dfa113ee">http://vocab.terralid.org#c_dfa113ee</a>


###  copper(II) oxide
- **Definition**: copper(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - CuO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421787">https://www.wikidata.org/wiki/Q421787</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2153fad4">http://vocab.terralid.org#c_2153fad4</a>


###  diboron trioxide
- **Definition**: diboron trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - B2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411076">https://www.wikidata.org/wiki/Q411076</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ec1ff2de">http://vocab.terralid.org#c_ec1ff2de</a>


###  dicarbon monoxide
- **Definition**: Dicarbon monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - C2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2741198">https://www.wikidata.org/wiki/Q2741198</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8f4dc06f">http://vocab.terralid.org#c_8f4dc06f</a>


###  dichlorine monoxide
- **Definition**: dichlorine monoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cl2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1154631">https://www.wikidata.org/wiki/Q1154631</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cb2f4398">http://vocab.terralid.org#c_cb2f4398</a>


###  dichromium trioxide
- **Definition**: dichromium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Cr2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407905">https://www.wikidata.org/wiki/Q407905</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_416e9447">http://vocab.terralid.org#c_416e9447</a>


###  dinitrogen pentoxide
- **Definition**: dinitrogen pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q408458">https://www.wikidata.org/wiki/Q408458</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8e23fbf4">http://vocab.terralid.org#c_8e23fbf4</a>


###  dinitrogen tetroxide
- **Definition**: dinitrogen tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O4
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q382984">https://www.wikidata.org/wiki/Q382984</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_99b6629a">http://vocab.terralid.org#c_99b6629a</a>


###  dinitrogen trioxide
- **Definition**: dinitrogen trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - N2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407833">https://www.wikidata.org/wiki/Q407833</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29d3ff32">http://vocab.terralid.org#c_29d3ff32</a>


###  erbium(III) oxide
- **Definition**: erbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Er2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q187473">https://www.wikidata.org/wiki/Q187473</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5b76594c">http://vocab.terralid.org#c_5b76594c</a>


###  gadolinium(III) oxide
- **Definition**: gadolinium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Gd2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419919">https://www.wikidata.org/wiki/Q419919</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9c798327">http://vocab.terralid.org#c_9c798327</a>


###  gallium(III) oxide
- **Definition**: gallium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ga2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419487">https://www.wikidata.org/wiki/Q419487</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7d31fd7c">http://vocab.terralid.org#c_7d31fd7c</a>


###  germanium dioxide
- **Definition**: germanium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - GeO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419133">https://www.wikidata.org/wiki/Q419133</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fd57cc71">http://vocab.terralid.org#c_fd57cc71</a>


###  gold sesquioxide
- **Definition**: gold sesquioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Au2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q415247">https://www.wikidata.org/wiki/Q415247</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_63057619">http://vocab.terralid.org#c_63057619</a>


###  hafnium(IV) oxide
- **Definition**: hafnium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - HfO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418740">https://www.wikidata.org/wiki/Q418740</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bf5d3633">http://vocab.terralid.org#c_bf5d3633</a>


###  holmium(III) oxide
- **Definition**: holmium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ho2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421519">https://www.wikidata.org/wiki/Q421519</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19be4e22">http://vocab.terralid.org#c_19be4e22</a>


###  indium oxide
- **Definition**: indium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - In2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q424955">https://www.wikidata.org/wiki/Q424955</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_909ad0f4">http://vocab.terralid.org#c_909ad0f4</a>


###  iron(II) oxide
- **Definition**: iron(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - FeO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q196680">https://www.wikidata.org/wiki/Q196680</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2bcd7ca0">http://vocab.terralid.org#c_2bcd7ca0</a>


###  iron(III) oxide
- **Definition**: iron(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Fe2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419170">https://www.wikidata.org/wiki/Q419170</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f64b32e0">http://vocab.terralid.org#c_f64b32e0</a>


###  lanthanum(III) oxide
- **Definition**: lanthanum(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - La2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q417250">https://www.wikidata.org/wiki/Q417250</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_29b91fa4">http://vocab.terralid.org#c_29b91fa4</a>


###  lead dioxide
- **Definition**: lead dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PbO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q410749">https://www.wikidata.org/wiki/Q410749</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bcef2678">http://vocab.terralid.org#c_bcef2678</a>


###  lead(II) oxide
- **Definition**: lead(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PbO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407879">https://www.wikidata.org/wiki/Q407879</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_71d63f93">http://vocab.terralid.org#c_71d63f93</a>


###  lithium oxide
- **Definition**: lithium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Li2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q385662">https://www.wikidata.org/wiki/Q385662</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fdff16f4">http://vocab.terralid.org#c_fdff16f4</a>


###  lutetium(III) oxide
- **Definition**: lutetium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Lu2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418048">https://www.wikidata.org/wiki/Q418048</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cca0161a">http://vocab.terralid.org#c_cca0161a</a>


###  magnesium oxide
- **Definition**: magnesium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MgO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q214769">https://www.wikidata.org/wiki/Q214769</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4e952e50">http://vocab.terralid.org#c_4e952e50</a>


###  manganese dioxide
- **Definition**: manganese dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MnO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407674">https://www.wikidata.org/wiki/Q407674</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_33f0dd4f">http://vocab.terralid.org#c_33f0dd4f</a>


###  manganese heptoxide
- **Definition**: manganese heptoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Mn2O7
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q27506">https://www.wikidata.org/wiki/Q27506</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_734314c6">http://vocab.terralid.org#c_734314c6</a>


###  manganese(II) oxide
- **Definition**: manganese(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MnO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q414669">https://www.wikidata.org/wiki/Q414669</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_167c3f61">http://vocab.terralid.org#c_167c3f61</a>


###  mercury(II) oxide
- **Definition**: mercury(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - HgO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q174727">https://www.wikidata.org/wiki/Q174727</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_52244d14">http://vocab.terralid.org#c_52244d14</a>


###  molybdenum trioxide
- **Definition**: molybdenum trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - MoO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q416416">https://www.wikidata.org/wiki/Q416416</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2a4dfe8f">http://vocab.terralid.org#c_2a4dfe8f</a>


###  nickel(II) oxide
- **Definition**: nickel(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NiO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411221">https://www.wikidata.org/wiki/Q411221</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bbf2d83f">http://vocab.terralid.org#c_bbf2d83f</a>


###  nickel(III) oxide
- **Definition**: nickel(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ni2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419873">https://www.wikidata.org/wiki/Q419873</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0816776a">http://vocab.terralid.org#c_0816776a</a>


###  nitric oxide
- **Definition**: nitric oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q207843">https://www.wikidata.org/wiki/Q207843</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8b676b3">http://vocab.terralid.org#c_c8b676b3</a>


###  nitrogen dioxide
- **Definition**: nitrogen dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - NO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q207895">https://www.wikidata.org/wiki/Q207895</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_472e6ab5">http://vocab.terralid.org#c_472e6ab5</a>


###  osmium tetroxide
- **Definition**: osmium tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - OsO4
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q422021">https://www.wikidata.org/wiki/Q422021</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b7afbec3">http://vocab.terralid.org#c_b7afbec3</a>


###  oxidoaluminium
- **Definition**: oxidoaluminium
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - AlO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q133767">https://www.wikidata.org/wiki/Q133767</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87d3476d">http://vocab.terralid.org#c_87d3476d</a>


###  oxygen difluoride
- **Definition**: oxygen difluoride
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - OF2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411301">https://www.wikidata.org/wiki/Q411301</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ec6db833">http://vocab.terralid.org#c_ec6db833</a>


###  palladium(II) oxide
- **Definition**: palladium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PdO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421063">https://www.wikidata.org/wiki/Q421063</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_895707a7">http://vocab.terralid.org#c_895707a7</a>


###  phosphorus pentoxide
- **Definition**: phosphorus pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - P2O5, 
  - P4O10, 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q369309">https://www.wikidata.org/wiki/Q369309</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6ec9fef6">http://vocab.terralid.org#c_6ec9fef6</a>


###  plutonium(IV) oxide
- **Definition**: plutonium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - PuO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q413258">https://www.wikidata.org/wiki/Q413258</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f1eaea78">http://vocab.terralid.org#c_f1eaea78</a>


###  potassium oxide
- **Definition**: potassium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - K2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q408880">https://www.wikidata.org/wiki/Q408880</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_39c30ce1">http://vocab.terralid.org#c_39c30ce1</a>


###  promethium(III) oxide
- **Definition**: promethium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Pm2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421194">https://www.wikidata.org/wiki/Q421194</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f937fd73">http://vocab.terralid.org#c_f937fd73</a>


###  rhenium trioxide
- **Definition**: rhenium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ReO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418954">https://www.wikidata.org/wiki/Q418954</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f51699f5">http://vocab.terralid.org#c_f51699f5</a>


###  rhenium(VII) oxide
- **Definition**: rhenium(VII) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Re2O7
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418325">https://www.wikidata.org/wiki/Q418325</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd8b38a2">http://vocab.terralid.org#c_dd8b38a2</a>


###  rhodium(III) oxide
- **Definition**: rhodium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Rh2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q3488660">https://www.wikidata.org/wiki/Q3488660</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9cad68a9">http://vocab.terralid.org#c_9cad68a9</a>


###  rubidium oxide
- **Definition**: rubidium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Rb2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q425243">https://www.wikidata.org/wiki/Q425243</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_288073f5">http://vocab.terralid.org#c_288073f5</a>


###  ruthenium tetroxide
- **Definition**: ruthenium tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - RuO4
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q416759">https://www.wikidata.org/wiki/Q416759</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_96b4ede4">http://vocab.terralid.org#c_96b4ede4</a>


###  ruthenium(IV) oxide
- **Definition**: ruthenium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - RuO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q417022">https://www.wikidata.org/wiki/Q417022</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1bd5e88e">http://vocab.terralid.org#c_1bd5e88e</a>


###  samarium(III) oxide
- **Definition**: samarium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sm2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421401">https://www.wikidata.org/wiki/Q421401</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4364919">http://vocab.terralid.org#c_f4364919</a>


###  scandium oxide
- **Definition**: scandium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Sc2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418024">https://www.wikidata.org/wiki/Q418024</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2b783324">http://vocab.terralid.org#c_2b783324</a>


###  selenium dioxide
- **Definition**: selenium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SeO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411386">https://www.wikidata.org/wiki/Q411386</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_175ec3f0">http://vocab.terralid.org#c_175ec3f0</a>


###  selenium trioxide
- **Definition**: selenium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SeO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q6070">https://www.wikidata.org/wiki/Q6070</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a9fa058d">http://vocab.terralid.org#c_a9fa058d</a>


###  silicon dioxide
- **Definition**: silicon dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SiO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q116269">https://www.wikidata.org/wiki/Q116269</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_32a7b3c4">http://vocab.terralid.org#c_32a7b3c4</a>


###  silver oxide
- **Definition**: silver oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ag2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407815">https://www.wikidata.org/wiki/Q407815</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e9450ea">http://vocab.terralid.org#c_6e9450ea</a>


###  silver(II) oxide
- **Definition**: silver(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - AgO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q12043383">https://www.wikidata.org/wiki/Q12043383</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_69c7ff92">http://vocab.terralid.org#c_69c7ff92</a>


###  sodium oxide
- **Definition**: sodium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Na2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407467">https://www.wikidata.org/wiki/Q407467</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bfcf2bf1">http://vocab.terralid.org#c_bfcf2bf1</a>


###  strontium oxide
- **Definition**: strontium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SrO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418413">https://www.wikidata.org/wiki/Q418413</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_83e09194">http://vocab.terralid.org#c_83e09194</a>


###  sulfur dioxide
- **Definition**: sulfur dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q5282">https://www.wikidata.org/wiki/Q5282</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4416752">http://vocab.terralid.org#c_f4416752</a>


###  sulfur trioxide
- **Definition**: sulfur trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q242715">https://www.wikidata.org/wiki/Q242715</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c41c55a1">http://vocab.terralid.org#c_c41c55a1</a>


###  tantalum pentoxide
- **Definition**: tantalum pentoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ta2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q425103">https://www.wikidata.org/wiki/Q425103</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_395b4a43">http://vocab.terralid.org#c_395b4a43</a>


###  tellurium dioxide
- **Definition**: tellurium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TeO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q425220">https://www.wikidata.org/wiki/Q425220</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_015515bc">http://vocab.terralid.org#c_015515bc</a>


###  tellurium trioxide
- **Definition**: tellurium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TeO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419581">https://www.wikidata.org/wiki/Q419581</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_99e07679">http://vocab.terralid.org#c_99e07679</a>


###  terbium(III) oxide
- **Definition**: terbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tb2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419879">https://www.wikidata.org/wiki/Q419879</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a4a81fb8">http://vocab.terralid.org#c_a4a81fb8</a>


###  tetraoxygen
- **Definition**: tetraoxygen
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - O4
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q457709">https://www.wikidata.org/wiki/Q457709</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e0df7c75">http://vocab.terralid.org#c_e0df7c75</a>


###  tetraphosphorus hexaoxide
- **Definition**: tetraphosphorus hexaoxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - P4O6
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411876">https://www.wikidata.org/wiki/Q411876</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_abd90373">http://vocab.terralid.org#c_abd90373</a>


###  thallium(I) oxide
- **Definition**: thallium(I) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tl2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2983581">https://www.wikidata.org/wiki/Q2983581</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_df381ea7">http://vocab.terralid.org#c_df381ea7</a>


###  thallium(III) oxide
- **Definition**: thallium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tl2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q419381">https://www.wikidata.org/wiki/Q419381</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_278bad09">http://vocab.terralid.org#c_278bad09</a>


###  thorium dioxide
- **Definition**: thorium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ThO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q420634">https://www.wikidata.org/wiki/Q420634</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_65128842">http://vocab.terralid.org#c_65128842</a>


###  thulium(III) oxide
- **Definition**: thulium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Tm2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q258759">https://www.wikidata.org/wiki/Q258759</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9421cf94">http://vocab.terralid.org#c_9421cf94</a>


###  tin(II) oxide
- **Definition**: tin(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SnO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q204980">https://www.wikidata.org/wiki/Q204980</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4276df9f">http://vocab.terralid.org#c_4276df9f</a>


###  tin(IV) oxide
- **Definition**: tin(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - SnO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q129163">https://www.wikidata.org/wiki/Q129163</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_56fa630e">http://vocab.terralid.org#c_56fa630e</a>


###  titanium dioxide
- **Definition**: titanium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - TiO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q193521">https://www.wikidata.org/wiki/Q193521</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bbd38114">http://vocab.terralid.org#c_bbd38114</a>


###  titanium(III) oxide
- **Definition**: titanium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Ti2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2626625">https://www.wikidata.org/wiki/Q2626625</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4b5def73">http://vocab.terralid.org#c_4b5def73</a>


###  tungsten trioxide
- **Definition**: tungsten trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - WO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q417406">https://www.wikidata.org/wiki/Q417406</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_95ed9d33">http://vocab.terralid.org#c_95ed9d33</a>


###  tungsten(III) oxide
- **Definition**: tungsten(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - W2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q379014">https://www.wikidata.org/wiki/Q379014</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_53345ff8">http://vocab.terralid.org#c_53345ff8</a>


###  tungsten(IV) oxide
- **Definition**: tungsten(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - WO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421387">https://www.wikidata.org/wiki/Q421387</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4494faac">http://vocab.terralid.org#c_4494faac</a>


###  uranium dioxide
- **Definition**: uranium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - UO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q378379">https://www.wikidata.org/wiki/Q378379</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cdfad8d8">http://vocab.terralid.org#c_cdfad8d8</a>


###  uranium trioxide
- **Definition**: uranium trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - UO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q425420">https://www.wikidata.org/wiki/Q425420</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0a93f841">http://vocab.terralid.org#c_0a93f841</a>


###  vanadium(II) oxide
- **Definition**: vanadium(II) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - VO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1966236">https://www.wikidata.org/wiki/Q1966236</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e207f179">http://vocab.terralid.org#c_e207f179</a>


###  vanadium(III) oxide
- **Definition**: vanadium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - V2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q425350">https://www.wikidata.org/wiki/Q425350</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c8abed0">http://vocab.terralid.org#c_6c8abed0</a>


###  vanadium(IV) oxide
- **Definition**: vanadium(IV) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - VO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421440">https://www.wikidata.org/wiki/Q421440</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_07ec6d7d">http://vocab.terralid.org#c_07ec6d7d</a>


###  vanadium(V) oxide
- **Definition**: vanadium(V) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - V2O5
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q409173">https://www.wikidata.org/wiki/Q409173</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f832c87b">http://vocab.terralid.org#c_f832c87b</a>


###  water
- **Definition**: water
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - H2O
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q283">https://www.wikidata.org/wiki/Q283</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0a346cac">http://vocab.terralid.org#c_0a346cac</a>


###  xenon tetroxide
- **Definition**: xenon tetroxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - XeO4
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411822">https://www.wikidata.org/wiki/Q411822</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f478024d">http://vocab.terralid.org#c_f478024d</a>


###  xenon trioxide
- **Definition**: xenon trioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - XeO3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411169">https://www.wikidata.org/wiki/Q411169</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_244e4f2c">http://vocab.terralid.org#c_244e4f2c</a>


###  ytterbium(III) oxide
- **Definition**: ytterbium(III) oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Yb2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q416720">https://www.wikidata.org/wiki/Q416720</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0fc5693f">http://vocab.terralid.org#c_0fc5693f</a>


###  yttrium oxide
- **Definition**: yttrium oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - Y2O3
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q414685">https://www.wikidata.org/wiki/Q414685</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1a025f99">http://vocab.terralid.org#c_1a025f99</a>


###  zinc oxide
- **Definition**: zinc oxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ZnO
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q190077">https://www.wikidata.org/wiki/Q190077</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bd12be77">http://vocab.terralid.org#c_bd12be77</a>


###  zirconium dioxide
- **Definition**: zirconium dioxide
- **Child of**:
  - [`oxide`](#oxide)
- **Alternate labels:**
  - ZrO2
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q36200">https://www.wikidata.org/wiki/Q36200</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b5b645cf">http://vocab.terralid.org#c_b5b645cf</a>



##  pigment component
- **Definition**: The general ingredients creating a pigment.
- **Concept URI:** <a href="http://vocab.terralid.org#c_924da16f">http://vocab.terralid.org#c_924da16f</a>


###  binder
- **Definition**: The part of the pigment that holds the colour-giving
parts together and adheres them to the surface.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300014720">http://vocab.getty.edu/aat/300014720</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q863583">https://www.wikidata.org/wiki/Q863583</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_acda28e6">http://vocab.terralid.org#c_acda28e6</a>


###  colorant
- **Definition**: The colour-giving constituent of a pigment or glass.
- **Child of**:
  - [`glass component`](#glass-component)
  - [`pigment component`](#pigment-component)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q911922">https://www.wikidata.org/wiki/Q911922</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300013026">http://vocab.getty.edu/aat/300013026</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4e57487f">http://vocab.terralid.org#c_4e57487f</a>


###  flux
- **Definition**: Material added to another material to lower its
melting point.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300015137">http://vocab.getty.edu/aat/300015137</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1134475">https://www.wikidata.org/wiki/Q1134475</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c5cb1257">http://vocab.terralid.org#c_c5cb1257</a>


###  impurity
- **Definition**: Material unintentionally included in the pigment.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300223750">http://vocab.getty.edu/aat/300223750</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q7216430">https://www.wikidata.org/wiki/Q7216430</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e3a64656">http://vocab.terralid.org#c_e3a64656</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>


###  various
- **Definition**: It is not possible to differentiate between the
components of the pigment anymore.
- **Child of**:
  - [`pigment component`](#pigment-component)
- **Concept URI:** <a href="http://vocab.terralid.org#c_31227633">http://vocab.terralid.org#c_31227633</a>



##  pigment name
- **Other Properties:**
  - **note**: 
This vocabulary is based on the pigments listed in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_38acd1d1">http://vocab.terralid.org#c_38acd1d1</a>


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
  - <a href="https://www.wikidata.org/wiki/Q381133">https://www.wikidata.org/wiki/Q381133</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_27446acf">http://vocab.terralid.org#c_27446acf</a>


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
  - <a href="https://www.wikidata.org/wiki/Q407125">https://www.wikidata.org/wiki/Q407125</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1940d870">http://vocab.terralid.org#c_1940d870</a>


###  aluminium oxide (pigment)
- **Definition**: An Al-based inorganic and natural pigment with the
chemical formula Al2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2O3 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q177342">https://www.wikidata.org/wiki/Q177342</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ca798b6c">http://vocab.terralid.org#c_ca798b6c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_ab4883bd">http://vocab.terralid.org#c_ab4883bd</a>


###  anatase
- **Definition**: A Ti-based inorganic and natural pigment with the
chemical formula TiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - TiO2 (anatase)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q413357">https://www.wikidata.org/wiki/Q413357</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a24e7815">http://vocab.terralid.org#c_a24e7815</a>


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
  - <a href="https://www.wikidata.org/wiki/Q156526">https://www.wikidata.org/wiki/Q156526</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5219129d">http://vocab.terralid.org#c_5219129d</a>


###  anhydrite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaSO4, 
  - calcium sulfate (anhydrous), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q105439">https://www.wikidata.org/wiki/Q105439</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_acf85f04">http://vocab.terralid.org#c_acf85f04</a>


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
  - <a href="https://www.wikidata.org/wiki/Q409041">https://www.wikidata.org/wiki/Q409041</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8810667b">http://vocab.terralid.org#c_8810667b</a>


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
  - <a href="https://www.wikidata.org/wiki/Q417254">https://www.wikidata.org/wiki/Q417254</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb9c523c">http://vocab.terralid.org#c_eb9c523c</a>


###  arsenic(III) oxide
- **Definition**: A As-based inorganic and natural pigment with the
chemical formula As2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As2O3 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q7739">https://www.wikidata.org/wiki/Q7739</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00694ff3">http://vocab.terralid.org#c_00694ff3</a>


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
  - <a href="https://www.wikidata.org/wiki/Q17990717">https://www.wikidata.org/wiki/Q17990717</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e53b6bc">http://vocab.terralid.org#c_6e53b6bc</a>


###  asbestiform minerals
- **Definition**: A group of inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q4803674">https://www.wikidata.org/wiki/Q4803674</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ab399c01">http://vocab.terralid.org#c_ab399c01</a>


###  asphalt
- **Definition**: An inorganic and natural pigment based on a chemical
complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q167510">https://www.wikidata.org/wiki/Q167510</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_68d45411">http://vocab.terralid.org#c_68d45411</a>


###  atacamite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - copper chloride hydroxide, 
  - Cu2Cl(OH)3 (atacamite), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q409775">https://www.wikidata.org/wiki/Q409775</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f252764f">http://vocab.terralid.org#c_f252764f</a>


###  azurite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu3(CO3)2(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu3(CO3)2(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q4161307">https://www.wikidata.org/wiki/Q4161307</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f3c28be9">http://vocab.terralid.org#c_f3c28be9</a>


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
  - <a href="https://www.wikidata.org/wiki/Q409224">https://www.wikidata.org/wiki/Q409224</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9267b7f6">http://vocab.terralid.org#c_9267b7f6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q82900287">https://www.wikidata.org/wiki/Q82900287</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b57c07a6">http://vocab.terralid.org#c_b57c07a6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q309038">https://www.wikidata.org/wiki/Q309038</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a83e8eaa">http://vocab.terralid.org#c_a83e8eaa</a>


###  bassanite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.xH2O, where x ~ 0.5-0.8.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaSO4.xH2O, where x ~ 0.5-0.8, 
  - calcium sulfate (hemihydrate), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q408259">https://www.wikidata.org/wiki/Q408259</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_727afc46">http://vocab.terralid.org#c_727afc46</a>


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
  - <a href="https://www.wikidata.org/wiki/Q942">https://www.wikidata.org/wiki/Q942</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_abd27d33">http://vocab.terralid.org#c_abd27d33</a>


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
  - <a href="https://www.wikidata.org/wiki/Q419292">https://www.wikidata.org/wiki/Q419292</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ffbcca13">http://vocab.terralid.org#c_ffbcca13</a>


###  bone and yeast cokes
- **Definition**: A C-based inorganic and synthetic pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_d10be7f5">http://vocab.terralid.org#c_d10be7f5</a>


###  botallackite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2Cl(OH)3 (botallackite)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2739239">https://www.wikidata.org/wiki/Q2739239</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0a8e15d2">http://vocab.terralid.org#c_0a8e15d2</a>


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
  - <a href="https://www.wikidata.org/wiki/Q411036">https://www.wikidata.org/wiki/Q411036</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b5df1234">http://vocab.terralid.org#c_b5df1234</a>


###  brown ochre and burnt sienna
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q110645329">https://www.wikidata.org/wiki/Q110645329</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b3250fc4">http://vocab.terralid.org#c_b3250fc4</a>


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
  - <a href="https://www.wikidata.org/wiki/Q23767">https://www.wikidata.org/wiki/Q23767</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e570ba6a">http://vocab.terralid.org#c_e570ba6a</a>


####  aragonite
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`calcium carbonate`](#calcium-carbonate)
- **Alternate labels:**
  - CaCO3 (aragonite)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q82003566">https://www.wikidata.org/wiki/Q82003566</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d5cf070">http://vocab.terralid.org#c_6d5cf070</a>


####  chalk
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`calcium carbonate`](#calcium-carbonate)
- **Alternate labels:**
  - CaCO3 (chalk)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q183670">https://www.wikidata.org/wiki/Q183670</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4b6f93ce">http://vocab.terralid.org#c_4b6f93ce</a>


####  coral
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`calcium carbonate`](#calcium-carbonate)
- **Alternate labels:**
  - CaCO3 (coral)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q171446">https://www.wikidata.org/wiki/Q171446</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4a82a3e9">http://vocab.terralid.org#c_4a82a3e9</a>


####  eggshell
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`calcium carbonate`](#calcium-carbonate)
- **Alternate labels:**
  - CaCO3 (eggshell)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2731253">https://www.wikidata.org/wiki/Q2731253</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_23185837">http://vocab.terralid.org#c_23185837</a>


####  oyster shell
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaCO3.
- **Child of**:
  - [`calcium carbonate`](#calcium-carbonate)
- **Alternate labels:**
  - CaCO3 (oyster shell)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q110619733">https://www.wikidata.org/wiki/Q110619733</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f7844dc4">http://vocab.terralid.org#c_f7844dc4</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_0f9765a8">http://vocab.terralid.org#c_0f9765a8</a>


###  cassiterite
- **Definition**: A Sn-based inorganic and natural pigment with the
chemical formula SnO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SnO2 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q191222">https://www.wikidata.org/wiki/Q191222</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a2fb615f">http://vocab.terralid.org#c_a2fb615f</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1552133">https://www.wikidata.org/wiki/Q1552133</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q425142">https://www.wikidata.org/wiki/Q425142</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_77bedf08">http://vocab.terralid.org#c_77bedf08</a>


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
  - <a href="https://www.wikidata.org/wiki/Q409122">https://www.wikidata.org/wiki/Q409122</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7971c791">http://vocab.terralid.org#c_7971c791</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3665757">https://www.wikidata.org/wiki/Q3665757</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee47568f">http://vocab.terralid.org#c_ee47568f</a>


###  chars
- **Definition**: A C-based inorganic and natural pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_e7d6bfa2">http://vocab.terralid.org#c_e7d6bfa2</a>


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
  - <a href="https://www.wikidata.org/wiki/Q427254">https://www.wikidata.org/wiki/Q427254</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_30be1f40">http://vocab.terralid.org#c_30be1f40</a>


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
  - <a href="https://www.wikidata.org/wiki/Q422903">https://www.wikidata.org/wiki/Q422903</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_76870482">http://vocab.terralid.org#c_76870482</a>


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
  - <a href="https://www.wikidata.org/wiki/Q6163776">https://www.wikidata.org/wiki/Q6163776</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c845ef5">http://vocab.terralid.org#c_6c845ef5</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_112626eb">http://vocab.terralid.org#c_112626eb</a>


###  chromium(III) oxide
- **Definition**: A Cr-based inorganic and synthetic pigment with the
chemical formula Cr2O3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cr2O3 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407905">https://www.wikidata.org/wiki/Q407905</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6052da16">http://vocab.terralid.org#c_6052da16</a>


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
  - <a href="https://www.wikidata.org/wiki/Q22907242">https://www.wikidata.org/wiki/Q22907242</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2f6f42e6">http://vocab.terralid.org#c_2f6f42e6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q104614">https://www.wikidata.org/wiki/Q104614</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d0ab0694">http://vocab.terralid.org#c_d0ab0694</a>


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
  - <a href="https://www.wikidata.org/wiki/Q24489">https://www.wikidata.org/wiki/Q24489</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_976245b6">http://vocab.terralid.org#c_976245b6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q4063718">https://www.wikidata.org/wiki/Q4063718</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e4becf48">http://vocab.terralid.org#c_e4becf48</a>


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
  - <a href="https://www.wikidata.org/wiki/Q15634038">https://www.wikidata.org/wiki/Q15634038</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_df972a0a">http://vocab.terralid.org#c_df972a0a</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f649fe61">http://vocab.terralid.org#c_f649fe61</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_54df3c30">http://vocab.terralid.org#c_54df3c30</a>


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
  - <a href="https://www.wikidata.org/wiki/Q4134928">https://www.wikidata.org/wiki/Q4134928</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dbdef691">http://vocab.terralid.org#c_dbdef691</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_73305a8a">http://vocab.terralid.org#c_73305a8a</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_2a1c5fe3">http://vocab.terralid.org#c_2a1c5fe3</a>


###  copper arsenite group
- **Definition**: A group of Cu-As-based synthetic pigments.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q23636739">https://www.wikidata.org/wiki/Q23636739</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c29fdc48">http://vocab.terralid.org#c_c29fdc48</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1291820">https://www.wikidata.org/wiki/Q1291820</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8a0b38f">http://vocab.terralid.org#c_c8a0b38f</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_0dc73827">http://vocab.terralid.org#c_0dc73827</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83528898">https://www.wikidata.org/wiki/Q83528898</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d50a0c1c">http://vocab.terralid.org#c_d50a0c1c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83528898">https://www.wikidata.org/wiki/Q83528898</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d27d8cdd">http://vocab.terralid.org#c_d27d8cdd</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83528898">https://www.wikidata.org/wiki/Q83528898</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0e32d3f0">http://vocab.terralid.org#c_0e32d3f0</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83528898">https://www.wikidata.org/wiki/Q83528898</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3cbb9a04">http://vocab.terralid.org#c_3cbb9a04</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83528898">https://www.wikidata.org/wiki/Q83528898</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1ae29fc6">http://vocab.terralid.org#c_1ae29fc6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q186357">https://www.wikidata.org/wiki/Q186357</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6ef22ba7">http://vocab.terralid.org#c_6ef22ba7</a>


###  copper(II) oxide (pigment)
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula CuO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - tenorite type and tenorite, 
  - CuO (pigment), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421787">https://www.wikidata.org/wiki/Q421787</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ce78bc60">http://vocab.terralid.org#c_ce78bc60</a>


###  cuprite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2O (pigment), 
  - copper(I) oxide (pigment), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q407335">https://www.wikidata.org/wiki/Q407335</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_84df1f14">http://vocab.terralid.org#c_84df1f14</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3706845">https://www.wikidata.org/wiki/Q3706845</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e83576ca">http://vocab.terralid.org#c_e83576ca</a>


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
  - <a href="https://www.wikidata.org/wiki/Q167741">https://www.wikidata.org/wiki/Q167741</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9a35c6da">http://vocab.terralid.org#c_9a35c6da</a>


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
  - <a href="https://www.wikidata.org/wiki/Q421877">https://www.wikidata.org/wiki/Q421877</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a8e7855c">http://vocab.terralid.org#c_a8e7855c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q253181">https://www.wikidata.org/wiki/Q253181</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_318b6d40">http://vocab.terralid.org#c_318b6d40</a>


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
  - <a href="https://www.wikidata.org/wiki/Q133807926">https://www.wikidata.org/wiki/Q133807926</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_485b59c0">http://vocab.terralid.org#c_485b59c0</a>


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
  - <a href="https://www.wikidata.org/wiki/Q131611792">https://www.wikidata.org/wiki/Q131611792</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c9467ff">http://vocab.terralid.org#c_6c9467ff</a>


###  feldspar minerals
- **Definition**: A group of inorganic and natural pigments.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q170258">https://www.wikidata.org/wiki/Q170258</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b9f1d4d2">http://vocab.terralid.org#c_b9f1d4d2</a>


###  feldspathoid minerals
- **Definition**: A group of inorganic and natural pigment.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1006122">https://www.wikidata.org/wiki/Q1006122</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_86f42d6e">http://vocab.terralid.org#c_86f42d6e</a>


###  flame carbons
- **Definition**: A C-based inorganic and synthetic pigment based on a
chemical complex.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb4c525f">http://vocab.terralid.org#c_eb4c525f</a>


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
  - <a href="https://www.wikidata.org/wiki/Q413374">https://www.wikidata.org/wiki/Q413374</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f70ed0af">http://vocab.terralid.org#c_f70ed0af</a>


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
  - <a href="https://www.wikidata.org/wiki/Q37559">https://www.wikidata.org/wiki/Q37559</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3f1a6b61">http://vocab.terralid.org#c_3f1a6b61</a>


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
  - <a href="https://www.wikidata.org/wiki/Q909115">https://www.wikidata.org/wiki/Q909115</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_caa85d4c">http://vocab.terralid.org#c_caa85d4c</a>


###  glass (pigment)
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
  - <a href="https://www.wikidata.org/wiki/Q11469">https://www.wikidata.org/wiki/Q11469</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c095a984">http://vocab.terralid.org#c_c095a984</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1552133">https://www.wikidata.org/wiki/Q1552133</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q423034">https://www.wikidata.org/wiki/Q423034</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_377e324e">http://vocab.terralid.org#c_377e324e</a>


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
  - <a href="https://www.wikidata.org/wiki/Q413272">https://www.wikidata.org/wiki/Q413272</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8fff9159">http://vocab.terralid.org#c_8fff9159</a>


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
  - <a href="https://www.wikidata.org/wiki/Q189703">https://www.wikidata.org/wiki/Q189703</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7955b2c">http://vocab.terralid.org#c_d7955b2c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q5309">https://www.wikidata.org/wiki/Q5309</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_28a6feab">http://vocab.terralid.org#c_28a6feab</a>


###  green earths
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1552133">https://www.wikidata.org/wiki/Q1552133</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e2f4e9bd">http://vocab.terralid.org#c_e2f4e9bd</a>


###  gypsum
- **Definition**: A Ca-based inorganic and natural pigment with the
chemical formula CaSO4.2H2O.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - CaSO4.2H2O, 
  - calcium sulfate (dihydrate), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q82658">https://www.wikidata.org/wiki/Q82658</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_959fe0ea">http://vocab.terralid.org#c_959fe0ea</a>


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
  - <a href="https://www.wikidata.org/wiki/Q5646726">https://www.wikidata.org/wiki/Q5646726</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_699e5788">http://vocab.terralid.org#c_699e5788</a>


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
  - <a href="https://www.wikidata.org/wiki/Q5646726">https://www.wikidata.org/wiki/Q5646726</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ccccde03">http://vocab.terralid.org#c_ccccde03</a>


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
  - <a href="https://www.wikidata.org/wiki/Q103223">https://www.wikidata.org/wiki/Q103223</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7ee5ce6a">http://vocab.terralid.org#c_7ee5ce6a</a>


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
  - <a href="https://www.wikidata.org/wiki/Q55611196">https://www.wikidata.org/wiki/Q55611196</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_60f19008">http://vocab.terralid.org#c_60f19008</a>


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
  - <a href="https://www.wikidata.org/wiki/Q422662">https://www.wikidata.org/wiki/Q422662</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fc6e3616">http://vocab.terralid.org#c_fc6e3616</a>


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
  - <a href="https://www.wikidata.org/wiki/Q411168">https://www.wikidata.org/wiki/Q411168</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_aadde1cf">http://vocab.terralid.org#c_aadde1cf</a>


###  kaolinite
- **Definition**: A Al-Si-based inorganic and natural clay mineral
pigment from the kaolinite group with the chemical formula
Al2Si2O5(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2Si2O5(OH)4 (kaolinite)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q20406255">https://www.wikidata.org/wiki/Q20406255</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a34b704f">http://vocab.terralid.org#c_a34b704f</a>


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
  - <a href="https://www.wikidata.org/wiki/Q10914750">https://www.wikidata.org/wiki/Q10914750</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f420149c">http://vocab.terralid.org#c_f420149c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_e6963953">http://vocab.terralid.org#c_e6963953</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d78709c">http://vocab.terralid.org#c_1d78709c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q4338141">https://www.wikidata.org/wiki/Q4338141</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0d5c40fd">http://vocab.terralid.org#c_0d5c40fd</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d5dcb6d8">http://vocab.terralid.org#c_d5dcb6d8</a>


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
  - <a href="https://www.wikidata.org/wiki/Q2738147">https://www.wikidata.org/wiki/Q2738147</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_86d5c260">http://vocab.terralid.org#c_86d5c260</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_bad809ea">http://vocab.terralid.org#c_bad809ea</a>


###  lead sulfate (other types)
- **Definition**: A Pb-based inorganic and natural pigment made of
lead sulfides other than PbSO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_5d066542">http://vocab.terralid.org#c_5d066542</a>


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
  - <a href="https://www.wikidata.org/wiki/Q883704">https://www.wikidata.org/wiki/Q883704</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7d971fe0">http://vocab.terralid.org#c_7d971fe0</a>


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
  - <a href="https://www.wikidata.org/wiki/Q125731333">https://www.wikidata.org/wiki/Q125731333</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_01593656">http://vocab.terralid.org#c_01593656</a>


###  lead white
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula 2PbCO3.Pb(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - 2PbCO3.Pb(OH)2, 
  - lead carbonate hydroxide (pigment), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q116470614">https://www.wikidata.org/wiki/Q116470614</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_34bc82ee">http://vocab.terralid.org#c_34bc82ee</a>


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
  - <a href="https://www.wikidata.org/wiki/Q410583">https://www.wikidata.org/wiki/Q410583</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2048807b">http://vocab.terralid.org#c_2048807b</a>


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
  - <a href="https://www.wikidata.org/wiki/Q2362697">https://www.wikidata.org/wiki/Q2362697</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f8a16acc">http://vocab.terralid.org#c_f8a16acc</a>


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
  - <a href="https://www.wikidata.org/wiki/Q82525114">https://www.wikidata.org/wiki/Q82525114</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_16d6b816">http://vocab.terralid.org#c_16d6b816</a>


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
  - <a href="https://www.wikidata.org/wiki/Q425450">https://www.wikidata.org/wiki/Q425450</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bb46e184">http://vocab.terralid.org#c_bb46e184</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_7903d63d">http://vocab.terralid.org#c_7903d63d</a>


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
  - <a href="https://www.wikidata.org/wiki/Q181395">https://www.wikidata.org/wiki/Q181395</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2bd15e2a">http://vocab.terralid.org#c_2bd15e2a</a>


###  malachite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2CO3(OH)2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2CO3(OH)2
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q408815">https://www.wikidata.org/wiki/Q408815</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cd222c05">http://vocab.terralid.org#c_cd222c05</a>


###  manganese oxides
- **Definition**: A Mn-based inorganic and natural pigment made of
various manganese oxides.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q110921543">https://www.wikidata.org/wiki/Q110921543</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d1315130">http://vocab.terralid.org#c_d1315130</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3297608">https://www.wikidata.org/wiki/Q3297608</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8cc93dc4">http://vocab.terralid.org#c_8cc93dc4</a>


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
  - <a href="https://www.wikidata.org/wiki/Q901499">https://www.wikidata.org/wiki/Q901499</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_159b6705">http://vocab.terralid.org#c_159b6705</a>


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
  - <a href="https://www.wikidata.org/wiki/Q415961">https://www.wikidata.org/wiki/Q415961</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7de3a131">http://vocab.terralid.org#c_7de3a131</a>


###  mica group minerals
- **Definition**: A group of inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q114675">https://www.wikidata.org/wiki/Q114675</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5c078f15">http://vocab.terralid.org#c_5c078f15</a>


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
  - <a href="https://www.wikidata.org/wiki/Q422131">https://www.wikidata.org/wiki/Q422131</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_488d8f86">http://vocab.terralid.org#c_488d8f86</a>


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
  - <a href="https://www.wikidata.org/wiki/Q693323">https://www.wikidata.org/wiki/Q693323</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00240e2a">http://vocab.terralid.org#c_00240e2a</a>


###  nacrite
- **Definition**: A Al-Si-based inorganic and natural clay mineral
pigment from the kaolinite group with the chemical formula
Al2Si2O5(OH)4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Al2Si2O5(OH)4 (nacrite)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q418903">https://www.wikidata.org/wiki/Q418903</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_39f96274">http://vocab.terralid.org#c_39f96274</a>


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
  - <a href="https://www.wikidata.org/wiki/Q899295">https://www.wikidata.org/wiki/Q899295</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0a295fe8">http://vocab.terralid.org#c_0a295fe8</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1069438">https://www.wikidata.org/wiki/Q1069438</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c858e62d">http://vocab.terralid.org#c_c858e62d</a>


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
  - <a href="https://www.wikidata.org/wiki/Q420274">https://www.wikidata.org/wiki/Q420274</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2cd83a62">http://vocab.terralid.org#c_2cd83a62</a>


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
  - <a href="https://www.wikidata.org/wiki/Q83020604">https://www.wikidata.org/wiki/Q83020604</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0874360a">http://vocab.terralid.org#c_0874360a</a>


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
  - <a href="https://www.wikidata.org/wiki/Q414065">https://www.wikidata.org/wiki/Q414065</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6c81f28a">http://vocab.terralid.org#c_6c81f28a</a>


###  pararealgar
- **Definition**: An As-based inorganic and natural pigment with the
chemical formula As4S4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As4S4 (pararealgar)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1058825">https://www.wikidata.org/wiki/Q1058825</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5d1e4ab8">http://vocab.terralid.org#c_5d1e4ab8</a>


###  paratacamite
- **Definition**: A Cu-based inorganic and natural pigment with the
chemical formula Cu2Cl(OH)3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Cu2Cl(OH)3 (paratacamite)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1057152">https://www.wikidata.org/wiki/Q1057152</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e71b2ebb">http://vocab.terralid.org#c_e71b2ebb</a>


###  plattnerite
- **Definition**: A Pb-based inorganic and natural pigment with the
chemical formula PbO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbO2 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q2738313">https://www.wikidata.org/wiki/Q2738313</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e9ae944d">http://vocab.terralid.org#c_e9ae944d</a>


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
  - <a href="https://www.wikidata.org/wiki/Q421894">https://www.wikidata.org/wiki/Q421894</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_afeb342a">http://vocab.terralid.org#c_afeb342a</a>


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
  - <a href="https://www.wikidata.org/wiki/Q2479376">https://www.wikidata.org/wiki/Q2479376</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c7ff0c22">http://vocab.terralid.org#c_c7ff0c22</a>


###  pumice
- **Definition**: A Si-based inorganic and natural pigment made of
mixture of amorphous SiO2 and other phases.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q25931026">https://www.wikidata.org/wiki/Q25931026</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5af4a831">http://vocab.terralid.org#c_5af4a831</a>


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
  - <a href="https://www.wikidata.org/wiki/Q333827">https://www.wikidata.org/wiki/Q333827</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ad522ba1">http://vocab.terralid.org#c_ad522ba1</a>


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
  - <a href="https://www.wikidata.org/wiki/Q50769">https://www.wikidata.org/wiki/Q50769</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8c5cddc6">http://vocab.terralid.org#c_8c5cddc6</a>


###  quartz
- **Definition**: A Si-based inorganic and natural pigment with the
chemical formula SiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - SiO2 (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q43010">https://www.wikidata.org/wiki/Q43010</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a1cb5378">http://vocab.terralid.org#c_a1cb5378</a>


###  realgar
- **Definition**: An As-based inorganic and natural pigment with the
chemical formula As4S4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - As4S4 (realgar)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q109746">https://www.wikidata.org/wiki/Q109746</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2c36600a">http://vocab.terralid.org#c_2c36600a</a>


###  red lake pigments
- **Definition**: A Metal-organic-complex inorganic and natural
pigment with a complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_87413a8f">http://vocab.terralid.org#c_87413a8f</a>


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
  - <a href="https://www.wikidata.org/wiki/Q17141476">https://www.wikidata.org/wiki/Q17141476</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_287b8eaf">http://vocab.terralid.org#c_287b8eaf</a>


###  red ochre
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1054292">https://www.wikidata.org/wiki/Q1054292</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_64214b59">http://vocab.terralid.org#c_64214b59</a>


###  rutile
- **Definition**: A Ti-based inorganic and natural pigment with the
chemical formula TiO2.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - TiO2 (rutile)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q320603">https://www.wikidata.org/wiki/Q320603</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_523cbfab">http://vocab.terralid.org#c_523cbfab</a>


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
  - <a href="https://www.wikidata.org/wiki/Q774061">https://www.wikidata.org/wiki/Q774061</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q767608">https://www.wikidata.org/wiki/Q767608</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5156c6e4">http://vocab.terralid.org#c_5156c6e4</a>


###  serpentine group clay minerals
- **Definition**: Complex inorganic and natural clay mineral pigments
from the serpentinite group.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q335249">https://www.wikidata.org/wiki/Q335249</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9591f687">http://vocab.terralid.org#c_9591f687</a>


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
  - <a href="https://www.wikidata.org/wiki/Q107387254">https://www.wikidata.org/wiki/Q107387254</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_94c83a39">http://vocab.terralid.org#c_94c83a39</a>


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
  - <a href="https://www.wikidata.org/wiki/Q41534">https://www.wikidata.org/wiki/Q41534</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e5e5a283">http://vocab.terralid.org#c_e5e5a283</a>


###  stibnite
- **Definition**: A Sb-based inorganic and natural pigment with the
chemical formula Sb2S3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Sb2S3 (mineral)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q421831">https://www.wikidata.org/wiki/Q421831</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7a2bfe0e">http://vocab.terralid.org#c_7a2bfe0e</a>


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
  - <a href="https://www.wikidata.org/wiki/Q682">https://www.wikidata.org/wiki/Q682</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_272d1738">http://vocab.terralid.org#c_272d1738</a>


###  synthetic lead carbonate
- **Definition**: A Pb-based inorganic and synthetic pigment with the
chemical formula PbCO3.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - PbCO3 (synthetic)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q411260">https://www.wikidata.org/wiki/Q411260</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a9faa87b">http://vocab.terralid.org#c_a9faa87b</a>


###  synthetic manganese phosphate
- **Definition**: A Mn-based inorganic and synthetic pigment with the
chemical formula MnPO4.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - MnPO4 (synthetic)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_6b2692af">http://vocab.terralid.org#c_6b2692af</a>


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
  - <a href="https://www.wikidata.org/wiki/Q134583">https://www.wikidata.org/wiki/Q134583</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_08bba0d7">http://vocab.terralid.org#c_08bba0d7</a>


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
  - <a href="https://www.wikidata.org/wiki/Q20730193">https://www.wikidata.org/wiki/Q20730193</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_70e78128">http://vocab.terralid.org#c_70e78128</a>


###  Turner's yellow
- **Definition**: A Pb-based inorganic and synthetic pigment with the
chemical formula PbCl2.5-7PbO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - Lead oxychloride, 
  - PbCl2.5-7PbO, 
  - C.I. Pigment Yellow 30, 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q133256795">https://www.wikidata.org/wiki/Q133256795</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_acadfc5a">http://vocab.terralid.org#c_acadfc5a</a>


###  umbers and wads
- **Definition**: A Fe-Mn-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q901731">https://www.wikidata.org/wiki/Q901731</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1546d26c">http://vocab.terralid.org#c_1546d26c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3518638">https://www.wikidata.org/wiki/Q3518638</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6973d71d">http://vocab.terralid.org#c_6973d71d</a>


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
  - <a href="https://www.wikidata.org/wiki/Q194358">https://www.wikidata.org/wiki/Q194358</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a24984db">http://vocab.terralid.org#c_a24984db</a>


###  vermillion
- **Definition**: A Hg-based inorganic and synthetic pigment with the
chemical formula α-HgS.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - synthetic mercury(II) sulfide, 
  - α-HgS (synthetic), 
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q104614">https://www.wikidata.org/wiki/Q104614</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1291f4c0">http://vocab.terralid.org#c_1291f4c0</a>


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
  - <a href="https://www.wikidata.org/wiki/Q3777850">https://www.wikidata.org/wiki/Q3777850</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f5569e8c">http://vocab.terralid.org#c_f5569e8c</a>


###  yellow lake pigments
- **Definition**: A Metal-organic-complex inorganic and natural
pigment with a complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Concept URI:** <a href="http://vocab.terralid.org#c_7380fd9d">http://vocab.terralid.org#c_7380fd9d</a>


###  yellow ochre
- **Definition**: A Fe-based inorganic and natural pigment with a
complex composition.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q3348755">https://www.wikidata.org/wiki/Q3348755</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_813e37ee">http://vocab.terralid.org#c_813e37ee</a>


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
  - <a href="https://www.wikidata.org/wiki/Q27114864">https://www.wikidata.org/wiki/Q27114864</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8027db1a">http://vocab.terralid.org#c_8027db1a</a>


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
  - <a href="https://www.wikidata.org/wiki/Q204952">https://www.wikidata.org/wiki/Q204952</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_03a70634">http://vocab.terralid.org#c_03a70634</a>


###  zinc(II) oxide
- **Definition**: A Zn-based inorganic and natural pigment with the
chemical formula ZnO.
- **Child of**:
  - [`pigment name`](#pigment-name)
- **Alternate labels:**
  - ZnO (pigment)
- **Other Properties:**
  - **note**: 
Based on information in Eastaugh, N., Walsh, V. (2004). The Pigment compendium: Optical Microscopy of Historic Pigments. Oxford : Elsevier Butterworth-Heinemann
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q190077">https://www.wikidata.org/wiki/Q190077</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_73cbee47">http://vocab.terralid.org#c_73cbee47</a>



##  production context
- **Definition**: Classification for the type of raw materials used in
the production of the object.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f5cb57a0">http://vocab.terralid.org#c_f5cb57a0</a>


###  primary
- **Definition**: The material was not altered after its initial
production from raw materials.
- **Child of**:
  - [`production context`](#production-context)
- **Concept URI:** <a href="http://vocab.terralid.org#c_80dcdedf">http://vocab.terralid.org#c_80dcdedf</a>


###  secondary
- **Definition**: The material was not directly derived from its raw
materials but represent the re-use (mixing, recycling) of materials.
- **Child of**:
  - [`production context`](#production-context)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d179db0a">http://vocab.terralid.org#c_d179db0a</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  production process
- **Definition**: The process by which a material was modified as part
of the production process.
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1408286">https://www.wikidata.org/wiki/Q1408286</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_25f0249a">http://vocab.terralid.org#c_25f0249a</a>


###  absorption
- **Definition**: The material is exposed to another material from
which a specific compound or the entire material gets dissolved into
the material.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053004">http://vocab.getty.edu/aat/300053004</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q332828">https://www.wikidata.org/wiki/Q332828</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_31f5fc72">http://vocab.terralid.org#c_31f5fc72</a>


###  acid reaction
- **Definition**: The partial or complete dissolution of all parts of
a material when exposed to acids.
- **Child of**:
  - [`production process`](#production-process)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6237ab6b">http://vocab.terralid.org#c_6237ab6b</a>


###  grinding
- **Definition**: The material was mechanically reduced to smaller
particles by applying friction.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053090">http://vocab.getty.edu/aat/300053090</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q26882416">https://www.wikidata.org/wiki/Q26882416</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a1b2b905">http://vocab.terralid.org#c_a1b2b905</a>


###  heating
- **Definition**: The material was exposed to high temperatures.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053885">http://vocab.getty.edu/aat/300053885</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q4311765">https://www.wikidata.org/wiki/Q4311765</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_22488ba9">http://vocab.terralid.org#c_22488ba9</a>


###  leaching
- **Definition**: The dissolution of specific parts of a material by
covering or submerging it in a solution such as an acid, solvent, or
water.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053761">http://vocab.getty.edu/aat/300053761</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1483184">https://www.wikidata.org/wiki/Q1483184</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5916e942">http://vocab.terralid.org#c_5916e942</a>


###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`alteration process`](#alteration-process)
  - [`analytical instrument`](#analytical-instrument)
  - [`object material`](#object-material)
  - [`production process`](#production-process)
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc979f8">http://vocab.terralid.org#c_ebc979f8</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>


###  weathering
- **Definition**: The material was exposed to react with its
environment and meteoric water.
- **Child of**:
  - [`production process`](#production-process)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300226583">http://vocab.getty.edu/aat/300226583</a> (closeMatch)
  - <a href="http://vocab.getty.edu/aat/300054115">http://vocab.getty.edu/aat/300054115</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q179177">https://www.wikidata.org/wiki/Q179177</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f37a4790">http://vocab.terralid.org#c_f37a4790</a>



##  recycling indicator
- **Definition**: Classification to indicate whether an object shows
signs of being a recycling product.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e4626b4d">http://vocab.terralid.org#c_e4626b4d</a>


###  not recycled
- **Definition**: The material is not the result of re-using other
materials.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3a6292d6">http://vocab.terralid.org#c_3a6292d6</a>


###  recycled
- **Definition**: One or several materials were converted into the
object.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/end-use-potential/recycling">http://resource.geosciml.org/classifier/cgi/end-use-potential/recycling</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d1e3b55d">http://vocab.terralid.org#c_d1e3b55d</a>


###  recycling suspected
- **Definition**: Indications for a conversion of one or several
materials into the object exist but do not warrant a confirmation.
- **Child of**:
  - [`recycling indicator`](#recycling-indicator)
- **Concept URI:** <a href="http://vocab.terralid.org#c_08e80a7e">http://vocab.terralid.org#c_08e80a7e</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



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
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q906323">https://www.wikidata.org/wiki/Q906323</a> (closeMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c7d45a2d">http://vocab.terralid.org#c_c7d45a2d</a>


###  other
- **Definition**: Any material, type or term not covered by other
terms.
- **Child of**:
  - [`alteration process`](#alteration-process)
  - [`analytical instrument`](#analytical-instrument)
  - [`object material`](#object-material)
  - [`production process`](#production-process)
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ebc979f8">http://vocab.terralid.org#c_ebc979f8</a>


###  Pb Isotope CRMs
- **Definition**: Reference materials used for the calibration of lead
isotope measurement.
- **Child of**:
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cb977df5">http://vocab.terralid.org#c_cb977df5</a>


####  BCR-2
- **Definition**: Reference material prepared by the USGS from basalts
in the Bridal Veil Flow Quarry close to the Columbia River (Oregon,
USA).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bcr-2-geochemical-reference-material-information-sheet-0](https://www.usgs.gov/media/files/bcr-2-geochemical-reference-material-information-sheet-0)
- **Concept URI:** <a href="http://vocab.terralid.org#c_494f507e">http://vocab.terralid.org#c_494f507e</a>


#####  BCR-2G
- **Definition**: Synthethic glass prepared from BCR-2 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BCR-2`](#bcr-2)
- **References**:
  - [https://www.usgs.gov/media/files/bcr-2g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bcr-2g-microanalysis-reference-material-information-sheet)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d365f198">http://vocab.terralid.org#c_d365f198</a>


####  BHVO-2
- **Definition**: Reference material prepared by the USGS from the
surface layer of pahoehoe lava that overflowed from the Halemaumau
Crater in the Kilauea Caldera (Hawaii, USA).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bhvo-2-geochemical-reference-material-information-sheet](https://www.usgs.gov/media/files/bhvo-2-geochemical-reference-material-information-sheet)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e2f20350">http://vocab.terralid.org#c_e2f20350</a>


#####  BHVO-2G
- **Definition**: Synthethic glass prepared from BHVO-2 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BHVO-2`](#bhvo-2)
- **References**:
  - [https://www.usgs.gov/media/files/bhvo-2g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bhvo-2g-microanalysis-reference-material-information-sheet)
- **Concept URI:** <a href="http://vocab.terralid.org#c_638c273b">http://vocab.terralid.org#c_638c273b</a>


####  BIR-1
- **Definition**: Reference material prepared by the USGS from
interglacial lava flows referred to as Rekjavik dolerites (Iceland).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://www.usgs.gov/media/files/bir-1-and-bir-1a-geochemical-reference-material-information-sheet](https://www.usgs.gov/media/files/bir-1-and-bir-1a-geochemical-reference-material-information-sheet)
- **Concept URI:** <a href="http://vocab.terralid.org#c_09290acc">http://vocab.terralid.org#c_09290acc</a>


#####  BIR-1G
- **Definition**: Synthethic glass prepared from BIR-1 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`BIR-1`](#bir-1)
- **References**:
  - [https://www.usgs.gov/media/files/bir-1g-microanalysis-reference-material-information-sheet](https://www.usgs.gov/media/files/bir-1g-microanalysis-reference-material-information-sheet)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ab7e838c">http://vocab.terralid.org#c_ab7e838c</a>


####  ERM-3800
- **Definition**: Lead isotope CRM prepared to provide a CRM with
sufficient isotopic homogeneity to measure differences in the isotopic
composition on the delta-scale.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://doi.org/10.1039/B821400J](https://doi.org/10.1039/B821400J)
- **Concept URI:** <a href="http://vocab.terralid.org#c_910cb973">http://vocab.terralid.org#c_910cb973</a>


####  GSD-1
- **Definition**: Reference material prepared by the Institute of
Geophysical and Geochemical Exploration (IGGE) from a stream sediment
sample collected from a tributary flowing through biotitic granite in
Shanxi province (China).
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://doi.org/10.1111/j.1751-908X.1985.tb00439.x](https://doi.org/10.1111/j.1751-908X.1985.tb00439.x)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f3131ccc">http://vocab.terralid.org#c_f3131ccc</a>


#####  GSD-1G
- **Definition**: Synthethic glass prepared from GSD-1 used for the
measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`GSD-1`](#gsd-1)
- **References**:
  - [https://doi.org/10.1111/j.1751-908X.2005.tb00903.x](https://doi.org/10.1111/j.1751-908X.2005.tb00903.x)
  - [https://doi.org/10.1111/j.1751-908X.2010.00114.x](https://doi.org/10.1111/j.1751-908X.2010.00114.x)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f1060ba4">http://vocab.terralid.org#c_f1060ba4</a>


####  NIST SRM 3328
- **Definition**: Lead isotope CRM prepared from NIST SRM 981, for
which it defines the delta-scale.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/3328.pdf](https://tsapps.nist.gov/srmext/certificates/3328.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2fd6cc95">http://vocab.terralid.org#c_2fd6cc95</a>


####  NIST SRM 610
- **Definition**: Trace element CRM prepared from synthetic glass
widely used for the measurement of lead isotope ratios with laser
ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/612.pdf](https://tsapps.nist.gov/srmext/certificates/612.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bc05e76c">http://vocab.terralid.org#c_bc05e76c</a>


####  NIST SRM 612
- **Definition**: Trace element CRM prepared from synthetic glass used
for the measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/612.pdf](https://tsapps.nist.gov/srmext/certificates/612.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_18a8ec86">http://vocab.terralid.org#c_18a8ec86</a>


####  NIST SRM 614
- **Definition**: Trace element CRM prepared from synthetic glass used
for the measurement of lead isotope ratios with laser ablation.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/614.pdf](https://tsapps.nist.gov/srmext/certificates/614.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1d25bfbf">http://vocab.terralid.org#c_1d25bfbf</a>


####  NIST SRM 981
- **Definition**: Lead isotope CRM prepared from commercially
available high purity lead metal.
- **Child of**:
  - [`Pb Isotope CRMs`](#pb-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/archives/981.pdf](https://tsapps.nist.gov/srmext/certificates/archives/981.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8bafd421">http://vocab.terralid.org#c_8bafd421</a>


###  Tl isotope CRMs
- **Definition**: CRMs used for the calibration of thallium isotope
measurements.
- **Child of**:
  - [`reference material`](#reference-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1041fd60">http://vocab.terralid.org#c_1041fd60</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_bf10432d">http://vocab.terralid.org#c_bf10432d</a>


####  NIST SRM 997
- **Definition**: Thallium isotope CRM prepared from commercially
available high purity thallium metal.
- **Child of**:
  - [`Tl isotope CRMs`](#tl-isotope-crms)
- **References**:
  - [https://tsapps.nist.gov/srmext/certificates/archives/997.pdf](https://tsapps.nist.gov/srmext/certificates/archives/997.pdf)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7a5dc24d">http://vocab.terralid.org#c_7a5dc24d</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  registry
- **Definition**: A registry offers authoritative information on a
defined topic.
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q19386377">https://www.wikidata.org/wiki/Q19386377</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000022">https://vocabs.dariah.eu/bbt/Concept/000022</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_062fe0b0">http://vocab.terralid.org#c_062fe0b0</a>


###  gazetteer
- **Definition**: A service publishing structured authoritative
information about a certain topic, usually locations, based on
ontological principles.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1006160">https://www.wikidata.org/wiki/Q1006160</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q81661634">https://www.wikidata.org/wiki/Q81661634</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_59d96666">http://vocab.terralid.org#c_59d96666</a>


####  Geonames
- **Definition**: Geonames is a geographical database with global
coverage.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q830106">https://www.wikidata.org/wiki/Q830106</a> (exactMatch)
- **References**:
  - [https://www.geonames.org/](https://www.geonames.org/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c18450b7">http://vocab.terralid.org#c_c18450b7</a>


####  iDAI.gazetteer
- **Definition**: The gazetteer of the German Archaeological
Institute.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q93290690">https://www.wikidata.org/wiki/Q93290690</a> (exactMatch)
- **References**:
  - [https://gazetteer.dainst.org/app/?lang=en#!/home](https://gazetteer.dainst.org/app/?lang=en#!/home)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb965d6a">http://vocab.terralid.org#c_eb965d6a</a>


####  PeriodO
- **Definition**: PeriodO is a gazetteer for chronological information
of archaeological, historical and art-historical periods.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q104904881">https://www.wikidata.org/wiki/Q104904881</a> (exactMatch)
- **References**:
  - [https://perio.do/](https://perio.do/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d012defe">http://vocab.terralid.org#c_d012defe</a>


####  Pleiades
- **Definition**: Pleiades is a community-built gazetteer for
archaeological and historical sites with focus on the ancient
Mediterrean and neighbouring regions.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q138510884">https://www.wikidata.org/wiki/Q138510884</a> (exactMatch)
- **References**:
  - [https://pleiades.stoa.org/](https://pleiades.stoa.org/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_81d9c666">http://vocab.terralid.org#c_81d9c666</a>


####  TGN
- **Definition**: The Getty Thesaurus of Geographic Names is a
structured vocabulary for places important in arts and architecture.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1520117">https://www.wikidata.org/wiki/Q1520117</a> (exactMatch)
- **References**:
  - [https://www.getty.edu/research/tools/vocabularies/tgn/index.html](https://www.getty.edu/research/tools/vocabularies/tgn/index.html)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2c0d9965">http://vocab.terralid.org#c_2c0d9965</a>


####  WHG
- **Definition**: The World History Gazetteer provides authoritative
data for historic and archaeological sites for the entire globe.
- **Child of**:
  - [`gazetteer`](#gazetteer)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q130424771">https://www.wikidata.org/wiki/Q130424771</a> (exactMatch)
- **References**:
  - [https://whgazetteer.org/](https://whgazetteer.org/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_321798be">http://vocab.terralid.org#c_321798be</a>


###  GND
- **Definition**: The Gemeinsame Normdatei (GND, Integrated Authority
File) of the German National Library provides authoritative data on a
wide range of topics, among them persons, corporate bodies and
geographic entities. Its main target groups are libraries who used it
for cataloguing their publication.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q54506313">https://www.wikidata.org/wiki/Q54506313</a> (exactMatch)
- **References**:
  - [https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ef46e5df">http://vocab.terralid.org#c_ef46e5df</a>


###  iDAI ChronOntology
- **Definition**: ChronOntology is the ontology for chronological
information of the German Archaological Institute.
- **Child of**:
  - [`registry`](#registry)
- **References**:
  - [https://chronontology.dainst.org/](https://chronontology.dainst.org/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fb11b880">http://vocab.terralid.org#c_fb11b880</a>


###  ORCID
- **Definition**: The Open Researcher and Contributor ID organization
offers persistent identifiers of the same name for persons, with
researchers and scholars as their main audience.
- **Child of**:
  - [`registry`](#registry)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q51044">https://www.wikidata.org/wiki/Q51044</a> (exactMatch)
- **References**:
  - [https://orcid.org/](https://orcid.org/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c62b90a7">http://vocab.terralid.org#c_c62b90a7</a>



##  relationType
- **Definition**: Describes a relationship between the source being
regstered (A) and the related source (B).
- **Other Properties:**
  - **scopeNote**: 
Within TerraLID, the related source (B) is always the entity in TerraLID. 
  - **note**: 
This is a reproduction of the controlled list relationType in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2c9da0f0">http://vocab.terralid.org#c_2c9da0f0</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d01b03c">http://vocab.terralid.org#c_6d01b03c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_50f18eec">http://vocab.terralid.org#c_50f18eec</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_ad976a89">http://vocab.terralid.org#c_ad976a89</a>


###  Continues
- **Definition**: indicates A is a continuation of the work B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#continues](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#continues)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ec92c2c0">http://vocab.terralid.org#c_ec92c2c0</a>


###  Describes
- **Definition**: indicates A describes B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#describes](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#describes)
- **Concept URI:** <a href="http://vocab.terralid.org#c_79a5511e">http://vocab.terralid.org#c_79a5511e</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_85ea27dc">http://vocab.terralid.org#c_85ea27dc</a>


###  HasMetadata
- **Definition**: indicates resource A has additional metadata B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasmetadata](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#hasmetadata)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f14ca7a6">http://vocab.terralid.org#c_f14ca7a6</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_99ef8f93">http://vocab.terralid.org#c_99ef8f93</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_42798d88">http://vocab.terralid.org#c_42798d88</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_4e153d89">http://vocab.terralid.org#c_4e153d89</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_bfa26094">http://vocab.terralid.org#c_bfa26094</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_7209d768">http://vocab.terralid.org#c_7209d768</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_38b56cad">http://vocab.terralid.org#c_38b56cad</a>


###  IsContinuedBy
- **Definition**: indicates A is continued by the work B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscontinuedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#iscontinuedby)
- **Concept URI:** <a href="http://vocab.terralid.org#c_33f972fe">http://vocab.terralid.org#c_33f972fe</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_8aa44c44">http://vocab.terralid.org#c_8aa44c44</a>


###  IsDescribedBy
- **Definition**: indicates A is described by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdescribedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isdescribedby)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c3c2de24">http://vocab.terralid.org#c_c3c2de24</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d85f7b3a">http://vocab.terralid.org#c_d85f7b3a</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_58ed789b">http://vocab.terralid.org#c_58ed789b</a>


###  IsMetadataFor
- **Definition**: indicates additional metadata A for a resource B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ismetadatafor](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ismetadatafor)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b8eafed9">http://vocab.terralid.org#c_b8eafed9</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_5bf18e08">http://vocab.terralid.org#c_5bf18e08</a>


###  IsObsoletedBy
- **Definition**: indicates A is replaced by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isobsoletedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isobsoletedby)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b87ae52a">http://vocab.terralid.org#c_b87ae52a</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f214a28f">http://vocab.terralid.org#c_f214a28f</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_43052c1f">http://vocab.terralid.org#c_43052c1f</a>


###  IsPreviousVersionOf
- **Definition**: indicates A is a previous edition of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispreviousversionof](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#ispreviousversionof)
- **Concept URI:** <a href="http://vocab.terralid.org#c_36fff7dd">http://vocab.terralid.org#c_36fff7dd</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_50fb5931">http://vocab.terralid.org#c_50fb5931</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_6510b31c">http://vocab.terralid.org#c_6510b31c</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_f0352501">http://vocab.terralid.org#c_f0352501</a>


###  IsReviewedBy
- **Definition**: indicates that A is reviewed by B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreviewedby](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#isreviewedby)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8941e0d4">http://vocab.terralid.org#c_8941e0d4</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7654681">http://vocab.terralid.org#c_d7654681</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_7f290a34">http://vocab.terralid.org#c_7f290a34</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_de611488">http://vocab.terralid.org#c_de611488</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e9a7d5d">http://vocab.terralid.org#c_3e9a7d5d</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_4ccf0580">http://vocab.terralid.org#c_4ccf0580</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d1c5bee2">http://vocab.terralid.org#c_d1c5bee2</a>


###  Obsoletes
- **Definition**: indicates A replaces B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#obsoletes](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#obsoletes)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a03285c1">http://vocab.terralid.org#c_a03285c1</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_9e3bfeb6">http://vocab.terralid.org#c_9e3bfeb6</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_83af8ee5">http://vocab.terralid.org#c_83af8ee5</a>


###  Reviews
- **Definition**: indicates that A is a review of B
- **Child of**:
  - [`relationType`](#relationtype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#reviews](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/relationType/#reviews)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1565380d">http://vocab.terralid.org#c_1565380d</a>



##  resourceType
- **Definition**: The type of a resource.
- **Other Properties:**
  - **note**: 
This is a reproduction of a subset of the controlled list resourceTypeGeneral in the DataCite Metadata version schema 4.7. The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000022">https://vocabs.dariah.eu/bbt/Concept/000022</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4f75cdd5">http://vocab.terralid.org#c_4f75cdd5</a>


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
  - <a href="https://www.wikidata.org/wiki/Q758901">https://www.wikidata.org/wiki/Q758901</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#audiovisual](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#audiovisual)
- **Concept URI:** <a href="http://vocab.terralid.org#c_30709214">http://vocab.terralid.org#c_30709214</a>


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
  - <a href="https://www.wikidata.org/wiki/Q618779">https://www.wikidata.org/wiki/Q618779</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#award](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#award)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a8c92376">http://vocab.terralid.org#c_a8c92376</a>


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
  - <a href="https://www.wikidata.org/wiki/Q571">https://www.wikidata.org/wiki/Q571</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#book](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#book)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5c0c5449">http://vocab.terralid.org#c_5c0c5449</a>


###  BookChapter
- **Definition**: One of the main divisions of a book.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q139074677">https://www.wikidata.org/wiki/Q139074677</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#bookchapter](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#bookchapter)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fc66bc62">http://vocab.terralid.org#c_fc66bc62</a>


###  Collection (ResourceType)
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
- **Concept URI:** <a href="http://vocab.terralid.org#c_76209e5e">http://vocab.terralid.org#c_76209e5e</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_0afde725">http://vocab.terralid.org#c_0afde725</a>


###  ConferencePaper
- **Definition**: Article that is written with the goal of being
accepted to a conference.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q23927052">https://www.wikidata.org/wiki/Q23927052</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferencepaper](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferencepaper)
- **Concept URI:** <a href="http://vocab.terralid.org#c_afd22872">http://vocab.terralid.org#c_afd22872</a>


###  ConferenceProceeding
- **Definition**: Collection of academic papers published in the
context of an academic conference.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1143604">https://www.wikidata.org/wiki/Q1143604</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferenceproceeding](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#conferenceproceeding)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4ec6c8f6">http://vocab.terralid.org#c_4ec6c8f6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q17009938">https://www.wikidata.org/wiki/Q17009938</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#datapaper](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#datapaper)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b3d49316">http://vocab.terralid.org#c_b3d49316</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1172284">https://www.wikidata.org/wiki/Q1172284</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dataset](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dataset)
- **Concept URI:** <a href="http://vocab.terralid.org#c_985fe775">http://vocab.terralid.org#c_985fe775</a>


###  Dissertation
- **Definition**: A written essay, treatise, or thesis, especially one
written by a candidate for the degree of Doctor of Philosophy.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1266946">https://www.wikidata.org/wiki/Q1266946</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dissertation](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#dissertation)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3839e9ab">http://vocab.terralid.org#c_3839e9ab</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1656682">https://www.wikidata.org/wiki/Q1656682</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#event](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#event)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4229295c">http://vocab.terralid.org#c_4229295c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q478798">https://www.wikidata.org/wiki/Q478798</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#image](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#image)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d16e61fe">http://vocab.terralid.org#c_d16e61fe</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d40d5def">http://vocab.terralid.org#c_d40d5def</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d0e1459">http://vocab.terralid.org#c_6d0e1459</a>


###  Journal
- **Definition**: A scholarly publication consisting of articles that
is published regularly throughout the year.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q737498">https://www.wikidata.org/wiki/Q737498</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journal](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journal)
- **Concept URI:** <a href="http://vocab.terralid.org#c_15f86bc5">http://vocab.terralid.org#c_15f86bc5</a>


###  JournalArticle
- **Definition**: A written composition on a topic of interest, which
forms a separate part of a journal.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q13442814">https://www.wikidata.org/wiki/Q13442814</a> (closeMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journalarticle](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#journalarticle)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b0ef03ef">http://vocab.terralid.org#c_b0ef03ef</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_095c193d">http://vocab.terralid.org#c_095c193d</a>


###  Other (resourceType)
- **Definition**: Any resource not covered by other terms. If
selected, provide resource type in metadata field "additional
information".
- **Child of**:
  - [`resourceType`](#resourcetype)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#other](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#other)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e4111c25">http://vocab.terralid.org#c_e4111c25</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_c5e4fd1c">http://vocab.terralid.org#c_c5e4fd1c</a>


###  PeerReview
- **Definition**: Evaluation of scientific, academic, or professional
work by others working in the same field.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q215028">https://www.wikidata.org/wiki/Q215028</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#peerreview](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#peerreview)
- **Concept URI:** <a href="http://vocab.terralid.org#c_192f8727">http://vocab.terralid.org#c_192f8727</a>


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
  - <a href="https://www.wikidata.org/wiki/Q223557">https://www.wikidata.org/wiki/Q223557</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#physicalobject](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#physicalobject)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1e1210c6">http://vocab.terralid.org#c_1e1210c6</a>


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
  - <a href="https://www.wikidata.org/wiki/Q580922">https://www.wikidata.org/wiki/Q580922</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#preprint](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#preprint)
- **Concept URI:** <a href="http://vocab.terralid.org#c_945645e4">http://vocab.terralid.org#c_945645e4</a>


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
  - <a href="https://www.wikidata.org/wiki/Q1172284">https://www.wikidata.org/wiki/Q1172284</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#project](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#project)
- **Concept URI:** <a href="http://vocab.terralid.org#c_78ce6c50">http://vocab.terralid.org#c_78ce6c50</a>


###  Report
- **Definition**: A document that presents information in an organized
format for a specific audience and purpose.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q10870555">https://www.wikidata.org/wiki/Q10870555</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#report](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#report)
- **Concept URI:** <a href="http://vocab.terralid.org#c_21afb462">http://vocab.terralid.org#c_21afb462</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_40899a25">http://vocab.terralid.org#c_40899a25</a>


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
  - <a href="https://www.wikidata.org/wiki/Q7397">https://www.wikidata.org/wiki/Q7397</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#software](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#software)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b359ddc1">http://vocab.terralid.org#c_b359ddc1</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_c2b67ae7">http://vocab.terralid.org#c_c2b67ae7</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_2ac847b2">http://vocab.terralid.org#c_2ac847b2</a>


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
- **Concept URI:** <a href="http://vocab.terralid.org#c_d9a7c870">http://vocab.terralid.org#c_d9a7c870</a>


###  Text
- **Definition**: A resource consisting primarily of words for reading
that is not covered by any other textual resource type in this list.
- **Child of**:
  - [`resourceType`](#resourcetype)
- **Other Properties:**
  - **note**: 
The name and definition of this entry are taken from the DataCite Metadata Schema v4.7, published under a Creative Commons Attribution 4.0 (CC-BY 4.0) International license. 
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q234460">https://www.wikidata.org/wiki/Q234460</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#text](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#text)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9fadd71a">http://vocab.terralid.org#c_9fadd71a</a>


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
  - <a href="https://www.wikidata.org/wiki/Q627335">https://www.wikidata.org/wiki/Q627335</a> (exactMatch)
- **References**:
  - [https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#workflow](https://datacite-metadata-schema.readthedocs.io/en/4.7/appendices/appendix-1/resourceTypeGeneral/#workflow)
- **Concept URI:** <a href="http://vocab.terralid.org#c_eb3431d5">http://vocab.terralid.org#c_eb3431d5</a>



##  sample access
- **Definition**: General information about whether objects or
materials are available for investigation.
- **Concept URI:** <a href="http://vocab.terralid.org#c_6de9e3f7">http://vocab.terralid.org#c_6de9e3f7</a>


###  accessible
- **Definition**: The object or material is generally accessible for
investigation.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** <a href="http://vocab.terralid.org#c_06c40941">http://vocab.terralid.org#c_06c40941</a>


###  destroyed
- **Definition**: The object or material was completely destroyed
(e.g., during analysis or in a destruction event) with records for
this event being available.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5df8720f">http://vocab.terralid.org#c_5df8720f</a>


###  inaccessible
- **Definition**: The object or material is not accessible for
investigation or analysis in general.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fba4dbc9">http://vocab.terralid.org#c_fba4dbc9</a>


###  lost
- **Definition**: The object or material cannot be localised any more
and its whereabouts cannot be reconstructed.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e9109c4">http://vocab.terralid.org#c_6e9109c4</a>


###  policy
- **Definition**: The institution holding the object or material has a
policy regulating access to objects and materials for investigation.
- **Child of**:
  - [`sample access`](#sample-access)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b1cf95c1">http://vocab.terralid.org#c_b1cf95c1</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  sample housing
- **Definition**: The material the object is stored in.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000017">https://vocabs.dariah.eu/bbt/Concept/000017</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b53eb953">http://vocab.terralid.org#c_b53eb953</a>


###  cardboard box
- **Definition**: A container made of thick stiff pasteboard with
either a lid or a foldable parts on its top for closing it.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300215468">http://vocab.getty.edu/aat/300215468</a> (broadMatch)
  - <a href="http://vocab.getty.edu/aat/300200342">http://vocab.getty.edu/aat/300200342</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1a3ca880">http://vocab.terralid.org#c_1a3ca880</a>


####  acid-free cardboard box
- **Definition**: A cardboard box certified to be acid free.
- **Child of**:
  - [`cardboard box`](#cardboard-box)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6fedae89">http://vocab.terralid.org#c_6fedae89</a>


####  non acid-free cardboard box
- **Definition**: A cardboard box not certified to be acid free.
- **Child of**:
  - [`cardboard box`](#cardboard-box)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ae7c0b8c">http://vocab.terralid.org#c_ae7c0b8c</a>


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
  - <a href="http://vocab.getty.edu/aat/300077356">http://vocab.getty.edu/aat/300077356</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q3561331">https://www.wikidata.org/wiki/Q3561331</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c56bc948">http://vocab.terralid.org#c_c56bc948</a>


####  controlled environment display case
- **Definition**: A display case equipped to control the environment
in it (e.g., temperature, humidity, chemical pollutants).
- **Child of**:
  - [`display case`](#display-case)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d9a8b325">http://vocab.terralid.org#c_d9a8b325</a>


####  uncontrolled environment display case
- **Definition**: A display case not equipped to control the
environment in it.
- **Child of**:
  - [`display case`](#display-case)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e1c7a89c">http://vocab.terralid.org#c_e1c7a89c</a>


###  Eppendorf tube
- **Definition**: A tube with a hinged sealing cap made of
(shatterproof) plastics.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1933961">https://www.wikidata.org/wiki/Q1933961</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300198822">http://vocab.getty.edu/aat/300198822</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_518ec832">http://vocab.terralid.org#c_518ec832</a>


###  fabric bag
- **Definition**: A flexible container made of woven material.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300194509">http://vocab.getty.edu/aat/300194509</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cbbc3d94">http://vocab.terralid.org#c_cbbc3d94</a>


####  cotton fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`fabric bag`](#fabric-bag)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ccf5461d">http://vocab.terralid.org#c_ccf5461d</a>


####  plastics fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`fabric bag`](#fabric-bag)
  - [`plastics bag`](#plastics-bag)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f26d0d8c">http://vocab.terralid.org#c_f26d0d8c</a>


###  glass vial
- **Definition**: A vial made of glass and closed with a lid, often
made of plastics. They come in various shapes and sizes and with
various types of lids.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300198822">http://vocab.getty.edu/aat/300198822</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e7fdebfb">http://vocab.terralid.org#c_e7fdebfb</a>


###  no housing
- **Definition**: The objects are not stored in a container, usually
because of their size and/or weight.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0e85ae39">http://vocab.terralid.org#c_0e85ae39</a>


###  paper bag
- **Definition**: A flexible container made of paper. Includes
envelopes, which are paper bags that can be seabled by some sort of
pre-applied adhesive on the closing flap.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Alternate labels:**
  - paper envelope
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q379754">https://www.wikidata.org/wiki/Q379754</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300194509">http://vocab.getty.edu/aat/300194509</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_850e4a23">http://vocab.terralid.org#c_850e4a23</a>


####  acid-free paper bag
- **Definition**: A paper bag or envelope certified to be acid free.
- **Child of**:
  - [`paper bag`](#paper-bag)
- **Concept URI:** <a href="http://vocab.terralid.org#c_77b00da1">http://vocab.terralid.org#c_77b00da1</a>


####  non acid-free paper bag
- **Definition**: A paper bag or envelope not certified to be acid
free.
- **Child of**:
  - [`paper bag`](#paper-bag)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a1f7691a">http://vocab.terralid.org#c_a1f7691a</a>


###  plastics bag
- **Definition**: A usually non-sealable flexible container made of
plastics.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300194509">http://vocab.getty.edu/aat/300194509</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f641a35c">http://vocab.terralid.org#c_f641a35c</a>


####  plastics fabric bag
- **Definition**: A fabric bag with cotton as material for the fabric.
- **Child of**:
  - [`fabric bag`](#fabric-bag)
  - [`plastics bag`](#plastics-bag)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f26d0d8c">http://vocab.terralid.org#c_f26d0d8c</a>


####  ziplock bag
- **Definition**: A re-sealable storage made of plastics, usually
polyethylene (PE).
- **Child of**:
  - [`plastics bag`](#plastics-bag)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300194509">http://vocab.getty.edu/aat/300194509</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_10420b12">http://vocab.terralid.org#c_10420b12</a>


###  PTFE/Teflon vial
- **Definition**: A vial with lid made of PTFE or Teflon.
- **Child of**:
  - [`sample housing`](#sample-housing)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300198822">http://vocab.getty.edu/aat/300198822</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3bb341cf">http://vocab.terralid.org#c_3bb341cf</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  sample introduction
- **Definition**: The aggregate state in which the sample is being
analysed.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d31174dd">http://vocab.terralid.org#c_d31174dd</a>


###  laser ablation
- **Definition**: The sample was ablated with a laser and the ablated
particles are analysed.
- **Child of**:
  - [`sample introduction`](#sample-introduction)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379663">http://vocab.getty.edu/aat/300379663</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q1806547">https://www.wikidata.org/wiki/Q1806547</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_95cd19d8">http://vocab.terralid.org#c_95cd19d8</a>


###  solution
- **Definition**: The sample was dissolved in liquids and the solution
is analysed.
- **Child of**:
  - [`sample introduction`](#sample-introduction)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q5447188">https://www.wikidata.org/wiki/Q5447188</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300210311">http://vocab.getty.edu/aat/300210311</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4301bc07">http://vocab.terralid.org#c_4301bc07</a>



##  sample material
- **Definition**: The physical matter that was sampled for analysis.
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dd76eaab">http://vocab.terralid.org#c_dd76eaab</a>


###  alteration product
- **Definition**: Material that was transformed by the interaction of
its pristine state with the (depositional) environment.
- **Child of**:
  - [`sample material`](#sample-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d5356583">http://vocab.terralid.org#c_d5356583</a>


####  alteration product (anthropogenic)
- **Definition**: Anthropogenic material that is impacted by
interaction processes with the (depositional) environment.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`anthropogenic material`](#anthropogenic-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1e35bdea">http://vocab.terralid.org#c_1e35bdea</a>


####  alteration product (hydrothermal)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by hydrothermal solutions.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b81f7872">http://vocab.terralid.org#c_b81f7872</a>


####  alteration product (supergene)
- **Definition**: A rock whose chemical or mineralogical composition
is changed by weathering.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`assemblage`](#assemblage)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f4468f4e">http://vocab.terralid.org#c_f4468f4e</a>


###  anthropogenic material
- **Definition**: Material that was created by humans.
- **Child of**:
  - [`sample material`](#sample-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material">http://resource.geosciml.org/classifier/cgi/lithology/anthropogenic_material</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_62b205ba">http://vocab.terralid.org#c_62b205ba</a>


####  alteration product (anthropogenic)
- **Definition**: Anthropogenic material that is impacted by
interaction processes with the (depositional) environment.
- **Child of**:
  - [`alteration product`](#alteration-product)
  - [`anthropogenic material`](#anthropogenic-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1e35bdea">http://vocab.terralid.org#c_1e35bdea</a>


####  ceramic
- **Definition**: The object is (predominantly) made of a nonmetallic
malleable material that was intentionally transformed at high
temperatures into a non-malleable state.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23972</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300235507">http://vocab.getty.edu/aat/300235507</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q45621">https://www.wikidata.org/wiki/Q45621</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d7fb0caf">http://vocab.terralid.org#c_d7fb0caf</a>


####  glass
- **Definition**: The object is (predominantly) made of an inorganic
vitrous material based on fused silica.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23774</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11469">https://www.wikidata.org/wiki/Q11469</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300010797">http://vocab.getty.edu/aat/300010797</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ee038e9e">http://vocab.terralid.org#c_ee038e9e</a>


####  metal
- **Definition**: The object is (predominantly) made of a metallic
material.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23792</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300010900">http://vocab.getty.edu/aat/300010900</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11426">https://www.wikidata.org/wiki/Q11426</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_068f3adc">http://vocab.terralid.org#c_068f3adc</a>


#####  coin
- **Definition**: A usually small, flat and round piece of metal
primarily used as medium of exchange or legal tender. It usually
follows a standardised system in weight and sometimes size and is
produced in large quantities.
- **Child of**:
  - [`metal`](#metal)
- **Matches:**
  - <a href="http://nomisma.org/id/coin">http://nomisma.org/id/coin</a> (exactMatch)
  - <a href="http://www.wikidata.org/entity/Q41207">http://www.wikidata.org/entity/Q41207</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300037222">http://vocab.getty.edu/aat/300037222</a> (exactMatch)
  - <a href="http://d-nb.info/gnd/4040629-5">http://d-nb.info/gnd/4040629-5</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000017">https://vocabs.dariah.eu/bbt/Concept/000017</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9775890c">http://vocab.terralid.org#c_9775890c</a>


####  pigment
- **Definition**: The term is used rather loosely here to describe any
material that is used for colouring another material.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`object material`](#object-material)
- **Alternate labels:**
  - dye, 
  - paint, 
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300013026">http://vocab.getty.edu/aat/300013026</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q161179">https://www.wikidata.org/wiki/Q161179</a> (exactMatch)
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23964</a> (narrowMatch)
  - <a href="http://vocab.getty.edu/aat/300013109">http://vocab.getty.edu/aat/300013109</a> (narrowMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_461a3e6b">http://vocab.terralid.org#c_461a3e6b</a>


####  unaltered material
- **Definition**: Anthropogenic material without any perceivable
impact from interaction prosesses with the (depositional) environment.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered">http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3a384c38">http://vocab.terralid.org#c_3a384c38</a>


###  bulk
- **Definition**: A fraction of the material that represents the
average composition of the material.
- **Child of**:
  - [`sample material`](#sample-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d339fac4">http://vocab.terralid.org#c_d339fac4</a>


###  geological material
- **Definition**: Material that was created by geological processes.
- **Child of**:
  - [`sample material`](#sample-material)
- **Concept URI:** <a href="http://vocab.terralid.org#c_888076c5">http://vocab.terralid.org#c_888076c5</a>


####  gossan
- **Definition**: The outcropping, heavily weathered part of a
mineralisation.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan">http://resource.geosciml.org/classifier/cgi/earth-resource-expression/gossan</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q639293">https://www.wikidata.org/wiki/Q639293</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e6cf20b1">http://vocab.terralid.org#c_e6cf20b1</a>


####  host rock
- **Definition**: The country rock or rock body in which a
mineralisation occurs.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/host-rock</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9c0fc70d">http://vocab.terralid.org#c_9c0fc70d</a>


####  mineral
- **Definition**: A crystalline component of the material with a
fairly well-defined crystal structure and chemical composition.
- **Child of**:
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23931">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23931</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300011068">http://vocab.getty.edu/aat/300011068</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q7946">https://www.wikidata.org/wiki/Q7946</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b5560869">http://vocab.terralid.org#c_b5560869</a>


####  ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (exactMatch)
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23771</a> (exactMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/raw-material-role/ore">http://resource.geosciml.org/classifier/cgi/raw-material-role/ore</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300152583">http://vocab.getty.edu/aat/300152583</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4dffb82b">http://vocab.terralid.org#c_4dffb82b</a>


#####  alteration
- **Definition**: The part of the ore that is affected by natural
post-genetic processes, often including interaction with a hydrous
fluid.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/alteration-product</a> (exactMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/eventprocess/alteration">http://resource.geosciml.org/classifier/cgi/eventprocess/alteration</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_27e6e534">http://vocab.terralid.org#c_27e6e534</a>


#####  ore mineral
- **Definition**: The economically viable part of the ore.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/raw-material-role/ore">http://resource.geosciml.org/classifier/cgi/raw-material-role/ore</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1969263">https://www.wikidata.org/wiki/Q1969263</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_39a52896">http://vocab.terralid.org#c_39a52896</a>


######  major mineral
- **Definition**: An economically viable mineral dominating the ore's
mineralogical composition.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6e9f3cf6">http://vocab.terralid.org#c_6e9f3cf6</a>


######  minor mineral
- **Definition**: An economically viable mineral constituting a minor
part in the ore's mineralogy.
- **Child of**:
  - [`ore mineral`](#ore-mineral)
- **Concept URI:** <a href="http://vocab.terralid.org#c_42b68c9f">http://vocab.terralid.org#c_42b68c9f</a>


#####  primary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was not altered by hydrothermal
processes or weathering.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1823779e">http://vocab.terralid.org#c_1823779e</a>


#####  secondary ore
- **Definition**: The material that is extracted from a mineralisation
because of its economic value that was altered by hydrothermal
processes or weathering. The term usually refers to ore that became
enriched in the targeted elements because of alteration processes.
- **Child of**:
  - [`ore`](#ore)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/ore</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_adc64d1b">http://vocab.terralid.org#c_adc64d1b</a>


####  sediment
- **Definition**: The object is unconsolidated geogenic material that
was deposited by water, wind, or ice.
- **Child of**:
  - [`geological material`](#geological-material)
  - [`object material`](#object-material)
- **Matches:**
  - <a href="https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770">https://vocabs.acdh.oeaw.ac.at/oeai-materials/concept23770</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300379424">http://vocab.getty.edu/aat/300379424</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q180184">https://www.wikidata.org/wiki/Q180184</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fc64d08c">http://vocab.terralid.org#c_fc64d08c</a>


####  unaltered material
- **Definition**: Anthropogenic material without any perceivable
impact from interaction prosesses with the (depositional) environment.
- **Child of**:
  - [`anthropogenic material`](#anthropogenic-material)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered">http://resource.geosciml.org/classifier/cgi/alterationtype/not_altered</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3a384c38">http://vocab.terralid.org#c_3a384c38</a>


####  wall rock
- **Definition**: The section of the host rock that was affected by
epigenetic processes resulting in the mineralisation.
- **Child of**:
  - [`assemblage`](#assemblage)
  - [`geological material`](#geological-material)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock">http://resource.geosciml.org/classifier/cgi/earth-resource-material-role/wall-rock</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000003">https://vocabs.dariah.eu/bbt/Concept/000003</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_25814b64">http://vocab.terralid.org#c_25814b64</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  sample state
- **Definition**: The state of the sample after analysis.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9313eed2">http://vocab.terralid.org#c_9313eed2</a>


###  material consumed
- **Definition**: Part of the sample was consumed during analysis,
e.g. by dissolving it.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** <a href="http://vocab.terralid.org#c_27d9869d">http://vocab.terralid.org#c_27d9869d</a>


###  modified
- **Definition**: The sample was modified during analysis, e.g. by
heating or partial dissolution.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b1bf2e14">http://vocab.terralid.org#c_b1bf2e14</a>


###  no material left
- **Definition**: The sample was completely consumed by the analysis.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** <a href="http://vocab.terralid.org#c_19d31994">http://vocab.terralid.org#c_19d31994</a>


###  unchanged
- **Definition**: The sample was not modified by the analysis.
- **Child of**:
  - [`sample state`](#sample-state)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b4ef9d51">http://vocab.terralid.org#c_b4ef9d51</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  sample type
- **Definition**: The type of material obtained by sampling.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000017">https://vocabs.dariah.eu/bbt/Concept/000017</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f8762e3d">http://vocab.terralid.org#c_f8762e3d</a>


###  cut
- **Definition**: The sample is cut from the object with e.g. a blade
or saw.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053069">http://vocab.getty.edu/aat/300053069</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a7cdeda3">http://vocab.terralid.org#c_a7cdeda3</a>


###  drill shavings
- **Definition**: The sample was obtained with a rotary tool and is
present in larger pieces.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://pid.geoscience.gov.au/def/voc/ga/sampletype/drill_chips_cuttings">http://pid.geoscience.gov.au/def/voc/ga/sampletype/drill_chips_cuttings</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bfd0ca9e">http://vocab.terralid.org#c_bfd0ca9e</a>


###  hand specimen fragments
- **Definition**: The object was crushed in to pieces, which were then
taken as sample. This is usually only done with larger items of
geological origin such as rocks.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://pid.geoscience.gov.au/def/voc/ga/sampletype/crush">http://pid.geoscience.gov.au/def/voc/ga/sampletype/crush</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d8e9f67e">http://vocab.terralid.org#c_d8e9f67e</a>


###  hand-picked
- **Definition**: A part of the object was crushed and the sample
manually separated after visual inspection of each fragment.
- **Child of**:
  - [`sample type`](#sample-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_26707627">http://vocab.terralid.org#c_26707627</a>


###  in-situ
- **Definition**: The analysis was carried out directly on the object
without collecting a separate sample.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300220837">http://vocab.getty.edu/aat/300220837</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q216681">https://www.wikidata.org/wiki/Q216681</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1a77d68d">http://vocab.terralid.org#c_1a77d68d</a>


###  leachate
- **Definition**: Acids or other solvents were applied to a usually
crushed part of the object to extract the sample as solution. Usually
only done with geological material.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053761">http://vocab.getty.edu/aat/300053761</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fb28d155">http://vocab.terralid.org#c_fb28d155</a>


###  loose material
- **Definition**: The object already had detached pieces, which were
collected as sample.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300117130">http://vocab.getty.edu/aat/300117130</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d57dc599">http://vocab.terralid.org#c_d57dc599</a>


###  mineral separate
- **Definition**: A part of the object was crushed and the sample
extracted based on its physical or chemical properties (e.g., density,
magnetic properties).
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://pid.geoscience.gov.au/def/voc/ga/sampletype/mineral_separate">http://pid.geoscience.gov.au/def/voc/ga/sampletype/mineral_separate</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0118bbdc">http://vocab.terralid.org#c_0118bbdc</a>


###  powder
- **Definition**: A powder was obtained during sampling or sampled
material was subsequently ground to powder.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://pid.geoscience.gov.au/def/voc/ga/sampletype/powder">http://pid.geoscience.gov.au/def/voc/ga/sampletype/powder</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300014647">http://vocab.getty.edu/aat/300014647</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2908004">https://www.wikidata.org/wiki/Q2908004</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_153bc01e">http://vocab.terralid.org#c_153bc01e</a>


###  section
- **Definition**: A larger piece of the object is cut with the aim to
create a section of it, usually for inspection with a microscope
and/or if the object is too large to fit into the analytical
instrument's sample chamber.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379391">http://vocab.getty.edu/aat/300379391</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fb91df68">http://vocab.terralid.org#c_fb91df68</a>


####  polished section
- **Definition**: The section is polished to an even surface.
- **Child of**:
  - [`section`](#section)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053867">http://vocab.getty.edu/aat/300053867</a> (relatedMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d33a496b">http://vocab.terralid.org#c_d33a496b</a>


####  thin section
- **Definition**: The section is cut and polished to a thickness that
it becomes translucent.
- **Child of**:
  - [`section`](#section)
- **Matches:**
  - <a href="http://pid.geoscience.gov.au/def/voc/ga/sampletype/polished_thin_section">http://pid.geoscience.gov.au/def/voc/ga/sampletype/polished_thin_section</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300386708">http://vocab.getty.edu/aat/300386708</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q542715">https://www.wikidata.org/wiki/Q542715</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4365b275">http://vocab.terralid.org#c_4365b275</a>


###  swabbed material
- **Definition**: Acids or other solvents are applied with a soft and
absorbent tool (e.g., Q-tip, sponge) on the object to extract the
sample as solution absorbed to the same tool and/or particles adhering
to it. Usually only carried out on archaeological materials.
- **Child of**:
  - [`sample type`](#sample-type)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300434176">http://vocab.getty.edu/aat/300434176</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_07f899ac">http://vocab.terralid.org#c_07f899ac</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  sampling method
- **Definition**: The method used to extract a sample from an object.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000023">https://vocabs.dariah.eu/bbt/Concept/000023</a> (broadMatch)
  - <a href="http://vocab.getty.edu/aat/300379429">http://vocab.getty.edu/aat/300379429</a> (relatedMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2e6c0e69">http://vocab.terralid.org#c_2e6c0e69</a>


###  ablating
- **Definition**: The removal of material with a high energy beam such
as a laser.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Alternate labels:**
  - laser ablation (sampling method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300379663">http://vocab.getty.edu/aat/300379663</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_89610abe">http://vocab.terralid.org#c_89610abe</a>


###  abrading
- **Definition**: The mechanical removal of material by applying
material with a rough surface and higher hardness than the object.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053077">http://vocab.getty.edu/aat/300053077</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q3819233">https://www.wikidata.org/wiki/Q3819233</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3cc85343">http://vocab.terralid.org#c_3cc85343</a>


###  crushing
- **Definition**: The fragmentation of a material by applying
mechanical force to it until it breals.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053084">http://vocab.getty.edu/aat/300053084</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2991605">https://www.wikidata.org/wiki/Q2991605</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9b8c9c7e">http://vocab.terralid.org#c_9b8c9c7e</a>


###  cutting
- **Definition**: The use of a blade or saw to remove a chunk from the
sample.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053069">http://vocab.getty.edu/aat/300053069</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q196751">https://www.wikidata.org/wiki/Q196751</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a5e29dda">http://vocab.terralid.org#c_a5e29dda</a>


###  dissolution
- **Definition**: The removal of material with an acid or solvent.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300380018">http://vocab.getty.edu/aat/300380018</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q3133701">https://www.wikidata.org/wiki/Q3133701</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_959163ef">http://vocab.terralid.org#c_959163ef</a>


####  etching/leaching
- **Definition**: The dissolution of specific parts of a material by
covering or submerging it in an acid or solvent. While etching only
affects the surface, leaching affects the entire sample.
- **Child of**:
  - [`dissolution`](#dissolution)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053761">http://vocab.getty.edu/aat/300053761</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300053840">http://vocab.getty.edu/aat/300053840</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_02b29aae">http://vocab.terralid.org#c_02b29aae</a>


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
  - <a href="http://vocab.getty.edu/aat/300434176">http://vocab.getty.edu/aat/300434176</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_15912994">http://vocab.terralid.org#c_15912994</a>


###  drilling
- **Definition**: The use of a rotating tool to remove material.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053151">http://vocab.getty.edu/aat/300053151</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q890886">https://www.wikidata.org/wiki/Q890886</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_961ffe7e">http://vocab.terralid.org#c_961ffe7e</a>


####  micromill
- **Definition**: A rotary tool equipped with a camera that allows
drilling on the micrometre scale in high spatial resolution.
- **Child of**:
  - [`drilling`](#drilling)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e06764b7">http://vocab.terralid.org#c_e06764b7</a>


###  fragment collection
- **Definition**: The collection of material that was already detached
from the object.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300077121">http://vocab.getty.edu/aat/300077121</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_64e8e4be">http://vocab.terralid.org#c_64e8e4be</a>


###  separation
- **Definition**: The division of material into its components
according to the components' properties.
- **Child of**:
  - [`sampling method`](#sampling-method)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300053748">http://vocab.getty.edu/aat/300053748</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q898987">https://www.wikidata.org/wiki/Q898987</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3eae3e76">http://vocab.terralid.org#c_3eae3e76</a>


####  density separation
- **Definition**: The separation process is based on the material
components' specific densities.
- **Child of**:
  - [`separation`](#separation)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300427901">http://vocab.getty.edu/aat/300427901</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5eab7b34">http://vocab.terralid.org#c_5eab7b34</a>


####  hand-picking
- **Definition**: The separation of a specific component from crushed
material by hand, usually according to its optical properties or
shape.
- **Child of**:
  - [`separation`](#separation)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f3f96906">http://vocab.terralid.org#c_f3f96906</a>


####  magnet separation
- **Definition**: The separation process is based on the material
components' magnetic properties.
- **Child of**:
  - [`separation`](#separation)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300425051">http://vocab.getty.edu/aat/300425051</a> (relatedMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_852bd94d">http://vocab.terralid.org#c_852bd94d</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  site type
- **Definition**: Set of categories to characterise the use of a site
by humans or its geological relevance.
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cad56412">http://vocab.terralid.org#c_cad56412</a>


###  anthropogenic site
- **Definition**: The site is characterised by traces of human
activity without any further specification.
- **Child of**:
  - [`site type`](#site-type)
- **Concept URI:** <a href="http://vocab.terralid.org#c_241d96ca">http://vocab.terralid.org#c_241d96ca</a>


####  artefact scatter
- **Definition**: Site with artefacts arranged on a (previous) ground
surface.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300451777">http://vocab.getty.edu/aat/300451777</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d2a764d2">http://vocab.terralid.org#c_d2a764d2</a>


####  built structures
- **Definition**: The parts of the environment that was constructed by
humans.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000018">https://vocabs.dariah.eu/bbt/Concept/000018</a> (broadMatch)
  - <a href="http://vocab.getty.edu/aat/300264550">http://vocab.getty.edu/aat/300264550</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4327d421">http://vocab.terralid.org#c_4327d421</a>


#####  building
- **Definition**: A structure built for a specific use.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300004790">http://vocab.getty.edu/aat/300004790</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q41176">https://www.wikidata.org/wiki/Q41176</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_dcd55898">http://vocab.terralid.org#c_dcd55898</a>


######  administrative structure
- **Definition**: Building or ensemble of buildings used to conduct
the management and other administrative activities of an organisation
or institution.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007049">http://vocab.getty.edu/aat/300007049</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0fcad077">http://vocab.terralid.org#c_0fcad077</a>


######  agricultural structure
- **Definition**: Building or ensemble of buildings used in
agriculture.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300004895">http://vocab.getty.edu/aat/300004895</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q10480682">https://www.wikidata.org/wiki/Q10480682</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f1d0e7f8">http://vocab.terralid.org#c_f1d0e7f8</a>


######  communal structure
- **Definition**: Building or ensemble of buildings used for communal
activities such as gatherings or cultural activities or constructed to
serve communal needs such as bathhouses.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300005120">http://vocab.getty.edu/aat/300005120</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_98f1e2ac">http://vocab.terralid.org#c_98f1e2ac</a>


######  house
- **Definition**: Building or ensemble of buildings used to provide
shelter and accommodation.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300257729">http://vocab.getty.edu/aat/300257729</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q3947">https://www.wikidata.org/wiki/Q3947</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_645bace2">http://vocab.terralid.org#c_645bace2</a>


######  military structure
- **Definition**: Building or ensemble of buildings used by military
forces.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300006887">http://vocab.getty.edu/aat/300006887</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_49d89222">http://vocab.terralid.org#c_49d89222</a>


######  religious structure
- **Definition**: Building or ensemble of buildings used for
ceremonial and ritual activities.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1370598">https://www.wikidata.org/wiki/Q1370598</a> (closeMatch)
  - <a href="http://vocab.getty.edu/aat/300263489">http://vocab.getty.edu/aat/300263489</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7b246286">http://vocab.terralid.org#c_7b246286</a>


######  workshop
- **Definition**: Building or ensemble of buildings for a specific
craft or industry.
- **Child of**:
  - [`building`](#building)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007733">http://vocab.getty.edu/aat/300007733</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q656720">https://www.wikidata.org/wiki/Q656720</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c06a2eb0">http://vocab.terralid.org#c_c06a2eb0</a>


#######  foundry
- **Definition**: Built structure used to melt and cast metal.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300266773">http://vocab.getty.edu/aat/300266773</a> (closeMatch)
  - <a href="https://www.wikidata.org/wiki/Q13883136">https://www.wikidata.org/wiki/Q13883136</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3d91691e">http://vocab.terralid.org#c_3d91691e</a>


#######  melting site
- **Definition**: Built structure used to prepare metals for the
production of items from it such as refining, alloying, melting of
scraps.
- **Child of**:
  - [`workshop`](#workshop)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f6c15b72">http://vocab.terralid.org#c_f6c15b72</a>


#######  non-metallurgical workshop
- **Definition**: Workshop unrelated to metallurgical activities.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007733">http://vocab.getty.edu/aat/300007733</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_92076176">http://vocab.terralid.org#c_92076176</a>


#######  smelting site
- **Definition**: Built structure used to produce metal from ores.
- **Child of**:
  - [`workshop`](#workshop)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300103997">http://vocab.getty.edu/aat/300103997</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ba016e0c">http://vocab.terralid.org#c_ba016e0c</a>


#####  camp
- **Definition**: A temporary settlement, usually of small size and
with non-permanent architecture.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300257104">http://vocab.getty.edu/aat/300257104</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a4821cf4">http://vocab.terralid.org#c_a4821cf4</a>


#####  infrastructure
- **Definition**: Built structure that allows the movement of goods or
people.
- **Child of**:
  - [`built structures`](#built-structures)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300386980">http://vocab.getty.edu/aat/300386980</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q121359">https://www.wikidata.org/wiki/Q121359</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3ae8c85b">http://vocab.terralid.org#c_3ae8c85b</a>


######  bridge
- **Definition**: Built structure that provides passage over a
depression or other structure.
- **Child of**:
  - [`infrastructure`](#infrastructure)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007836">http://vocab.getty.edu/aat/300007836</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q12280">https://www.wikidata.org/wiki/Q12280</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_11c6ca85">http://vocab.terralid.org#c_11c6ca85</a>


######  road
- **Definition**: Built structure that connects locations on the
ground.
- **Child of**:
  - [`infrastructure`](#infrastructure)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300007800">http://vocab.getty.edu/aat/300007800</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q34442">https://www.wikidata.org/wiki/Q34442</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3d1e781c">http://vocab.terralid.org#c_3d1e781c</a>


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
  - <a href="https://www.wikidata.org/wiki/Q486972">https://www.wikidata.org/wiki/Q486972</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300008389">http://vocab.getty.edu/aat/300008389</a> (narrowMatch)
  - <a href="http://vocab.getty.edu/aat/300008372">http://vocab.getty.edu/aat/300008372</a> (narrowMatch)
  - <a href="http://vocab.getty.edu/aat/300008375">http://vocab.getty.edu/aat/300008375</a> (narrowMatch)
  - <a href="http://vocab.getty.edu/aat/300444153">http://vocab.getty.edu/aat/300444153</a> (narrowMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c8fd0d05">http://vocab.terralid.org#c_c8fd0d05</a>


####  funerary site
- **Definition**: Site primarily used to bury deceased humans,
sometimes also animals.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** <a href="http://vocab.terralid.org#c_87b21259">http://vocab.terralid.org#c_87b21259</a>


#####  burial cave
- **Definition**: A natural opening in the earth used to bury deceased
humans, sometimes animals.
- **Child of**:
  - [`cave`](#cave)
  - [`funerary site`](#funerary-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300387008">http://vocab.getty.edu/aat/300387008</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q111340496">https://www.wikidata.org/wiki/Q111340496</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00c534fa">http://vocab.terralid.org#c_00c534fa</a>


#####  burial ground
- **Definition**: Site with burials of deceased humans, sometimes
animals.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Alternate labels:**
  - cemeteries
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300266755">http://vocab.getty.edu/aat/300266755</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_269c18b5">http://vocab.terralid.org#c_269c18b5</a>


#####  grave
- **Definition**: Feature dug into the earth without any constructed
structures to bury a deceased human, sometimes animal.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/eh_com/concepts/137492">http://purl.org/heritagedata/schemes/eh_com/concepts/137492</a> (exactMatch)
  - <a href="http://purl.org/heritagedata/schemes/eh_evd/concepts/151454">http://purl.org/heritagedata/schemes/eh_evd/concepts/151454</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300005907">http://vocab.getty.edu/aat/300005907</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q173387">https://www.wikidata.org/wiki/Q173387</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_75e7f1d3">http://vocab.terralid.org#c_75e7f1d3</a>


#####  tomb
- **Definition**: Built structure (on the ground or into the ground)
dedicated to the interment of a deceased human, sometimes animal.
- **Child of**:
  - [`funerary site`](#funerary-site)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/eh_com/concepts/138345">http://purl.org/heritagedata/schemes/eh_com/concepts/138345</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300005926">http://vocab.getty.edu/aat/300005926</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q381885">https://www.wikidata.org/wiki/Q381885</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2e5ac6fa">http://vocab.terralid.org#c_2e5ac6fa</a>


####  hearth
- **Definition**: Remains of human activities carried out to create
and maintain a controlled fire without any dedicated architectural
remains.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q585473">https://www.wikidata.org/wiki/Q585473</a> (closeMatch)
  - <a href="http://purl.org/heritagedata/schemes/eh_com/concepts/138029">http://purl.org/heritagedata/schemes/eh_com/concepts/138029</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d1e6826">http://vocab.terralid.org#c_6d1e6826</a>


####  infilling
- **Definition**: Material used to fill in a negative feature in the
ground.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300264840">http://vocab.getty.edu/aat/300264840</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q125275846">https://www.wikidata.org/wiki/Q125275846</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_536290b6">http://vocab.terralid.org#c_536290b6</a>


####  isolated feature
- **Definition**: An isolated structure assumedly originating from
human activity.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** <a href="http://vocab.terralid.org#c_99186ef5">http://vocab.terralid.org#c_99186ef5</a>


####  mine
- **Definition**: Place at which resources are extracted from the
earth through exacavation activities.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300000390">http://vocab.getty.edu/aat/300000390</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q820477">https://www.wikidata.org/wiki/Q820477</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_d6f184d2">http://vocab.terralid.org#c_d6f184d2</a>


#####  open pit mine
- **Definition**: Place at which resources are extracted open-air from
the earth through excavation activities.
- **Child of**:
  - [`mine`](#mine)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q113681824">https://www.wikidata.org/wiki/Q113681824</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300000390">http://vocab.getty.edu/aat/300000390</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_20e4e9cd">http://vocab.terralid.org#c_20e4e9cd</a>


#####  underground mine
- **Definition**: Place at which resources are extracted underground
from the earth through excavation activities.
- **Child of**:
  - [`mine`](#mine)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q4232315">https://www.wikidata.org/wiki/Q4232315</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300000390">http://vocab.getty.edu/aat/300000390</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fa1cf9f1">http://vocab.terralid.org#c_fa1cf9f1</a>


####  mining-related site
- **Definition**: Any structure related to the operation of mines or
the processing of the mine's output.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300000388">http://vocab.getty.edu/aat/300000388</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_0e020c21">http://vocab.terralid.org#c_0e020c21</a>


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
  - <a href="http://vocab.getty.edu/aat/300000821">http://vocab.getty.edu/aat/300000821</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_143dd859">http://vocab.terralid.org#c_143dd859</a>


#####  mining project
- **Definition**: An informal grouping of mineral deposits commonly
used for reporting.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/project">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/project</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a790da1a">http://vocab.terralid.org#c_a790da1a</a>


#####  mining sink-hole
- **Definition**: A depression in the ground caused by mining activity
(either open-air working or collapsed underground workings).
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Alternate labels:**
  - pinge
- **Concept URI:** <a href="http://vocab.terralid.org#c_5163843b">http://vocab.terralid.org#c_5163843b</a>


#####  ore beneficiation site
- **Definition**: Structure used to remove economically unviable parts
of the material extracted from a mine and to sort it in preparation
for smelting.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300404101">http://vocab.getty.edu/aat/300404101</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_df11f809">http://vocab.terralid.org#c_df11f809</a>


#####  slag dump
- **Definition**: Area collecting discarded material from smelting
operations.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300000832">http://vocab.getty.edu/aat/300000832</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e652be5b">http://vocab.terralid.org#c_e652be5b</a>


#####  tailing dump
- **Definition**: Area collecting discarded material from ore
beneficiation activities is collected.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1784525">https://www.wikidata.org/wiki/Q1784525</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300000832">http://vocab.getty.edu/aat/300000832</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5f810e19">http://vocab.terralid.org#c_5f810e19</a>


####  pit
- **Definition**: A negative feature dug into the ground.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300008027">http://vocab.getty.edu/aat/300008027</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1af01438">http://vocab.terralid.org#c_1af01438</a>


####  post hole
- **Definition**: A hole dug to include a timber post, usually with
its packing.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://purl.org/heritagedata/schemes/eh_com/concepts/138109">http://purl.org/heritagedata/schemes/eh_com/concepts/138109</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_16c0c950">http://vocab.terralid.org#c_16c0c950</a>


####  refuse area
- **Definition**: Areas primarily used for the collection of discarded
materials.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300000824">http://vocab.getty.edu/aat/300000824</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9bf30dd9">http://vocab.terralid.org#c_9bf30dd9</a>


#####  debris dump
- **Definition**: Area collecting discarded material from structures
such as buildings or furnaces.
- **Child of**:
  - [`refuse area`](#refuse-area)
- **Concept URI:** <a href="http://vocab.terralid.org#c_15466516">http://vocab.terralid.org#c_15466516</a>


#####  midden
- **Definition**: Area collecting refuse predominantly originating
from human occupational activities.
- **Child of**:
  - [`refuse area`](#refuse-area)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300120507">http://vocab.getty.edu/aat/300120507</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1152199">https://www.wikidata.org/wiki/Q1152199</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_475e1a3a">http://vocab.terralid.org#c_475e1a3a</a>


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
  - <a href="http://vocab.getty.edu/aat/300000821">http://vocab.getty.edu/aat/300000821</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_143dd859">http://vocab.terralid.org#c_143dd859</a>


#####  slag dump
- **Definition**: Area collecting discarded material from smelting
operations.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300000832">http://vocab.getty.edu/aat/300000832</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e652be5b">http://vocab.terralid.org#c_e652be5b</a>


#####  tailing dump
- **Definition**: Area collecting discarded material from ore
beneficiation activities is collected.
- **Child of**:
  - [`mining-related site`](#mining-related-site)
  - [`refuse area`](#refuse-area)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q1784525">https://www.wikidata.org/wiki/Q1784525</a> (exactMatch)
  - <a href="http://vocab.getty.edu/aat/300000832">http://vocab.getty.edu/aat/300000832</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_5f810e19">http://vocab.terralid.org#c_5f810e19</a>


####  single find
- **Definition**: An isolated item, seemingly unrelated to any
structure or other traces of human activity.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Matches:**
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000024">https://vocabs.dariah.eu/bbt/Concept/000024</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6d29fe63">http://vocab.terralid.org#c_6d29fe63</a>


####  storage pit
- **Definition**: A pit dug in the ground to store materials.
- **Child of**:
  - [`anthropogenic site`](#anthropogenic-site)
- **Concept URI:** <a href="http://vocab.terralid.org#c_8f51e8b9">http://vocab.terralid.org#c_8f51e8b9</a>


###  geological site
- **Definition**: The site is characterised by its geological
features.
- **Child of**:
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q10376531">https://www.wikidata.org/wiki/Q10376531</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000019">https://vocabs.dariah.eu/bbt/Concept/000019</a> (broadMatch)
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type</a> (narrowMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_823bba89">http://vocab.terralid.org#c_823bba89</a>


####  cave
- **Definition**: A natural opening in the earth large enough for
humans to explore and sometimes also to use.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300008746">http://vocab.getty.edu/aat/300008746</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q35509">https://www.wikidata.org/wiki/Q35509</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_1f2bd128">http://vocab.terralid.org#c_1f2bd128</a>


#####  burial cave
- **Definition**: A natural opening in the earth used to bury deceased
humans, sometimes animals.
- **Child of**:
  - [`cave`](#cave)
  - [`funerary site`](#funerary-site)
- **Matches:**
  - <a href="http://vocab.getty.edu/aat/300387008">http://vocab.getty.edu/aat/300387008</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q111340496">https://www.wikidata.org/wiki/Q111340496</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_00c534fa">http://vocab.terralid.org#c_00c534fa</a>


####  deposit
- **Definition**: A single body of naturally occurring and genetically
connected material with an anomalous concentration of a mineral or
rock type that has potential for human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/deposit">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/deposit</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q15104915">https://www.wikidata.org/wiki/Q15104915</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4d90feaa">http://vocab.terralid.org#c_4d90feaa</a>


####  field
- **Definition**: An area characterised by several geologically
related mineral occurrences.
- **Child of**:
  - [`geological site`](#geological-site)
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/field">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/field</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4fba9c43">http://vocab.terralid.org#c_4fba9c43</a>


####  locality
- **Definition**: An area characterised by several geologically
related mineral occurrences with potential of human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Alternate labels:**
  - mining prospect
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/prospect">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/prospect</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_b01341cd">http://vocab.terralid.org#c_b01341cd</a>


####  occurrence
- **Definition**: A single body of naturally occurring and genetically
connected material of any concentration that might have potential for
human utilisation.
- **Child of**:
  - [`geological site`](#geological-site)
- **Alternate labels:**
  - mineralisation
- **Matches:**
  - <a href="http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/occurrence">http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type/occurrence</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_177cd232">http://vocab.terralid.org#c_177cd232</a>


#####  outcrop
- **Definition**: An occurrence that is accessible on the ground.
- **Child of**:
  - [`occurrence`](#occurrence)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q531953">https://www.wikidata.org/wiki/Q531953</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_9db8b2d9">http://vocab.terralid.org#c_9db8b2d9</a>


###  unknown
- **Definition**: The information is not available.
- **Child of**:
  - [`alteration extent`](#alteration-extent)
  - [`alteration process`](#alteration-process)
  - [`authenticity`](#authenticity)
  - [`compound origin`](#compound-origin)
  - [`compound type`](#compound-type)
  - [`context type`](#context-type)
  - [`corrosion extent`](#corrosion-extent)
  - [`discovery activity`](#discovery-activity)
  - [`glass component`](#glass-component)
  - [`object material`](#object-material)
  - [`pigment component`](#pigment-component)
  - [`production context`](#production-context)
  - [`production process`](#production-process)
  - [`recycling indicator`](#recycling-indicator)
  - [`reference material`](#reference-material)
  - [`sample access`](#sample-access)
  - [`sample housing`](#sample-housing)
  - [`sample material`](#sample-material)
  - [`sample state`](#sample-state)
  - [`sample type`](#sample-type)
  - [`sampling method`](#sampling-method)
  - [`site type`](#site-type)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q24238356">https://www.wikidata.org/wiki/Q24238356</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3e4fdfbb">http://vocab.terralid.org#c_3e4fdfbb</a>



##  unit of measurement
- **Definition**: A particular quantity that was chosen as a scale for
measurements of the same dimension.
- **Matches:**
  - <a href="http://qudt.org/schema/qudt/Unit">http://qudt.org/schema/qudt/Unit</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q47574">https://www.wikidata.org/wiki/Q47574</a> (exactMatch)
  - <a href="https://vocabs.dariah.eu/bbt/Concept/000021">https://vocabs.dariah.eu/bbt/Concept/000021</a> (broadMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ac36f033">http://vocab.terralid.org#c_ac36f033</a>


###  concentration
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q3686031">https://www.wikidata.org/wiki/Q3686031</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_2f3c3933">http://vocab.terralid.org#c_2f3c3933</a>


####  %
- **Definition**: The unspecified fraction of an compound as a
fraction of 100.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q11229">https://www.wikidata.org/wiki/Q11229</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_f1f818b8">http://vocab.terralid.org#c_f1f818b8</a>


####  at%
- **Definition**: The ratio of the number of atoms of one element to
the total number of atoms, expressed as percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Concept URI:** <a href="http://vocab.terralid.org#c_69a07382">http://vocab.terralid.org#c_69a07382</a>


####  oxide%
- **Definition**: The mass fraction of an oxide, expressed as percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q110162802">https://www.wikidata.org/wiki/Q110162802</a> (closeMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_815a8de3">http://vocab.terralid.org#c_815a8de3</a>


####  wt%
- **Definition**: The mass fraction of an element expressed as
percent.
- **Child of**:
  - [`concentration`](#concentration)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q110162802">https://www.wikidata.org/wiki/Q110162802</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_bc79dc60">http://vocab.terralid.org#c_bc79dc60</a>


####  µg/g
- **Definition**: The mass of the measurant expressed as one part per
million parts.
- **Child of**:
  - [`concentration`](#concentration)
- **Alternate labels:**
  - ppm, 
  - mg/kg, 
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MicroGM-PER-GM">http://qudt.org/vocab/unit/MicroGM-PER-GM</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3b8ef5ef">http://vocab.terralid.org#c_3b8ef5ef</a>


####  µg/kg
- **Definition**: The mass of the measurant expressed as one part per
1000000000 parts.
- **Child of**:
  - [`concentration`](#concentration)
- **Alternate labels:**
  - ppb, 
  - ng/g, 
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MicroGM-PER-KiloGM">http://qudt.org/vocab/unit/MicroGM-PER-KiloGM</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_cb4c170e">http://vocab.terralid.org#c_cb4c170e</a>


###  cps
- **Definition**: The number of events registered by a detector in one
second.
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q115536343">https://www.wikidata.org/wiki/Q115536343</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ba8f4496">http://vocab.terralid.org#c_ba8f4496</a>


###  distance
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q126017">https://www.wikidata.org/wiki/Q126017</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_c83fe291">http://vocab.terralid.org#c_c83fe291</a>


####  cm
- **Definition**: One hundredth of the SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/CentiM">http://qudt.org/vocab/unit/CentiM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q174728">https://www.wikidata.org/wiki/Q174728</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_4444cd3e">http://vocab.terralid.org#c_4444cd3e</a>


####  km
- **Definition**: The SI unit of the distance multiplied by one
thousand.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/KiloM">http://qudt.org/vocab/unit/KiloM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q828224">https://www.wikidata.org/wiki/Q828224</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a099372d">http://vocab.terralid.org#c_a099372d</a>


####  m
- **Definition**: The SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/M">http://qudt.org/vocab/unit/M</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11573">https://www.wikidata.org/wiki/Q11573</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_98b8d986">http://vocab.terralid.org#c_98b8d986</a>


####  mm
- **Definition**: One thousandth of the SI unit of the distance.
- **Child of**:
  - [`distance`](#distance)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MilliM">http://qudt.org/vocab/unit/MilliM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q174789">https://www.wikidata.org/wiki/Q174789</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_50025783">http://vocab.terralid.org#c_50025783</a>


###  electric potential
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q55451">https://www.wikidata.org/wiki/Q55451</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_ded3a888">http://vocab.terralid.org#c_ded3a888</a>


####  mV
- **Definition**: One thousandth of the SI unit of the eletric
potential.
- **Child of**:
  - [`electric potential`](#electric-potential)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MilliV">http://qudt.org/vocab/unit/MilliV</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q2448803">https://www.wikidata.org/wiki/Q2448803</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_17398a30">http://vocab.terralid.org#c_17398a30</a>


####  V
- **Definition**: The SI unit of the electric potential.
- **Child of**:
  - [`electric potential`](#electric-potential)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/V">http://qudt.org/vocab/unit/V</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q25250">https://www.wikidata.org/wiki/Q25250</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e16769fb">http://vocab.terralid.org#c_e16769fb</a>


###  mass
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q11423">https://www.wikidata.org/wiki/Q11423</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7550f509">http://vocab.terralid.org#c_7550f509</a>


####  g
- **Definition**: One thousandth of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/GM">http://qudt.org/vocab/unit/GM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q41803">https://www.wikidata.org/wiki/Q41803</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_7ede7b9c">http://vocab.terralid.org#c_7ede7b9c</a>


####  kg
- **Definition**: The SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/KiloGM">http://qudt.org/vocab/unit/KiloGM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q11570">https://www.wikidata.org/wiki/Q11570</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_3739cdc8">http://vocab.terralid.org#c_3739cdc8</a>


####  mg
- **Definition**: One milllionth thousanth of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MilliGM">http://qudt.org/vocab/unit/MilliGM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q3241121">https://www.wikidata.org/wiki/Q3241121</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_e5f24560">http://vocab.terralid.org#c_e5f24560</a>


####  µg
- **Definition**: The 0.000000001-fold of the SI unit of the mass.
- **Child of**:
  - [`mass`](#mass)
- **Alternate labels:**
  - ug
- **Matches:**
  - <a href="http://qudt.org/vocab/unit/MicroGM">http://qudt.org/vocab/unit/MicroGM</a> (exactMatch)
  - <a href="https://www.wikidata.org/wiki/Q1645498">https://www.wikidata.org/wiki/Q1645498</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6fc8030c">http://vocab.terralid.org#c_6fc8030c</a>


###  time
- **Child of**:
  - [`unit of measurement`](#unit-of-measurement)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q11471">https://www.wikidata.org/wiki/Q11471</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_fd424d2e">http://vocab.terralid.org#c_fd424d2e</a>


####  a
- **Definition**: The age of an item in years.
- **Child of**:
  - [`time`](#time)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q577">https://www.wikidata.org/wiki/Q577</a> (exactMatch)
  - <a href="http://qudt.org/vocab/unit/YR">http://qudt.org/vocab/unit/YR</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_6b05ca15">http://vocab.terralid.org#c_6b05ca15</a>


####  Ma
- **Definition**: The age on an item in millions of years, i.e.
multiples of 1000000 years.
- **Child of**:
  - [`time`](#time)
- **Matches:**
  - <a href="https://www.wikidata.org/wiki/Q20764">https://www.wikidata.org/wiki/Q20764</a> (exactMatch)
  - <a href="http://qudt.org/vocab/unit/MegaYR">http://qudt.org/vocab/unit/MegaYR</a> (exactMatch)
- **Concept URI:** <a href="http://vocab.terralid.org#c_a39e16f9">http://vocab.terralid.org#c_a39e16f9</a>


