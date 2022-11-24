# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSystemTemplateDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provided_actions': 'list[ProvidedAction]',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'provided_actions': 'provided_actions',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, provided_actions=None, x_request_id=None, connection=None, content_length=None, date=None):
        """ShowSystemTemplateDetailResponse

        The model defined in huaweicloud sdk

        :param provided_actions: 
        :type provided_actions: list[:class:`huaweicloudsdkdwr.v3.ProvidedAction`]
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ShowSystemTemplateDetailResponse, self).__init__()

        self._provided_actions = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if provided_actions is not None:
            self.provided_actions = provided_actions
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def provided_actions(self):
        """Gets the provided_actions of this ShowSystemTemplateDetailResponse.

        :return: The provided_actions of this ShowSystemTemplateDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.ProvidedAction`]
        """
        return self._provided_actions

    @provided_actions.setter
    def provided_actions(self, provided_actions):
        """Sets the provided_actions of this ShowSystemTemplateDetailResponse.

        :param provided_actions: The provided_actions of this ShowSystemTemplateDetailResponse.
        :type provided_actions: list[:class:`huaweicloudsdkdwr.v3.ProvidedAction`]
        """
        self._provided_actions = provided_actions

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowSystemTemplateDetailResponse.

        :return: The x_request_id of this ShowSystemTemplateDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowSystemTemplateDetailResponse.

        :param x_request_id: The x_request_id of this ShowSystemTemplateDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this ShowSystemTemplateDetailResponse.

        :return: The connection of this ShowSystemTemplateDetailResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ShowSystemTemplateDetailResponse.

        :param connection: The connection of this ShowSystemTemplateDetailResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this ShowSystemTemplateDetailResponse.

        :return: The content_length of this ShowSystemTemplateDetailResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ShowSystemTemplateDetailResponse.

        :param content_length: The content_length of this ShowSystemTemplateDetailResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this ShowSystemTemplateDetailResponse.

        :return: The date of this ShowSystemTemplateDetailResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ShowSystemTemplateDetailResponse.

        :param date: The date of this ShowSystemTemplateDetailResponse.
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
        if not isinstance(other, ShowSystemTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
