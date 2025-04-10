# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCursorTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cursor_time': 'int'
    }

    attribute_map = {
        'cursor_time': 'cursor_time'
    }

    def __init__(self, cursor_time=None):
        r"""ShowCursorTimeResponse

        The model defined in huaweicloud sdk

        :param cursor_time: 游标时间值
        :type cursor_time: int
        """
        
        super(ShowCursorTimeResponse, self).__init__()

        self._cursor_time = None
        self.discriminator = None

        if cursor_time is not None:
            self.cursor_time = cursor_time

    @property
    def cursor_time(self):
        r"""Gets the cursor_time of this ShowCursorTimeResponse.

        游标时间值

        :return: The cursor_time of this ShowCursorTimeResponse.
        :rtype: int
        """
        return self._cursor_time

    @cursor_time.setter
    def cursor_time(self, cursor_time):
        r"""Sets the cursor_time of this ShowCursorTimeResponse.

        游标时间值

        :param cursor_time: The cursor_time of this ShowCursorTimeResponse.
        :type cursor_time: int
        """
        self._cursor_time = cursor_time

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
        if not isinstance(other, ShowCursorTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
