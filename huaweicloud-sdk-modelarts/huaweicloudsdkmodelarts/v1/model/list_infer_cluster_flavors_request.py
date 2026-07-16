# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferClusterFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'flavor_type': 'flavor_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, flavor_type=None, limit=None, offset=None):
        r"""ListInferClusterFlavorsRequest

        The model defined in huaweicloud sdk

        :param flavor_type: **参数解释：** 规格类型。 **约束限制：** 不涉及。 **取值范围：** - CPU - GPU - ASCEND **默认取值：** 不涉及。
        :type flavor_type: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        """
        
        

        self._flavor_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if flavor_type is not None:
            self.flavor_type = flavor_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this ListInferClusterFlavorsRequest.

        **参数解释：** 规格类型。 **约束限制：** 不涉及。 **取值范围：** - CPU - GPU - ASCEND **默认取值：** 不涉及。

        :return: The flavor_type of this ListInferClusterFlavorsRequest.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this ListInferClusterFlavorsRequest.

        **参数解释：** 规格类型。 **约束限制：** 不涉及。 **取值范围：** - CPU - GPU - ASCEND **默认取值：** 不涉及。

        :param flavor_type: The flavor_type of this ListInferClusterFlavorsRequest.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def limit(self):
        r"""Gets the limit of this ListInferClusterFlavorsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferClusterFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferClusterFlavorsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferClusterFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferClusterFlavorsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferClusterFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferClusterFlavorsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferClusterFlavorsRequest.
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
        if not isinstance(other, ListInferClusterFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
