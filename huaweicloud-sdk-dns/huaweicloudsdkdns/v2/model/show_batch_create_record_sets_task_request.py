# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchCreateRecordSetsTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_id': 'str',
        'error_item_limit': 'int',
        'error_item_offset': 'int'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'error_item_limit': 'error_item_limit',
        'error_item_offset': 'error_item_offset'
    }

    def __init__(self, zone_id=None, error_item_limit=None, error_item_offset=None):
        r"""ShowBatchCreateRecordSetsTaskRequest

        The model defined in huaweicloud sdk

        :param zone_id: **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type zone_id: str
        :param error_item_limit: **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 2000
        :type error_item_limit: int
        :param error_item_offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 0
        :type error_item_offset: int
        """
        
        

        self._zone_id = None
        self._error_item_limit = None
        self._error_item_offset = None
        self.discriminator = None

        self.zone_id = zone_id
        if error_item_limit is not None:
            self.error_item_limit = error_item_limit
        if error_item_offset is not None:
            self.error_item_offset = error_item_offset

    @property
    def zone_id(self):
        r"""Gets the zone_id of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The zone_id of this ShowBatchCreateRecordSetsTaskRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 域名ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param zone_id: The zone_id of this ShowBatchCreateRecordSetsTaskRequest.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def error_item_limit(self):
        r"""Gets the error_item_limit of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 2000

        :return: The error_item_limit of this ShowBatchCreateRecordSetsTaskRequest.
        :rtype: int
        """
        return self._error_item_limit

    @error_item_limit.setter
    def error_item_limit(self, error_item_limit):
        r"""Sets the error_item_limit of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 分页查询时配置每页返回的失败条目个数。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 2000

        :param error_item_limit: The error_item_limit of this ShowBatchCreateRecordSetsTaskRequest.
        :type error_item_limit: int
        """
        self._error_item_limit = error_item_limit

    @property
    def error_item_offset(self):
        r"""Gets the error_item_offset of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 0

        :return: The error_item_offset of this ShowBatchCreateRecordSetsTaskRequest.
        :rtype: int
        """
        return self._error_item_offset

    @error_item_offset.setter
    def error_item_offset(self, error_item_offset):
        r"""Sets the error_item_offset of this ShowBatchCreateRecordSetsTaskRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个失败条目开始查询。 **约束限制：** 不涉及。 **取值范围：** 0~2000。 **默认取值：** 0

        :param error_item_offset: The error_item_offset of this ShowBatchCreateRecordSetsTaskRequest.
        :type error_item_offset: int
        """
        self._error_item_offset = error_item_offset

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
        if not isinstance(other, ShowBatchCreateRecordSetsTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
