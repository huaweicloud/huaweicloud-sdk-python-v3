# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'statement': 'list[Statement]'
    }

    attribute_map = {
        'version': 'version',
        'statement': 'statement'
    }

    def __init__(self, version=None, statement=None):
        r"""Policy

        The model defined in huaweicloud sdk

        :param version: 权限版本号。  1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。  1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。
        :type version: str
        :param statement: 授权语句，描述自定义策略的具体内容。
        :type statement: list[:class:`huaweicloudsdkdwr.v3.Statement`]
        """
        
        

        self._version = None
        self._statement = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if statement is not None:
            self.statement = statement

    @property
    def version(self):
        r"""Gets the version of this Policy.

        权限版本号。  1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。  1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :return: The version of this Policy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Policy.

        权限版本号。  1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。  1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :param version: The version of this Policy.
        :type version: str
        """
        self._version = version

    @property
    def statement(self):
        r"""Gets the statement of this Policy.

        授权语句，描述自定义策略的具体内容。

        :return: The statement of this Policy.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Statement`]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this Policy.

        授权语句，描述自定义策略的具体内容。

        :param statement: The statement of this Policy.
        :type statement: list[:class:`huaweicloudsdkdwr.v3.Statement`]
        """
        self._statement = statement

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
