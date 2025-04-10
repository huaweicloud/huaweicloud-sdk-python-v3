# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatGatewayOption:

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
        'spec': 'str',
        'session_conf': 'SessionConfiguration'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'session_conf': 'session_conf'
    }

    def __init__(self, name=None, description=None, spec=None, session_conf=None):
        r"""UpdateNatGatewayOption

        The model defined in huaweicloud sdk

        :param name: 公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。
        :type name: str
        :param description: 公网NAT网关的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 公网NAT网关的规格。 取值为： \&quot;1\&quot;：小型，SNAT最大连接数10000 \&quot;2\&quot;：中型，SNAT最大连接数50000 \&quot;3\&quot;：大型，SNAT最大连接数200000 \&quot;4\&quot;：超大型，SNAT最大连接数1000000 
        :type spec: str
        :param session_conf: 
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        
        

        self._name = None
        self._description = None
        self._spec = None
        self._session_conf = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec
        if session_conf is not None:
            self.session_conf = session_conf

    @property
    def name(self):
        r"""Gets the name of this UpdateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this UpdateNatGatewayOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateNatGatewayOption.

        公网NAT网关的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateNatGatewayOption.

        公网NAT网关的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this UpdateNatGatewayOption.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this UpdateNatGatewayOption.

        公网NAT网关的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :return: The spec of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this UpdateNatGatewayOption.

        公网NAT网关的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this UpdateNatGatewayOption.
        :type spec: str
        """
        self._spec = spec

    @property
    def session_conf(self):
        r"""Gets the session_conf of this UpdateNatGatewayOption.

        :return: The session_conf of this UpdateNatGatewayOption.
        :rtype: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        return self._session_conf

    @session_conf.setter
    def session_conf(self, session_conf):
        r"""Sets the session_conf of this UpdateNatGatewayOption.

        :param session_conf: The session_conf of this UpdateNatGatewayOption.
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        self._session_conf = session_conf

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
        if not isinstance(other, UpdateNatGatewayOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
