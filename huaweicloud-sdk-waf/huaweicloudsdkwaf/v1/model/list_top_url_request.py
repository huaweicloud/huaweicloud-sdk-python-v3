# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        '_from': 'int',
        'to': 'int',
        'top': 'int',
        'hosts': 'str',
        'instances': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'top': 'top',
        'hosts': 'hosts',
        'instances': 'instances'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, top=None, hosts=None, instances=None):
        r"""ListTopUrlRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 企业项目id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enterprise_project_id: str
        :param _from: **参数解释：** 起始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        :param top: **参数解释：** 要查询的前几的结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type top: int
        :param hosts: **参数解释：** 要查询域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: str
        :param instances: **参数解释：** 要查询实例列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instances: str
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._top = None
        self._hosts = None
        self._instances = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        if top is not None:
            self.top = top
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListTopUrlRequest.

        **参数解释：** 企业项目id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enterprise_project_id of this ListTopUrlRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListTopUrlRequest.

        **参数解释：** 企业项目id **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListTopUrlRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        r"""Gets the _from of this ListTopUrlRequest.

        **参数解释：** 起始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListTopUrlRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListTopUrlRequest.

        **参数解释：** 起始时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListTopUrlRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListTopUrlRequest.

        **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListTopUrlRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListTopUrlRequest.

        **参数解释：** 结束时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListTopUrlRequest.
        :type to: int
        """
        self._to = to

    @property
    def top(self):
        r"""Gets the top of this ListTopUrlRequest.

        **参数解释：** 要查询的前几的结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The top of this ListTopUrlRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this ListTopUrlRequest.

        **参数解释：** 要查询的前几的结果 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param top: The top of this ListTopUrlRequest.
        :type top: int
        """
        self._top = top

    @property
    def hosts(self):
        r"""Gets the hosts of this ListTopUrlRequest.

        **参数解释：** 要查询域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this ListTopUrlRequest.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListTopUrlRequest.

        **参数解释：** 要查询域名列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this ListTopUrlRequest.
        :type hosts: str
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this ListTopUrlRequest.

        **参数解释：** 要查询实例列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instances of this ListTopUrlRequest.
        :rtype: str
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListTopUrlRequest.

        **参数解释：** 要查询实例列表 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instances: The instances of this ListTopUrlRequest.
        :type instances: str
        """
        self._instances = instances

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTopUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
