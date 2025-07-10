# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectionsBody:

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
        'detail': 'bool'
    }

    attribute_map = {
        'store_name': 'store_name',
        'detail': 'detail'
    }

    def __init__(self, store_name=None, detail=None):
        r"""ListCollectionsBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param detail: **参数解释：** 列举collection的详细信息。 **约束限制：** 不涉及。 **取值范围：** true 或者 false。 **默认取值:** false。
        :type detail: bool
        """
        
        

        self._store_name = None
        self._detail = None
        self.discriminator = None

        self.store_name = store_name
        if detail is not None:
            self.detail = detail

    @property
    def store_name(self):
        r"""Gets the store_name of this ListCollectionsBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this ListCollectionsBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this ListCollectionsBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this ListCollectionsBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def detail(self):
        r"""Gets the detail of this ListCollectionsBody.

        **参数解释：** 列举collection的详细信息。 **约束限制：** 不涉及。 **取值范围：** true 或者 false。 **默认取值:** false。

        :return: The detail of this ListCollectionsBody.
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ListCollectionsBody.

        **参数解释：** 列举collection的详细信息。 **约束限制：** 不涉及。 **取值范围：** true 或者 false。 **默认取值:** false。

        :param detail: The detail of this ListCollectionsBody.
        :type detail: bool
        """
        self._detail = detail

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
        if not isinstance(other, ListCollectionsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
