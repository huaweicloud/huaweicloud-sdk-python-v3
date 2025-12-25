# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsRequest:

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
        'backup_id': 'str',
        'backup_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'mode': 'str',
        'order_field': 'str',
        'order_rule': 'str',
        'backup_status': 'str',
        'backup_name': 'str',
        'backup_description': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'mode': 'mode',
        'order_field': 'order_field',
        'order_rule': 'order_rule',
        'backup_status': 'backup_status',
        'backup_name': 'backup_name',
        'backup_description': 'backup_description',
        'instance_name': 'instance_name'
    }

    def __init__(self, instance_id=None, backup_id=None, backup_type=None, offset=None, limit=None, begin_time=None, end_time=None, mode=None, order_field=None, order_rule=None, backup_status=None, backup_name=None, backup_description=None, instance_name=None):
        r"""ListBackupsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释：** 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。如果instance_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的instance_id精确匹配查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type instance_id: str
        :param backup_id: **参数解释：** 备份ID。如果backup_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的backup_id精确匹配查询。 **约束限制：** 当该字段传入的备份ID归属为自动增量备份时，实例ID必传，且实例ID必须为精确匹配。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type backup_id: str
        :param backup_type: **参数解释：** 备份类型。 **约束限制：** 当该字段取值为“Incremental”时，实例ID必传。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。  **默认取值：** 不涉及。
        :type backup_type: str
        :param offset: **参数解释：** 索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。 **约束限制：** 不涉及。 **取值范围：** 大于或等于0。 **默认取值：** 0，表示从最新的备份创建时间对应的备份开始查询。
        :type offset: int
        :param limit: **参数解释：** 查询备份个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 100。不传该参数时，默认查询前100条备份信息。
        :type limit: int
        :param begin_time: **参数解释：** 查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “end_time”有值时，“begin_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type begin_time: str
        :param end_time: **参数解释：** 查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “begin_time”有值时，“end_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type end_time: str
        :param mode: **参数解释：** 实例模式。 **约束限制：** 不涉及。 **取值范围：** - Sharding - ReplicaSet - Single  **默认取值：** 不涉及。
        :type mode: str
        :param order_field: **参数解释：** 排序字段。 **约束限制：** “order_rule”有值时，“order_field”必选。 **取值范围：** - name，备份名称。 - instanceName，实例名称。 - type，备份类型。 - datastoreType，引擎类型。 - beginTime，开始时间。 - status，备份状态。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。
        :type order_field: str
        :param order_rule: **参数解释：** 排序规则。 **约束限制：** “order_field”有值时，“order_rule”必选。 **取值范围：** - asc: 升序排序。 - desc: 降序排序。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。
        :type order_rule: str
        :param backup_status: **参数解释：** 备份状态。 **约束限制：** 不涉及。 **取值范围：** - COMPLETED - BUILDING - FAILED  **默认取值：** 不涉及。
        :type backup_status: str
        :param backup_name: **参数解释：** 备份名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type backup_name: str
        :param backup_description: **参数解释：** 备份描述，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type backup_description: str
        :param instance_name: **参数解释：** 实例名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type instance_name: str
        """
        
        

        self._instance_id = None
        self._backup_id = None
        self._backup_type = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self._mode = None
        self._order_field = None
        self._order_rule = None
        self._backup_status = None
        self._backup_name = None
        self._backup_description = None
        self._instance_name = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if mode is not None:
            self.mode = mode
        if order_field is not None:
            self.order_field = order_field
        if order_rule is not None:
            self.order_rule = order_rule
        if backup_status is not None:
            self.backup_status = backup_status
        if backup_name is not None:
            self.backup_name = backup_name
        if backup_description is not None:
            self.backup_description = backup_description
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBackupsRequest.

        **参数解释：** 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。如果instance_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的instance_id精确匹配查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The instance_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBackupsRequest.

        **参数解释：** 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。如果instance_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的instance_id精确匹配查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param instance_id: The instance_id of this ListBackupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ListBackupsRequest.

        **参数解释：** 备份ID。如果backup_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的backup_id精确匹配查询。 **约束限制：** 当该字段传入的备份ID归属为自动增量备份时，实例ID必传，且实例ID必须为精确匹配。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The backup_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ListBackupsRequest.

        **参数解释：** 备份ID。如果backup_id以“”起始，表示按照“”后面的值模糊匹配，否则，按照实际填写的backup_id精确匹配查询。 **约束限制：** 当该字段传入的备份ID归属为自动增量备份时，实例ID必传，且实例ID必须为精确匹配。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param backup_id: The backup_id of this ListBackupsRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        r"""Gets the backup_type of this ListBackupsRequest.

        **参数解释：** 备份类型。 **约束限制：** 当该字段取值为“Incremental”时，实例ID必传。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。  **默认取值：** 不涉及。

        :return: The backup_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this ListBackupsRequest.

        **参数解释：** 备份类型。 **约束限制：** 当该字段取值为“Incremental”时，实例ID必传。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。 - 当该字段未传入值时，默认只查询所有的全量备份，包括自动全备备份和手动全量备份。当该字段取值为“Incremental”时，实例ID必传。  **默认取值：** 不涉及。

        :param backup_type: The backup_type of this ListBackupsRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def offset(self):
        r"""Gets the offset of this ListBackupsRequest.

        **参数解释：** 索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。 **约束限制：** 不涉及。 **取值范围：** 大于或等于0。 **默认取值：** 0，表示从最新的备份创建时间对应的备份开始查询。

        :return: The offset of this ListBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackupsRequest.

        **参数解释：** 索引位置偏移量，表示从指定project ID下最新的备份创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的备份信息。 **约束限制：** 不涉及。 **取值范围：** 大于或等于0。 **默认取值：** 0，表示从最新的备份创建时间对应的备份开始查询。

        :param offset: The offset of this ListBackupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackupsRequest.

        **参数解释：** 查询备份个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 100。不传该参数时，默认查询前100条备份信息。

        :return: The limit of this ListBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackupsRequest.

        **参数解释：** 查询备份个数上限值。 **约束限制：** 不涉及。 **取值范围：** 1~100。 **默认取值：** 100。不传该参数时，默认查询前100条备份信息。

        :param limit: The limit of this ListBackupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListBackupsRequest.

        **参数解释：** 查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “end_time”有值时，“begin_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The begin_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListBackupsRequest.

        **参数解释：** 查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “end_time”有值时，“begin_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param begin_time: The begin_time of this ListBackupsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBackupsRequest.

        **参数解释：** 查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “begin_time”有值时，“end_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The end_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBackupsRequest.

        **参数解释：** 查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **约束限制：** “begin_time”有值时，“end_time”必选。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param end_time: The end_time of this ListBackupsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def mode(self):
        r"""Gets the mode of this ListBackupsRequest.

        **参数解释：** 实例模式。 **约束限制：** 不涉及。 **取值范围：** - Sharding - ReplicaSet - Single  **默认取值：** 不涉及。

        :return: The mode of this ListBackupsRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListBackupsRequest.

        **参数解释：** 实例模式。 **约束限制：** 不涉及。 **取值范围：** - Sharding - ReplicaSet - Single  **默认取值：** 不涉及。

        :param mode: The mode of this ListBackupsRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def order_field(self):
        r"""Gets the order_field of this ListBackupsRequest.

        **参数解释：** 排序字段。 **约束限制：** “order_rule”有值时，“order_field”必选。 **取值范围：** - name，备份名称。 - instanceName，实例名称。 - type，备份类型。 - datastoreType，引擎类型。 - beginTime，开始时间。 - status，备份状态。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。

        :return: The order_field of this ListBackupsRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        r"""Sets the order_field of this ListBackupsRequest.

        **参数解释：** 排序字段。 **约束限制：** “order_rule”有值时，“order_field”必选。 **取值范围：** - name，备份名称。 - instanceName，实例名称。 - type，备份类型。 - datastoreType，引擎类型。 - beginTime，开始时间。 - status，备份状态。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。

        :param order_field: The order_field of this ListBackupsRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_rule(self):
        r"""Gets the order_rule of this ListBackupsRequest.

        **参数解释：** 排序规则。 **约束限制：** “order_field”有值时，“order_rule”必选。 **取值范围：** - asc: 升序排序。 - desc: 降序排序。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。

        :return: The order_rule of this ListBackupsRequest.
        :rtype: str
        """
        return self._order_rule

    @order_rule.setter
    def order_rule(self, order_rule):
        r"""Sets the order_rule of this ListBackupsRequest.

        **参数解释：** 排序规则。 **约束限制：** “order_field”有值时，“order_rule”必选。 **取值范围：** - asc: 升序排序。 - desc: 降序排序。  **默认取值：** 如果不传值，则默认根据备份开始时间，即响应参数的begin_time，倒序排序。

        :param order_rule: The order_rule of this ListBackupsRequest.
        :type order_rule: str
        """
        self._order_rule = order_rule

    @property
    def backup_status(self):
        r"""Gets the backup_status of this ListBackupsRequest.

        **参数解释：** 备份状态。 **约束限制：** 不涉及。 **取值范围：** - COMPLETED - BUILDING - FAILED  **默认取值：** 不涉及。

        :return: The backup_status of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_status

    @backup_status.setter
    def backup_status(self, backup_status):
        r"""Sets the backup_status of this ListBackupsRequest.

        **参数解释：** 备份状态。 **约束限制：** 不涉及。 **取值范围：** - COMPLETED - BUILDING - FAILED  **默认取值：** 不涉及。

        :param backup_status: The backup_status of this ListBackupsRequest.
        :type backup_status: str
        """
        self._backup_status = backup_status

    @property
    def backup_name(self):
        r"""Gets the backup_name of this ListBackupsRequest.

        **参数解释：** 备份名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The backup_name of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this ListBackupsRequest.

        **参数解释：** 备份名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param backup_name: The backup_name of this ListBackupsRequest.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def backup_description(self):
        r"""Gets the backup_description of this ListBackupsRequest.

        **参数解释：** 备份描述，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The backup_description of this ListBackupsRequest.
        :rtype: str
        """
        return self._backup_description

    @backup_description.setter
    def backup_description(self, backup_description):
        r"""Sets the backup_description of this ListBackupsRequest.

        **参数解释：** 备份描述，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param backup_description: The backup_description of this ListBackupsRequest.
        :type backup_description: str
        """
        self._backup_description = backup_description

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListBackupsRequest.

        **参数解释：** 实例名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The instance_name of this ListBackupsRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListBackupsRequest.

        **参数解释：** 实例名称，支持模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param instance_name: The instance_name of this ListBackupsRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, ListBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
