# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBucketsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "ListBucketsResponse"

    sensitive_list = []

    openapi_types = {
        'owner': 'Owner',
        'buckets': 'Buckets',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'x_obs_bucket_type': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'owner': 'Owner',
        'buckets': 'Buckets',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'x_obs_bucket_type': 'x-obs-bucket-type',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, owner=None, buckets=None, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, x_obs_bucket_type=None, connection=None, content_length=None, date=None):
        r"""ListBucketsResponse

        The model defined in huaweicloud sdk

        :param owner: 
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        :param buckets: 
        :type buckets: :class:`huaweicloudsdkobs.v1.Buckets`
        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_bucket_type: 
        :type x_obs_bucket_type: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ListBucketsResponse, self).__init__()

        self._owner = None
        self._buckets = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._x_obs_bucket_type = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if buckets is not None:
            self.buckets = buckets
        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_bucket_type is not None:
            self.x_obs_bucket_type = x_obs_bucket_type
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def owner(self):
        r"""Gets the owner of this ListBucketsResponse.

        :return: The owner of this ListBucketsResponse.
        :rtype: :class:`huaweicloudsdkobs.v1.Owner`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListBucketsResponse.

        :param owner: The owner of this ListBucketsResponse.
        :type owner: :class:`huaweicloudsdkobs.v1.Owner`
        """
        self._owner = owner

    @property
    def buckets(self):
        r"""Gets the buckets of this ListBucketsResponse.

        :return: The buckets of this ListBucketsResponse.
        :rtype: :class:`huaweicloudsdkobs.v1.Buckets`
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        r"""Sets the buckets of this ListBucketsResponse.

        :param buckets: The buckets of this ListBucketsResponse.
        :type buckets: :class:`huaweicloudsdkobs.v1.Buckets`
        """
        self._buckets = buckets

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this ListBucketsResponse.

        :return: The x_obs_id_2 of this ListBucketsResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this ListBucketsResponse.

        :param x_obs_id_2: The x_obs_id_2 of this ListBucketsResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this ListBucketsResponse.

        :return: The x_obs_request_id of this ListBucketsResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this ListBucketsResponse.

        :param x_obs_request_id: The x_obs_request_id of this ListBucketsResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this ListBucketsResponse.

        :return: The e_tag of this ListBucketsResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this ListBucketsResponse.

        :param e_tag: The e_tag of this ListBucketsResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_bucket_type(self):
        r"""Gets the x_obs_bucket_type of this ListBucketsResponse.

        :return: The x_obs_bucket_type of this ListBucketsResponse.
        :rtype: str
        """
        return self._x_obs_bucket_type

    @x_obs_bucket_type.setter
    def x_obs_bucket_type(self, x_obs_bucket_type):
        r"""Sets the x_obs_bucket_type of this ListBucketsResponse.

        :param x_obs_bucket_type: The x_obs_bucket_type of this ListBucketsResponse.
        :type x_obs_bucket_type: str
        """
        self._x_obs_bucket_type = x_obs_bucket_type

    @property
    def connection(self):
        r"""Gets the connection of this ListBucketsResponse.

        :return: The connection of this ListBucketsResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ListBucketsResponse.

        :param connection: The connection of this ListBucketsResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this ListBucketsResponse.

        :return: The content_length of this ListBucketsResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ListBucketsResponse.

        :param content_length: The content_length of this ListBucketsResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this ListBucketsResponse.

        :return: The date of this ListBucketsResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ListBucketsResponse.

        :param date: The date of this ListBucketsResponse.
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
        if not isinstance(other, ListBucketsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
