# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkcodehub.v3.model.add_deploy_key_request import AddDeployKeyRequest
from huaweicloudsdkcodehub.v3.model.add_deploy_key_request_body import AddDeployKeyRequestBody
from huaweicloudsdkcodehub.v3.model.add_deploy_key_response import AddDeployKeyResponse
from huaweicloudsdkcodehub.v3.model.add_deploy_key_v2_request import AddDeployKeyV2Request
from huaweicloudsdkcodehub.v3.model.add_deploy_key_v2_response import AddDeployKeyV2Response
from huaweicloudsdkcodehub.v3.model.add_hooks_request import AddHooksRequest
from huaweicloudsdkcodehub.v3.model.add_hooks_response import AddHooksResponse
from huaweicloudsdkcodehub.v3.model.add_repo_members_request import AddRepoMembersRequest
from huaweicloudsdkcodehub.v3.model.add_repo_members_response import AddRepoMembersResponse
from huaweicloudsdkcodehub.v3.model.add_ssh_key_request import AddSshKeyRequest
from huaweicloudsdkcodehub.v3.model.add_ssh_key_request_body import AddSshKeyRequestBody
from huaweicloudsdkcodehub.v3.model.add_ssh_key_response import AddSshKeyResponse
from huaweicloudsdkcodehub.v3.model.branch import Branch
from huaweicloudsdkcodehub.v3.model.branch_list import BranchList
from huaweicloudsdkcodehub.v3.model.commit import Commit
from huaweicloudsdkcodehub.v3.model.commit_action import CommitAction
from huaweicloudsdkcodehub.v3.model.commit_info import CommitInfo
from huaweicloudsdkcodehub.v3.model.commit_list import CommitList
from huaweicloudsdkcodehub.v3.model.commit_statistic import CommitStatistic
from huaweicloudsdkcodehub.v3.model.create_commit_request import CreateCommitRequest
from huaweicloudsdkcodehub.v3.model.create_commit_request_body import CreateCommitRequestBody
from huaweicloudsdkcodehub.v3.model.create_commit_response import CreateCommitResponse
from huaweicloudsdkcodehub.v3.model.create_commit_response_body import CreateCommitResponseBody
from huaweicloudsdkcodehub.v3.model.create_commit_response_body_stats import CreateCommitResponseBodyStats
from huaweicloudsdkcodehub.v3.model.create_project_and_repositories_request import CreateProjectAndRepositoriesRequest
from huaweicloudsdkcodehub.v3.model.create_project_and_repositories_response import CreateProjectAndRepositoriesResponse
from huaweicloudsdkcodehub.v3.model.create_project_andfork_repositories_request import CreateProjectAndforkRepositoriesRequest
from huaweicloudsdkcodehub.v3.model.create_project_andfork_repositories_response import CreateProjectAndforkRepositoriesResponse
from huaweicloudsdkcodehub.v3.model.create_project_repo_request import CreateProjectRepoRequest
from huaweicloudsdkcodehub.v3.model.create_repo_member_request import CreateRepoMemberRequest
from huaweicloudsdkcodehub.v3.model.create_repo_member_result import CreateRepoMemberResult
from huaweicloudsdkcodehub.v3.model.create_repo_request import CreateRepoRequest
from huaweicloudsdkcodehub.v3.model.create_repository_request import CreateRepositoryRequest
from huaweicloudsdkcodehub.v3.model.create_repository_response import CreateRepositoryResponse
from huaweicloudsdkcodehub.v3.model.delete_deploy_key_request import DeleteDeployKeyRequest
from huaweicloudsdkcodehub.v3.model.delete_deploy_key_response import DeleteDeployKeyResponse
from huaweicloudsdkcodehub.v3.model.delete_deploy_key_v2_request import DeleteDeployKeyV2Request
from huaweicloudsdkcodehub.v3.model.delete_deploy_key_v2_response import DeleteDeployKeyV2Response
from huaweicloudsdkcodehub.v3.model.delete_hooks_request import DeleteHooksRequest
from huaweicloudsdkcodehub.v3.model.delete_hooks_response import DeleteHooksResponse
from huaweicloudsdkcodehub.v3.model.delete_repo_member_request import DeleteRepoMemberRequest
from huaweicloudsdkcodehub.v3.model.delete_repo_member_response import DeleteRepoMemberResponse
from huaweicloudsdkcodehub.v3.model.delete_repository_request import DeleteRepositoryRequest
from huaweicloudsdkcodehub.v3.model.delete_repository_response import DeleteRepositoryResponse
from huaweicloudsdkcodehub.v3.model.delete_s_shkey_request import DeleteSShkeyRequest
from huaweicloudsdkcodehub.v3.model.delete_s_shkey_response import DeleteSShkeyResponse
from huaweicloudsdkcodehub.v3.model.devstar_repo_info import DevstarRepoInfo
from huaweicloudsdkcodehub.v3.model.diff_commit_info import DiffCommitInfo
from huaweicloudsdkcodehub.v3.model.empty import Empty
from huaweicloudsdkcodehub.v3.model.error import Error
from huaweicloudsdkcodehub.v3.model.external_key_message import ExternalKeyMessage
from huaweicloudsdkcodehub.v3.model.file_content_info import FileContentInfo
from huaweicloudsdkcodehub.v3.model.files_response_info import FilesResponseInfo
from huaweicloudsdkcodehub.v3.model.fork_project_repo_request import ForkProjectRepoRequest
from huaweicloudsdkcodehub.v3.model.get_all_repository_by_project_id_request import GetAllRepositoryByProjectIdRequest
from huaweicloudsdkcodehub.v3.model.get_all_repository_by_project_id_response import GetAllRepositoryByProjectIdResponse
from huaweicloudsdkcodehub.v3.model.get_product_templates_request import GetProductTemplatesRequest
from huaweicloudsdkcodehub.v3.model.get_product_templates_response import GetProductTemplatesResponse
from huaweicloudsdkcodehub.v3.model.get_repository_by_project_id_request import GetRepositoryByProjectIdRequest
from huaweicloudsdkcodehub.v3.model.get_repository_by_project_id_response import GetRepositoryByProjectIdResponse
from huaweicloudsdkcodehub.v3.model.get_templates_request import GetTemplatesRequest
from huaweicloudsdkcodehub.v3.model.get_templates_response import GetTemplatesResponse
from huaweicloudsdkcodehub.v3.model.key import Key
from huaweicloudsdkcodehub.v3.model.list_commit_statistics_request import ListCommitStatisticsRequest
from huaweicloudsdkcodehub.v3.model.list_commit_statistics_response import ListCommitStatisticsResponse
from huaweicloudsdkcodehub.v3.model.list_commits_request import ListCommitsRequest
from huaweicloudsdkcodehub.v3.model.list_commits_response import ListCommitsResponse
from huaweicloudsdkcodehub.v3.model.list_files_request import ListFilesRequest
from huaweicloudsdkcodehub.v3.model.list_files_response import ListFilesResponse
from huaweicloudsdkcodehub.v3.model.list_hooks_request import ListHooksRequest
from huaweicloudsdkcodehub.v3.model.list_hooks_response import ListHooksResponse
from huaweicloudsdkcodehub.v3.model.list_product_two_templates_request import ListProductTwoTemplatesRequest
from huaweicloudsdkcodehub.v3.model.list_product_two_templates_response import ListProductTwoTemplatesResponse
from huaweicloudsdkcodehub.v3.model.list_repo_members_request import ListRepoMembersRequest
from huaweicloudsdkcodehub.v3.model.list_repo_members_response import ListRepoMembersResponse
from huaweicloudsdkcodehub.v3.model.list_repository_status_request import ListRepositoryStatusRequest
from huaweicloudsdkcodehub.v3.model.list_repository_status_response import ListRepositoryStatusResponse
from huaweicloudsdkcodehub.v3.model.list_ssh_keys_request import ListSshKeysRequest
from huaweicloudsdkcodehub.v3.model.list_ssh_keys_response import ListSshKeysResponse
from huaweicloudsdkcodehub.v3.model.list_subfiles_request import ListSubfilesRequest
from huaweicloudsdkcodehub.v3.model.list_subfiles_response import ListSubfilesResponse
from huaweicloudsdkcodehub.v3.model.list_templates_two_request import ListTemplatesTwoRequest
from huaweicloudsdkcodehub.v3.model.list_templates_two_response import ListTemplatesTwoResponse
from huaweicloudsdkcodehub.v3.model.list_two_templates_request import ListTwoTemplatesRequest
from huaweicloudsdkcodehub.v3.model.list_two_templates_response import ListTwoTemplatesResponse
from huaweicloudsdkcodehub.v3.model.list_user_all_repositories_request import ListUserAllRepositoriesRequest
from huaweicloudsdkcodehub.v3.model.list_user_all_repositories_response import ListUserAllRepositoriesResponse
from huaweicloudsdkcodehub.v3.model.logs_tree import LogsTree
from huaweicloudsdkcodehub.v3.model.password_request import PasswordRequest
from huaweicloudsdkcodehub.v3.model.private_key_verify import PrivateKeyVerify
from huaweicloudsdkcodehub.v3.model.project_repository import ProjectRepository
from huaweicloudsdkcodehub.v3.model.public_key import PublicKey
from huaweicloudsdkcodehub.v3.model.public_key_list import PublicKeyList
from huaweicloudsdkcodehub.v3.model.repo_commit_statistics import RepoCommitStatistics
from huaweicloudsdkcodehub.v3.model.repo_daily_codeline import RepoDailyCodeline
from huaweicloudsdkcodehub.v3.model.repo_hook import RepoHook
from huaweicloudsdkcodehub.v3.model.repo_info import RepoInfo
from huaweicloudsdkcodehub.v3.model.repo_info_v2 import RepoInfoV2
from huaweicloudsdkcodehub.v3.model.repo_list_hook import RepoListHook
from huaweicloudsdkcodehub.v3.model.repo_list_info import RepoListInfo
from huaweicloudsdkcodehub.v3.model.repo_list_info_v2 import RepoListInfoV2
from huaweicloudsdkcodehub.v3.model.repo_member_info import RepoMemberInfo
from huaweicloudsdkcodehub.v3.model.repo_statistics import RepoStatistics
from huaweicloudsdkcodehub.v3.model.repo_statistics_event import RepoStatisticsEvent
from huaweicloudsdkcodehub.v3.model.repo_statistics_launch import RepoStatisticsLaunch
from huaweicloudsdkcodehub.v3.model.repository import Repository
from huaweicloudsdkcodehub.v3.model.repository_hook_request import RepositoryHookRequest
from huaweicloudsdkcodehub.v3.model.repository_member import RepositoryMember
from huaweicloudsdkcodehub.v3.model.repository_member_list import RepositoryMemberList
from huaweicloudsdkcodehub.v3.model.repository_template_vo import RepositoryTemplateVO
from huaweicloudsdkcodehub.v3.model.repository_template_vo2 import RepositoryTemplateVO2
from huaweicloudsdkcodehub.v3.model.set_repo_role_request import SetRepoRoleRequest
from huaweicloudsdkcodehub.v3.model.set_repo_role_request_body import SetRepoRoleRequestBody
from huaweicloudsdkcodehub.v3.model.set_repo_role_response import SetRepoRoleResponse
from huaweicloudsdkcodehub.v3.model.share_templates_request import ShareTemplatesRequest
from huaweicloudsdkcodehub.v3.model.share_templates_response import ShareTemplatesResponse
from huaweicloudsdkcodehub.v3.model.show_all_repository_by_two_project_id_request import ShowAllRepositoryByTwoProjectIdRequest
from huaweicloudsdkcodehub.v3.model.show_all_repository_by_two_project_id_response import ShowAllRepositoryByTwoProjectIdResponse
from huaweicloudsdkcodehub.v3.model.show_branches_by_repository_id_request import ShowBranchesByRepositoryIdRequest
from huaweicloudsdkcodehub.v3.model.show_branches_by_repository_id_response import ShowBranchesByRepositoryIdResponse
from huaweicloudsdkcodehub.v3.model.show_branches_by_two_repository_id_request import ShowBranchesByTwoRepositoryIdRequest
from huaweicloudsdkcodehub.v3.model.show_branches_by_two_repository_id_response import ShowBranchesByTwoRepositoryIdResponse
from huaweicloudsdkcodehub.v3.model.show_commits_by_branch_request import ShowCommitsByBranchRequest
from huaweicloudsdkcodehub.v3.model.show_commits_by_branch_response import ShowCommitsByBranchResponse
from huaweicloudsdkcodehub.v3.model.show_commits_by_repo_id_request import ShowCommitsByRepoIdRequest
from huaweicloudsdkcodehub.v3.model.show_commits_by_repo_id_response import ShowCommitsByRepoIdResponse
from huaweicloudsdkcodehub.v3.model.show_diff_commit_request import ShowDiffCommitRequest
from huaweicloudsdkcodehub.v3.model.show_diff_commit_response import ShowDiffCommitResponse
from huaweicloudsdkcodehub.v3.model.show_file_request import ShowFileRequest
from huaweicloudsdkcodehub.v3.model.show_file_response import ShowFileResponse
from huaweicloudsdkcodehub.v3.model.show_has_pipeline_request import ShowHasPipelineRequest
from huaweicloudsdkcodehub.v3.model.show_has_pipeline_response import ShowHasPipelineResponse
from huaweicloudsdkcodehub.v3.model.show_image_blob_request import ShowImageBlobRequest
from huaweicloudsdkcodehub.v3.model.show_image_blob_response import ShowImageBlobResponse
from huaweicloudsdkcodehub.v3.model.show_master_request import ShowMasterRequest
from huaweicloudsdkcodehub.v3.model.show_master_response import ShowMasterResponse
from huaweicloudsdkcodehub.v3.model.show_private_key_verify_request import ShowPrivateKeyVerifyRequest
from huaweicloudsdkcodehub.v3.model.show_private_key_verify_response import ShowPrivateKeyVerifyResponse
from huaweicloudsdkcodehub.v3.model.show_repo_id_request import ShowRepoIdRequest
from huaweicloudsdkcodehub.v3.model.show_repo_id_response import ShowRepoIdResponse
from huaweicloudsdkcodehub.v3.model.show_repository_archive_request import ShowRepositoryArchiveRequest
from huaweicloudsdkcodehub.v3.model.show_repository_archive_response import ShowRepositoryArchiveResponse
from huaweicloudsdkcodehub.v3.model.show_repository_by_uuid_request import ShowRepositoryByUuidRequest
from huaweicloudsdkcodehub.v3.model.show_repository_by_uuid_response import ShowRepositoryByUuidResponse
from huaweicloudsdkcodehub.v3.model.show_repository_name_exist_request import ShowRepositoryNameExistRequest
from huaweicloudsdkcodehub.v3.model.show_repository_name_exist_response import ShowRepositoryNameExistResponse
from huaweicloudsdkcodehub.v3.model.show_repository_statistics_request import ShowRepositoryStatisticsRequest
from huaweicloudsdkcodehub.v3.model.show_repository_statistics_request_body import ShowRepositoryStatisticsRequestBody
from huaweicloudsdkcodehub.v3.model.show_repository_statistics_response import ShowRepositoryStatisticsResponse
from huaweicloudsdkcodehub.v3.model.show_single_commit_request import ShowSingleCommitRequest
from huaweicloudsdkcodehub.v3.model.show_single_commit_response import ShowSingleCommitResponse
from huaweicloudsdkcodehub.v3.model.show_statistic_commit_request import ShowStatisticCommitRequest
from huaweicloudsdkcodehub.v3.model.show_statistic_commit_response import ShowStatisticCommitResponse
from huaweicloudsdkcodehub.v3.model.show_statistic_commit_v3_request import ShowStatisticCommitV3Request
from huaweicloudsdkcodehub.v3.model.show_statistic_commit_v3_response import ShowStatisticCommitV3Response
from huaweicloudsdkcodehub.v3.model.show_statistical_data_request import ShowStatisticalDataRequest
from huaweicloudsdkcodehub.v3.model.show_statistical_data_response import ShowStatisticalDataResponse
from huaweicloudsdkcodehub.v3.model.specific_commit_info import SpecificCommitInfo
from huaweicloudsdkcodehub.v3.model.specific_commit_info_last_pipeline import SpecificCommitInfoLastPipeline
from huaweicloudsdkcodehub.v3.model.specific_commit_info_stats import SpecificCommitInfoStats
from huaweicloudsdkcodehub.v3.model.tag import Tag
from huaweicloudsdkcodehub.v3.model.tag_list import TagList
from huaweicloudsdkcodehub.v3.model.template_list_info import TemplateListInfo
from huaweicloudsdkcodehub.v3.model.template_repository import TemplateRepository
from huaweicloudsdkcodehub.v3.model.template_repository_list import TemplateRepositoryList
from huaweicloudsdkcodehub.v3.model.validate_https_info_request import ValidateHttpsInfoRequest
from huaweicloudsdkcodehub.v3.model.validate_https_info_response import ValidateHttpsInfoResponse
from huaweicloudsdkcodehub.v3.model.validate_https_info_v2_request import ValidateHttpsInfoV2Request
from huaweicloudsdkcodehub.v3.model.validate_https_info_v2_response import ValidateHttpsInfoV2Response
