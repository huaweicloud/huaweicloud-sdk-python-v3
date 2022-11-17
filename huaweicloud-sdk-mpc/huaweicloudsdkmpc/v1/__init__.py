# coding: utf-8

from __future__ import absolute_import

# import MpcClient
from huaweicloudsdkmpc.v1.mpc_client import MpcClient
from huaweicloudsdkmpc.v1.mpc_async_client import MpcAsyncClient
# import models into sdk package
from huaweicloudsdkmpc.v1.model.animated_graphics_output_param import AnimatedGraphicsOutputParam
from huaweicloudsdkmpc.v1.model.animated_graphics_task import AnimatedGraphicsTask
from huaweicloudsdkmpc.v1.model.audio import Audio
from huaweicloudsdkmpc.v1.model.audio_file import AudioFile
from huaweicloudsdkmpc.v1.model.audio_info import AudioInfo
from huaweicloudsdkmpc.v1.model.audio_process import AudioProcess
from huaweicloudsdkmpc.v1.model.audio_track import AudioTrack
from huaweicloudsdkmpc.v1.model.av_parameters import AvParameters
from huaweicloudsdkmpc.v1.model.basic_task_info import BasicTaskInfo
from huaweicloudsdkmpc.v1.model.basic_watermark import BasicWatermark
from huaweicloudsdkmpc.v1.model.cancel_remux_task_request import CancelRemuxTaskRequest
from huaweicloudsdkmpc.v1.model.cancel_remux_task_response import CancelRemuxTaskResponse
from huaweicloudsdkmpc.v1.model.clip_info import ClipInfo
from huaweicloudsdkmpc.v1.model.common import Common
from huaweicloudsdkmpc.v1.model.common_create_task_req import CommonCreateTaskReq
from huaweicloudsdkmpc.v1.model.common_create_task_rsp import CommonCreateTaskRsp
from huaweicloudsdkmpc.v1.model.common_query_task_rsp import CommonQueryTaskRsp
from huaweicloudsdkmpc.v1.model.common_task import CommonTask
from huaweicloudsdkmpc.v1.model.common_task_meta import CommonTaskMeta
from huaweicloudsdkmpc.v1.model.concat_info import ConcatInfo
from huaweicloudsdkmpc.v1.model.create_animated_graphics_task_req import CreateAnimatedGraphicsTaskReq
from huaweicloudsdkmpc.v1.model.create_animated_graphics_task_request import CreateAnimatedGraphicsTaskRequest
from huaweicloudsdkmpc.v1.model.create_animated_graphics_task_response import CreateAnimatedGraphicsTaskResponse
from huaweicloudsdkmpc.v1.model.create_editing_job_req import CreateEditingJobReq
from huaweicloudsdkmpc.v1.model.create_editing_job_request import CreateEditingJobRequest
from huaweicloudsdkmpc.v1.model.create_editing_job_response import CreateEditingJobResponse
from huaweicloudsdkmpc.v1.model.create_encrypt_req import CreateEncryptReq
from huaweicloudsdkmpc.v1.model.create_encrypt_task_request import CreateEncryptTaskRequest
from huaweicloudsdkmpc.v1.model.create_encrypt_task_response import CreateEncryptTaskResponse
from huaweicloudsdkmpc.v1.model.create_extract_task_req import CreateExtractTaskReq
from huaweicloudsdkmpc.v1.model.create_extract_task_request import CreateExtractTaskRequest
from huaweicloudsdkmpc.v1.model.create_extract_task_response import CreateExtractTaskResponse
from huaweicloudsdkmpc.v1.model.create_mb_tasks_report_request import CreateMbTasksReportRequest
from huaweicloudsdkmpc.v1.model.create_mb_tasks_report_response import CreateMbTasksReportResponse
from huaweicloudsdkmpc.v1.model.create_media_process_req import CreateMediaProcessReq
from huaweicloudsdkmpc.v1.model.create_media_process_task_request import CreateMediaProcessTaskRequest
from huaweicloudsdkmpc.v1.model.create_media_process_task_response import CreateMediaProcessTaskResponse
from huaweicloudsdkmpc.v1.model.create_merge_channels_req import CreateMergeChannelsReq
from huaweicloudsdkmpc.v1.model.create_merge_channels_task_request import CreateMergeChannelsTaskRequest
from huaweicloudsdkmpc.v1.model.create_merge_channels_task_response import CreateMergeChannelsTaskResponse
from huaweicloudsdkmpc.v1.model.create_mpe_call_back_request import CreateMpeCallBackRequest
from huaweicloudsdkmpc.v1.model.create_mpe_call_back_response import CreateMpeCallBackResponse
from huaweicloudsdkmpc.v1.model.create_quality_enhance_template_request import CreateQualityEnhanceTemplateRequest
from huaweicloudsdkmpc.v1.model.create_quality_enhance_template_response import CreateQualityEnhanceTemplateResponse
from huaweicloudsdkmpc.v1.model.create_remux_task_req import CreateRemuxTaskReq
from huaweicloudsdkmpc.v1.model.create_remux_task_request import CreateRemuxTaskRequest
from huaweicloudsdkmpc.v1.model.create_remux_task_response import CreateRemuxTaskResponse
from huaweicloudsdkmpc.v1.model.create_reset_tracks_req import CreateResetTracksReq
from huaweicloudsdkmpc.v1.model.create_reset_tracks_task_request import CreateResetTracksTaskRequest
from huaweicloudsdkmpc.v1.model.create_reset_tracks_task_response import CreateResetTracksTaskResponse
from huaweicloudsdkmpc.v1.model.create_retry_remux_task_request import CreateRetryRemuxTaskRequest
from huaweicloudsdkmpc.v1.model.create_retry_remux_task_response import CreateRetryRemuxTaskResponse
from huaweicloudsdkmpc.v1.model.create_template_group_request import CreateTemplateGroupRequest
from huaweicloudsdkmpc.v1.model.create_template_group_response import CreateTemplateGroupResponse
from huaweicloudsdkmpc.v1.model.create_thumb_req import CreateThumbReq
from huaweicloudsdkmpc.v1.model.create_thumbnails_task_request import CreateThumbnailsTaskRequest
from huaweicloudsdkmpc.v1.model.create_thumbnails_task_response import CreateThumbnailsTaskResponse
from huaweicloudsdkmpc.v1.model.create_trans_template_request import CreateTransTemplateRequest
from huaweicloudsdkmpc.v1.model.create_trans_template_response import CreateTransTemplateResponse
from huaweicloudsdkmpc.v1.model.create_transcoding_req import CreateTranscodingReq
from huaweicloudsdkmpc.v1.model.create_transcoding_task_request import CreateTranscodingTaskRequest
from huaweicloudsdkmpc.v1.model.create_transcoding_task_response import CreateTranscodingTaskResponse
from huaweicloudsdkmpc.v1.model.create_watermark_template_request import CreateWatermarkTemplateRequest
from huaweicloudsdkmpc.v1.model.create_watermark_template_response import CreateWatermarkTemplateResponse
from huaweicloudsdkmpc.v1.model.crop import Crop
from huaweicloudsdkmpc.v1.model.delete_animated_graphics_task_request import DeleteAnimatedGraphicsTaskRequest
from huaweicloudsdkmpc.v1.model.delete_animated_graphics_task_response import DeleteAnimatedGraphicsTaskResponse
from huaweicloudsdkmpc.v1.model.delete_editing_job_request import DeleteEditingJobRequest
from huaweicloudsdkmpc.v1.model.delete_editing_job_response import DeleteEditingJobResponse
from huaweicloudsdkmpc.v1.model.delete_encrypt_task_request import DeleteEncryptTaskRequest
from huaweicloudsdkmpc.v1.model.delete_encrypt_task_response import DeleteEncryptTaskResponse
from huaweicloudsdkmpc.v1.model.delete_extract_task_request import DeleteExtractTaskRequest
from huaweicloudsdkmpc.v1.model.delete_extract_task_response import DeleteExtractTaskResponse
from huaweicloudsdkmpc.v1.model.delete_media_process_task_request import DeleteMediaProcessTaskRequest
from huaweicloudsdkmpc.v1.model.delete_media_process_task_response import DeleteMediaProcessTaskResponse
from huaweicloudsdkmpc.v1.model.delete_merge_channels_task_request import DeleteMergeChannelsTaskRequest
from huaweicloudsdkmpc.v1.model.delete_merge_channels_task_response import DeleteMergeChannelsTaskResponse
from huaweicloudsdkmpc.v1.model.delete_quality_enhance_template_request import DeleteQualityEnhanceTemplateRequest
from huaweicloudsdkmpc.v1.model.delete_quality_enhance_template_response import DeleteQualityEnhanceTemplateResponse
from huaweicloudsdkmpc.v1.model.delete_remux_task_request import DeleteRemuxTaskRequest
from huaweicloudsdkmpc.v1.model.delete_remux_task_response import DeleteRemuxTaskResponse
from huaweicloudsdkmpc.v1.model.delete_reset_tracks_task_request import DeleteResetTracksTaskRequest
from huaweicloudsdkmpc.v1.model.delete_reset_tracks_task_response import DeleteResetTracksTaskResponse
from huaweicloudsdkmpc.v1.model.delete_template_group_request import DeleteTemplateGroupRequest
from huaweicloudsdkmpc.v1.model.delete_template_group_response import DeleteTemplateGroupResponse
from huaweicloudsdkmpc.v1.model.delete_template_request import DeleteTemplateRequest
from huaweicloudsdkmpc.v1.model.delete_template_response import DeleteTemplateResponse
from huaweicloudsdkmpc.v1.model.delete_thumbnails_task_request import DeleteThumbnailsTaskRequest
from huaweicloudsdkmpc.v1.model.delete_thumbnails_task_response import DeleteThumbnailsTaskResponse
from huaweicloudsdkmpc.v1.model.delete_transcoding_task_request import DeleteTranscodingTaskRequest
from huaweicloudsdkmpc.v1.model.delete_transcoding_task_response import DeleteTranscodingTaskResponse
from huaweicloudsdkmpc.v1.model.delete_watermark_template_request import DeleteWatermarkTemplateRequest
from huaweicloudsdkmpc.v1.model.delete_watermark_template_response import DeleteWatermarkTemplateResponse
from huaweicloudsdkmpc.v1.model.each_encrypt_rsp import EachEncryptRsp
from huaweicloudsdkmpc.v1.model.edit_audio_info import EditAudioInfo
from huaweicloudsdkmpc.v1.model.edit_hls_info import EditHlsInfo
from huaweicloudsdkmpc.v1.model.edit_setting import EditSetting
from huaweicloudsdkmpc.v1.model.edit_video_info import EditVideoInfo
from huaweicloudsdkmpc.v1.model.editing_job import EditingJob
from huaweicloudsdkmpc.v1.model.encryption import Encryption
from huaweicloudsdkmpc.v1.model.error_response import ErrorResponse
from huaweicloudsdkmpc.v1.model.extract_task import ExtractTask
from huaweicloudsdkmpc.v1.model.hls_encrypt import HlsEncrypt
from huaweicloudsdkmpc.v1.model.image_watermark import ImageWatermark
from huaweicloudsdkmpc.v1.model.image_watermark_setting import ImageWatermarkSetting
from huaweicloudsdkmpc.v1.model.input_setting import InputSetting
from huaweicloudsdkmpc.v1.model.list_animated_graphics_task_request import ListAnimatedGraphicsTaskRequest
from huaweicloudsdkmpc.v1.model.list_animated_graphics_task_response import ListAnimatedGraphicsTaskResponse
from huaweicloudsdkmpc.v1.model.list_editing_job_request import ListEditingJobRequest
from huaweicloudsdkmpc.v1.model.list_editing_job_response import ListEditingJobResponse
from huaweicloudsdkmpc.v1.model.list_encrypt_task_request import ListEncryptTaskRequest
from huaweicloudsdkmpc.v1.model.list_encrypt_task_response import ListEncryptTaskResponse
from huaweicloudsdkmpc.v1.model.list_extract_task_request import ListExtractTaskRequest
from huaweicloudsdkmpc.v1.model.list_extract_task_response import ListExtractTaskResponse
from huaweicloudsdkmpc.v1.model.list_media_process_task_request import ListMediaProcessTaskRequest
from huaweicloudsdkmpc.v1.model.list_media_process_task_response import ListMediaProcessTaskResponse
from huaweicloudsdkmpc.v1.model.list_merge_channels_task_request import ListMergeChannelsTaskRequest
from huaweicloudsdkmpc.v1.model.list_merge_channels_task_response import ListMergeChannelsTaskResponse
from huaweicloudsdkmpc.v1.model.list_quality_enhance_default_template_request import ListQualityEnhanceDefaultTemplateRequest
from huaweicloudsdkmpc.v1.model.list_quality_enhance_default_template_response import ListQualityEnhanceDefaultTemplateResponse
from huaweicloudsdkmpc.v1.model.list_remux_task_request import ListRemuxTaskRequest
from huaweicloudsdkmpc.v1.model.list_remux_task_response import ListRemuxTaskResponse
from huaweicloudsdkmpc.v1.model.list_reset_tracks_task_request import ListResetTracksTaskRequest
from huaweicloudsdkmpc.v1.model.list_reset_tracks_task_response import ListResetTracksTaskResponse
from huaweicloudsdkmpc.v1.model.list_template_group_request import ListTemplateGroupRequest
from huaweicloudsdkmpc.v1.model.list_template_group_response import ListTemplateGroupResponse
from huaweicloudsdkmpc.v1.model.list_template_request import ListTemplateRequest
from huaweicloudsdkmpc.v1.model.list_template_response import ListTemplateResponse
from huaweicloudsdkmpc.v1.model.list_thumbnails_task_request import ListThumbnailsTaskRequest
from huaweicloudsdkmpc.v1.model.list_thumbnails_task_response import ListThumbnailsTaskResponse
from huaweicloudsdkmpc.v1.model.list_transcode_detail_request import ListTranscodeDetailRequest
from huaweicloudsdkmpc.v1.model.list_transcode_detail_response import ListTranscodeDetailResponse
from huaweicloudsdkmpc.v1.model.list_transcoding_task_request import ListTranscodingTaskRequest
from huaweicloudsdkmpc.v1.model.list_transcoding_task_response import ListTranscodingTaskResponse
from huaweicloudsdkmpc.v1.model.list_watermark_template_request import ListWatermarkTemplateRequest
from huaweicloudsdkmpc.v1.model.list_watermark_template_response import ListWatermarkTemplateResponse
from huaweicloudsdkmpc.v1.model.mb_task_parameter import MbTaskParameter
from huaweicloudsdkmpc.v1.model.mb_tasks_report_req import MbTasksReportReq
from huaweicloudsdkmpc.v1.model.media_detail import MediaDetail
from huaweicloudsdkmpc.v1.model.media_process_task_info import MediaProcessTaskInfo
from huaweicloudsdkmpc.v1.model.merge_channels_task_info import MergeChannelsTaskInfo
from huaweicloudsdkmpc.v1.model.meta_data import MetaData
from huaweicloudsdkmpc.v1.model.mix_info import MixInfo
from huaweicloudsdkmpc.v1.model.mix_info_layout import MixInfoLayout
from huaweicloudsdkmpc.v1.model.modify_trans_template_group import ModifyTransTemplateGroup
from huaweicloudsdkmpc.v1.model.modify_trans_template_req import ModifyTransTemplateReq
from huaweicloudsdkmpc.v1.model.mosaic_info import MosaicInfo
from huaweicloudsdkmpc.v1.model.mpc_multi_audio import MpcMultiAudio
from huaweicloudsdkmpc.v1.model.mpe_call_back_req import MpeCallBackReq
from huaweicloudsdkmpc.v1.model.mpe_meta_data import MpeMetaData
from huaweicloudsdkmpc.v1.model.mul_input_file_info import MulInputFileInfo
from huaweicloudsdkmpc.v1.model.multi_audio import MultiAudio
from huaweicloudsdkmpc.v1.model.multi_concat_info import MultiConcatInfo
from huaweicloudsdkmpc.v1.model.multi_task_info import MultiTaskInfo
from huaweicloudsdkmpc.v1.model.obs_obj_info import ObsObjInfo
from huaweicloudsdkmpc.v1.model.origin_para import OriginPara
from huaweicloudsdkmpc.v1.model.output_file_info import OutputFileInfo
from huaweicloudsdkmpc.v1.model.output_policy import OutputPolicy
from huaweicloudsdkmpc.v1.model.output_setting import OutputSetting
from huaweicloudsdkmpc.v1.model.output_thumbnail_para import OutputThumbnailPara
from huaweicloudsdkmpc.v1.model.output_video_para import OutputVideoPara
from huaweicloudsdkmpc.v1.model.output_watermark_para import OutputWatermarkPara
from huaweicloudsdkmpc.v1.model.pane_setting import PaneSetting
from huaweicloudsdkmpc.v1.model.pic_info import PicInfo
from huaweicloudsdkmpc.v1.model.quality_enhance_template import QualityEnhanceTemplate
from huaweicloudsdkmpc.v1.model.quality_enhance_template_info import QualityEnhanceTemplateInfo
from huaweicloudsdkmpc.v1.model.quality_enhance_video import QualityEnhanceVideo
from huaweicloudsdkmpc.v1.model.query_trans_template import QueryTransTemplate
from huaweicloudsdkmpc.v1.model.query_transcodings_task_response import QueryTranscodingsTaskResponse
from huaweicloudsdkmpc.v1.model.remux_output_param import RemuxOutputParam
from huaweicloudsdkmpc.v1.model.remux_retry_req import RemuxRetryReq
from huaweicloudsdkmpc.v1.model.remux_task import RemuxTask
from huaweicloudsdkmpc.v1.model.reset_tracks_task_info import ResetTracksTaskInfo
from huaweicloudsdkmpc.v1.model.source_info import SourceInfo
from huaweicloudsdkmpc.v1.model.sub_audio_file import SubAudioFile
from huaweicloudsdkmpc.v1.model.subtitle import Subtitle
from huaweicloudsdkmpc.v1.model.task_detail_info import TaskDetailInfo
from huaweicloudsdkmpc.v1.model.task_info import TaskInfo
from huaweicloudsdkmpc.v1.model.template_group import TemplateGroup
from huaweicloudsdkmpc.v1.model.template_info import TemplateInfo
from huaweicloudsdkmpc.v1.model.text_watermark import TextWatermark
from huaweicloudsdkmpc.v1.model.thumb_task import ThumbTask
from huaweicloudsdkmpc.v1.model.thumbnail import Thumbnail
from huaweicloudsdkmpc.v1.model.thumbnail_para import ThumbnailPara
from huaweicloudsdkmpc.v1.model.tracks_info import TracksInfo
from huaweicloudsdkmpc.v1.model.trans_template import TransTemplate
from huaweicloudsdkmpc.v1.model.trans_template_group import TransTemplateGroup
from huaweicloudsdkmpc.v1.model.transcode_detail import TranscodeDetail
from huaweicloudsdkmpc.v1.model.update_quality_enhance_template_req import UpdateQualityEnhanceTemplateReq
from huaweicloudsdkmpc.v1.model.update_quality_enhance_template_request import UpdateQualityEnhanceTemplateRequest
from huaweicloudsdkmpc.v1.model.update_quality_enhance_template_response import UpdateQualityEnhanceTemplateResponse
from huaweicloudsdkmpc.v1.model.update_template_group_request import UpdateTemplateGroupRequest
from huaweicloudsdkmpc.v1.model.update_template_group_response import UpdateTemplateGroupResponse
from huaweicloudsdkmpc.v1.model.update_trans_template_request import UpdateTransTemplateRequest
from huaweicloudsdkmpc.v1.model.update_trans_template_response import UpdateTransTemplateResponse
from huaweicloudsdkmpc.v1.model.update_watermark_template_request import UpdateWatermarkTemplateRequest
from huaweicloudsdkmpc.v1.model.update_watermark_template_response import UpdateWatermarkTemplateResponse
from huaweicloudsdkmpc.v1.model.video import Video
from huaweicloudsdkmpc.v1.model.video_and_template import VideoAndTemplate
from huaweicloudsdkmpc.v1.model.video_common import VideoCommon
from huaweicloudsdkmpc.v1.model.video_contrast import VideoContrast
from huaweicloudsdkmpc.v1.model.video_deblock import VideoDeblock
from huaweicloudsdkmpc.v1.model.video_denoise import VideoDenoise
from huaweicloudsdkmpc.v1.model.video_info import VideoInfo
from huaweicloudsdkmpc.v1.model.video_obj import VideoObj
from huaweicloudsdkmpc.v1.model.video_parameters import VideoParameters
from huaweicloudsdkmpc.v1.model.video_process import VideoProcess
from huaweicloudsdkmpc.v1.model.video_saturation import VideoSaturation
from huaweicloudsdkmpc.v1.model.video_sharp import VideoSharp
from huaweicloudsdkmpc.v1.model.video_superresolution import VideoSuperresolution
from huaweicloudsdkmpc.v1.model.watermark_request import WatermarkRequest
from huaweicloudsdkmpc.v1.model.watermark_template import WatermarkTemplate
from huaweicloudsdkmpc.v1.model.x_code_error import XCodeError

