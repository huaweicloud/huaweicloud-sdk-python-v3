# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedReasonRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'count': 'int'
    }

    attribute_map = {
        'reason': 'reason',
        'count': 'count'
    }

    def __init__(self, reason=None, count=None):
        r"""FailedReasonRecord

        The model defined in huaweicloud sdk

        :param reason: 失败原因
        :type reason: str
        :param count: 失败数量
        :type count: int
        """
        
        

        self._reason = None
        self._count = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if count is not None:
            self.count = count

    @property
    def reason(self):
        r"""Gets the reason of this FailedReasonRecord.

        失败原因

        :return: The reason of this FailedReasonRecord.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailedReasonRecord.

        失败原因

        :param reason: The reason of this FailedReasonRecord.
        :type reason: str
        """
        self._reason = reason

    @property
    def count(self):
        r"""Gets the count of this FailedReasonRecord.

        失败数量

        :return: The count of this FailedReasonRecord.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this FailedReasonRecord.

        失败数量

        :param count: The count of this FailedReasonRecord.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, FailedReasonRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
