# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParamGroupParameterDifferences:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameter_name': 'str',
        'source_value': 'str',
        'target_value': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'source_value': 'source_value',
        'target_value': 'target_value'
    }

    def __init__(self, parameter_name=None, source_value=None, target_value=None):
        """ParamGroupParameterDifferences

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称。
        :type parameter_name: str
        :param source_value: 源参数模板中的参数值。
        :type source_value: str
        :param target_value: 目标参数模板中的参数值。
        :type target_value: str
        """
        
        

        self._parameter_name = None
        self._source_value = None
        self._target_value = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if source_value is not None:
            self.source_value = source_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def parameter_name(self):
        """Gets the parameter_name of this ParamGroupParameterDifferences.

        参数名称。

        :return: The parameter_name of this ParamGroupParameterDifferences.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this ParamGroupParameterDifferences.

        参数名称。

        :param parameter_name: The parameter_name of this ParamGroupParameterDifferences.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def source_value(self):
        """Gets the source_value of this ParamGroupParameterDifferences.

        源参数模板中的参数值。

        :return: The source_value of this ParamGroupParameterDifferences.
        :rtype: str
        """
        return self._source_value

    @source_value.setter
    def source_value(self, source_value):
        """Sets the source_value of this ParamGroupParameterDifferences.

        源参数模板中的参数值。

        :param source_value: The source_value of this ParamGroupParameterDifferences.
        :type source_value: str
        """
        self._source_value = source_value

    @property
    def target_value(self):
        """Gets the target_value of this ParamGroupParameterDifferences.

        目标参数模板中的参数值。

        :return: The target_value of this ParamGroupParameterDifferences.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this ParamGroupParameterDifferences.

        目标参数模板中的参数值。

        :param target_value: The target_value of this ParamGroupParameterDifferences.
        :type target_value: str
        """
        self._target_value = target_value

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
        if not isinstance(other, ParamGroupParameterDifferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
