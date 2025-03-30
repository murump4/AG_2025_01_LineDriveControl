import time
import src.ZLAC8030D_API as ZLA_API

driver = ZLA_API.ZLA8030D(port="COM4", slave_address=1, baudrate=115200)
print(f"Driver temperature: {driver.driver_temperature}")
print(driver.motor_temperature)
print(f"Left motor errors: {driver.motor_errors_left}")
print(f"Right motor errors: {driver.motor_errors_right}")
print(driver.motor_status)

print(f"Motor control mode: {driver.control_mode}")
# driver.control_mode = ZLA_API.ControlMode.VELOCITY
# print(f"Motor control mode: {driver.control_mode}")

# print(f"Motor synchronous mode: {driver.sync_mode}")
# driver.sync_mode = ZLA_API.SyncMode.ASYNCHRONOUS_MODE
print(f"Motor synchronous mode: {driver.sync_mode}")

print(f"Motor direction: {driver.direction}")
# driver.direction = ZLA_API.Direction.CW
# print(f"Motor direction: {driver.direction}")

print(f"Motor speed resolution: {driver.motor_speed_resolution}")
# driver.motor_speed_resolution = ZLA_API.RPMSelector._1P2_RPM
# print(f"Motor speed resolution: {driver.motor_speed_resolution}")

# print(f"Motor parking mode: {driver.parking_mode}")
# driver.parking_mode = ZLA_API.ParkingMode.OPEN
# print(f"Motor parking mode: {driver.parking_mode}")

# print(f"Motor max speed: {driver.max_speed}")
driver.max_speed = 10
print(f"Motor max speed: {driver.max_speed}")

# Write every parameter to EEPROM
# driver.write_eeprom()

remaining_time = 3
print(f"STRT IN {remaining_time}s!")
time.sleep(remaining_time)

# print(f"Motor control word status: {driver.control_word}")
driver.control_word = ZLA_API.ControlWord.STOP
print(f"Motor control word status: {driver.control_word}")

print(f"Motor left speed: {driver.speed_left}")
# driver.speed_left = 10

