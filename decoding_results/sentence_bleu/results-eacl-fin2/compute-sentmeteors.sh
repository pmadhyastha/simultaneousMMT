#!/bin/bash


pushd sent_scores

for tlang in de fr; do
  for ts in test16 test17 test18; do
    for hyp in `find "${ts}/en-${tlang}" -name "*.gs"`; do
      echo $hyp
      java -jar /data/ozan/tools/multeval/lib/meteor-1.5.jar ${hyp} "../${ts}.${tlang}" -l ${tlang} &> ${hyp}.sentmeteors &
    done
    wait
  done
done
wait

popd
