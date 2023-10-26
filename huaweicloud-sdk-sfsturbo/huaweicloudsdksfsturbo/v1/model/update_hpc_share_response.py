# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHpcShareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gc_time': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'gc_time': 'gc_time',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, gc_time=None, x_request_id=None):
        """UpdateHpcShareResponse

        The model defined in huaweicloud sdk

        :param gc_time: 文件系统 gc_time
        :type gc_time: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateHpcShareResponse, self).__init__()

        self._gc_time = None
        self._x_request_id = None
        self.discriminator = None

        if gc_time is not None:
            self.gc_time = gc_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def gc_time(self):
        """Gets the gc_time of this UpdateHpcShareResponse.

        文件系统 gc_time

        :return: The gc_time of this UpdateHpcShareResponse.
        :rtype: int
        """
        return self._gc_time

    @gc_time.setter
    def gc_time(self, gc_time):
        """Sets the gc_time of this UpdateHpcShareResponse.

        文件系统 gc_time

        :param gc_time: The gc_time of this UpdateHpcShareResponse.
        :type gc_time: int
        """
        self._gc_time = gc_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateHpcShareResponse.

        :return: The x_request_id of this UpdateHpcShareResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateHpcShareResponse.

        :param x_request_id: The x_request_id of this UpdateHpcShareResponse.
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
        if not isinstance(other, UpdateHpcShareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
