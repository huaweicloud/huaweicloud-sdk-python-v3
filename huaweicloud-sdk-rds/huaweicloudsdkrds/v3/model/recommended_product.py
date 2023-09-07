# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecommendedProduct:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recommended_level': 'str',
        'application_scenarios': 'str',
        'flavors': 'list[RecommendFlavor]'
    }

    attribute_map = {
        'recommended_level': 'recommended_level',
        'application_scenarios': 'application_scenarios',
        'flavors': 'flavors'
    }

    def __init__(self, recommended_level=None, application_scenarios=None, flavors=None):
        """RecommendedProduct

        The model defined in huaweicloud sdk

        :param recommended_level: 推荐级别
        :type recommended_level: str
        :param application_scenarios: 应用场景
        :type application_scenarios: str
        :param flavors: 规格信息
        :type flavors: list[:class:`huaweicloudsdkrds.v3.RecommendFlavor`]
        """
        
        

        self._recommended_level = None
        self._application_scenarios = None
        self._flavors = None
        self.discriminator = None

        self.recommended_level = recommended_level
        self.application_scenarios = application_scenarios
        self.flavors = flavors

    @property
    def recommended_level(self):
        """Gets the recommended_level of this RecommendedProduct.

        推荐级别

        :return: The recommended_level of this RecommendedProduct.
        :rtype: str
        """
        return self._recommended_level

    @recommended_level.setter
    def recommended_level(self, recommended_level):
        """Sets the recommended_level of this RecommendedProduct.

        推荐级别

        :param recommended_level: The recommended_level of this RecommendedProduct.
        :type recommended_level: str
        """
        self._recommended_level = recommended_level

    @property
    def application_scenarios(self):
        """Gets the application_scenarios of this RecommendedProduct.

        应用场景

        :return: The application_scenarios of this RecommendedProduct.
        :rtype: str
        """
        return self._application_scenarios

    @application_scenarios.setter
    def application_scenarios(self, application_scenarios):
        """Sets the application_scenarios of this RecommendedProduct.

        应用场景

        :param application_scenarios: The application_scenarios of this RecommendedProduct.
        :type application_scenarios: str
        """
        self._application_scenarios = application_scenarios

    @property
    def flavors(self):
        """Gets the flavors of this RecommendedProduct.

        规格信息

        :return: The flavors of this RecommendedProduct.
        :rtype: list[:class:`huaweicloudsdkrds.v3.RecommendFlavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        """Sets the flavors of this RecommendedProduct.

        规格信息

        :param flavors: The flavors of this RecommendedProduct.
        :type flavors: list[:class:`huaweicloudsdkrds.v3.RecommendFlavor`]
        """
        self._flavors = flavors

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
        if not isinstance(other, RecommendedProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
