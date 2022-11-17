# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'behavior_type': 'str',
        'threshold': 'float',
        'deduplication': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'behavior_type': 'behavior_type',
        'threshold': 'threshold',
        'deduplication': 'deduplication'
    }

    def __init__(self, alias=None, behavior_type=None, threshold=None, deduplication=None):
        """CustomizeParameter

        The model defined in huaweicloud sdk

        :param alias: 别名。
        :type alias: str
        :param behavior_type: 行为类型。
        :type behavior_type: str
        :param threshold: 阈值。
        :type threshold: float
        :param deduplication: 去重。
        :type deduplication: str
        """
        
        

        self._alias = None
        self._behavior_type = None
        self._threshold = None
        self._deduplication = None
        self.discriminator = None

        self.alias = alias
        self.behavior_type = behavior_type
        if threshold is not None:
            self.threshold = threshold
        self.deduplication = deduplication

    @property
    def alias(self):
        """Gets the alias of this CustomizeParameter.

        别名。

        :return: The alias of this CustomizeParameter.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CustomizeParameter.

        别名。

        :param alias: The alias of this CustomizeParameter.
        :type alias: str
        """
        self._alias = alias

    @property
    def behavior_type(self):
        """Gets the behavior_type of this CustomizeParameter.

        行为类型。

        :return: The behavior_type of this CustomizeParameter.
        :rtype: str
        """
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, behavior_type):
        """Sets the behavior_type of this CustomizeParameter.

        行为类型。

        :param behavior_type: The behavior_type of this CustomizeParameter.
        :type behavior_type: str
        """
        self._behavior_type = behavior_type

    @property
    def threshold(self):
        """Gets the threshold of this CustomizeParameter.

        阈值。

        :return: The threshold of this CustomizeParameter.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CustomizeParameter.

        阈值。

        :param threshold: The threshold of this CustomizeParameter.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def deduplication(self):
        """Gets the deduplication of this CustomizeParameter.

        去重。

        :return: The deduplication of this CustomizeParameter.
        :rtype: str
        """
        return self._deduplication

    @deduplication.setter
    def deduplication(self, deduplication):
        """Sets the deduplication of this CustomizeParameter.

        去重。

        :param deduplication: The deduplication of this CustomizeParameter.
        :type deduplication: str
        """
        self._deduplication = deduplication

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
        if not isinstance(other, CustomizeParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
