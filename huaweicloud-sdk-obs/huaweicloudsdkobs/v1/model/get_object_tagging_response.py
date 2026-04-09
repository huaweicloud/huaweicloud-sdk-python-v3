# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetObjectTaggingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetObjectTaggingResponse"

    sensitive_list = []

    openapi_types = {
        'tagging': 'PutObjectTaggingRequestBody',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str',
        'x_obs_version_id': 'str'
    }

    attribute_map = {
        'tagging': 'Tagging',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date',
        'x_obs_version_id': 'x-obs-version-id'
    }

    def __init__(self, tagging=None, x_obs_id_2=None, x_obs_request_id=None, connection=None, content_length=None, date=None, x_obs_version_id=None):
        r"""GetObjectTaggingResponse

        The model defined in huaweicloud sdk

        :param tagging: 
        :type tagging: :class:`huaweicloudsdkobs.v1.PutObjectTaggingRequestBody`
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

        self._tagging = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self._x_obs_version_id = None
        self.discriminator = None

        if tagging is not None:
            self.tagging = tagging
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
    def tagging(self):
        r"""Gets the tagging of this GetObjectTaggingResponse.

        :return: The tagging of this GetObjectTaggingResponse.
        :rtype: :class:`huaweicloudsdkobs.v1.PutObjectTaggingRequestBody`
        """
        return self._tagging

    @tagging.setter
    def tagging(self, tagging):
        r"""Sets the tagging of this GetObjectTaggingResponse.

        :param tagging: The tagging of this GetObjectTaggingResponse.
        :type tagging: :class:`huaweicloudsdkobs.v1.PutObjectTaggingRequestBody`
        """
        self._tagging = tagging

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetObjectTaggingResponse.

        :return: The x_obs_id_2 of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetObjectTaggingResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetObjectTaggingResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetObjectTaggingResponse.

        :return: The x_obs_request_id of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetObjectTaggingResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetObjectTaggingResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def connection(self):
        r"""Gets the connection of this GetObjectTaggingResponse.

        :return: The connection of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetObjectTaggingResponse.

        :param connection: The connection of this GetObjectTaggingResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this GetObjectTaggingResponse.

        :return: The content_length of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetObjectTaggingResponse.

        :param content_length: The content_length of this GetObjectTaggingResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this GetObjectTaggingResponse.

        :return: The date of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetObjectTaggingResponse.

        :param date: The date of this GetObjectTaggingResponse.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_version_id(self):
        r"""Gets the x_obs_version_id of this GetObjectTaggingResponse.

        :return: The x_obs_version_id of this GetObjectTaggingResponse.
        :rtype: str
        """
        return self._x_obs_version_id

    @x_obs_version_id.setter
    def x_obs_version_id(self, x_obs_version_id):
        r"""Sets the x_obs_version_id of this GetObjectTaggingResponse.

        :param x_obs_version_id: The x_obs_version_id of this GetObjectTaggingResponse.
        :type x_obs_version_id: str
        """
        self._x_obs_version_id = x_obs_version_id

    def to_dict(self):
        import warnings
        warnings.warn("GetObjectTaggingResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetObjectTaggingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
