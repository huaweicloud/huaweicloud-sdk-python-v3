# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticStatusV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unresolved': 'int',
        'resolved': 'int',
        'dismissed': 'int'
    }

    attribute_map = {
        'unresolved': 'unresolved',
        'resolved': 'resolved',
        'dismissed': 'dismissed'
    }

    def __init__(self, unresolved=None, resolved=None, dismissed=None):
        """StatisticStatusV2

        The model defined in huaweicloud sdk

        :param unresolved: 未解决
        :type unresolved: int
        :param resolved: 已解决
        :type resolved: int
        :param dismissed: 已忽略
        :type dismissed: int
        """
        
        

        self._unresolved = None
        self._resolved = None
        self._dismissed = None
        self.discriminator = None

        if unresolved is not None:
            self.unresolved = unresolved
        if resolved is not None:
            self.resolved = resolved
        if dismissed is not None:
            self.dismissed = dismissed

    @property
    def unresolved(self):
        """Gets the unresolved of this StatisticStatusV2.

        未解决

        :return: The unresolved of this StatisticStatusV2.
        :rtype: int
        """
        return self._unresolved

    @unresolved.setter
    def unresolved(self, unresolved):
        """Sets the unresolved of this StatisticStatusV2.

        未解决

        :param unresolved: The unresolved of this StatisticStatusV2.
        :type unresolved: int
        """
        self._unresolved = unresolved

    @property
    def resolved(self):
        """Gets the resolved of this StatisticStatusV2.

        已解决

        :return: The resolved of this StatisticStatusV2.
        :rtype: int
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this StatisticStatusV2.

        已解决

        :param resolved: The resolved of this StatisticStatusV2.
        :type resolved: int
        """
        self._resolved = resolved

    @property
    def dismissed(self):
        """Gets the dismissed of this StatisticStatusV2.

        已忽略

        :return: The dismissed of this StatisticStatusV2.
        :rtype: int
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this StatisticStatusV2.

        已忽略

        :param dismissed: The dismissed of this StatisticStatusV2.
        :type dismissed: int
        """
        self._dismissed = dismissed

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
        if not isinstance(other, StatisticStatusV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
