[AG/2025/01 Linear Drive Control](../README.md)
===

# [Work Diary](/docs/work_diary.md)

## Time logs

| Date          | Start time    | End time  | Note                                                      |
| ---           | ---           | ---       | ---                                                       |
| 2025.03.29    | 11:00         | 13:35     | Initialize and plan project, RegAddresses recorded        |
| 2025.03.30    | 11:23         | 14:55     | Status requests implemented and tested                    |
| 2025.03.30    | 17:00         | 19:04     | Default commands implemented, configuration tests         |

- A két motor hajtható szinkronban? Mi van ha az egyik elakad, a másik menne???
    - Doksit át kell böngészni!
    - Ezt meg kell nézni a valóságban is!
- A kerekek 200kg terhelésre vannak tervezve párosával. El fog tudni vinni ekkora tömeget?
- Velocity vagy torque mód tesztelése, mindkettő szóba jöhet.
    - Elsőre velocity-vel fogunk próbálkozni, a joystick sebességet fog szabályozni.
    - A nagy terhelés miatt azonban lehet érdemes megvizsgálni majd a torque módot!

# Required to finish:

- 5Ohm 100W Regen ellenállás
- Feedback LED-ek
- RS485 HAT (UART - AX HAT lehet oké ide!)
- AN input HAT (I2C)
- RTC HAT

# To Do

- 2h Project implementation and documentation read
- 3h Servo driver init function implementation
- 2h Servo driver status read function implementation (With automatic warning in case of error!)
- 8h Servo driver velocity control function implementation
- 2h Demo environment implementation to test servo driver (CMD)
- 1h Joystick Analog input implementation (debug analog input via I2C)
- 3h LED feedback control process (timed flashing based on the status)
    - 2db Overload Left - Right
    - 2db Overtemperature Left - Right
    - 2db Error Left - Right
    - 2db Error driver
    - 2db Overtemperature driver
    - 1db Servo Enable
    - 1db Communication error
    - 1db Heartbeat

