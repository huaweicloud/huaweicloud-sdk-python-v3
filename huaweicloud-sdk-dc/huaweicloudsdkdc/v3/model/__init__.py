# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkdc.v3.model.batch_create_resource_tags_request import BatchCreateResourceTagsRequest
from huaweicloudsdkdc.v3.model.batch_create_resource_tags_response import BatchCreateResourceTagsResponse
from huaweicloudsdkdc.v3.model.batch_operate_resource_tags_request_body import BatchOperateResourceTagsRequestBody
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect import CreateHostedDirectConnect
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_request import CreateHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_request_body import CreateHostedDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_response import CreateHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.create_resource_tag_request import CreateResourceTagRequest
from huaweicloudsdkdc.v3.model.create_resource_tag_request_body import CreateResourceTagRequestBody
from huaweicloudsdkdc.v3.model.create_resource_tag_response import CreateResourceTagResponse
from huaweicloudsdkdc.v3.model.create_virtual_gateway import CreateVirtualGateway
from huaweicloudsdkdc.v3.model.create_virtual_gateway_request import CreateVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.create_virtual_gateway_request_body import CreateVirtualGatewayRequestBody
from huaweicloudsdkdc.v3.model.create_virtual_gateway_response import CreateVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.create_virtual_interface import CreateVirtualInterface
from huaweicloudsdkdc.v3.model.create_virtual_interface_request import CreateVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.create_virtual_interface_request_body import CreateVirtualInterfaceRequestBody
from huaweicloudsdkdc.v3.model.create_virtual_interface_response import CreateVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.delete_direct_connect_request import DeleteDirectConnectRequest
from huaweicloudsdkdc.v3.model.delete_direct_connect_response import DeleteDirectConnectResponse
from huaweicloudsdkdc.v3.model.delete_hosted_direct_connect_request import DeleteHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.delete_hosted_direct_connect_response import DeleteHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.delete_resource_tag_request import DeleteResourceTagRequest
from huaweicloudsdkdc.v3.model.delete_resource_tag_response import DeleteResourceTagResponse
from huaweicloudsdkdc.v3.model.delete_virtual_gateway_request import DeleteVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.delete_virtual_gateway_response import DeleteVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.delete_virtual_interface_request import DeleteVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.delete_virtual_interface_response import DeleteVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.direct_connect import DirectConnect
from huaweicloudsdkdc.v3.model.hosted_direct_connect import HostedDirectConnect
from huaweicloudsdkdc.v3.model.list_direct_connects_request import ListDirectConnectsRequest
from huaweicloudsdkdc.v3.model.list_direct_connects_response import ListDirectConnectsResponse
from huaweicloudsdkdc.v3.model.list_hosted_direct_connects_request import ListHostedDirectConnectsRequest
from huaweicloudsdkdc.v3.model.list_hosted_direct_connects_response import ListHostedDirectConnectsResponse
from huaweicloudsdkdc.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkdc.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_request import ListTagResourceInstancesRequest
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_request_body import ListTagResourceInstancesRequestBody
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_response import ListTagResourceInstancesResponse
from huaweicloudsdkdc.v3.model.list_virtual_gateways_request import ListVirtualGatewaysRequest
from huaweicloudsdkdc.v3.model.list_virtual_gateways_response import ListVirtualGatewaysResponse
from huaweicloudsdkdc.v3.model.list_virtual_interfaces_request import ListVirtualInterfacesRequest
from huaweicloudsdkdc.v3.model.list_virtual_interfaces_response import ListVirtualInterfacesResponse
from huaweicloudsdkdc.v3.model.match import Match
from huaweicloudsdkdc.v3.model.page_info import PageInfo
from huaweicloudsdkdc.v3.model.resource import Resource
from huaweicloudsdkdc.v3.model.show_direct_connect_request import ShowDirectConnectRequest
from huaweicloudsdkdc.v3.model.show_direct_connect_response import ShowDirectConnectResponse
from huaweicloudsdkdc.v3.model.show_hosted_direct_connect_request import ShowHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.show_hosted_direct_connect_response import ShowHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.show_resource_tag_request import ShowResourceTagRequest
from huaweicloudsdkdc.v3.model.show_resource_tag_response import ShowResourceTagResponse
from huaweicloudsdkdc.v3.model.show_virtual_gateway_request import ShowVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.show_virtual_gateway_response import ShowVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.show_virtual_interface_request import ShowVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.show_virtual_interface_response import ShowVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.tag import Tag
from huaweicloudsdkdc.v3.model.tags import Tags
from huaweicloudsdkdc.v3.model.tenant_id_def import TenantIdDef
from huaweicloudsdkdc.v3.model.update_direct_connect import UpdateDirectConnect
from huaweicloudsdkdc.v3.model.update_direct_connect_request import UpdateDirectConnectRequest
from huaweicloudsdkdc.v3.model.update_direct_connect_request_body import UpdateDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.update_direct_connect_response import UpdateDirectConnectResponse
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect import UpdateHostedDirectConnect
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_request import UpdateHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_request_body import UpdateHostedDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_response import UpdateHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.update_virtual_gateway import UpdateVirtualGateway
from huaweicloudsdkdc.v3.model.update_virtual_gateway_request import UpdateVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.update_virtual_gateway_request_body import UpdateVirtualGatewayRequestBody
from huaweicloudsdkdc.v3.model.update_virtual_gateway_response import UpdateVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.update_virtual_interface import UpdateVirtualInterface
from huaweicloudsdkdc.v3.model.update_virtual_interface_request import UpdateVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.update_virtual_interface_request_body import UpdateVirtualInterfaceRequestBody
from huaweicloudsdkdc.v3.model.update_virtual_interface_response import UpdateVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.vif_extend_attribute import VifExtendAttribute
from huaweicloudsdkdc.v3.model.vif_peer import VifPeer
from huaweicloudsdkdc.v3.model.virtual_gateway import VirtualGateway
from huaweicloudsdkdc.v3.model.virtual_interface import VirtualInterface
