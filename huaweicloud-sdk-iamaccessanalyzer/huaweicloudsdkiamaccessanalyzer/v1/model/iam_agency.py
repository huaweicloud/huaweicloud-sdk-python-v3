# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IAMAgency:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trust_policy': 'str'
    }

    attribute_map = {
        'trust_policy': 'trust_policy'
    }

    def __init__(self, trust_policy=None):
        """IAMAgency

        The model defined in huaweicloud sdk

        :param trust_policy: 此策略的json格式策略文档。
        :type trust_policy: str
        """
        
        

        self._trust_policy = None
        self.discriminator = None

        self.trust_policy = trust_policy

    @property
    def trust_policy(self):
        """Gets the trust_policy of this IAMAgency.

        此策略的json格式策略文档。

        :return: The trust_policy of this IAMAgency.
        :rtype: str
        """
        return self._trust_policy

    @trust_policy.setter
    def trust_policy(self, trust_policy):
        """Sets the trust_policy of this IAMAgency.

        此策略的json格式策略文档。

        :param trust_policy: The trust_policy of this IAMAgency.
        :type trust_policy: str
        """
        self._trust_policy = trust_policy

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
        if not isinstance(other, IAMAgency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
