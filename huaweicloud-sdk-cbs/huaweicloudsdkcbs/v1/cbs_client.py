# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CbsClient(Client):
    def __init__(self):
        super(CbsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CbsClient":
            raise TypeError("client type error, support client type is CbsClient")

        return ClientBuilder(clazz)

    def collect_hot_questions(self, request):
        """热点问题统计

        获取完全匹配的热点标准问题列表。
        默认按照完全匹配标准问题被问及的频次降序排序。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectHotQuestions
        :type request: :class:`huaweicloudsdkcbs.v1.CollectHotQuestionsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectHotQuestionsResponse`
        """
        return self._collect_hot_questions_with_http_info(request)

    def _collect_hot_questions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'exclude' in local_var_params:
            query_params.append(('exclude', local_var_params['exclude']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/qa-pairs/hots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectHotQuestionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_key_words(self, request):
        """关键词统计

        用户问关键词统计。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectKeyWords
        :type request: :class:`huaweicloudsdkcbs.v1.CollectKeyWordsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectKeyWordsResponse`
        """
        return self._collect_key_words_with_http_info(request)

    def _collect_key_words_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/keywords',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectKeyWordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_reply_rates(self, request):
        """问答统计

        指定领域获取指定时间范围内的问题答复率，支持按周期统计。
        如果领域未指定则表示获取所有领域的问题答复率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectReplyRates
        :type request: :class:`huaweicloudsdkcbs.v1.CollectReplyRatesRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectReplyRatesResponse`
        """
        return self._collect_reply_rates_with_http_info(request)

    def _collect_reply_rates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/reply-rates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectReplyRatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_session_stats(self, request):
        """访问统计

        获取用户会话统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectSessionStats
        :type request: :class:`huaweicloudsdkcbs.v1.CollectSessionStatsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CollectSessionStatsResponse`
        """
        return self._collect_session_stats_with_http_info(request)

    def _collect_session_stats_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'time_zone' in local_var_params:
            query_params.append(('time_zone', local_var_params['time_zone']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/session-stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectSessionStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_session(self, request):
        """开启会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口创建会话。该接口仅支持老用户，新用户请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSession
        :type request: :class:`huaweicloudsdkcbs.v1.CreateSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.CreateSessionResponse`
        """
        return self._create_session_with_http_info(request)

    def _create_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_session(self, request):
        """关闭会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口关闭会话。该接口即将下线，请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSession
        :type request: :class:`huaweicloudsdkcbs.v1.DeleteSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.DeleteSessionResponse`
        """
        return self._delete_session_with_http_info(request)

    def _delete_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions/{session_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_compose_video(self, request):
        """合成视频(按包周期收费)

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteComposeVideo
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteComposeVideoRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteComposeVideoResponse`
        """
        return self._execute_compose_video_with_http_info(request)

    def _execute_compose_video_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/compose',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteComposeVideoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_compose_video_ondemand(self, request):
        """合成视频(按需收费)

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteComposeVideoOndemand
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteComposeVideoOndemandRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteComposeVideoOndemandResponse`
        """
        return self._execute_compose_video_ondemand_with_http_info(request)

    def _execute_compose_video_ondemand_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/compose/on-demand',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteComposeVideoOndemandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_create_video(self, request):
        """创建视频

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteCreateVideo
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteCreateVideoRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteCreateVideoResponse`
        """
        return self._execute_create_video_with_http_info(request)

    def _execute_create_video_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteCreateVideoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_delete_video_by_id(self, request):
        """删除视频

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDeleteVideoById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteDeleteVideoByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteDeleteVideoByIdResponse`
        """
        return self._execute_delete_video_by_id_with_http_info(request)

    def _execute_delete_video_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteDeleteVideoByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_deleteimage_by_id(self, request):
        """删除图片

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDeleteimageById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteDeleteimageByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteDeleteimageByIdResponse`
        """
        return self._execute_deleteimage_by_id_with_http_info(request)

    def _execute_deleteimage_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteDeleteimageByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_character_info_by_id(self, request):
        """获取形象详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetCharacterInfoById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetCharacterInfoByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetCharacterInfoByIdResponse`
        """
        return self._execute_get_character_info_by_id_with_http_info(request)

    def _execute_get_character_info_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'character_id' in local_var_params:
            path_params['character_id'] = local_var_params['character_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/characters/{character_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetCharacterInfoByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_characters(self, request):
        """获取形象列表

        TODO:
        
        本期不做形象进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetCharacters
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetCharactersRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetCharactersResponse`
        """
        return self._execute_get_characters_with_http_info(request)

    def _execute_get_characters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'train_status' in local_var_params:
            query_params.append(('train_status', local_var_params['train_status']))
        if 'character_name' in local_var_params:
            query_params.append(('character_name', local_var_params['character_name']))
        if 'support_interact' in local_var_params:
            query_params.append(('support_interact', local_var_params['support_interact']))
        if 'gender' in local_var_params:
            query_params.append(('gender', local_var_params['gender']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/characters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetCharactersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_frams_list_by_images_id(self, request):
        """获取播报框

        获取指定图片可用的播报框列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetFramsListByImagesId
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetFramsListByImagesIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetFramsListByImagesIdResponse`
        """
        return self._execute_get_frams_list_by_images_id_with_http_info(request)

    def _execute_get_frams_list_by_images_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_id' in local_var_params:
            query_params.append(('image_id', local_var_params['image_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/image-frames',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetFramsListByImagesIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_images_list(self, request):
        """获取图片列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetImagesList
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetImagesListRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetImagesListResponse`
        """
        return self._execute_get_images_list_with_http_info(request)

    def _execute_get_images_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'resolution_type' in local_var_params:
            query_params.append(('resolution_type', local_var_params['resolution_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetImagesListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_video_info_by_id(self, request):
        """获取视频详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetVideoInfoById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetVideoInfoByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetVideoInfoByIdResponse`
        """
        return self._execute_get_video_info_by_id_with_http_info(request)

    def _execute_get_video_info_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetVideoInfoByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_get_videos_list(self, request):
        """获取视频列表

        该接口用于获取视频列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGetVideosList
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteGetVideosListRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteGetVideosListResponse`
        """
        return self._execute_get_videos_list_with_http_info(request)

    def _execute_get_videos_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGetVideosListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_post_create_images(self, request):
        """创建图片

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecutePostCreateImages
        :type request: :class:`huaweicloudsdkcbs.v1.ExecutePostCreateImagesRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecutePostCreateImagesResponse`
        """
        return self._execute_post_create_images_with_http_info(request)

    def _execute_post_create_images_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'type' in local_var_params:
            form_params['type'] = local_var_params['type']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'resolution_type' in local_var_params:
            form_params['resolution_type'] = local_var_params['resolution_type']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecutePostCreateImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_qa_chat(self, request):
        """问答机器人会话

        用户调用该接口和机器人进行聊天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteQaChat
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteQaChatRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteQaChatResponse`
        """
        return self._execute_qa_chat_with_http_info(request)

    def _execute_qa_chat_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/chat',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteQaChatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_session(self, request):
        """处理会话

        问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口与机器人进行会话。该接口即将下线，请优先使用问答机器人API接口进行调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteSession
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteSessionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteSessionResponse`
        """
        return self._execute_session_with_http_info(request)

    def _execute_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/sessions/{session_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_update_image_name(self, request):
        """修改图片名

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUpdateImageName
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateImageNameRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateImageNameResponse`
        """
        return self._execute_update_image_name_with_http_info(request)

    def _execute_update_image_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/images/{image_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteUpdateImageNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_update_video_by_id(self, request):
        """更新视频名

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUpdateVideoById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateVideoByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateVideoByIdResponse`
        """
        return self._execute_update_video_by_id_with_http_info(request)

    def _execute_update_video_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteUpdateVideoByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_update_video_info_by_id(self, request):
        """配置视频

        通过该接口配置视频
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUpdateVideoInfoById
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateVideoInfoByIdRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteUpdateVideoInfoByIdResponse`
        """
        return self._execute_update_video_info_by_id_with_http_info(request)

    def _execute_update_video_info_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteUpdateVideoInfoByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_upload_image(self, request):
        """上传播报插图

        上传图片并生成图片链接，图片需小于10m；
        同一个视频同时最多支持50张插图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUploadImage
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteUploadImageRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteUploadImageResponse`
        """
        return self._execute_upload_image_with_http_info(request)

    def _execute_upload_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/upload/image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteUploadImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_upload_ppt(self, request):
        """通过pdf上传多张插图

        当前仅支持上传PDF，如有PPT请将PPT转化为PDF再进行上传，文件需小于10m；
        该接口会将pdf每一页转换图片，并生成链接；
        同一个视频同时最多支持50张插图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteUploadPpt
        :type request: :class:`huaweicloudsdkcbs.v1.ExecuteUploadPptRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ExecuteUploadPptResponse`
        """
        return self._execute_upload_ppt_with_http_info(request)

    def _execute_upload_ppt_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'video_id' in local_var_params:
            path_params['video_id'] = local_var_params['video_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/digital-human/video/{video_id}/upload/ppt',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteUploadPptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_suggestions(self, request):
        """获取问题提示

        获取用户输入问题的提示问题列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSuggestions
        :type request: :class:`huaweicloudsdkcbs.v1.ListSuggestionsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.ListSuggestionsResponse`
        """
        return self._list_suggestions_with_http_info(request)

    def _list_suggestions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/suggestions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSuggestionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_labor(self, request):
        """标记为转人工

        智能问答返回的结果后，用户是否转人工。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagLabor
        :type request: :class:`huaweicloudsdkcbs.v1.TagLaborRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.TagLaborResponse`
        """
        return self._tag_labor_with_http_info(request)

    def _tag_labor_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/{request_id}/labor',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagLaborResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_satisfaction(self, request):
        """问答满意评价

        用户提出问题后，对智能问答返回的结果是否满意。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagSatisfaction
        :type request: :class:`huaweicloudsdkcbs.v1.TagSatisfactionRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.TagSatisfactionResponse`
        """
        return self._tag_satisfaction_with_http_info(request)

    def _tag_satisfaction_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests/{request_id}/satisfaction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagSatisfactionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def post_requests(self, request):
        """PostRequests

        问答服务的输入为用户提问，输出是与输入最匹配的Top N(默认为top5)个知识点，知识点按得分从高到低排序。
        
        说明： 
        返回知识点如果含有答案字段（answer），则表示返回匹配成功结果，如果没有答案字段，则表示推荐结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PostRequests
        :type request: :class:`huaweicloudsdkcbs.v1.PostRequestsRequest`
        :rtype: :class:`huaweicloudsdkcbs.v1.PostRequestsResponse`
        """
        return self._post_requests_with_http_info(request)

    def _post_requests_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'qabot_id' in local_var_params:
            path_params['qabot_id'] = local_var_params['qabot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/qabots/{qabot_id}/requests',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PostRequestsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
