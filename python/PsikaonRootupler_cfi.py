import FWCore.ParameterSet.Config as cms

rootuple = cms.EDAnalyzer('JPsiKaon',
                          #dimuons = cms.InputTag("selectedPatMuons"),
                          dimuons = cms.InputTag("slimmedMuons"),
                          #Trak = cms.InputTag("cleanPatTrackCands"),
                          Trak = cms.InputTag("packedPFCandidates"),
                          #Trak_lowpt = cms.InputTag("lostTracks"),
                          #primaryVertices = cms.InputTag("offlinePrimaryVertices"),
                          primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
                          bslabel = cms.InputTag("offlineBeamSpot"),
                          TriggerResults = cms.InputTag("TriggerResults", "", "HLT"),
                          OnlyBest = cms.bool(False),
                          isMC = cms.bool(False),
                          OnlyGen = cms.bool(False),
                          )
