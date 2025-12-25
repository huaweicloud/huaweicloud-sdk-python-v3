# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'status': 'str',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'status': 'status',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_name=None, group_id=None, status=None, start=None, limit=None):
        r"""ListResourceGroupRequest

        The model defined in huaweicloud sdk

        :param group_name: **参数解释** 资源分组名称。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。
        :type group_name: str
        :param group_id: **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\&quot;rg\&quot;开头，后面跟着22个字母或数字。 **默认取值** 不涉及。
        :type group_id: str
        :param status: **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。
        :type status: str
        :param start: **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,9999999]区间内。 **默认取值** 0
        :type start: int
        :param limit: **参数解释** 单次查询的条数限制。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100
        :type limit: int
        """
        
        

        self._group_name = None
        self._group_id = None
        self._status = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if status is not None:
            self.status = status
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_name(self):
        r"""Gets the group_name of this ListResourceGroupRequest.

        **参数解释** 资源分组名称。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。

        :return: The group_name of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListResourceGroupRequest.

        **参数解释** 资源分组名称。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。

        :param group_name: The group_name of this ListResourceGroupRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ListResourceGroupRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\"rg\"开头，后面跟着22个字母或数字。 **默认取值** 不涉及。

        :return: The group_id of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListResourceGroupRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\"rg\"开头，后面跟着22个字母或数字。 **默认取值** 不涉及。

        :param group_id: The group_id of this ListResourceGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def status(self):
        r"""Gets the status of this ListResourceGroupRequest.

        **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。

        :return: The status of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListResourceGroupRequest.

        **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。

        :param status: The status of this ListResourceGroupRequest.
        :type status: str
        """
        self._status = status

    @property
    def start(self):
        r"""Gets the start of this ListResourceGroupRequest.

        **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,9999999]区间内。 **默认取值** 0

        :return: The start of this ListResourceGroupRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListResourceGroupRequest.

        **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,9999999]区间内。 **默认取值** 0

        :param start: The start of this ListResourceGroupRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceGroupRequest.

        **参数解释** 单次查询的条数限制。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100

        :return: The limit of this ListResourceGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceGroupRequest.

        **参数解释** 单次查询的条数限制。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100

        :param limit: The limit of this ListResourceGroupRequest.
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
        if not isinstance(other, ListResourceGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
