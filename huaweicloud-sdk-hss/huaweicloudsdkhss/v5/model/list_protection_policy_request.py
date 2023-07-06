# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'policy_name': 'str',
        'protect_policy_id': 'str',
        'operating_system': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'policy_name': 'policy_name',
        'protect_policy_id': 'protect_policy_id',
        'operating_system': 'operating_system'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, policy_name=None, protect_policy_id=None, operating_system=None):
        """ListProtectionPolicyRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param policy_name: 防护策略名称
        :type policy_name: str
        :param protect_policy_id: 防护策略id
        :type protect_policy_id: str
        :param operating_system: 策略支持的操作系统
        :type operating_system: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._policy_name = None
        self._protect_policy_id = None
        self._operating_system = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if policy_name is not None:
            self.policy_name = policy_name
        if protect_policy_id is not None:
            self.protect_policy_id = protect_policy_id
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def region(self):
        """Gets the region of this ListProtectionPolicyRequest.

        region id

        :return: The region of this ListProtectionPolicyRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListProtectionPolicyRequest.

        region id

        :param region: The region of this ListProtectionPolicyRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListProtectionPolicyRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListProtectionPolicyRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListProtectionPolicyRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListProtectionPolicyRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListProtectionPolicyRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListProtectionPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProtectionPolicyRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListProtectionPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProtectionPolicyRequest.

        每页显示个数

        :return: The limit of this ListProtectionPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProtectionPolicyRequest.

        每页显示个数

        :param limit: The limit of this ListProtectionPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_name(self):
        """Gets the policy_name of this ListProtectionPolicyRequest.

        防护策略名称

        :return: The policy_name of this ListProtectionPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ListProtectionPolicyRequest.

        防护策略名称

        :param policy_name: The policy_name of this ListProtectionPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def protect_policy_id(self):
        """Gets the protect_policy_id of this ListProtectionPolicyRequest.

        防护策略id

        :return: The protect_policy_id of this ListProtectionPolicyRequest.
        :rtype: str
        """
        return self._protect_policy_id

    @protect_policy_id.setter
    def protect_policy_id(self, protect_policy_id):
        """Sets the protect_policy_id of this ListProtectionPolicyRequest.

        防护策略id

        :param protect_policy_id: The protect_policy_id of this ListProtectionPolicyRequest.
        :type protect_policy_id: str
        """
        self._protect_policy_id = protect_policy_id

    @property
    def operating_system(self):
        """Gets the operating_system of this ListProtectionPolicyRequest.

        策略支持的操作系统

        :return: The operating_system of this ListProtectionPolicyRequest.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this ListProtectionPolicyRequest.

        策略支持的操作系统

        :param operating_system: The operating_system of this ListProtectionPolicyRequest.
        :type operating_system: str
        """
        self._operating_system = operating_system

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
        if not isinstance(other, ListProtectionPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
