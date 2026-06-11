# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddReadonlyNodeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'num': 'int',
        'delay': 'int',
        'is_auto_pay': 'bool',
        'group_id': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'num': 'num',
        'delay': 'delay',
        'is_auto_pay': 'is_auto_pay',
        'group_id': 'group_id',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, spec_code=None, num=None, delay=None, is_auto_pay=None, group_id=None, availability_zone=None):
        r"""AddReadonlyNodeRequestBody

        The model defined in huaweicloud sdk

        :param spec_code: **参数解释：** 资源规格编码。获取方法请参见查询数据库规格中参数的值。示例：dds.mongodb.c6.large.4.rr。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type spec_code: str
        :param num: **参数解释：** 待新增只读节点个数。 **约束限制：** 不涉及。 **取值范围：** [1, 5]。 **默认取值：** 不涉及。
        :type num: int
        :param delay: **参数解释：** 同步延迟时间。 **约束限制：** 集群不支持设置。 **取值范围：** 0~1200秒。 **默认取值：** 不涉及。
        :type delay: int
        :param is_auto_pay: **参数解释：** 新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制：** 不涉及。 **取值范围：** - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。 **默认取值：** false。
        :type is_auto_pay: bool
        :param group_id: **参数解释：** 目标Shard组ID。集群实例添加只读节点时传入目标Shard组ID。 **约束限制：** 副本集实例不支持设置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type group_id: str
        :param availability_zone: **参数解释：** 新增只读节点的可用区ID。可根据“查询实例列表和详情”接口响应参数获取。 **约束限制：** 该参数仅对多可用区部署的实例生效。仅支持传入一个可用区且必须属于当前实例的多个可用区内的其中一个。 **取值范围：** 不涉及。 **默认取值：** 若不传此参数，新增的只读节点将相对均匀分布在主备节点所在可用区。
        :type availability_zone: str
        """
        
        

        self._spec_code = None
        self._num = None
        self._delay = None
        self._is_auto_pay = None
        self._group_id = None
        self._availability_zone = None
        self.discriminator = None

        self.spec_code = spec_code
        self.num = num
        if delay is not None:
            self.delay = delay
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if group_id is not None:
            self.group_id = group_id
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def spec_code(self):
        r"""Gets the spec_code of this AddReadonlyNodeRequestBody.

        **参数解释：** 资源规格编码。获取方法请参见查询数据库规格中参数的值。示例：dds.mongodb.c6.large.4.rr。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The spec_code of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this AddReadonlyNodeRequestBody.

        **参数解释：** 资源规格编码。获取方法请参见查询数据库规格中参数的值。示例：dds.mongodb.c6.large.4.rr。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param spec_code: The spec_code of this AddReadonlyNodeRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        r"""Gets the num of this AddReadonlyNodeRequestBody.

        **参数解释：** 待新增只读节点个数。 **约束限制：** 不涉及。 **取值范围：** [1, 5]。 **默认取值：** 不涉及。

        :return: The num of this AddReadonlyNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this AddReadonlyNodeRequestBody.

        **参数解释：** 待新增只读节点个数。 **约束限制：** 不涉及。 **取值范围：** [1, 5]。 **默认取值：** 不涉及。

        :param num: The num of this AddReadonlyNodeRequestBody.
        :type num: int
        """
        self._num = num

    @property
    def delay(self):
        r"""Gets the delay of this AddReadonlyNodeRequestBody.

        **参数解释：** 同步延迟时间。 **约束限制：** 集群不支持设置。 **取值范围：** 0~1200秒。 **默认取值：** 不涉及。

        :return: The delay of this AddReadonlyNodeRequestBody.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this AddReadonlyNodeRequestBody.

        **参数解释：** 同步延迟时间。 **约束限制：** 集群不支持设置。 **取值范围：** 0~1200秒。 **默认取值：** 不涉及。

        :param delay: The delay of this AddReadonlyNodeRequestBody.
        :type delay: int
        """
        self._delay = delay

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this AddReadonlyNodeRequestBody.

        **参数解释：** 新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制：** 不涉及。 **取值范围：** - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。 **默认取值：** false。

        :return: The is_auto_pay of this AddReadonlyNodeRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this AddReadonlyNodeRequestBody.

        **参数解释：** 新增包年包月实例的只读节点时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 **约束限制：** 不涉及。 **取值范围：** - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。 **默认取值：** false。

        :param is_auto_pay: The is_auto_pay of this AddReadonlyNodeRequestBody.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def group_id(self):
        r"""Gets the group_id of this AddReadonlyNodeRequestBody.

        **参数解释：** 目标Shard组ID。集群实例添加只读节点时传入目标Shard组ID。 **约束限制：** 副本集实例不支持设置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The group_id of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddReadonlyNodeRequestBody.

        **参数解释：** 目标Shard组ID。集群实例添加只读节点时传入目标Shard组ID。 **约束限制：** 副本集实例不支持设置。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param group_id: The group_id of this AddReadonlyNodeRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this AddReadonlyNodeRequestBody.

        **参数解释：** 新增只读节点的可用区ID。可根据“查询实例列表和详情”接口响应参数获取。 **约束限制：** 该参数仅对多可用区部署的实例生效。仅支持传入一个可用区且必须属于当前实例的多个可用区内的其中一个。 **取值范围：** 不涉及。 **默认取值：** 若不传此参数，新增的只读节点将相对均匀分布在主备节点所在可用区。

        :return: The availability_zone of this AddReadonlyNodeRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this AddReadonlyNodeRequestBody.

        **参数解释：** 新增只读节点的可用区ID。可根据“查询实例列表和详情”接口响应参数获取。 **约束限制：** 该参数仅对多可用区部署的实例生效。仅支持传入一个可用区且必须属于当前实例的多个可用区内的其中一个。 **取值范围：** 不涉及。 **默认取值：** 若不传此参数，新增的只读节点将相对均匀分布在主备节点所在可用区。

        :param availability_zone: The availability_zone of this AddReadonlyNodeRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, AddReadonlyNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
