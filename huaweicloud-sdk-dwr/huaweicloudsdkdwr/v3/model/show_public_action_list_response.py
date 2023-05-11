# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicActionListResponse(SdkResponse):

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
        'action_templates': 'list[PublicTemplateItem]',
        'total': 'int',
        'is_truncated': 'bool',
        'offset': 'int',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'count': 'count',
        'action_templates': 'action_templates',
        'total': 'total',
        'is_truncated': 'is_truncated',
        'offset': 'offset',
        'x_request_id': 'X-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, count=None, action_templates=None, total=None, is_truncated=None, offset=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ShowPublicActionListResponse

        The model defined in huaweicloud sdk

        :param count: 列表条目数
        :type count: int
        :param action_templates: 模板列表信息
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.PublicTemplateItem`]
        :param total: 列表总条目数
        :type total: int
        :param is_truncated: 是否为分页返回
        :type is_truncated: bool
        :param offset: 下次查询的起始位置
        :type offset: int
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ShowPublicActionListResponse, self).__init__()

        self._count = None
        self._action_templates = None
        self._total = None
        self._is_truncated = None
        self._offset = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if action_templates is not None:
            self.action_templates = action_templates
        if total is not None:
            self.total = total
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if offset is not None:
            self.offset = offset
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
        """Gets the count of this ShowPublicActionListResponse.

        列表条目数

        :return: The count of this ShowPublicActionListResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowPublicActionListResponse.

        列表条目数

        :param count: The count of this ShowPublicActionListResponse.
        :type count: int
        """
        self._count = count

    @property
    def action_templates(self):
        """Gets the action_templates of this ShowPublicActionListResponse.

        模板列表信息

        :return: The action_templates of this ShowPublicActionListResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.PublicTemplateItem`]
        """
        return self._action_templates

    @action_templates.setter
    def action_templates(self, action_templates):
        """Sets the action_templates of this ShowPublicActionListResponse.

        模板列表信息

        :param action_templates: The action_templates of this ShowPublicActionListResponse.
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.PublicTemplateItem`]
        """
        self._action_templates = action_templates

    @property
    def total(self):
        """Gets the total of this ShowPublicActionListResponse.

        列表总条目数

        :return: The total of this ShowPublicActionListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowPublicActionListResponse.

        列表总条目数

        :param total: The total of this ShowPublicActionListResponse.
        :type total: int
        """
        self._total = total

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ShowPublicActionListResponse.

        是否为分页返回

        :return: The is_truncated of this ShowPublicActionListResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ShowPublicActionListResponse.

        是否为分页返回

        :param is_truncated: The is_truncated of this ShowPublicActionListResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def offset(self):
        """Gets the offset of this ShowPublicActionListResponse.

        下次查询的起始位置

        :return: The offset of this ShowPublicActionListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowPublicActionListResponse.

        下次查询的起始位置

        :param offset: The offset of this ShowPublicActionListResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowPublicActionListResponse.

        :return: The x_request_id of this ShowPublicActionListResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowPublicActionListResponse.

        :param x_request_id: The x_request_id of this ShowPublicActionListResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ShowPublicActionListResponse.

        :return: The connection of this ShowPublicActionListResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ShowPublicActionListResponse.

        :param connection: The connection of this ShowPublicActionListResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ShowPublicActionListResponse.

        :return: The content_length of this ShowPublicActionListResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ShowPublicActionListResponse.

        :param content_length: The content_length of this ShowPublicActionListResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ShowPublicActionListResponse.

        :return: The date of this ShowPublicActionListResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ShowPublicActionListResponse.

        :param date: The date of this ShowPublicActionListResponse.
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
        if not isinstance(other, ShowPublicActionListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
