#!/usr/bin/env bash
set -euo pipefail

APP_NAME="symlink-generator-3d"
INSTALL_DIR="${HOME}/.local/share/${APP_NAME}"
BIN_DIR="${HOME}/.local/bin"
LAUNCHER="${BIN_DIR}/${APP_NAME}"

mkdir -p "${INSTALL_DIR}" "${BIN_DIR}"

cp "gui_symlink_generator.py" "${INSTALL_DIR}/gui_symlink_generator.py"
chmod 755 "${INSTALL_DIR}/gui_symlink_generator.py"

cat > "${LAUNCHER}" <<EOF
#!/usr/bin/env bash
exec python3 "${INSTALL_DIR}/gui_symlink_generator.py" "\$@"
EOF
chmod 755 "${LAUNCHER}"

echo "Installed ${APP_NAME}."
echo "Launcher: ${LAUNCHER}"
echo
if [[ ":${PATH}:" != *":${BIN_DIR}:"* ]]; then
  echo "Add ${BIN_DIR} to your PATH to run '${APP_NAME}' from any terminal:"
  echo "  export PATH=\"${BIN_DIR}:\$PATH\""
else
  echo "Run with: ${APP_NAME}"
fi
