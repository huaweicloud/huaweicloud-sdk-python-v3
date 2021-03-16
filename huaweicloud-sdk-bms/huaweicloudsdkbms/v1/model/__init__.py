# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkbms.v1.model.absolute import Absolute
from huaweicloudsdkbms.v1.model.address import Address
from huaweicloudsdkbms.v1.model.address_info import AddressInfo
from huaweicloudsdkbms.v1.model.addresses import Addresses
from huaweicloudsdkbms.v1.model.attach_baremetal_server_volume_request import AttachBaremetalServerVolumeRequest
from huaweicloudsdkbms.v1.model.attach_baremetal_server_volume_response import AttachBaremetalServerVolumeResponse
from huaweicloudsdkbms.v1.model.attach_volume_body import AttachVolumeBody
from huaweicloudsdkbms.v1.model.band_width import BandWidth
from huaweicloudsdkbms.v1.model.batch_reboot_baremetal_servers_request import BatchRebootBaremetalServersRequest
from huaweicloudsdkbms.v1.model.batch_reboot_baremetal_servers_response import BatchRebootBaremetalServersResponse
from huaweicloudsdkbms.v1.model.batch_start_baremetal_servers_request import BatchStartBaremetalServersRequest
from huaweicloudsdkbms.v1.model.batch_start_baremetal_servers_response import BatchStartBaremetalServersResponse
from huaweicloudsdkbms.v1.model.batch_stop_baremetal_servers_request import BatchStopBaremetalServersRequest
from huaweicloudsdkbms.v1.model.batch_stop_baremetal_servers_response import BatchStopBaremetalServersResponse
from huaweicloudsdkbms.v1.model.change_baremetal_name_body import ChangeBaremetalNameBody
from huaweicloudsdkbms.v1.model.change_baremetal_name_responses_servers import ChangeBaremetalNameResponsesServers
from huaweicloudsdkbms.v1.model.change_baremetal_name_server import ChangeBaremetalNameServer
from huaweicloudsdkbms.v1.model.change_baremetal_server_name_request import ChangeBaremetalServerNameRequest
from huaweicloudsdkbms.v1.model.change_baremetal_server_name_response import ChangeBaremetalServerNameResponse
from huaweicloudsdkbms.v1.model.create_bare_metal_servers_request import CreateBareMetalServersRequest
from huaweicloudsdkbms.v1.model.create_bare_metal_servers_response import CreateBareMetalServersResponse
from huaweicloudsdkbms.v1.model.create_baremetal_servers_body import CreateBaremetalServersBody
from huaweicloudsdkbms.v1.model.create_scheduler_hints import CreateSchedulerHints
from huaweicloudsdkbms.v1.model.create_servers import CreateServers
from huaweicloudsdkbms.v1.model.data_volumes import DataVolumes
from huaweicloudsdkbms.v1.model.delete_windows_bare_metal_server_password_request import DeleteWindowsBareMetalServerPasswordRequest
from huaweicloudsdkbms.v1.model.delete_windows_bare_metal_server_password_response import DeleteWindowsBareMetalServerPasswordResponse
from huaweicloudsdkbms.v1.model.detach_baremetal_server_volume_request import DetachBaremetalServerVolumeRequest
from huaweicloudsdkbms.v1.model.detach_baremetal_server_volume_response import DetachBaremetalServerVolumeResponse
from huaweicloudsdkbms.v1.model.eip import Eip
from huaweicloudsdkbms.v1.model.entitie import Entitie
from huaweicloudsdkbms.v1.model.entities import Entities
from huaweicloudsdkbms.v1.model.extend_param import ExtendParam
from huaweicloudsdkbms.v1.model.extend_param_eip import ExtendParamEip
from huaweicloudsdkbms.v1.model.fault import Fault
from huaweicloudsdkbms.v1.model.fixed_ips import FixedIps
from huaweicloudsdkbms.v1.model.flavor_info import FlavorInfo
from huaweicloudsdkbms.v1.model.flavor_infos import FlavorInfos
from huaweicloudsdkbms.v1.model.flavors_resp import FlavorsResp
from huaweicloudsdkbms.v1.model.image import Image
from huaweicloudsdkbms.v1.model.image_info import ImageInfo
from huaweicloudsdkbms.v1.model.interface_attachments import InterfaceAttachments
from huaweicloudsdkbms.v1.model.key_value import KeyValue
from huaweicloudsdkbms.v1.model.links import Links
from huaweicloudsdkbms.v1.model.links_info import LinksInfo
from huaweicloudsdkbms.v1.model.list_bare_metal_server_details_request import ListBareMetalServerDetailsRequest
from huaweicloudsdkbms.v1.model.list_bare_metal_server_details_response import ListBareMetalServerDetailsResponse
from huaweicloudsdkbms.v1.model.list_bare_metal_servers_request import ListBareMetalServersRequest
from huaweicloudsdkbms.v1.model.list_bare_metal_servers_response import ListBareMetalServersResponse
from huaweicloudsdkbms.v1.model.list_baremetal_flavor_detail_extends_request import ListBaremetalFlavorDetailExtendsRequest
from huaweicloudsdkbms.v1.model.list_baremetal_flavor_detail_extends_response import ListBaremetalFlavorDetailExtendsResponse
from huaweicloudsdkbms.v1.model.meta_data import MetaData
from huaweicloudsdkbms.v1.model.meta_data_info import MetaDataInfo
from huaweicloudsdkbms.v1.model.metadata_infos import MetadataInfos
from huaweicloudsdkbms.v1.model.metadata_install import MetadataInstall
from huaweicloudsdkbms.v1.model.metadata_list import MetadataList
from huaweicloudsdkbms.v1.model.nics import Nics
from huaweicloudsdkbms.v1.model.os_extended_volumes import OsExtendedVolumes
from huaweicloudsdkbms.v1.model.os_extended_volumes_info import OsExtendedVolumesInfo
from huaweicloudsdkbms.v1.model.os_extra_specs import OsExtraSpecs
from huaweicloudsdkbms.v1.model.os_reinstall import OsReinstall
from huaweicloudsdkbms.v1.model.os_reinstall_body import OsReinstallBody
from huaweicloudsdkbms.v1.model.os_start_body import OsStartBody
from huaweicloudsdkbms.v1.model.os_stop_body import OsStopBody
from huaweicloudsdkbms.v1.model.os_stop_body_type import OsStopBodyType
from huaweicloudsdkbms.v1.model.public_ip import PublicIp
from huaweicloudsdkbms.v1.model.reboot_body import RebootBody
from huaweicloudsdkbms.v1.model.reinstall_baremetal_server_os_request import ReinstallBaremetalServerOsRequest
from huaweicloudsdkbms.v1.model.reinstall_baremetal_server_os_response import ReinstallBaremetalServerOsResponse
from huaweicloudsdkbms.v1.model.reset_password import ResetPassword
from huaweicloudsdkbms.v1.model.reset_password_body import ResetPasswordBody
from huaweicloudsdkbms.v1.model.reset_pwd_one_click_request import ResetPwdOneClickRequest
from huaweicloudsdkbms.v1.model.reset_pwd_one_click_response import ResetPwdOneClickResponse
from huaweicloudsdkbms.v1.model.root_volume import RootVolume
from huaweicloudsdkbms.v1.model.scheduler_hints import SchedulerHints
from huaweicloudsdkbms.v1.model.security_groups import SecurityGroups
from huaweicloudsdkbms.v1.model.security_groups_info import SecurityGroupsInfo
from huaweicloudsdkbms.v1.model.security_groups_list import SecurityGroupsList
from huaweicloudsdkbms.v1.model.server_details import ServerDetails
from huaweicloudsdkbms.v1.model.servers_info_type import ServersInfoType
from huaweicloudsdkbms.v1.model.servers_list import ServersList
from huaweicloudsdkbms.v1.model.show_baremetal_server_interface_attachments_request import ShowBaremetalServerInterfaceAttachmentsRequest
from huaweicloudsdkbms.v1.model.show_baremetal_server_interface_attachments_response import ShowBaremetalServerInterfaceAttachmentsResponse
from huaweicloudsdkbms.v1.model.show_baremetal_server_volume_info_request import ShowBaremetalServerVolumeInfoRequest
from huaweicloudsdkbms.v1.model.show_baremetal_server_volume_info_response import ShowBaremetalServerVolumeInfoResponse
from huaweicloudsdkbms.v1.model.show_job_infos_request import ShowJobInfosRequest
from huaweicloudsdkbms.v1.model.show_job_infos_response import ShowJobInfosResponse
from huaweicloudsdkbms.v1.model.show_reset_pwd_request import ShowResetPwdRequest
from huaweicloudsdkbms.v1.model.show_reset_pwd_response import ShowResetPwdResponse
from huaweicloudsdkbms.v1.model.show_specified_version_request import ShowSpecifiedVersionRequest
from huaweicloudsdkbms.v1.model.show_specified_version_response import ShowSpecifiedVersionResponse
from huaweicloudsdkbms.v1.model.show_tenant_quota_request import ShowTenantQuotaRequest
from huaweicloudsdkbms.v1.model.show_tenant_quota_response import ShowTenantQuotaResponse
from huaweicloudsdkbms.v1.model.show_windows_baremetal_server_pwd_request import ShowWindowsBaremetalServerPwdRequest
from huaweicloudsdkbms.v1.model.show_windows_baremetal_server_pwd_response import ShowWindowsBaremetalServerPwdResponse
from huaweicloudsdkbms.v1.model.start_servers_info import StartServersInfo
from huaweicloudsdkbms.v1.model.sub_jobs import SubJobs
from huaweicloudsdkbms.v1.model.system_tags import SystemTags
from huaweicloudsdkbms.v1.model.update_baremetal_server_metadata_request import UpdateBaremetalServerMetadataRequest
from huaweicloudsdkbms.v1.model.update_baremetal_server_metadata_response import UpdateBaremetalServerMetadataResponse
from huaweicloudsdkbms.v1.model.version_links import VersionLinks
from huaweicloudsdkbms.v1.model.versions import Versions
from huaweicloudsdkbms.v1.model.volume_attachment import VolumeAttachment
from huaweicloudsdkbms.v1.model.volume_attachments import VolumeAttachments