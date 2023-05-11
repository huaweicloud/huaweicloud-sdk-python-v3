# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'sql_name': 'str',
        'sql': 'str',
        'description': 'str',
        'group': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'sql_name': 'sql_name',
        'sql': 'sql',
        'description': 'description',
        'group': 'group',
        'owner': 'owner'
    }

    def __init__(self, sql_id=None, sql_name=None, sql=None, description=None, group=None, owner=None):
        """SqlsResp

        The model defined in huaweicloud sdk

        :param sql_id: SQL模板ID。
        :type sql_id: str
        :param sql_name: SQL模板名称。
        :type sql_name: str
        :param sql: SQL模板文本。
        :type sql: str
        :param description: SQL模板描述信息。
        :type description: str
        :param group: 分组名称。
        :type group: str
        :param owner: SQL模板的创建者。
        :type owner: str
        """
        
        

        self._sql_id = None
        self._sql_name = None
        self._sql = None
        self._description = None
        self._group = None
        self._owner = None
        self.discriminator = None

        if sql_id is not None:
            self.sql_id = sql_id
        if sql_name is not None:
            self.sql_name = sql_name
        if sql is not None:
            self.sql = sql
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group
        if owner is not None:
            self.owner = owner

    @property
    def sql_id(self):
        """Gets the sql_id of this SqlsResp.

        SQL模板ID。

        :return: The sql_id of this SqlsResp.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """Sets the sql_id of this SqlsResp.

        SQL模板ID。

        :param sql_id: The sql_id of this SqlsResp.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_name(self):
        """Gets the sql_name of this SqlsResp.

        SQL模板名称。

        :return: The sql_name of this SqlsResp.
        :rtype: str
        """
        return self._sql_name

    @sql_name.setter
    def sql_name(self, sql_name):
        """Sets the sql_name of this SqlsResp.

        SQL模板名称。

        :param sql_name: The sql_name of this SqlsResp.
        :type sql_name: str
        """
        self._sql_name = sql_name

    @property
    def sql(self):
        """Gets the sql of this SqlsResp.

        SQL模板文本。

        :return: The sql of this SqlsResp.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this SqlsResp.

        SQL模板文本。

        :param sql: The sql of this SqlsResp.
        :type sql: str
        """
        self._sql = sql

    @property
    def description(self):
        """Gets the description of this SqlsResp.

        SQL模板描述信息。

        :return: The description of this SqlsResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SqlsResp.

        SQL模板描述信息。

        :param description: The description of this SqlsResp.
        :type description: str
        """
        self._description = description

    @property
    def group(self):
        """Gets the group of this SqlsResp.

        分组名称。

        :return: The group of this SqlsResp.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SqlsResp.

        分组名称。

        :param group: The group of this SqlsResp.
        :type group: str
        """
        self._group = group

    @property
    def owner(self):
        """Gets the owner of this SqlsResp.

        SQL模板的创建者。

        :return: The owner of this SqlsResp.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SqlsResp.

        SQL模板的创建者。

        :param owner: The owner of this SqlsResp.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, SqlsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
