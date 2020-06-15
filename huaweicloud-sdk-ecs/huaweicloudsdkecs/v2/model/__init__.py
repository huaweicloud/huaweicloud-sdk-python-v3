# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkecs.v2.model.attach_server_volume_option import AttachServerVolumeOption
from huaweicloudsdkecs.v2.model.attach_server_volume_request import AttachServerVolumeRequest
from huaweicloudsdkecs.v2.model.attach_server_volume_request_body import AttachServerVolumeRequestBody
from huaweicloudsdkecs.v2.model.attach_server_volume_response import AttachServerVolumeResponse
from huaweicloudsdkecs.v2.model.batch_add_server_nic_option import BatchAddServerNicOption
from huaweicloudsdkecs.v2.model.batch_add_server_nics_request import BatchAddServerNicsRequest
from huaweicloudsdkecs.v2.model.batch_add_server_nics_request_body import BatchAddServerNicsRequestBody
from huaweicloudsdkecs.v2.model.batch_add_server_nics_response import BatchAddServerNicsResponse
from huaweicloudsdkecs.v2.model.batch_create_server_tags_request import BatchCreateServerTagsRequest
from huaweicloudsdkecs.v2.model.batch_create_server_tags_request_body import BatchCreateServerTagsRequestBody
from huaweicloudsdkecs.v2.model.batch_create_server_tags_response import BatchCreateServerTagsResponse
from huaweicloudsdkecs.v2.model.batch_delete_server_nic_option import BatchDeleteServerNicOption
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_request import BatchDeleteServerNicsRequest
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_request_body import BatchDeleteServerNicsRequestBody
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_response import BatchDeleteServerNicsResponse
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_request import BatchDeleteServerTagsRequest
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_request_body import BatchDeleteServerTagsRequestBody
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_response import BatchDeleteServerTagsResponse
from huaweicloudsdkecs.v2.model.batch_reboot_servers_request import BatchRebootServersRequest
from huaweicloudsdkecs.v2.model.batch_reboot_servers_request_body import BatchRebootServersRequestBody
from huaweicloudsdkecs.v2.model.batch_reboot_servers_response import BatchRebootServersResponse
from huaweicloudsdkecs.v2.model.batch_reboot_severs_option import BatchRebootSeversOption
from huaweicloudsdkecs.v2.model.batch_start_servers_option import BatchStartServersOption
from huaweicloudsdkecs.v2.model.batch_start_servers_request import BatchStartServersRequest
from huaweicloudsdkecs.v2.model.batch_start_servers_request_body import BatchStartServersRequestBody
from huaweicloudsdkecs.v2.model.batch_start_servers_response import BatchStartServersResponse
from huaweicloudsdkecs.v2.model.batch_stop_servers_option import BatchStopServersOption
from huaweicloudsdkecs.v2.model.batch_stop_servers_request import BatchStopServersRequest
from huaweicloudsdkecs.v2.model.batch_stop_servers_request_body import BatchStopServersRequestBody
from huaweicloudsdkecs.v2.model.batch_stop_servers_response import BatchStopServersResponse
from huaweicloudsdkecs.v2.model.block_device_attachable_quantity import BlockDeviceAttachableQuantity
from huaweicloudsdkecs.v2.model.create_post_paid_servers_request import CreatePostPaidServersRequest
from huaweicloudsdkecs.v2.model.create_post_paid_servers_request_body import CreatePostPaidServersRequestBody
from huaweicloudsdkecs.v2.model.create_post_paid_servers_response import CreatePostPaidServersResponse
from huaweicloudsdkecs.v2.model.delete_servers_request import DeleteServersRequest
from huaweicloudsdkecs.v2.model.delete_servers_request_body import DeleteServersRequestBody
from huaweicloudsdkecs.v2.model.delete_servers_response import DeleteServersResponse
from huaweicloudsdkecs.v2.model.detach_server_volume_request import DetachServerVolumeRequest
from huaweicloudsdkecs.v2.model.detach_server_volume_response import DetachServerVolumeResponse
from huaweicloudsdkecs.v2.model.flavor import Flavor
from huaweicloudsdkecs.v2.model.flavor_extra_spec import FlavorExtraSpec
from huaweicloudsdkecs.v2.model.flavor_link import FlavorLink
from huaweicloudsdkecs.v2.model.interface_attachment import InterfaceAttachment
from huaweicloudsdkecs.v2.model.ipv6_bandwidth import Ipv6Bandwidth
from huaweicloudsdkecs.v2.model.job_entities import JobEntities
from huaweicloudsdkecs.v2.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkecs.v2.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkecs.v2.model.list_server_block_devices_request import ListServerBlockDevicesRequest
from huaweicloudsdkecs.v2.model.list_server_block_devices_response import ListServerBlockDevicesResponse
from huaweicloudsdkecs.v2.model.list_server_interfaces_request import ListServerInterfacesRequest
from huaweicloudsdkecs.v2.model.list_server_interfaces_response import ListServerInterfacesResponse
from huaweicloudsdkecs.v2.model.list_servers_details_request import ListServersDetailsRequest
from huaweicloudsdkecs.v2.model.list_servers_details_response import ListServersDetailsResponse
from huaweicloudsdkecs.v2.model.nova_create_servers_option import NovaCreateServersOption
from huaweicloudsdkecs.v2.model.nova_create_servers_request import NovaCreateServersRequest
from huaweicloudsdkecs.v2.model.nova_create_servers_request_body import NovaCreateServersRequestBody
from huaweicloudsdkecs.v2.model.nova_create_servers_response import NovaCreateServersResponse
from huaweicloudsdkecs.v2.model.nova_create_servers_result import NovaCreateServersResult
from huaweicloudsdkecs.v2.model.nova_create_servers_scheduler_hint import NovaCreateServersSchedulerHint
from huaweicloudsdkecs.v2.model.nova_delete_server_request import NovaDeleteServerRequest
from huaweicloudsdkecs.v2.model.nova_delete_server_response import NovaDeleteServerResponse
from huaweicloudsdkecs.v2.model.nova_link import NovaLink
from huaweicloudsdkecs.v2.model.nova_list_servers_details_request import NovaListServersDetailsRequest
from huaweicloudsdkecs.v2.model.nova_list_servers_details_response import NovaListServersDetailsResponse
from huaweicloudsdkecs.v2.model.nova_network import NovaNetwork
from huaweicloudsdkecs.v2.model.nova_server import NovaServer
from huaweicloudsdkecs.v2.model.nova_server_block_device_mapping import NovaServerBlockDeviceMapping
from huaweicloudsdkecs.v2.model.nova_server_fault import NovaServerFault
from huaweicloudsdkecs.v2.model.nova_server_flavor import NovaServerFlavor
from huaweicloudsdkecs.v2.model.nova_server_image import NovaServerImage
from huaweicloudsdkecs.v2.model.nova_server_network import NovaServerNetwork
from huaweicloudsdkecs.v2.model.nova_server_security_group import NovaServerSecurityGroup
from huaweicloudsdkecs.v2.model.nova_server_volume import NovaServerVolume
from huaweicloudsdkecs.v2.model.nova_show_server_request import NovaShowServerRequest
from huaweicloudsdkecs.v2.model.nova_show_server_response import NovaShowServerResponse
from huaweicloudsdkecs.v2.model.page_link import PageLink
from huaweicloudsdkecs.v2.model.post_paid_server import PostPaidServer
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume import PostPaidServerDataVolume
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume_extend_param import PostPaidServerDataVolumeExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume_metadata import PostPaidServerDataVolumeMetadata
from huaweicloudsdkecs.v2.model.post_paid_server_eip import PostPaidServerEip
from huaweicloudsdkecs.v2.model.post_paid_server_eip_bandwidth import PostPaidServerEipBandwidth
from huaweicloudsdkecs.v2.model.post_paid_server_eip_extend_param import PostPaidServerEipExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_extend_param import PostPaidServerExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_ipv6_bandwidth import PostPaidServerIpv6Bandwidth
from huaweicloudsdkecs.v2.model.post_paid_server_nic import PostPaidServerNic
from huaweicloudsdkecs.v2.model.post_paid_server_publicip import PostPaidServerPublicip
from huaweicloudsdkecs.v2.model.post_paid_server_root_volume import PostPaidServerRootVolume
from huaweicloudsdkecs.v2.model.post_paid_server_root_volume_extend_param import PostPaidServerRootVolumeExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_scheduler_hints import PostPaidServerSchedulerHints
from huaweicloudsdkecs.v2.model.post_paid_server_security_group import PostPaidServerSecurityGroup
from huaweicloudsdkecs.v2.model.post_paid_server_tag import PostPaidServerTag
from huaweicloudsdkecs.v2.model.resize_post_paid_server_option import ResizePostPaidServerOption
from huaweicloudsdkecs.v2.model.resize_post_paid_server_request import ResizePostPaidServerRequest
from huaweicloudsdkecs.v2.model.resize_post_paid_server_request_body import ResizePostPaidServerRequestBody
from huaweicloudsdkecs.v2.model.resize_post_paid_server_response import ResizePostPaidServerResponse
from huaweicloudsdkecs.v2.model.server_address import ServerAddress
from huaweicloudsdkecs.v2.model.server_attachable_quantity import ServerAttachableQuantity
from huaweicloudsdkecs.v2.model.server_block_device import ServerBlockDevice
from huaweicloudsdkecs.v2.model.server_detail import ServerDetail
from huaweicloudsdkecs.v2.model.server_extend_volume_attachment import ServerExtendVolumeAttachment
from huaweicloudsdkecs.v2.model.server_fault import ServerFault
from huaweicloudsdkecs.v2.model.server_flavor import ServerFlavor
from huaweicloudsdkecs.v2.model.server_id import ServerId
from huaweicloudsdkecs.v2.model.server_image import ServerImage
from huaweicloudsdkecs.v2.model.server_interface_fixed_ip import ServerInterfaceFixedIp
from huaweicloudsdkecs.v2.model.server_nic_security_group import ServerNicSecurityGroup
from huaweicloudsdkecs.v2.model.server_scheduler_hints import ServerSchedulerHints
from huaweicloudsdkecs.v2.model.server_security_group import ServerSecurityGroup
from huaweicloudsdkecs.v2.model.server_system_tag import ServerSystemTag
from huaweicloudsdkecs.v2.model.server_tag import ServerTag
from huaweicloudsdkecs.v2.model.show_job_request import ShowJobRequest
from huaweicloudsdkecs.v2.model.show_job_response import ShowJobResponse
from huaweicloudsdkecs.v2.model.show_server_request import ShowServerRequest
from huaweicloudsdkecs.v2.model.show_server_response import ShowServerResponse
from huaweicloudsdkecs.v2.model.show_server_tags_request import ShowServerTagsRequest
from huaweicloudsdkecs.v2.model.show_server_tags_response import ShowServerTagsResponse
from huaweicloudsdkecs.v2.model.sub_job import SubJob
from huaweicloudsdkecs.v2.model.sub_job_entities import SubJobEntities
from huaweicloudsdkecs.v2.model.update_server_option import UpdateServerOption
from huaweicloudsdkecs.v2.model.update_server_request import UpdateServerRequest
from huaweicloudsdkecs.v2.model.update_server_request_body import UpdateServerRequestBody
from huaweicloudsdkecs.v2.model.update_server_response import UpdateServerResponse