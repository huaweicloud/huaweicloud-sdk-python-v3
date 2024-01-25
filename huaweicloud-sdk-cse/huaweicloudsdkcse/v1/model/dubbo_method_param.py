# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DubboMethodParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_key': 'str',
        'param_source': 'str',
        'param_type': 'str'
    }

    attribute_map = {
        'param_key': 'paramKey',
        'param_source': 'paramSource',
        'param_type': 'paramType'
    }

    def __init__(self, param_key=None, param_source=None, param_type=None):
        """DubboMethodParam

        The model defined in huaweicloud sdk

        :param param_key: 参数键。
        :type param_key: str
        :param param_source: 参数来源。
        :type param_source: str
        :param param_type: 参数类型。
        :type param_type: str
        """
        
        

        self._param_key = None
        self._param_source = None
        self._param_type = None
        self.discriminator = None

        if param_key is not None:
            self.param_key = param_key
        if param_source is not None:
            self.param_source = param_source
        if param_type is not None:
            self.param_type = param_type

    @property
    def param_key(self):
        """Gets the param_key of this DubboMethodParam.

        参数键。

        :return: The param_key of this DubboMethodParam.
        :rtype: str
        """
        return self._param_key

    @param_key.setter
    def param_key(self, param_key):
        """Sets the param_key of this DubboMethodParam.

        参数键。

        :param param_key: The param_key of this DubboMethodParam.
        :type param_key: str
        """
        self._param_key = param_key

    @property
    def param_source(self):
        """Gets the param_source of this DubboMethodParam.

        参数来源。

        :return: The param_source of this DubboMethodParam.
        :rtype: str
        """
        return self._param_source

    @param_source.setter
    def param_source(self, param_source):
        """Sets the param_source of this DubboMethodParam.

        参数来源。

        :param param_source: The param_source of this DubboMethodParam.
        :type param_source: str
        """
        self._param_source = param_source

    @property
    def param_type(self):
        """Gets the param_type of this DubboMethodParam.

        参数类型。

        :return: The param_type of this DubboMethodParam.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this DubboMethodParam.

        参数类型。

        :param param_type: The param_type of this DubboMethodParam.
        :type param_type: str
        """
        self._param_type = param_type

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
        if not isinstance(other, DubboMethodParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
