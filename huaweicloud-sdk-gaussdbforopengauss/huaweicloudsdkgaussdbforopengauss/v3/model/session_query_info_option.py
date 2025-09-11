# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionQueryInfoOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'client_ip': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'client_ip': 'client_ip',
        'user_name': 'user_name'
    }

    def __init__(self, database_name=None, client_ip=None, user_name=None):
        r"""SessionQueryInfoOption

        The model defined in huaweicloud sdk

        :param database_name: **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type database_name: str
        :param client_ip: **参数解释**： 客户端IP。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type client_ip: str
        :param user_name: **参数解释**： 用户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type user_name: str
        """
        
        

        self._database_name = None
        self._client_ip = None
        self._user_name = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if client_ip is not None:
            self.client_ip = client_ip
        if user_name is not None:
            self.user_name = user_name

    @property
    def database_name(self):
        r"""Gets the database_name of this SessionQueryInfoOption.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The database_name of this SessionQueryInfoOption.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SessionQueryInfoOption.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param database_name: The database_name of this SessionQueryInfoOption.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def client_ip(self):
        r"""Gets the client_ip of this SessionQueryInfoOption.

        **参数解释**： 客户端IP。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The client_ip of this SessionQueryInfoOption.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this SessionQueryInfoOption.

        **参数解释**： 客户端IP。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param client_ip: The client_ip of this SessionQueryInfoOption.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def user_name(self):
        r"""Gets the user_name of this SessionQueryInfoOption.

        **参数解释**： 用户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The user_name of this SessionQueryInfoOption.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SessionQueryInfoOption.

        **参数解释**： 用户名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param user_name: The user_name of this SessionQueryInfoOption.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, SessionQueryInfoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
