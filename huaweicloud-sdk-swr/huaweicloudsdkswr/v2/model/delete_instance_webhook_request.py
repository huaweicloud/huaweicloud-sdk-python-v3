# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInstanceWebhookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'namespace_name': 'str',
        'policy_id': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'policy_id': 'policy_id'
    }

    def __init__(self, instance_id=None, namespace_name=None, policy_id=None):
        r"""DeleteInstanceWebhookRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param policy_id: 触发器策略ID
        :type policy_id: int
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._policy_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.policy_id = policy_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteInstanceWebhookRequest.

        企业仓库实例ID

        :return: The instance_id of this DeleteInstanceWebhookRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteInstanceWebhookRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this DeleteInstanceWebhookRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this DeleteInstanceWebhookRequest.

        命名空间名称

        :return: The namespace_name of this DeleteInstanceWebhookRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this DeleteInstanceWebhookRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this DeleteInstanceWebhookRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this DeleteInstanceWebhookRequest.

        触发器策略ID

        :return: The policy_id of this DeleteInstanceWebhookRequest.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this DeleteInstanceWebhookRequest.

        触发器策略ID

        :param policy_id: The policy_id of this DeleteInstanceWebhookRequest.
        :type policy_id: int
        """
        self._policy_id = policy_id

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
        if not isinstance(other, DeleteInstanceWebhookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
