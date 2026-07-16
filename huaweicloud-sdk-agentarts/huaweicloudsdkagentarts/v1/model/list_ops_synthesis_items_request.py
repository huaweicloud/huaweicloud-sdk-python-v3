# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsSynthesisItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'synthesis_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'synthesis_id': 'synthesis_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, synthesis_id=None, offset=None, limit=None):
        r"""ListOpsSynthesisItemsRequest

        The model defined in huaweicloud sdk

        :param synthesis_id: **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 
        :type synthesis_id: str
        :param offset: **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 
        :type limit: int
        """
        
        

        self._synthesis_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.synthesis_id = synthesis_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def synthesis_id(self):
        r"""Gets the synthesis_id of this ListOpsSynthesisItemsRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 

        :return: The synthesis_id of this ListOpsSynthesisItemsRequest.
        :rtype: str
        """
        return self._synthesis_id

    @synthesis_id.setter
    def synthesis_id(self, synthesis_id):
        r"""Sets the synthesis_id of this ListOpsSynthesisItemsRequest.

        **参数解释：** 合成任务的唯一标识符（ID），该参数用于在路径中指定特定的合成任务，以便执行查询、停止或删除等操作。 **约束限制：** 字符串长度限制为1到64个字符。通常采用标准 UUID格式。 **取值范围：** 1-64位字符。 **默认取值：** 不涉及。 

        :param synthesis_id: The synthesis_id of this ListOpsSynthesisItemsRequest.
        :type synthesis_id: str
        """
        self._synthesis_id = synthesis_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsSynthesisItemsRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :return: The offset of this ListOpsSynthesisItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsSynthesisItemsRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsSynthesisItemsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsSynthesisItemsRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :return: The limit of this ListOpsSynthesisItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsSynthesisItemsRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :param limit: The limit of this ListOpsSynthesisItemsRequest.
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
        if not isinstance(other, ListOpsSynthesisItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
