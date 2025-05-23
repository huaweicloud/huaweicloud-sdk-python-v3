# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkosm.v2.model.accessory_json_format_req import AccessoryJsonFormatReq
from huaweicloudsdkosm.v2.model.accessory_limit_vo import AccessoryLimitVo
from huaweicloudsdkosm.v2.model.accessory_url import AccessoryUrl
from huaweicloudsdkosm.v2.model.agency_v2 import AgencyV2
from huaweicloudsdkosm.v2.model.agree_tenant_authorization_v2_req import AgreeTenantAuthorizationV2Req
from huaweicloudsdkosm.v2.model.agreement_vo import AgreementVO
from huaweicloudsdkosm.v2.model.answer import Answer
from huaweicloudsdkosm.v2.model.answer_detail import AnswerDetail
from huaweicloudsdkosm.v2.model.answer_info import AnswerInfo
from huaweicloudsdkosm.v2.model.answer_qa_pair import AnswerQaPair
from huaweicloudsdkosm.v2.model.area_code_simple_info_v2 import AreaCodeSimpleInfoV2
from huaweicloudsdkosm.v2.model.article import Article
from huaweicloudsdkosm.v2.model.ask_question_req import AskQuestionReq
from huaweicloudsdkosm.v2.model.case_label_info import CaseLabelInfo
from huaweicloudsdkosm.v2.model.case_query_label import CaseQueryLabel
from huaweicloudsdkosm.v2.model.case_realtion_info import CaseRealtionInfo
from huaweicloudsdkosm.v2.model.cbs_flow_entry import CbsFlowEntry
from huaweicloudsdkosm.v2.model.check_hosts_request import CheckHostsRequest
from huaweicloudsdkosm.v2.model.check_hosts_response import CheckHostsResponse
from huaweicloudsdkosm.v2.model.check_need_verify_request import CheckNeedVerifyRequest
from huaweicloudsdkosm.v2.model.check_need_verify_response import CheckNeedVerifyResponse
from huaweicloudsdkosm.v2.model.check_verify_codes_request import CheckVerifyCodesRequest
from huaweicloudsdkosm.v2.model.check_verify_codes_response import CheckVerifyCodesResponse
from huaweicloudsdkosm.v2.model.common_param_v2 import CommonParamV2
from huaweicloudsdkosm.v2.model.confirm_authorizations_request import ConfirmAuthorizationsRequest
from huaweicloudsdkosm.v2.model.confirm_authorizations_response import ConfirmAuthorizationsResponse
from huaweicloudsdkosm.v2.model.contact_v2 import ContactV2
from huaweicloudsdkosm.v2.model.contact_way_info_v2 import ContactWayInfoV2
from huaweicloudsdkosm.v2.model.create_and_delete_privilege_req import CreateAndDeletePrivilegeReq
from huaweicloudsdkosm.v2.model.create_ask_question_request import CreateAskQuestionRequest
from huaweicloudsdkosm.v2.model.create_ask_question_response import CreateAskQuestionResponse
from huaweicloudsdkosm.v2.model.create_case_extends_param_request import CreateCaseExtendsParamRequest
from huaweicloudsdkosm.v2.model.create_case_extends_param_response import CreateCaseExtendsParamResponse
from huaweicloudsdkosm.v2.model.create_case_labels_request import CreateCaseLabelsRequest
from huaweicloudsdkosm.v2.model.create_case_labels_response import CreateCaseLabelsResponse
from huaweicloudsdkosm.v2.model.create_cases_request import CreateCasesRequest
from huaweicloudsdkosm.v2.model.create_cases_response import CreateCasesResponse
from huaweicloudsdkosm.v2.model.create_diagnose_feedback_request import CreateDiagnoseFeedbackRequest
from huaweicloudsdkosm.v2.model.create_diagnose_feedback_response import CreateDiagnoseFeedbackResponse
from huaweicloudsdkosm.v2.model.create_diagnose_job_request import CreateDiagnoseJobRequest
from huaweicloudsdkosm.v2.model.create_diagnose_job_response import CreateDiagnoseJobResponse
from huaweicloudsdkosm.v2.model.create_evaluate_request import CreateEvaluateRequest
from huaweicloudsdkosm.v2.model.create_evaluate_response import CreateEvaluateResponse
from huaweicloudsdkosm.v2.model.create_feedback_req import CreateFeedbackReq
from huaweicloudsdkosm.v2.model.create_feedback_request import CreateFeedbackRequest
from huaweicloudsdkosm.v2.model.create_feedback_response import CreateFeedbackResponse
from huaweicloudsdkosm.v2.model.create_feedback_v2_req import CreateFeedbackV2Req
from huaweicloudsdkosm.v2.model.create_labels_req import CreateLabelsReq
from huaweicloudsdkosm.v2.model.create_labels_request import CreateLabelsRequest
from huaweicloudsdkosm.v2.model.create_labels_response import CreateLabelsResponse
from huaweicloudsdkosm.v2.model.create_message_do_v2 import CreateMessageDoV2
from huaweicloudsdkosm.v2.model.create_message_v2_req import CreateMessageV2Req
from huaweicloudsdkosm.v2.model.create_messages_request import CreateMessagesRequest
from huaweicloudsdkosm.v2.model.create_messages_response import CreateMessagesResponse
from huaweicloudsdkosm.v2.model.create_order_incident_v2_req import CreateOrderIncidentV2Req
from huaweicloudsdkosm.v2.model.create_privileges_request import CreatePrivilegesRequest
from huaweicloudsdkosm.v2.model.create_privileges_response import CreatePrivilegesResponse
from huaweicloudsdkosm.v2.model.create_qa_ask_request import CreateQaAskRequest
from huaweicloudsdkosm.v2.model.create_qa_ask_response import CreateQaAskResponse
from huaweicloudsdkosm.v2.model.create_qa_feedbacks_request import CreateQaFeedbacksRequest
from huaweicloudsdkosm.v2.model.create_qa_feedbacks_response import CreateQaFeedbacksResponse
from huaweicloudsdkosm.v2.model.create_question_in_session_request import CreateQuestionInSessionRequest
from huaweicloudsdkosm.v2.model.create_question_in_session_response import CreateQuestionInSessionResponse
from huaweicloudsdkosm.v2.model.create_relations_req import CreateRelationsReq
from huaweicloudsdkosm.v2.model.create_relations_request import CreateRelationsRequest
from huaweicloudsdkosm.v2.model.create_relations_response import CreateRelationsResponse
from huaweicloudsdkosm.v2.model.create_score_v2_req import CreateScoreV2Req
from huaweicloudsdkosm.v2.model.create_scores_request import CreateScoresRequest
from huaweicloudsdkosm.v2.model.create_scores_response import CreateScoresResponse
from huaweicloudsdkosm.v2.model.create_session_request import CreateSessionRequest
from huaweicloudsdkosm.v2.model.create_session_response import CreateSessionResponse
from huaweicloudsdkosm.v2.model.data_center_v2_do import DataCenterV2Do
from huaweicloudsdkosm.v2.model.delete_accessories_request import DeleteAccessoriesRequest
from huaweicloudsdkosm.v2.model.delete_accessories_response import DeleteAccessoriesResponse
from huaweicloudsdkosm.v2.model.delete_case_labels_request import DeleteCaseLabelsRequest
from huaweicloudsdkosm.v2.model.delete_case_labels_response import DeleteCaseLabelsResponse
from huaweicloudsdkosm.v2.model.delete_labels_request import DeleteLabelsRequest
from huaweicloudsdkosm.v2.model.delete_labels_response import DeleteLabelsResponse
from huaweicloudsdkosm.v2.model.delete_relation_request import DeleteRelationRequest
from huaweicloudsdkosm.v2.model.delete_relation_response import DeleteRelationResponse
from huaweicloudsdkosm.v2.model.delete_relations_req import DeleteRelationsReq
from huaweicloudsdkosm.v2.model.diagnose_record_vo import DiagnoseRecordVo
from huaweicloudsdkosm.v2.model.diagnose_resource_vo import DiagnoseResourceVo
from huaweicloudsdkosm.v2.model.download_accessories_request import DownloadAccessoriesRequest
from huaweicloudsdkosm.v2.model.download_accessories_response import DownloadAccessoriesResponse
from huaweicloudsdkosm.v2.model.download_cases_request import DownloadCasesRequest
from huaweicloudsdkosm.v2.model.download_cases_response import DownloadCasesResponse
from huaweicloudsdkosm.v2.model.download_images_request import DownloadImagesRequest
from huaweicloudsdkosm.v2.model.download_images_response import DownloadImagesResponse
from huaweicloudsdkosm.v2.model.evaluate_request_req import EvaluateRequestReq
from huaweicloudsdkosm.v2.model.extend_question import ExtendQuestion
from huaweicloudsdkosm.v2.model.extends_param_v2 import ExtendsParamV2
from huaweicloudsdkosm.v2.model.feedback_option import FeedbackOption
from huaweicloudsdkosm.v2.model.file_operate_log import FileOperateLog
from huaweicloudsdkosm.v2.model.im_status_v2 import ImStatusV2
from huaweicloudsdkosm.v2.model.im_unread_v2 import ImUnreadV2
from huaweicloudsdkosm.v2.model.incident_detail_ext_info_v2 import IncidentDetailExtInfoV2
from huaweicloudsdkosm.v2.model.incident_detail_info_v2 import IncidentDetailInfoV2
from huaweicloudsdkosm.v2.model.incident_info import IncidentInfo
from huaweicloudsdkosm.v2.model.incident_info_v2 import IncidentInfoV2
from huaweicloudsdkosm.v2.model.incident_message_v2 import IncidentMessageV2
from huaweicloudsdkosm.v2.model.incident_operate_log_v2 import IncidentOperateLogV2
from huaweicloudsdkosm.v2.model.incident_order_auth_detail_info_v2 import IncidentOrderAuthDetailInfoV2
from huaweicloudsdkosm.v2.model.incident_order_auth_v2 import IncidentOrderAuthV2
from huaweicloudsdkosm.v2.model.incident_order_cc_email_info_v2 import IncidentOrderCCEmailInfoV2
from huaweicloudsdkosm.v2.model.incident_product_category_v2 import IncidentProductCategoryV2
from huaweicloudsdkosm.v2.model.incident_satisfaction_v2_do import IncidentSatisfactionV2Do
from huaweicloudsdkosm.v2.model.incident_status_count import IncidentStatusCount
from huaweicloudsdkosm.v2.model.incident_sub_type_v2_do import IncidentSubTypeV2Do
from huaweicloudsdkosm.v2.model.incident_temp_v2 import IncidentTempV2
from huaweicloudsdkosm.v2.model.intellectual_property_v2 import IntellectualPropertyV2
from huaweicloudsdkosm.v2.model.item_result_detail_vo import ItemResultDetailVo
from huaweicloudsdkosm.v2.model.item_result_vo import ItemResultVo
from huaweicloudsdkosm.v2.model.label_info import LabelInfo
from huaweicloudsdkosm.v2.model.lang_result import LangResult
from huaweicloudsdkosm.v2.model.list_accessory_access_urls_request import ListAccessoryAccessUrlsRequest
from huaweicloudsdkosm.v2.model.list_accessory_access_urls_response import ListAccessoryAccessUrlsResponse
from huaweicloudsdkosm.v2.model.list_agencies_request import ListAgenciesRequest
from huaweicloudsdkosm.v2.model.list_agencies_response import ListAgenciesResponse
from huaweicloudsdkosm.v2.model.list_area_codes_request import ListAreaCodesRequest
from huaweicloudsdkosm.v2.model.list_area_codes_response import ListAreaCodesResponse
from huaweicloudsdkosm.v2.model.list_articles_request import ListArticlesRequest
from huaweicloudsdkosm.v2.model.list_articles_response import ListArticlesResponse
from huaweicloudsdkosm.v2.model.list_authorizations_request import ListAuthorizationsRequest
from huaweicloudsdkosm.v2.model.list_authorizations_response import ListAuthorizationsResponse
from huaweicloudsdkosm.v2.model.list_case_categories_request import ListCaseCategoriesRequest
from huaweicloudsdkosm.v2.model.list_case_categories_response import ListCaseCategoriesResponse
from huaweicloudsdkosm.v2.model.list_case_cc_emails_request import ListCaseCcEmailsRequest
from huaweicloudsdkosm.v2.model.list_case_cc_emails_response import ListCaseCcEmailsResponse
from huaweicloudsdkosm.v2.model.list_case_counts_request import ListCaseCountsRequest
from huaweicloudsdkosm.v2.model.list_case_counts_response import ListCaseCountsResponse
from huaweicloudsdkosm.v2.model.list_case_labels_request import ListCaseLabelsRequest
from huaweicloudsdkosm.v2.model.list_case_labels_response import ListCaseLabelsResponse
from huaweicloudsdkosm.v2.model.list_case_limits_request import ListCaseLimitsRequest
from huaweicloudsdkosm.v2.model.list_case_limits_response import ListCaseLimitsResponse
from huaweicloudsdkosm.v2.model.list_case_operate_logs_request import ListCaseOperateLogsRequest
from huaweicloudsdkosm.v2.model.list_case_operate_logs_response import ListCaseOperateLogsResponse
from huaweicloudsdkosm.v2.model.list_case_quotas_request import ListCaseQuotasRequest
from huaweicloudsdkosm.v2.model.list_case_quotas_response import ListCaseQuotasResponse
from huaweicloudsdkosm.v2.model.list_case_templates_request import ListCaseTemplatesRequest
from huaweicloudsdkosm.v2.model.list_case_templates_response import ListCaseTemplatesResponse
from huaweicloudsdkosm.v2.model.list_cases_request import ListCasesRequest
from huaweicloudsdkosm.v2.model.list_cases_response import ListCasesResponse
from huaweicloudsdkosm.v2.model.list_customers_regions_request import ListCustomersRegionsRequest
from huaweicloudsdkosm.v2.model.list_customers_regions_response import ListCustomersRegionsResponse
from huaweicloudsdkosm.v2.model.list_diagnose_items_request import ListDiagnoseItemsRequest
from huaweicloudsdkosm.v2.model.list_diagnose_items_response import ListDiagnoseItemsResponse
from huaweicloudsdkosm.v2.model.list_diagnose_job_request import ListDiagnoseJobRequest
from huaweicloudsdkosm.v2.model.list_diagnose_job_response import ListDiagnoseJobResponse
from huaweicloudsdkosm.v2.model.list_diagnose_records_request import ListDiagnoseRecordsRequest
from huaweicloudsdkosm.v2.model.list_diagnose_records_response import ListDiagnoseRecordsResponse
from huaweicloudsdkosm.v2.model.list_diagnose_resources_request import ListDiagnoseResourcesRequest
from huaweicloudsdkosm.v2.model.list_diagnose_resources_response import ListDiagnoseResourcesResponse
from huaweicloudsdkosm.v2.model.list_extends_params_request import ListExtendsParamsRequest
from huaweicloudsdkosm.v2.model.list_extends_params_response import ListExtendsParamsResponse
from huaweicloudsdkosm.v2.model.list_feedback_option_request import ListFeedbackOptionRequest
from huaweicloudsdkosm.v2.model.list_feedback_option_response import ListFeedbackOptionResponse
from huaweicloudsdkosm.v2.model.list_has_verified_contacts_request import ListHasVerifiedContactsRequest
from huaweicloudsdkosm.v2.model.list_has_verified_contacts_response import ListHasVerifiedContactsResponse
from huaweicloudsdkosm.v2.model.list_history_operate_logs_request import ListHistoryOperateLogsRequest
from huaweicloudsdkosm.v2.model.list_history_operate_logs_response import ListHistoryOperateLogsResponse
from huaweicloudsdkosm.v2.model.list_history_sessions_request import ListHistorySessionsRequest
from huaweicloudsdkosm.v2.model.list_history_sessions_response import ListHistorySessionsResponse
from huaweicloudsdkosm.v2.model.list_labels_request import ListLabelsRequest
from huaweicloudsdkosm.v2.model.list_labels_response import ListLabelsResponse
from huaweicloudsdkosm.v2.model.list_messages_request import ListMessagesRequest
from huaweicloudsdkosm.v2.model.list_messages_response import ListMessagesResponse
from huaweicloudsdkosm.v2.model.list_more_instant_messages_request import ListMoreInstantMessagesRequest
from huaweicloudsdkosm.v2.model.list_more_instant_messages_response import ListMoreInstantMessagesResponse
from huaweicloudsdkosm.v2.model.list_new_instant_messages_request import ListNewInstantMessagesRequest
from huaweicloudsdkosm.v2.model.list_new_instant_messages_response import ListNewInstantMessagesResponse
from huaweicloudsdkosm.v2.model.list_notices_request import ListNoticesRequest
from huaweicloudsdkosm.v2.model.list_notices_response import ListNoticesResponse
from huaweicloudsdkosm.v2.model.list_order_incident_request import ListOrderIncidentRequest
from huaweicloudsdkosm.v2.model.list_order_incident_response import ListOrderIncidentResponse
from huaweicloudsdkosm.v2.model.list_privileges_request import ListPrivilegesRequest
from huaweicloudsdkosm.v2.model.list_privileges_response import ListPrivilegesResponse
from huaweicloudsdkosm.v2.model.list_problem_types_request import ListProblemTypesRequest
from huaweicloudsdkosm.v2.model.list_problem_types_response import ListProblemTypesResponse
from huaweicloudsdkosm.v2.model.list_product_categories_request import ListProductCategoriesRequest
from huaweicloudsdkosm.v2.model.list_product_categories_response import ListProductCategoriesResponse
from huaweicloudsdkosm.v2.model.list_recommend_words_request import ListRecommendWordsRequest
from huaweicloudsdkosm.v2.model.list_recommend_words_response import ListRecommendWordsResponse
from huaweicloudsdkosm.v2.model.list_regions_request import ListRegionsRequest
from huaweicloudsdkosm.v2.model.list_regions_response import ListRegionsResponse
from huaweicloudsdkosm.v2.model.list_relation_request import ListRelationRequest
from huaweicloudsdkosm.v2.model.list_relation_response import ListRelationResponse
from huaweicloudsdkosm.v2.model.list_satisfaction_dimensions_request import ListSatisfactionDimensionsRequest
from huaweicloudsdkosm.v2.model.list_satisfaction_dimensions_response import ListSatisfactionDimensionsResponse
from huaweicloudsdkosm.v2.model.list_severities_request import ListSeveritiesRequest
from huaweicloudsdkosm.v2.model.list_severities_response import ListSeveritiesResponse
from huaweicloudsdkosm.v2.model.list_sub_customers_request import ListSubCustomersRequest
from huaweicloudsdkosm.v2.model.list_sub_customers_response import ListSubCustomersResponse
from huaweicloudsdkosm.v2.model.list_tools_request import ListToolsRequest
from huaweicloudsdkosm.v2.model.list_tools_response import ListToolsResponse
from huaweicloudsdkosm.v2.model.list_transport_histories_request import ListTransportHistoriesRequest
from huaweicloudsdkosm.v2.model.list_transport_histories_response import ListTransportHistoriesResponse
from huaweicloudsdkosm.v2.model.list_unread_new_instant_messages_request import ListUnreadNewInstantMessagesRequest
from huaweicloudsdkosm.v2.model.list_unread_new_instant_messages_response import ListUnreadNewInstantMessagesResponse
from huaweicloudsdkosm.v2.model.notice import Notice
from huaweicloudsdkosm.v2.model.operate_authorization_v2_req import OperateAuthorizationV2Req
from huaweicloudsdkosm.v2.model.operate_history_session import OperateHistorySession
from huaweicloudsdkosm.v2.model.operate_log import OperateLog
from huaweicloudsdkosm.v2.model.partners_service_info import PartnersServiceInfo
from huaweicloudsdkosm.v2.model.put_case_ext_param_req import PutCaseExtParamReq
from huaweicloudsdkosm.v2.model.qa_ask_req import QaAskReq
from huaweicloudsdkosm.v2.model.qa_feedback_req import QaFeedbackReq
from huaweicloudsdkosm.v2.model.qa_flow_hit_node_vo import QaFlowHitNodeVo
from huaweicloudsdkosm.v2.model.qa_flow_hit_result import QaFlowHitResult
from huaweicloudsdkosm.v2.model.qa_graph_answer import QaGraphAnswer
from huaweicloudsdkosm.v2.model.qa_pair import QaPair
from huaweicloudsdkosm.v2.model.qabot_answer import QabotAnswer
from huaweicloudsdkosm.v2.model.query_associated_question_req import QueryAssociatedQuestionReq
from huaweicloudsdkosm.v2.model.query_diagnose_items_req import QueryDiagnoseItemsReq
from huaweicloudsdkosm.v2.model.query_message_info_v2 import QueryMessageInfoV2
from huaweicloudsdkosm.v2.model.query_tsc_diagnose_resources_req import QueryTscDiagnoseResourcesReq
from huaweicloudsdkosm.v2.model.recommend_word import RecommendWord
from huaweicloudsdkosm.v2.model.region import Region
from huaweicloudsdkosm.v2.model.relation_theme import RelationTheme
from huaweicloudsdkosm.v2.model.relevance_qapair import RelevanceQapair
from huaweicloudsdkosm.v2.model.revoke_message_request import RevokeMessageRequest
from huaweicloudsdkosm.v2.model.revoke_message_response import RevokeMessageResponse
from huaweicloudsdkosm.v2.model.satisfaction_dimension_simple_info_v2 import SatisfactionDimensionSimpleInfoV2
from huaweicloudsdkosm.v2.model.search_articles_req import SearchArticlesReq
from huaweicloudsdkosm.v2.model.search_notices_req import SearchNoticesReq
from huaweicloudsdkosm.v2.model.search_qa_pairs_req import SearchQaPairsReq
from huaweicloudsdkosm.v2.model.search_tools_req import SearchToolsReq
from huaweicloudsdkosm.v2.model.send_verify_code_req import SendVerifyCodeReq
from huaweicloudsdkosm.v2.model.send_verify_codes_request import SendVerifyCodesRequest
from huaweicloudsdkosm.v2.model.send_verify_codes_response import SendVerifyCodesResponse
from huaweicloudsdkosm.v2.model.session_ask_question_req import SessionAskQuestionReq
from huaweicloudsdkosm.v2.model.severity_v2_do import SeverityV2Do
from huaweicloudsdkosm.v2.model.show_accessory_limits_request import ShowAccessoryLimitsRequest
from huaweicloudsdkosm.v2.model.show_accessory_limits_response import ShowAccessoryLimitsResponse
from huaweicloudsdkosm.v2.model.show_associated_questions_request import ShowAssociatedQuestionsRequest
from huaweicloudsdkosm.v2.model.show_associated_questions_response import ShowAssociatedQuestionsResponse
from huaweicloudsdkosm.v2.model.show_authorization_detail_request import ShowAuthorizationDetailRequest
from huaweicloudsdkosm.v2.model.show_authorization_detail_response import ShowAuthorizationDetailResponse
from huaweicloudsdkosm.v2.model.show_case_detail_request import ShowCaseDetailRequest
from huaweicloudsdkosm.v2.model.show_case_detail_response import ShowCaseDetailResponse
from huaweicloudsdkosm.v2.model.show_case_extends_param_request import ShowCaseExtendsParamRequest
from huaweicloudsdkosm.v2.model.show_case_extends_param_response import ShowCaseExtendsParamResponse
from huaweicloudsdkosm.v2.model.show_case_status_request import ShowCaseStatusRequest
from huaweicloudsdkosm.v2.model.show_case_status_response import ShowCaseStatusResponse
from huaweicloudsdkosm.v2.model.show_configuration_request import ShowConfigurationRequest
from huaweicloudsdkosm.v2.model.show_configuration_response import ShowConfigurationResponse
from huaweicloudsdkosm.v2.model.show_customer_privilege_policy_request import ShowCustomerPrivilegePolicyRequest
from huaweicloudsdkosm.v2.model.show_customer_privilege_policy_response import ShowCustomerPrivilegePolicyResponse
from huaweicloudsdkosm.v2.model.show_download_accessory_url_request import ShowDownloadAccessoryUrlRequest
from huaweicloudsdkosm.v2.model.show_download_accessory_url_response import ShowDownloadAccessoryUrlResponse
from huaweicloudsdkosm.v2.model.show_latest_published_agreement_request import ShowLatestPublishedAgreementRequest
from huaweicloudsdkosm.v2.model.show_latest_published_agreement_response import ShowLatestPublishedAgreementResponse
from huaweicloudsdkosm.v2.model.show_login_type_request import ShowLoginTypeRequest
from huaweicloudsdkosm.v2.model.show_login_type_response import ShowLoginTypeResponse
from huaweicloudsdkosm.v2.model.show_partners_cases_privilege_request import ShowPartnersCasesPrivilegeRequest
from huaweicloudsdkosm.v2.model.show_partners_cases_privilege_response import ShowPartnersCasesPrivilegeResponse
from huaweicloudsdkosm.v2.model.show_partners_service_info_request import ShowPartnersServiceInfoRequest
from huaweicloudsdkosm.v2.model.show_partners_service_info_response import ShowPartnersServiceInfoResponse
from huaweicloudsdkosm.v2.model.show_qa_pair_detail_request import ShowQaPairDetailRequest
from huaweicloudsdkosm.v2.model.show_qa_pair_detail_response import ShowQaPairDetailResponse
from huaweicloudsdkosm.v2.model.show_qa_pairs_request import ShowQaPairsRequest
from huaweicloudsdkosm.v2.model.show_qa_pairs_response import ShowQaPairsResponse
from huaweicloudsdkosm.v2.model.show_signed_latest_published_agreement_request import ShowSignedLatestPublishedAgreementRequest
from huaweicloudsdkosm.v2.model.show_signed_latest_published_agreement_response import ShowSignedLatestPublishedAgreementResponse
from huaweicloudsdkosm.v2.model.show_theme_request import ShowThemeRequest
from huaweicloudsdkosm.v2.model.show_theme_response import ShowThemeResponse
from huaweicloudsdkosm.v2.model.sign_agreement_req import SignAgreementReq
from huaweicloudsdkosm.v2.model.sign_published_agreement_request import SignPublishedAgreementRequest
from huaweicloudsdkosm.v2.model.sign_published_agreement_response import SignPublishedAgreementResponse
from huaweicloudsdkosm.v2.model.simple_accessory_v2 import SimpleAccessoryV2
from huaweicloudsdkosm.v2.model.simple_incident_business_type_v2 import SimpleIncidentBusinessTypeV2
from huaweicloudsdkosm.v2.model.simple_qa_pair import SimpleQaPair
from huaweicloudsdkosm.v2.model.sub_cutomer_info_v2 import SubCutomerInfoV2
from huaweicloudsdkosm.v2.model.submit_diagnose_job_req import SubmitDiagnoseJobReq
from huaweicloudsdkosm.v2.model.tenant_agree_auth_detail_v2 import TenantAgreeAuthDetailV2
from huaweicloudsdkosm.v2.model.tenant_config_v2 import TenantConfigV2
from huaweicloudsdkosm.v2.model.tool import Tool
from huaweicloudsdkosm.v2.model.update_authorizations_request import UpdateAuthorizationsRequest
from huaweicloudsdkosm.v2.model.update_authorizations_response import UpdateAuthorizationsResponse
from huaweicloudsdkosm.v2.model.update_case_contact_info_req import UpdateCaseContactInfoReq
from huaweicloudsdkosm.v2.model.update_case_contact_info_request import UpdateCaseContactInfoRequest
from huaweicloudsdkosm.v2.model.update_case_contact_info_response import UpdateCaseContactInfoResponse
from huaweicloudsdkosm.v2.model.update_cases_request import UpdateCasesRequest
from huaweicloudsdkosm.v2.model.update_cases_response import UpdateCasesResponse
from huaweicloudsdkosm.v2.model.update_labels_req import UpdateLabelsReq
from huaweicloudsdkosm.v2.model.update_labels_request import UpdateLabelsRequest
from huaweicloudsdkosm.v2.model.update_labels_response import UpdateLabelsResponse
from huaweicloudsdkosm.v2.model.update_new_instant_messages_read_request import UpdateNewInstantMessagesReadRequest
from huaweicloudsdkosm.v2.model.update_new_instant_messages_read_response import UpdateNewInstantMessagesReadResponse
from huaweicloudsdkosm.v2.model.update_unread_new_instant_msg_v2_req import UpdateUnreadNewInstantMsgV2Req
from huaweicloudsdkosm.v2.model.upload_accessory_request import UploadAccessoryRequest
from huaweicloudsdkosm.v2.model.upload_accessory_request_body import UploadAccessoryRequestBody
from huaweicloudsdkosm.v2.model.upload_accessory_response import UploadAccessoryResponse
from huaweicloudsdkosm.v2.model.upload_json_accessories_request import UploadJsonAccessoriesRequest
from huaweicloudsdkosm.v2.model.upload_json_accessories_response import UploadJsonAccessoriesResponse
from huaweicloudsdkosm.v2.model.user_instant_incident_msg_v2 import UserInstantIncidentMsgV2
from huaweicloudsdkosm.v2.model.verify_host_v2_req import VerifyHostV2Req
from huaweicloudsdkosm.v2.model.verify_verify_code_v2_req import VerifyVerifyCodeV2Req
from huaweicloudsdkosm.v2.model.work_order_operate_v2_req import WorkOrderOperateV2Req
