# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBeautyPreviewJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'post_beauty_image_download_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'state': 'state',
        'post_beauty_image_download_url': 'post_beauty_image_download_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, state=None, post_beauty_image_download_url=None, x_request_id=None):
        """ShowBeautyPreviewJobResponse

        The model defined in huaweicloud sdk

        :param state: 任务的状态。 * WAIT_IMAGE_UPLOAD：待上传美白前图片 * WAITING：等待生成美白预览图 * PROCESSING：美白预览图生成中 * SUCCESS：美白预览图生成成功 * FAILED：美白预览图生成失败
        :type state: str
        :param post_beauty_image_download_url: 美白后图片下载url。
        :type post_beauty_image_download_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowBeautyPreviewJobResponse, self).__init__()

        self._state = None
        self._post_beauty_image_download_url = None
        self._x_request_id = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if post_beauty_image_download_url is not None:
            self.post_beauty_image_download_url = post_beauty_image_download_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def state(self):
        """Gets the state of this ShowBeautyPreviewJobResponse.

        任务的状态。 * WAIT_IMAGE_UPLOAD：待上传美白前图片 * WAITING：等待生成美白预览图 * PROCESSING：美白预览图生成中 * SUCCESS：美白预览图生成成功 * FAILED：美白预览图生成失败

        :return: The state of this ShowBeautyPreviewJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowBeautyPreviewJobResponse.

        任务的状态。 * WAIT_IMAGE_UPLOAD：待上传美白前图片 * WAITING：等待生成美白预览图 * PROCESSING：美白预览图生成中 * SUCCESS：美白预览图生成成功 * FAILED：美白预览图生成失败

        :param state: The state of this ShowBeautyPreviewJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def post_beauty_image_download_url(self):
        """Gets the post_beauty_image_download_url of this ShowBeautyPreviewJobResponse.

        美白后图片下载url。

        :return: The post_beauty_image_download_url of this ShowBeautyPreviewJobResponse.
        :rtype: str
        """
        return self._post_beauty_image_download_url

    @post_beauty_image_download_url.setter
    def post_beauty_image_download_url(self, post_beauty_image_download_url):
        """Sets the post_beauty_image_download_url of this ShowBeautyPreviewJobResponse.

        美白后图片下载url。

        :param post_beauty_image_download_url: The post_beauty_image_download_url of this ShowBeautyPreviewJobResponse.
        :type post_beauty_image_download_url: str
        """
        self._post_beauty_image_download_url = post_beauty_image_download_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowBeautyPreviewJobResponse.

        :return: The x_request_id of this ShowBeautyPreviewJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowBeautyPreviewJobResponse.

        :param x_request_id: The x_request_id of this ShowBeautyPreviewJobResponse.
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
        if not isinstance(other, ShowBeautyPreviewJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
