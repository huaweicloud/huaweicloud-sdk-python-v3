# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjWhitelist:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_ids': 'list[str]',
        'desc': 'str',
        'enabled': 'bool',
        'sql': 'str'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'desc': 'desc',
        'enabled': 'enabled',
        'sql': 'sql'
    }

    def __init__(self, db_ids=None, desc=None, enabled=None, sql=None):
        r"""ObjWhitelist

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID
        :type db_ids: list[str]
        :param desc: 描述信息
        :type desc: str
        :param enabled: 状态
        :type enabled: bool
        :param sql: SQL语句
        :type sql: str
        """
        
        

        self._db_ids = None
        self._desc = None
        self._enabled = None
        self._sql = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if desc is not None:
            self.desc = desc
        if enabled is not None:
            self.enabled = enabled
        self.sql = sql

    @property
    def db_ids(self):
        r"""Gets the db_ids of this ObjWhitelist.

        数据库ID

        :return: The db_ids of this ObjWhitelist.
        :rtype: list[str]
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this ObjWhitelist.

        数据库ID

        :param db_ids: The db_ids of this ObjWhitelist.
        :type db_ids: list[str]
        """
        self._db_ids = db_ids

    @property
    def desc(self):
        r"""Gets the desc of this ObjWhitelist.

        描述信息

        :return: The desc of this ObjWhitelist.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ObjWhitelist.

        描述信息

        :param desc: The desc of this ObjWhitelist.
        :type desc: str
        """
        self._desc = desc

    @property
    def enabled(self):
        r"""Gets the enabled of this ObjWhitelist.

        状态

        :return: The enabled of this ObjWhitelist.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ObjWhitelist.

        状态

        :param enabled: The enabled of this ObjWhitelist.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def sql(self):
        r"""Gets the sql of this ObjWhitelist.

        SQL语句

        :return: The sql of this ObjWhitelist.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ObjWhitelist.

        SQL语句

        :param sql: The sql of this ObjWhitelist.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, ObjWhitelist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
