# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Update2dModelTrainingJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'training_video_upload_url': 'list[str]',
        'action_video_upload_url': 'list[str]',
        'audio_upload_url': 'str',
        'cover_upload_url': 'str',
        'id_card_image1_upload_url': 'str',
        'id_card_image2_upload_url': 'str',
        'grant_file_upload_url': 'str',
        'pre_beauty_image_upload_url': 'str',
        'post_beauty_image_upload_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'training_video_upload_url': 'training_video_upload_url',
        'action_video_upload_url': 'action_video_upload_url',
        'audio_upload_url': 'audio_upload_url',
        'cover_upload_url': 'cover_upload_url',
        'id_card_image1_upload_url': 'id_card_image1_upload_url',
        'id_card_image2_upload_url': 'id_card_image2_upload_url',
        'grant_file_upload_url': 'grant_file_upload_url',
        'pre_beauty_image_upload_url': 'pre_beauty_image_upload_url',
        'post_beauty_image_upload_url': 'post_beauty_image_upload_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, training_video_upload_url=None, action_video_upload_url=None, audio_upload_url=None, cover_upload_url=None, id_card_image1_upload_url=None, id_card_image2_upload_url=None, grant_file_upload_url=None, pre_beauty_image_upload_url=None, post_beauty_image_upload_url=None, x_request_id=None):
        r"""Update2dModelTrainingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param training_video_upload_url: 分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type training_video_upload_url: list[str]
        :param action_video_upload_url: 分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type action_video_upload_url: list[str]
        :param audio_upload_url: 音频数据训练上传URL。该url在文件上传成功后失效，只能上传一次 &gt; 通过该地址上传时，需设置content-type为application/zip。
        :type audio_upload_url: str
        :param cover_upload_url: 模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type cover_upload_url: str
        :param id_card_image1_upload_url: 身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type id_card_image1_upload_url: str
        :param id_card_image2_upload_url: 身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type id_card_image2_upload_url: str
        :param grant_file_upload_url: 授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type grant_file_upload_url: str
        :param pre_beauty_image_upload_url: 美白前图片上传url。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type pre_beauty_image_upload_url: str
        :param post_beauty_image_upload_url: 美白后图片上传url。 &gt; 通过该地址上传时，需设置content-type为application/octet-stream
        :type post_beauty_image_upload_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(Update2dModelTrainingJobResponse, self).__init__()

        self._job_id = None
        self._training_video_upload_url = None
        self._action_video_upload_url = None
        self._audio_upload_url = None
        self._cover_upload_url = None
        self._id_card_image1_upload_url = None
        self._id_card_image2_upload_url = None
        self._grant_file_upload_url = None
        self._pre_beauty_image_upload_url = None
        self._post_beauty_image_upload_url = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if training_video_upload_url is not None:
            self.training_video_upload_url = training_video_upload_url
        if action_video_upload_url is not None:
            self.action_video_upload_url = action_video_upload_url
        if audio_upload_url is not None:
            self.audio_upload_url = audio_upload_url
        if cover_upload_url is not None:
            self.cover_upload_url = cover_upload_url
        if id_card_image1_upload_url is not None:
            self.id_card_image1_upload_url = id_card_image1_upload_url
        if id_card_image2_upload_url is not None:
            self.id_card_image2_upload_url = id_card_image2_upload_url
        if grant_file_upload_url is not None:
            self.grant_file_upload_url = grant_file_upload_url
        if pre_beauty_image_upload_url is not None:
            self.pre_beauty_image_upload_url = pre_beauty_image_upload_url
        if post_beauty_image_upload_url is not None:
            self.post_beauty_image_upload_url = post_beauty_image_upload_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this Update2dModelTrainingJobResponse.

        任务ID。

        :return: The job_id of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Update2dModelTrainingJobResponse.

        任务ID。

        :param job_id: The job_id of this Update2dModelTrainingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def training_video_upload_url(self):
        r"""Gets the training_video_upload_url of this Update2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The training_video_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._training_video_upload_url

    @training_video_upload_url.setter
    def training_video_upload_url(self, training_video_upload_url):
        r"""Sets the training_video_upload_url of this Update2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param training_video_upload_url: The training_video_upload_url of this Update2dModelTrainingJobResponse.
        :type training_video_upload_url: list[str]
        """
        self._training_video_upload_url = training_video_upload_url

    @property
    def action_video_upload_url(self):
        r"""Gets the action_video_upload_url of this Update2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The action_video_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._action_video_upload_url

    @action_video_upload_url.setter
    def action_video_upload_url(self, action_video_upload_url):
        r"""Sets the action_video_upload_url of this Update2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param action_video_upload_url: The action_video_upload_url of this Update2dModelTrainingJobResponse.
        :type action_video_upload_url: list[str]
        """
        self._action_video_upload_url = action_video_upload_url

    @property
    def audio_upload_url(self):
        r"""Gets the audio_upload_url of this Update2dModelTrainingJobResponse.

        音频数据训练上传URL。该url在文件上传成功后失效，只能上传一次 > 通过该地址上传时，需设置content-type为application/zip。

        :return: The audio_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._audio_upload_url

    @audio_upload_url.setter
    def audio_upload_url(self, audio_upload_url):
        r"""Sets the audio_upload_url of this Update2dModelTrainingJobResponse.

        音频数据训练上传URL。该url在文件上传成功后失效，只能上传一次 > 通过该地址上传时，需设置content-type为application/zip。

        :param audio_upload_url: The audio_upload_url of this Update2dModelTrainingJobResponse.
        :type audio_upload_url: str
        """
        self._audio_upload_url = audio_upload_url

    @property
    def cover_upload_url(self):
        r"""Gets the cover_upload_url of this Update2dModelTrainingJobResponse.

        模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The cover_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._cover_upload_url

    @cover_upload_url.setter
    def cover_upload_url(self, cover_upload_url):
        r"""Sets the cover_upload_url of this Update2dModelTrainingJobResponse.

        模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param cover_upload_url: The cover_upload_url of this Update2dModelTrainingJobResponse.
        :type cover_upload_url: str
        """
        self._cover_upload_url = cover_upload_url

    @property
    def id_card_image1_upload_url(self):
        r"""Gets the id_card_image1_upload_url of this Update2dModelTrainingJobResponse.

        身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The id_card_image1_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image1_upload_url

    @id_card_image1_upload_url.setter
    def id_card_image1_upload_url(self, id_card_image1_upload_url):
        r"""Sets the id_card_image1_upload_url of this Update2dModelTrainingJobResponse.

        身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param id_card_image1_upload_url: The id_card_image1_upload_url of this Update2dModelTrainingJobResponse.
        :type id_card_image1_upload_url: str
        """
        self._id_card_image1_upload_url = id_card_image1_upload_url

    @property
    def id_card_image2_upload_url(self):
        r"""Gets the id_card_image2_upload_url of this Update2dModelTrainingJobResponse.

        身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The id_card_image2_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image2_upload_url

    @id_card_image2_upload_url.setter
    def id_card_image2_upload_url(self, id_card_image2_upload_url):
        r"""Sets the id_card_image2_upload_url of this Update2dModelTrainingJobResponse.

        身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param id_card_image2_upload_url: The id_card_image2_upload_url of this Update2dModelTrainingJobResponse.
        :type id_card_image2_upload_url: str
        """
        self._id_card_image2_upload_url = id_card_image2_upload_url

    @property
    def grant_file_upload_url(self):
        r"""Gets the grant_file_upload_url of this Update2dModelTrainingJobResponse.

        授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The grant_file_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._grant_file_upload_url

    @grant_file_upload_url.setter
    def grant_file_upload_url(self, grant_file_upload_url):
        r"""Sets the grant_file_upload_url of this Update2dModelTrainingJobResponse.

        授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param grant_file_upload_url: The grant_file_upload_url of this Update2dModelTrainingJobResponse.
        :type grant_file_upload_url: str
        """
        self._grant_file_upload_url = grant_file_upload_url

    @property
    def pre_beauty_image_upload_url(self):
        r"""Gets the pre_beauty_image_upload_url of this Update2dModelTrainingJobResponse.

        美白前图片上传url。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The pre_beauty_image_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._pre_beauty_image_upload_url

    @pre_beauty_image_upload_url.setter
    def pre_beauty_image_upload_url(self, pre_beauty_image_upload_url):
        r"""Sets the pre_beauty_image_upload_url of this Update2dModelTrainingJobResponse.

        美白前图片上传url。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param pre_beauty_image_upload_url: The pre_beauty_image_upload_url of this Update2dModelTrainingJobResponse.
        :type pre_beauty_image_upload_url: str
        """
        self._pre_beauty_image_upload_url = pre_beauty_image_upload_url

    @property
    def post_beauty_image_upload_url(self):
        r"""Gets the post_beauty_image_upload_url of this Update2dModelTrainingJobResponse.

        美白后图片上传url。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :return: The post_beauty_image_upload_url of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._post_beauty_image_upload_url

    @post_beauty_image_upload_url.setter
    def post_beauty_image_upload_url(self, post_beauty_image_upload_url):
        r"""Sets the post_beauty_image_upload_url of this Update2dModelTrainingJobResponse.

        美白后图片上传url。 > 通过该地址上传时，需设置content-type为application/octet-stream

        :param post_beauty_image_upload_url: The post_beauty_image_upload_url of this Update2dModelTrainingJobResponse.
        :type post_beauty_image_upload_url: str
        """
        self._post_beauty_image_upload_url = post_beauty_image_upload_url

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this Update2dModelTrainingJobResponse.

        :return: The x_request_id of this Update2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this Update2dModelTrainingJobResponse.

        :param x_request_id: The x_request_id of this Update2dModelTrainingJobResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Update2dModelTrainingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
