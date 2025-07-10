# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEntitiesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'collection_name': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'filter': 'filter'
    }

    def __init__(self, store_name=None, collection_name=None, filter=None):
        r"""DeleteEntitiesBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param collection_name: **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type collection_name: str
        :param filter: **参数解释：** 用于过滤匹配entity的标量过滤条件。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type filter: str
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._filter = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        self.filter = filter

    @property
    def store_name(self):
        r"""Gets the store_name of this DeleteEntitiesBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this DeleteEntitiesBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this DeleteEntitiesBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this DeleteEntitiesBody.

        **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The collection_name of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this DeleteEntitiesBody.

        **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param collection_name: The collection_name of this DeleteEntitiesBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def filter(self):
        r"""Gets the filter of this DeleteEntitiesBody.

        **参数解释：** 用于过滤匹配entity的标量过滤条件。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The filter of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this DeleteEntitiesBody.

        **参数解释：** 用于过滤匹配entity的标量过滤条件。 **约束限制：** 要构建标量过滤条件，请参阅filter表达式规则。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param filter: The filter of this DeleteEntitiesBody.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, DeleteEntitiesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
