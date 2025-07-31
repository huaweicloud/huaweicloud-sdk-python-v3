# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNetworkPolicyRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace': 'str',
        'policy_content': 'NetworkPolicyBody'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'policy_content': 'policy_content'
    }

    def __init__(self, name=None, namespace=None, policy_content=None):
        r"""CreateNetworkPolicyRequestInfo

        The model defined in huaweicloud sdk

        :param name: 策略名称
        :type name: str
        :param namespace: 命名空间
        :type namespace: str
        :param policy_content: 
        :type policy_content: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
        """
        
        

        self._name = None
        self._namespace = None
        self._policy_content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        self.policy_content = policy_content

    @property
    def name(self):
        r"""Gets the name of this CreateNetworkPolicyRequestInfo.

        策略名称

        :return: The name of this CreateNetworkPolicyRequestInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateNetworkPolicyRequestInfo.

        策略名称

        :param name: The name of this CreateNetworkPolicyRequestInfo.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateNetworkPolicyRequestInfo.

        命名空间

        :return: The namespace of this CreateNetworkPolicyRequestInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateNetworkPolicyRequestInfo.

        命名空间

        :param namespace: The namespace of this CreateNetworkPolicyRequestInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policy_content(self):
        r"""Gets the policy_content of this CreateNetworkPolicyRequestInfo.

        :return: The policy_content of this CreateNetworkPolicyRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
        """
        return self._policy_content

    @policy_content.setter
    def policy_content(self, policy_content):
        r"""Sets the policy_content of this CreateNetworkPolicyRequestInfo.

        :param policy_content: The policy_content of this CreateNetworkPolicyRequestInfo.
        :type policy_content: :class:`huaweicloudsdkhss.v5.NetworkPolicyBody`
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
        if not isinstance(other, CreateNetworkPolicyRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
