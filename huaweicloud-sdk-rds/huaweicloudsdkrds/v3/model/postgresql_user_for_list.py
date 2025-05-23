# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlUserForList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'attributes': 'object',
        'memberof': 'list[str]',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'attributes': 'attributes',
        'memberof': 'memberof',
        'comment': 'comment'
    }

    def __init__(self, name=None, attributes=None, memberof=None, comment=None):
        r"""PostgresqlUserForList

        The model defined in huaweicloud sdk

        :param name: 帐号名。
        :type name: str
        :param attributes: 用户的权限属性。
        :type attributes: object
        :param memberof: 用户的默认权限。
        :type memberof: list[str]
        :param comment: 数据库用户备注。
        :type comment: str
        """
        
        

        self._name = None
        self._attributes = None
        self._memberof = None
        self._comment = None
        self.discriminator = None

        self.name = name
        if attributes is not None:
            self.attributes = attributes
        if memberof is not None:
            self.memberof = memberof
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        r"""Gets the name of this PostgresqlUserForList.

        帐号名。

        :return: The name of this PostgresqlUserForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PostgresqlUserForList.

        帐号名。

        :param name: The name of this PostgresqlUserForList.
        :type name: str
        """
        self._name = name

    @property
    def attributes(self):
        r"""Gets the attributes of this PostgresqlUserForList.

        用户的权限属性。

        :return: The attributes of this PostgresqlUserForList.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this PostgresqlUserForList.

        用户的权限属性。

        :param attributes: The attributes of this PostgresqlUserForList.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def memberof(self):
        r"""Gets the memberof of this PostgresqlUserForList.

        用户的默认权限。

        :return: The memberof of this PostgresqlUserForList.
        :rtype: list[str]
        """
        return self._memberof

    @memberof.setter
    def memberof(self, memberof):
        r"""Sets the memberof of this PostgresqlUserForList.

        用户的默认权限。

        :param memberof: The memberof of this PostgresqlUserForList.
        :type memberof: list[str]
        """
        self._memberof = memberof

    @property
    def comment(self):
        r"""Gets the comment of this PostgresqlUserForList.

        数据库用户备注。

        :return: The comment of this PostgresqlUserForList.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this PostgresqlUserForList.

        数据库用户备注。

        :param comment: The comment of this PostgresqlUserForList.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, PostgresqlUserForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
