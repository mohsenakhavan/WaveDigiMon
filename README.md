<div id="english">

# 🎯 WaveDigiMon: Sound Wave Digitization Monitor

## 🔊 Scientific Background: Sound to Digital Conversion

### Sound Wave Physics
Sound waves are pressure variations that travel through a medium (typically air). These mechanical waves have several key properties:
- **Amplitude**: The magnitude of pressure variation
- **Frequency**: Number of pressure variations per second (measured in Hz)
- **Wavelength**: Physical distance between wave peaks

### Conversion Process
1. **Acoustic to Electric (Transduction)**
   - Sound waves strike the microphone's diaphragm
   - Mechanical energy converts to electrical signals through:
     * Dynamic microphones: Moving coil generates voltage
     * Condenser microphones: Capacitance variations create voltage changes
   - Result: Continuous analog electrical signal

2. **Analog to Digital Conversion (ADC)**
   - **Sampling**: 
     * Signal measured at fixed time intervals (10Hz in this project)
     * Following Nyquist Theorem: Sample rate must be > 2× highest frequency
   - **Quantization**:
     * Continuous voltage values mapped to discrete levels
     * 10-bit resolution = 1024 possible values (0-1023)
     * Quantization error introduced but minimized by high resolution
   - **Encoding**:
     * Digital values converted to binary format
     * Data transmitted via serial communication

## Project Images

| Hardware Setup | Monitoring Interface |
|:-------------:|:-------------------:|
| ![Hardware Configuration](https://github.com/user-attachments/assets/d6763fde-98e9-40dd-8fa6-4b4719cc4a43) | ![Monitoring Dashboard](https://github.com/user-attachments/assets/4df0d1cf-a233-408a-967d-e27f16d042ae) |
| *Arduino setup with sound sensor and connections* | *Real-time sound visualization dashboard* |

## 🚀 Setup and Installation

### Hardware Requirements
- Arduino board (Uno or similar)
- Sound sensor module
- USB cable
- Breadboard and jumper wires

### Hardware Setup
1. Connect sound sensor to Arduino:
   - VCC → 5V
   - GND → GND
   - OUT → A0 (Analog input)

### Software Requirements
- Arduino IDE
- Python 3.x
- Required Python packages:
  ```bash
  pip install pyserial matplotlib tkinter
  ```

### Running the Project
1. **Arduino Setup**:
   - Open Arduino IDE
   - Load `arduino.ino`
   - Select correct board and port
   - Upload sketch

2. **Python Setup**:
   - Modify `SERIAL_PORT` in `main.py` to match your Arduino port
   - Run the Python script:
     ```bash
     python main.py
     ```

3. **Verification**:
   - Terminal window shows raw values
   - Graph window displays real-time visualization
   - Expected value range: 0-1023

## 🔧 Troubleshooting
- **No Serial Connection**: Check port name and permissions
- **No Data**: Verify sensor connections
- **Erratic Readings**: Check power supply stability

</div>

---

<div id="persian" dir="rtl">

# 🎯 موج‌نما: سیستم مانیتورینگ دیجیتال صدا

## 🔊 پایه علمی: تبدیل صدا به دیجیتال

### فیزیک امواج صوتی
امواج صوتی تغییرات فشار هستند که از طریق یک محیط (معمولاً هوا) منتقل می‌شوند. این امواج مکانیکی دارای چند ویژگی کلیدی هستند:
- **دامنه**: بزرگی تغییرات فشار
- **فرکانس**: تعداد تغییرات فشار در ثانیه (اندازه‌گیری شده در هرتز)
- **طول موج**: فاصله فیزیکی بین قله‌های موج

### فرآیند تبدیل
1. **تبدیل صوتی به الکتریکی (ترنسداکشن)**
   - امواج صوتی به دیافراگم میکروفون برخورد می‌کنند
   - انرژی مکانیکی از طریق روش‌های زیر به سیگنال‌های الکتریکی تبدیل می‌شود:
     * میکروفون‌های داینامیک: سیم‌پیچ متحرک ولتاژ تولید می‌کند
     * میکروفون‌های خازنی: تغییرات ظرفیت خازنی تغییرات ولتاژ ایجاد می‌کند
   - نتیجه: سیگنال الکتریکی آنالوگ پیوسته

2. **تبدیل آنالوگ به دیجیتال (ADC)**
   - **نمونه‌برداری**: 
     * سیگنال در فواصل زمانی ثابت اندازه‌گیری می‌شود (۱۰ هرتز در این پروژه)
     * طبق قضیه نایکوئیست: نرخ نمونه‌برداری باید بیش از ۲ برابر بالاترین فرکانس باشد
   - **کوانتیزاسیون**:
     * مقادیر ولتاژ پیوسته به سطوح گسسته نگاشت می‌شوند
     * رزولوشن ۱۰ بیت = ۱۰۲۴ مقدار ممکن (۰-۱۰۲۳)
     * خطای کوانتیزاسیون معرفی می‌شود اما با رزولوشن بالا به حداقل می‌رسد
   - **کدگذاری**:
     * مقادیر دیجیتال به فرمت باینری تبدیل می‌شوند
     * داده‌ها از طریق ارتباط سریال منتقل می‌شوند

## 🚀 نصب و راه‌اندازی

### نیازمندی‌های سخت‌افزاری
- برد آردوینو (اونو یا مشابه)
- ماژول سنسور صدا
- کابل USB
- بردبورد و سیم‌های رابط

### راه‌اندازی سخت‌افزار
1. اتصال سنسور صدا به آردوینو:
   - VCC به ۵ ولت
   - GND به GND
   - OUT به A0 (ورودی آنالوگ)

### نیازمندی‌های نرم‌افزاری
- Arduino IDE
- Python 3.x
- پکیج‌های مورد نیاز پایتون:
  ```bash
  pip install pyserial matplotlib tkinter
  ```

### اجرای پروژه
1. **راه‌اندازی آردوینو**:
   - Arduino IDE را باز کنید
   - فایل `arduino.ino` را بارگذاری کنید
   - برد و پورت صحیح را انتخاب کنید
   - اسکچ را آپلود کنید

2. **راه‌اندازی پایتون**:
   - `SERIAL_PORT` در `main.py` را متناسب با پورت آردوینو خود تغییر دهید
   - اسکریپت پایتون را اجرا کنید:
     ```bash
     python main.py
     ```

3. **تأیید عملکرد**:
   - پنجره ترمینال مقادیر خام را نشان می‌دهد
   - پنجره نمودار تجسم بلادرنگ را نمایش می‌دهد
   - محدوده مورد انتظار مقادیر: ۰-۱۰۲۳

## 🔧 عیب‌یابی
- **عدم اتصال سریال**: نام پورت و مجوزها را بررسی کنید
- **عدم دریافت داده**: اتصالات سنسور را بررسی کنید
- **خوانش‌های نامنظم**: پایداری منبع تغذیه را بررسی کنید
---
