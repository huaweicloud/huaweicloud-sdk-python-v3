# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleScopeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'action': 'str',
        'status': 'str',
        'exception_ips': 'str',
        'source_ips': 'str',
        'source_ports': 'str',
        'db_ids': 'str',
        'db_names': 'str',
        'db_users': 'str',
        'all_audit': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'action': 'action',
        'status': 'status',
        'exception_ips': 'exception_ips',
        'source_ips': 'source_ips',
        'source_ports': 'source_ports',
        'db_ids': 'db_ids',
        'db_names': 'db_names',
        'db_users': 'db_users',
        'all_audit': 'all_audit'
    }

    def __init__(self, id=None, name=None, action=None, status=None, exception_ips=None, source_ips=None, source_ports=None, db_ids=None, db_names=None, db_users=None, all_audit=None):
        """RuleScopeInfo

        The model defined in huaweicloud sdk

        :param id: 审计范围规则ID
        :type id: str
        :param name: 审计范围名称
        :type name: str
        :param action: 审计范围动作
        :type action: str
        :param status: 审计范围规则状态
        :type status: str
        :param exception_ips: 审计范围例外IP
        :type exception_ips: str
        :param source_ips: 审计范围规则源IP
        :type source_ips: str
        :param source_ports: 审计范围源端口
        :type source_ports: str
        :param db_ids: 数据库ID
        :type db_ids: str
        :param db_names: 数据库名称
        :type db_names: str
        :param db_users: 数据库用户
        :type db_users: str
        :param all_audit: 是否全审计
        :type all_audit: bool
        """
        
        

        self._id = None
        self._name = None
        self._action = None
        self._status = None
        self._exception_ips = None
        self._source_ips = None
        self._source_ports = None
        self._db_ids = None
        self._db_names = None
        self._db_users = None
        self._all_audit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if exception_ips is not None:
            self.exception_ips = exception_ips
        if source_ips is not None:
            self.source_ips = source_ips
        if source_ports is not None:
            self.source_ports = source_ports
        if db_ids is not None:
            self.db_ids = db_ids
        if db_names is not None:
            self.db_names = db_names
        if db_users is not None:
            self.db_users = db_users
        if all_audit is not None:
            self.all_audit = all_audit

    @property
    def id(self):
        """Gets the id of this RuleScopeInfo.

        审计范围规则ID

        :return: The id of this RuleScopeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleScopeInfo.

        审计范围规则ID

        :param id: The id of this RuleScopeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RuleScopeInfo.

        审计范围名称

        :return: The name of this RuleScopeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleScopeInfo.

        审计范围名称

        :param name: The name of this RuleScopeInfo.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        """Gets the action of this RuleScopeInfo.

        审计范围动作

        :return: The action of this RuleScopeInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RuleScopeInfo.

        审计范围动作

        :param action: The action of this RuleScopeInfo.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        """Gets the status of this RuleScopeInfo.

        审计范围规则状态

        :return: The status of this RuleScopeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RuleScopeInfo.

        审计范围规则状态

        :param status: The status of this RuleScopeInfo.
        :type status: str
        """
        self._status = status

    @property
    def exception_ips(self):
        """Gets the exception_ips of this RuleScopeInfo.

        审计范围例外IP

        :return: The exception_ips of this RuleScopeInfo.
        :rtype: str
        """
        return self._exception_ips

    @exception_ips.setter
    def exception_ips(self, exception_ips):
        """Sets the exception_ips of this RuleScopeInfo.

        审计范围例外IP

        :param exception_ips: The exception_ips of this RuleScopeInfo.
        :type exception_ips: str
        """
        self._exception_ips = exception_ips

    @property
    def source_ips(self):
        """Gets the source_ips of this RuleScopeInfo.

        审计范围规则源IP

        :return: The source_ips of this RuleScopeInfo.
        :rtype: str
        """
        return self._source_ips

    @source_ips.setter
    def source_ips(self, source_ips):
        """Sets the source_ips of this RuleScopeInfo.

        审计范围规则源IP

        :param source_ips: The source_ips of this RuleScopeInfo.
        :type source_ips: str
        """
        self._source_ips = source_ips

    @property
    def source_ports(self):
        """Gets the source_ports of this RuleScopeInfo.

        审计范围源端口

        :return: The source_ports of this RuleScopeInfo.
        :rtype: str
        """
        return self._source_ports

    @source_ports.setter
    def source_ports(self, source_ports):
        """Sets the source_ports of this RuleScopeInfo.

        审计范围源端口

        :param source_ports: The source_ports of this RuleScopeInfo.
        :type source_ports: str
        """
        self._source_ports = source_ports

    @property
    def db_ids(self):
        """Gets the db_ids of this RuleScopeInfo.

        数据库ID

        :return: The db_ids of this RuleScopeInfo.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        """Sets the db_ids of this RuleScopeInfo.

        数据库ID

        :param db_ids: The db_ids of this RuleScopeInfo.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def db_names(self):
        """Gets the db_names of this RuleScopeInfo.

        数据库名称

        :return: The db_names of this RuleScopeInfo.
        :rtype: str
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        """Sets the db_names of this RuleScopeInfo.

        数据库名称

        :param db_names: The db_names of this RuleScopeInfo.
        :type db_names: str
        """
        self._db_names = db_names

    @property
    def db_users(self):
        """Gets the db_users of this RuleScopeInfo.

        数据库用户

        :return: The db_users of this RuleScopeInfo.
        :rtype: str
        """
        return self._db_users

    @db_users.setter
    def db_users(self, db_users):
        """Sets the db_users of this RuleScopeInfo.

        数据库用户

        :param db_users: The db_users of this RuleScopeInfo.
        :type db_users: str
        """
        self._db_users = db_users

    @property
    def all_audit(self):
        """Gets the all_audit of this RuleScopeInfo.

        是否全审计

        :return: The all_audit of this RuleScopeInfo.
        :rtype: bool
        """
        return self._all_audit

    @all_audit.setter
    def all_audit(self, all_audit):
        """Sets the all_audit of this RuleScopeInfo.

        是否全审计

        :param all_audit: The all_audit of this RuleScopeInfo.
        :type all_audit: bool
        """
        self._all_audit = all_audit

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
        if not isinstance(other, RuleScopeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
