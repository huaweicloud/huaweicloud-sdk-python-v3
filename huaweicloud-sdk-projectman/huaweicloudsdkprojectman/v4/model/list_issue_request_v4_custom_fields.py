# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueRequestV4CustomFields:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_field': 'str',
        'value': 'str'
    }

    attribute_map = {
        'custom_field': 'custom_field',
        'value': 'value'
    }

    def __init__(self, custom_field=None, value=None):
        """ListIssueRequestV4CustomFields

        The model defined in huaweicloud sdk

        :param custom_field: 自定义属性字段
        :type custom_field: str
        :param value: 自定义属性对应的值
        :type value: str
        """
        
        

        self._custom_field = None
        self._value = None
        self.discriminator = None

        if custom_field is not None:
            self.custom_field = custom_field
        if value is not None:
            self.value = value

    @property
    def custom_field(self):
        """Gets the custom_field of this ListIssueRequestV4CustomFields.

        自定义属性字段

        :return: The custom_field of this ListIssueRequestV4CustomFields.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this ListIssueRequestV4CustomFields.

        自定义属性字段

        :param custom_field: The custom_field of this ListIssueRequestV4CustomFields.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def value(self):
        """Gets the value of this ListIssueRequestV4CustomFields.

        自定义属性对应的值

        :return: The value of this ListIssueRequestV4CustomFields.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListIssueRequestV4CustomFields.

        自定义属性对应的值

        :param value: The value of this ListIssueRequestV4CustomFields.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ListIssueRequestV4CustomFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
