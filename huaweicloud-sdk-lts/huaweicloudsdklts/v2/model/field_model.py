# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'is_analysis': 'bool'
    }

    attribute_map = {
        'field_name': 'field_name',
        'is_analysis': 'is_analysis'
    }

    def __init__(self, field_name=None, is_analysis=None):
        """FieldModel

        The model defined in huaweicloud sdk

        :param field_name: 字段名称
        :type field_name: str
        :param is_analysis: 是否开启快速分析。
        :type is_analysis: bool
        """
        
        

        self._field_name = None
        self._is_analysis = None
        self.discriminator = None

        self.field_name = field_name
        if is_analysis is not None:
            self.is_analysis = is_analysis

    @property
    def field_name(self):
        """Gets the field_name of this FieldModel.

        字段名称

        :return: The field_name of this FieldModel.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this FieldModel.

        字段名称

        :param field_name: The field_name of this FieldModel.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def is_analysis(self):
        """Gets the is_analysis of this FieldModel.

        是否开启快速分析。

        :return: The is_analysis of this FieldModel.
        :rtype: bool
        """
        return self._is_analysis

    @is_analysis.setter
    def is_analysis(self, is_analysis):
        """Sets the is_analysis of this FieldModel.

        是否开启快速分析。

        :param is_analysis: The is_analysis of this FieldModel.
        :type is_analysis: bool
        """
        self._is_analysis = is_analysis

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
        if not isinstance(other, FieldModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
