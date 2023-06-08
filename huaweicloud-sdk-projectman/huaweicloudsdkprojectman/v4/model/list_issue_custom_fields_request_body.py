# coding: utf-8

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
        'names': 'list[str]',
        'included_not_in_use': 'bool'
    }

    attribute_map = {
        'custom_fields': 'custom_fields',
        'names': 'names',
        'included_not_in_use': 'included_not_in_use'
    }

    def __init__(self, custom_fields=None, names=None, included_not_in_use=None):
        """ListIssueCustomFieldsRequestBody

        The model defined in huaweicloud sdk

        :param custom_fields: 自定义字段
        :type custom_fields: list[str]
        :param names: 自定义字段页面显示的含义
        :type names: list[str]
        :param included_not_in_use: 查询结果是否包括未使用的自定义字段，默认仅查询使用中的自定义字段，设为true时查询项目中所有自定义字段
        :type included_not_in_use: bool
        """
        
        

        self._custom_fields = None
        self._names = None
        self._included_not_in_use = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if names is not None:
            self.names = names
        if included_not_in_use is not None:
            self.included_not_in_use = included_not_in_use

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

    @property
    def included_not_in_use(self):
        """Gets the included_not_in_use of this ListIssueCustomFieldsRequestBody.

        查询结果是否包括未使用的自定义字段，默认仅查询使用中的自定义字段，设为true时查询项目中所有自定义字段

        :return: The included_not_in_use of this ListIssueCustomFieldsRequestBody.
        :rtype: bool
        """
        return self._included_not_in_use

    @included_not_in_use.setter
    def included_not_in_use(self, included_not_in_use):
        """Sets the included_not_in_use of this ListIssueCustomFieldsRequestBody.

        查询结果是否包括未使用的自定义字段，默认仅查询使用中的自定义字段，设为true时查询项目中所有自定义字段

        :param included_not_in_use: The included_not_in_use of this ListIssueCustomFieldsRequestBody.
        :type included_not_in_use: bool
        """
        self._included_not_in_use = included_not_in_use

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
