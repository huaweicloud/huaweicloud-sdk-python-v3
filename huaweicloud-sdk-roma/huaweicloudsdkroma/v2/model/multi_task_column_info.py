# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskColumnInfo:

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
        'field_type': 'str',
        'field_length': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'field_type': 'field_type',
        'field_length': 'field_length'
    }

    def __init__(self, field_name=None, field_type=None, field_length=None):
        r"""MultiTaskColumnInfo

        The model defined in huaweicloud sdk

        :param field_name: 字段名
        :type field_name: str
        :param field_type: 字段类型
        :type field_type: str
        :param field_length: 字段长度
        :type field_length: str
        """
        
        

        self._field_name = None
        self._field_type = None
        self._field_length = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_type is not None:
            self.field_type = field_type
        if field_length is not None:
            self.field_length = field_length

    @property
    def field_name(self):
        r"""Gets the field_name of this MultiTaskColumnInfo.

        字段名

        :return: The field_name of this MultiTaskColumnInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this MultiTaskColumnInfo.

        字段名

        :param field_name: The field_name of this MultiTaskColumnInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def field_type(self):
        r"""Gets the field_type of this MultiTaskColumnInfo.

        字段类型

        :return: The field_type of this MultiTaskColumnInfo.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this MultiTaskColumnInfo.

        字段类型

        :param field_type: The field_type of this MultiTaskColumnInfo.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_length(self):
        r"""Gets the field_length of this MultiTaskColumnInfo.

        字段长度

        :return: The field_length of this MultiTaskColumnInfo.
        :rtype: str
        """
        return self._field_length

    @field_length.setter
    def field_length(self, field_length):
        r"""Sets the field_length of this MultiTaskColumnInfo.

        字段长度

        :param field_length: The field_length of this MultiTaskColumnInfo.
        :type field_length: str
        """
        self._field_length = field_length

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
        if not isinstance(other, MultiTaskColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
