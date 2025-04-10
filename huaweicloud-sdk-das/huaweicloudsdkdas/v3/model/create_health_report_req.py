# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHealthReportReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_at': 'int',
        'end_at': 'int'
    }

    attribute_map = {
        'start_at': 'start_at',
        'end_at': 'end_at'
    }

    def __init__(self, start_at=None, end_at=None):
        r"""CreateHealthReportReq

        The model defined in huaweicloud sdk

        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        """
        
        

        self._start_at = None
        self._end_at = None
        self.discriminator = None

        self.start_at = start_at
        self.end_at = end_at

    @property
    def start_at(self):
        r"""Gets the start_at of this CreateHealthReportReq.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this CreateHealthReportReq.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this CreateHealthReportReq.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this CreateHealthReportReq.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this CreateHealthReportReq.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this CreateHealthReportReq.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this CreateHealthReportReq.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this CreateHealthReportReq.
        :type end_at: int
        """
        self._end_at = end_at

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
        if not isinstance(other, CreateHealthReportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
