# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleScopeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'db_ids': 'str',
        'db_names': 'str',
        'db_users': 'str',
        'exception_ips': 'str',
        'rule_name': 'str',
        'source_ips': 'str',
        'source_ports': 'str'
    }

    attribute_map = {
        'action': 'action',
        'db_ids': 'db_ids',
        'db_names': 'db_names',
        'db_users': 'db_users',
        'exception_ips': 'exception_ips',
        'rule_name': 'rule_name',
        'source_ips': 'source_ips',
        'source_ports': 'source_ports'
    }

    def __init__(self, action=None, db_ids=None, db_names=None, db_users=None, exception_ips=None, rule_name=None, source_ips=None, source_ports=None):
        r"""RuleScopeRequest

        The model defined in huaweicloud sdk

        :param action: 操作类型，多个用英文,分隔
        :type action: str
        :param db_ids: 数据库ID，多个用英文逗号分隔，全部传[ALL]
        :type db_ids: str
        :param db_names: 数据库名称，多个用英文逗号分隔，全部传[全部数据库]
        :type db_names: str
        :param db_users: 数据库账号，多个用英文逗号分隔
        :type db_users: str
        :param exception_ips: 例外IP，多个用英文逗号分隔
        :type exception_ips: str
        :param rule_name: 名称
        :type rule_name: str
        :param source_ips: 源IP，多个用英文逗号分隔
        :type source_ips: str
        :param source_ports: 源端口，多个用英文逗号分隔
        :type source_ports: str
        """
        
        

        self._action = None
        self._db_ids = None
        self._db_names = None
        self._db_users = None
        self._exception_ips = None
        self._rule_name = None
        self._source_ips = None
        self._source_ports = None
        self.discriminator = None

        if action is not None:
            self.action = action
        self.db_ids = db_ids
        self.db_names = db_names
        if db_users is not None:
            self.db_users = db_users
        if exception_ips is not None:
            self.exception_ips = exception_ips
        self.rule_name = rule_name
        if source_ips is not None:
            self.source_ips = source_ips
        if source_ports is not None:
            self.source_ports = source_ports

    @property
    def action(self):
        r"""Gets the action of this RuleScopeRequest.

        操作类型，多个用英文,分隔

        :return: The action of this RuleScopeRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RuleScopeRequest.

        操作类型，多个用英文,分隔

        :param action: The action of this RuleScopeRequest.
        :type action: str
        """
        self._action = action

    @property
    def db_ids(self):
        r"""Gets the db_ids of this RuleScopeRequest.

        数据库ID，多个用英文逗号分隔，全部传[ALL]

        :return: The db_ids of this RuleScopeRequest.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this RuleScopeRequest.

        数据库ID，多个用英文逗号分隔，全部传[ALL]

        :param db_ids: The db_ids of this RuleScopeRequest.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def db_names(self):
        r"""Gets the db_names of this RuleScopeRequest.

        数据库名称，多个用英文逗号分隔，全部传[全部数据库]

        :return: The db_names of this RuleScopeRequest.
        :rtype: str
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this RuleScopeRequest.

        数据库名称，多个用英文逗号分隔，全部传[全部数据库]

        :param db_names: The db_names of this RuleScopeRequest.
        :type db_names: str
        """
        self._db_names = db_names

    @property
    def db_users(self):
        r"""Gets the db_users of this RuleScopeRequest.

        数据库账号，多个用英文逗号分隔

        :return: The db_users of this RuleScopeRequest.
        :rtype: str
        """
        return self._db_users

    @db_users.setter
    def db_users(self, db_users):
        r"""Sets the db_users of this RuleScopeRequest.

        数据库账号，多个用英文逗号分隔

        :param db_users: The db_users of this RuleScopeRequest.
        :type db_users: str
        """
        self._db_users = db_users

    @property
    def exception_ips(self):
        r"""Gets the exception_ips of this RuleScopeRequest.

        例外IP，多个用英文逗号分隔

        :return: The exception_ips of this RuleScopeRequest.
        :rtype: str
        """
        return self._exception_ips

    @exception_ips.setter
    def exception_ips(self, exception_ips):
        r"""Sets the exception_ips of this RuleScopeRequest.

        例外IP，多个用英文逗号分隔

        :param exception_ips: The exception_ips of this RuleScopeRequest.
        :type exception_ips: str
        """
        self._exception_ips = exception_ips

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleScopeRequest.

        名称

        :return: The rule_name of this RuleScopeRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleScopeRequest.

        名称

        :param rule_name: The rule_name of this RuleScopeRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def source_ips(self):
        r"""Gets the source_ips of this RuleScopeRequest.

        源IP，多个用英文逗号分隔

        :return: The source_ips of this RuleScopeRequest.
        :rtype: str
        """
        return self._source_ips

    @source_ips.setter
    def source_ips(self, source_ips):
        r"""Sets the source_ips of this RuleScopeRequest.

        源IP，多个用英文逗号分隔

        :param source_ips: The source_ips of this RuleScopeRequest.
        :type source_ips: str
        """
        self._source_ips = source_ips

    @property
    def source_ports(self):
        r"""Gets the source_ports of this RuleScopeRequest.

        源端口，多个用英文逗号分隔

        :return: The source_ports of this RuleScopeRequest.
        :rtype: str
        """
        return self._source_ports

    @source_ports.setter
    def source_ports(self, source_ports):
        r"""Sets the source_ports of this RuleScopeRequest.

        源端口，多个用英文逗号分隔

        :param source_ports: The source_ports of this RuleScopeRequest.
        :type source_ports: str
        """
        self._source_ports = source_ports

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
        if not isinstance(other, RuleScopeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
