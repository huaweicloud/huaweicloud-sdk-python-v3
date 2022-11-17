# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersForEnterpriseProjectResUsers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'id': 'str',
        'name': 'str',
        'enabled': 'bool',
        'description': 'str',
        'policy_num': 'int',
        'lastest_policy_time': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'id': 'id',
        'name': 'name',
        'enabled': 'enabled',
        'description': 'description',
        'policy_num': 'policy_num',
        'lastest_policy_time': 'lastest_policy_time'
    }

    def __init__(self, domain_id=None, id=None, name=None, enabled=None, description=None, policy_num=None, lastest_policy_time=None):
        """ListUsersForEnterpriseProjectResUsers

        The model defined in huaweicloud sdk

        :param domain_id: 授权用户所属账号ID。
        :type domain_id: str
        :param id: 授权用户ID。
        :type id: str
        :param name: 授权用户名。
        :type name: str
        :param enabled: 授权用户是否启用，true表示启用，false表示停用，默认为true。
        :type enabled: bool
        :param description: 授权用户描述信息。
        :type description: str
        :param policy_num: 授权用户的策略数。
        :type policy_num: int
        :param lastest_policy_time: 用户最近与企业项目关联策略的时间（毫秒）。
        :type lastest_policy_time: int
        """
        
        

        self._domain_id = None
        self._id = None
        self._name = None
        self._enabled = None
        self._description = None
        self._policy_num = None
        self._lastest_policy_time = None
        self.discriminator = None

        self.domain_id = domain_id
        self.id = id
        self.name = name
        self.enabled = enabled
        self.description = description
        self.policy_num = policy_num
        self.lastest_policy_time = lastest_policy_time

    @property
    def domain_id(self):
        """Gets the domain_id of this ListUsersForEnterpriseProjectResUsers.

        授权用户所属账号ID。

        :return: The domain_id of this ListUsersForEnterpriseProjectResUsers.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListUsersForEnterpriseProjectResUsers.

        授权用户所属账号ID。

        :param domain_id: The domain_id of this ListUsersForEnterpriseProjectResUsers.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        """Gets the id of this ListUsersForEnterpriseProjectResUsers.

        授权用户ID。

        :return: The id of this ListUsersForEnterpriseProjectResUsers.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListUsersForEnterpriseProjectResUsers.

        授权用户ID。

        :param id: The id of this ListUsersForEnterpriseProjectResUsers.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListUsersForEnterpriseProjectResUsers.

        授权用户名。

        :return: The name of this ListUsersForEnterpriseProjectResUsers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListUsersForEnterpriseProjectResUsers.

        授权用户名。

        :param name: The name of this ListUsersForEnterpriseProjectResUsers.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this ListUsersForEnterpriseProjectResUsers.

        授权用户是否启用，true表示启用，false表示停用，默认为true。

        :return: The enabled of this ListUsersForEnterpriseProjectResUsers.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListUsersForEnterpriseProjectResUsers.

        授权用户是否启用，true表示启用，false表示停用，默认为true。

        :param enabled: The enabled of this ListUsersForEnterpriseProjectResUsers.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def description(self):
        """Gets the description of this ListUsersForEnterpriseProjectResUsers.

        授权用户描述信息。

        :return: The description of this ListUsersForEnterpriseProjectResUsers.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListUsersForEnterpriseProjectResUsers.

        授权用户描述信息。

        :param description: The description of this ListUsersForEnterpriseProjectResUsers.
        :type description: str
        """
        self._description = description

    @property
    def policy_num(self):
        """Gets the policy_num of this ListUsersForEnterpriseProjectResUsers.

        授权用户的策略数。

        :return: The policy_num of this ListUsersForEnterpriseProjectResUsers.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        """Sets the policy_num of this ListUsersForEnterpriseProjectResUsers.

        授权用户的策略数。

        :param policy_num: The policy_num of this ListUsersForEnterpriseProjectResUsers.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def lastest_policy_time(self):
        """Gets the lastest_policy_time of this ListUsersForEnterpriseProjectResUsers.

        用户最近与企业项目关联策略的时间（毫秒）。

        :return: The lastest_policy_time of this ListUsersForEnterpriseProjectResUsers.
        :rtype: int
        """
        return self._lastest_policy_time

    @lastest_policy_time.setter
    def lastest_policy_time(self, lastest_policy_time):
        """Sets the lastest_policy_time of this ListUsersForEnterpriseProjectResUsers.

        用户最近与企业项目关联策略的时间（毫秒）。

        :param lastest_policy_time: The lastest_policy_time of this ListUsersForEnterpriseProjectResUsers.
        :type lastest_policy_time: int
        """
        self._lastest_policy_time = lastest_policy_time

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
        if not isinstance(other, ListUsersForEnterpriseProjectResUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
