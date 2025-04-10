# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnlockNodeReadonlyStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_preservation_time': 'int'
    }

    attribute_map = {
        'status_preservation_time': 'status_preservation_time'
    }

    def __init__(self, status_preservation_time=None):
        r"""UnlockNodeReadonlyStatusRequestBody

        The model defined in huaweicloud sdk

        :param status_preservation_time: Ha保持不再设置节点只读状态的时间，单位为分钟。
        :type status_preservation_time: int
        """
        
        

        self._status_preservation_time = None
        self.discriminator = None

        self.status_preservation_time = status_preservation_time

    @property
    def status_preservation_time(self):
        r"""Gets the status_preservation_time of this UnlockNodeReadonlyStatusRequestBody.

        Ha保持不再设置节点只读状态的时间，单位为分钟。

        :return: The status_preservation_time of this UnlockNodeReadonlyStatusRequestBody.
        :rtype: int
        """
        return self._status_preservation_time

    @status_preservation_time.setter
    def status_preservation_time(self, status_preservation_time):
        r"""Sets the status_preservation_time of this UnlockNodeReadonlyStatusRequestBody.

        Ha保持不再设置节点只读状态的时间，单位为分钟。

        :param status_preservation_time: The status_preservation_time of this UnlockNodeReadonlyStatusRequestBody.
        :type status_preservation_time: int
        """
        self._status_preservation_time = status_preservation_time

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
        if not isinstance(other, UnlockNodeReadonlyStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
