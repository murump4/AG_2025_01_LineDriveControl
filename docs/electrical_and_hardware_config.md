[AG/2025/01 Linear Drive Control](../README.md)
===

# [Electrical and Hardware configuration](/docs/electrical_and_hardware_config.md)

## System components

- ZLTech ZLAC8030D Servo driver
  - ModbusRTU protoccol __SELECTED__ for the project
  - CAN protocol
  - 2 motor sync and async driver
- ZLTech ZLLG16ASM800 v2.0
- Raspberry Pi Zero:
  - ModbusRTU HAT
  - ADC input HAT
  - Feedback LED-s
  - RTC
  - Debug UART
- Power Supply for Raspberry Pi
- MicroUSB to Ethernet adapter for debug and config
- Joystick
- Emergency STOP input handling
  - Software based
  - Electrical