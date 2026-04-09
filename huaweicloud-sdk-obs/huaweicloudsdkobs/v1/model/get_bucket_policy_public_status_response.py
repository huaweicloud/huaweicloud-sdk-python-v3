# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketPolicyPublicStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketPolicyPublicStatusResponse"

    sensitive_list = []

    openapi_types = {
        'is_public': 'bool',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'x_obs_bucket_type': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'is_public': 'IsPublic',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'x_obs_bucket_type': 'x-obs-bucket-type',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, is_public=None, x_obs_id_2=None, x_obs_request_id=None, x_obs_bucket_type=None, connection=None, content_length=None, date=None):
        r"""GetBucketPolicyPublicStatusResponse

        The model defined in huaweicloud sdk

        :param is_public: Public access status of the bucket policy. 
        :type is_public: bool
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param x_obs_bucket_type: 
        :type x_obs_bucket_type: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super().__init__()

        self._is_public = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._x_obs_bucket_type = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if is_public is not None:
            self.is_public = is_public
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if x_obs_bucket_type is not None:
            self.x_obs_bucket_type = x_obs_bucket_type
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def is_public(self):
        r"""Gets the is_public of this GetBucketPolicyPublicStatusResponse.

        Public access status of the bucket policy. 

        :return: The is_public of this GetBucketPolicyPublicStatusResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this GetBucketPolicyPublicStatusResponse.

        Public access status of the bucket policy. 

        :param is_public: The is_public of this GetBucketPolicyPublicStatusResponse.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetBucketPolicyPublicStatusResponse.

        :return: The x_obs_id_2 of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetBucketPolicyPublicStatusResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetBucketPolicyPublicStatusResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetBucketPolicyPublicStatusResponse.

        :return: The x_obs_request_id of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetBucketPolicyPublicStatusResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetBucketPolicyPublicStatusResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def x_obs_bucket_type(self):
        r"""Gets the x_obs_bucket_type of this GetBucketPolicyPublicStatusResponse.

        :return: The x_obs_bucket_type of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._x_obs_bucket_type

    @x_obs_bucket_type.setter
    def x_obs_bucket_type(self, x_obs_bucket_type):
        r"""Sets the x_obs_bucket_type of this GetBucketPolicyPublicStatusResponse.

        :param x_obs_bucket_type: The x_obs_bucket_type of this GetBucketPolicyPublicStatusResponse.
        :type x_obs_bucket_type: str
        """
        self._x_obs_bucket_type = x_obs_bucket_type

    @property
    def connection(self):
        r"""Gets the connection of this GetBucketPolicyPublicStatusResponse.

        :return: The connection of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetBucketPolicyPublicStatusResponse.

        :param connection: The connection of this GetBucketPolicyPublicStatusResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this GetBucketPolicyPublicStatusResponse.

        :return: The content_length of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetBucketPolicyPublicStatusResponse.

        :param content_length: The content_length of this GetBucketPolicyPublicStatusResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this GetBucketPolicyPublicStatusResponse.

        :return: The date of this GetBucketPolicyPublicStatusResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketPolicyPublicStatusResponse.

        :param date: The date of this GetBucketPolicyPublicStatusResponse.
        :type date: str
        """
        self._date = date

    def to_dict(self):
        import warnings
        warnings.warn("GetBucketPolicyPublicStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetBucketPolicyPublicStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
