# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkiec.v1.iec_client import IecClient
from huaweicloudsdkiec.v1.iec_async_client import IecAsyncClient

from huaweicloudsdkiec.v1.model.add_nics_request import AddNicsRequest
from huaweicloudsdkiec.v1.model.add_nics_request_body import AddNicsRequestBody
from huaweicloudsdkiec.v1.model.add_nics_response import AddNicsResponse
from huaweicloudsdkiec.v1.model.allowed_address_pair import AllowedAddressPair
from huaweicloudsdkiec.v1.model.associate_subnet_request import AssociateSubnetRequest
from huaweicloudsdkiec.v1.model.associate_subnet_request_body import AssociateSubnetRequestBody
from huaweicloudsdkiec.v1.model.associate_subnet_response import AssociateSubnetResponse
from huaweicloudsdkiec.v1.model.attachment import Attachment
from huaweicloudsdkiec.v1.model.bandwidth import Bandwidth
from huaweicloudsdkiec.v1.model.bandwidth_config import BandwidthConfig
from huaweicloudsdkiec.v1.model.bandwidth_config_instance import BandwidthConfigInstance
from huaweicloudsdkiec.v1.model.bandwidth_type_option import BandwidthTypeOption
from huaweicloudsdkiec.v1.model.base_id import BaseId
from huaweicloudsdkiec.v1.model.batch_reboot import BatchReboot
from huaweicloudsdkiec.v1.model.batch_reboot_instance_request import BatchRebootInstanceRequest
from huaweicloudsdkiec.v1.model.batch_reboot_instance_request_body import BatchRebootInstanceRequestBody
from huaweicloudsdkiec.v1.model.batch_reboot_instance_response import BatchRebootInstanceResponse
from huaweicloudsdkiec.v1.model.batch_start import BatchStart
from huaweicloudsdkiec.v1.model.batch_start_instance_request import BatchStartInstanceRequest
from huaweicloudsdkiec.v1.model.batch_start_instance_request_body import BatchStartInstanceRequestBody
from huaweicloudsdkiec.v1.model.batch_start_instance_response import BatchStartInstanceResponse
from huaweicloudsdkiec.v1.model.batch_stop import BatchStop
from huaweicloudsdkiec.v1.model.batch_stop_instance_request import BatchStopInstanceRequest
from huaweicloudsdkiec.v1.model.batch_stop_instance_request_body import BatchStopInstanceRequestBody
from huaweicloudsdkiec.v1.model.batch_stop_instance_response import BatchStopInstanceResponse
from huaweicloudsdkiec.v1.model.change_os_metadata import ChangeOsMetadata
from huaweicloudsdkiec.v1.model.change_os_option import ChangeOsOption
from huaweicloudsdkiec.v1.model.change_os_request import ChangeOsRequest
from huaweicloudsdkiec.v1.model.change_os_response import ChangeOsResponse
from huaweicloudsdkiec.v1.model.cloud_image_region_info import CloudImageRegionInfo
from huaweicloudsdkiec.v1.model.coverage import Coverage
from huaweicloudsdkiec.v1.model.coverage_instance import CoverageInstance
from huaweicloudsdkiec.v1.model.coverage_resp import CoverageResp
from huaweicloudsdkiec.v1.model.coverage_site import CoverageSite
from huaweicloudsdkiec.v1.model.coverage_site_instance import CoverageSiteInstance
from huaweicloudsdkiec.v1.model.coverage_site_resp import CoverageSiteResp
from huaweicloudsdkiec.v1.model.create_deployment_request import CreateDeploymentRequest
from huaweicloudsdkiec.v1.model.create_deployment_request_body import CreateDeploymentRequestBody
from huaweicloudsdkiec.v1.model.create_deployment_response import CreateDeploymentResponse
from huaweicloudsdkiec.v1.model.create_firewall_option import CreateFirewallOption
from huaweicloudsdkiec.v1.model.create_firewall_request import CreateFirewallRequest
from huaweicloudsdkiec.v1.model.create_firewall_request_body import CreateFirewallRequestBody
from huaweicloudsdkiec.v1.model.create_firewall_response import CreateFirewallResponse
from huaweicloudsdkiec.v1.model.create_image_request import CreateImageRequest
from huaweicloudsdkiec.v1.model.create_image_request_body import CreateImageRequestBody
from huaweicloudsdkiec.v1.model.create_image_response import CreateImageResponse
from huaweicloudsdkiec.v1.model.create_instance_option import CreateInstanceOption
from huaweicloudsdkiec.v1.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkiec.v1.model.create_instance_request_body import CreateInstanceRequestBody
from huaweicloudsdkiec.v1.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkiec.v1.model.create_keypair_request import CreateKeypairRequest
from huaweicloudsdkiec.v1.model.create_keypair_request_body import CreateKeypairRequestBody
from huaweicloudsdkiec.v1.model.create_keypair_response import CreateKeypairResponse
from huaweicloudsdkiec.v1.model.create_port_option import CreatePortOption
from huaweicloudsdkiec.v1.model.create_port_request import CreatePortRequest
from huaweicloudsdkiec.v1.model.create_port_request_body import CreatePortRequestBody
from huaweicloudsdkiec.v1.model.create_port_response import CreatePortResponse
from huaweicloudsdkiec.v1.model.create_public_ip_bandwidth_option import CreatePublicIpBandwidthOption
from huaweicloudsdkiec.v1.model.create_public_ip_option import CreatePublicIpOption
from huaweicloudsdkiec.v1.model.create_public_ip_request import CreatePublicIpRequest
from huaweicloudsdkiec.v1.model.create_public_ip_request_body import CreatePublicIpRequestBody
from huaweicloudsdkiec.v1.model.create_public_ip_response import CreatePublicIpResponse
from huaweicloudsdkiec.v1.model.create_routes_request import CreateRoutesRequest
from huaweicloudsdkiec.v1.model.create_routes_request_body import CreateRoutesRequestBody
from huaweicloudsdkiec.v1.model.create_routes_response import CreateRoutesResponse
from huaweicloudsdkiec.v1.model.create_routetable_option import CreateRoutetableOption
from huaweicloudsdkiec.v1.model.create_routetable_request import CreateRoutetableRequest
from huaweicloudsdkiec.v1.model.create_routetable_request_body import CreateRoutetableRequestBody
from huaweicloudsdkiec.v1.model.create_routetable_response import CreateRoutetableResponse
from huaweicloudsdkiec.v1.model.create_security_group_option import CreateSecurityGroupOption
from huaweicloudsdkiec.v1.model.create_security_group_request import CreateSecurityGroupRequest
from huaweicloudsdkiec.v1.model.create_security_group_request_body import CreateSecurityGroupRequestBody
from huaweicloudsdkiec.v1.model.create_security_group_response import CreateSecurityGroupResponse
from huaweicloudsdkiec.v1.model.create_security_group_rule_option import CreateSecurityGroupRuleOption
from huaweicloudsdkiec.v1.model.create_security_group_rule_request import CreateSecurityGroupRuleRequest
from huaweicloudsdkiec.v1.model.create_security_group_rule_request_body import CreateSecurityGroupRuleRequestBody
from huaweicloudsdkiec.v1.model.create_security_group_rule_response import CreateSecurityGroupRuleResponse
from huaweicloudsdkiec.v1.model.create_subnet_option import CreateSubnetOption
from huaweicloudsdkiec.v1.model.create_subnet_request import CreateSubnetRequest
from huaweicloudsdkiec.v1.model.create_subnet_request_body import CreateSubnetRequestBody
from huaweicloudsdkiec.v1.model.create_subnet_response import CreateSubnetResponse
from huaweicloudsdkiec.v1.model.create_vpc_option import CreateVpcOption
from huaweicloudsdkiec.v1.model.create_vpc_request import CreateVpcRequest
from huaweicloudsdkiec.v1.model.create_vpc_request_body import CreateVpcRequestBody
from huaweicloudsdkiec.v1.model.create_vpc_response import CreateVpcResponse
from huaweicloudsdkiec.v1.model.data_volume import DataVolume
from huaweicloudsdkiec.v1.model.delete_bandwidth_request import DeleteBandwidthRequest
from huaweicloudsdkiec.v1.model.delete_bandwidth_response import DeleteBandwidthResponse
from huaweicloudsdkiec.v1.model.delete_deployment_request import DeleteDeploymentRequest
from huaweicloudsdkiec.v1.model.delete_deployment_response import DeleteDeploymentResponse
from huaweicloudsdkiec.v1.model.delete_edge_cloud_request import DeleteEdgeCloudRequest
from huaweicloudsdkiec.v1.model.delete_edge_cloud_response import DeleteEdgeCloudResponse
from huaweicloudsdkiec.v1.model.delete_firewall_request import DeleteFirewallRequest
from huaweicloudsdkiec.v1.model.delete_firewall_response import DeleteFirewallResponse
from huaweicloudsdkiec.v1.model.delete_image_request import DeleteImageRequest
from huaweicloudsdkiec.v1.model.delete_image_response import DeleteImageResponse
from huaweicloudsdkiec.v1.model.delete_instances_request import DeleteInstancesRequest
from huaweicloudsdkiec.v1.model.delete_instances_request_body import DeleteInstancesRequestBody
from huaweicloudsdkiec.v1.model.delete_instances_response import DeleteInstancesResponse
from huaweicloudsdkiec.v1.model.delete_keypair_request import DeleteKeypairRequest
from huaweicloudsdkiec.v1.model.delete_keypair_response import DeleteKeypairResponse
from huaweicloudsdkiec.v1.model.delete_nics_request import DeleteNicsRequest
from huaweicloudsdkiec.v1.model.delete_nics_request_body import DeleteNicsRequestBody
from huaweicloudsdkiec.v1.model.delete_nics_response import DeleteNicsResponse
from huaweicloudsdkiec.v1.model.delete_port_request import DeletePortRequest
from huaweicloudsdkiec.v1.model.delete_port_response import DeletePortResponse
from huaweicloudsdkiec.v1.model.delete_public_ip_request import DeletePublicIpRequest
from huaweicloudsdkiec.v1.model.delete_public_ip_response import DeletePublicIpResponse
from huaweicloudsdkiec.v1.model.delete_route_option import DeleteRouteOption
from huaweicloudsdkiec.v1.model.delete_routes_request import DeleteRoutesRequest
from huaweicloudsdkiec.v1.model.delete_routes_request_body import DeleteRoutesRequestBody
from huaweicloudsdkiec.v1.model.delete_routes_response import DeleteRoutesResponse
from huaweicloudsdkiec.v1.model.delete_routetable_request import DeleteRoutetableRequest
from huaweicloudsdkiec.v1.model.delete_routetable_response import DeleteRoutetableResponse
from huaweicloudsdkiec.v1.model.delete_security_group_request import DeleteSecurityGroupRequest
from huaweicloudsdkiec.v1.model.delete_security_group_response import DeleteSecurityGroupResponse
from huaweicloudsdkiec.v1.model.delete_security_group_rule_request import DeleteSecurityGroupRuleRequest
from huaweicloudsdkiec.v1.model.delete_security_group_rule_response import DeleteSecurityGroupRuleResponse
from huaweicloudsdkiec.v1.model.delete_subnet_request import DeleteSubnetRequest
from huaweicloudsdkiec.v1.model.delete_subnet_response import DeleteSubnetResponse
from huaweicloudsdkiec.v1.model.delete_vpc_request import DeleteVpcRequest
from huaweicloudsdkiec.v1.model.delete_vpc_response import DeleteVpcResponse
from huaweicloudsdkiec.v1.model.demand import Demand
from huaweicloudsdkiec.v1.model.demand_instance import DemandInstance
from huaweicloudsdkiec.v1.model.demand_resp import DemandResp
from huaweicloudsdkiec.v1.model.deployment import Deployment
from huaweicloudsdkiec.v1.model.deployment_edgecloud import DeploymentEdgecloud
from huaweicloudsdkiec.v1.model.disassociate_subnet_request import DisassociateSubnetRequest
from huaweicloudsdkiec.v1.model.disassociate_subnet_request_body import DisassociateSubnetRequestBody
from huaweicloudsdkiec.v1.model.disassociate_subnet_response import DisassociateSubnetResponse
from huaweicloudsdkiec.v1.model.distribution import Distribution
from huaweicloudsdkiec.v1.model.dns_assignment import DnsAssignment
from huaweicloudsdkiec.v1.model.edge_cloud import EdgeCloud
from huaweicloudsdkiec.v1.model.edge_cloud_option import EdgeCloudOption
from huaweicloudsdkiec.v1.model.edge_image_region_info import EdgeImageRegionInfo
from huaweicloudsdkiec.v1.model.error_site import ErrorSite
from huaweicloudsdkiec.v1.model.execute_deployment_request import ExecuteDeploymentRequest
from huaweicloudsdkiec.v1.model.execute_deployment_response import ExecuteDeploymentResponse
from huaweicloudsdkiec.v1.model.expand_edgecloud_request import ExpandEdgecloudRequest
from huaweicloudsdkiec.v1.model.expand_edgecloud_response import ExpandEdgecloudResponse
from huaweicloudsdkiec.v1.model.extra_dhcp_option import ExtraDhcpOption
from huaweicloudsdkiec.v1.model.fail_reason import FailReason
from huaweicloudsdkiec.v1.model.firewall import Firewall
from huaweicloudsdkiec.v1.model.firewall_policy import FirewallPolicy
from huaweicloudsdkiec.v1.model.firewall_rule import FirewallRule
from huaweicloudsdkiec.v1.model.firewall_subnet_option import FirewallSubnetOption
from huaweicloudsdkiec.v1.model.fixed_ip import FixedIp
from huaweicloudsdkiec.v1.model.flavor import Flavor
from huaweicloudsdkiec.v1.model.flavor_instance import FlavorInstance
from huaweicloudsdkiec.v1.model.geo_location import GeoLocation
from huaweicloudsdkiec.v1.model.image_info import ImageInfo
from huaweicloudsdkiec.v1.model.image_list import ImageList
from huaweicloudsdkiec.v1.model.instance import Instance
from huaweicloudsdkiec.v1.model.instance_address import InstanceAddress
from huaweicloudsdkiec.v1.model.instance_job import InstanceJob
from huaweicloudsdkiec.v1.model.instance_security_group import InstanceSecurityGroup
from huaweicloudsdkiec.v1.model.ip_pool import IpPool
from huaweicloudsdkiec.v1.model.ipv6_bandwidth import Ipv6Bandwidth
from huaweicloudsdkiec.v1.model.job_result import JobResult
from huaweicloudsdkiec.v1.model.list_bandwidth_types_request import ListBandwidthTypesRequest
from huaweicloudsdkiec.v1.model.list_bandwidth_types_response import ListBandwidthTypesResponse
from huaweicloudsdkiec.v1.model.list_bandwidths_request import ListBandwidthsRequest
from huaweicloudsdkiec.v1.model.list_bandwidths_response import ListBandwidthsResponse
from huaweicloudsdkiec.v1.model.list_cloud_images_request import ListCloudImagesRequest
from huaweicloudsdkiec.v1.model.list_cloud_images_response import ListCloudImagesResponse
from huaweicloudsdkiec.v1.model.list_deployments_request import ListDeploymentsRequest
from huaweicloudsdkiec.v1.model.list_deployments_response import ListDeploymentsResponse
from huaweicloudsdkiec.v1.model.list_edge_cloud_request import ListEdgeCloudRequest
from huaweicloudsdkiec.v1.model.list_edge_cloud_response import ListEdgeCloudResponse
from huaweicloudsdkiec.v1.model.list_firewalls_request import ListFirewallsRequest
from huaweicloudsdkiec.v1.model.list_firewalls_response import ListFirewallsResponse
from huaweicloudsdkiec.v1.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkiec.v1.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkiec.v1.model.list_images_request import ListImagesRequest
from huaweicloudsdkiec.v1.model.list_images_response import ListImagesResponse
from huaweicloudsdkiec.v1.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkiec.v1.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkiec.v1.model.list_keypairs_request import ListKeypairsRequest
from huaweicloudsdkiec.v1.model.list_keypairs_response import ListKeypairsResponse
from huaweicloudsdkiec.v1.model.list_ports_request import ListPortsRequest
from huaweicloudsdkiec.v1.model.list_ports_response import ListPortsResponse
from huaweicloudsdkiec.v1.model.list_public_ips_request import ListPublicIpsRequest
from huaweicloudsdkiec.v1.model.list_public_ips_response import ListPublicIpsResponse
from huaweicloudsdkiec.v1.model.list_quota_request import ListQuotaRequest
from huaweicloudsdkiec.v1.model.list_quota_response import ListQuotaResponse
from huaweicloudsdkiec.v1.model.list_related_routetables_request import ListRelatedRoutetablesRequest
from huaweicloudsdkiec.v1.model.list_related_routetables_response import ListRelatedRoutetablesResponse
from huaweicloudsdkiec.v1.model.list_routes_request import ListRoutesRequest
from huaweicloudsdkiec.v1.model.list_routes_response import ListRoutesResponse
from huaweicloudsdkiec.v1.model.list_routetable_option import ListRoutetableOption
from huaweicloudsdkiec.v1.model.list_routetables_request import ListRoutetablesRequest
from huaweicloudsdkiec.v1.model.list_routetables_response import ListRoutetablesResponse
from huaweicloudsdkiec.v1.model.list_security_group_rules_request import ListSecurityGroupRulesRequest
from huaweicloudsdkiec.v1.model.list_security_group_rules_response import ListSecurityGroupRulesResponse
from huaweicloudsdkiec.v1.model.list_security_groups_request import ListSecurityGroupsRequest
from huaweicloudsdkiec.v1.model.list_security_groups_response import ListSecurityGroupsResponse
from huaweicloudsdkiec.v1.model.list_sites_request import ListSitesRequest
from huaweicloudsdkiec.v1.model.list_sites_response import ListSitesResponse
from huaweicloudsdkiec.v1.model.list_subnets_request import ListSubnetsRequest
from huaweicloudsdkiec.v1.model.list_subnets_response import ListSubnetsResponse
from huaweicloudsdkiec.v1.model.list_vpcs_request import ListVpcsRequest
from huaweicloudsdkiec.v1.model.list_vpcs_response import ListVpcsResponse
from huaweicloudsdkiec.v1.model.location import Location
from huaweicloudsdkiec.v1.model.net_config import NetConfig
from huaweicloudsdkiec.v1.model.net_config_instance import NetConfigInstance
from huaweicloudsdkiec.v1.model.nic_id import NicId
from huaweicloudsdkiec.v1.model.operator import Operator
from huaweicloudsdkiec.v1.model.os_extra_specs import OsExtraSpecs
from huaweicloudsdkiec.v1.model.port import Port
from huaweicloudsdkiec.v1.model.public_ip import PublicIp
from huaweicloudsdkiec.v1.model.publicip_info import PublicipInfo
from huaweicloudsdkiec.v1.model.quota_resource import QuotaResource
from huaweicloudsdkiec.v1.model.quota_resources import QuotaResources
from huaweicloudsdkiec.v1.model.rebuild_image_request import RebuildImageRequest
from huaweicloudsdkiec.v1.model.rebuild_image_request_body import RebuildImageRequestBody
from huaweicloudsdkiec.v1.model.rebuild_image_response import RebuildImageResponse
from huaweicloudsdkiec.v1.model.register_image_request import RegisterImageRequest
from huaweicloudsdkiec.v1.model.register_image_request_body import RegisterImageRequestBody
from huaweicloudsdkiec.v1.model.register_image_response import RegisterImageResponse
from huaweicloudsdkiec.v1.model.resource import Resource
from huaweicloudsdkiec.v1.model.root_volume import RootVolume
from huaweicloudsdkiec.v1.model.route import Route
from huaweicloudsdkiec.v1.model.route_option import RouteOption
from huaweicloudsdkiec.v1.model.routetable import Routetable
from huaweicloudsdkiec.v1.model.security_group import SecurityGroup
from huaweicloudsdkiec.v1.model.security_group_option import SecurityGroupOption
from huaweicloudsdkiec.v1.model.security_group_rule import SecurityGroupRule
from huaweicloudsdkiec.v1.model.show_bandwidth_request import ShowBandwidthRequest
from huaweicloudsdkiec.v1.model.show_bandwidth_response import ShowBandwidthResponse
from huaweicloudsdkiec.v1.model.show_edge_cloud_request import ShowEdgeCloudRequest
from huaweicloudsdkiec.v1.model.show_edge_cloud_response import ShowEdgeCloudResponse
from huaweicloudsdkiec.v1.model.show_firewall_request import ShowFirewallRequest
from huaweicloudsdkiec.v1.model.show_firewall_response import ShowFirewallResponse
from huaweicloudsdkiec.v1.model.show_image_request import ShowImageRequest
from huaweicloudsdkiec.v1.model.show_image_response import ShowImageResponse
from huaweicloudsdkiec.v1.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkiec.v1.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkiec.v1.model.show_keypair_request import ShowKeypairRequest
from huaweicloudsdkiec.v1.model.show_keypair_response import ShowKeypairResponse
from huaweicloudsdkiec.v1.model.show_port_request import ShowPortRequest
from huaweicloudsdkiec.v1.model.show_port_response import ShowPortResponse
from huaweicloudsdkiec.v1.model.show_public_ip_request import ShowPublicIpRequest
from huaweicloudsdkiec.v1.model.show_public_ip_response import ShowPublicIpResponse
from huaweicloudsdkiec.v1.model.show_routetable_request import ShowRoutetableRequest
from huaweicloudsdkiec.v1.model.show_routetable_response import ShowRoutetableResponse
from huaweicloudsdkiec.v1.model.show_security_group_request import ShowSecurityGroupRequest
from huaweicloudsdkiec.v1.model.show_security_group_response import ShowSecurityGroupResponse
from huaweicloudsdkiec.v1.model.show_security_group_rule_request import ShowSecurityGroupRuleRequest
from huaweicloudsdkiec.v1.model.show_security_group_rule_response import ShowSecurityGroupRuleResponse
from huaweicloudsdkiec.v1.model.show_subnet_request import ShowSubnetRequest
from huaweicloudsdkiec.v1.model.show_subnet_response import ShowSubnetResponse
from huaweicloudsdkiec.v1.model.show_volume_request import ShowVolumeRequest
from huaweicloudsdkiec.v1.model.show_volume_response import ShowVolumeResponse
from huaweicloudsdkiec.v1.model.show_volume_types_request import ShowVolumeTypesRequest
from huaweicloudsdkiec.v1.model.show_volume_types_response import ShowVolumeTypesResponse
from huaweicloudsdkiec.v1.model.show_vpc_request import ShowVpcRequest
from huaweicloudsdkiec.v1.model.show_vpc_response import ShowVpcResponse
from huaweicloudsdkiec.v1.model.simple_keypair import SimpleKeypair
from huaweicloudsdkiec.v1.model.site import Site
from huaweicloudsdkiec.v1.model.stack import Stack
from huaweicloudsdkiec.v1.model.subnet import Subnet
from huaweicloudsdkiec.v1.model.subnet_config import SubnetConfig
from huaweicloudsdkiec.v1.model.sys_tags import SysTags
from huaweicloudsdkiec.v1.model.update_bandwidth_option import UpdateBandwidthOption
from huaweicloudsdkiec.v1.model.update_bandwidth_request import UpdateBandwidthRequest
from huaweicloudsdkiec.v1.model.update_bandwidth_request_body import UpdateBandwidthRequestBody
from huaweicloudsdkiec.v1.model.update_bandwidth_response import UpdateBandwidthResponse
from huaweicloudsdkiec.v1.model.update_firewall_option import UpdateFirewallOption
from huaweicloudsdkiec.v1.model.update_firewall_request import UpdateFirewallRequest
from huaweicloudsdkiec.v1.model.update_firewall_request_body import UpdateFirewallRequestBody
from huaweicloudsdkiec.v1.model.update_firewall_resp import UpdateFirewallResp
from huaweicloudsdkiec.v1.model.update_firewall_response import UpdateFirewallResponse
from huaweicloudsdkiec.v1.model.update_firewall_rule_option import UpdateFirewallRuleOption
from huaweicloudsdkiec.v1.model.update_firewall_rule_request import UpdateFirewallRuleRequest
from huaweicloudsdkiec.v1.model.update_firewall_rule_request_body import UpdateFirewallRuleRequestBody
from huaweicloudsdkiec.v1.model.update_firewall_rule_resp import UpdateFirewallRuleResp
from huaweicloudsdkiec.v1.model.update_firewall_rule_response import UpdateFirewallRuleResponse
from huaweicloudsdkiec.v1.model.update_instance_option import UpdateInstanceOption
from huaweicloudsdkiec.v1.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkiec.v1.model.update_instance_request_body import UpdateInstanceRequestBody
from huaweicloudsdkiec.v1.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkiec.v1.model.update_port_option import UpdatePortOption
from huaweicloudsdkiec.v1.model.update_port_request import UpdatePortRequest
from huaweicloudsdkiec.v1.model.update_port_request_body import UpdatePortRequestBody
from huaweicloudsdkiec.v1.model.update_port_response import UpdatePortResponse
from huaweicloudsdkiec.v1.model.update_public_ip_option import UpdatePublicIpOption
from huaweicloudsdkiec.v1.model.update_public_ip_request import UpdatePublicIpRequest
from huaweicloudsdkiec.v1.model.update_public_ip_request_body import UpdatePublicIpRequestBody
from huaweicloudsdkiec.v1.model.update_public_ip_response import UpdatePublicIpResponse
from huaweicloudsdkiec.v1.model.update_routes_request import UpdateRoutesRequest
from huaweicloudsdkiec.v1.model.update_routes_request_body import UpdateRoutesRequestBody
from huaweicloudsdkiec.v1.model.update_routes_response import UpdateRoutesResponse
from huaweicloudsdkiec.v1.model.update_routetable_option import UpdateRoutetableOption
from huaweicloudsdkiec.v1.model.update_routetable_reques_body import UpdateRoutetableRequesBody
from huaweicloudsdkiec.v1.model.update_routetable_request import UpdateRoutetableRequest
from huaweicloudsdkiec.v1.model.update_routetable_response import UpdateRoutetableResponse
from huaweicloudsdkiec.v1.model.update_subnet_option import UpdateSubnetOption
from huaweicloudsdkiec.v1.model.update_subnet_request import UpdateSubnetRequest
from huaweicloudsdkiec.v1.model.update_subnet_request_body import UpdateSubnetRequestBody
from huaweicloudsdkiec.v1.model.update_subnet_response import UpdateSubnetResponse
from huaweicloudsdkiec.v1.model.update_subnet_response_object import UpdateSubnetResponseObject
from huaweicloudsdkiec.v1.model.update_vpc_option import UpdateVpcOption
from huaweicloudsdkiec.v1.model.update_vpc_request import UpdateVpcRequest
from huaweicloudsdkiec.v1.model.update_vpc_request_body import UpdateVpcRequestBody
from huaweicloudsdkiec.v1.model.update_vpc_response import UpdateVpcResponse
from huaweicloudsdkiec.v1.model.volume import Volume
from huaweicloudsdkiec.v1.model.volume_type import VolumeType
from huaweicloudsdkiec.v1.model.volumes_attached import VolumesAttached
from huaweicloudsdkiec.v1.model.vpc import Vpc

