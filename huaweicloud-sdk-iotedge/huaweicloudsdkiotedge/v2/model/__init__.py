# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkiotedge.v2.model.access_roma_brief_info import AccessRomaBriefInfo
from huaweicloudsdkiotedge.v2.model.access_roma_info import AccessRomaInfo
from huaweicloudsdkiotedge.v2.model.active_standby_config_dto import ActiveStandbyConfigDTO
from huaweicloudsdkiotedge.v2.model.add_app_configs_templates_request import AddAppConfigsTemplatesRequest
from huaweicloudsdkiotedge.v2.model.add_app_configs_templates_response import AddAppConfigsTemplatesResponse
from huaweicloudsdkiotedge.v2.model.add_device_request import AddDeviceRequest
from huaweicloudsdkiotedge.v2.model.add_device_request_body import AddDeviceRequestBody
from huaweicloudsdkiotedge.v2.model.add_device_response import AddDeviceResponse
from huaweicloudsdkiotedge.v2.model.add_general_app_configs_template_request import AddGeneralAppConfigsTemplateRequest
from huaweicloudsdkiotedge.v2.model.add_general_app_configs_template_response import AddGeneralAppConfigsTemplateResponse
from huaweicloudsdkiotedge.v2.model.add_general_ot_template_request import AddGeneralOtTemplateRequest
from huaweicloudsdkiotedge.v2.model.add_general_ot_template_response import AddGeneralOtTemplateResponse
from huaweicloudsdkiotedge.v2.model.add_ot_templates_request import AddOtTemplatesRequest
from huaweicloudsdkiotedge.v2.model.add_ot_templates_response import AddOtTemplatesResponse
from huaweicloudsdkiotedge.v2.model.auth_ak_sk_info import AuthAkSkInfo
from huaweicloudsdkiotedge.v2.model.authorize_na2_nodes_request_dto import AuthorizeNa2NodesRequestDTO
from huaweicloudsdkiotedge.v2.model.base_path_dto import BasePathDTO
from huaweicloudsdkiotedge.v2.model.batch_associate_na_to_nodes_request import BatchAssociateNaToNodesRequest
from huaweicloudsdkiotedge.v2.model.batch_associate_na_to_nodes_response import BatchAssociateNaToNodesResponse
from huaweicloudsdkiotedge.v2.model.batch_confirm_configs_new_request import BatchConfirmConfigsNewRequest
from huaweicloudsdkiotedge.v2.model.batch_confirm_configs_new_response import BatchConfirmConfigsNewResponse
from huaweicloudsdkiotedge.v2.model.batch_import_config_request_body import BatchImportConfigRequestBody
from huaweicloudsdkiotedge.v2.model.batch_import_configs_request import BatchImportConfigsRequest
from huaweicloudsdkiotedge.v2.model.batch_import_configs_request_body import BatchImportConfigsRequestBody
from huaweicloudsdkiotedge.v2.model.batch_import_configs_response import BatchImportConfigsResponse
from huaweicloudsdkiotedge.v2.model.batch_list_app_configs_templates_request import BatchListAppConfigsTemplatesRequest
from huaweicloudsdkiotedge.v2.model.batch_list_app_configs_templates_response import BatchListAppConfigsTemplatesResponse
from huaweicloudsdkiotedge.v2.model.batch_list_dc_devices_request import BatchListDcDevicesRequest
from huaweicloudsdkiotedge.v2.model.batch_list_dc_devices_response import BatchListDcDevicesResponse
from huaweicloudsdkiotedge.v2.model.batch_list_dc_ds_request import BatchListDcDsRequest
from huaweicloudsdkiotedge.v2.model.batch_list_dc_ds_response import BatchListDcDsResponse
from huaweicloudsdkiotedge.v2.model.batch_list_dc_points_request import BatchListDcPointsRequest
from huaweicloudsdkiotedge.v2.model.batch_list_dc_points_response import BatchListDcPointsResponse
from huaweicloudsdkiotedge.v2.model.batch_list_edge_app_versions_request import BatchListEdgeAppVersionsRequest
from huaweicloudsdkiotedge.v2.model.batch_list_edge_app_versions_response import BatchListEdgeAppVersionsResponse
from huaweicloudsdkiotedge.v2.model.batch_list_edge_apps_request import BatchListEdgeAppsRequest
from huaweicloudsdkiotedge.v2.model.batch_list_edge_apps_response import BatchListEdgeAppsResponse
from huaweicloudsdkiotedge.v2.model.batch_list_modules_request import BatchListModulesRequest
from huaweicloudsdkiotedge.v2.model.batch_list_modules_response import BatchListModulesResponse
from huaweicloudsdkiotedge.v2.model.batch_list_ot_templates_request import BatchListOtTemplatesRequest
from huaweicloudsdkiotedge.v2.model.batch_list_ot_templates_response import BatchListOtTemplatesResponse
from huaweicloudsdkiotedge.v2.model.certificate_local_path_dto import CertificateLocalPathDTO
from huaweicloudsdkiotedge.v2.model.confirm_ia_config_request_body import ConfirmIaConfigRequestBody
from huaweicloudsdkiotedge.v2.model.confirm_ia_configs_request_body import ConfirmIaConfigsRequestBody
from huaweicloudsdkiotedge.v2.model.container_configs_dto import ContainerConfigsDTO
from huaweicloudsdkiotedge.v2.model.container_configs_req_dto import ContainerConfigsReqDTO
from huaweicloudsdkiotedge.v2.model.container_configs_res_dto import ContainerConfigsResDTO
from huaweicloudsdkiotedge.v2.model.container_port_dto import ContainerPortDTO
from huaweicloudsdkiotedge.v2.model.container_settings_dto import ContainerSettingsDTO
from huaweicloudsdkiotedge.v2.model.container_settings_req_dto import ContainerSettingsReqDTO
from huaweicloudsdkiotedge.v2.model.create_app_configs_templates_req_dto import CreateAppConfigsTemplatesReqDTO
from huaweicloudsdkiotedge.v2.model.create_dc_ds_req_dto import CreateDcDsReqDTO
from huaweicloudsdkiotedge.v2.model.create_dc_point_req_dto import CreateDcPointReqDTO
from huaweicloudsdkiotedge.v2.model.create_dc_point_request import CreateDcPointRequest
from huaweicloudsdkiotedge.v2.model.create_dc_point_resp_dto import CreateDcPointRespDTO
from huaweicloudsdkiotedge.v2.model.create_dc_point_response import CreateDcPointResponse
from huaweicloudsdkiotedge.v2.model.create_ds_request import CreateDsRequest
from huaweicloudsdkiotedge.v2.model.create_ds_response import CreateDsResponse
from huaweicloudsdkiotedge.v2.model.create_edge_app_request import CreateEdgeAppRequest
from huaweicloudsdkiotedge.v2.model.create_edge_app_response import CreateEdgeAppResponse
from huaweicloudsdkiotedge.v2.model.create_edge_application_request_dto import CreateEdgeApplicationRequestDTO
from huaweicloudsdkiotedge.v2.model.create_edge_application_version_dto import CreateEdgeApplicationVersionDTO
from huaweicloudsdkiotedge.v2.model.create_edge_application_version_request import CreateEdgeApplicationVersionRequest
from huaweicloudsdkiotedge.v2.model.create_edge_application_version_response import CreateEdgeApplicationVersionResponse
from huaweicloudsdkiotedge.v2.model.create_edge_module_req_dto import CreateEdgeModuleReqDTO
from huaweicloudsdkiotedge.v2.model.create_edge_node_request import CreateEdgeNodeRequest
from huaweicloudsdkiotedge.v2.model.create_edge_node_response import CreateEdgeNodeResponse
from huaweicloudsdkiotedge.v2.model.create_external_entity_req_dto import CreateExternalEntityReqDTO
from huaweicloudsdkiotedge.v2.model.create_external_entity_request import CreateExternalEntityRequest
from huaweicloudsdkiotedge.v2.model.create_external_entity_response import CreateExternalEntityResponse
from huaweicloudsdkiotedge.v2.model.create_install_cmd_request import CreateInstallCmdRequest
from huaweicloudsdkiotedge.v2.model.create_install_cmd_request_dto import CreateInstallCmdRequestDTO
from huaweicloudsdkiotedge.v2.model.create_install_cmd_response import CreateInstallCmdResponse
from huaweicloudsdkiotedge.v2.model.create_module_request import CreateModuleRequest
from huaweicloudsdkiotedge.v2.model.create_module_response import CreateModuleResponse
from huaweicloudsdkiotedge.v2.model.create_ot_templates_req_dto import CreateOtTemplatesReqDTO
from huaweicloudsdkiotedge.v2.model.create_router_req_dto import CreateRouterReqDTO
from huaweicloudsdkiotedge.v2.model.delete_app_configs_template_request import DeleteAppConfigsTemplateRequest
from huaweicloudsdkiotedge.v2.model.delete_app_configs_template_response import DeleteAppConfigsTemplateResponse
from huaweicloudsdkiotedge.v2.model.delete_dc_ds_request import DeleteDcDsRequest
from huaweicloudsdkiotedge.v2.model.delete_dc_ds_response import DeleteDcDsResponse
from huaweicloudsdkiotedge.v2.model.delete_dc_point_request import DeleteDcPointRequest
from huaweicloudsdkiotedge.v2.model.delete_dc_point_response import DeleteDcPointResponse
from huaweicloudsdkiotedge.v2.model.delete_device_request import DeleteDeviceRequest
from huaweicloudsdkiotedge.v2.model.delete_device_response import DeleteDeviceResponse
from huaweicloudsdkiotedge.v2.model.delete_edge_app_request import DeleteEdgeAppRequest
from huaweicloudsdkiotedge.v2.model.delete_edge_app_response import DeleteEdgeAppResponse
from huaweicloudsdkiotedge.v2.model.delete_edge_application_version_request import DeleteEdgeApplicationVersionRequest
from huaweicloudsdkiotedge.v2.model.delete_edge_application_version_response import DeleteEdgeApplicationVersionResponse
from huaweicloudsdkiotedge.v2.model.delete_edge_node_request import DeleteEdgeNodeRequest
from huaweicloudsdkiotedge.v2.model.delete_edge_node_response import DeleteEdgeNodeResponse
from huaweicloudsdkiotedge.v2.model.delete_external_entity_request import DeleteExternalEntityRequest
from huaweicloudsdkiotedge.v2.model.delete_external_entity_response import DeleteExternalEntityResponse
from huaweicloudsdkiotedge.v2.model.delete_ia_config_request import DeleteIaConfigRequest
from huaweicloudsdkiotedge.v2.model.delete_ia_config_response import DeleteIaConfigResponse
from huaweicloudsdkiotedge.v2.model.delete_module_request import DeleteModuleRequest
from huaweicloudsdkiotedge.v2.model.delete_module_response import DeleteModuleResponse
from huaweicloudsdkiotedge.v2.model.delete_na_request import DeleteNaRequest
from huaweicloudsdkiotedge.v2.model.delete_na_response import DeleteNaResponse
from huaweicloudsdkiotedge.v2.model.delete_ot_template_request import DeleteOtTemplateRequest
from huaweicloudsdkiotedge.v2.model.delete_ot_template_response import DeleteOtTemplateResponse
from huaweicloudsdkiotedge.v2.model.device_auth_info_dto import DeviceAuthInfoDTO
from huaweicloudsdkiotedge.v2.model.device_auth_info_display_dto import DeviceAuthInfoDisplayDTO
from huaweicloudsdkiotedge.v2.model.device_data_record import DeviceDataRecord
from huaweicloudsdkiotedge.v2.model.edge_app_instance_dto import EdgeAppInstanceDTO
from huaweicloudsdkiotedge.v2.model.edge_device_auth_info import EdgeDeviceAuthInfo
from huaweicloudsdkiotedge.v2.model.edge_module_dto import EdgeModuleDTO
from huaweicloudsdkiotedge.v2.model.edge_node_creation import EdgeNodeCreation
from huaweicloudsdkiotedge.v2.model.edge_node_dto import EdgeNodeDTO
from huaweicloudsdkiotedge.v2.model.ext_device import ExtDevice
from huaweicloudsdkiotedge.v2.model.external_entity_resp_dto import ExternalEntityRespDTO
from huaweicloudsdkiotedge.v2.model.ha_config_dto import HaConfigDTO
from huaweicloudsdkiotedge.v2.model.http_get_dto import HttpGetDTO
from huaweicloudsdkiotedge.v2.model.import_points_request import ImportPointsRequest
from huaweicloudsdkiotedge.v2.model.import_points_request_body import ImportPointsRequestBody
from huaweicloudsdkiotedge.v2.model.import_points_response import ImportPointsResponse
from huaweicloudsdkiotedge.v2.model.list_devices_request import ListDevicesRequest
from huaweicloudsdkiotedge.v2.model.list_devices_response import ListDevicesResponse
from huaweicloudsdkiotedge.v2.model.list_edge_nodes_request import ListEdgeNodesRequest
from huaweicloudsdkiotedge.v2.model.list_edge_nodes_response import ListEdgeNodesResponse
from huaweicloudsdkiotedge.v2.model.list_external_entity_request import ListExternalEntityRequest
from huaweicloudsdkiotedge.v2.model.list_external_entity_response import ListExternalEntityResponse
from huaweicloudsdkiotedge.v2.model.list_ia_configs_request import ListIaConfigsRequest
from huaweicloudsdkiotedge.v2.model.list_ia_configs_response import ListIaConfigsResponse
from huaweicloudsdkiotedge.v2.model.list_na_authorized_nodes_request import ListNaAuthorizedNodesRequest
from huaweicloudsdkiotedge.v2.model.list_na_authorized_nodes_response import ListNaAuthorizedNodesResponse
from huaweicloudsdkiotedge.v2.model.list_nas_request import ListNasRequest
from huaweicloudsdkiotedge.v2.model.list_nas_response import ListNasResponse
from huaweicloudsdkiotedge.v2.model.list_routes_request import ListRoutesRequest
from huaweicloudsdkiotedge.v2.model.list_routes_response import ListRoutesResponse
from huaweicloudsdkiotedge.v2.model.log_config_dto import LogConfigDTO
from huaweicloudsdkiotedge.v2.model.module_container_settings_res_dto import ModuleContainerSettingsResDTO
from huaweicloudsdkiotedge.v2.model.mqtt_connection_info import MqttConnectionInfo
from huaweicloudsdkiotedge.v2.model.nic import Nic
from huaweicloudsdkiotedge.v2.model.offline_cache_configs_dto import OfflineCacheConfigsDTO
from huaweicloudsdkiotedge.v2.model.page_info_dto import PageInfoDTO
from huaweicloudsdkiotedge.v2.model.point_clean_dto import PointCleanDTO
from huaweicloudsdkiotedge.v2.model.point_scaling_dto import PointScalingDTO
from huaweicloudsdkiotedge.v2.model.point_validitying_dto import PointValidityingDTO
from huaweicloudsdkiotedge.v2.model.probe_dto import ProbeDTO
from huaweicloudsdkiotedge.v2.model.processing_config_dto import ProcessingConfigDTO
from huaweicloudsdkiotedge.v2.model.query_app_configs_template_brief_resp_dto import QueryAppConfigsTemplateBriefRespDTO
from huaweicloudsdkiotedge.v2.model.query_application_brief_response_dto import QueryApplicationBriefResponseDTO
from huaweicloudsdkiotedge.v2.model.query_authorized_node_dto import QueryAuthorizedNodeDTO
from huaweicloudsdkiotedge.v2.model.query_dc_device_resp_dto import QueryDcDeviceRespDTO
from huaweicloudsdkiotedge.v2.model.query_dc_ds_brief_resp_dto import QueryDcDsBriefRespDTO
from huaweicloudsdkiotedge.v2.model.query_device_simplify_dto import QueryDeviceSimplifyDto
from huaweicloudsdkiotedge.v2.model.query_edge_app_version_brief_response_dto import QueryEdgeAppVersionBriefResponseDTO
from huaweicloudsdkiotedge.v2.model.query_ia_config_response_dto import QueryIaConfigResponseDTO
from huaweicloudsdkiotedge.v2.model.query_na_brief_response_dto import QueryNaBriefResponseDTO
from huaweicloudsdkiotedge.v2.model.query_ot_template_brief_resp_dto import QueryOtTemplateBriefRespDTO
from huaweicloudsdkiotedge.v2.model.resource_config_dto import ResourceConfigDTO
from huaweicloudsdkiotedge.v2.model.resource_dto import ResourceDTO
from huaweicloudsdkiotedge.v2.model.router_detail_resp_dto import RouterDetailRespDTO
from huaweicloudsdkiotedge.v2.model.router_resp_dto import RouterRespDTO
from huaweicloudsdkiotedge.v2.model.show_app_configs_template_request import ShowAppConfigsTemplateRequest
from huaweicloudsdkiotedge.v2.model.show_app_configs_template_response import ShowAppConfigsTemplateResponse
from huaweicloudsdkiotedge.v2.model.show_dc_ds_request import ShowDcDsRequest
from huaweicloudsdkiotedge.v2.model.show_dc_ds_response import ShowDcDsResponse
from huaweicloudsdkiotedge.v2.model.show_dc_point_request import ShowDcPointRequest
from huaweicloudsdkiotedge.v2.model.show_dc_point_response import ShowDcPointResponse
from huaweicloudsdkiotedge.v2.model.show_edge_app_request import ShowEdgeAppRequest
from huaweicloudsdkiotedge.v2.model.show_edge_app_response import ShowEdgeAppResponse
from huaweicloudsdkiotedge.v2.model.show_edge_application_version_request import ShowEdgeApplicationVersionRequest
from huaweicloudsdkiotedge.v2.model.show_edge_application_version_response import ShowEdgeApplicationVersionResponse
from huaweicloudsdkiotedge.v2.model.show_edge_node_request import ShowEdgeNodeRequest
from huaweicloudsdkiotedge.v2.model.show_edge_node_response import ShowEdgeNodeResponse
from huaweicloudsdkiotedge.v2.model.show_ia_config_request import ShowIaConfigRequest
from huaweicloudsdkiotedge.v2.model.show_ia_config_response import ShowIaConfigResponse
from huaweicloudsdkiotedge.v2.model.show_module_request import ShowModuleRequest
from huaweicloudsdkiotedge.v2.model.show_module_response import ShowModuleResponse
from huaweicloudsdkiotedge.v2.model.show_module_shadow_request import ShowModuleShadowRequest
from huaweicloudsdkiotedge.v2.model.show_module_shadow_response import ShowModuleShadowResponse
from huaweicloudsdkiotedge.v2.model.show_na_request import ShowNaRequest
from huaweicloudsdkiotedge.v2.model.show_na_response import ShowNaResponse
from huaweicloudsdkiotedge.v2.model.show_ot_template_request import ShowOtTemplateRequest
from huaweicloudsdkiotedge.v2.model.show_ot_template_response import ShowOtTemplateResponse
from huaweicloudsdkiotedge.v2.model.show_point_template_request import ShowPointTemplateRequest
from huaweicloudsdkiotedge.v2.model.show_point_template_response import ShowPointTemplateResponse
from huaweicloudsdkiotedge.v2.model.show_points_request import ShowPointsRequest
from huaweicloudsdkiotedge.v2.model.show_points_response import ShowPointsResponse
from huaweicloudsdkiotedge.v2.model.show_product_config_request import ShowProductConfigRequest
from huaweicloudsdkiotedge.v2.model.show_product_config_response import ShowProductConfigResponse
from huaweicloudsdkiotedge.v2.model.synchronize_dc_configs_request import SynchronizeDcConfigsRequest
from huaweicloudsdkiotedge.v2.model.synchronize_dc_configs_response import SynchronizeDcConfigsResponse
from huaweicloudsdkiotedge.v2.model.tcp_socket_dto import TcpSocketDTO
from huaweicloudsdkiotedge.v2.model.update_dc_ds_req_dto import UpdateDcDsReqDTO
from huaweicloudsdkiotedge.v2.model.update_dc_ds_request import UpdateDcDsRequest
from huaweicloudsdkiotedge.v2.model.update_dc_ds_response import UpdateDcDsResponse
from huaweicloudsdkiotedge.v2.model.update_dc_point_req_dto import UpdateDcPointReqDTO
from huaweicloudsdkiotedge.v2.model.update_dc_point_request import UpdateDcPointRequest
from huaweicloudsdkiotedge.v2.model.update_dc_point_response import UpdateDcPointResponse
from huaweicloudsdkiotedge.v2.model.update_desireds import UpdateDesireds
from huaweicloudsdkiotedge.v2.model.update_device_request import UpdateDeviceRequest
from huaweicloudsdkiotedge.v2.model.update_device_response import UpdateDeviceResponse
from huaweicloudsdkiotedge.v2.model.update_edge_app_version_dto import UpdateEdgeAppVersionDTO
from huaweicloudsdkiotedge.v2.model.update_edge_app_version_state_dto import UpdateEdgeAppVersionStateDTO
from huaweicloudsdkiotedge.v2.model.update_edge_application_version_request import UpdateEdgeApplicationVersionRequest
from huaweicloudsdkiotedge.v2.model.update_edge_application_version_response import UpdateEdgeApplicationVersionResponse
from huaweicloudsdkiotedge.v2.model.update_edge_application_version_state_request import UpdateEdgeApplicationVersionStateRequest
from huaweicloudsdkiotedge.v2.model.update_edge_application_version_state_response import UpdateEdgeApplicationVersionStateResponse
from huaweicloudsdkiotedge.v2.model.update_edge_module_req_dto import UpdateEdgeModuleReqDTO
from huaweicloudsdkiotedge.v2.model.update_edge_module_state_req_dto import UpdateEdgeModuleStateReqDTO
from huaweicloudsdkiotedge.v2.model.update_external_entity_req_dto import UpdateExternalEntityReqDTO
from huaweicloudsdkiotedge.v2.model.update_external_entity_request import UpdateExternalEntityRequest
from huaweicloudsdkiotedge.v2.model.update_external_entity_response import UpdateExternalEntityResponse
from huaweicloudsdkiotedge.v2.model.update_ia_config_request import UpdateIaConfigRequest
from huaweicloudsdkiotedge.v2.model.update_ia_config_request_dto import UpdateIaConfigRequestDTO
from huaweicloudsdkiotedge.v2.model.update_ia_config_response import UpdateIaConfigResponse
from huaweicloudsdkiotedge.v2.model.update_module_request import UpdateModuleRequest
from huaweicloudsdkiotedge.v2.model.update_module_response import UpdateModuleResponse
from huaweicloudsdkiotedge.v2.model.update_module_shadow_request import UpdateModuleShadowRequest
from huaweicloudsdkiotedge.v2.model.update_module_shadow_response import UpdateModuleShadowResponse
from huaweicloudsdkiotedge.v2.model.update_module_shadows_request_body import UpdateModuleShadowsRequestBody
from huaweicloudsdkiotedge.v2.model.update_module_state_request import UpdateModuleStateRequest
from huaweicloudsdkiotedge.v2.model.update_module_state_response import UpdateModuleStateResponse
from huaweicloudsdkiotedge.v2.model.update_na_request import UpdateNaRequest
from huaweicloudsdkiotedge.v2.model.update_na_request_dto import UpdateNaRequestDTO
from huaweicloudsdkiotedge.v2.model.update_na_response import UpdateNaResponse
from huaweicloudsdkiotedge.v2.model.update_routes_request import UpdateRoutesRequest
from huaweicloudsdkiotedge.v2.model.update_routes_response import UpdateRoutesResponse
from huaweicloudsdkiotedge.v2.model.volume_dto import VolumeDTO
