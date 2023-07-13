# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcRealtimeScaleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale': 'list[TimeValueData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'scale': 'scale',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, scale=None, x_request_id=None):
        """ListRtcRealtimeScaleResponse

        The model defined in huaweicloud sdk

        :param scale: 时间戳及相应时间的指标数值列表
        :type scale: list[:class:`huaweicloudsdkcloudrtc.v1.TimeValueData`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcRealtimeScaleResponse, self).__init__()

        self._scale = None
        self._x_request_id = None
        self.discriminator = None

        if scale is not None:
            self.scale = scale
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def scale(self):
        """Gets the scale of this ListRtcRealtimeScaleResponse.

        时间戳及相应时间的指标数值列表

        :return: The scale of this ListRtcRealtimeScaleResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.TimeValueData`]
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this ListRtcRealtimeScaleResponse.

        时间戳及相应时间的指标数值列表

        :param scale: The scale of this ListRtcRealtimeScaleResponse.
        :type scale: list[:class:`huaweicloudsdkcloudrtc.v1.TimeValueData`]
        """
        self._scale = scale

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcRealtimeScaleResponse.

        :return: The x_request_id of this ListRtcRealtimeScaleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcRealtimeScaleResponse.

        :param x_request_id: The x_request_id of this ListRtcRealtimeScaleResponse.
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
        if not isinstance(other, ListRtcRealtimeScaleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
