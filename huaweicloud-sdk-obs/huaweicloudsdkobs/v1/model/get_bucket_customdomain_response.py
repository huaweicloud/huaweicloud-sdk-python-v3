# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketCustomdomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketCustomdomainResponse"

    sensitive_list = []

    openapi_types = {
        'domains': 'Domains',
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'e_tag': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'domains': 'Domains',
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'e_tag': 'ETag',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, domains=None, x_obs_id_2=None, x_obs_request_id=None, e_tag=None, connection=None, content_length=None, date=None):
        r"""GetBucketCustomdomainResponse

        The model defined in huaweicloud sdk

        :param domains: 
        :type domains: :class:`huaweicloudsdkobs.v1.Domains`
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
        
        super(GetBucketCustomdomainResponse, self).__init__()

        self._domains = None
        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._e_tag = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
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
    def domains(self):
        r"""Gets the domains of this GetBucketCustomdomainResponse.

        :return: The domains of this GetBucketCustomdomainResponse.
        :rtype: :class:`huaweicloudsdkobs.v1.Domains`
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this GetBucketCustomdomainResponse.

        :param domains: The domains of this GetBucketCustomdomainResponse.
        :type domains: :class:`huaweicloudsdkobs.v1.Domains`
        """
        self._domains = domains

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetBucketCustomdomainResponse.

        :return: The x_obs_id_2 of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetBucketCustomdomainResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetBucketCustomdomainResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetBucketCustomdomainResponse.

        :return: The x_obs_request_id of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetBucketCustomdomainResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetBucketCustomdomainResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def e_tag(self):
        r"""Gets the e_tag of this GetBucketCustomdomainResponse.

        :return: The e_tag of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this GetBucketCustomdomainResponse.

        :param e_tag: The e_tag of this GetBucketCustomdomainResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def connection(self):
        r"""Gets the connection of this GetBucketCustomdomainResponse.

        :return: The connection of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetBucketCustomdomainResponse.

        :param connection: The connection of this GetBucketCustomdomainResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this GetBucketCustomdomainResponse.

        :return: The content_length of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetBucketCustomdomainResponse.

        :param content_length: The content_length of this GetBucketCustomdomainResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this GetBucketCustomdomainResponse.

        :return: The date of this GetBucketCustomdomainResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketCustomdomainResponse.

        :param date: The date of this GetBucketCustomdomainResponse.
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
        if not isinstance(other, GetBucketCustomdomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
