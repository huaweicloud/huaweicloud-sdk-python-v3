# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreRuntimeVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, runtime_id=None, offset=None, limit=None):
        r"""ListCoreRuntimeVersionsRequest

        The model defined in huaweicloud sdk

        :param runtime_id: 运行时ID，用于唯一标识一个Agent运行时实例。
        :type runtime_id: str
        :param offset: **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1
        :type offset: int
        :param limit: **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10
        :type limit: int
        """
        
        

        self._runtime_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.runtime_id = runtime_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this ListCoreRuntimeVersionsRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :return: The runtime_id of this ListCoreRuntimeVersionsRequest.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ListCoreRuntimeVersionsRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :param runtime_id: The runtime_id of this ListCoreRuntimeVersionsRequest.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreRuntimeVersionsRequest.

        **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1

        :return: The offset of this ListCoreRuntimeVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreRuntimeVersionsRequest.

        **参数解释**：  分页起始页码，默认值为1。 **约束限制**: 不涉及。 **取值范围**： 1 - 1000 **默认取值**: 1

        :param offset: The offset of this ListCoreRuntimeVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreRuntimeVersionsRequest.

        **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10

        :return: The limit of this ListCoreRuntimeVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreRuntimeVersionsRequest.

        **参数解释**：  每页记录数，默认值为10。 **约束限制**: 不涉及。 **取值范围**： 10 - 100 **默认取值**: 10

        :param limit: The limit of this ListCoreRuntimeVersionsRequest.
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
        if not isinstance(other, ListCoreRuntimeVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
