# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LicensePropertyRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'values': 'list[str]',
        'predicate': 'str'
    }

    attribute_map = {
        'values': 'values',
        'predicate': 'predicate'
    }

    def __init__(self, values=None, predicate=None):
        """LicensePropertyRules

        The model defined in huaweicloud sdk

        :param values: license详情
        :type values: list[str]
        :param predicate: 比较规则
        :type predicate: str
        """
        
        

        self._values = None
        self._predicate = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if predicate is not None:
            self.predicate = predicate

    @property
    def values(self):
        """Gets the values of this LicensePropertyRules.

        license详情

        :return: The values of this LicensePropertyRules.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this LicensePropertyRules.

        license详情

        :param values: The values of this LicensePropertyRules.
        :type values: list[str]
        """
        self._values = values

    @property
    def predicate(self):
        """Gets the predicate of this LicensePropertyRules.

        比较规则

        :return: The predicate of this LicensePropertyRules.
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this LicensePropertyRules.

        比较规则

        :param predicate: The predicate of this LicensePropertyRules.
        :type predicate: str
        """
        self._predicate = predicate

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
        if not isinstance(other, LicensePropertyRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
