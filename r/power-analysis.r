
library("pwr")
# These calculations are to determine the required sample size for the Enjoyment and Data Quality conceptual replication,
# comparing the adjective game that has been developed against an implementation of a standard (non-game)
# experimental paragidm using the same interface. This is a conceptual replication of a similar study with
# some changes in the materials and how variables are operationalised.
#
# Three hypotheses will be tested, each independent of the others and with an alpha of 0.05. The first two
# match hypotheses in the experiment that this one is replicating. The third is novel for this experiment.
# The first, that  players will experience more enjoyment in the game condition. The second, that players
# will provive poorer quality data in the game condition. Fourth, that the time per input will be greater
# in the game condition.

# The folowing values come from another pre-registered study that was very similar to this one, differing
# in that the task stopped after 20 inputs, whereas here it stops after 8 minutes. There have also been
# various changes to the experimental materials.

observedEffectSizeHyp1 <- 0.7038880393185863
observedEffectSizeHyp2 <- -0.765324535559455
observedEffectSizeTimeTaken <- 0.4841053594456612

# Enjoyment (Observed)
alt <- "greater" # We are interested in whether the game is more enjoyable than the tool/experiment version.
                 # There are reasons why the tool may be more enjoyable (eg. enjoying contributing to citizen science)
                 # But this would still just be a failure of the game to be enjoyable. Being equal or worse to the
                 # tool condition makes no difference: from both we would conclude that the game does not satisfy
                 # our definition of an 'applied game' (needs to be enjoyable) that motivates its use in our reserach.
pwr.t.test(d = observedEffectSizeHyp1, sig.level = 0.05, power = 0.8, alternative = alt)

# Enjoyment (Minimum effect size of interest)
alt <- "greater"
effectSizeOfInterest <- cohen.ES(test = "t", size = "medium")$effect.size
                 # Designing an applied game is a significant investment of effort. It is only justifiable as a
                 # methodology if it leads to a fairly substantial effect on participant motivation (which we
                 # are operationalising here as enjoyment). Less than a medium effect size would indicate that the game
                 # is not particularly useful as a replacement for a standard experimental setup. Whether it has
                 # a small, or no effect (or negative effect) makes no difference with regards to whether
                 # is is an ecologically valid example of a (practically useful) 'applied game'.
pwr.t.test(d = effectSizeOfInterest, sig.level = 0.05, power = 0.8, alternative = alt)


# Data Quality
pwr.t.test(d = observedEffectSizeHyp2, sig.level = 0.05, power = 0.8)

# Time per input (Minimum effect size of interest)
pwr.t.test(d = observedEffectSizeTimeTaken, sig.level = 0.05, power = 0.8)


# Largest sample size required is 67.95 per group. We will round this to 68 making an overall required sample
# size of 136. We will pad this up to 140 in case we have a few excluded participants due to our exclusion
# criteria.
