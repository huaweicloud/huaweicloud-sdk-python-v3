# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'loadbalancer': 'int',
        'certificate': 'int',
        'listener': 'int',
        'l7policy': 'int',
        'condition_per_policy': 'int',
        'pool': 'int',
        'healthmonitor': 'int',
        'member': 'int',
        'members_per_pool': 'int',
        'listeners_per_pool': 'int',
        'ipgroup': 'int',
        'ipgroup_bindings': 'int',
        'ipgroup_max_length': 'int',
        'security_policy': 'int',
        'listeners_per_loadbalancer': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'loadbalancer': 'loadbalancer',
        'certificate': 'certificate',
        'listener': 'listener',
        'l7policy': 'l7policy',
        'condition_per_policy': 'condition_per_policy',
        'pool': 'pool',
        'healthmonitor': 'healthmonitor',
        'member': 'member',
        'members_per_pool': 'members_per_pool',
        'listeners_per_pool': 'listeners_per_pool',
        'ipgroup': 'ipgroup',
        'ipgroup_bindings': 'ipgroup_bindings',
        'ipgroup_max_length': 'ipgroup_max_length',
        'security_policy': 'security_policy',
        'listeners_per_loadbalancer': 'listeners_per_loadbalancer'
    }

    def __init__(self, project_id=None, loadbalancer=None, certificate=None, listener=None, l7policy=None, condition_per_policy=None, pool=None, healthmonitor=None, member=None, members_per_pool=None, listeners_per_pool=None, ipgroup=None, ipgroup_bindings=None, ipgroup_max_length=None, security_policy=None, listeners_per_loadbalancer=None):
        """Quota

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。
        :type project_id: str
        :param loadbalancer: 负载均衡器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type loadbalancer: int
        :param certificate: 证书配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type certificate: int
        :param listener: 监听器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type listener: int
        :param l7policy: 转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type l7policy: int
        :param condition_per_policy: 转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type condition_per_policy: int
        :param pool: 后端云服务器组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type pool: int
        :param healthmonitor: 健康检查配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type healthmonitor: int
        :param member: 后端云服务器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type member: int
        :param members_per_pool: 单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type members_per_pool: int
        :param listeners_per_pool: 单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。
        :type listeners_per_pool: int
        :param ipgroup: IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type ipgroup: int
        :param ipgroup_bindings: IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type ipgroup_bindings: int
        :param ipgroup_max_length: IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type ipgroup_max_length: int
        :param security_policy: 自定义安全策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type security_policy: int
        :param listeners_per_loadbalancer: 单个LB实例下的监听器配额。 取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  &gt; 当前单个LB下监听器配额实际未限制，但建议不要超过默认配额。
        :type listeners_per_loadbalancer: int
        """
        
        

        self._project_id = None
        self._loadbalancer = None
        self._certificate = None
        self._listener = None
        self._l7policy = None
        self._condition_per_policy = None
        self._pool = None
        self._healthmonitor = None
        self._member = None
        self._members_per_pool = None
        self._listeners_per_pool = None
        self._ipgroup = None
        self._ipgroup_bindings = None
        self._ipgroup_max_length = None
        self._security_policy = None
        self._listeners_per_loadbalancer = None
        self.discriminator = None

        self.project_id = project_id
        self.loadbalancer = loadbalancer
        self.certificate = certificate
        self.listener = listener
        self.l7policy = l7policy
        self.condition_per_policy = condition_per_policy
        self.pool = pool
        self.healthmonitor = healthmonitor
        self.member = member
        self.members_per_pool = members_per_pool
        self.listeners_per_pool = listeners_per_pool
        self.ipgroup = ipgroup
        self.ipgroup_bindings = ipgroup_bindings
        self.ipgroup_max_length = ipgroup_max_length
        self.security_policy = security_policy
        self.listeners_per_loadbalancer = listeners_per_loadbalancer

    @property
    def project_id(self):
        """Gets the project_id of this Quota.

        项目ID。

        :return: The project_id of this Quota.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Quota.

        项目ID。

        :param project_id: The project_id of this Quota.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def loadbalancer(self):
        """Gets the loadbalancer of this Quota.

        负载均衡器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The loadbalancer of this Quota.
        :rtype: int
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        """Sets the loadbalancer of this Quota.

        负载均衡器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param loadbalancer: The loadbalancer of this Quota.
        :type loadbalancer: int
        """
        self._loadbalancer = loadbalancer

    @property
    def certificate(self):
        """Gets the certificate of this Quota.

        证书配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The certificate of this Quota.
        :rtype: int
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Quota.

        证书配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param certificate: The certificate of this Quota.
        :type certificate: int
        """
        self._certificate = certificate

    @property
    def listener(self):
        """Gets the listener of this Quota.

        监听器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The listener of this Quota.
        :rtype: int
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        """Sets the listener of this Quota.

        监听器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param listener: The listener of this Quota.
        :type listener: int
        """
        self._listener = listener

    @property
    def l7policy(self):
        """Gets the l7policy of this Quota.

        转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The l7policy of this Quota.
        :rtype: int
        """
        return self._l7policy

    @l7policy.setter
    def l7policy(self, l7policy):
        """Sets the l7policy of this Quota.

        转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param l7policy: The l7policy of this Quota.
        :type l7policy: int
        """
        self._l7policy = l7policy

    @property
    def condition_per_policy(self):
        """Gets the condition_per_policy of this Quota.

        转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The condition_per_policy of this Quota.
        :rtype: int
        """
        return self._condition_per_policy

    @condition_per_policy.setter
    def condition_per_policy(self, condition_per_policy):
        """Sets the condition_per_policy of this Quota.

        转发策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param condition_per_policy: The condition_per_policy of this Quota.
        :type condition_per_policy: int
        """
        self._condition_per_policy = condition_per_policy

    @property
    def pool(self):
        """Gets the pool of this Quota.

        后端云服务器组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The pool of this Quota.
        :rtype: int
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Quota.

        后端云服务器组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param pool: The pool of this Quota.
        :type pool: int
        """
        self._pool = pool

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this Quota.

        健康检查配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The healthmonitor of this Quota.
        :rtype: int
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this Quota.

        健康检查配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param healthmonitor: The healthmonitor of this Quota.
        :type healthmonitor: int
        """
        self._healthmonitor = healthmonitor

    @property
    def member(self):
        """Gets the member of this Quota.

        后端云服务器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The member of this Quota.
        :rtype: int
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Quota.

        后端云服务器配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param member: The member of this Quota.
        :type member: int
        """
        self._member = member

    @property
    def members_per_pool(self):
        """Gets the members_per_pool of this Quota.

        单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The members_per_pool of this Quota.
        :rtype: int
        """
        return self._members_per_pool

    @members_per_pool.setter
    def members_per_pool(self, members_per_pool):
        """Sets the members_per_pool of this Quota.

        单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param members_per_pool: The members_per_pool of this Quota.
        :type members_per_pool: int
        """
        self._members_per_pool = members_per_pool

    @property
    def listeners_per_pool(self):
        """Gets the listeners_per_pool of this Quota.

        单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :return: The listeners_per_pool of this Quota.
        :rtype: int
        """
        return self._listeners_per_pool

    @listeners_per_pool.setter
    def listeners_per_pool(self, listeners_per_pool):
        """Sets the listeners_per_pool of this Quota.

        单个pool下的member的配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。

        :param listeners_per_pool: The listeners_per_pool of this Quota.
        :type listeners_per_pool: int
        """
        self._listeners_per_pool = listeners_per_pool

    @property
    def ipgroup(self):
        """Gets the ipgroup of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The ipgroup of this Quota.
        :rtype: int
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param ipgroup: The ipgroup of this Quota.
        :type ipgroup: int
        """
        self._ipgroup = ipgroup

    @property
    def ipgroup_bindings(self):
        """Gets the ipgroup_bindings of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The ipgroup_bindings of this Quota.
        :rtype: int
        """
        return self._ipgroup_bindings

    @ipgroup_bindings.setter
    def ipgroup_bindings(self, ipgroup_bindings):
        """Sets the ipgroup_bindings of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param ipgroup_bindings: The ipgroup_bindings of this Quota.
        :type ipgroup_bindings: int
        """
        self._ipgroup_bindings = ipgroup_bindings

    @property
    def ipgroup_max_length(self):
        """Gets the ipgroup_max_length of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The ipgroup_max_length of this Quota.
        :rtype: int
        """
        return self._ipgroup_max_length

    @ipgroup_max_length.setter
    def ipgroup_max_length(self, ipgroup_max_length):
        """Sets the ipgroup_max_length of this Quota.

        IP地址组配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param ipgroup_max_length: The ipgroup_max_length of this Quota.
        :type ipgroup_max_length: int
        """
        self._ipgroup_max_length = ipgroup_max_length

    @property
    def security_policy(self):
        """Gets the security_policy of this Quota.

        自定义安全策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The security_policy of this Quota.
        :rtype: int
        """
        return self._security_policy

    @security_policy.setter
    def security_policy(self, security_policy):
        """Sets the security_policy of this Quota.

        自定义安全策略配额。  取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param security_policy: The security_policy of this Quota.
        :type security_policy: int
        """
        self._security_policy = security_policy

    @property
    def listeners_per_loadbalancer(self):
        """Gets the listeners_per_loadbalancer of this Quota.

        单个LB实例下的监听器配额。 取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  > 当前单个LB下监听器配额实际未限制，但建议不要超过默认配额。

        :return: The listeners_per_loadbalancer of this Quota.
        :rtype: int
        """
        return self._listeners_per_loadbalancer

    @listeners_per_loadbalancer.setter
    def listeners_per_loadbalancer(self, listeners_per_loadbalancer):
        """Sets the listeners_per_loadbalancer of this Quota.

        单个LB实例下的监听器配额。 取值： - 大于等于0：表示当前配额数量。 - -1：表示无配额限制。  > 当前单个LB下监听器配额实际未限制，但建议不要超过默认配额。

        :param listeners_per_loadbalancer: The listeners_per_loadbalancer of this Quota.
        :type listeners_per_loadbalancer: int
        """
        self._listeners_per_loadbalancer = listeners_per_loadbalancer

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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
