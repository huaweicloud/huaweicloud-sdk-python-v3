# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupPolicyResponseInfo:

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
        'policy_name': 'str',
        'pod_selector': 'str',
        'security_groups': 'list[SecurityGroup]',
        'workload_id': 'str',
        'workload_name': 'str',
        'workload_type': 'str',
        'namespace_id': 'str',
        'namespace': 'str',
        'create_time': 'str',
        'policy_content': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'pod_selector': 'pod_selector',
        'security_groups': 'security_groups',
        'workload_id': 'workload_id',
        'workload_name': 'workload_name',
        'workload_type': 'workload_type',
        'namespace_id': 'namespace_id',
        'namespace': 'namespace',
        'create_time': 'create_time',
        'policy_content': 'policy_content'
    }

    def __init__(self, policy_id=None, policy_name=None, pod_selector=None, security_groups=None, workload_id=None, workload_name=None, workload_type=None, namespace_id=None, namespace=None, create_time=None, policy_content=None):
        r"""SecurityGroupPolicyResponseInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略Id
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param pod_selector: 选择器
        :type pod_selector: str
        :param security_groups: 安全组列表
        :type security_groups: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        :param workload_id: 工作负载ID
        :type workload_id: str
        :param workload_name: 工作负载名称
        :type workload_name: str
        :param workload_type: 工作负载类型
        :type workload_type: str
        :param namespace_id: 命名空间id
        :type namespace_id: str
        :param namespace: 命名空间
        :type namespace: str
        :param create_time: 创建时间
        :type create_time: str
        :param policy_content: 策略yaml格式内容
        :type policy_content: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._pod_selector = None
        self._security_groups = None
        self._workload_id = None
        self._workload_name = None
        self._workload_type = None
        self._namespace_id = None
        self._namespace = None
        self._create_time = None
        self._policy_content = None
        self.discriminator = None

        self.policy_id = policy_id
        self.policy_name = policy_name
        self.pod_selector = pod_selector
        self.security_groups = security_groups
        self.workload_id = workload_id
        self.workload_name = workload_name
        self.workload_type = workload_type
        if namespace_id is not None:
            self.namespace_id = namespace_id
        self.namespace = namespace
        self.create_time = create_time
        self.policy_content = policy_content

    @property
    def policy_id(self):
        r"""Gets the policy_id of this SecurityGroupPolicyResponseInfo.

        策略Id

        :return: The policy_id of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this SecurityGroupPolicyResponseInfo.

        策略Id

        :param policy_id: The policy_id of this SecurityGroupPolicyResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this SecurityGroupPolicyResponseInfo.

        策略名称

        :return: The policy_name of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this SecurityGroupPolicyResponseInfo.

        策略名称

        :param policy_name: The policy_name of this SecurityGroupPolicyResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def pod_selector(self):
        r"""Gets the pod_selector of this SecurityGroupPolicyResponseInfo.

        选择器

        :return: The pod_selector of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        r"""Sets the pod_selector of this SecurityGroupPolicyResponseInfo.

        选择器

        :param pod_selector: The pod_selector of this SecurityGroupPolicyResponseInfo.
        :type pod_selector: str
        """
        self._pod_selector = pod_selector

    @property
    def security_groups(self):
        r"""Gets the security_groups of this SecurityGroupPolicyResponseInfo.

        安全组列表

        :return: The security_groups of this SecurityGroupPolicyResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this SecurityGroupPolicyResponseInfo.

        安全组列表

        :param security_groups: The security_groups of this SecurityGroupPolicyResponseInfo.
        :type security_groups: list[:class:`huaweicloudsdkhss.v5.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def workload_id(self):
        r"""Gets the workload_id of this SecurityGroupPolicyResponseInfo.

        工作负载ID

        :return: The workload_id of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this SecurityGroupPolicyResponseInfo.

        工作负载ID

        :param workload_id: The workload_id of this SecurityGroupPolicyResponseInfo.
        :type workload_id: str
        """
        self._workload_id = workload_id

    @property
    def workload_name(self):
        r"""Gets the workload_name of this SecurityGroupPolicyResponseInfo.

        工作负载名称

        :return: The workload_name of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this SecurityGroupPolicyResponseInfo.

        工作负载名称

        :param workload_name: The workload_name of this SecurityGroupPolicyResponseInfo.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def workload_type(self):
        r"""Gets the workload_type of this SecurityGroupPolicyResponseInfo.

        工作负载类型

        :return: The workload_type of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this SecurityGroupPolicyResponseInfo.

        工作负载类型

        :param workload_type: The workload_type of this SecurityGroupPolicyResponseInfo.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this SecurityGroupPolicyResponseInfo.

        命名空间id

        :return: The namespace_id of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this SecurityGroupPolicyResponseInfo.

        命名空间id

        :param namespace_id: The namespace_id of this SecurityGroupPolicyResponseInfo.
        :type namespace_id: str
        """
        self._namespace_id = namespace_id

    @property
    def namespace(self):
        r"""Gets the namespace of this SecurityGroupPolicyResponseInfo.

        命名空间

        :return: The namespace of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this SecurityGroupPolicyResponseInfo.

        命名空间

        :param namespace: The namespace of this SecurityGroupPolicyResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def create_time(self):
        r"""Gets the create_time of this SecurityGroupPolicyResponseInfo.

        创建时间

        :return: The create_time of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SecurityGroupPolicyResponseInfo.

        创建时间

        :param create_time: The create_time of this SecurityGroupPolicyResponseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def policy_content(self):
        r"""Gets the policy_content of this SecurityGroupPolicyResponseInfo.

        策略yaml格式内容

        :return: The policy_content of this SecurityGroupPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_content

    @policy_content.setter
    def policy_content(self, policy_content):
        r"""Sets the policy_content of this SecurityGroupPolicyResponseInfo.

        策略yaml格式内容

        :param policy_content: The policy_content of this SecurityGroupPolicyResponseInfo.
        :type policy_content: str
        """
        self._policy_content = policy_content

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
        if not isinstance(other, SecurityGroupPolicyResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
