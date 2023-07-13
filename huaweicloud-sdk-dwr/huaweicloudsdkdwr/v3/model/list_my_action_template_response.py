# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMyActionTemplateResponse(SdkResponse):

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
        'action_templates': 'list[ThirdActionTemplateItem]',
        'offset': 'int',
        'is_truncated': 'bool',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'count': 'count',
        'action_templates': 'action_templates',
        'offset': 'offset',
        'is_truncated': 'is_truncated',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, count=None, action_templates=None, offset=None, is_truncated=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ListMyActionTemplateResponse

        The model defined in huaweicloud sdk

        :param count: 列表条目数
        :type count: int
        :param action_templates: 模板列表信息
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.ThirdActionTemplateItem`]
        :param offset: 下一次查询的起始位置。
        :type offset: int
        :param is_truncated: 表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。
        :type is_truncated: bool
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ListMyActionTemplateResponse, self).__init__()

        self._count = None
        self._action_templates = None
        self._offset = None
        self._is_truncated = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if action_templates is not None:
            self.action_templates = action_templates
        if offset is not None:
            self.offset = offset
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def count(self):
        """Gets the count of this ListMyActionTemplateResponse.

        列表条目数

        :return: The count of this ListMyActionTemplateResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListMyActionTemplateResponse.

        列表条目数

        :param count: The count of this ListMyActionTemplateResponse.
        :type count: int
        """
        self._count = count

    @property
    def action_templates(self):
        """Gets the action_templates of this ListMyActionTemplateResponse.

        模板列表信息

        :return: The action_templates of this ListMyActionTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.ThirdActionTemplateItem`]
        """
        return self._action_templates

    @action_templates.setter
    def action_templates(self, action_templates):
        """Sets the action_templates of this ListMyActionTemplateResponse.

        模板列表信息

        :param action_templates: The action_templates of this ListMyActionTemplateResponse.
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.ThirdActionTemplateItem`]
        """
        self._action_templates = action_templates

    @property
    def offset(self):
        """Gets the offset of this ListMyActionTemplateResponse.

        下一次查询的起始位置。

        :return: The offset of this ListMyActionTemplateResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMyActionTemplateResponse.

        下一次查询的起始位置。

        :param offset: The offset of this ListMyActionTemplateResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ListMyActionTemplateResponse.

        表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。

        :return: The is_truncated of this ListMyActionTemplateResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ListMyActionTemplateResponse.

        表明是否本次返回的结果列表被截断。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果。

        :param is_truncated: The is_truncated of this ListMyActionTemplateResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListMyActionTemplateResponse.

        :return: The x_request_id of this ListMyActionTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListMyActionTemplateResponse.

        :param x_request_id: The x_request_id of this ListMyActionTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ListMyActionTemplateResponse.

        :return: The connection of this ListMyActionTemplateResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ListMyActionTemplateResponse.

        :param connection: The connection of this ListMyActionTemplateResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ListMyActionTemplateResponse.

        :return: The content_length of this ListMyActionTemplateResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ListMyActionTemplateResponse.

        :param content_length: The content_length of this ListMyActionTemplateResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ListMyActionTemplateResponse.

        :return: The date of this ListMyActionTemplateResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListMyActionTemplateResponse.

        :param date: The date of this ListMyActionTemplateResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ListMyActionTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
