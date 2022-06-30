# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStreamPortraitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stream_portraits': 'list[StreamPortrait]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'stream_portraits': 'stream_portraits',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, stream_portraits=None, x_request_id=None):
        """ShowStreamPortraitResponse

        The model defined in huaweicloud sdk

        :param stream_portraits: 播放画像信息列表。
        :type stream_portraits: list[:class:`huaweicloudsdklive.v2.StreamPortrait`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowStreamPortraitResponse, self).__init__()

        self._stream_portraits = None
        self._x_request_id = None
        self.discriminator = None

        if stream_portraits is not None:
            self.stream_portraits = stream_portraits
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def stream_portraits(self):
        """Gets the stream_portraits of this ShowStreamPortraitResponse.

        播放画像信息列表。

        :return: The stream_portraits of this ShowStreamPortraitResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.StreamPortrait`]
        """
        return self._stream_portraits

    @stream_portraits.setter
    def stream_portraits(self, stream_portraits):
        """Sets the stream_portraits of this ShowStreamPortraitResponse.

        播放画像信息列表。

        :param stream_portraits: The stream_portraits of this ShowStreamPortraitResponse.
        :type stream_portraits: list[:class:`huaweicloudsdklive.v2.StreamPortrait`]
        """
        self._stream_portraits = stream_portraits

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowStreamPortraitResponse.


        :return: The x_request_id of this ShowStreamPortraitResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowStreamPortraitResponse.


        :param x_request_id: The x_request_id of this ShowStreamPortraitResponse.
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
        if not isinstance(other, ShowStreamPortraitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
