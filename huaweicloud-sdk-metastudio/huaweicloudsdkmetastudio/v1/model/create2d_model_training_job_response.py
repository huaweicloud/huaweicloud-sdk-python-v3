# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Create2dModelTrainingJobResponse(SdkResponse):

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
        'cover_upload_url': 'str',
        'id_card_image1_upload_url': 'str',
        'id_card_image2_upload_url': 'str',
        'grant_file_upload_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'training_video_upload_url': 'training_video_upload_url',
        'cover_upload_url': 'cover_upload_url',
        'id_card_image1_upload_url': 'id_card_image1_upload_url',
        'id_card_image2_upload_url': 'id_card_image2_upload_url',
        'grant_file_upload_url': 'grant_file_upload_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, training_video_upload_url=None, cover_upload_url=None, id_card_image1_upload_url=None, id_card_image2_upload_url=None, grant_file_upload_url=None, x_request_id=None):
        """Create2dModelTrainingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param training_video_upload_url: 分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。
        :type training_video_upload_url: list[str]
        :param cover_upload_url: 模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。
        :type cover_upload_url: str
        :param id_card_image1_upload_url: 身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。
        :type id_card_image1_upload_url: str
        :param id_card_image2_upload_url: 身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。
        :type id_card_image2_upload_url: str
        :param grant_file_upload_url: 授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。
        :type grant_file_upload_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(Create2dModelTrainingJobResponse, self).__init__()

        self._job_id = None
        self._training_video_upload_url = None
        self._cover_upload_url = None
        self._id_card_image1_upload_url = None
        self._id_card_image2_upload_url = None
        self._grant_file_upload_url = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if training_video_upload_url is not None:
            self.training_video_upload_url = training_video_upload_url
        if cover_upload_url is not None:
            self.cover_upload_url = cover_upload_url
        if id_card_image1_upload_url is not None:
            self.id_card_image1_upload_url = id_card_image1_upload_url
        if id_card_image2_upload_url is not None:
            self.id_card_image2_upload_url = id_card_image2_upload_url
        if grant_file_upload_url is not None:
            self.grant_file_upload_url = grant_file_upload_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this Create2dModelTrainingJobResponse.

        任务ID。

        :return: The job_id of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Create2dModelTrainingJobResponse.

        任务ID。

        :param job_id: The job_id of this Create2dModelTrainingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def training_video_upload_url(self):
        """Gets the training_video_upload_url of this Create2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。

        :return: The training_video_upload_url of this Create2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._training_video_upload_url

    @training_video_upload_url.setter
    def training_video_upload_url(self, training_video_upload_url):
        """Sets the training_video_upload_url of this Create2dModelTrainingJobResponse.

        分身数字人训练视频上传URL。该url在文件上传成功后失效，只能上传一次。注意：视频必须是1080p或者4K分辨率（横、竖屏皆可）的mp4格式，视频长度须大于等于3分钟且小于等于10分钟，否则审核会不通过。

        :param training_video_upload_url: The training_video_upload_url of this Create2dModelTrainingJobResponse.
        :type training_video_upload_url: list[str]
        """
        self._training_video_upload_url = training_video_upload_url

    @property
    def cover_upload_url(self):
        """Gets the cover_upload_url of this Create2dModelTrainingJobResponse.

        模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。

        :return: The cover_upload_url of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._cover_upload_url

    @cover_upload_url.setter
    def cover_upload_url(self, cover_upload_url):
        """Sets the cover_upload_url of this Create2dModelTrainingJobResponse.

        模型封面上传URL。该URL在文件上传成功后失效，只能上传一次。

        :param cover_upload_url: The cover_upload_url of this Create2dModelTrainingJobResponse.
        :type cover_upload_url: str
        """
        self._cover_upload_url = cover_upload_url

    @property
    def id_card_image1_upload_url(self):
        """Gets the id_card_image1_upload_url of this Create2dModelTrainingJobResponse.

        身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :return: The id_card_image1_upload_url of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image1_upload_url

    @id_card_image1_upload_url.setter
    def id_card_image1_upload_url(self, id_card_image1_upload_url):
        """Sets the id_card_image1_upload_url of this Create2dModelTrainingJobResponse.

        身份证正面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :param id_card_image1_upload_url: The id_card_image1_upload_url of this Create2dModelTrainingJobResponse.
        :type id_card_image1_upload_url: str
        """
        self._id_card_image1_upload_url = id_card_image1_upload_url

    @property
    def id_card_image2_upload_url(self):
        """Gets the id_card_image2_upload_url of this Create2dModelTrainingJobResponse.

        身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :return: The id_card_image2_upload_url of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image2_upload_url

    @id_card_image2_upload_url.setter
    def id_card_image2_upload_url(self, id_card_image2_upload_url):
        """Sets the id_card_image2_upload_url of this Create2dModelTrainingJobResponse.

        身份证反面照片上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :param id_card_image2_upload_url: The id_card_image2_upload_url of this Create2dModelTrainingJobResponse.
        :type id_card_image2_upload_url: str
        """
        self._id_card_image2_upload_url = id_card_image2_upload_url

    @property
    def grant_file_upload_url(self):
        """Gets the grant_file_upload_url of this Create2dModelTrainingJobResponse.

        授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :return: The grant_file_upload_url of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._grant_file_upload_url

    @grant_file_upload_url.setter
    def grant_file_upload_url(self, grant_file_upload_url):
        """Sets the grant_file_upload_url of this Create2dModelTrainingJobResponse.

        授权书上传URL。该URL在文件上传成功后失效，只能上传一次。注意：非NA用户必须上传，否则审核会不通过。

        :param grant_file_upload_url: The grant_file_upload_url of this Create2dModelTrainingJobResponse.
        :type grant_file_upload_url: str
        """
        self._grant_file_upload_url = grant_file_upload_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this Create2dModelTrainingJobResponse.

        :return: The x_request_id of this Create2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this Create2dModelTrainingJobResponse.

        :param x_request_id: The x_request_id of this Create2dModelTrainingJobResponse.
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
        if not isinstance(other, Create2dModelTrainingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
