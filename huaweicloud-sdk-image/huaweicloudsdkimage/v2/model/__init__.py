# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkimage.v2.model.bounding_box import BoundingBox
from huaweicloudsdkimage.v2.model.celebrity_recognition_req import CelebrityRecognitionReq
from huaweicloudsdkimage.v2.model.celebrity_recognition_result_body import CelebrityRecognitionResultBody
from huaweicloudsdkimage.v2.model.create_image_highresolution_matting_task_request import CreateImageHighresolutionMattingTaskRequest
from huaweicloudsdkimage.v2.model.create_image_highresolution_matting_task_response import CreateImageHighresolutionMattingTaskResponse
from huaweicloudsdkimage.v2.model.create_video_tagging_media_task_request import CreateVideoTaggingMediaTaskRequest
from huaweicloudsdkimage.v2.model.create_video_tagging_media_task_request_body import CreateVideoTaggingMediaTaskRequestBody
from huaweicloudsdkimage.v2.model.create_video_tagging_media_task_response import CreateVideoTaggingMediaTaskResponse
from huaweicloudsdkimage.v2.model.image_description_req import ImageDescriptionReq
from huaweicloudsdkimage.v2.model.image_description_response_result import ImageDescriptionResponseResult
from huaweicloudsdkimage.v2.model.image_highresolution_matting_config import ImageHighresolutionMattingConfig
from huaweicloudsdkimage.v2.model.image_highresolution_matting_config_common import ImageHighresolutionMattingConfigCommon
from huaweicloudsdkimage.v2.model.image_highresolution_matting_inference import ImageHighresolutionMattingInference
from huaweicloudsdkimage.v2.model.image_highresolution_matting_input import ImageHighresolutionMattingInput
from huaweicloudsdkimage.v2.model.image_highresolution_matting_input_data import ImageHighresolutionMattingInputData
from huaweicloudsdkimage.v2.model.image_highresolution_matting_request_body import ImageHighresolutionMattingRequestBody
from huaweicloudsdkimage.v2.model.image_main_object_detection_instance import ImageMainObjectDetectionInstance
from huaweicloudsdkimage.v2.model.image_main_object_detection_req import ImageMainObjectDetectionReq
from huaweicloudsdkimage.v2.model.image_media_tagging_det_instance import ImageMediaTaggingDetInstance
from huaweicloudsdkimage.v2.model.image_media_tagging_det_item_body import ImageMediaTaggingDetItemBody
from huaweicloudsdkimage.v2.model.image_media_tagging_det_item_body_i18n_tag import ImageMediaTaggingDetItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_media_tagging_det_req import ImageMediaTaggingDetReq
from huaweicloudsdkimage.v2.model.image_media_tagging_det_response_result import ImageMediaTaggingDetResponseResult
from huaweicloudsdkimage.v2.model.image_media_tagging_instance import ImageMediaTaggingInstance
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body import ImageMediaTaggingItemBody
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body_i18n_tag import ImageMediaTaggingItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body_i18n_type import ImageMediaTaggingItemBodyI18nType
from huaweicloudsdkimage.v2.model.image_media_tagging_req import ImageMediaTaggingReq
from huaweicloudsdkimage.v2.model.image_media_tagging_response_result import ImageMediaTaggingResponseResult
from huaweicloudsdkimage.v2.model.image_super_resolution_req import ImageSuperResolutionReq
from huaweicloudsdkimage.v2.model.image_super_resolution_response_result import ImageSuperResolutionResponseResult
from huaweicloudsdkimage.v2.model.image_tagging_bounding_box import ImageTaggingBoundingBox
from huaweicloudsdkimage.v2.model.image_tagging_instance import ImageTaggingInstance
from huaweicloudsdkimage.v2.model.image_tagging_item_body import ImageTaggingItemBody
from huaweicloudsdkimage.v2.model.image_tagging_item_body_i18n_tag import ImageTaggingItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_tagging_item_body_i18n_type import ImageTaggingItemBodyI18nType
from huaweicloudsdkimage.v2.model.image_tagging_req import ImageTaggingReq
from huaweicloudsdkimage.v2.model.image_tagging_response_result import ImageTaggingResponseResult
from huaweicloudsdkimage.v2.model.recapture_detect_req import RecaptureDetectReq
from huaweicloudsdkimage.v2.model.recapture_detect_response_result import RecaptureDetectResponseResult
from huaweicloudsdkimage.v2.model.recapture_detect_response_result_detail import RecaptureDetectResponseResultDetail
from huaweicloudsdkimage.v2.model.run_celebrity_recognition_request import RunCelebrityRecognitionRequest
from huaweicloudsdkimage.v2.model.run_celebrity_recognition_response import RunCelebrityRecognitionResponse
from huaweicloudsdkimage.v2.model.run_image_description_request import RunImageDescriptionRequest
from huaweicloudsdkimage.v2.model.run_image_description_response import RunImageDescriptionResponse
from huaweicloudsdkimage.v2.model.run_image_main_object_detection_request import RunImageMainObjectDetectionRequest
from huaweicloudsdkimage.v2.model.run_image_main_object_detection_response import RunImageMainObjectDetectionResponse
from huaweicloudsdkimage.v2.model.run_image_media_tagging_det_request import RunImageMediaTaggingDetRequest
from huaweicloudsdkimage.v2.model.run_image_media_tagging_det_response import RunImageMediaTaggingDetResponse
from huaweicloudsdkimage.v2.model.run_image_media_tagging_request import RunImageMediaTaggingRequest
from huaweicloudsdkimage.v2.model.run_image_media_tagging_response import RunImageMediaTaggingResponse
from huaweicloudsdkimage.v2.model.run_image_super_resolution_request import RunImageSuperResolutionRequest
from huaweicloudsdkimage.v2.model.run_image_super_resolution_response import RunImageSuperResolutionResponse
from huaweicloudsdkimage.v2.model.run_image_tagging_request import RunImageTaggingRequest
from huaweicloudsdkimage.v2.model.run_image_tagging_response import RunImageTaggingResponse
from huaweicloudsdkimage.v2.model.run_recapture_detect_request import RunRecaptureDetectRequest
from huaweicloudsdkimage.v2.model.run_recapture_detect_response import RunRecaptureDetectResponse
from huaweicloudsdkimage.v2.model.show_image_highresolution_matting_task_request import ShowImageHighresolutionMattingTaskRequest
from huaweicloudsdkimage.v2.model.show_image_highresolution_matting_task_response import ShowImageHighresolutionMattingTaskResponse
from huaweicloudsdkimage.v2.model.show_video_tagging_media_task_request import ShowVideoTaggingMediaTaskRequest
from huaweicloudsdkimage.v2.model.show_video_tagging_media_task_response import ShowVideoTaggingMediaTaskResponse
from huaweicloudsdkimage.v2.model.task_callback import TaskCallback
from huaweicloudsdkimage.v2.model.task_output import TaskOutput
from huaweicloudsdkimage.v2.model.task_output_obs import TaskOutputObs
from huaweicloudsdkimage.v2.model.video_tagging_media_task_input import VideoTaggingMediaTaskInput
from huaweicloudsdkimage.v2.model.video_tagging_media_task_input_data import VideoTaggingMediaTaskInputData
from huaweicloudsdkimage.v2.model.video_tagging_task_config import VideoTaggingTaskConfig
from huaweicloudsdkimage.v2.model.video_tagging_task_config_common import VideoTaggingTaskConfigCommon
from huaweicloudsdkimage.v2.model.video_tagginginference import VideoTagginginference
