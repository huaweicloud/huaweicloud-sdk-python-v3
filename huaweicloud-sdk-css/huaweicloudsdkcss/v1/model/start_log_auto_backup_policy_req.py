# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartLogAutoBackupPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'period': 'str'
    }

    attribute_map = {
        'period': 'period'
    }

    def __init__(self, period=None):
        """StartLogAutoBackupPolicyReq

        The model defined in huaweicloud sdk

        :param period: 备份开始时间。格式：格林威治标准时间。
        :type period: str
        """
        
        

        self._period = None
        self.discriminator = None

        self.period = period

    @property
    def period(self):
        """Gets the period of this StartLogAutoBackupPolicyReq.

        备份开始时间。格式：格林威治标准时间。

        :return: The period of this StartLogAutoBackupPolicyReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this StartLogAutoBackupPolicyReq.

        备份开始时间。格式：格林威治标准时间。

        :param period: The period of this StartLogAutoBackupPolicyReq.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, StartLogAutoBackupPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
