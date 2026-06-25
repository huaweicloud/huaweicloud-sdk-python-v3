# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceBackupSummaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'order_field': 'str',
        'order_rule': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'order_field': 'order_field',
        'order_rule': 'order_rule',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, engine=None, order_field=None, order_rule=None, instance_id=None, instance_name=None, offset=None, limit=None, x_language=None):
        r"""ListInstanceBackupSummaryRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**：  引擎类型。只支持筛选RDS for MySQL,RDS for MariaDB, TaurusDB标准版引擎  **约束限制**：  不涉及。  **取值范围**：  - mysql - mariadb - taurusdb  **默认取值**：  不涉及。
        :type engine: str
        :param order_field: **参数解释**：  排序字段。 根据指定字段排序查询结果。  **约束限制**：  不涉及。  **取值范围**： - backup_used_space:根据备份数据总量排序 - obs ：根据日志备份用量排序  **默认取值**：  不涉及。
        :type order_field: str
        :param order_rule: **参数解释**：  排序规则。  **约束限制**：  不涉及。  **取值范围**：  - ASC ： 根据排序字段升序 - DESC ：根据排序字段降序  **默认取值**：  DESC
        :type order_rule: str
        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_name: str
        :param offset: **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为数字，不能为负数。  **取值范围**：  大于等于0的整数。  **默认取值**：  0。
        :type offset: int
        :param limit: **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  默认为10，不能为负数，最小值为1，最大值为50。  **默认取值**：  10。
        :type limit: int
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。
        :type x_language: str
        """
        
        

        self._engine = None
        self._order_field = None
        self._order_rule = None
        self._instance_id = None
        self._instance_name = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if order_field is not None:
            self.order_field = order_field
        if order_rule is not None:
            self.order_rule = order_rule
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def engine(self):
        r"""Gets the engine of this ListInstanceBackupSummaryRequest.

        **参数解释**：  引擎类型。只支持筛选RDS for MySQL,RDS for MariaDB, TaurusDB标准版引擎  **约束限制**：  不涉及。  **取值范围**：  - mysql - mariadb - taurusdb  **默认取值**：  不涉及。

        :return: The engine of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstanceBackupSummaryRequest.

        **参数解释**：  引擎类型。只支持筛选RDS for MySQL,RDS for MariaDB, TaurusDB标准版引擎  **约束限制**：  不涉及。  **取值范围**：  - mysql - mariadb - taurusdb  **默认取值**：  不涉及。

        :param engine: The engine of this ListInstanceBackupSummaryRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def order_field(self):
        r"""Gets the order_field of this ListInstanceBackupSummaryRequest.

        **参数解释**：  排序字段。 根据指定字段排序查询结果。  **约束限制**：  不涉及。  **取值范围**： - backup_used_space:根据备份数据总量排序 - obs ：根据日志备份用量排序  **默认取值**：  不涉及。

        :return: The order_field of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        r"""Sets the order_field of this ListInstanceBackupSummaryRequest.

        **参数解释**：  排序字段。 根据指定字段排序查询结果。  **约束限制**：  不涉及。  **取值范围**： - backup_used_space:根据备份数据总量排序 - obs ：根据日志备份用量排序  **默认取值**：  不涉及。

        :param order_field: The order_field of this ListInstanceBackupSummaryRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_rule(self):
        r"""Gets the order_rule of this ListInstanceBackupSummaryRequest.

        **参数解释**：  排序规则。  **约束限制**：  不涉及。  **取值范围**：  - ASC ： 根据排序字段升序 - DESC ：根据排序字段降序  **默认取值**：  DESC

        :return: The order_rule of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._order_rule

    @order_rule.setter
    def order_rule(self, order_rule):
        r"""Sets the order_rule of this ListInstanceBackupSummaryRequest.

        **参数解释**：  排序规则。  **约束限制**：  不涉及。  **取值范围**：  - ASC ： 根据排序字段升序 - DESC ：根据排序字段降序  **默认取值**：  DESC

        :param order_rule: The order_rule of this ListInstanceBackupSummaryRequest.
        :type order_rule: str
        """
        self._order_rule = order_rule

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceBackupSummaryRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceBackupSummaryRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ListInstanceBackupSummaryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListInstanceBackupSummaryRequest.

        **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_name of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListInstanceBackupSummaryRequest.

        **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_name: The instance_name of this ListInstanceBackupSummaryRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceBackupSummaryRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为数字，不能为负数。  **取值范围**：  大于等于0的整数。  **默认取值**：  0。

        :return: The offset of this ListInstanceBackupSummaryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceBackupSummaryRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为数字，不能为负数。  **取值范围**：  大于等于0的整数。  **默认取值**：  0。

        :param offset: The offset of this ListInstanceBackupSummaryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceBackupSummaryRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  默认为10，不能为负数，最小值为1，最大值为50。  **默认取值**：  10。

        :return: The limit of this ListInstanceBackupSummaryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceBackupSummaryRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  默认为10，不能为负数，最小值为1，最大值为50。  **默认取值**：  10。

        :param limit: The limit of this ListInstanceBackupSummaryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListInstanceBackupSummaryRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。

        :return: The x_language of this ListInstanceBackupSummaryRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListInstanceBackupSummaryRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。

        :param x_language: The x_language of this ListInstanceBackupSummaryRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListInstanceBackupSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
