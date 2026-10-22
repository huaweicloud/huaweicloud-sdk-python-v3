# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBiactiveInstanceCandidatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'target_region_code': 'str',
        'target_instance_name': 'str',
        'data_sync_mode': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'target_region_code': 'target_region_code',
        'target_instance_name': 'target_instance_name',
        'data_sync_mode': 'data_sync_mode',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, target_region_code=None, target_instance_name=None, data_sync_mode=None, offset=None, limit=None):
        r"""ListBiactiveInstanceCandidatesRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释：** 实例ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type instance_id: str
        :param target_region_code: **参数解释：** 目标Region的编码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type target_region_code: str
        :param target_instance_name: **参数解释：** 按目标实例名称过滤。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type target_instance_name: str
        :param data_sync_mode: **参数解释：** 数据同步模式。 **约束限制：** 不涉及。 **取值范围：** - TABLE：表级数据同步模式。 **默认取值：** 不传该参数时表示实例级数据同步模式。
        :type data_sync_mode: str
        :param offset: **参数解释：** 索引位置偏移量，表示从最新一条记录开始偏移offset条数据后查询。 **约束限制：** 取值大于或等于0。 **取值范围：** 不涉及。 **默认取值：** 不传该参数时，查询偏移量默认为0。
        :type offset: int
        :param limit: **参数解释：** 查询实例个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 不传该参数时，默认查询前100条实例信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._target_region_code = None
        self._target_instance_name = None
        self._data_sync_mode = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.target_region_code = target_region_code
        if target_instance_name is not None:
            self.target_instance_name = target_instance_name
        if data_sync_mode is not None:
            self.data_sync_mode = data_sync_mode
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 实例ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The instance_id of this ListBiactiveInstanceCandidatesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 实例ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param instance_id: The instance_id of this ListBiactiveInstanceCandidatesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def target_region_code(self):
        r"""Gets the target_region_code of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 目标Region的编码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_region_code of this ListBiactiveInstanceCandidatesRequest.
        :rtype: str
        """
        return self._target_region_code

    @target_region_code.setter
    def target_region_code(self, target_region_code):
        r"""Sets the target_region_code of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 目标Region的编码。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param target_region_code: The target_region_code of this ListBiactiveInstanceCandidatesRequest.
        :type target_region_code: str
        """
        self._target_region_code = target_region_code

    @property
    def target_instance_name(self):
        r"""Gets the target_instance_name of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 按目标实例名称过滤。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_instance_name of this ListBiactiveInstanceCandidatesRequest.
        :rtype: str
        """
        return self._target_instance_name

    @target_instance_name.setter
    def target_instance_name(self, target_instance_name):
        r"""Sets the target_instance_name of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 按目标实例名称过滤。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param target_instance_name: The target_instance_name of this ListBiactiveInstanceCandidatesRequest.
        :type target_instance_name: str
        """
        self._target_instance_name = target_instance_name

    @property
    def data_sync_mode(self):
        r"""Gets the data_sync_mode of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 数据同步模式。 **约束限制：** 不涉及。 **取值范围：** - TABLE：表级数据同步模式。 **默认取值：** 不传该参数时表示实例级数据同步模式。

        :return: The data_sync_mode of this ListBiactiveInstanceCandidatesRequest.
        :rtype: str
        """
        return self._data_sync_mode

    @data_sync_mode.setter
    def data_sync_mode(self, data_sync_mode):
        r"""Sets the data_sync_mode of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 数据同步模式。 **约束限制：** 不涉及。 **取值范围：** - TABLE：表级数据同步模式。 **默认取值：** 不传该参数时表示实例级数据同步模式。

        :param data_sync_mode: The data_sync_mode of this ListBiactiveInstanceCandidatesRequest.
        :type data_sync_mode: str
        """
        self._data_sync_mode = data_sync_mode

    @property
    def offset(self):
        r"""Gets the offset of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 索引位置偏移量，表示从最新一条记录开始偏移offset条数据后查询。 **约束限制：** 取值大于或等于0。 **取值范围：** 不涉及。 **默认取值：** 不传该参数时，查询偏移量默认为0。

        :return: The offset of this ListBiactiveInstanceCandidatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 索引位置偏移量，表示从最新一条记录开始偏移offset条数据后查询。 **约束限制：** 取值大于或等于0。 **取值范围：** 不涉及。 **默认取值：** 不传该参数时，查询偏移量默认为0。

        :param offset: The offset of this ListBiactiveInstanceCandidatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 查询实例个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListBiactiveInstanceCandidatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBiactiveInstanceCandidatesRequest.

        **参数解释：** 查询实例个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListBiactiveInstanceCandidatesRequest.
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
        if not isinstance(other, ListBiactiveInstanceCandidatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
