# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpaceBuiltinStrategiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, limit=None, offset=None):
        r"""ListCoreSpaceBuiltinStrategiesRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 每页返回的最大结果数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 50。 
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        """
        
        

        self._limit = None
        self._offset = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreSpaceBuiltinStrategiesRequest.

        **参数解释：** 每页返回的最大结果数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 50。 

        :return: The limit of this ListCoreSpaceBuiltinStrategiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreSpaceBuiltinStrategiesRequest.

        **参数解释：** 每页返回的最大结果数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 50。 

        :param limit: The limit of this ListCoreSpaceBuiltinStrategiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreSpaceBuiltinStrategiesRequest.

        **参数解释：** 返回结果偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListCoreSpaceBuiltinStrategiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreSpaceBuiltinStrategiesRequest.

        **参数解释：** 返回结果偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListCoreSpaceBuiltinStrategiesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCoreSpaceBuiltinStrategiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
