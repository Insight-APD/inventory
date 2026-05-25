# Offline Inventory System

Оффлайн-система складского учета и эксплуатации оборудования.

## Возможности

- Android + Windows
- Работа по LAN
- SQLite
- QR-коды
- XLSX экспорт
- Backup / Restore
- PDF/URL инструкции
- PWA + APK

## Запуск backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Запуск frontend

```bash
cd frontend
npm install
npm run dev
```

## Сборка APK

```bash
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init
npm run build
npx cap add android
npx cap sync
npx cap open android
```

Далее в Android Studio:
Build → Build APK