# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyReadAndWriteStrategyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_weight': 'object'
    }

    attribute_map = {
        'read_weight': 'read_weight'
    }

    def __init__(self, read_weight=None):
        r"""ModifyReadAndWriteStrategyReq

        The model defined in huaweicloud sdk

        :param read_weight: 主数据库实例与只读数据库实例的读权重集合。
        :type read_weight: object
        """
        
        

        self._read_weight = None
        self.discriminator = None

        self.read_weight = read_weight

    @property
    def read_weight(self):
        r"""Gets the read_weight of this ModifyReadAndWriteStrategyReq.

        主数据库实例与只读数据库实例的读权重集合。

        :return: The read_weight of this ModifyReadAndWriteStrategyReq.
        :rtype: object
        """
        return self._read_weight

    @read_weight.setter
    def read_weight(self, read_weight):
        r"""Sets the read_weight of this ModifyReadAndWriteStrategyReq.

        主数据库实例与只读数据库实例的读权重集合。

        :param read_weight: The read_weight of this ModifyReadAndWriteStrategyReq.
        :type read_weight: object
        """
        self._read_weight = read_weight

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
        if not isinstance(other, ModifyReadAndWriteStrategyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
