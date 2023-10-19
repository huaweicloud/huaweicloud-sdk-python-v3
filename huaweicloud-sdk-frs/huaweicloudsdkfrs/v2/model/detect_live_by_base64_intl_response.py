# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLiveByBase64IntlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_result': 'LiveDetectRespVideoresult',
        'warning_list': 'list[WarningList]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'video_result': 'video-result',
        'warning_list': 'warning-list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, video_result=None, warning_list=None, x_request_id=None):
        """DetectLiveByBase64IntlResponse

        The model defined in huaweicloud sdk

        :param video_result: 
        :type video_result: :class:`huaweicloudsdkfrs.v2.LiveDetectRespVideoresult`
        :param warning_list: [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/api-face/face_02_0077.html)。调用失败时无此字段](tag:hc) [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0077.html)。调用失败时无此字段](tag:hk)
        :type warning_list: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DetectLiveByBase64IntlResponse, self).__init__()

        self._video_result = None
        self._warning_list = None
        self._x_request_id = None
        self.discriminator = None

        if video_result is not None:
            self.video_result = video_result
        if warning_list is not None:
            self.warning_list = warning_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def video_result(self):
        """Gets the video_result of this DetectLiveByBase64IntlResponse.

        :return: The video_result of this DetectLiveByBase64IntlResponse.
        :rtype: :class:`huaweicloudsdkfrs.v2.LiveDetectRespVideoresult`
        """
        return self._video_result

    @video_result.setter
    def video_result(self, video_result):
        """Sets the video_result of this DetectLiveByBase64IntlResponse.

        :param video_result: The video_result of this DetectLiveByBase64IntlResponse.
        :type video_result: :class:`huaweicloudsdkfrs.v2.LiveDetectRespVideoresult`
        """
        self._video_result = video_result

    @property
    def warning_list(self):
        """Gets the warning_list of this DetectLiveByBase64IntlResponse.

        [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/api-face/face_02_0077.html)。调用失败时无此字段](tag:hc) [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0077.html)。调用失败时无此字段](tag:hk)

        :return: The warning_list of this DetectLiveByBase64IntlResponse.
        :rtype: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        """
        return self._warning_list

    @warning_list.setter
    def warning_list(self, warning_list):
        """Sets the warning_list of this DetectLiveByBase64IntlResponse.

        [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/api-face/face_02_0077.html)。调用失败时无此字段](tag:hc) [警告信息列表，WarningList结构见[WarningList](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0077.html)。调用失败时无此字段](tag:hk)

        :param warning_list: The warning_list of this DetectLiveByBase64IntlResponse.
        :type warning_list: list[:class:`huaweicloudsdkfrs.v2.WarningList`]
        """
        self._warning_list = warning_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DetectLiveByBase64IntlResponse.

        :return: The x_request_id of this DetectLiveByBase64IntlResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DetectLiveByBase64IntlResponse.

        :param x_request_id: The x_request_id of this DetectLiveByBase64IntlResponse.
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
        if not isinstance(other, DetectLiveByBase64IntlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
