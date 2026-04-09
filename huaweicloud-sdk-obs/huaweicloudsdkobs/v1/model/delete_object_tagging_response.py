# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectTaggingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObjectTaggingResponse"

    sensitive_list = []

    openapi_types = {
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str',
        'x_obs_version_id': 'str'
    }

    attribute_map = {
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date',
        'x_obs_version_id': 'x-obs-version-id'
    }

    def __init__(self, x_obs_id_2=None, x_obs_request_id=None, connection=None, content_length=None, date=None, x_obs_version_id=None):
        r"""DeleteObjectTaggingResponse

        The model defined in huaweicloud sdk

        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        :param x_obs_version_id: 
        :type x_obs_version_id: str
        """
        
        super().__init__()

        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self._x_obs_version_id = None
        self.discriminator = None

        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date
        if x_obs_version_id is not None:
            self.x_obs_version_id = x_obs_version_id

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this DeleteObjectTaggingResponse.

        :return: The x_obs_id_2 of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this DeleteObjectTaggingResponse.

        :param x_obs_id_2: The x_obs_id_2 of this DeleteObjectTaggingResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this DeleteObjectTaggingResponse.

        :return: The x_obs_request_id of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this DeleteObjectTaggingResponse.

        :param x_obs_request_id: The x_obs_request_id of this DeleteObjectTaggingResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def connection(self):
        r"""Gets the connection of this DeleteObjectTaggingResponse.

        :return: The connection of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this DeleteObjectTaggingResponse.

        :param connection: The connection of this DeleteObjectTaggingResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this DeleteObjectTaggingResponse.

        :return: The content_length of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this DeleteObjectTaggingResponse.

        :param content_length: The content_length of this DeleteObjectTaggingResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this DeleteObjectTaggingResponse.

        :return: The date of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this DeleteObjectTaggingResponse.

        :param date: The date of this DeleteObjectTaggingResponse.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_version_id(self):
        r"""Gets the x_obs_version_id of this DeleteObjectTaggingResponse.

        :return: The x_obs_version_id of this DeleteObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_version_id

    @x_obs_version_id.setter
    def x_obs_version_id(self, x_obs_version_id):
        r"""Sets the x_obs_version_id of this DeleteObjectTaggingResponse.

        :param x_obs_version_id: The x_obs_version_id of this DeleteObjectTaggingResponse.
        :type x_obs_version_id: str
        """
        self._x_obs_version_id = x_obs_version_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteObjectTaggingResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteObjectTaggingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
