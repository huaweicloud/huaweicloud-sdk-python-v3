# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_templates': 'list[ShowFunctionTemplateResponseBody]',
        'next_marker': 'int'
    }

    attribute_map = {
        'func_templates': 'func_templates',
        'next_marker': 'next_marker'
    }

    def __init__(self, func_templates=None, next_marker=None):
        """ListFunctionTemplateResponse

        The model defined in huaweicloud sdk

        :param func_templates: 函数模板列表
        :type func_templates: list[:class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTemplateResponseBody`]
        :param next_marker: 函数下次记录读取位置。
        :type next_marker: int
        """
        
        super(ListFunctionTemplateResponse, self).__init__()

        self._func_templates = None
        self._next_marker = None
        self.discriminator = None

        if func_templates is not None:
            self.func_templates = func_templates
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def func_templates(self):
        """Gets the func_templates of this ListFunctionTemplateResponse.

        函数模板列表

        :return: The func_templates of this ListFunctionTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTemplateResponseBody`]
        """
        return self._func_templates

    @func_templates.setter
    def func_templates(self, func_templates):
        """Sets the func_templates of this ListFunctionTemplateResponse.

        函数模板列表

        :param func_templates: The func_templates of this ListFunctionTemplateResponse.
        :type func_templates: list[:class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTemplateResponseBody`]
        """
        self._func_templates = func_templates

    @property
    def next_marker(self):
        """Gets the next_marker of this ListFunctionTemplateResponse.

        函数下次记录读取位置。

        :return: The next_marker of this ListFunctionTemplateResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListFunctionTemplateResponse.

        函数下次记录读取位置。

        :param next_marker: The next_marker of this ListFunctionTemplateResponse.
        :type next_marker: int
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListFunctionTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
