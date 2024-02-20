# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criterion': 'Criterion',
        'key': 'str'
    }

    attribute_map = {
        'criterion': 'criterion',
        'key': 'key'
    }

    def __init__(self, criterion=None, key=None):
        """FindingFilter

        The model defined in huaweicloud sdk

        :param criterion: 
        :type criterion: :class:`huaweicloudsdkiamaccessanalyzer.v1.Criterion`
        :param key: 过滤键。
        :type key: str
        """
        
        

        self._criterion = None
        self._key = None
        self.discriminator = None

        self.criterion = criterion
        self.key = key

    @property
    def criterion(self):
        """Gets the criterion of this FindingFilter.

        :return: The criterion of this FindingFilter.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.Criterion`
        """
        return self._criterion

    @criterion.setter
    def criterion(self, criterion):
        """Sets the criterion of this FindingFilter.

        :param criterion: The criterion of this FindingFilter.
        :type criterion: :class:`huaweicloudsdkiamaccessanalyzer.v1.Criterion`
        """
        self._criterion = criterion

    @property
    def key(self):
        """Gets the key of this FindingFilter.

        过滤键。

        :return: The key of this FindingFilter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FindingFilter.

        过滤键。

        :param key: The key of this FindingFilter.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, FindingFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
