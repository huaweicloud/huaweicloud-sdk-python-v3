# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObjectsResponse"

    sensitive_list = []

    openapi_types = {
        'encoding_type': 'str',
        'deleted': 'list[DeleteResultDeleted]',
        'error': 'list[DeleteResultError]',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'encoding_type': 'EncodingType',
        'deleted': 'Deleted',
        'error': 'Error',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, encoding_type=None, deleted=None, error=None, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, connection=None, content_length=None, date=None):
        r"""DeleteObjectsResponse

        The model defined in huaweicloud sdk

        :param encoding_type: Encodes the **key** in the response based on the specified type. If **encoding-type** is specified in the request, the **Key** in the response is encoded.
        :type encoding_type: str
        :param deleted: 
        :type deleted: list[:class:`huaweicloudsdkobs.v1.DeleteResultDeleted`]
        :param error: 
        :type error: list[:class:`huaweicloudsdkobs.v1.DeleteResultError`]
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param e_tag: 
        :type e_tag: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(DeleteObjectsResponse, self).__init__()

        self._encoding_type = None
        self._deleted = None
        self._error = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if encoding_type is not None:
            self.encoding_type = encoding_type
        if deleted is not None:
            self.deleted = deleted
        if error is not None:
            self.error = error
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if e_tag is not None:
            self.e_tag = e_tag
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def encoding_type(self):
        r"""Gets the encoding_type of this DeleteObjectsResponse.

        Encodes the **key** in the response based on the specified type. If **encoding-type** is specified in the request, the **Key** in the response is encoded.

        :return: The encoding_type of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        r"""Sets the encoding_type of this DeleteObjectsResponse.

        Encodes the **key** in the response based on the specified type. If **encoding-type** is specified in the request, the **Key** in the response is encoded.

        :param encoding_type: The encoding_type of this DeleteObjectsResponse.
        :type encoding_type: str
        """
        self._encoding_type = encoding_type

    @property
    def deleted(self):
        r"""Gets the deleted of this DeleteObjectsResponse.

        :return: The deleted of this DeleteObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkobs.v1.DeleteResultDeleted`]
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this DeleteObjectsResponse.

        :param deleted: The deleted of this DeleteObjectsResponse.
        :type deleted: list[:class:`huaweicloudsdkobs.v1.DeleteResultDeleted`]
        """
        self._deleted = deleted

    @property
    def error(self):
        r"""Gets the error of this DeleteObjectsResponse.

        :return: The error of this DeleteObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkobs.v1.DeleteResultError`]
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this DeleteObjectsResponse.

        :param error: The error of this DeleteObjectsResponse.
        :type error: list[:class:`huaweicloudsdkobs.v1.DeleteResultError`]
        """
        self._error = error

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this DeleteObjectsResponse.

        :return: The x_obs_id_2 of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this DeleteObjectsResponse.

        :param x_obs_id_2: The x_obs_id_2 of this DeleteObjectsResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this DeleteObjectsResponse.

        :return: The x_obs_request_id of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this DeleteObjectsResponse.

        :param x_obs_request_id: The x_obs_request_id of this DeleteObjectsResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this DeleteObjectsResponse.

        :return: The e_tag of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this DeleteObjectsResponse.

        :param e_tag: The e_tag of this DeleteObjectsResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def connection(self):
        r"""Gets the connection of this DeleteObjectsResponse.

        :return: The connection of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this DeleteObjectsResponse.

        :param connection: The connection of this DeleteObjectsResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this DeleteObjectsResponse.

        :return: The content_length of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this DeleteObjectsResponse.

        :param content_length: The content_length of this DeleteObjectsResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this DeleteObjectsResponse.

        :return: The date of this DeleteObjectsResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this DeleteObjectsResponse.

        :param date: The date of this DeleteObjectsResponse.
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
        if not isinstance(other, DeleteObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
