# coding: utf-8

import pprint
import re

import six





class RolePolicy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'depends': 'list[PolicyDepends]',
        'statement': 'list[PolicyStatement]',
        'version': 'str'
    }

    attribute_map = {
        'depends': 'Depends',
        'statement': 'Statement',
        'version': 'Version'
    }

    def __init__(self, depends=None, statement=None, version=None):
        """RolePolicy - a model defined in huaweicloud sdk"""
        
        

        self._depends = None
        self._statement = None
        self._version = None
        self.discriminator = None

        if depends is not None:
            self.depends = depends
        self.statement = statement
        self.version = version

    @property
    def depends(self):
        """Gets the depends of this RolePolicy.

        该权限所依赖的权限。

        :return: The depends of this RolePolicy.
        :rtype: list[PolicyDepends]
        """
        return self._depends

    @depends.setter
    def depends(self, depends):
        """Sets the depends of this RolePolicy.

        该权限所依赖的权限。

        :param depends: The depends of this RolePolicy.
        :type: list[PolicyDepends]
        """
        self._depends = depends

    @property
    def statement(self):
        """Gets the statement of this RolePolicy.

        授权语句，描述权限的具体内容。

        :return: The statement of this RolePolicy.
        :rtype: list[PolicyStatement]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this RolePolicy.

        授权语句，描述权限的具体内容。

        :param statement: The statement of this RolePolicy.
        :type: list[PolicyStatement]
        """
        self._statement = statement

    @property
    def version(self):
        """Gets the version of this RolePolicy.

        权限版本号。   > - 1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。   > - 1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :return: The version of this RolePolicy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RolePolicy.

        权限版本号。   > - 1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。   > - 1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :param version: The version of this RolePolicy.
        :type: str
        """
        self._version = version

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RolePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
