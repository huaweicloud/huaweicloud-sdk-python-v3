# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiParameter:

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
        '_in': 'str',
        'default': 'str',
        'description': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'name': 'name',
        '_in': 'in',
        'default': 'default',
        'description': 'description',
        'required': 'required'
    }

    def __init__(self, name=None, _in=None, default=None, description=None, required=None):
        """LdApiParameter

        The model defined in huaweicloud sdk

        :param name: 参数名称： - 参数位于Headers、 Parameters时，用户自行定义，支持英文、数字、点、中划线、下划线，且需要英文开头，不区分大小写。 - 参数位于Body时候，参数以application/json、application/xml、application/text为名，但实际是以请求body里的键值对作为参数名和参数值，比如请求消息样例，参数名为application/json，参数值为{\\\&quot;table\\\&quot;:\\\&quot;apic01\\\&quot;,\\\&quot;id\\\&quot;:\\\&quot;1\\\&quot;}，后端取table：apic01，id：1这两个键值对作为入参。 - 注意：定义参数不要重名，否则会覆盖掉，当Headers、Parameters重复时候，Parameters会被覆盖，当Parameters和Body里的键值对重复时候，Parameters会被覆盖。
        :type name: str
        :param _in: 该参数在调用API时候所放的位置： - Headers ：放于请求头 - Parameters ：放于请求参数 - Body：放于请求体
        :type _in: str
        :param default: 参数默认值
        :type default: str
        :param description: 参数描述  不支持&lt;，&gt;字符
        :type description: str
        :param required: 参数是否必须。true：必须，false：不必须
        :type required: bool
        """
        
        

        self._name = None
        self.__in = None
        self._default = None
        self._description = None
        self._required = None
        self.discriminator = None

        self.name = name
        self._in = _in
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required

    @property
    def name(self):
        """Gets the name of this LdApiParameter.

        参数名称： - 参数位于Headers、 Parameters时，用户自行定义，支持英文、数字、点、中划线、下划线，且需要英文开头，不区分大小写。 - 参数位于Body时候，参数以application/json、application/xml、application/text为名，但实际是以请求body里的键值对作为参数名和参数值，比如请求消息样例，参数名为application/json，参数值为{\\\"table\\\":\\\"apic01\\\",\\\"id\\\":\\\"1\\\"}，后端取table：apic01，id：1这两个键值对作为入参。 - 注意：定义参数不要重名，否则会覆盖掉，当Headers、Parameters重复时候，Parameters会被覆盖，当Parameters和Body里的键值对重复时候，Parameters会被覆盖。

        :return: The name of this LdApiParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LdApiParameter.

        参数名称： - 参数位于Headers、 Parameters时，用户自行定义，支持英文、数字、点、中划线、下划线，且需要英文开头，不区分大小写。 - 参数位于Body时候，参数以application/json、application/xml、application/text为名，但实际是以请求body里的键值对作为参数名和参数值，比如请求消息样例，参数名为application/json，参数值为{\\\"table\\\":\\\"apic01\\\",\\\"id\\\":\\\"1\\\"}，后端取table：apic01，id：1这两个键值对作为入参。 - 注意：定义参数不要重名，否则会覆盖掉，当Headers、Parameters重复时候，Parameters会被覆盖，当Parameters和Body里的键值对重复时候，Parameters会被覆盖。

        :param name: The name of this LdApiParameter.
        :type name: str
        """
        self._name = name

    @property
    def _in(self):
        """Gets the _in of this LdApiParameter.

        该参数在调用API时候所放的位置： - Headers ：放于请求头 - Parameters ：放于请求参数 - Body：放于请求体

        :return: The _in of this LdApiParameter.
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this LdApiParameter.

        该参数在调用API时候所放的位置： - Headers ：放于请求头 - Parameters ：放于请求参数 - Body：放于请求体

        :param _in: The _in of this LdApiParameter.
        :type _in: str
        """
        self.__in = _in

    @property
    def default(self):
        """Gets the default of this LdApiParameter.

        参数默认值

        :return: The default of this LdApiParameter.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this LdApiParameter.

        参数默认值

        :param default: The default of this LdApiParameter.
        :type default: str
        """
        self._default = default

    @property
    def description(self):
        """Gets the description of this LdApiParameter.

        参数描述  不支持<，>字符

        :return: The description of this LdApiParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LdApiParameter.

        参数描述  不支持<，>字符

        :param description: The description of this LdApiParameter.
        :type description: str
        """
        self._description = description

    @property
    def required(self):
        """Gets the required of this LdApiParameter.

        参数是否必须。true：必须，false：不必须

        :return: The required of this LdApiParameter.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this LdApiParameter.

        参数是否必须。true：必须，false：不必须

        :param required: The required of this LdApiParameter.
        :type required: bool
        """
        self._required = required

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
        if not isinstance(other, LdApiParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
