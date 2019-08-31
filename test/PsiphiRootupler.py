import FWCore.ParameterSet.Config as cms
process = cms.Process("Rootuple")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data')
#process.GlobalTag = GlobalTag(process.GlobalTag, '94X_dataRun2_ReReco_EOY17_v1', '')

process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(2000))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

##MiniAOD
#'/store/data/Run2018C/Charmonium/MINIAOD/PromptReco-v2/000/319/756/00000/EEF6CEC1-698B-E811-8081-02163E00AF5F.root',
## RE-REco
#'/store/data/Run2018C/Charmonium/MINIAOD/17Sep2018-v1/60000/FF015DDD-854C-FA4B-9E21-36DEAD0A0B0E.root',

##MiniAOD MC 2018
#'/store/mc/RunIIAutumn18MiniAOD/BsToPsiPhi_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/70000/FF529DEB-C5A7-2B43-A966-08F081AC7A29.root',

'file:/afs/cern.ch/user/j/jmejiagu/public/miniAODmuonexample/CMSSW_10_2_9/src/E22382D6-8607-9A41-8E9F-8A49F1CBB4FA.root',
        
 )
)

process.triggerSelection = cms.EDFilter("TriggerResultsFilter",
                                        triggerConditions = cms.vstring('HLT_Dimuon20_Jpsi_Barrel_Seagulls_v*',
                                                                        'HLT_Dimuon25_Jpsi_v*',
                                                                        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v*',
                                                                        'HLT_DoubleMu4_JpsiTrk_Displaced_v*',
                                                                        'HLT_DoubleMu4_Jpsi_Displaced_v*'                                   
                                                                       ),
                                        hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
                                        l1tResults = cms.InputTag( "" ),
                                        throw = cms.bool(False)
                                        )

process.load("myAnalyzers.JPsiKsPAT.PsiphiRootupler_cfi")
process.rootuple.isMC = cms.bool(True) 
process.rootuple.GenParticles = cms.InputTag("prunedGenParticles") 

process.TFileService = cms.Service("TFileService",
#        fileName = cms.string('Rootuple_BstoJpsiphi_2018_MiniAOD.root'),
         fileName = cms.string('Rootuple_BstoJpsiphi_MC2018_MiniAOD.root'),                                  
)


process.mySequence = cms.Sequence(
                                   process.triggerSelection *
                                   process.rootuple
				   )
#process.p = cms.Path(process.mySequence)

#process.p = cms.Path(process.triggerSelection*process.rootuple)
process.p = cms.Path(process.rootuple)




