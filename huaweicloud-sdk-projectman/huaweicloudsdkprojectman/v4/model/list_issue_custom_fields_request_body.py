# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueCustomFieldsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_fields': 'list[str]',
        'names': 'list[str]'
    }

    attribute_map = {
        'custom_fields': 'custom_fields',
        'names': 'names'
    }

    def __init__(self, custom_fields=None, names=None):
        """ListIssueCustomFieldsRequestBody

        The model defined in huaweicloud sdk

        :param custom_fields: 自定义字段
        :type custom_fields: list[str]
        :param names: 自定义字段页面显示的含义
        :type names: list[str]
        """
        
        

        self._custom_fields = None
        self._names = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if names is not None:
            self.names = names

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ListIssueCustomFieldsRequestBody.

        自定义字段

        :return: The custom_fields of this ListIssueCustomFieldsRequestBody.
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ListIssueCustomFieldsRequestBody.

        自定义字段

        :param custom_fields: The custom_fields of this ListIssueCustomFieldsRequestBody.
        :type custom_fields: list[str]
        """
        self._custom_fields = custom_fields

    @property
    def names(self):
        """Gets the names of this ListIssueCustomFieldsRequestBody.

        自定义字段页面显示的含义

        :return: The names of this ListIssueCustomFieldsRequestBody.
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this ListIssueCustomFieldsRequestBody.

        自定义字段页面显示的含义

        :param names: The names of this ListIssueCustomFieldsRequestBody.
        :type names: list[str]
        """
        self._names = names

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
        if not isinstance(other, ListIssueCustomFieldsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
