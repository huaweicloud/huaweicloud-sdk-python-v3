# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkdli.v1.dli_client import DliClient
from huaweicloudsdkdli.v1.dli_async_client import DliAsyncClient

from huaweicloudsdkdli.v1.model.associate_connection_queue_req import AssociateConnectionQueueReq
from huaweicloudsdkdli.v1.model.associate_queue_to_elastic_resource_pool_request import AssociateQueueToElasticResourcePoolRequest
from huaweicloudsdkdli.v1.model.associate_queue_to_elastic_resource_pool_request_body import AssociateQueueToElasticResourcePoolRequestBody
from huaweicloudsdkdli.v1.model.associate_queue_to_elastic_resource_pool_response import AssociateQueueToElasticResourcePoolResponse
from huaweicloudsdkdli.v1.model.associate_queue_to_enhanced_connection_request import AssociateQueueToEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.associate_queue_to_enhanced_connection_response import AssociateQueueToEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.auth_infos import AuthInfos
from huaweicloudsdkdli.v1.model.authorize_resource_request_body import AuthorizeResourceRequestBody
from huaweicloudsdkdli.v1.model.available_queue_info import AvailableQueueInfo
from huaweicloudsdkdli.v1.model.batch_delete_flink_jobs_request import BatchDeleteFlinkJobsRequest
from huaweicloudsdkdli.v1.model.batch_delete_flink_jobs_request_body import BatchDeleteFlinkJobsRequestBody
from huaweicloudsdkdli.v1.model.batch_delete_flink_jobs_response import BatchDeleteFlinkJobsResponse
from huaweicloudsdkdli.v1.model.batch_delete_queue_plans_request import BatchDeleteQueuePlansRequest
from huaweicloudsdkdli.v1.model.batch_delete_queue_plans_response import BatchDeleteQueuePlansResponse
from huaweicloudsdkdli.v1.model.batch_delete_sql_job_templates_request import BatchDeleteSqlJobTemplatesRequest
from huaweicloudsdkdli.v1.model.batch_delete_sql_job_templates_response import BatchDeleteSqlJobTemplatesResponse
from huaweicloudsdkdli.v1.model.batch_job_info import BatchJobInfo
from huaweicloudsdkdli.v1.model.batch_run_flink_jobs_request import BatchRunFlinkJobsRequest
from huaweicloudsdkdli.v1.model.batch_run_flink_jobs_request_body import BatchRunFlinkJobsRequestBody
from huaweicloudsdkdli.v1.model.batch_run_flink_jobs_response import BatchRunFlinkJobsResponse
from huaweicloudsdkdli.v1.model.cancel_spark_job_request import CancelSparkJobRequest
from huaweicloudsdkdli.v1.model.cancel_spark_job_response import CancelSparkJobResponse
from huaweicloudsdkdli.v1.model.cancel_sql_job_request import CancelSqlJobRequest
from huaweicloudsdkdli.v1.model.cancel_sql_job_response import CancelSqlJobResponse
from huaweicloudsdkdli.v1.model.change_authorization_request import ChangeAuthorizationRequest
from huaweicloudsdkdli.v1.model.change_authorization_response import ChangeAuthorizationResponse
from huaweicloudsdkdli.v1.model.change_flink_job_status_report_request import ChangeFlinkJobStatusReportRequest
from huaweicloudsdkdli.v1.model.change_flink_job_status_report_response import ChangeFlinkJobStatusReportResponse
from huaweicloudsdkdli.v1.model.change_queue_plan_request import ChangeQueuePlanRequest
from huaweicloudsdkdli.v1.model.change_queue_plan_response import ChangeQueuePlanResponse
from huaweicloudsdkdli.v1.model.check_sql_request import CheckSqlRequest
from huaweicloudsdkdli.v1.model.check_sql_request_body import CheckSqlRequestBody
from huaweicloudsdkdli.v1.model.check_sql_response import CheckSqlResponse
from huaweicloudsdkdli.v1.model.common_resp import CommonResp
from huaweicloudsdkdli.v1.model.create_agency_request import CreateAgencyRequest
from huaweicloudsdkdli.v1.model.create_auth_info_req import CreateAuthInfoReq
from huaweicloudsdkdli.v1.model.create_auth_info_request import CreateAuthInfoRequest
from huaweicloudsdkdli.v1.model.create_auth_info_response import CreateAuthInfoResponse
from huaweicloudsdkdli.v1.model.create_connectivity_task_request import CreateConnectivityTaskRequest
from huaweicloudsdkdli.v1.model.create_connectivity_task_response import CreateConnectivityTaskResponse
from huaweicloudsdkdli.v1.model.create_database_request import CreateDatabaseRequest
from huaweicloudsdkdli.v1.model.create_database_request_body import CreateDatabaseRequestBody
from huaweicloudsdkdli.v1.model.create_database_response import CreateDatabaseResponse
from huaweicloudsdkdli.v1.model.create_datasource_connection_req import CreateDatasourceConnectionReq
from huaweicloudsdkdli.v1.model.create_datasource_connection_request import CreateDatasourceConnectionRequest
from huaweicloudsdkdli.v1.model.create_datasource_connection_response import CreateDatasourceConnectionResponse
from huaweicloudsdkdli.v1.model.create_dli_agency_request import CreateDliAgencyRequest
from huaweicloudsdkdli.v1.model.create_dli_agency_response import CreateDliAgencyResponse
from huaweicloudsdkdli.v1.model.create_elastic_resource_pool_request import CreateElasticResourcePoolRequest
from huaweicloudsdkdli.v1.model.create_elastic_resource_pool_request_body import CreateElasticResourcePoolRequestBody
from huaweicloudsdkdli.v1.model.create_elastic_resource_pool_response import CreateElasticResourcePoolResponse
from huaweicloudsdkdli.v1.model.create_enhanced_connection_request import CreateEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.create_enhanced_connection_response import CreateEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.create_enhanced_connection_routes_request import CreateEnhancedConnectionRoutesRequest
from huaweicloudsdkdli.v1.model.create_enhanced_connection_routes_response import CreateEnhancedConnectionRoutesResponse
from huaweicloudsdkdli.v1.model.create_enhanced_connections_req import CreateEnhancedConnectionsReq
from huaweicloudsdkdli.v1.model.create_flink_jar_job_request import CreateFlinkJarJobRequest
from huaweicloudsdkdli.v1.model.create_flink_jar_job_response import CreateFlinkJarJobResponse
from huaweicloudsdkdli.v1.model.create_flink_jar_request_body import CreateFlinkJarRequestBody
from huaweicloudsdkdli.v1.model.create_flink_sql_job_graph_request import CreateFlinkSqlJobGraphRequest
from huaweicloudsdkdli.v1.model.create_flink_sql_job_graph_response import CreateFlinkSqlJobGraphResponse
from huaweicloudsdkdli.v1.model.create_flink_sql_job_request import CreateFlinkSqlJobRequest
from huaweicloudsdkdli.v1.model.create_flink_sql_job_request_body import CreateFlinkSqlJobRequestBody
from huaweicloudsdkdli.v1.model.create_flink_sql_job_response import CreateFlinkSqlJobResponse
from huaweicloudsdkdli.v1.model.create_flink_sql_job_template_request import CreateFlinkSqlJobTemplateRequest
from huaweicloudsdkdli.v1.model.create_flink_sql_job_template_response import CreateFlinkSqlJobTemplateResponse
from huaweicloudsdkdli.v1.model.create_flink_template_request_body import CreateFlinkTemplateRequestBody
from huaweicloudsdkdli.v1.model.create_global_value_req import CreateGlobalValueReq
from huaweicloudsdkdli.v1.model.create_global_variable_request import CreateGlobalVariableRequest
from huaweicloudsdkdli.v1.model.create_global_variable_response import CreateGlobalVariableResponse
from huaweicloudsdkdli.v1.model.create_ief_message_channel_req import CreateIefMessageChannelReq
from huaweicloudsdkdli.v1.model.create_ief_message_channel_request import CreateIefMessageChannelRequest
from huaweicloudsdkdli.v1.model.create_ief_message_channel_response import CreateIefMessageChannelResponse
from huaweicloudsdkdli.v1.model.create_ief_system_events_request import CreateIefSystemEventsRequest
from huaweicloudsdkdli.v1.model.create_ief_system_events_response import CreateIefSystemEventsResponse
from huaweicloudsdkdli.v1.model.create_job_auth_info_request import CreateJobAuthInfoRequest
from huaweicloudsdkdli.v1.model.create_job_auth_info_request_body import CreateJobAuthInfoRequestBody
from huaweicloudsdkdli.v1.model.create_job_auth_info_response import CreateJobAuthInfoResponse
from huaweicloudsdkdli.v1.model.create_job_resp_job import CreateJobRespJob
from huaweicloudsdkdli.v1.model.create_job_templates_request_body import CreateJobTemplatesRequestBody
from huaweicloudsdkdli.v1.model.create_queue_plan_request import CreateQueuePlanRequest
from huaweicloudsdkdli.v1.model.create_queue_plan_response import CreateQueuePlanResponse
from huaweicloudsdkdli.v1.model.create_queue_property_request import CreateQueuePropertyRequest
from huaweicloudsdkdli.v1.model.create_queue_property_response import CreateQueuePropertyResponse
from huaweicloudsdkdli.v1.model.create_queue_req import CreateQueueReq
from huaweicloudsdkdli.v1.model.create_queue_request import CreateQueueRequest
from huaweicloudsdkdli.v1.model.create_queue_response import CreateQueueResponse
from huaweicloudsdkdli.v1.model.create_route_request_body import CreateRouteRequestBody
from huaweicloudsdkdli.v1.model.create_route_to_enhanced_connection_request import CreateRouteToEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.create_route_to_enhanced_connection_request_body import CreateRouteToEnhancedConnectionRequestBody
from huaweicloudsdkdli.v1.model.create_route_to_enhanced_connection_response import CreateRouteToEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.create_session_req_group import CreateSessionReqGroup
from huaweicloudsdkdli.v1.model.create_session_req_resource import CreateSessionReqResource
from huaweicloudsdkdli.v1.model.create_spark_job_request import CreateSparkJobRequest
from huaweicloudsdkdli.v1.model.create_spark_job_response import CreateSparkJobResponse
from huaweicloudsdkdli.v1.model.create_spark_job_template_request import CreateSparkJobTemplateRequest
from huaweicloudsdkdli.v1.model.create_spark_job_template_response import CreateSparkJobTemplateResponse
from huaweicloudsdkdli.v1.model.create_sql_job_request import CreateSqlJobRequest
from huaweicloudsdkdli.v1.model.create_sql_job_request_body import CreateSqlJobRequestBody
from huaweicloudsdkdli.v1.model.create_sql_job_response import CreateSqlJobResponse
from huaweicloudsdkdli.v1.model.create_sql_job_template_request import CreateSqlJobTemplateRequest
from huaweicloudsdkdli.v1.model.create_sql_job_template_response import CreateSqlJobTemplateResponse
from huaweicloudsdkdli.v1.model.create_sql_templates_request_body import CreateSqlTemplatesRequestBody
from huaweicloudsdkdli.v1.model.create_table_req import CreateTableReq
from huaweicloudsdkdli.v1.model.create_table_req_column import CreateTableReqColumn
from huaweicloudsdkdli.v1.model.create_table_request import CreateTableRequest
from huaweicloudsdkdli.v1.model.create_table_response import CreateTableResponse
from huaweicloudsdkdli.v1.model.database import Database
from huaweicloudsdkdli.v1.model.delete_auth_info_request import DeleteAuthInfoRequest
from huaweicloudsdkdli.v1.model.delete_auth_info_response import DeleteAuthInfoResponse
from huaweicloudsdkdli.v1.model.delete_database_request import DeleteDatabaseRequest
from huaweicloudsdkdli.v1.model.delete_database_response import DeleteDatabaseResponse
from huaweicloudsdkdli.v1.model.delete_datasource_connection_request import DeleteDatasourceConnectionRequest
from huaweicloudsdkdli.v1.model.delete_datasource_connection_response import DeleteDatasourceConnectionResponse
from huaweicloudsdkdli.v1.model.delete_elastic_resource_pool_request import DeleteElasticResourcePoolRequest
from huaweicloudsdkdli.v1.model.delete_elastic_resource_pool_response import DeleteElasticResourcePoolResponse
from huaweicloudsdkdli.v1.model.delete_enhanced_connection_request import DeleteEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.delete_enhanced_connection_response import DeleteEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.delete_enhanced_connection_routes_request import DeleteEnhancedConnectionRoutesRequest
from huaweicloudsdkdli.v1.model.delete_enhanced_connection_routes_response import DeleteEnhancedConnectionRoutesResponse
from huaweicloudsdkdli.v1.model.delete_flink_job_request import DeleteFlinkJobRequest
from huaweicloudsdkdli.v1.model.delete_flink_job_response import DeleteFlinkJobResponse
from huaweicloudsdkdli.v1.model.delete_flink_sql_job_template_request import DeleteFlinkSqlJobTemplateRequest
from huaweicloudsdkdli.v1.model.delete_flink_sql_job_template_response import DeleteFlinkSqlJobTemplateResponse
from huaweicloudsdkdli.v1.model.delete_global_variable_request import DeleteGlobalVariableRequest
from huaweicloudsdkdli.v1.model.delete_global_variable_response import DeleteGlobalVariableResponse
from huaweicloudsdkdli.v1.model.delete_job_auth_info_request import DeleteJobAuthInfoRequest
from huaweicloudsdkdli.v1.model.delete_job_auth_info_response import DeleteJobAuthInfoResponse
from huaweicloudsdkdli.v1.model.delete_queue_plan_request import DeleteQueuePlanRequest
from huaweicloudsdkdli.v1.model.delete_queue_plan_response import DeleteQueuePlanResponse
from huaweicloudsdkdli.v1.model.delete_queue_properties_request_body import DeleteQueuePropertiesRequestBody
from huaweicloudsdkdli.v1.model.delete_queue_property_request import DeleteQueuePropertyRequest
from huaweicloudsdkdli.v1.model.delete_queue_property_response import DeleteQueuePropertyResponse
from huaweicloudsdkdli.v1.model.delete_queue_request import DeleteQueueRequest
from huaweicloudsdkdli.v1.model.delete_queue_response import DeleteQueueResponse
from huaweicloudsdkdli.v1.model.delete_resource_request import DeleteResourceRequest
from huaweicloudsdkdli.v1.model.delete_resource_response import DeleteResourceResponse
from huaweicloudsdkdli.v1.model.delete_route_from_enhanced_connection_request import DeleteRouteFromEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.delete_route_from_enhanced_connection_response import DeleteRouteFromEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.delete_sql_templates_request_body import DeleteSqlTemplatesRequestBody
from huaweicloudsdkdli.v1.model.delete_table_request import DeleteTableRequest
from huaweicloudsdkdli.v1.model.delete_table_response import DeleteTableResponse
from huaweicloudsdkdli.v1.model.delete_template_resp_template import DeleteTemplateRespTemplate
from huaweicloudsdkdli.v1.model.disassociate_connection_queue_req import DisassociateConnectionQueueReq
from huaweicloudsdkdli.v1.model.disassociate_queue_from_enhanced_connection_request import DisassociateQueueFromEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.disassociate_queue_from_enhanced_connection_response import DisassociateQueueFromEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.elastic_resource_pools_response import ElasticResourcePoolsResponse
from huaweicloudsdkdli.v1.model.enhanced_connection_resource_info import EnhancedConnectionResourceInfo
from huaweicloudsdkdli.v1.model.enhanced_connections_host import EnhancedConnectionsHost
from huaweicloudsdkdli.v1.model.export_flink_job_request_body import ExportFlinkJobRequestBody
from huaweicloudsdkdli.v1.model.export_flink_jobs_request import ExportFlinkJobsRequest
from huaweicloudsdkdli.v1.model.export_flink_jobs_response import ExportFlinkJobsResponse
from huaweicloudsdkdli.v1.model.export_sql_job_result_request import ExportSqlJobResultRequest
from huaweicloudsdkdli.v1.model.export_sql_job_result_response import ExportSqlJobResultResponse
from huaweicloudsdkdli.v1.model.export_sql_result_request_body import ExportSqlResultRequestBody
from huaweicloudsdkdli.v1.model.export_table_request import ExportTableRequest
from huaweicloudsdkdli.v1.model.export_table_request_body import ExportTableRequestBody
from huaweicloudsdkdli.v1.model.export_table_response import ExportTableResponse
from huaweicloudsdkdli.v1.model.flink_job_config import FlinkJobConfig
from huaweicloudsdkdli.v1.model.flink_job_detail import FlinkJobDetail
from huaweicloudsdkdli.v1.model.flink_job_info import FlinkJobInfo
from huaweicloudsdkdli.v1.model.flink_job_list import FlinkJobList
from huaweicloudsdkdli.v1.model.flink_template import FlinkTemplate
from huaweicloudsdkdli.v1.model.flink_template_detail import FlinkTemplateDetail
from huaweicloudsdkdli.v1.model.flink_template_list import FlinkTemplateList
from huaweicloudsdkdli.v1.model.gen_stream_graph_req import GenStreamGraphReq
from huaweicloudsdkdli.v1.model.grant_data_permission_req import GrantDataPermissionReq
from huaweicloudsdkdli.v1.model.grant_data_permission_resp_privilege import GrantDataPermissionRespPrivilege
from huaweicloudsdkdli.v1.model.grant_queue_permission_req import GrantQueuePermissionReq
from huaweicloudsdkdli.v1.model.ief_events import IefEvents
from huaweicloudsdkdli.v1.model.ief_flink_job_messages_req import IefFlinkJobMessagesReq
from huaweicloudsdkdli.v1.model.ief_flink_job_status_report_req import IefFlinkJobStatusReportReq
from huaweicloudsdkdli.v1.model.ief_system_events_req import IefSystemEventsReq
from huaweicloudsdkdli.v1.model.import_flink_job_request_body import ImportFlinkJobRequestBody
from huaweicloudsdkdli.v1.model.import_flink_jobs_request import ImportFlinkJobsRequest
from huaweicloudsdkdli.v1.model.import_flink_jobs_response import ImportFlinkJobsResponse
from huaweicloudsdkdli.v1.model.import_table_request import ImportTableRequest
from huaweicloudsdkdli.v1.model.import_table_request_body import ImportTableRequestBody
from huaweicloudsdkdli.v1.model.import_table_response import ImportTableResponse
from huaweicloudsdkdli.v1.model.insert_queue_property_request_body import InsertQueuePropertyRequestBody
from huaweicloudsdkdli.v1.model.insert_queue_property_request_body_properties import InsertQueuePropertyRequestBodyProperties
from huaweicloudsdkdli.v1.model.job_map_info import JobMapInfo
from huaweicloudsdkdli.v1.model.job_template_info import JobTemplateInfo
from huaweicloudsdkdli.v1.model.jobs import Jobs
from huaweicloudsdkdli.v1.model.list_all_tables_request import ListAllTablesRequest
from huaweicloudsdkdli.v1.model.list_all_tables_response import ListAllTablesResponse
from huaweicloudsdkdli.v1.model.list_auth_info_request import ListAuthInfoRequest
from huaweicloudsdkdli.v1.model.list_auth_info_response import ListAuthInfoResponse
from huaweicloudsdkdli.v1.model.list_authorization_privileges_request import ListAuthorizationPrivilegesRequest
from huaweicloudsdkdli.v1.model.list_authorization_privileges_response import ListAuthorizationPrivilegesResponse
from huaweicloudsdkdli.v1.model.list_database_users_request import ListDatabaseUsersRequest
from huaweicloudsdkdli.v1.model.list_database_users_response import ListDatabaseUsersResponse
from huaweicloudsdkdli.v1.model.list_databases_request import ListDatabasesRequest
from huaweicloudsdkdli.v1.model.list_databases_response import ListDatabasesResponse
from huaweicloudsdkdli.v1.model.list_datasource_connections_request import ListDatasourceConnectionsRequest
from huaweicloudsdkdli.v1.model.list_datasource_connections_response import ListDatasourceConnectionsResponse
from huaweicloudsdkdli.v1.model.list_elastic_resource_pool_queues_request import ListElasticResourcePoolQueuesRequest
from huaweicloudsdkdli.v1.model.list_elastic_resource_pool_queues_response import ListElasticResourcePoolQueuesResponse
from huaweicloudsdkdli.v1.model.list_elastic_resource_pool_scale_records_request import ListElasticResourcePoolScaleRecordsRequest
from huaweicloudsdkdli.v1.model.list_elastic_resource_pool_scale_records_response import ListElasticResourcePoolScaleRecordsResponse
from huaweicloudsdkdli.v1.model.list_elastic_resource_pools_request import ListElasticResourcePoolsRequest
from huaweicloudsdkdli.v1.model.list_elastic_resource_pools_response import ListElasticResourcePoolsResponse
from huaweicloudsdkdli.v1.model.list_enhanced_connections_detail import ListEnhancedConnectionsDetail
from huaweicloudsdkdli.v1.model.list_enhanced_connections_request import ListEnhancedConnectionsRequest
from huaweicloudsdkdli.v1.model.list_enhanced_connections_response import ListEnhancedConnectionsResponse
from huaweicloudsdkdli.v1.model.list_flink_jobs_request import ListFlinkJobsRequest
from huaweicloudsdkdli.v1.model.list_flink_jobs_response import ListFlinkJobsResponse
from huaweicloudsdkdli.v1.model.list_flink_sql_job_templates_request import ListFlinkSqlJobTemplatesRequest
from huaweicloudsdkdli.v1.model.list_flink_sql_job_templates_response import ListFlinkSqlJobTemplatesResponse
from huaweicloudsdkdli.v1.model.list_global_value import ListGlobalValue
from huaweicloudsdkdli.v1.model.list_global_variables_request import ListGlobalVariablesRequest
from huaweicloudsdkdli.v1.model.list_global_variables_response import ListGlobalVariablesResponse
from huaweicloudsdkdli.v1.model.list_group_packages_resource import ListGroupPackagesResource
from huaweicloudsdkdli.v1.model.list_job_auth_infos_request import ListJobAuthInfosRequest
from huaweicloudsdkdli.v1.model.list_job_auth_infos_response import ListJobAuthInfosResponse
from huaweicloudsdkdli.v1.model.list_jobs_jobs import ListJobsJobs
from huaweicloudsdkdli.v1.model.list_queue_plans_request import ListQueuePlansRequest
from huaweicloudsdkdli.v1.model.list_queue_plans_response import ListQueuePlansResponse
from huaweicloudsdkdli.v1.model.list_queue_properties_request import ListQueuePropertiesRequest
from huaweicloudsdkdli.v1.model.list_queue_properties_response import ListQueuePropertiesResponse
from huaweicloudsdkdli.v1.model.list_queue_property_resp_properties import ListQueuePropertyRespProperties
from huaweicloudsdkdli.v1.model.list_queue_users_request import ListQueueUsersRequest
from huaweicloudsdkdli.v1.model.list_queue_users_response import ListQueueUsersResponse
from huaweicloudsdkdli.v1.model.list_queues_request import ListQueuesRequest
from huaweicloudsdkdli.v1.model.list_queues_response import ListQueuesResponse
from huaweicloudsdkdli.v1.model.list_resource_packages_resp_moudle import ListResourcePackagesRespMoudle
from huaweicloudsdkdli.v1.model.list_resources_request import ListResourcesRequest
from huaweicloudsdkdli.v1.model.list_resources_response import ListResourcesResponse
from huaweicloudsdkdli.v1.model.list_spark_job_templates_request import ListSparkJobTemplatesRequest
from huaweicloudsdkdli.v1.model.list_spark_job_templates_response import ListSparkJobTemplatesResponse
from huaweicloudsdkdli.v1.model.list_spark_jobs_request import ListSparkJobsRequest
from huaweicloudsdkdli.v1.model.list_spark_jobs_response import ListSparkJobsResponse
from huaweicloudsdkdli.v1.model.list_sql_job_templates_request import ListSqlJobTemplatesRequest
from huaweicloudsdkdli.v1.model.list_sql_job_templates_response import ListSqlJobTemplatesResponse
from huaweicloudsdkdli.v1.model.list_sql_jobs_request import ListSqlJobsRequest
from huaweicloudsdkdli.v1.model.list_sql_jobs_response import ListSqlJobsResponse
from huaweicloudsdkdli.v1.model.list_table_privileges_request import ListTablePrivilegesRequest
from huaweicloudsdkdli.v1.model.list_table_privileges_response import ListTablePrivilegesResponse
from huaweicloudsdkdli.v1.model.list_table_users_request import ListTableUsersRequest
from huaweicloudsdkdli.v1.model.list_table_users_response import ListTableUsersResponse
from huaweicloudsdkdli.v1.model.obs_buckets import ObsBuckets
from huaweicloudsdkdli.v1.model.partition_infos import PartitionInfos
from huaweicloudsdkdli.v1.model.partitions import Partitions
from huaweicloudsdkdli.v1.model.preview_sql_job_result_request import PreviewSqlJobResultRequest
from huaweicloudsdkdli.v1.model.preview_sql_job_result_response import PreviewSqlJobResultResponse
from huaweicloudsdkdli.v1.model.privilege import Privilege
from huaweicloudsdkdli.v1.model.privileges_info import PrivilegesInfo
from huaweicloudsdkdli.v1.model.project_privilege import ProjectPrivilege
from huaweicloudsdkdli.v1.model.queue_details import QueueDetails
from huaweicloudsdkdli.v1.model.queue_info import QueueInfo
from huaweicloudsdkdli.v1.model.queue_plan_entity import QueuePlanEntity
from huaweicloudsdkdli.v1.model.queue_plan_ids import QueuePlanIds
from huaweicloudsdkdli.v1.model.queue_scaling_policies_response import QueueScalingPoliciesResponse
from huaweicloudsdkdli.v1.model.queue_scaling_policy_info import QueueScalingPolicyInfo
from huaweicloudsdkdli.v1.model.register_authorized_queue_request import RegisterAuthorizedQueueRequest
from huaweicloudsdkdli.v1.model.register_authorized_queue_response import RegisterAuthorizedQueueResponse
from huaweicloudsdkdli.v1.model.register_bucket_request import RegisterBucketRequest
from huaweicloudsdkdli.v1.model.register_bucket_response import RegisterBucketResponse
from huaweicloudsdkdli.v1.model.run_authorization_action_request import RunAuthorizationActionRequest
from huaweicloudsdkdli.v1.model.run_authorization_action_response import RunAuthorizationActionResponse
from huaweicloudsdkdli.v1.model.run_ief_job_action_call_back_request import RunIefJobActionCallBackRequest
from huaweicloudsdkdli.v1.model.run_ief_job_action_call_back_response import RunIefJobActionCallBackResponse
from huaweicloudsdkdli.v1.model.run_queue_action_req import RunQueueActionReq
from huaweicloudsdkdli.v1.model.run_queue_action_request import RunQueueActionRequest
from huaweicloudsdkdli.v1.model.run_queue_action_response import RunQueueActionResponse
from huaweicloudsdkdli.v1.model.set_queue_plan_req import SetQueuePlanReq
from huaweicloudsdkdli.v1.model.show_batch_job_detail_resp import ShowBatchJobDetailResp
from huaweicloudsdkdli.v1.model.show_batch_log_request import ShowBatchLogRequest
from huaweicloudsdkdli.v1.model.show_batch_log_response import ShowBatchLogResponse
from huaweicloudsdkdli.v1.model.show_connectivity_task_request import ShowConnectivityTaskRequest
from huaweicloudsdkdli.v1.model.show_connectivity_task_response import ShowConnectivityTaskResponse
from huaweicloudsdkdli.v1.model.show_database_users_privilege import ShowDatabaseUsersPrivilege
from huaweicloudsdkdli.v1.model.show_datasource_connection_request import ShowDatasourceConnectionRequest
from huaweicloudsdkdli.v1.model.show_datasource_connection_resp import ShowDatasourceConnectionResp
from huaweicloudsdkdli.v1.model.show_datasource_connection_response import ShowDatasourceConnectionResponse
from huaweicloudsdkdli.v1.model.show_describe_table_request import ShowDescribeTableRequest
from huaweicloudsdkdli.v1.model.show_describe_table_response import ShowDescribeTableResponse
from huaweicloudsdkdli.v1.model.show_dli_agency_request import ShowDliAgencyRequest
from huaweicloudsdkdli.v1.model.show_dli_agency_response import ShowDliAgencyResponse
from huaweicloudsdkdli.v1.model.show_enhanced_connection_privilege_request import ShowEnhancedConnectionPrivilegeRequest
from huaweicloudsdkdli.v1.model.show_enhanced_connection_privilege_response import ShowEnhancedConnectionPrivilegeResponse
from huaweicloudsdkdli.v1.model.show_enhanced_connection_request import ShowEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.show_enhanced_connection_response import ShowEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.show_flink_job_execution_graph_request import ShowFlinkJobExecutionGraphRequest
from huaweicloudsdkdli.v1.model.show_flink_job_execution_graph_response import ShowFlinkJobExecutionGraphResponse
from huaweicloudsdkdli.v1.model.show_flink_job_request import ShowFlinkJobRequest
from huaweicloudsdkdli.v1.model.show_flink_job_response import ShowFlinkJobResponse
from huaweicloudsdkdli.v1.model.show_flink_metric_request import ShowFlinkMetricRequest
from huaweicloudsdkdli.v1.model.show_flink_metric_response import ShowFlinkMetricResponse
from huaweicloudsdkdli.v1.model.show_job_monitor_info_req import ShowJobMonitorInfoReq
from huaweicloudsdkdli.v1.model.show_job_monitor_info_resp_payload import ShowJobMonitorInfoRespPayload
from huaweicloudsdkdli.v1.model.show_job_monitor_info_resp_payload_jobs import ShowJobMonitorInfoRespPayloadJobs
from huaweicloudsdkdli.v1.model.show_job_monitor_info_resp_payload_jobs_metrics import ShowJobMonitorInfoRespPayloadJobsMetrics
from huaweicloudsdkdli.v1.model.show_job_monitor_info_resp_payload_jobs_metrics_sources import ShowJobMonitorInfoRespPayloadJobsMetricsSources
from huaweicloudsdkdli.v1.model.show_partitions_request import ShowPartitionsRequest
from huaweicloudsdkdli.v1.model.show_partitions_response import ShowPartitionsResponse
from huaweicloudsdkdli.v1.model.show_queue_request import ShowQueueRequest
from huaweicloudsdkdli.v1.model.show_queue_response import ShowQueueResponse
from huaweicloudsdkdli.v1.model.show_quota_properties_body import ShowQuotaPropertiesBody
from huaweicloudsdkdli.v1.model.show_quota_request import ShowQuotaRequest
from huaweicloudsdkdli.v1.model.show_quota_response import ShowQuotaResponse
from huaweicloudsdkdli.v1.model.show_quota_response_body_quotas import ShowQuotaResponseBodyQuotas
from huaweicloudsdkdli.v1.model.show_resource_info_request import ShowResourceInfoRequest
from huaweicloudsdkdli.v1.model.show_resource_info_response import ShowResourceInfoResponse
from huaweicloudsdkdli.v1.model.show_spark_job_request import ShowSparkJobRequest
from huaweicloudsdkdli.v1.model.show_spark_job_response import ShowSparkJobResponse
from huaweicloudsdkdli.v1.model.show_spark_job_status_request import ShowSparkJobStatusRequest
from huaweicloudsdkdli.v1.model.show_spark_job_status_response import ShowSparkJobStatusResponse
from huaweicloudsdkdli.v1.model.show_spark_job_template_request import ShowSparkJobTemplateRequest
from huaweicloudsdkdli.v1.model.show_spark_job_template_response import ShowSparkJobTemplateResponse
from huaweicloudsdkdli.v1.model.show_sql_job_detail_request import ShowSqlJobDetailRequest
from huaweicloudsdkdli.v1.model.show_sql_job_detail_response import ShowSqlJobDetailResponse
from huaweicloudsdkdli.v1.model.show_sql_job_progress_request import ShowSqlJobProgressRequest
from huaweicloudsdkdli.v1.model.show_sql_job_progress_response import ShowSqlJobProgressResponse
from huaweicloudsdkdli.v1.model.show_sql_job_status_request import ShowSqlJobStatusRequest
from huaweicloudsdkdli.v1.model.show_sql_job_status_response import ShowSqlJobStatusResponse
from huaweicloudsdkdli.v1.model.show_sql_sample_templates_request import ShowSqlSampleTemplatesRequest
from huaweicloudsdkdli.v1.model.show_sql_sample_templates_response import ShowSqlSampleTemplatesResponse
from huaweicloudsdkdli.v1.model.show_stream_job_list_job_config import ShowStreamJobListJobConfig
from huaweicloudsdkdli.v1.model.show_table_content_request import ShowTableContentRequest
from huaweicloudsdkdli.v1.model.show_table_content_response import ShowTableContentResponse
from huaweicloudsdkdli.v1.model.show_table_users_resp_privilege import ShowTableUsersRespPrivilege
from huaweicloudsdkdli.v1.model.sqls_resp import SqlsResp
from huaweicloudsdkdli.v1.model.sqls_sample_resp import SqlsSampleResp
from huaweicloudsdkdli.v1.model.state import State
from huaweicloudsdkdli.v1.model.stop_flink_jobs_request import StopFlinkJobsRequest
from huaweicloudsdkdli.v1.model.stop_flink_jobs_request_body import StopFlinkJobsRequestBody
from huaweicloudsdkdli.v1.model.stop_flink_jobs_response import StopFlinkJobsResponse
from huaweicloudsdkdli.v1.model.stream_graph_info import StreamGraphInfo
from huaweicloudsdkdli.v1.model.sub_job_datas import SubJobDatas
from huaweicloudsdkdli.v1.model.table import Table
from huaweicloudsdkdli.v1.model.table_user_permissions_resp_privilege import TableUserPermissionsRespPrivilege
from huaweicloudsdkdli.v1.model.tms_tag import TmsTag
from huaweicloudsdkdli.v1.model.tms_tag_entity import TmsTagEntity
from huaweicloudsdkdli.v1.model.update_auth_info_request import UpdateAuthInfoRequest
from huaweicloudsdkdli.v1.model.update_auth_info_request_body import UpdateAuthInfoRequestBody
from huaweicloudsdkdli.v1.model.update_auth_info_response import UpdateAuthInfoResponse
from huaweicloudsdkdli.v1.model.update_database_owner_request import UpdateDatabaseOwnerRequest
from huaweicloudsdkdli.v1.model.update_database_owner_response import UpdateDatabaseOwnerResponse
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_queue_request import UpdateElasticResourcePoolQueueRequest
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_queue_response import UpdateElasticResourcePoolQueueResponse
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_queue_scaling_policy_info import UpdateElasticResourcePoolQueueScalingPolicyInfo
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_request import UpdateElasticResourcePoolRequest
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_request_body import UpdateElasticResourcePoolRequestBody
from huaweicloudsdkdli.v1.model.update_elastic_resource_pool_response import UpdateElasticResourcePoolResponse
from huaweicloudsdkdli.v1.model.update_enhanced_connection_request import UpdateEnhancedConnectionRequest
from huaweicloudsdkdli.v1.model.update_enhanced_connection_response import UpdateEnhancedConnectionResponse
from huaweicloudsdkdli.v1.model.update_flink_jar_job_request import UpdateFlinkJarJobRequest
from huaweicloudsdkdli.v1.model.update_flink_jar_job_response import UpdateFlinkJarJobResponse
from huaweicloudsdkdli.v1.model.update_flink_jar_request_body import UpdateFlinkJarRequestBody
from huaweicloudsdkdli.v1.model.update_flink_sql_job_request import UpdateFlinkSqlJobRequest
from huaweicloudsdkdli.v1.model.update_flink_sql_job_response import UpdateFlinkSqlJobResponse
from huaweicloudsdkdli.v1.model.update_flink_sql_job_template_request import UpdateFlinkSqlJobTemplateRequest
from huaweicloudsdkdli.v1.model.update_flink_sql_job_template_response import UpdateFlinkSqlJobTemplateResponse
from huaweicloudsdkdli.v1.model.update_flink_sql_request_body import UpdateFlinkSqlRequestBody
from huaweicloudsdkdli.v1.model.update_flink_template_request_body import UpdateFlinkTemplateRequestBody
from huaweicloudsdkdli.v1.model.update_global_value_req import UpdateGlobalValueReq
from huaweicloudsdkdli.v1.model.update_global_variable_request import UpdateGlobalVariableRequest
from huaweicloudsdkdli.v1.model.update_global_variable_response import UpdateGlobalVariableResponse
from huaweicloudsdkdli.v1.model.update_group_or_resource_owner_request import UpdateGroupOrResourceOwnerRequest
from huaweicloudsdkdli.v1.model.update_group_or_resource_owner_response import UpdateGroupOrResourceOwnerResponse
from huaweicloudsdkdli.v1.model.update_host_massage_req import UpdateHostMassageReq
from huaweicloudsdkdli.v1.model.update_job_auth_info_request import UpdateJobAuthInfoRequest
from huaweicloudsdkdli.v1.model.update_job_auth_info_request_body import UpdateJobAuthInfoRequestBody
from huaweicloudsdkdli.v1.model.update_job_auth_info_response import UpdateJobAuthInfoResponse
from huaweicloudsdkdli.v1.model.update_job_resp_job import UpdateJobRespJob
from huaweicloudsdkdli.v1.model.update_job_templates_request_body import UpdateJobTemplatesRequestBody
from huaweicloudsdkdli.v1.model.update_owner_request_body import UpdateOwnerRequestBody
from huaweicloudsdkdli.v1.model.update_queue_cidr_req import UpdateQueueCidrReq
from huaweicloudsdkdli.v1.model.update_queue_cidr_request import UpdateQueueCidrRequest
from huaweicloudsdkdli.v1.model.update_queue_cidr_response import UpdateQueueCidrResponse
from huaweicloudsdkdli.v1.model.update_queue_property_request import UpdateQueuePropertyRequest
from huaweicloudsdkdli.v1.model.update_queue_property_request_body import UpdateQueuePropertyRequestBody
from huaweicloudsdkdli.v1.model.update_queue_property_request_body_properties import UpdateQueuePropertyRequestBodyProperties
from huaweicloudsdkdli.v1.model.update_queue_property_response import UpdateQueuePropertyResponse
from huaweicloudsdkdli.v1.model.update_resource_owner import UpdateResourceOwner
from huaweicloudsdkdli.v1.model.update_spark_job_template_request import UpdateSparkJobTemplateRequest
from huaweicloudsdkdli.v1.model.update_spark_job_template_response import UpdateSparkJobTemplateResponse
from huaweicloudsdkdli.v1.model.update_sql_job_template_request import UpdateSqlJobTemplateRequest
from huaweicloudsdkdli.v1.model.update_sql_job_template_response import UpdateSqlJobTemplateResponse
from huaweicloudsdkdli.v1.model.update_sql_templates_request_body import UpdateSqlTemplatesRequestBody
from huaweicloudsdkdli.v1.model.update_table_owner_request import UpdateTableOwnerRequest
from huaweicloudsdkdli.v1.model.update_table_owner_response import UpdateTableOwnerResponse
from huaweicloudsdkdli.v1.model.upload_files_request import UploadFilesRequest
from huaweicloudsdkdli.v1.model.upload_files_response import UploadFilesResponse
from huaweicloudsdkdli.v1.model.upload_group_package_req import UploadGroupPackageReq
from huaweicloudsdkdli.v1.model.upload_jars_request import UploadJarsRequest
from huaweicloudsdkdli.v1.model.upload_jars_response import UploadJarsResponse
from huaweicloudsdkdli.v1.model.upload_package_group_details_resp import UploadPackageGroupDetailsResp
from huaweicloudsdkdli.v1.model.upload_package_group_req import UploadPackageGroupReq
from huaweicloudsdkdli.v1.model.upload_python_files_request import UploadPythonFilesRequest
from huaweicloudsdkdli.v1.model.upload_python_files_response import UploadPythonFilesResponse
from huaweicloudsdkdli.v1.model.upload_resources_request import UploadResourcesRequest
from huaweicloudsdkdli.v1.model.upload_resources_response import UploadResourcesResponse
from huaweicloudsdkdli.v1.model.verity_connectivity_req import VerityConnectivityReq

