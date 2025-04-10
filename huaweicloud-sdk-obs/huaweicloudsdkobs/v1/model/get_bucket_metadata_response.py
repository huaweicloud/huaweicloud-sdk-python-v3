# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketMetadataResponse"

    sensitive_list = []

    openapi_types = {
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'x_obs_fs_file_interface': 'str',
        'x_obs_version': 'str',
        'access_control_allow_origin': 'str',
        'access_control_allow_methods': 'str',
        'x_obs_bucket_location': 'str',
        'connection': 'str',
        'x_obs_epid': 'str',
        'date': 'str',
        'access_control_allow_headers': 'str',
        'access_control_expose_headers': 'str',
        'e_tag': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_az_redundancy': 'str',
        'content_length': 'str',
        'access_control_max_age': 'int',
        'x_obs_ies_location': 'str'
    }

    attribute_map = {
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'x_obs_fs_file_interface': 'x-obs-fs-file-interface',
        'x_obs_version': 'x-obs-version',
        'access_control_allow_origin': 'Access-Control-Allow-Origin',
        'access_control_allow_methods': 'Access-Control-Allow-Methods',
        'x_obs_bucket_location': 'x-obs-bucket-location',
        'connection': 'Connection',
        'x_obs_epid': 'x-obs-epid',
        'date': 'Date',
        'access_control_allow_headers': 'Access-Control-Allow-Headers',
        'access_control_expose_headers': 'Access-Control-Expose-Headers',
        'e_tag': 'ETag',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_az_redundancy': 'x-obs-az-redundancy',
        'content_length': 'Content-Length',
        'access_control_max_age': 'Access-Control-Max-Age',
        'x_obs_ies_location': 'x-obs-ies-location'
    }

    def __init__(self, x_obs_id_2=None, x_obs_request_id=None, x_obs_fs_file_interface=None, x_obs_version=None, access_control_allow_origin=None, access_control_allow_methods=None, x_obs_bucket_location=None, connection=None, x_obs_epid=None, date=None, access_control_allow_headers=None, access_control_expose_headers=None, e_tag=None, x_obs_storage_class=None, x_obs_az_redundancy=None, content_length=None, access_control_max_age=None, x_obs_ies_location=None):
        r"""GetBucketMetadataResponse

        The model defined in huaweicloud sdk

        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param x_obs_fs_file_interface: 
        :type x_obs_fs_file_interface: str
        :param x_obs_version: 
        :type x_obs_version: str
        :param access_control_allow_origin: 
        :type access_control_allow_origin: str
        :param access_control_allow_methods: 
        :type access_control_allow_methods: str
        :param x_obs_bucket_location: 
        :type x_obs_bucket_location: str
        :param connection: 
        :type connection: str
        :param x_obs_epid: 
        :type x_obs_epid: str
        :param date: 
        :type date: str
        :param access_control_allow_headers: 
        :type access_control_allow_headers: str
        :param access_control_expose_headers: 
        :type access_control_expose_headers: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_storage_class: 
        :type x_obs_storage_class: str
        :param x_obs_az_redundancy: 
        :type x_obs_az_redundancy: str
        :param content_length: 
        :type content_length: str
        :param access_control_max_age: 
        :type access_control_max_age: int
        :param x_obs_ies_location: 
        :type x_obs_ies_location: str
        """
        
        super(GetBucketMetadataResponse, self).__init__()

        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._x_obs_fs_file_interface = None
        self._x_obs_version = None
        self._access_control_allow_origin = None
        self._access_control_allow_methods = None
        self._x_obs_bucket_location = None
        self._connection = None
        self._x_obs_epid = None
        self._date = None
        self._access_control_allow_headers = None
        self._access_control_expose_headers = None
        self._e_tag = None
        self._x_obs_storage_class = None
        self._x_obs_az_redundancy = None
        self._content_length = None
        self._access_control_max_age = None
        self._x_obs_ies_location = None
        self.discriminator = None

        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if x_obs_fs_file_interface is not None:
            self.x_obs_fs_file_interface = x_obs_fs_file_interface
        if x_obs_version is not None:
            self.x_obs_version = x_obs_version
        if access_control_allow_origin is not None:
            self.access_control_allow_origin = access_control_allow_origin
        if access_control_allow_methods is not None:
            self.access_control_allow_methods = access_control_allow_methods
        if x_obs_bucket_location is not None:
            self.x_obs_bucket_location = x_obs_bucket_location
        if connection is not None:
            self.connection = connection
        if x_obs_epid is not None:
            self.x_obs_epid = x_obs_epid
        if date is not None:
            self.date = date
        if access_control_allow_headers is not None:
            self.access_control_allow_headers = access_control_allow_headers
        if access_control_expose_headers is not None:
            self.access_control_expose_headers = access_control_expose_headers
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_az_redundancy is not None:
            self.x_obs_az_redundancy = x_obs_az_redundancy
        if content_length is not None:
            self.content_length = content_length
        if access_control_max_age is not None:
            self.access_control_max_age = access_control_max_age
        if x_obs_ies_location is not None:
            self.x_obs_ies_location = x_obs_ies_location

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetBucketMetadataResponse.

        :return: The x_obs_id_2 of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetBucketMetadataResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetBucketMetadataResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetBucketMetadataResponse.

        :return: The x_obs_request_id of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetBucketMetadataResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetBucketMetadataResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def x_obs_fs_file_interface(self):
        r"""Gets the x_obs_fs_file_interface of this GetBucketMetadataResponse.

        :return: The x_obs_fs_file_interface of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_fs_file_interface

    @x_obs_fs_file_interface.setter
    def x_obs_fs_file_interface(self, x_obs_fs_file_interface):
        r"""Sets the x_obs_fs_file_interface of this GetBucketMetadataResponse.

        :param x_obs_fs_file_interface: The x_obs_fs_file_interface of this GetBucketMetadataResponse.
        :type x_obs_fs_file_interface: str
        """
        self._x_obs_fs_file_interface = x_obs_fs_file_interface

    @property
    def x_obs_version(self):
        r"""Gets the x_obs_version of this GetBucketMetadataResponse.

        :return: The x_obs_version of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_version

    @x_obs_version.setter
    def x_obs_version(self, x_obs_version):
        r"""Sets the x_obs_version of this GetBucketMetadataResponse.

        :param x_obs_version: The x_obs_version of this GetBucketMetadataResponse.
        :type x_obs_version: str
        """
        self._x_obs_version = x_obs_version

    @property
    def access_control_allow_origin(self):
        r"""Gets the access_control_allow_origin of this GetBucketMetadataResponse.

        :return: The access_control_allow_origin of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_origin

    @access_control_allow_origin.setter
    def access_control_allow_origin(self, access_control_allow_origin):
        r"""Sets the access_control_allow_origin of this GetBucketMetadataResponse.

        :param access_control_allow_origin: The access_control_allow_origin of this GetBucketMetadataResponse.
        :type access_control_allow_origin: str
        """
        self._access_control_allow_origin = access_control_allow_origin

    @property
    def access_control_allow_methods(self):
        r"""Gets the access_control_allow_methods of this GetBucketMetadataResponse.

        :return: The access_control_allow_methods of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_methods

    @access_control_allow_methods.setter
    def access_control_allow_methods(self, access_control_allow_methods):
        r"""Sets the access_control_allow_methods of this GetBucketMetadataResponse.

        :param access_control_allow_methods: The access_control_allow_methods of this GetBucketMetadataResponse.
        :type access_control_allow_methods: str
        """
        self._access_control_allow_methods = access_control_allow_methods

    @property
    def x_obs_bucket_location(self):
        r"""Gets the x_obs_bucket_location of this GetBucketMetadataResponse.

        :return: The x_obs_bucket_location of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_bucket_location

    @x_obs_bucket_location.setter
    def x_obs_bucket_location(self, x_obs_bucket_location):
        r"""Sets the x_obs_bucket_location of this GetBucketMetadataResponse.

        :param x_obs_bucket_location: The x_obs_bucket_location of this GetBucketMetadataResponse.
        :type x_obs_bucket_location: str
        """
        self._x_obs_bucket_location = x_obs_bucket_location

    @property
    def connection(self):
        r"""Gets the connection of this GetBucketMetadataResponse.

        :return: The connection of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetBucketMetadataResponse.

        :param connection: The connection of this GetBucketMetadataResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def x_obs_epid(self):
        r"""Gets the x_obs_epid of this GetBucketMetadataResponse.

        :return: The x_obs_epid of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_epid

    @x_obs_epid.setter
    def x_obs_epid(self, x_obs_epid):
        r"""Sets the x_obs_epid of this GetBucketMetadataResponse.

        :param x_obs_epid: The x_obs_epid of this GetBucketMetadataResponse.
        :type x_obs_epid: str
        """
        self._x_obs_epid = x_obs_epid

    @property
    def date(self):
        r"""Gets the date of this GetBucketMetadataResponse.

        :return: The date of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketMetadataResponse.

        :param date: The date of this GetBucketMetadataResponse.
        :type date: str
        """
        self._date = date

    @property
    def access_control_allow_headers(self):
        r"""Gets the access_control_allow_headers of this GetBucketMetadataResponse.

        :return: The access_control_allow_headers of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_headers

    @access_control_allow_headers.setter
    def access_control_allow_headers(self, access_control_allow_headers):
        r"""Sets the access_control_allow_headers of this GetBucketMetadataResponse.

        :param access_control_allow_headers: The access_control_allow_headers of this GetBucketMetadataResponse.
        :type access_control_allow_headers: str
        """
        self._access_control_allow_headers = access_control_allow_headers

    @property
    def access_control_expose_headers(self):
        r"""Gets the access_control_expose_headers of this GetBucketMetadataResponse.

        :return: The access_control_expose_headers of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._access_control_expose_headers

    @access_control_expose_headers.setter
    def access_control_expose_headers(self, access_control_expose_headers):
        r"""Sets the access_control_expose_headers of this GetBucketMetadataResponse.

        :param access_control_expose_headers: The access_control_expose_headers of this GetBucketMetadataResponse.
        :type access_control_expose_headers: str
        """
        self._access_control_expose_headers = access_control_expose_headers

    @property
    def e_tag(self):
        r"""Gets the e_tag of this GetBucketMetadataResponse.

        :return: The e_tag of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this GetBucketMetadataResponse.

        :param e_tag: The e_tag of this GetBucketMetadataResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this GetBucketMetadataResponse.

        :return: The x_obs_storage_class of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this GetBucketMetadataResponse.

        :param x_obs_storage_class: The x_obs_storage_class of this GetBucketMetadataResponse.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_az_redundancy(self):
        r"""Gets the x_obs_az_redundancy of this GetBucketMetadataResponse.

        :return: The x_obs_az_redundancy of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_az_redundancy

    @x_obs_az_redundancy.setter
    def x_obs_az_redundancy(self, x_obs_az_redundancy):
        r"""Sets the x_obs_az_redundancy of this GetBucketMetadataResponse.

        :param x_obs_az_redundancy: The x_obs_az_redundancy of this GetBucketMetadataResponse.
        :type x_obs_az_redundancy: str
        """
        self._x_obs_az_redundancy = x_obs_az_redundancy

    @property
    def content_length(self):
        r"""Gets the content_length of this GetBucketMetadataResponse.

        :return: The content_length of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetBucketMetadataResponse.

        :param content_length: The content_length of this GetBucketMetadataResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def access_control_max_age(self):
        r"""Gets the access_control_max_age of this GetBucketMetadataResponse.

        :return: The access_control_max_age of this GetBucketMetadataResponse.
        :rtype: int
        """
        return self._access_control_max_age

    @access_control_max_age.setter
    def access_control_max_age(self, access_control_max_age):
        r"""Sets the access_control_max_age of this GetBucketMetadataResponse.

        :param access_control_max_age: The access_control_max_age of this GetBucketMetadataResponse.
        :type access_control_max_age: int
        """
        self._access_control_max_age = access_control_max_age

    @property
    def x_obs_ies_location(self):
        r"""Gets the x_obs_ies_location of this GetBucketMetadataResponse.

        :return: The x_obs_ies_location of this GetBucketMetadataResponse.
        :rtype: str
        """
        return self._x_obs_ies_location

    @x_obs_ies_location.setter
    def x_obs_ies_location(self, x_obs_ies_location):
        r"""Sets the x_obs_ies_location of this GetBucketMetadataResponse.

        :param x_obs_ies_location: The x_obs_ies_location of this GetBucketMetadataResponse.
        :type x_obs_ies_location: str
        """
        self._x_obs_ies_location = x_obs_ies_location

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
        if not isinstance(other, GetBucketMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
