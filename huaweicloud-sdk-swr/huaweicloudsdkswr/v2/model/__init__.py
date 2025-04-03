# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkswr.v2.model.auth_info import AuthInfo
from huaweicloudsdkswr.v2.model.create_authorization_token_request import CreateAuthorizationTokenRequest
from huaweicloudsdkswr.v2.model.create_authorization_token_response import CreateAuthorizationTokenResponse
from huaweicloudsdkswr.v2.model.create_image_sync_repo_request import CreateImageSyncRepoRequest
from huaweicloudsdkswr.v2.model.create_image_sync_repo_request_body import CreateImageSyncRepoRequestBody
from huaweicloudsdkswr.v2.model.create_image_sync_repo_response import CreateImageSyncRepoResponse
from huaweicloudsdkswr.v2.model.create_manual_image_sync_repo_request import CreateManualImageSyncRepoRequest
from huaweicloudsdkswr.v2.model.create_manual_image_sync_repo_request_body import CreateManualImageSyncRepoRequestBody
from huaweicloudsdkswr.v2.model.create_manual_image_sync_repo_response import CreateManualImageSyncRepoResponse
from huaweicloudsdkswr.v2.model.create_namespace_auth_request import CreateNamespaceAuthRequest
from huaweicloudsdkswr.v2.model.create_namespace_auth_response import CreateNamespaceAuthResponse
from huaweicloudsdkswr.v2.model.create_namespace_request import CreateNamespaceRequest
from huaweicloudsdkswr.v2.model.create_namespace_request_body import CreateNamespaceRequestBody
from huaweicloudsdkswr.v2.model.create_namespace_response import CreateNamespaceResponse
from huaweicloudsdkswr.v2.model.create_repo_domains_request import CreateRepoDomainsRequest
from huaweicloudsdkswr.v2.model.create_repo_domains_request_body import CreateRepoDomainsRequestBody
from huaweicloudsdkswr.v2.model.create_repo_domains_response import CreateRepoDomainsResponse
from huaweicloudsdkswr.v2.model.create_repo_request import CreateRepoRequest
from huaweicloudsdkswr.v2.model.create_repo_request_body import CreateRepoRequestBody
from huaweicloudsdkswr.v2.model.create_repo_response import CreateRepoResponse
from huaweicloudsdkswr.v2.model.create_repo_tag_request import CreateRepoTagRequest
from huaweicloudsdkswr.v2.model.create_repo_tag_request_body import CreateRepoTagRequestBody
from huaweicloudsdkswr.v2.model.create_repo_tag_response import CreateRepoTagResponse
from huaweicloudsdkswr.v2.model.create_retention_request import CreateRetentionRequest
from huaweicloudsdkswr.v2.model.create_retention_request_body import CreateRetentionRequestBody
from huaweicloudsdkswr.v2.model.create_retention_response import CreateRetentionResponse
from huaweicloudsdkswr.v2.model.create_secret_request import CreateSecretRequest
from huaweicloudsdkswr.v2.model.create_secret_response import CreateSecretResponse
from huaweicloudsdkswr.v2.model.create_trigger_request import CreateTriggerRequest
from huaweicloudsdkswr.v2.model.create_trigger_request_body import CreateTriggerRequestBody
from huaweicloudsdkswr.v2.model.create_trigger_response import CreateTriggerResponse
from huaweicloudsdkswr.v2.model.create_user_repository_auth_request import CreateUserRepositoryAuthRequest
from huaweicloudsdkswr.v2.model.create_user_repository_auth_response import CreateUserRepositoryAuthResponse
from huaweicloudsdkswr.v2.model.delete_image_sync_repo_request import DeleteImageSyncRepoRequest
from huaweicloudsdkswr.v2.model.delete_image_sync_repo_request_body import DeleteImageSyncRepoRequestBody
from huaweicloudsdkswr.v2.model.delete_image_sync_repo_response import DeleteImageSyncRepoResponse
from huaweicloudsdkswr.v2.model.delete_namespace_auth_request import DeleteNamespaceAuthRequest
from huaweicloudsdkswr.v2.model.delete_namespace_auth_response import DeleteNamespaceAuthResponse
from huaweicloudsdkswr.v2.model.delete_namespaces_request import DeleteNamespacesRequest
from huaweicloudsdkswr.v2.model.delete_namespaces_response import DeleteNamespacesResponse
from huaweicloudsdkswr.v2.model.delete_repo_domains_request import DeleteRepoDomainsRequest
from huaweicloudsdkswr.v2.model.delete_repo_domains_response import DeleteRepoDomainsResponse
from huaweicloudsdkswr.v2.model.delete_repo_request import DeleteRepoRequest
from huaweicloudsdkswr.v2.model.delete_repo_response import DeleteRepoResponse
from huaweicloudsdkswr.v2.model.delete_repo_tag_request import DeleteRepoTagRequest
from huaweicloudsdkswr.v2.model.delete_repo_tag_response import DeleteRepoTagResponse
from huaweicloudsdkswr.v2.model.delete_retention_request import DeleteRetentionRequest
from huaweicloudsdkswr.v2.model.delete_retention_response import DeleteRetentionResponse
from huaweicloudsdkswr.v2.model.delete_trigger_request import DeleteTriggerRequest
from huaweicloudsdkswr.v2.model.delete_trigger_response import DeleteTriggerResponse
from huaweicloudsdkswr.v2.model.delete_user_repository_auth_request import DeleteUserRepositoryAuthRequest
from huaweicloudsdkswr.v2.model.delete_user_repository_auth_response import DeleteUserRepositoryAuthResponse
from huaweicloudsdkswr.v2.model.image_tag import ImageTag
from huaweicloudsdkswr.v2.model.link import Link
from huaweicloudsdkswr.v2.model.list_api_versions_request import ListApiVersionsRequest
from huaweicloudsdkswr.v2.model.list_api_versions_response import ListApiVersionsResponse
from huaweicloudsdkswr.v2.model.list_image_auto_sync_repos_details_request import ListImageAutoSyncReposDetailsRequest
from huaweicloudsdkswr.v2.model.list_image_auto_sync_repos_details_response import ListImageAutoSyncReposDetailsResponse
from huaweicloudsdkswr.v2.model.list_namespaces_request import ListNamespacesRequest
from huaweicloudsdkswr.v2.model.list_namespaces_response import ListNamespacesResponse
from huaweicloudsdkswr.v2.model.list_quotas_request import ListQuotasRequest
from huaweicloudsdkswr.v2.model.list_quotas_response import ListQuotasResponse
from huaweicloudsdkswr.v2.model.list_repo_domains_request import ListRepoDomainsRequest
from huaweicloudsdkswr.v2.model.list_repo_domains_response import ListRepoDomainsResponse
from huaweicloudsdkswr.v2.model.list_repos_details_request import ListReposDetailsRequest
from huaweicloudsdkswr.v2.model.list_repos_details_response import ListReposDetailsResponse
from huaweicloudsdkswr.v2.model.list_repository_tags_request import ListRepositoryTagsRequest
from huaweicloudsdkswr.v2.model.list_repository_tags_response import ListRepositoryTagsResponse
from huaweicloudsdkswr.v2.model.list_retention_histories_request import ListRetentionHistoriesRequest
from huaweicloudsdkswr.v2.model.list_retention_histories_response import ListRetentionHistoriesResponse
from huaweicloudsdkswr.v2.model.list_retentions_request import ListRetentionsRequest
from huaweicloudsdkswr.v2.model.list_retentions_response import ListRetentionsResponse
from huaweicloudsdkswr.v2.model.list_shared_repos_details_request import ListSharedReposDetailsRequest
from huaweicloudsdkswr.v2.model.list_shared_repos_details_response import ListSharedReposDetailsResponse
from huaweicloudsdkswr.v2.model.list_triggers_details_request import ListTriggersDetailsRequest
from huaweicloudsdkswr.v2.model.list_triggers_details_response import ListTriggersDetailsResponse
from huaweicloudsdkswr.v2.model.report_data import ReportData
from huaweicloudsdkswr.v2.model.retention import Retention
from huaweicloudsdkswr.v2.model.retention_log import RetentionLog
from huaweicloudsdkswr.v2.model.rule import Rule
from huaweicloudsdkswr.v2.model.show_access_domain_request import ShowAccessDomainRequest
from huaweicloudsdkswr.v2.model.show_access_domain_response import ShowAccessDomainResponse
from huaweicloudsdkswr.v2.model.show_api_version_request import ShowApiVersionRequest
from huaweicloudsdkswr.v2.model.show_api_version_response import ShowApiVersionResponse
from huaweicloudsdkswr.v2.model.show_domain_overview_request import ShowDomainOverviewRequest
from huaweicloudsdkswr.v2.model.show_domain_overview_response import ShowDomainOverviewResponse
from huaweicloudsdkswr.v2.model.show_domain_resource_reports_request import ShowDomainResourceReportsRequest
from huaweicloudsdkswr.v2.model.show_domain_resource_reports_response import ShowDomainResourceReportsResponse
from huaweicloudsdkswr.v2.model.show_namespace import ShowNamespace
from huaweicloudsdkswr.v2.model.show_namespace_auth_request import ShowNamespaceAuthRequest
from huaweicloudsdkswr.v2.model.show_namespace_auth_response import ShowNamespaceAuthResponse
from huaweicloudsdkswr.v2.model.show_namespace_request import ShowNamespaceRequest
from huaweicloudsdkswr.v2.model.show_namespace_response import ShowNamespaceResponse
from huaweicloudsdkswr.v2.model.show_quota import ShowQuota
from huaweicloudsdkswr.v2.model.show_repo_domains_response import ShowRepoDomainsResponse
from huaweicloudsdkswr.v2.model.show_repos_resp import ShowReposResp
from huaweicloudsdkswr.v2.model.show_repos_tag_resp import ShowReposTagResp
from huaweicloudsdkswr.v2.model.show_repository_request import ShowRepositoryRequest
from huaweicloudsdkswr.v2.model.show_repository_response import ShowRepositoryResponse
from huaweicloudsdkswr.v2.model.show_retention_request import ShowRetentionRequest
from huaweicloudsdkswr.v2.model.show_retention_response import ShowRetentionResponse
from huaweicloudsdkswr.v2.model.show_share_feature_gates_request import ShowShareFeatureGatesRequest
from huaweicloudsdkswr.v2.model.show_share_feature_gates_response import ShowShareFeatureGatesResponse
from huaweicloudsdkswr.v2.model.show_sync_job_request import ShowSyncJobRequest
from huaweicloudsdkswr.v2.model.show_sync_job_response import ShowSyncJobResponse
from huaweicloudsdkswr.v2.model.show_trigger_request import ShowTriggerRequest
from huaweicloudsdkswr.v2.model.show_trigger_response import ShowTriggerResponse
from huaweicloudsdkswr.v2.model.show_user_repository_auth_request import ShowUserRepositoryAuthRequest
from huaweicloudsdkswr.v2.model.show_user_repository_auth_response import ShowUserRepositoryAuthResponse
from huaweicloudsdkswr.v2.model.sync_job import SyncJob
from huaweicloudsdkswr.v2.model.sync_repo import SyncRepo
from huaweicloudsdkswr.v2.model.tag_selector import TagSelector
from huaweicloudsdkswr.v2.model.trigger import Trigger
from huaweicloudsdkswr.v2.model.trigger_histories import TriggerHistories
from huaweicloudsdkswr.v2.model.update_namespace_auth_request import UpdateNamespaceAuthRequest
from huaweicloudsdkswr.v2.model.update_namespace_auth_response import UpdateNamespaceAuthResponse
from huaweicloudsdkswr.v2.model.update_repo_domains_request import UpdateRepoDomainsRequest
from huaweicloudsdkswr.v2.model.update_repo_domains_request_body import UpdateRepoDomainsRequestBody
from huaweicloudsdkswr.v2.model.update_repo_domains_response import UpdateRepoDomainsResponse
from huaweicloudsdkswr.v2.model.update_repo_request import UpdateRepoRequest
from huaweicloudsdkswr.v2.model.update_repo_request_body import UpdateRepoRequestBody
from huaweicloudsdkswr.v2.model.update_repo_response import UpdateRepoResponse
from huaweicloudsdkswr.v2.model.update_retention_request import UpdateRetentionRequest
from huaweicloudsdkswr.v2.model.update_retention_request_body import UpdateRetentionRequestBody
from huaweicloudsdkswr.v2.model.update_retention_response import UpdateRetentionResponse
from huaweicloudsdkswr.v2.model.update_trigger_request import UpdateTriggerRequest
from huaweicloudsdkswr.v2.model.update_trigger_request_body import UpdateTriggerRequestBody
from huaweicloudsdkswr.v2.model.update_trigger_response import UpdateTriggerResponse
from huaweicloudsdkswr.v2.model.update_user_repository_auth_request import UpdateUserRepositoryAuthRequest
from huaweicloudsdkswr.v2.model.update_user_repository_auth_response import UpdateUserRepositoryAuthResponse
from huaweicloudsdkswr.v2.model.user_auth import UserAuth
from huaweicloudsdkswr.v2.model.version_detail import VersionDetail
