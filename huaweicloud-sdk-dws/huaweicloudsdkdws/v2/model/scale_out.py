# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleOut:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'subnet_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, count=None, subnet_id=None):
        r"""ScaleOut

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 扩容节点数。 **取值范围**： 大于等于3。
        :type count: int
        :param subnet_id: **参数解释**： 子网ID。 **取值范围**： 同VPC下有效的子网ID。
        :type subnet_id: str
        """
        
        

        self._count = None
        self._subnet_id = None
        self.discriminator = None

        self.count = count
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def count(self):
        r"""Gets the count of this ScaleOut.

        **参数解释**： 扩容节点数。 **取值范围**： 大于等于3。

        :return: The count of this ScaleOut.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ScaleOut.

        **参数解释**： 扩容节点数。 **取值范围**： 大于等于3。

        :param count: The count of this ScaleOut.
        :type count: int
        """
        self._count = count

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ScaleOut.

        **参数解释**： 子网ID。 **取值范围**： 同VPC下有效的子网ID。

        :return: The subnet_id of this ScaleOut.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ScaleOut.

        **参数解释**： 子网ID。 **取值范围**： 同VPC下有效的子网ID。

        :param subnet_id: The subnet_id of this ScaleOut.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ScaleOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
