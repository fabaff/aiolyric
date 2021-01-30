"""
Class object for LyricDevice
Documentation: https://github.com/timmo001/aiolyric

Generated by generator/generator.py - 2020-08-31 14:06:02.854691
"""
from .base import LyricBase, LyricBaseClient


class Vacationhold(LyricBase):
    @property
    def enabled(self):
        return self.attributes.get("enabled", False)


class Currentscheduleperiod(LyricBase):
    @property
    def day(self):
        return self.attributes.get("day", None)

    @property
    def period(self):
        return self.attributes.get("period", None)


class Schedulecapabilities(LyricBase):
    @property
    def availableScheduleTypes(self):
        return self.attributes.get("availableScheduleTypes", [])

    @property
    def schedulableFan(self):
        return self.attributes.get("schedulableFan", False)


class Scheduletype(LyricBase):
    @property
    def scheduleType(self):
        return self.attributes.get("scheduleType", None)

    @property
    def scheduleSubType(self):
        return self.attributes.get("scheduleSubType", None)


class SettingsHardwaresettings(LyricBase):
    @property
    def brightness(self):
        return self.attributes.get("brightness", None)

    @property
    def maxBrightness(self):
        return self.attributes.get("maxBrightness", None)


class SettingsTemperaturemode(LyricBase):
    @property
    def air(self):
        return self.attributes.get("air", True)


class SettingsSpecialmode(LyricBase):
    @property
    def _(self):
        return None


class Settings(LyricBase):
    @property
    def hardwareSettings(self):
        return SettingsHardwaresettings(self.attributes.get("hardwareSettings", {}))

    @property
    def temperatureMode(self):
        return SettingsTemperaturemode(self.attributes.get("temperatureMode", {}))

    @property
    def specialMode(self):
        return SettingsSpecialmode(self.attributes.get("specialMode", {}))

    @property
    def devicePairingEnabled(self):
        return self.attributes.get("devicePairingEnabled", True)


class Devicesettings(LyricBase):
    @property
    def _(self):
        return None


class Service(LyricBase):
    @property
    def mode(self):
        return self.attributes.get("mode", None)


class Changeablevalues(LyricBase):
    @property
    def autoChangeoverActive(self):
        return self.attributes.get("autoChangeoverActive", None)

    @property
    def mode(self):
        return self.attributes.get("mode", None)

    @property
    def heatSetpoint(self):
        return self.attributes.get("heatSetpoint", None)

    @property
    def coolSetpoint(self):
        return self.attributes.get("coolSetpoint", None)

    @property
    def thermostatSetpointStatus(self):
        return self.attributes.get("thermostatSetpointStatus", None)

    @property
    def nextPeriodTime(self):
        return self.attributes.get("nextPeriodTime", None)

    @property
    def heatCoolMode(self):
        return self.attributes.get("heatCoolMode", None)

    @property
    def endHeatSetpoint(self):
        return self.attributes.get("endHeatSetpoint", None)

    @property
    def endCoolSetpoint(self):
        return self.attributes.get("endCoolSetpoint", None)


class Operationstatus(LyricBase):
    @property
    def mode(self):
        return self.attributes.get("mode", None)

    @property
    def fanRequest(self):
        return self.attributes.get("fanRequest", False)

    @property
    def circulationFanRequest(self):
        return self.attributes.get("circulationFanRequest", False)


class LyricDevice(LyricBaseClient):
    @property
    def locationID(self):
        return self.attributes.get("locationID", None)

    @property
    def displayedOutdoorHumidity(self):
        return self.attributes.get("displayedOutdoorHumidity", None)

    @property
    def vacationHold(self):
        return Vacationhold(self.attributes.get("vacationHold", {}))

    @property
    def currentSchedulePeriod(self):
        return Currentscheduleperiod(self.attributes.get("currentSchedulePeriod", {}))

    @property
    def scheduleCapabilities(self):
        return Schedulecapabilities(self.attributes.get("scheduleCapabilities", {}))

    @property
    def scheduleType(self):
        return Scheduletype(self.attributes.get("scheduleType", {}))

    @property
    def scheduleStatus(self):
        return self.attributes.get("scheduleStatus", None)

    @property
    def allowedTimeIncrements(self):
        return self.attributes.get("allowedTimeIncrements", None)

    @property
    def settings(self):
        return Settings(self.attributes.get("settings", {}))

    @property
    def deviceClass(self):
        return self.attributes.get("deviceClass", None)

    @property
    def deviceType(self):
        return self.attributes.get("deviceType", None)

    @property
    def deviceID(self):
        return self.attributes.get("deviceID", None)

    @property
    def name(self):
        return self.attributes.get("name", None)

    @property
    def isAlive(self):
        return self.attributes.get("isAlive", True)

    @property
    def isUpgrading(self):
        return self.attributes.get("isUpgrading", False)

    @property
    def isProvisioned(self):
        return self.attributes.get("isProvisioned", True)

    @property
    def macID(self):
        return self.attributes.get("macID", None)

    @property
    def deviceSettings(self):
        return Devicesettings(self.attributes.get("deviceSettings", {}))

    @property
    def service(self):
        return Service(self.attributes.get("service", {}))

    @property
    def deviceRegistrationDate(self):
        return self.attributes.get("deviceRegistrationDate", None)

    @property
    def dataSyncStatus(self):
        return self.attributes.get("dataSyncStatus", None)

    @property
    def units(self):
        return self.attributes.get("units", None)

    @property
    def indoorTemperature(self):
        return self.attributes.get("indoorTemperature", None)

    @property
    def outdoorTemperature(self):
        return self.attributes.get("outdoorTemperature", None)

    @property
    def allowedModes(self):
        return self.attributes.get("allowedModes", [])

    @property
    def deadband(self):
        return self.attributes.get("deadband", None)

    @property
    def hasDualSetpointStatus(self):
        return self.attributes.get("hasDualSetpointStatus", False)

    @property
    def minHeatSetpoint(self):
        return self.attributes.get("minHeatSetpoint", None)

    @property
    def maxHeatSetpoint(self):
        return self.attributes.get("maxHeatSetpoint", None)

    @property
    def minCoolSetpoint(self):
        return self.attributes.get("minCoolSetpoint", None)

    @property
    def maxCoolSetpoint(self):
        return self.attributes.get("maxCoolSetpoint", None)

    @property
    def changeableValues(self):
        return Changeablevalues(self.attributes.get("changeableValues", {}))

    @property
    def operationStatus(self):
        return Operationstatus(self.attributes.get("operationStatus", {}))

    @property
    def deviceModel(self):
        return self.attributes.get("deviceModel", None)
