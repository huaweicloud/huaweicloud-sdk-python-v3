# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateNatOption:

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
        'description': 'str',
        'spec': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'spec': 'spec'
    }

    def __init__(self, name=None, description=None, spec=None):
        r"""UpdatePrivateNatOption

        The model defined in huaweicloud sdk

        :param name: 私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。
        :type name: str
        :param description: 私网NAT网关的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 私网NAT网关实例的规格。 取值为： \&quot;Small\&quot;：小型 \&quot;Medium\&quot;：中型 \&quot;Large\&quot;：大型 \&quot;Extra-large\&quot;：超大型
        :type spec: str
        """
        
        

        self._name = None
        self._description = None
        self._spec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec

    @property
    def name(self):
        r"""Gets the name of this UpdatePrivateNatOption.

        私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this UpdatePrivateNatOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdatePrivateNatOption.

        私网NAT网关实例的名字。 私网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this UpdatePrivateNatOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdatePrivateNatOption.

        私网NAT网关的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this UpdatePrivateNatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePrivateNatOption.

        私网NAT网关的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this UpdatePrivateNatOption.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this UpdatePrivateNatOption.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :return: The spec of this UpdatePrivateNatOption.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this UpdatePrivateNatOption.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :param spec: The spec of this UpdatePrivateNatOption.
        :type spec: str
        """
        self._spec = spec

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
        if not isinstance(other, UpdatePrivateNatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
