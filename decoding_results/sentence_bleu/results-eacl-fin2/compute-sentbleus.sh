#!/bin/bash


pushd sent_scores

for tlang in de fr; do
  for ts in test16 test17 test18; do
    for hyp in `find "${ts}/en-${tlang}" -name "*.gs"`; do
      echo $hyp
      sacrebleu -sl -b $hyp < ../"${ts}.${tlang}" > ${hyp}.sentbleus &
    done
  done
done
wait

popd
