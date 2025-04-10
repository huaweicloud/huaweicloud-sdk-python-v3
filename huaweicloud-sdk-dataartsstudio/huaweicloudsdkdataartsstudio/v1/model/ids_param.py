# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdsParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'del_types': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'del_types': 'del_types'
    }

    def __init__(self, ids=None, del_types=None):
        r"""IdsParam

        The model defined in huaweicloud sdk

        :param ids: ID列表，ID字符串。
        :type ids: list[str]
        :param del_types: 删除物理表。 枚举值：   - PHYSICAL_TABLE: 关系建模 
        :type del_types: str
        """
        
        

        self._ids = None
        self._del_types = None
        self.discriminator = None

        self.ids = ids
        if del_types is not None:
            self.del_types = del_types

    @property
    def ids(self):
        r"""Gets the ids of this IdsParam.

        ID列表，ID字符串。

        :return: The ids of this IdsParam.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this IdsParam.

        ID列表，ID字符串。

        :param ids: The ids of this IdsParam.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def del_types(self):
        r"""Gets the del_types of this IdsParam.

        删除物理表。 枚举值：   - PHYSICAL_TABLE: 关系建模 

        :return: The del_types of this IdsParam.
        :rtype: str
        """
        return self._del_types

    @del_types.setter
    def del_types(self, del_types):
        r"""Sets the del_types of this IdsParam.

        删除物理表。 枚举值：   - PHYSICAL_TABLE: 关系建模 

        :param del_types: The del_types of this IdsParam.
        :type del_types: str
        """
        self._del_types = del_types

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
        if not isinstance(other, IdsParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
