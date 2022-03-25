# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.7.6, generator: @autorest/python@5.14.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class accessFlags(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    READ = "Read"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REMOTE = "Remote"
    EXECUTE = "Execute"
    ADMIN = "Admin"
    SUPERADMIN = "SuperAdmin"

class actionSettingType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    PASSWORD = "Password"

class actionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNINITIALIZED = "Uninitialized"
    READY = "Ready"
    RUNNING = "Running"
    WAITING = "Waiting"
    FINISHED = "Finished"

class enrollmentType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNINITIALIZED = "Uninitialized"
    ADDMEMBERSHIP = "AddMembership"
    ACTIVATEUSERCREDENTIAL = "ActivateUserCredential"
    ENROLLEPHEMERALCONTAINER = "EnrollEphemeralContainer"
    ENROLLPERSISTENTRUNNER = "EnrollPersistentRunner"
    ENROLLCLOUDWORKER = "EnrollCloudWorker"
    ENROLLPERSISTENTCLOUD = "EnrollPersistentCloud"

class enum6(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    AGNOSTIC = "Agnostic"
    CLOUD = "Cloud"
    WINDOWS64 = "Windows64"
    WINDOWS32 = "Windows32"
    LINUX64 = "Linux64"
    LINUX32 = "Linux32"
    MACOS = "MacOS"
    ANDROID = "Android"
    IOS = "iOS"

class filterDataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    STRING = "String"
    INTEGER = "Integer"
    BOOLEAN = "Boolean"
    TIMESTAMP = "Timestamp"

class jobScheduleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    RUNNOW = "RunNow"
    RUNONCE = "RunOnce"
    RUNEVERY = "RunEvery"

class jobThreadState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNINITIALIZED = "Uninitialized"
    NOTSTARTED = "NotStarted"
    RUNNING = "Running"
    WAITING = "Waiting"
    FINISHED = "Finished"

class nodeAffinity(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    EPHEMERALCONTAINER = "EphemeralContainer"
    PERSISTENTRUNNER = "PersistentRunner"
    CLOUDWORKER = "CloudWorker"
    PERSISTENTCLOUD = "PersistentCloud"
    UTILITY = "Utility"
    KUBEMASTERAGENTLESS = "KubeMasterAgentless"

class nodeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NOTENROLLED = "NotEnrolled"
    ENROLLED = "Enrolled"

class platform(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    AGNOSTIC = "Agnostic"
    CLOUD = "Cloud"
    WINDOWS64 = "Windows64"
    WINDOWS32 = "Windows32"
    LINUX64 = "Linux64"
    LINUX32 = "Linux32"
    MACOS = "MacOS"
    ANDROID = "Android"
    IOS = "iOS"

class repositoryLicense(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    FREE = "Free"
    PAID = "Paid"

class repositoryScope(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    PRIVATE = "Private"
    PUBLIC = "Public"

class runLocation(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNINITIALIZED = "Uninitialized"
    RUNONPRODIGALOBJECT = "RunOnProdigalObject"
    RUNONGENERICPOOL = "RunOnGenericPool"
    RUNONSPECIFICOBJECT = "RunOnSpecificObject"
    RUNONDEDICATEDSERVICE = "RunOnDedicatedService"
    RUNONCONNECTION = "RunOnConnection"

class sortDirection(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ASCENDING = "Ascending"
    DESCENDING = "Descending"

class stepResult(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNINITIALIZED = "Uninitialized"
    SUCCESS = "Success"
    FAILURE = "Failure"
