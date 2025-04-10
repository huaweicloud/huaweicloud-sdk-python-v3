# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthenticationSchemeItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'description': 'str',
        'spec_uri': 'str',
        'documentation_uri': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'description': 'description',
        'spec_uri': 'specUri',
        'documentation_uri': 'documentationUri',
        'primary': 'primary'
    }

    def __init__(self, type=None, name=None, description=None, spec_uri=None, documentation_uri=None, primary=None):
        r"""AuthenticationSchemeItemDto

        The model defined in huaweicloud sdk

        :param type: 认证类型，指定鉴权的方式
        :type type: str
        :param name: 认证概要名称
        :type name: str
        :param description: 认证概要的描述信息
        :type description: str
        :param spec_uri: 规范链接
        :type spec_uri: str
        :param documentation_uri: 帮助文档链接
        :type documentation_uri: str
        :param primary: 是否为主要的认证方式
        :type primary: bool
        """
        
        

        self._type = None
        self._name = None
        self._description = None
        self._spec_uri = None
        self._documentation_uri = None
        self._primary = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec_uri is not None:
            self.spec_uri = spec_uri
        if documentation_uri is not None:
            self.documentation_uri = documentation_uri
        if primary is not None:
            self.primary = primary

    @property
    def type(self):
        r"""Gets the type of this AuthenticationSchemeItemDto.

        认证类型，指定鉴权的方式

        :return: The type of this AuthenticationSchemeItemDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AuthenticationSchemeItemDto.

        认证类型，指定鉴权的方式

        :param type: The type of this AuthenticationSchemeItemDto.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this AuthenticationSchemeItemDto.

        认证概要名称

        :return: The name of this AuthenticationSchemeItemDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AuthenticationSchemeItemDto.

        认证概要名称

        :param name: The name of this AuthenticationSchemeItemDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AuthenticationSchemeItemDto.

        认证概要的描述信息

        :return: The description of this AuthenticationSchemeItemDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AuthenticationSchemeItemDto.

        认证概要的描述信息

        :param description: The description of this AuthenticationSchemeItemDto.
        :type description: str
        """
        self._description = description

    @property
    def spec_uri(self):
        r"""Gets the spec_uri of this AuthenticationSchemeItemDto.

        规范链接

        :return: The spec_uri of this AuthenticationSchemeItemDto.
        :rtype: str
        """
        return self._spec_uri

    @spec_uri.setter
    def spec_uri(self, spec_uri):
        r"""Sets the spec_uri of this AuthenticationSchemeItemDto.

        规范链接

        :param spec_uri: The spec_uri of this AuthenticationSchemeItemDto.
        :type spec_uri: str
        """
        self._spec_uri = spec_uri

    @property
    def documentation_uri(self):
        r"""Gets the documentation_uri of this AuthenticationSchemeItemDto.

        帮助文档链接

        :return: The documentation_uri of this AuthenticationSchemeItemDto.
        :rtype: str
        """
        return self._documentation_uri

    @documentation_uri.setter
    def documentation_uri(self, documentation_uri):
        r"""Sets the documentation_uri of this AuthenticationSchemeItemDto.

        帮助文档链接

        :param documentation_uri: The documentation_uri of this AuthenticationSchemeItemDto.
        :type documentation_uri: str
        """
        self._documentation_uri = documentation_uri

    @property
    def primary(self):
        r"""Gets the primary of this AuthenticationSchemeItemDto.

        是否为主要的认证方式

        :return: The primary of this AuthenticationSchemeItemDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this AuthenticationSchemeItemDto.

        是否为主要的认证方式

        :param primary: The primary of this AuthenticationSchemeItemDto.
        :type primary: bool
        """
        self._primary = primary

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
        if not isinstance(other, AuthenticationSchemeItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
