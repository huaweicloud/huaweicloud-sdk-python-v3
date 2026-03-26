# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceBackupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'offset': 'str',
        'limit': 'str',
        'order_field': 'str',
        'order_rule': 'str',
        'filter_field': 'str',
        'filter_content': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'order_field': 'order_field',
        'order_rule': 'order_rule',
        'filter_field': 'filter_field',
        'filter_content': 'filter_content'
    }

    def __init__(self, x_language=None, instance_id=None, offset=None, limit=None, order_field=None, order_rule=None, filter_field=None, filter_content=None):
        r"""ShowInstanceBackupsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param offset: **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。
        :type offset: str
        :param limit: **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。
        :type limit: str
        :param order_field: **参数解释**:  根据指定字段排序。  **约束限制**:  不涉及。  **取值范围**:  - name：备份名称。 - beginTime：备份开启时间。 - type：备份类型。  **默认取值**: 不涉及。
        :type order_field: str
        :param order_rule: **参数解释**: 排序规则。  **约束限制**: 不涉及。  **取值范围**: - asc：升序。 - desc：降序。  **默认取值**: 不涉及。
        :type order_rule: str
        :param filter_field: **参数解释**: 过滤字段类型。 **约束限制**: 不涉及。 **取值范围**: name：根据备份名称进行过滤。 **默认取值**: 不涉及。
        :type filter_field: str
        :param filter_content: **参数解释**: 过滤内容。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type filter_content: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._offset = None
        self._limit = None
        self._order_field = None
        self._order_rule = None
        self._filter_field = None
        self._filter_content = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_field is not None:
            self.order_field = order_field
        if order_rule is not None:
            self.order_rule = order_rule
        if filter_field is not None:
            self.filter_field = filter_field
        if filter_content is not None:
            self.filter_content = filter_content

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowInstanceBackupsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowInstanceBackupsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowInstanceBackupsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceBackupsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceBackupsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowInstanceBackupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceBackupsRequest.

        **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。

        :return: The offset of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceBackupsRequest.

        **参数解释**：    索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    0。

        :param offset: The offset of this ShowInstanceBackupsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceBackupsRequest.

        **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。

        :return: The limit of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceBackupsRequest.

        **参数解释**：  查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  100。

        :param limit: The limit of this ShowInstanceBackupsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def order_field(self):
        r"""Gets the order_field of this ShowInstanceBackupsRequest.

        **参数解释**:  根据指定字段排序。  **约束限制**:  不涉及。  **取值范围**:  - name：备份名称。 - beginTime：备份开启时间。 - type：备份类型。  **默认取值**: 不涉及。

        :return: The order_field of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        r"""Sets the order_field of this ShowInstanceBackupsRequest.

        **参数解释**:  根据指定字段排序。  **约束限制**:  不涉及。  **取值范围**:  - name：备份名称。 - beginTime：备份开启时间。 - type：备份类型。  **默认取值**: 不涉及。

        :param order_field: The order_field of this ShowInstanceBackupsRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_rule(self):
        r"""Gets the order_rule of this ShowInstanceBackupsRequest.

        **参数解释**: 排序规则。  **约束限制**: 不涉及。  **取值范围**: - asc：升序。 - desc：降序。  **默认取值**: 不涉及。

        :return: The order_rule of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._order_rule

    @order_rule.setter
    def order_rule(self, order_rule):
        r"""Sets the order_rule of this ShowInstanceBackupsRequest.

        **参数解释**: 排序规则。  **约束限制**: 不涉及。  **取值范围**: - asc：升序。 - desc：降序。  **默认取值**: 不涉及。

        :param order_rule: The order_rule of this ShowInstanceBackupsRequest.
        :type order_rule: str
        """
        self._order_rule = order_rule

    @property
    def filter_field(self):
        r"""Gets the filter_field of this ShowInstanceBackupsRequest.

        **参数解释**: 过滤字段类型。 **约束限制**: 不涉及。 **取值范围**: name：根据备份名称进行过滤。 **默认取值**: 不涉及。

        :return: The filter_field of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._filter_field

    @filter_field.setter
    def filter_field(self, filter_field):
        r"""Sets the filter_field of this ShowInstanceBackupsRequest.

        **参数解释**: 过滤字段类型。 **约束限制**: 不涉及。 **取值范围**: name：根据备份名称进行过滤。 **默认取值**: 不涉及。

        :param filter_field: The filter_field of this ShowInstanceBackupsRequest.
        :type filter_field: str
        """
        self._filter_field = filter_field

    @property
    def filter_content(self):
        r"""Gets the filter_content of this ShowInstanceBackupsRequest.

        **参数解释**: 过滤内容。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The filter_content of this ShowInstanceBackupsRequest.
        :rtype: str
        """
        return self._filter_content

    @filter_content.setter
    def filter_content(self, filter_content):
        r"""Sets the filter_content of this ShowInstanceBackupsRequest.

        **参数解释**: 过滤内容。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param filter_content: The filter_content of this ShowInstanceBackupsRequest.
        :type filter_content: str
        """
        self._filter_content = filter_content

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
        if not isinstance(other, ShowInstanceBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
