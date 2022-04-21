# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetentionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'rules': 'list[Rule]'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'rules': 'rules'
    }

    def __init__(self, algorithm=None, rules=None):
        """CreateRetentionRequestBody

        The model defined in huaweicloud sdk

        :param algorithm: 回收规则匹配策略，固定为\&quot;or\&quot;
        :type algorithm: str
        :param rules: 镜像老化规则
        :type rules: list[:class:`huaweicloudsdkswr.v2.Rule`]
        """
        
        

        self._algorithm = None
        self._rules = None
        self.discriminator = None

        self.algorithm = algorithm
        self.rules = rules

    @property
    def algorithm(self):
        """Gets the algorithm of this CreateRetentionRequestBody.

        回收规则匹配策略，固定为\"or\"

        :return: The algorithm of this CreateRetentionRequestBody.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this CreateRetentionRequestBody.

        回收规则匹配策略，固定为\"or\"

        :param algorithm: The algorithm of this CreateRetentionRequestBody.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def rules(self):
        """Gets the rules of this CreateRetentionRequestBody.

        镜像老化规则

        :return: The rules of this CreateRetentionRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CreateRetentionRequestBody.

        镜像老化规则

        :param rules: The rules of this CreateRetentionRequestBody.
        :type rules: list[:class:`huaweicloudsdkswr.v2.Rule`]
        """
        self._rules = rules

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
        if not isinstance(other, CreateRetentionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
