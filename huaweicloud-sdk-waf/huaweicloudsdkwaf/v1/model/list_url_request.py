# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top': 'int',
        'recent': 'str',
        '_from': 'int',
        'to': 'int',
        'hosts': 'list[str]',
        'instances': 'list[str]'
    }

    attribute_map = {
        'top': 'top',
        'recent': 'recent',
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances'
    }

    def __init__(self, top=None, recent=None, _from=None, to=None, hosts=None, instances=None):
        r"""ListUrlRequest

        The model defined in huaweicloud sdk

        :param top: 受攻击次数最多的几条url
        :type top: int
        :param recent: **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及
        :type recent: str
        :param _from: **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        :param hosts: 要查询事件的域名id列表
        :type hosts: list[str]
        :param instances: 要查询事件的独享域名id列表
        :type instances: list[str]
        """
        
        

        self._top = None
        self._recent = None
        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self.discriminator = None

        self.top = top
        if recent is not None:
            self.recent = recent
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances

    @property
    def top(self):
        r"""Gets the top of this ListUrlRequest.

        受攻击次数最多的几条url

        :return: The top of this ListUrlRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this ListUrlRequest.

        受攻击次数最多的几条url

        :param top: The top of this ListUrlRequest.
        :type top: int
        """
        self._top = top

    @property
    def recent(self):
        r"""Gets the recent of this ListUrlRequest.

        **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及

        :return: The recent of this ListUrlRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this ListUrlRequest.

        **参数解释：** 查询日志的时间范围，如1week（1周）、1month（1个月） **约束限制：** 不涉及 **取值范围：** - yesterday - today - 3days - 1week - 1month  **默认取值：** 不涉及

        :param recent: The recent of this ListUrlRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def _from(self):
        r"""Gets the _from of this ListUrlRequest.

        **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListUrlRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListUrlRequest.

        **参数解释：** 开始时间，统计周期的起始时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListUrlRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListUrlRequest.

        **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListUrlRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListUrlRequest.

        **参数解释：** 结束时间，统计周期的终止时间戳（毫秒级）。不使用recent参数时需要填写 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListUrlRequest.
        :type to: int
        """
        self._to = to

    @property
    def hosts(self):
        r"""Gets the hosts of this ListUrlRequest.

        要查询事件的域名id列表

        :return: The hosts of this ListUrlRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListUrlRequest.

        要查询事件的域名id列表

        :param hosts: The hosts of this ListUrlRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this ListUrlRequest.

        要查询事件的独享域名id列表

        :return: The instances of this ListUrlRequest.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListUrlRequest.

        要查询事件的独享域名id列表

        :param instances: The instances of this ListUrlRequest.
        :type instances: list[str]
        """
        self._instances = instances

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
        if not isinstance(other, ListUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
