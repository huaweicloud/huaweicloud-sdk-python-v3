# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussGrantRequest:

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
        'users': 'list[GaussDBforOpenGaussUserWithPrivilege]'
    }

    attribute_map = {
        'db_name': 'db_name',
        'users': 'users'
    }

    def __init__(self, db_name=None, users=None):
        r"""GaussDBforOpenGaussGrantRequest

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。  GaussDB 模板库包括postgres， template0 ，template1。
        :type db_name: str
        :param users: 每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。
        :type users: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserWithPrivilege`]
        """
        
        

        self._db_name = None
        self._users = None
        self.discriminator = None

        self.db_name = db_name
        self.users = users

    @property
    def db_name(self):
        r"""Gets the db_name of this GaussDBforOpenGaussGrantRequest.

        数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。  GaussDB 模板库包括postgres， template0 ，template1。

        :return: The db_name of this GaussDBforOpenGaussGrantRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this GaussDBforOpenGaussGrantRequest.

        数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB 模板库重名。  GaussDB 模板库包括postgres， template0 ，template1。

        :param db_name: The db_name of this GaussDBforOpenGaussGrantRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def users(self):
        r"""Gets the users of this GaussDBforOpenGaussGrantRequest.

        每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。

        :return: The users of this GaussDBforOpenGaussGrantRequest.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserWithPrivilege`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this GaussDBforOpenGaussGrantRequest.

        每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。

        :param users: The users of this GaussDBforOpenGaussGrantRequest.
        :type users: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussUserWithPrivilege`]
        """
        self._users = users

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
        if not isinstance(other, GaussDBforOpenGaussGrantRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
