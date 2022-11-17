# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotebookToolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'tools': 'list[NotebookToolDto]'
    }

    attribute_map = {
        'count': 'count',
        'tools': 'tools'
    }

    def __init__(self, count=None, tools=None):
        """ListNotebookToolResponse

        The model defined in huaweicloud sdk

        :param count: 总个数
        :type count: int
        :param tools: tool详情列表
        :type tools: list[:class:`huaweicloudsdkeihealth.v1.NotebookToolDto`]
        """
        
        super(ListNotebookToolResponse, self).__init__()

        self._count = None
        self._tools = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if tools is not None:
            self.tools = tools

    @property
    def count(self):
        """Gets the count of this ListNotebookToolResponse.

        总个数

        :return: The count of this ListNotebookToolResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListNotebookToolResponse.

        总个数

        :param count: The count of this ListNotebookToolResponse.
        :type count: int
        """
        self._count = count

    @property
    def tools(self):
        """Gets the tools of this ListNotebookToolResponse.

        tool详情列表

        :return: The tools of this ListNotebookToolResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NotebookToolDto`]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this ListNotebookToolResponse.

        tool详情列表

        :param tools: The tools of this ListNotebookToolResponse.
        :type tools: list[:class:`huaweicloudsdkeihealth.v1.NotebookToolDto`]
        """
        self._tools = tools

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
        if not isinstance(other, ListNotebookToolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
