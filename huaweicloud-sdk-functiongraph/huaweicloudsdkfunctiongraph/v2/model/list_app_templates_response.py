# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[ListAppTemplatesResult]',
        'next_marker': 'int',
        'count': 'int'
    }

    attribute_map = {
        'templates': 'templates',
        'next_marker': 'next_marker',
        'count': 'count'
    }

    def __init__(self, templates=None, next_marker=None, count=None):
        r"""ListAppTemplatesResponse

        The model defined in huaweicloud sdk

        :param templates: 函数应用程序模板列表
        :type templates: list[:class:`huaweicloudsdkfunctiongraph.v2.ListAppTemplatesResult`]
        :param next_marker: 下次读取位置
        :type next_marker: int
        :param count: 应用程序模板总数
        :type count: int
        """
        
        super(ListAppTemplatesResponse, self).__init__()

        self._templates = None
        self._next_marker = None
        self._count = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if next_marker is not None:
            self.next_marker = next_marker
        if count is not None:
            self.count = count

    @property
    def templates(self):
        r"""Gets the templates of this ListAppTemplatesResponse.

        函数应用程序模板列表

        :return: The templates of this ListAppTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ListAppTemplatesResult`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListAppTemplatesResponse.

        函数应用程序模板列表

        :param templates: The templates of this ListAppTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkfunctiongraph.v2.ListAppTemplatesResult`]
        """
        self._templates = templates

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAppTemplatesResponse.

        下次读取位置

        :return: The next_marker of this ListAppTemplatesResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAppTemplatesResponse.

        下次读取位置

        :param next_marker: The next_marker of this ListAppTemplatesResponse.
        :type next_marker: int
        """
        self._next_marker = next_marker

    @property
    def count(self):
        r"""Gets the count of this ListAppTemplatesResponse.

        应用程序模板总数

        :return: The count of this ListAppTemplatesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAppTemplatesResponse.

        应用程序模板总数

        :param count: The count of this ListAppTemplatesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAppTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
