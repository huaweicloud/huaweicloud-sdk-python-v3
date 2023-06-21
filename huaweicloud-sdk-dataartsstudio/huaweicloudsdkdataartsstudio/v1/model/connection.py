# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Connection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'guid': 'str',
        'display_text': 'str',
        'type_name': 'str',
        'connection_type': 'str',
        'qualified_name': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'display_text': 'display_text',
        'type_name': 'type_name',
        'connection_type': 'connection_type',
        'qualified_name': 'qualified_name'
    }

    def __init__(self, guid=None, display_text=None, type_name=None, connection_type=None, qualified_name=None):
        """Connection

        The model defined in huaweicloud sdk

        :param guid: 关联guid
        :type guid: str
        :param display_text: 显示内容
        :type display_text: str
        :param type_name: 类型名称
        :type type_name: str
        :param connection_type: 连接类型
        :type connection_type: str
        :param qualified_name: 限定名称
        :type qualified_name: str
        """
        
        

        self._guid = None
        self._display_text = None
        self._type_name = None
        self._connection_type = None
        self._qualified_name = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if display_text is not None:
            self.display_text = display_text
        if type_name is not None:
            self.type_name = type_name
        if connection_type is not None:
            self.connection_type = connection_type
        if qualified_name is not None:
            self.qualified_name = qualified_name

    @property
    def guid(self):
        """Gets the guid of this Connection.

        关联guid

        :return: The guid of this Connection.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Connection.

        关联guid

        :param guid: The guid of this Connection.
        :type guid: str
        """
        self._guid = guid

    @property
    def display_text(self):
        """Gets the display_text of this Connection.

        显示内容

        :return: The display_text of this Connection.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this Connection.

        显示内容

        :param display_text: The display_text of this Connection.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def type_name(self):
        """Gets the type_name of this Connection.

        类型名称

        :return: The type_name of this Connection.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this Connection.

        类型名称

        :param type_name: The type_name of this Connection.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def connection_type(self):
        """Gets the connection_type of this Connection.

        连接类型

        :return: The connection_type of this Connection.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this Connection.

        连接类型

        :param connection_type: The connection_type of this Connection.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def qualified_name(self):
        """Gets the qualified_name of this Connection.

        限定名称

        :return: The qualified_name of this Connection.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this Connection.

        限定名称

        :param qualified_name: The qualified_name of this Connection.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
