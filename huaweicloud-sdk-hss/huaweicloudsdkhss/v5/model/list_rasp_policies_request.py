# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRaspPoliciesRequest:

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
        'os_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'policy_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'os_type': 'os_type',
        'limit': 'limit',
        'offset': 'offset',
        'policy_name': 'policy_name'
    }

    def __init__(self, region=None, enterprise_project_id=None, os_type=None, limit=None, offset=None, policy_name=None):
        r"""ListRaspPoliciesRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param os_type: 操作系统类型，包含如下2种。 - Linux - Windows
        :type os_type: str
        :param limit: 每页显示个数，默认10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param policy_name: 策略名称
        :type policy_name: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._os_type = None
        self._limit = None
        self._offset = None
        self._policy_name = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if os_type is not None:
            self.os_type = os_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if policy_name is not None:
            self.policy_name = policy_name

    @property
    def region(self):
        r"""Gets the region of this ListRaspPoliciesRequest.

        region id

        :return: The region of this ListRaspPoliciesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListRaspPoliciesRequest.

        region id

        :param region: The region of this ListRaspPoliciesRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRaspPoliciesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListRaspPoliciesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRaspPoliciesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListRaspPoliciesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ListRaspPoliciesRequest.

        操作系统类型，包含如下2种。 - Linux - Windows

        :return: The os_type of this ListRaspPoliciesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListRaspPoliciesRequest.

        操作系统类型，包含如下2种。 - Linux - Windows

        :param os_type: The os_type of this ListRaspPoliciesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def limit(self):
        r"""Gets the limit of this ListRaspPoliciesRequest.

        每页显示个数，默认10

        :return: The limit of this ListRaspPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRaspPoliciesRequest.

        每页显示个数，默认10

        :param limit: The limit of this ListRaspPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRaspPoliciesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListRaspPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRaspPoliciesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListRaspPoliciesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListRaspPoliciesRequest.

        策略名称

        :return: The policy_name of this ListRaspPoliciesRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListRaspPoliciesRequest.

        策略名称

        :param policy_name: The policy_name of this ListRaspPoliciesRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, ListRaspPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
