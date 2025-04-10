# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteCommandRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_id': 'str',
        'command': 'str',
        'database': 'int'
    }

    attribute_map = {
        'client_id': 'client_id',
        'command': 'command',
        'database': 'database'
    }

    def __init__(self, client_id=None, command=None, database=None):
        r"""ExecuteCommandRequestBody

        The model defined in huaweicloud sdk

        :param client_id: 客户端ID
        :type client_id: str
        :param command: 命令
        :type command: str
        :param database: 数据库编号
        :type database: int
        """
        
        

        self._client_id = None
        self._command = None
        self._database = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if command is not None:
            self.command = command
        if database is not None:
            self.database = database

    @property
    def client_id(self):
        r"""Gets the client_id of this ExecuteCommandRequestBody.

        客户端ID

        :return: The client_id of this ExecuteCommandRequestBody.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ExecuteCommandRequestBody.

        客户端ID

        :param client_id: The client_id of this ExecuteCommandRequestBody.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def command(self):
        r"""Gets the command of this ExecuteCommandRequestBody.

        命令

        :return: The command of this ExecuteCommandRequestBody.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ExecuteCommandRequestBody.

        命令

        :param command: The command of this ExecuteCommandRequestBody.
        :type command: str
        """
        self._command = command

    @property
    def database(self):
        r"""Gets the database of this ExecuteCommandRequestBody.

        数据库编号

        :return: The database of this ExecuteCommandRequestBody.
        :rtype: int
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ExecuteCommandRequestBody.

        数据库编号

        :param database: The database of this ExecuteCommandRequestBody.
        :type database: int
        """
        self._database = database

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
        if not isinstance(other, ExecuteCommandRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
