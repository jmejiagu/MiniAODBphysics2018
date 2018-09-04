import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'/store/group/phys_bphys/asanchez/MINIAOD/120EB174-5D92-E611-BD71-001E67E6F931.root'
    #'file:/asanchez/data/store/data/Run2016G/Charmonium/MINIAOD/23Sep2016-v1/A4B4AC67-B996-E611-9ECD-008CFAFBE8CE.root'
    #'/store/data/Run2017B/MuOnia/MINIAOD/PromptReco-v1/000/297/723/00000/9040368C-DE5E-E711-ACFF-02163E0134FF.root'
    '/store/data/Run2017B/MuOnia/MINIAOD/PromptReco-v1/000/297/047/00000/76B44962-2B56-E711-A977-02163E01A597.root'    
    #'/store/data/Run2017B/Charmonium/MINIAOD/PromptReco-v1/000/297/050/00000/183B4680-3356-E711-B33A-02163E014487.root',
    )
)

process.upkPatTrigger = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag( 'slimmedPatTrigger' ),
    triggerResults              = cms.InputTag( 'TriggerResults::HLT' ),
    unpackFilterLabels          = cms.bool( True )
)

process.demo1 = cms.EDAnalyzer("MiniAODTriggerAnalyzer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    prescales = cms.InputTag("patTrigger"),
    objects = cms.InputTag("unpackedPatTrigger")#"slimmedPatTrigger")#selectedPatTrigger"),
)

process.demo2 = cms.EDAnalyzer("PackedCandAnalyzer",
    electrons = cms.InputTag("slimmedElectrons"),
    muons = cms.InputTag("slimmedMuonsWithTrigger"), #slimmedMuons"),
    jets = cms.InputTag("slimmedJets"),
    pfCands = cms.InputTag("packedPFCandidates"),
)

process.load("myAnalyzers.JPsiKsPAT.slimmedMuonsTriggerMatcher_cfi")

process.p = cms.Path(process.slimmedMuonsWithTriggerSequence*process.demo1*process.demo2)
#process.p = cms.Path(process.slimmedMuonsWithTriggerSequence*process.demo1*process.slimmedMuonsWithTriggerSequence*process.demo2)

