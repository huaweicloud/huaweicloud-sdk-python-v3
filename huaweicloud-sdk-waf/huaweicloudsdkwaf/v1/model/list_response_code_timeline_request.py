# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResponseCodeTimelineRequest:

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
        'hosts': 'list[str]',
        'instances': 'list[str]',
        'response_source': 'str',
        'group_by': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances',
        'response_source': 'response_source',
        'group_by': 'group_by'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, hosts=None, instances=None, response_source=None, group_by=None):
        r"""ListResponseCodeTimelineRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0
        :type enterprise_project_id: str
        :param _from: **参数解释：** 起始时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        :param hosts: **参数解释：** 要查询的域名列表，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: list[str]
        :param instances: **参数解释：** 要查询的实例列表，通过 “查询WAF独享引擎列表”（ListInstance）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instances: list[str]
        :param response_source: **参数解释：** 响应源 **约束限制：** 不涉及 **取值范围：** - WAF - UPSTREAM  **默认取值：** 不涉及
        :type response_source: str
        :param group_by: **参数解释：** 展示维度，按天展示时传\&quot;DAY\&quot; **约束限制：** 不涉及 **取值范围：** - DAY  **默认取值：** 不涉及
        :type group_by: str
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self._response_source = None
        self._group_by = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if response_source is not None:
            self.response_source = response_source
        if group_by is not None:
            self.group_by = group_by

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListResponseCodeTimelineRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :return: The enterprise_project_id of this ListResponseCodeTimelineRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListResponseCodeTimelineRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListResponseCodeTimelineRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        r"""Gets the _from of this ListResponseCodeTimelineRequest.

        **参数解释：** 起始时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListResponseCodeTimelineRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListResponseCodeTimelineRequest.

        **参数解释：** 起始时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListResponseCodeTimelineRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListResponseCodeTimelineRequest.

        **参数解释：** 结束时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListResponseCodeTimelineRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListResponseCodeTimelineRequest.

        **参数解释：** 结束时间（13位毫秒时间戳） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListResponseCodeTimelineRequest.
        :type to: int
        """
        self._to = to

    @property
    def hosts(self):
        r"""Gets the hosts of this ListResponseCodeTimelineRequest.

        **参数解释：** 要查询的域名列表，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this ListResponseCodeTimelineRequest.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListResponseCodeTimelineRequest.

        **参数解释：** 要查询的域名列表，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this ListResponseCodeTimelineRequest.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def instances(self):
        r"""Gets the instances of this ListResponseCodeTimelineRequest.

        **参数解释：** 要查询的实例列表，通过 “查询WAF独享引擎列表”（ListInstance）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instances of this ListResponseCodeTimelineRequest.
        :rtype: list[str]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListResponseCodeTimelineRequest.

        **参数解释：** 要查询的实例列表，通过 “查询WAF独享引擎列表”（ListInstance）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instances: The instances of this ListResponseCodeTimelineRequest.
        :type instances: list[str]
        """
        self._instances = instances

    @property
    def response_source(self):
        r"""Gets the response_source of this ListResponseCodeTimelineRequest.

        **参数解释：** 响应源 **约束限制：** 不涉及 **取值范围：** - WAF - UPSTREAM  **默认取值：** 不涉及

        :return: The response_source of this ListResponseCodeTimelineRequest.
        :rtype: str
        """
        return self._response_source

    @response_source.setter
    def response_source(self, response_source):
        r"""Sets the response_source of this ListResponseCodeTimelineRequest.

        **参数解释：** 响应源 **约束限制：** 不涉及 **取值范围：** - WAF - UPSTREAM  **默认取值：** 不涉及

        :param response_source: The response_source of this ListResponseCodeTimelineRequest.
        :type response_source: str
        """
        self._response_source = response_source

    @property
    def group_by(self):
        r"""Gets the group_by of this ListResponseCodeTimelineRequest.

        **参数解释：** 展示维度，按天展示时传\"DAY\" **约束限制：** 不涉及 **取值范围：** - DAY  **默认取值：** 不涉及

        :return: The group_by of this ListResponseCodeTimelineRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ListResponseCodeTimelineRequest.

        **参数解释：** 展示维度，按天展示时传\"DAY\" **约束限制：** 不涉及 **取值范围：** - DAY  **默认取值：** 不涉及

        :param group_by: The group_by of this ListResponseCodeTimelineRequest.
        :type group_by: str
        """
        self._group_by = group_by

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
        if not isinstance(other, ListResponseCodeTimelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
