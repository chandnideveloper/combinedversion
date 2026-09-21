#!/usr/bin/env bash
set -e

echo "=================================================================="
echo " Pushing all updated code to GitHub remotes"
echo "=================================================================="

pushd "az-qlikengine-api-repo" && git push origin main && popd
pushd "unified-parsing" && git push origin main && popd
pushd "mapping (2)/mapping" && git push origin main && popd
pushd "az-wa-repo-generationagent" && git push origin main && popd
pushd "unified-semantic-kernel" && git push origin main && popd
pushd "az-repo-mongodb-vl" && git push origin main && popd
pushd "vl-t2f-tableu-base-api" && git push origin main && popd
pushd "vl-t2f-mongo-db" && git push origin master && popd

echo "=================================================================="
echo " All repositories pushed successfully!"
echo "=================================================================="
