# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemTemplatesResponse(SdkResponse):

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
        'action_templates': 'list[ActionTemplateItem]',
        'offset': 'int',
        'is_truncated': 'bool',
        'total': 'int',
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
        'total': 'total',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, count=None, action_templates=None, offset=None, is_truncated=None, total=None, x_request_id=None, connection=None, content_length=None, date=None):
        r"""ListSystemTemplatesResponse

        The model defined in huaweicloud sdk

        :param count: 列表条目数。
        :type count: int
        :param action_templates: 模板列表信息。
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.ActionTemplateItem`]
        :param offset: 下一次查询的起始位置。 下一次查询的起始位置。
        :type offset: int
        :param is_truncated: 如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个算子。如果is_truncated为false，该字段不会返回。
        :type is_truncated: bool
        :param total: 查询到符合条件的列表总条数。
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ListSystemTemplatesResponse, self).__init__()

        self._count = None
        self._action_templates = None
        self._offset = None
        self._is_truncated = None
        self._total = None
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
        if total is not None:
            self.total = total
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
        r"""Gets the count of this ListSystemTemplatesResponse.

        列表条目数。

        :return: The count of this ListSystemTemplatesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSystemTemplatesResponse.

        列表条目数。

        :param count: The count of this ListSystemTemplatesResponse.
        :type count: int
        """
        self._count = count

    @property
    def action_templates(self):
        r"""Gets the action_templates of this ListSystemTemplatesResponse.

        模板列表信息。

        :return: The action_templates of this ListSystemTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.ActionTemplateItem`]
        """
        return self._action_templates

    @action_templates.setter
    def action_templates(self, action_templates):
        r"""Sets the action_templates of this ListSystemTemplatesResponse.

        模板列表信息。

        :param action_templates: The action_templates of this ListSystemTemplatesResponse.
        :type action_templates: list[:class:`huaweicloudsdkdwr.v3.ActionTemplateItem`]
        """
        self._action_templates = action_templates

    @property
    def offset(self):
        r"""Gets the offset of this ListSystemTemplatesResponse.

        下一次查询的起始位置。 下一次查询的起始位置。

        :return: The offset of this ListSystemTemplatesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSystemTemplatesResponse.

        下一次查询的起始位置。 下一次查询的起始位置。

        :param offset: The offset of this ListSystemTemplatesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def is_truncated(self):
        r"""Gets the is_truncated of this ListSystemTemplatesResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个算子。如果is_truncated为false，该字段不会返回。

        :return: The is_truncated of this ListSystemTemplatesResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        r"""Sets the is_truncated of this ListSystemTemplatesResponse.

        如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个算子。如果is_truncated为false，该字段不会返回。

        :param is_truncated: The is_truncated of this ListSystemTemplatesResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def total(self):
        r"""Gets the total of this ListSystemTemplatesResponse.

        查询到符合条件的列表总条数。

        :return: The total of this ListSystemTemplatesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSystemTemplatesResponse.

        查询到符合条件的列表总条数。

        :param total: The total of this ListSystemTemplatesResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSystemTemplatesResponse.

        :return: The x_request_id of this ListSystemTemplatesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSystemTemplatesResponse.

        :param x_request_id: The x_request_id of this ListSystemTemplatesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        r"""Gets the connection of this ListSystemTemplatesResponse.

        :return: The connection of this ListSystemTemplatesResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ListSystemTemplatesResponse.

        :param connection: The connection of this ListSystemTemplatesResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this ListSystemTemplatesResponse.

        :return: The content_length of this ListSystemTemplatesResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ListSystemTemplatesResponse.

        :param content_length: The content_length of this ListSystemTemplatesResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this ListSystemTemplatesResponse.

        :return: The date of this ListSystemTemplatesResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ListSystemTemplatesResponse.

        :param date: The date of this ListSystemTemplatesResponse.
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
        if not isinstance(other, ListSystemTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
