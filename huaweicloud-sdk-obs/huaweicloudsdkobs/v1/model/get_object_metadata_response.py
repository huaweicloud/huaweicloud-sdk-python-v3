# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetObjectMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetObjectMetadataResponse"

    sensitive_list = []

    openapi_types = {
        'x_obs_id_2': 'str',
        'x_obs_request_id': 'str',
        'x_obs_hash_crc64ecma': 'str',
        'access_control_allow_origin': 'str',
        'x_obs_server_side_encryption': 'str',
        'x_obs_restore': 'str',
        'x_obs_object_type': 'str',
        'x_obs_next_append_position': 'int',
        'access_control_allow_methods': 'str',
        'connection': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str',
        'x_obs_expiration': 'str',
        'date': 'str',
        'access_control_allow_headers': 'str',
        'x_obs_upload_id': 'str',
        'access_control_expose_headers': 'str',
        'e_tag': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
        'content_length': 'str',
        'access_control_max_age': 'int',
        'x_obs_website_redirect_location': 'str',
        'x_obs_version_id': 'str'
    }

    attribute_map = {
        'x_obs_id_2': 'x-obs-id-2',
        'x_obs_request_id': 'x-obs-request-id',
        'x_obs_hash_crc64ecma': 'x-obs-hash-crc64ecma',
        'access_control_allow_origin': 'Access-Control-Allow-Origin',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'x_obs_restore': 'x-obs-restore',
        'x_obs_object_type': 'x-obs-object-type',
        'x_obs_next_append_position': 'x-obs-next-append-position',
        'access_control_allow_methods': 'Access-Control-Allow-Methods',
        'connection': 'Connection',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'x_obs_expiration': 'x-obs-expiration',
        'date': 'Date',
        'access_control_allow_headers': 'Access-Control-Allow-Headers',
        'x_obs_upload_id': 'x-obs-uploadId',
        'access_control_expose_headers': 'Access-Control-Expose-Headers',
        'e_tag': 'ETag',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'content_length': 'Content-Length',
        'access_control_max_age': 'Access-Control-Max-Age',
        'x_obs_website_redirect_location': 'x-obs-website-redirect-location',
        'x_obs_version_id': 'x-obs-version-id'
    }

    def __init__(self, x_obs_id_2=None, x_obs_request_id=None, x_obs_hash_crc64ecma=None, access_control_allow_origin=None, x_obs_server_side_encryption=None, x_obs_restore=None, x_obs_object_type=None, x_obs_next_append_position=None, access_control_allow_methods=None, connection=None, x_obs_server_side_encryption_customer_key_md5=None, x_obs_expiration=None, date=None, access_control_allow_headers=None, x_obs_upload_id=None, access_control_expose_headers=None, e_tag=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_storage_class=None, x_obs_server_side_encryption_kms_key_id=None, content_length=None, access_control_max_age=None, x_obs_website_redirect_location=None, x_obs_version_id=None):
        r"""GetObjectMetadataResponse

        The model defined in huaweicloud sdk

        :param x_obs_id_2: 
        :type x_obs_id_2: str
        :param x_obs_request_id: 
        :type x_obs_request_id: str
        :param x_obs_hash_crc64ecma: 
        :type x_obs_hash_crc64ecma: str
        :param access_control_allow_origin: 
        :type access_control_allow_origin: str
        :param x_obs_server_side_encryption: 
        :type x_obs_server_side_encryption: str
        :param x_obs_restore: 
        :type x_obs_restore: str
        :param x_obs_object_type: 
        :type x_obs_object_type: str
        :param x_obs_next_append_position: 
        :type x_obs_next_append_position: int
        :param access_control_allow_methods: 
        :type access_control_allow_methods: str
        :param connection: 
        :type connection: str
        :param x_obs_server_side_encryption_customer_key_md5: 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param x_obs_expiration: 
        :type x_obs_expiration: str
        :param date: 
        :type date: str
        :param access_control_allow_headers: 
        :type access_control_allow_headers: str
        :param x_obs_upload_id: 
        :type x_obs_upload_id: str
        :param access_control_expose_headers: 
        :type access_control_expose_headers: str
        :param e_tag: 
        :type e_tag: str
        :param x_obs_server_side_encryption_customer_algorithm: 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_storage_class: 
        :type x_obs_storage_class: str
        :param x_obs_server_side_encryption_kms_key_id: 
        :type x_obs_server_side_encryption_kms_key_id: str
        :param content_length: 
        :type content_length: str
        :param access_control_max_age: 
        :type access_control_max_age: int
        :param x_obs_website_redirect_location: 
        :type x_obs_website_redirect_location: str
        :param x_obs_version_id: 
        :type x_obs_version_id: str
        """
        
        super(GetObjectMetadataResponse, self).__init__()

        self._x_obs_id_2 = None
        self._x_obs_request_id = None
        self._x_obs_hash_crc64ecma = None
        self._access_control_allow_origin = None
        self._x_obs_server_side_encryption = None
        self._x_obs_restore = None
        self._x_obs_object_type = None
        self._x_obs_next_append_position = None
        self._access_control_allow_methods = None
        self._connection = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self._x_obs_expiration = None
        self._date = None
        self._access_control_allow_headers = None
        self._x_obs_upload_id = None
        self._access_control_expose_headers = None
        self._e_tag = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_storage_class = None
        self._x_obs_server_side_encryption_kms_key_id = None
        self._content_length = None
        self._access_control_max_age = None
        self._x_obs_website_redirect_location = None
        self._x_obs_version_id = None
        self.discriminator = None

        if x_obs_id_2 is not None:
            self.x_obs_id_2 = x_obs_id_2
        if x_obs_request_id is not None:
            self.x_obs_request_id = x_obs_request_id
        if x_obs_hash_crc64ecma is not None:
            self.x_obs_hash_crc64ecma = x_obs_hash_crc64ecma
        if access_control_allow_origin is not None:
            self.access_control_allow_origin = access_control_allow_origin
        if x_obs_server_side_encryption is not None:
            self.x_obs_server_side_encryption = x_obs_server_side_encryption
        if x_obs_restore is not None:
            self.x_obs_restore = x_obs_restore
        if x_obs_object_type is not None:
            self.x_obs_object_type = x_obs_object_type
        if x_obs_next_append_position is not None:
            self.x_obs_next_append_position = x_obs_next_append_position
        if access_control_allow_methods is not None:
            self.access_control_allow_methods = access_control_allow_methods
        if connection is not None:
            self.connection = connection
        if x_obs_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5
        if x_obs_expiration is not None:
            self.x_obs_expiration = x_obs_expiration
        if date is not None:
            self.date = date
        if access_control_allow_headers is not None:
            self.access_control_allow_headers = access_control_allow_headers
        if x_obs_upload_id is not None:
            self.x_obs_upload_id = x_obs_upload_id
        if access_control_expose_headers is not None:
            self.access_control_expose_headers = access_control_expose_headers
        if e_tag is not None:
            self.e_tag = e_tag
        if x_obs_server_side_encryption_customer_algorithm is not None:
            self.x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_server_side_encryption_kms_key_id is not None:
            self.x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id
        if content_length is not None:
            self.content_length = content_length
        if access_control_max_age is not None:
            self.access_control_max_age = access_control_max_age
        if x_obs_website_redirect_location is not None:
            self.x_obs_website_redirect_location = x_obs_website_redirect_location
        if x_obs_version_id is not None:
            self.x_obs_version_id = x_obs_version_id

    @property
    def x_obs_id_2(self):
        r"""Gets the x_obs_id_2 of this GetObjectMetadataResponse.

        :return: The x_obs_id_2 of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_id_2

    @x_obs_id_2.setter
    def x_obs_id_2(self, x_obs_id_2):
        r"""Sets the x_obs_id_2 of this GetObjectMetadataResponse.

        :param x_obs_id_2: The x_obs_id_2 of this GetObjectMetadataResponse.
        :type x_obs_id_2: str
        """
        self._x_obs_id_2 = x_obs_id_2

    @property
    def x_obs_request_id(self):
        r"""Gets the x_obs_request_id of this GetObjectMetadataResponse.

        :return: The x_obs_request_id of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_request_id

    @x_obs_request_id.setter
    def x_obs_request_id(self, x_obs_request_id):
        r"""Sets the x_obs_request_id of this GetObjectMetadataResponse.

        :param x_obs_request_id: The x_obs_request_id of this GetObjectMetadataResponse.
        :type x_obs_request_id: str
        """
        self._x_obs_request_id = x_obs_request_id

    @property
    def x_obs_hash_crc64ecma(self):
        r"""Gets the x_obs_hash_crc64ecma of this GetObjectMetadataResponse.

        :return: The x_obs_hash_crc64ecma of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_hash_crc64ecma

    @x_obs_hash_crc64ecma.setter
    def x_obs_hash_crc64ecma(self, x_obs_hash_crc64ecma):
        r"""Sets the x_obs_hash_crc64ecma of this GetObjectMetadataResponse.

        :param x_obs_hash_crc64ecma: The x_obs_hash_crc64ecma of this GetObjectMetadataResponse.
        :type x_obs_hash_crc64ecma: str
        """
        self._x_obs_hash_crc64ecma = x_obs_hash_crc64ecma

    @property
    def access_control_allow_origin(self):
        r"""Gets the access_control_allow_origin of this GetObjectMetadataResponse.

        :return: The access_control_allow_origin of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_origin

    @access_control_allow_origin.setter
    def access_control_allow_origin(self, access_control_allow_origin):
        r"""Sets the access_control_allow_origin of this GetObjectMetadataResponse.

        :param access_control_allow_origin: The access_control_allow_origin of this GetObjectMetadataResponse.
        :type access_control_allow_origin: str
        """
        self._access_control_allow_origin = access_control_allow_origin

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this GetObjectMetadataResponse.

        :return: The x_obs_server_side_encryption of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this GetObjectMetadataResponse.

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this GetObjectMetadataResponse.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_restore(self):
        r"""Gets the x_obs_restore of this GetObjectMetadataResponse.

        :return: The x_obs_restore of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_restore

    @x_obs_restore.setter
    def x_obs_restore(self, x_obs_restore):
        r"""Sets the x_obs_restore of this GetObjectMetadataResponse.

        :param x_obs_restore: The x_obs_restore of this GetObjectMetadataResponse.
        :type x_obs_restore: str
        """
        self._x_obs_restore = x_obs_restore

    @property
    def x_obs_object_type(self):
        r"""Gets the x_obs_object_type of this GetObjectMetadataResponse.

        :return: The x_obs_object_type of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_object_type

    @x_obs_object_type.setter
    def x_obs_object_type(self, x_obs_object_type):
        r"""Sets the x_obs_object_type of this GetObjectMetadataResponse.

        :param x_obs_object_type: The x_obs_object_type of this GetObjectMetadataResponse.
        :type x_obs_object_type: str
        """
        self._x_obs_object_type = x_obs_object_type

    @property
    def x_obs_next_append_position(self):
        r"""Gets the x_obs_next_append_position of this GetObjectMetadataResponse.

        :return: The x_obs_next_append_position of this GetObjectMetadataResponse.
        :rtype: int
        """
        return self._x_obs_next_append_position

    @x_obs_next_append_position.setter
    def x_obs_next_append_position(self, x_obs_next_append_position):
        r"""Sets the x_obs_next_append_position of this GetObjectMetadataResponse.

        :param x_obs_next_append_position: The x_obs_next_append_position of this GetObjectMetadataResponse.
        :type x_obs_next_append_position: int
        """
        self._x_obs_next_append_position = x_obs_next_append_position

    @property
    def access_control_allow_methods(self):
        r"""Gets the access_control_allow_methods of this GetObjectMetadataResponse.

        :return: The access_control_allow_methods of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_methods

    @access_control_allow_methods.setter
    def access_control_allow_methods(self, access_control_allow_methods):
        r"""Sets the access_control_allow_methods of this GetObjectMetadataResponse.

        :param access_control_allow_methods: The access_control_allow_methods of this GetObjectMetadataResponse.
        :type access_control_allow_methods: str
        """
        self._access_control_allow_methods = access_control_allow_methods

    @property
    def connection(self):
        r"""Gets the connection of this GetObjectMetadataResponse.

        :return: The connection of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this GetObjectMetadataResponse.

        :param connection: The connection of this GetObjectMetadataResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataResponse.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataResponse.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataResponse.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def x_obs_expiration(self):
        r"""Gets the x_obs_expiration of this GetObjectMetadataResponse.

        :return: The x_obs_expiration of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_expiration

    @x_obs_expiration.setter
    def x_obs_expiration(self, x_obs_expiration):
        r"""Sets the x_obs_expiration of this GetObjectMetadataResponse.

        :param x_obs_expiration: The x_obs_expiration of this GetObjectMetadataResponse.
        :type x_obs_expiration: str
        """
        self._x_obs_expiration = x_obs_expiration

    @property
    def date(self):
        r"""Gets the date of this GetObjectMetadataResponse.

        :return: The date of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetObjectMetadataResponse.

        :param date: The date of this GetObjectMetadataResponse.
        :type date: str
        """
        self._date = date

    @property
    def access_control_allow_headers(self):
        r"""Gets the access_control_allow_headers of this GetObjectMetadataResponse.

        :return: The access_control_allow_headers of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._access_control_allow_headers

    @access_control_allow_headers.setter
    def access_control_allow_headers(self, access_control_allow_headers):
        r"""Sets the access_control_allow_headers of this GetObjectMetadataResponse.

        :param access_control_allow_headers: The access_control_allow_headers of this GetObjectMetadataResponse.
        :type access_control_allow_headers: str
        """
        self._access_control_allow_headers = access_control_allow_headers

    @property
    def x_obs_upload_id(self):
        r"""Gets the x_obs_upload_id of this GetObjectMetadataResponse.

        :return: The x_obs_upload_id of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_upload_id

    @x_obs_upload_id.setter
    def x_obs_upload_id(self, x_obs_upload_id):
        r"""Sets the x_obs_upload_id of this GetObjectMetadataResponse.

        :param x_obs_upload_id: The x_obs_upload_id of this GetObjectMetadataResponse.
        :type x_obs_upload_id: str
        """
        self._x_obs_upload_id = x_obs_upload_id

    @property
    def access_control_expose_headers(self):
        r"""Gets the access_control_expose_headers of this GetObjectMetadataResponse.

        :return: The access_control_expose_headers of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._access_control_expose_headers

    @access_control_expose_headers.setter
    def access_control_expose_headers(self, access_control_expose_headers):
        r"""Sets the access_control_expose_headers of this GetObjectMetadataResponse.

        :param access_control_expose_headers: The access_control_expose_headers of this GetObjectMetadataResponse.
        :type access_control_expose_headers: str
        """
        self._access_control_expose_headers = access_control_expose_headers

    @property
    def e_tag(self):
        r"""Gets the e_tag of this GetObjectMetadataResponse.

        :return: The e_tag of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        r"""Sets the e_tag of this GetObjectMetadataResponse.

        :param e_tag: The e_tag of this GetObjectMetadataResponse.
        :type e_tag: str
        """
        self._e_tag = e_tag

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataResponse.

        :return: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataResponse.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataResponse.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this GetObjectMetadataResponse.

        :return: The x_obs_storage_class of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this GetObjectMetadataResponse.

        :param x_obs_storage_class: The x_obs_storage_class of this GetObjectMetadataResponse.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this GetObjectMetadataResponse.

        :return: The x_obs_server_side_encryption_kms_key_id of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this GetObjectMetadataResponse.

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this GetObjectMetadataResponse.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def content_length(self):
        r"""Gets the content_length of this GetObjectMetadataResponse.

        :return: The content_length of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this GetObjectMetadataResponse.

        :param content_length: The content_length of this GetObjectMetadataResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def access_control_max_age(self):
        r"""Gets the access_control_max_age of this GetObjectMetadataResponse.

        :return: The access_control_max_age of this GetObjectMetadataResponse.
        :rtype: int
        """
        return self._access_control_max_age

    @access_control_max_age.setter
    def access_control_max_age(self, access_control_max_age):
        r"""Sets the access_control_max_age of this GetObjectMetadataResponse.

        :param access_control_max_age: The access_control_max_age of this GetObjectMetadataResponse.
        :type access_control_max_age: int
        """
        self._access_control_max_age = access_control_max_age

    @property
    def x_obs_website_redirect_location(self):
        r"""Gets the x_obs_website_redirect_location of this GetObjectMetadataResponse.

        :return: The x_obs_website_redirect_location of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_website_redirect_location

    @x_obs_website_redirect_location.setter
    def x_obs_website_redirect_location(self, x_obs_website_redirect_location):
        r"""Sets the x_obs_website_redirect_location of this GetObjectMetadataResponse.

        :param x_obs_website_redirect_location: The x_obs_website_redirect_location of this GetObjectMetadataResponse.
        :type x_obs_website_redirect_location: str
        """
        self._x_obs_website_redirect_location = x_obs_website_redirect_location

    @property
    def x_obs_version_id(self):
        r"""Gets the x_obs_version_id of this GetObjectMetadataResponse.

        :return: The x_obs_version_id of this GetObjectMetadataResponse.
        :rtype: str
        """
        return self._x_obs_version_id

    @x_obs_version_id.setter
    def x_obs_version_id(self, x_obs_version_id):
        r"""Sets the x_obs_version_id of this GetObjectMetadataResponse.

        :param x_obs_version_id: The x_obs_version_id of this GetObjectMetadataResponse.
        :type x_obs_version_id: str
        """
        self._x_obs_version_id = x_obs_version_id

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
        if not isinstance(other, GetObjectMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
