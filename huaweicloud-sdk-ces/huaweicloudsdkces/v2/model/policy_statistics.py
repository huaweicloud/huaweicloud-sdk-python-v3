# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'policy_num': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'policy_num': 'policy_num'
    }

    def __init__(self, namespace=None, policy_num=None):
        """PolicyStatistics

        The model defined in huaweicloud sdk

        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param policy_num: 对应命名空间的告警策略数目
        :type policy_num: int
        """
        
        

        self._namespace = None
        self._policy_num = None
        self.discriminator = None

        self.namespace = namespace
        self.policy_num = policy_num

    @property
    def namespace(self):
        """Gets the namespace of this PolicyStatistics.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this PolicyStatistics.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PolicyStatistics.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this PolicyStatistics.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policy_num(self):
        """Gets the policy_num of this PolicyStatistics.

        对应命名空间的告警策略数目

        :return: The policy_num of this PolicyStatistics.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        """Sets the policy_num of this PolicyStatistics.

        对应命名空间的告警策略数目

        :param policy_num: The policy_num of this PolicyStatistics.
        :type policy_num: int
        """
        self._policy_num = policy_num

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
        if not isinstance(other, PolicyStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
