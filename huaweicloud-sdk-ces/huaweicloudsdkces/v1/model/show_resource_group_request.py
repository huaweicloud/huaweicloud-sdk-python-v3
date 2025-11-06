# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'status': 'str',
        'namespace': 'str',
        'dname': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'status': 'status',
        'namespace': 'namespace',
        'dname': 'dname',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, status=None, namespace=None, dname=None, start=None, limit=None):
        r"""ShowResourceGroupRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释** 资源分组ID。 **约束限制** 不涉及 **取值范围** 以\&quot;rg\&quot;开头，后面跟着22个字母或数字 **默认取值** 不涉及
        :type group_id: str
        :param status: **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及
        :type status: str
        :param namespace: **参数解释** 资源类型，即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 [3,32]个字符之间 **默认取值** 不涉及
        :type namespace: str
        :param dname: **参数解释** 资源维度，如：弹性云服务器，则维度为instance_id，各资源的监控维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 包含字母、数字、_、-、/、#、\\或括号，长度为[1,131]个字符 **默认取值** 不涉及
        :type dname: str
        :param start: **参数解释** 分页起始值 **约束限制** 不涉及 **取值范围** [0,9999999] **默认取值** 0
        :type start: str
        :param limit: **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** [1,100] **默认取值** 100
        :type limit: str
        """
        
        

        self._group_id = None
        self._status = None
        self._namespace = None
        self._dname = None
        self._start = None
        self._limit = None
        self.discriminator = None

        self.group_id = group_id
        if status is not None:
            self.status = status
        if namespace is not None:
            self.namespace = namespace
        if dname is not None:
            self.dname = dname
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowResourceGroupRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及 **取值范围** 以\"rg\"开头，后面跟着22个字母或数字 **默认取值** 不涉及

        :return: The group_id of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowResourceGroupRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及 **取值范围** 以\"rg\"开头，后面跟着22个字母或数字 **默认取值** 不涉及

        :param group_id: The group_id of this ShowResourceGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def status(self):
        r"""Gets the status of this ShowResourceGroupRequest.

        **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及

        :return: The status of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResourceGroupRequest.

        **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及

        :param status: The status of this ShowResourceGroupRequest.
        :type status: str
        """
        self._status = status

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowResourceGroupRequest.

        **参数解释** 资源类型，即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 [3,32]个字符之间 **默认取值** 不涉及

        :return: The namespace of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowResourceGroupRequest.

        **参数解释** 资源类型，即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 [3,32]个字符之间 **默认取值** 不涉及

        :param namespace: The namespace of this ShowResourceGroupRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dname(self):
        r"""Gets the dname of this ShowResourceGroupRequest.

        **参数解释** 资源维度，如：弹性云服务器，则维度为instance_id，各资源的监控维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 包含字母、数字、_、-、/、#、\\或括号，长度为[1,131]个字符 **默认取值** 不涉及

        :return: The dname of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._dname

    @dname.setter
    def dname(self, dname):
        r"""Sets the dname of this ShowResourceGroupRequest.

        **参数解释** 资源维度，如：弹性云服务器，则维度为instance_id，各资源的监控维度名称可查看：“[服务指标维度](ces_03_0059.xml)”。 **约束限制** 不涉及 **取值范围** 包含字母、数字、_、-、/、#、\\或括号，长度为[1,131]个字符 **默认取值** 不涉及

        :param dname: The dname of this ShowResourceGroupRequest.
        :type dname: str
        """
        self._dname = dname

    @property
    def start(self):
        r"""Gets the start of this ShowResourceGroupRequest.

        **参数解释** 分页起始值 **约束限制** 不涉及 **取值范围** [0,9999999] **默认取值** 0

        :return: The start of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ShowResourceGroupRequest.

        **参数解释** 分页起始值 **约束限制** 不涉及 **取值范围** [0,9999999] **默认取值** 0

        :param start: The start of this ShowResourceGroupRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ShowResourceGroupRequest.

        **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** [1,100] **默认取值** 100

        :return: The limit of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowResourceGroupRequest.

        **参数解释** 单次查询的条数限制 **约束限制** 不涉及 **取值范围** [1,100] **默认取值** 100

        :param limit: The limit of this ShowResourceGroupRequest.
        :type limit: str
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
        if not isinstance(other, ShowResourceGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
