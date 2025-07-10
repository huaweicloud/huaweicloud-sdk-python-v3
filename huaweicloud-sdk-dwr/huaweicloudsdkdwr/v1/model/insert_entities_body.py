# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertEntitiesBody:

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
        'data': 'list[dict(str, object)]'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'data': 'data'
    }

    def __init__(self, store_name=None, collection_name=None, data=None):
        r"""InsertEntitiesBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 约束限制： 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param collection_name: **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type collection_name: str
        :param data: **参数解释：** 插入collection的entity数据。 **约束限制：** 满足插入collection的field schema。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type data: list[dict(str, object)]
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._data = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        self.data = data

    @property
    def store_name(self):
        r"""Gets the store_name of this InsertEntitiesBody.

        **参数解释：** 知识仓实例名称，region内唯一。 约束限制： 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this InsertEntitiesBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this InsertEntitiesBody.

        **参数解释：** 知识仓实例名称，region内唯一。 约束限制： 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this InsertEntitiesBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this InsertEntitiesBody.

        **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The collection_name of this InsertEntitiesBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this InsertEntitiesBody.

        **参数解释：** collection名称，知识仓内唯一。 **约束限制：** 长度范围为1到255个字符，支持字母、数字、中划线（-）和下划线（_），大小写敏感。第一个字符只能够是下划线（_）和字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param collection_name: The collection_name of this InsertEntitiesBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def data(self):
        r"""Gets the data of this InsertEntitiesBody.

        **参数解释：** 插入collection的entity数据。 **约束限制：** 满足插入collection的field schema。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The data of this InsertEntitiesBody.
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this InsertEntitiesBody.

        **参数解释：** 插入collection的entity数据。 **约束限制：** 满足插入collection的field schema。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param data: The data of this InsertEntitiesBody.
        :type data: list[dict(str, object)]
        """
        self._data = data

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
        if not isinstance(other, InsertEntitiesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
