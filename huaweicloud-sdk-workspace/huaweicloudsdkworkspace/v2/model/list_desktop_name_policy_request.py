# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopNamePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_contain_user': 'bool',
        'policy_name': 'str',
        'policy_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'is_contain_user': 'is_contain_user',
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, is_contain_user=None, policy_name=None, policy_id=None, offset=None, limit=None):
        """ListDesktopNamePolicyRequest

        The model defined in huaweicloud sdk

        :param is_contain_user: 是否包含用户名的桌面名称策略。 - true 包含 - false 不包含
        :type is_contain_user: bool
        :param policy_name: 策略名称，由数字、字母、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符，支持模糊筛选。
        :type policy_name: str
        :param policy_id: 策略id。
        :type policy_id: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-50，默认值50。
        :type limit: int
        """
        
        

        self._is_contain_user = None
        self._policy_name = None
        self._policy_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if is_contain_user is not None:
            self.is_contain_user = is_contain_user
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def is_contain_user(self):
        """Gets the is_contain_user of this ListDesktopNamePolicyRequest.

        是否包含用户名的桌面名称策略。 - true 包含 - false 不包含

        :return: The is_contain_user of this ListDesktopNamePolicyRequest.
        :rtype: bool
        """
        return self._is_contain_user

    @is_contain_user.setter
    def is_contain_user(self, is_contain_user):
        """Sets the is_contain_user of this ListDesktopNamePolicyRequest.

        是否包含用户名的桌面名称策略。 - true 包含 - false 不包含

        :param is_contain_user: The is_contain_user of this ListDesktopNamePolicyRequest.
        :type is_contain_user: bool
        """
        self._is_contain_user = is_contain_user

    @property
    def policy_name(self):
        """Gets the policy_name of this ListDesktopNamePolicyRequest.

        策略名称，由数字、字母、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符，支持模糊筛选。

        :return: The policy_name of this ListDesktopNamePolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ListDesktopNamePolicyRequest.

        策略名称，由数字、字母、下划线组成，必须以字母或下划线开头，长度范围为1~30个字符，支持模糊筛选。

        :param policy_name: The policy_name of this ListDesktopNamePolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        """Gets the policy_id of this ListDesktopNamePolicyRequest.

        策略id。

        :return: The policy_id of this ListDesktopNamePolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ListDesktopNamePolicyRequest.

        策略id。

        :param policy_id: The policy_id of this ListDesktopNamePolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def offset(self):
        """Gets the offset of this ListDesktopNamePolicyRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopNamePolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopNamePolicyRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopNamePolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDesktopNamePolicyRequest.

        用于分页查询，取值范围0-50，默认值50。

        :return: The limit of this ListDesktopNamePolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDesktopNamePolicyRequest.

        用于分页查询，取值范围0-50，默认值50。

        :param limit: The limit of this ListDesktopNamePolicyRequest.
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
        if not isinstance(other, ListDesktopNamePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
