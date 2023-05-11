# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMyActionTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'created_at': 'str',
        'version': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'created_at': 'created_at',
        'version': 'version',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, template_name=None, created_at=None, version=None, x_request_id=None, connection=None, content_length=None, date=None):
        """UpdateMyActionTemplateResponse

        The model defined in huaweicloud sdk

        :param template_name: 算子模板名称。
        :type template_name: str
        :param created_at: 算子模板创建的时间。
        :type created_at: str
        :param version: 版本号。
        :type version: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(UpdateMyActionTemplateResponse, self).__init__()

        self._template_name = None
        self._created_at = None
        self._version = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if created_at is not None:
            self.created_at = created_at
        if version is not None:
            self.version = version
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def template_name(self):
        """Gets the template_name of this UpdateMyActionTemplateResponse.

        算子模板名称。

        :return: The template_name of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this UpdateMyActionTemplateResponse.

        算子模板名称。

        :param template_name: The template_name of this UpdateMyActionTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def created_at(self):
        """Gets the created_at of this UpdateMyActionTemplateResponse.

        算子模板创建的时间。

        :return: The created_at of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateMyActionTemplateResponse.

        算子模板创建的时间。

        :param created_at: The created_at of this UpdateMyActionTemplateResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def version(self):
        """Gets the version of this UpdateMyActionTemplateResponse.

        版本号。

        :return: The version of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateMyActionTemplateResponse.

        版本号。

        :param version: The version of this UpdateMyActionTemplateResponse.
        :type version: str
        """
        self._version = version

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateMyActionTemplateResponse.

        :return: The x_request_id of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateMyActionTemplateResponse.

        :param x_request_id: The x_request_id of this UpdateMyActionTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this UpdateMyActionTemplateResponse.

        :return: The connection of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this UpdateMyActionTemplateResponse.

        :param connection: The connection of this UpdateMyActionTemplateResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this UpdateMyActionTemplateResponse.

        :return: The content_length of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this UpdateMyActionTemplateResponse.

        :param content_length: The content_length of this UpdateMyActionTemplateResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this UpdateMyActionTemplateResponse.

        :return: The date of this UpdateMyActionTemplateResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this UpdateMyActionTemplateResponse.

        :param date: The date of this UpdateMyActionTemplateResponse.
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
        if not isinstance(other, UpdateMyActionTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
