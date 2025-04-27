# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolverRuleParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'domain_name': 'str',
        'endpoint_id': 'str',
        'status': 'str',
        'rule_type': 'str',
        'ipaddress_count': 'int',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain_name': 'domain_name',
        'endpoint_id': 'endpoint_id',
        'status': 'status',
        'rule_type': 'rule_type',
        'ipaddress_count': 'ipaddress_count',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, domain_name=None, endpoint_id=None, status=None, rule_type=None, ipaddress_count=None, create_time=None, update_time=None):
        r"""ResolverRuleParam

        The model defined in huaweicloud sdk

        :param id: 转发规则ID。
        :type id: str
        :param name: 规则名称。
        :type name: str
        :param domain_name: 域名。
        :type domain_name: str
        :param endpoint_id: 当前规则所属的终端节点ID。
        :type endpoint_id: str
        :param status: 资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。
        :type status: str
        :param rule_type: 规则类型。 预留字段，当前默认为FORWARD。
        :type rule_type: str
        :param ipaddress_count: 当前规则下的IP地址数量。
        :type ipaddress_count: int
        :param create_time: 创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type create_time: str
        :param update_time: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._domain_name = None
        self._endpoint_id = None
        self._status = None
        self._rule_type = None
        self._ipaddress_count = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if domain_name is not None:
            self.domain_name = domain_name
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if status is not None:
            self.status = status
        if rule_type is not None:
            self.rule_type = rule_type
        if ipaddress_count is not None:
            self.ipaddress_count = ipaddress_count
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ResolverRuleParam.

        转发规则ID。

        :return: The id of this ResolverRuleParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResolverRuleParam.

        转发规则ID。

        :param id: The id of this ResolverRuleParam.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResolverRuleParam.

        规则名称。

        :return: The name of this ResolverRuleParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResolverRuleParam.

        规则名称。

        :param name: The name of this ResolverRuleParam.
        :type name: str
        """
        self._name = name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ResolverRuleParam.

        域名。

        :return: The domain_name of this ResolverRuleParam.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ResolverRuleParam.

        域名。

        :param domain_name: The domain_name of this ResolverRuleParam.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ResolverRuleParam.

        当前规则所属的终端节点ID。

        :return: The endpoint_id of this ResolverRuleParam.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ResolverRuleParam.

        当前规则所属的终端节点ID。

        :param endpoint_id: The endpoint_id of this ResolverRuleParam.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def status(self):
        r"""Gets the status of this ResolverRuleParam.

        资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。

        :return: The status of this ResolverRuleParam.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResolverRuleParam.

        资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。

        :param status: The status of this ResolverRuleParam.
        :type status: str
        """
        self._status = status

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ResolverRuleParam.

        规则类型。 预留字段，当前默认为FORWARD。

        :return: The rule_type of this ResolverRuleParam.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ResolverRuleParam.

        规则类型。 预留字段，当前默认为FORWARD。

        :param rule_type: The rule_type of this ResolverRuleParam.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def ipaddress_count(self):
        r"""Gets the ipaddress_count of this ResolverRuleParam.

        当前规则下的IP地址数量。

        :return: The ipaddress_count of this ResolverRuleParam.
        :rtype: int
        """
        return self._ipaddress_count

    @ipaddress_count.setter
    def ipaddress_count(self, ipaddress_count):
        r"""Sets the ipaddress_count of this ResolverRuleParam.

        当前规则下的IP地址数量。

        :param ipaddress_count: The ipaddress_count of this ResolverRuleParam.
        :type ipaddress_count: int
        """
        self._ipaddress_count = ipaddress_count

    @property
    def create_time(self):
        r"""Gets the create_time of this ResolverRuleParam.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The create_time of this ResolverRuleParam.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ResolverRuleParam.

        创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param create_time: The create_time of this ResolverRuleParam.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ResolverRuleParam.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The update_time of this ResolverRuleParam.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ResolverRuleParam.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param update_time: The update_time of this ResolverRuleParam.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ResolverRuleParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
