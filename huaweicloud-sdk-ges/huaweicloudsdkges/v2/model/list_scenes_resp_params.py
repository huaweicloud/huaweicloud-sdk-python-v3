# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScenesRespParams:

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
        'type': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'default_value': 'default_value'
    }

    def __init__(self, name=None, type=None, default_value=None):
        """ListScenesRespParams

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param type: 参数类型。取值范围[\&quot;string\&quot;,\&quot;int\&quot;]，目前仅支持\&quot;string\&quot;
        :type type: str
        :param default_value: 取值范围为空，或参数默认值，当为空是表示客户使用时必须传入此参数
        :type default_value: str
        """
        
        

        self._name = None
        self._type = None
        self._default_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if default_value is not None:
            self.default_value = default_value

    @property
    def name(self):
        """Gets the name of this ListScenesRespParams.

        参数名称。

        :return: The name of this ListScenesRespParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListScenesRespParams.

        参数名称。

        :param name: The name of this ListScenesRespParams.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ListScenesRespParams.

        参数类型。取值范围[\"string\",\"int\"]，目前仅支持\"string\"

        :return: The type of this ListScenesRespParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListScenesRespParams.

        参数类型。取值范围[\"string\",\"int\"]，目前仅支持\"string\"

        :param type: The type of this ListScenesRespParams.
        :type type: str
        """
        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this ListScenesRespParams.

        取值范围为空，或参数默认值，当为空是表示客户使用时必须传入此参数

        :return: The default_value of this ListScenesRespParams.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ListScenesRespParams.

        取值范围为空，或参数默认值，当为空是表示客户使用时必须传入此参数

        :param default_value: The default_value of this ListScenesRespParams.
        :type default_value: str
        """
        self._default_value = default_value

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
        if not isinstance(other, ListScenesRespParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
