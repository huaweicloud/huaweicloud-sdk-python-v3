# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPostgresqlParamValueResponse(SdkResponse):

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
        'value': 'str',
        'restart_required': 'bool',
        'value_range': 'str',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'restart_required': 'restart_required',
        'value_range': 'value_range',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, restart_required=None, value_range=None, type=None, description=None):
        """ShowPostgresqlParamValueResponse

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param value: 参数值。
        :type value: str
        :param restart_required: 是否需要重启。 - \&quot;false\&quot;表示否 - \&quot;true\&quot;表示是
        :type restart_required: bool
        :param value_range: 参数值范围，如Integer取值0-1、Boolean取值true|false等。
        :type value_range: str
        :param type: 参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。
        :type type: str
        :param description: 参数描述。
        :type description: str
        """
        
        super(ShowPostgresqlParamValueResponse, self).__init__()

        self._name = None
        self._value = None
        self._restart_required = None
        self._value_range = None
        self._type = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if restart_required is not None:
            self.restart_required = restart_required
        if value_range is not None:
            self.value_range = value_range
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ShowPostgresqlParamValueResponse.

        参数名称。

        :return: The name of this ShowPostgresqlParamValueResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPostgresqlParamValueResponse.

        参数名称。

        :param name: The name of this ShowPostgresqlParamValueResponse.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ShowPostgresqlParamValueResponse.

        参数值。

        :return: The value of this ShowPostgresqlParamValueResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowPostgresqlParamValueResponse.

        参数值。

        :param value: The value of this ShowPostgresqlParamValueResponse.
        :type value: str
        """
        self._value = value

    @property
    def restart_required(self):
        """Gets the restart_required of this ShowPostgresqlParamValueResponse.

        是否需要重启。 - \"false\"表示否 - \"true\"表示是

        :return: The restart_required of this ShowPostgresqlParamValueResponse.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        """Sets the restart_required of this ShowPostgresqlParamValueResponse.

        是否需要重启。 - \"false\"表示否 - \"true\"表示是

        :param restart_required: The restart_required of this ShowPostgresqlParamValueResponse.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def value_range(self):
        """Gets the value_range of this ShowPostgresqlParamValueResponse.

        参数值范围，如Integer取值0-1、Boolean取值true|false等。

        :return: The value_range of this ShowPostgresqlParamValueResponse.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ShowPostgresqlParamValueResponse.

        参数值范围，如Integer取值0-1、Boolean取值true|false等。

        :param value_range: The value_range of this ShowPostgresqlParamValueResponse.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def type(self):
        """Gets the type of this ShowPostgresqlParamValueResponse.

        参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。

        :return: The type of this ShowPostgresqlParamValueResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowPostgresqlParamValueResponse.

        参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。

        :param type: The type of this ShowPostgresqlParamValueResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ShowPostgresqlParamValueResponse.

        参数描述。

        :return: The description of this ShowPostgresqlParamValueResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowPostgresqlParamValueResponse.

        参数描述。

        :param description: The description of this ShowPostgresqlParamValueResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ShowPostgresqlParamValueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
