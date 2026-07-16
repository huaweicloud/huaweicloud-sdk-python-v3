# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreRuntimesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_ids': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'runtime_ids': 'runtime_ids',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, runtime_ids=None, name=None, offset=None, limit=None):
        r"""ListCoreRuntimesRequest

        The model defined in huaweicloud sdk

        :param runtime_ids: **参数解释**：  运行时ID列表精确查询，可选参数，如果有多个ID，ID之间用逗号分隔。 **约束限制**: 支持批量查询多个运行时ID，最多支持10个ID。
        :type runtime_ids: str
        :param name: **参数解释**：  Agent运行时名称，必须以字母开头，只包含字母数字和连字符。 **约束限制**: 不涉及。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。
        :type name: str
        :param offset: **参数解释**： 分页查询偏移量，表示从第几条记录开始查询，从1开始。 **默认取值**: 1
        :type offset: int
        :param limit: **参数解释**： 每页返回的记录数。 **默认取值**: 10
        :type limit: int
        """
        
        

        self._runtime_ids = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if runtime_ids is not None:
            self.runtime_ids = runtime_ids
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def runtime_ids(self):
        r"""Gets the runtime_ids of this ListCoreRuntimesRequest.

        **参数解释**：  运行时ID列表精确查询，可选参数，如果有多个ID，ID之间用逗号分隔。 **约束限制**: 支持批量查询多个运行时ID，最多支持10个ID。

        :return: The runtime_ids of this ListCoreRuntimesRequest.
        :rtype: str
        """
        return self._runtime_ids

    @runtime_ids.setter
    def runtime_ids(self, runtime_ids):
        r"""Sets the runtime_ids of this ListCoreRuntimesRequest.

        **参数解释**：  运行时ID列表精确查询，可选参数，如果有多个ID，ID之间用逗号分隔。 **约束限制**: 支持批量查询多个运行时ID，最多支持10个ID。

        :param runtime_ids: The runtime_ids of this ListCoreRuntimesRequest.
        :type runtime_ids: str
        """
        self._runtime_ids = runtime_ids

    @property
    def name(self):
        r"""Gets the name of this ListCoreRuntimesRequest.

        **参数解释**：  Agent运行时名称，必须以字母开头，只包含字母数字和连字符。 **约束限制**: 不涉及。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。

        :return: The name of this ListCoreRuntimesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCoreRuntimesRequest.

        **参数解释**：  Agent运行时名称，必须以字母开头，只包含字母数字和连字符。 **约束限制**: 不涉及。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。

        :param name: The name of this ListCoreRuntimesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreRuntimesRequest.

        **参数解释**： 分页查询偏移量，表示从第几条记录开始查询，从1开始。 **默认取值**: 1

        :return: The offset of this ListCoreRuntimesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreRuntimesRequest.

        **参数解释**： 分页查询偏移量，表示从第几条记录开始查询，从1开始。 **默认取值**: 1

        :param offset: The offset of this ListCoreRuntimesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreRuntimesRequest.

        **参数解释**： 每页返回的记录数。 **默认取值**: 10

        :return: The limit of this ListCoreRuntimesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreRuntimesRequest.

        **参数解释**： 每页返回的记录数。 **默认取值**: 10

        :param limit: The limit of this ListCoreRuntimesRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCoreRuntimesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
