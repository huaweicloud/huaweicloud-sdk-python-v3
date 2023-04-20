# coding: utf-8

from __future__ import absolute_import

# import CbsClient
from huaweicloudsdkcbs.v1.cbs_client import CbsClient
from huaweicloudsdkcbs.v1.cbs_async_client import CbsAsyncClient
# import models into sdk package
from huaweicloudsdkcbs.v1.model.basic_list_resp import BasicListResp
from huaweicloudsdkcbs.v1.model.candidate_intention import CandidateIntention
from huaweicloudsdkcbs.v1.model.character import Character
from huaweicloudsdkcbs.v1.model.character_config import CharacterConfig
from huaweicloudsdkcbs.v1.model.character_dimension import CharacterDimension
from huaweicloudsdkcbs.v1.model.character_position import CharacterPosition
from huaweicloudsdkcbs.v1.model.chat_answers import ChatAnswers
from huaweicloudsdkcbs.v1.model.collect_hot_questions_request import CollectHotQuestionsRequest
from huaweicloudsdkcbs.v1.model.collect_hot_questions_response import CollectHotQuestionsResponse
from huaweicloudsdkcbs.v1.model.collect_key_words_request import CollectKeyWordsRequest
from huaweicloudsdkcbs.v1.model.collect_key_words_response import CollectKeyWordsResponse
from huaweicloudsdkcbs.v1.model.collect_reply_rates_request import CollectReplyRatesRequest
from huaweicloudsdkcbs.v1.model.collect_reply_rates_response import CollectReplyRatesResponse
from huaweicloudsdkcbs.v1.model.collect_session_stats_request import CollectSessionStatsRequest
from huaweicloudsdkcbs.v1.model.collect_session_stats_response import CollectSessionStatsResponse
from huaweicloudsdkcbs.v1.model.create_res import CreateRes
from huaweicloudsdkcbs.v1.model.create_session_request import CreateSessionRequest
from huaweicloudsdkcbs.v1.model.create_session_response import CreateSessionResponse
from huaweicloudsdkcbs.v1.model.create_video_req import CreateVideoReq
from huaweicloudsdkcbs.v1.model.current_slot import CurrentSlot
from huaweicloudsdkcbs.v1.model.delete_session_request import DeleteSessionRequest
from huaweicloudsdkcbs.v1.model.delete_session_response import DeleteSessionResponse
from huaweicloudsdkcbs.v1.model.doc_bot_answers import DocBotAnswers
from huaweicloudsdkcbs.v1.model.doc_query_answer_detail import DocQueryAnswerDetail
from huaweicloudsdkcbs.v1.model.execute_compose_video_ondemand_request import ExecuteComposeVideoOndemandRequest
from huaweicloudsdkcbs.v1.model.execute_compose_video_ondemand_response import ExecuteComposeVideoOndemandResponse
from huaweicloudsdkcbs.v1.model.execute_compose_video_request import ExecuteComposeVideoRequest
from huaweicloudsdkcbs.v1.model.execute_compose_video_response import ExecuteComposeVideoResponse
from huaweicloudsdkcbs.v1.model.execute_create_video_request import ExecuteCreateVideoRequest
from huaweicloudsdkcbs.v1.model.execute_create_video_response import ExecuteCreateVideoResponse
from huaweicloudsdkcbs.v1.model.execute_delete_video_by_id_request import ExecuteDeleteVideoByIdRequest
from huaweicloudsdkcbs.v1.model.execute_delete_video_by_id_response import ExecuteDeleteVideoByIdResponse
from huaweicloudsdkcbs.v1.model.execute_deleteimage_by_id_request import ExecuteDeleteimageByIdRequest
from huaweicloudsdkcbs.v1.model.execute_deleteimage_by_id_response import ExecuteDeleteimageByIdResponse
from huaweicloudsdkcbs.v1.model.execute_get_character_info_by_id_request import ExecuteGetCharacterInfoByIdRequest
from huaweicloudsdkcbs.v1.model.execute_get_character_info_by_id_response import ExecuteGetCharacterInfoByIdResponse
from huaweicloudsdkcbs.v1.model.execute_get_characters_request import ExecuteGetCharactersRequest
from huaweicloudsdkcbs.v1.model.execute_get_characters_response import ExecuteGetCharactersResponse
from huaweicloudsdkcbs.v1.model.execute_get_frams_list_by_images_id_request import ExecuteGetFramsListByImagesIdRequest
from huaweicloudsdkcbs.v1.model.execute_get_frams_list_by_images_id_response import ExecuteGetFramsListByImagesIdResponse
from huaweicloudsdkcbs.v1.model.execute_get_images_list_request import ExecuteGetImagesListRequest
from huaweicloudsdkcbs.v1.model.execute_get_images_list_response import ExecuteGetImagesListResponse
from huaweicloudsdkcbs.v1.model.execute_get_video_info_by_id_request import ExecuteGetVideoInfoByIdRequest
from huaweicloudsdkcbs.v1.model.execute_get_video_info_by_id_response import ExecuteGetVideoInfoByIdResponse
from huaweicloudsdkcbs.v1.model.execute_get_videos_list_request import ExecuteGetVideosListRequest
from huaweicloudsdkcbs.v1.model.execute_get_videos_list_response import ExecuteGetVideosListResponse
from huaweicloudsdkcbs.v1.model.execute_post_create_images_request import ExecutePostCreateImagesRequest
from huaweicloudsdkcbs.v1.model.execute_post_create_images_response import ExecutePostCreateImagesResponse
from huaweicloudsdkcbs.v1.model.execute_qa_chat_request import ExecuteQaChatRequest
from huaweicloudsdkcbs.v1.model.execute_qa_chat_response import ExecuteQaChatResponse
from huaweicloudsdkcbs.v1.model.execute_session_request import ExecuteSessionRequest
from huaweicloudsdkcbs.v1.model.execute_session_response import ExecuteSessionResponse
from huaweicloudsdkcbs.v1.model.execute_update_image_name_request import ExecuteUpdateImageNameRequest
from huaweicloudsdkcbs.v1.model.execute_update_image_name_response import ExecuteUpdateImageNameResponse
from huaweicloudsdkcbs.v1.model.execute_update_video_by_id_request import ExecuteUpdateVideoByIdRequest
from huaweicloudsdkcbs.v1.model.execute_update_video_by_id_response import ExecuteUpdateVideoByIdResponse
from huaweicloudsdkcbs.v1.model.execute_update_video_info_by_id_request import ExecuteUpdateVideoInfoByIdRequest
from huaweicloudsdkcbs.v1.model.execute_update_video_info_by_id_response import ExecuteUpdateVideoInfoByIdResponse
from huaweicloudsdkcbs.v1.model.execute_upload_image_request import ExecuteUploadImageRequest
from huaweicloudsdkcbs.v1.model.execute_upload_image_request_body import ExecuteUploadImageRequestBody
from huaweicloudsdkcbs.v1.model.execute_upload_image_response import ExecuteUploadImageResponse
from huaweicloudsdkcbs.v1.model.execute_upload_ppt_request import ExecuteUploadPptRequest
from huaweicloudsdkcbs.v1.model.execute_upload_ppt_request_body import ExecuteUploadPptRequestBody
from huaweicloudsdkcbs.v1.model.execute_upload_ppt_response import ExecuteUploadPptResponse
from huaweicloudsdkcbs.v1.model.extends import Extends
from huaweicloudsdkcbs.v1.model.frame import Frame
from huaweicloudsdkcbs.v1.model.history_slot import HistorySlot
from huaweicloudsdkcbs.v1.model.history_slot_word import HistorySlotWord
from huaweicloudsdkcbs.v1.model.hot_question_count import HotQuestionCount
from huaweicloudsdkcbs.v1.model.image import Image
from huaweicloudsdkcbs.v1.model.image_frame import ImageFrame
from huaweicloudsdkcbs.v1.model.image_read_config import ImageReadConfig
from huaweicloudsdkcbs.v1.model.image_read_config_resp import ImageReadConfigResp
from huaweicloudsdkcbs.v1.model.image_url_resp import ImageUrlResp
from huaweicloudsdkcbs.v1.model.kbqa_answers import KbqaAnswers
from huaweicloudsdkcbs.v1.model.key_words_stat import KeyWordsStat
from huaweicloudsdkcbs.v1.model.left_right_position import LeftRightPosition
from huaweicloudsdkcbs.v1.model.list_suggestions_request import ListSuggestionsRequest
from huaweicloudsdkcbs.v1.model.list_suggestions_response import ListSuggestionsResponse
from huaweicloudsdkcbs.v1.model.ppt_read_config import PPTReadConfig
from huaweicloudsdkcbs.v1.model.ppt_read_config_resp import PPTReadConfigResp
from huaweicloudsdkcbs.v1.model.position import Position
from huaweicloudsdkcbs.v1.model.post_images_req import PostImagesReq
from huaweicloudsdkcbs.v1.model.post_qa_session_req import PostQaSessionReq
from huaweicloudsdkcbs.v1.model.post_requests_req import PostRequestsReq
from huaweicloudsdkcbs.v1.model.post_satisfaction_req import PostSatisfactionReq
from huaweicloudsdkcbs.v1.model.post_suggestions_req import PostSuggestionsReq
from huaweicloudsdkcbs.v1.model.put_video_info import PutVideoInfo
from huaweicloudsdkcbs.v1.model.qa_bot_answer import QaBotAnswer
from huaweicloudsdkcbs.v1.model.qa_bot_answers import QaBotAnswers
from huaweicloudsdkcbs.v1.model.qa_bot_answers_new import QaBotAnswersNew
from huaweicloudsdkcbs.v1.model.read_config import ReadConfig
from huaweicloudsdkcbs.v1.model.read_config_resp import ReadConfigResp
from huaweicloudsdkcbs.v1.model.recomend_answer import RecomendAnswer
from huaweicloudsdkcbs.v1.model.related_intention import RelatedIntention
from huaweicloudsdkcbs.v1.model.reply_rates_intervals import ReplyRatesIntervals
from huaweicloudsdkcbs.v1.model.reply_rates_total import ReplyRatesTotal
from huaweicloudsdkcbs.v1.model.resolution import Resolution
from huaweicloudsdkcbs.v1.model.session_extends import SessionExtends
from huaweicloudsdkcbs.v1.model.session_stats_intervals import SessionStatsIntervals
from huaweicloudsdkcbs.v1.model.session_stats_total import SessionStatsTotal
from huaweicloudsdkcbs.v1.model.skill_response import SkillResponse
from huaweicloudsdkcbs.v1.model.slot_value import SlotValue
from huaweicloudsdkcbs.v1.model.table_qa_answers import TableQaAnswers
from huaweicloudsdkcbs.v1.model.tag import Tag
from huaweicloudsdkcbs.v1.model.tag_labor_request import TagLaborRequest
from huaweicloudsdkcbs.v1.model.tag_labor_response import TagLaborResponse
from huaweicloudsdkcbs.v1.model.tag_satisfaction_request import TagSatisfactionRequest
from huaweicloudsdkcbs.v1.model.tag_satisfaction_response import TagSatisfactionResponse
from huaweicloudsdkcbs.v1.model.task_bot_answers import TaskBotAnswers
from huaweicloudsdkcbs.v1.model.time import Time
from huaweicloudsdkcbs.v1.model.tts_config import TtsConfig
from huaweicloudsdkcbs.v1.model.update_image_name_req import UpdateImageNameReq
from huaweicloudsdkcbs.v1.model.update_req import UpdateReq
from huaweicloudsdkcbs.v1.model.url_resp import UrlResp
from huaweicloudsdkcbs.v1.model.video import Video
from huaweicloudsdkcbs.v1.model.video_config import VideoConfig
from huaweicloudsdkcbs.v1.model.video_config_resp import VideoConfigResp

