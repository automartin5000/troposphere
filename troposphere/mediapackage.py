# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class EgressEndpoint(AWSProperty):
    props = {
        "PackagingConfigurationId": (str, True),
        "Url": (str, True),
    }


class Asset(AWSObject):
    resource_type = "AWS::MediaPackage::Asset"

    props = {
        "EgressEndpoints": ([EgressEndpoint], False),
        "Id": (str, True),
        "PackagingGroupId": (str, True),
        "ResourceId": (str, False),
        "SourceArn": (str, True),
        "SourceRoleArn": (str, True),
        "Tags": (Tags, False),
    }


class LogConfiguration(AWSProperty):
    props = {
        "LogGroupName": (str, False),
    }


class Channel(AWSObject):
    resource_type = "AWS::MediaPackage::Channel"

    props = {
        "Description": (str, False),
        "EgressAccessLogs": (LogConfiguration, False),
        "Id": (str, True),
        "IngressAccessLogs": (LogConfiguration, False),
        "Tags": (Tags, False),
    }


class Authorization(AWSProperty):
    props = {
        "CdnIdentifierSecret": (str, True),
        "SecretsRoleArn": (str, True),
    }


class SpekeKeyProvider(AWSProperty):
    props = {
        "RoleArn": (str, True),
        "SystemIds": ([str], True),
        "Url": (str, True),
    }


class CmafEncryption(AWSProperty):
    props = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointCmafEncryption(AWSProperty):
    props = {
        "ConstantInitializationVector": (str, False),
        "KeyRotationIntervalSeconds": (integer, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class StreamSelection(AWSProperty):
    props = {
        "MaxVideoBitsPerSecond": (integer, False),
        "MinVideoBitsPerSecond": (integer, False),
        "StreamOrder": (str, False),
    }


class HlsManifest(AWSProperty):
    props = {
        "AdMarkers": (str, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "ManifestName": (str, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "RepeatExtXKey": (boolean, False),
        "StreamSelection": (StreamSelection, False),
    }


class OriginEndpointHlsManifest(AWSProperty):
    props = {
        "AdMarkers": (str, False),
        "AdsOnDeliveryRestrictions": (str, False),
        "AdTriggers": ([str], False),
        "Id": (str, True),
        "IncludeIframeOnlyStream": (boolean, False),
        "ManifestName": (str, False),
        "PlaylistType": (str, False),
        "PlaylistWindowSeconds": (integer, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "Url": (str, False),
    }


class CmafPackage(AWSProperty):
    props = {
        "Encryption": (CmafEncryption, False),
        "HlsManifests": ([HlsManifest], True),
        "IncludeEncoderConfigurationInSegments": (boolean, False),
        "SegmentDurationSeconds": (integer, False),
    }


class DashEncryption(AWSProperty):
    props = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointDashEncryption(AWSProperty):
    props = {
        "KeyRotationIntervalSeconds": (integer, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class DashManifest(AWSProperty):
    props = {
        "ManifestLayout": (str, False),
        "ManifestName": (str, False),
        "MinBufferTimeSeconds": (integer, False),
        "Profile": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class DashPackage(AWSProperty):
    props = {
        "DashManifests": ([DashManifest], True),
        "Encryption": (DashEncryption, False),
        "PeriodTriggers": ([str], False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentTemplateFormat": (str, False),
    }


class HlsEncryption(AWSProperty):
    props = {
        "ConstantInitializationVector": (str, False),
        "EncryptionMethod": (str, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class OriginEndpointHlsEncryption(AWSProperty):
    props = {
        "ConstantInitializationVector": (str, False),
        "EncryptionMethod": (str, False),
        "KeyRotationIntervalSeconds": (integer, False),
        "RepeatExtXKey": (boolean, False),
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class HlsPackage(AWSProperty):
    props = {
        "Encryption": (HlsEncryption, False),
        "HlsManifests": ([HlsManifest], True),
        "SegmentDurationSeconds": (integer, False),
        "UseAudioRenditionGroup": (boolean, False),
    }


class MssEncryption(AWSProperty):
    props = {
        "SpekeKeyProvider": (SpekeKeyProvider, True),
    }


class MssManifest(AWSProperty):
    props = {
        "ManifestName": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class MssPackage(AWSProperty):
    props = {
        "Encryption": (MssEncryption, False),
        "MssManifests": ([MssManifest], True),
        "SegmentDurationSeconds": (integer, False),
    }


class OriginEndpointMssPackage(AWSProperty):
    props = {
        "Encryption": (MssEncryption, False),
        "ManifestWindowSeconds": (integer, False),
        "SegmentDurationSeconds": (integer, False),
        "StreamSelection": (StreamSelection, False),
    }


class OriginEndpointHlsPackage(AWSProperty):
    props = {
        "AdMarkers": (str, False),
        "AdsOnDeliveryRestrictions": (str, False),
        "AdTriggers": ([str], False),
        "Encryption": (OriginEndpointHlsEncryption, False),
        "IncludeIframeOnlyStream": (boolean, False),
        "PlaylistType": (str, False),
        "PlaylistWindowSeconds": (integer, False),
        "ProgramDateTimeIntervalSeconds": (integer, False),
        "SegmentDurationSeconds": (integer, False),
        "StreamSelection": (StreamSelection, False),
        "UseAudioRenditionGroup": (boolean, False),
    }


class OriginEndpointDashPackage(AWSProperty):
    props = {
        "AdsOnDeliveryRestrictions": (str, False),
        "AdTriggers": ([str], False),
        "Encryption": (OriginEndpointDashEncryption, False),
        "ManifestLayout": (str, False),
        "ManifestWindowSeconds": (integer, False),
        "MinBufferTimeSeconds": (integer, False),
        "MinUpdatePeriodSeconds": (integer, False),
        "PeriodTriggers": ([str], False),
        "Profile": (integer, False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentTemplateFormat": (str, False),
        "StreamSelection": (StreamSelection, False),
        "SuggestedPresentationDelaySeconds": (integer, False),
        "UtcTiming": (str, False),
        "UtcTimingUri": (str, False),
    }


class OriginEndpointCmafPackage(AWSProperty):
    props = {
        "Encryption": (OriginEndpointCmafEncryption, False),
        "HlsManifests": ([OriginEndpointHlsManifest], False),
        "SegmentDurationSeconds": (integer, False),
        "SegmentPrefix": (str, False),
        "StreamSelection": (StreamSelection, False),
    }


class OriginEndpoint(AWSObject):
    resource_type = "AWS::MediaPackage::OriginEndpoint"

    props = {
        "Authorization": (Authorization, False),
        "ChannelId": (str, True),
        "CmafPackage": (OriginEndpointCmafPackage, False),
        "DashPackage": (OriginEndpointDashPackage, False),
        "Description": (str, False),
        "HlsPackage": (OriginEndpointHlsPackage, False),
        "Id": (str, True),
        "ManifestName": (str, False),
        "MssPackage": (OriginEndpointMssPackage, False),
        "Origination": (str, False),
        "StartoverWindowSeconds": (integer, False),
        "Tags": (Tags, False),
        "TimeDelaySeconds": (integer, False),
        "Whitelist": ([str], False),
    }


class PackagingConfiguration(AWSObject):
    resource_type = "AWS::MediaPackage::PackagingConfiguration"

    props = {
        "CmafPackage": (CmafPackage, False),
        "DashPackage": (DashPackage, False),
        "HlsPackage": (HlsPackage, False),
        "Id": (str, True),
        "MssPackage": (MssPackage, False),
        "PackagingGroupId": (str, True),
        "Tags": (Tags, False),
    }


class PackagingGroup(AWSObject):
    resource_type = "AWS::MediaPackage::PackagingGroup"

    props = {
        "Authorization": (Authorization, False),
        "EgressAccessLogs": (LogConfiguration, False),
        "Id": (str, True),
        "Tags": (Tags, False),
    }
