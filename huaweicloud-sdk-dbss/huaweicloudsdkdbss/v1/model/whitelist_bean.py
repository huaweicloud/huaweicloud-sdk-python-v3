# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WhitelistBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_timestamp_ms': 'int',
        'db_ids': 'list[str]',
        'desc': 'str',
        'enabled': 'bool',
        'id': 'str',
        'sql': 'str',
        'update_timestamp_ms': 'int'
    }

    attribute_map = {
        'create_timestamp_ms': 'create_timestamp_ms',
        'db_ids': 'db_ids',
        'desc': 'desc',
        'enabled': 'enabled',
        'id': 'id',
        'sql': 'sql',
        'update_timestamp_ms': 'update_timestamp_ms'
    }

    def __init__(self, create_timestamp_ms=None, db_ids=None, desc=None, enabled=None, id=None, sql=None, update_timestamp_ms=None):
        r"""WhitelistBean

        The model defined in huaweicloud sdk

        :param create_timestamp_ms: 创建时间
        :type create_timestamp_ms: int
        :param db_ids: 数据库IDs
        :type db_ids: list[str]
        :param desc: 描述
        :type desc: str
        :param enabled: 状态 - true:启用 - false: 禁用
        :type enabled: bool
        :param id: 记录ID
        :type id: str
        :param sql: SQL语句
        :type sql: str
        :param update_timestamp_ms: 更新时间
        :type update_timestamp_ms: int
        """
        
        

        self._create_timestamp_ms = None
        self._db_ids = None
        self._desc = None
        self._enabled = None
        self._id = None
        self._sql = None
        self._update_timestamp_ms = None
        self.discriminator = None

        if create_timestamp_ms is not None:
            self.create_timestamp_ms = create_timestamp_ms
        if db_ids is not None:
            self.db_ids = db_ids
        if desc is not None:
            self.desc = desc
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if sql is not None:
            self.sql = sql
        if update_timestamp_ms is not None:
            self.update_timestamp_ms = update_timestamp_ms

    @property
    def create_timestamp_ms(self):
        r"""Gets the create_timestamp_ms of this WhitelistBean.

        创建时间

        :return: The create_timestamp_ms of this WhitelistBean.
        :rtype: int
        """
        return self._create_timestamp_ms

    @create_timestamp_ms.setter
    def create_timestamp_ms(self, create_timestamp_ms):
        r"""Sets the create_timestamp_ms of this WhitelistBean.

        创建时间

        :param create_timestamp_ms: The create_timestamp_ms of this WhitelistBean.
        :type create_timestamp_ms: int
        """
        self._create_timestamp_ms = create_timestamp_ms

    @property
    def db_ids(self):
        r"""Gets the db_ids of this WhitelistBean.

        数据库IDs

        :return: The db_ids of this WhitelistBean.
        :rtype: list[str]
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this WhitelistBean.

        数据库IDs

        :param db_ids: The db_ids of this WhitelistBean.
        :type db_ids: list[str]
        """
        self._db_ids = db_ids

    @property
    def desc(self):
        r"""Gets the desc of this WhitelistBean.

        描述

        :return: The desc of this WhitelistBean.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this WhitelistBean.

        描述

        :param desc: The desc of this WhitelistBean.
        :type desc: str
        """
        self._desc = desc

    @property
    def enabled(self):
        r"""Gets the enabled of this WhitelistBean.

        状态 - true:启用 - false: 禁用

        :return: The enabled of this WhitelistBean.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this WhitelistBean.

        状态 - true:启用 - false: 禁用

        :param enabled: The enabled of this WhitelistBean.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        r"""Gets the id of this WhitelistBean.

        记录ID

        :return: The id of this WhitelistBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WhitelistBean.

        记录ID

        :param id: The id of this WhitelistBean.
        :type id: str
        """
        self._id = id

    @property
    def sql(self):
        r"""Gets the sql of this WhitelistBean.

        SQL语句

        :return: The sql of this WhitelistBean.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this WhitelistBean.

        SQL语句

        :param sql: The sql of this WhitelistBean.
        :type sql: str
        """
        self._sql = sql

    @property
    def update_timestamp_ms(self):
        r"""Gets the update_timestamp_ms of this WhitelistBean.

        更新时间

        :return: The update_timestamp_ms of this WhitelistBean.
        :rtype: int
        """
        return self._update_timestamp_ms

    @update_timestamp_ms.setter
    def update_timestamp_ms(self, update_timestamp_ms):
        r"""Sets the update_timestamp_ms of this WhitelistBean.

        更新时间

        :param update_timestamp_ms: The update_timestamp_ms of this WhitelistBean.
        :type update_timestamp_ms: int
        """
        self._update_timestamp_ms = update_timestamp_ms

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
        if not isinstance(other, WhitelistBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
