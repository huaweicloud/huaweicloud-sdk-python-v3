# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafCustomRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'overseas_type': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'overseas_type': 'overseas_type'
    }

    def __init__(self, domain_name=None, overseas_type=None):
        r"""ListWafCustomRuleRequest

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param overseas_type: 防护区域，0-大陆，1-海外
        :type overseas_type: int
        """
        
        

        self._domain_name = None
        self._overseas_type = None
        self.discriminator = None

        self.domain_name = domain_name
        self.overseas_type = overseas_type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListWafCustomRuleRequest.

        域名

        :return: The domain_name of this ListWafCustomRuleRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListWafCustomRuleRequest.

        域名

        :param domain_name: The domain_name of this ListWafCustomRuleRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this ListWafCustomRuleRequest.

        防护区域，0-大陆，1-海外

        :return: The overseas_type of this ListWafCustomRuleRequest.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this ListWafCustomRuleRequest.

        防护区域，0-大陆，1-海外

        :param overseas_type: The overseas_type of this ListWafCustomRuleRequest.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

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
        if not isinstance(other, ListWafCustomRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
