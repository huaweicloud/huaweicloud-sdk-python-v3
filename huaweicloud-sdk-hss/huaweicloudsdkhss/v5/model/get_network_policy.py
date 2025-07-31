# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetNetworkPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'name': 'str',
        'namespace': 'str',
        'policy_content': 'NetworkPolicyBody',
        'create_time': 'datetime',
        'deploy_status': 'bool'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'name': 'name',
        'namespace': 'namespace',
        'policy_content': 'policy_content',
        'create_time': 'create_time',
        'deploy_status': 'deploy_status'
    }

    def __init__(self, policy_id=None, name=None, namespace=None, policy_content=None, create_time=None, deploy_status=None):
        r"""GetNetworkPolicy

        The model defined in huaweicloud sdk

        :param policy_id: 策略Id
        :type policy_id: str
        :param name: 策略名称
        :type name: str
        :param namespace: 命名空间
        :type namespace: str
        :param policy_content: 
        :type policy_content: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
        :param create_time: 创建时间
        :type create_time: datetime
        :param deploy_status: 下发策略到cce成功与否
        :type deploy_status: bool
        """
        
        

        self._policy_id = None
        self._name = None
        self._namespace = None
        self._policy_content = None
        self._create_time = None
        self._deploy_status = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if policy_content is not None:
            self.policy_content = policy_content
        if create_time is not None:
            self.create_time = create_time
        if deploy_status is not None:
            self.deploy_status = deploy_status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this GetNetworkPolicy.

        策略Id

        :return: The policy_id of this GetNetworkPolicy.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this GetNetworkPolicy.

        策略Id

        :param policy_id: The policy_id of this GetNetworkPolicy.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def name(self):
        r"""Gets the name of this GetNetworkPolicy.

        策略名称

        :return: The name of this GetNetworkPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetNetworkPolicy.

        策略名称

        :param name: The name of this GetNetworkPolicy.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this GetNetworkPolicy.

        命名空间

        :return: The namespace of this GetNetworkPolicy.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this GetNetworkPolicy.

        命名空间

        :param namespace: The namespace of this GetNetworkPolicy.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policy_content(self):
        r"""Gets the policy_content of this GetNetworkPolicy.

        :return: The policy_content of this GetNetworkPolicy.
        :rtype: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
        """
        return self._policy_content

    @policy_content.setter
    def policy_content(self, policy_content):
        r"""Sets the policy_content of this GetNetworkPolicy.

        :param policy_content: The policy_content of this GetNetworkPolicy.
        :type policy_content: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
        """
        self._policy_content = policy_content

    @property
    def create_time(self):
        r"""Gets the create_time of this GetNetworkPolicy.

        创建时间

        :return: The create_time of this GetNetworkPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GetNetworkPolicy.

        创建时间

        :param create_time: The create_time of this GetNetworkPolicy.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def deploy_status(self):
        r"""Gets the deploy_status of this GetNetworkPolicy.

        下发策略到cce成功与否

        :return: The deploy_status of this GetNetworkPolicy.
        :rtype: bool
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        r"""Sets the deploy_status of this GetNetworkPolicy.

        下发策略到cce成功与否

        :param deploy_status: The deploy_status of this GetNetworkPolicy.
        :type deploy_status: bool
        """
        self._deploy_status = deploy_status

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
        if not isinstance(other, GetNetworkPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
