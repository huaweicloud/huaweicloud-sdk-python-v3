# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSqlLimitControlReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'id': 'id',
        'action': 'action'
    }

    def __init__(self, db_name=None, id=None, action=None):
        r"""SwitchSqlLimitControlReqV3

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。
        :type db_name: str
        :param id: SQL限流ID。
        :type id: str
        :param action: SQL限流动作标志。 取值为“open”：表示开启当前SQL限流。 取值为“close”：表示关闭当前SQL限流。 取值为“disable_all”：表示禁用所有SQL限流。
        :type action: str
        """
        
        

        self._db_name = None
        self._id = None
        self._action = None
        self.discriminator = None

        self.db_name = db_name
        self.id = id
        self.action = action

    @property
    def db_name(self):
        r"""Gets the db_name of this SwitchSqlLimitControlReqV3.

        数据库名称。

        :return: The db_name of this SwitchSqlLimitControlReqV3.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SwitchSqlLimitControlReqV3.

        数据库名称。

        :param db_name: The db_name of this SwitchSqlLimitControlReqV3.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def id(self):
        r"""Gets the id of this SwitchSqlLimitControlReqV3.

        SQL限流ID。

        :return: The id of this SwitchSqlLimitControlReqV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SwitchSqlLimitControlReqV3.

        SQL限流ID。

        :param id: The id of this SwitchSqlLimitControlReqV3.
        :type id: str
        """
        self._id = id

    @property
    def action(self):
        r"""Gets the action of this SwitchSqlLimitControlReqV3.

        SQL限流动作标志。 取值为“open”：表示开启当前SQL限流。 取值为“close”：表示关闭当前SQL限流。 取值为“disable_all”：表示禁用所有SQL限流。

        :return: The action of this SwitchSqlLimitControlReqV3.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SwitchSqlLimitControlReqV3.

        SQL限流动作标志。 取值为“open”：表示开启当前SQL限流。 取值为“close”：表示关闭当前SQL限流。 取值为“disable_all”：表示禁用所有SQL限流。

        :param action: The action of this SwitchSqlLimitControlReqV3.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, SwitchSqlLimitControlReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
