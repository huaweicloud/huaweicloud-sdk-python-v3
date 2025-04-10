# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseUserComment:

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
        'host': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'comment': 'comment'
    }

    def __init__(self, name=None, host=None, comment=None):
        r"""UpdateDatabaseUserComment

        The model defined in huaweicloud sdk

        :param name: 数据库用户名。
        :type name: str
        :param host: 主机地址。
        :type host: str
        :param comment: 数据库用户备注,长度不能超过512个字符，不能包含回车和特殊字符!&lt;\&quot;&#x3D;&#39;&gt;&amp;。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。
        :type comment: str
        """
        
        

        self._name = None
        self._host = None
        self._comment = None
        self.discriminator = None

        self.name = name
        self.host = host
        self.comment = comment

    @property
    def name(self):
        r"""Gets the name of this UpdateDatabaseUserComment.

        数据库用户名。

        :return: The name of this UpdateDatabaseUserComment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateDatabaseUserComment.

        数据库用户名。

        :param name: The name of this UpdateDatabaseUserComment.
        :type name: str
        """
        self._name = name

    @property
    def host(self):
        r"""Gets the host of this UpdateDatabaseUserComment.

        主机地址。

        :return: The host of this UpdateDatabaseUserComment.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this UpdateDatabaseUserComment.

        主机地址。

        :param host: The host of this UpdateDatabaseUserComment.
        :type host: str
        """
        self._host = host

    @property
    def comment(self):
        r"""Gets the comment of this UpdateDatabaseUserComment.

        数据库用户备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。

        :return: The comment of this UpdateDatabaseUserComment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this UpdateDatabaseUserComment.

        数据库用户备注,长度不能超过512个字符，不能包含回车和特殊字符!<\"='>&。  该字段只针对新版本的实例生效，必须大于等于指定的内核版本-2.0.13.0，如果不符合内核版本要求，参考升级内核版本升级至最新。

        :param comment: The comment of this UpdateDatabaseUserComment.
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
        if not isinstance(other, UpdateDatabaseUserComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
