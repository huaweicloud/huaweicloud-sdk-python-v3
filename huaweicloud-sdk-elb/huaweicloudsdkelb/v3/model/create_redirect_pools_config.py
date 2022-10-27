# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedirectPoolsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'weight': 'weight'
    }

    def __init__(self, pool_id=None, weight=None):
        """CreateRedirectPoolsConfig

        The model defined in huaweicloud sdk

        :param pool_id: 后端主机组的ID。
        :type pool_id: str
        :param weight: 后端主机组的权重。  取值：0-100。
        :type weight: int
        """
        
        

        self._pool_id = None
        self._weight = None
        self.discriminator = None

        self.pool_id = pool_id
        self.weight = weight

    @property
    def pool_id(self):
        """Gets the pool_id of this CreateRedirectPoolsConfig.

        后端主机组的ID。

        :return: The pool_id of this CreateRedirectPoolsConfig.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this CreateRedirectPoolsConfig.

        后端主机组的ID。

        :param pool_id: The pool_id of this CreateRedirectPoolsConfig.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def weight(self):
        """Gets the weight of this CreateRedirectPoolsConfig.

        后端主机组的权重。  取值：0-100。

        :return: The weight of this CreateRedirectPoolsConfig.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateRedirectPoolsConfig.

        后端主机组的权重。  取值：0-100。

        :param weight: The weight of this CreateRedirectPoolsConfig.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, CreateRedirectPoolsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
