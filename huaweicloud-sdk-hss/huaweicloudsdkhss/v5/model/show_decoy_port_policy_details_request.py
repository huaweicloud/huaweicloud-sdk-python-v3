# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDecoyPortPolicyDetailsRequest:

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
        'policy_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'policy_id': 'policy_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, policy_id=None, offset=None, limit=None):
        r"""ShowDecoyPortPolicyDetailsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param policy_id: policy ID
        :type policy_id: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._policy_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.policy_id = policy_id
        self.offset = offset
        self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDecoyPortPolicyDetailsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ShowDecoyPortPolicyDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDecoyPortPolicyDetailsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ShowDecoyPortPolicyDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowDecoyPortPolicyDetailsRequest.

        policy ID

        :return: The policy_id of this ShowDecoyPortPolicyDetailsRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowDecoyPortPolicyDetailsRequest.

        policy ID

        :param policy_id: The policy_id of this ShowDecoyPortPolicyDetailsRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowDecoyPortPolicyDetailsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ShowDecoyPortPolicyDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDecoyPortPolicyDetailsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ShowDecoyPortPolicyDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDecoyPortPolicyDetailsRequest.

        每页显示个数

        :return: The limit of this ShowDecoyPortPolicyDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDecoyPortPolicyDetailsRequest.

        每页显示个数

        :param limit: The limit of this ShowDecoyPortPolicyDetailsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowDecoyPortPolicyDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
