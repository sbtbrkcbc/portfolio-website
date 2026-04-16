#!/bin/bash

echo "🚀 Sabit Burak Cebeci - Portfolio Project Export"
echo "================================================"
echo ""

# Export klasörü oluştur
EXPORT_DIR="/tmp/portfolio_export"
rm -rf $EXPORT_DIR
mkdir -p $EXPORT_DIR

echo "📦 Dosyalar hazırlanıyor..."

# Backend kopyala
echo "  ├── Backend dosyaları..."
mkdir -p $EXPORT_DIR/backend
cp -r /app/backend/routes $EXPORT_DIR/backend/
cp -r /app/backend/models $EXPORT_DIR/backend/
cp -r /app/backend/static $EXPORT_DIR/backend/
cp /app/backend/server.py $EXPORT_DIR/backend/
cp /app/backend/generate_cv.py $EXPORT_DIR/backend/
cp /app/backend/requirements.txt $EXPORT_DIR/backend/
cp /app/backend/DejaVuSans.ttf $EXPORT_DIR/backend/
cp /app/backend/profile_photo.jpg $EXPORT_DIR/backend/
cp /app/backend/.env.example $EXPORT_DIR/backend/

# Frontend kopyala
echo "  ├── Frontend dosyaları..."
mkdir -p $EXPORT_DIR/frontend
cp -r /app/frontend/src $EXPORT_DIR/frontend/
cp -r /app/frontend/public $EXPORT_DIR/frontend/
cp /app/frontend/package.json $EXPORT_DIR/frontend/
cp /app/frontend/tailwind.config.js $EXPORT_DIR/frontend/
cp /app/frontend/postcss.config.js $EXPORT_DIR/frontend/
cp /app/frontend/craco.config.js $EXPORT_DIR/frontend/
cp /app/frontend/jsconfig.json $EXPORT_DIR/frontend/
cp /app/frontend/components.json $EXPORT_DIR/frontend/
cp /app/frontend/.env.example $EXPORT_DIR/frontend/

# README ve Documentation
echo "  ├── Dokümantasyon..."
cp /app/EXPORT_README.md $EXPORT_DIR/README.md
cp /app/VERCEL_DEPLOYMENT.md $EXPORT_DIR/
cp /app/SEO_ARCHITECTURE.md $EXPORT_DIR/ 2>/dev/null || true

# .gitignore oluştur
cat > $EXPORT_DIR/.gitignore << 'EOF'
# Dependencies
node_modules/
venv/
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment
.env
.env.local

# Build
build/
dist/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
EOF

# Git init için hazırlık
cat > $EXPORT_DIR/.gitattributes << 'EOF'
* text=auto
*.js text eol=lf
*.jsx text eol=lf
*.py text eol=lf
*.md text eol=lf
EOF

echo ""
echo "✅ Proje dosyaları hazır!"
echo ""
echo "📍 Lokasyon: $EXPORT_DIR"
echo ""
echo "📋 İçerik:"
du -sh $EXPORT_DIR/* | sort -h
echo ""
echo "📦 ZIP oluşturuluyor..."

# ZIP oluştur
cd /tmp
zip -r portfolio_export.zip portfolio_export/ -q
echo ""
echo "✅ ZIP dosyası oluşturuldu: /tmp/portfolio_export.zip"
echo "📊 Boyut: $(du -h /tmp/portfolio_export.zip | cut -f1)"
echo ""
echo "🎉 Export tamamlandı!"
echo ""
echo "📝 Sonraki adımlar:"
echo "   1. ZIP dosyasını bilgisayarınıza indirin"
echo "   2. README.md dosyasını okuyun"
echo "   3. VERCEL_DEPLOYMENT.md rehberini takip edin"
echo ""
