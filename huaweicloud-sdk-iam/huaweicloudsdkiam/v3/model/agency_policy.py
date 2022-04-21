# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyPolicy:

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
        'statement': 'list[AgencyPolicyStatement]'
    }

    attribute_map = {
        'version': 'Version',
        'statement': 'Statement'
    }

    def __init__(self, version=None, statement=None):
        """AgencyPolicy

        The model defined in huaweicloud sdk

        :param version: 权限版本号，创建自定义策略时，该字段值填为“1.1”。 &gt; - 1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。 &gt; - 1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。
        :type version: str
        :param statement: 授权语句，描述自定义策略的具体内容，不超过8个。
        :type statement: list[:class:`huaweicloudsdkiam.v3.AgencyPolicyStatement`]
        """
        
        

        self._version = None
        self._statement = None
        self.discriminator = None

        self.version = version
        self.statement = statement

    @property
    def version(self):
        """Gets the version of this AgencyPolicy.

        权限版本号，创建自定义策略时，该字段值填为“1.1”。 > - 1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。 > - 1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :return: The version of this AgencyPolicy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AgencyPolicy.

        权限版本号，创建自定义策略时，该字段值填为“1.1”。 > - 1.0：系统预置的角色。以服务为粒度，提供有限的服务相关角色用于授权。 > - 1.1：策略。IAM最新提供的一种细粒度授权的能力，可以精确到具体服务的操作、资源以及请求条件等。

        :param version: The version of this AgencyPolicy.
        :type version: str
        """
        self._version = version

    @property
    def statement(self):
        """Gets the statement of this AgencyPolicy.

        授权语句，描述自定义策略的具体内容，不超过8个。

        :return: The statement of this AgencyPolicy.
        :rtype: list[:class:`huaweicloudsdkiam.v3.AgencyPolicyStatement`]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this AgencyPolicy.

        授权语句，描述自定义策略的具体内容，不超过8个。

        :param statement: The statement of this AgencyPolicy.
        :type statement: list[:class:`huaweicloudsdkiam.v3.AgencyPolicyStatement`]
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
        if not isinstance(other, AgencyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
