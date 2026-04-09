# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HeadObjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "HeadObjectRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_key': 'str',
        'date': 'str',
        'version_id': 'str',
        'origin': 'str',
        'access_control_request_headers': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_server_side_encryption_customer_key': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'date': 'Date',
        'version_id': 'versionId',
        'origin': 'Origin',
        'access_control_request_headers': 'Access-Control-Request-Headers',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_server_side_encryption_customer_key': 'x-obs-server-side-encryption-customer-key',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5'
    }

    def __init__(self, bucket_name=None, object_key=None, date=None, version_id=None, origin=None, access_control_request_headers=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_server_side_encryption_customer_key=None, x_obs_server_side_encryption_customer_key_md5=None):
        r"""HeadObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: Name of the bucket.
        :type bucket_name: str
        :param object_key: Name of the object whose metadata will be returned.
        :type object_key: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param version_id: Version ID of the object.
        :type version_id: str
        :param origin: Origin (usually a domain name) specified by the pre-request (a cross-origin request).
        :type origin: str
        :param access_control_request_headers: HTTP headers that can be contained in a request.
        :type access_control_request_headers: str
        :param x_obs_server_side_encryption_customer_algorithm: The decryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: Decryption key used for SSE-C.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: MD5 value of the key used to encrypt objects in SSE-C mode. An MD5 value is used to ensure that there is no error during the key transmission.Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        
        

        self._bucket_name = None
        self._object_key = None
        self._date = None
        self._version_id = None
        self._origin = None
        self._access_control_request_headers = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_server_side_encryption_customer_key = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.object_key = object_key
        if date is not None:
            self.date = date
        if version_id is not None:
            self.version_id = version_id
        if origin is not None:
            self.origin = origin
        if access_control_request_headers is not None:
            self.access_control_request_headers = access_control_request_headers
        if x_obs_server_side_encryption_customer_algorithm is not None:
            self.x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm
        if x_obs_server_side_encryption_customer_key is not None:
            self.x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key
        if x_obs_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this HeadObjectRequest.

        Name of the bucket.

        :return: The bucket_name of this HeadObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this HeadObjectRequest.

        Name of the bucket.

        :param bucket_name: The bucket_name of this HeadObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this HeadObjectRequest.

        Name of the object whose metadata will be returned.

        :return: The object_key of this HeadObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this HeadObjectRequest.

        Name of the object whose metadata will be returned.

        :param object_key: The object_key of this HeadObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        r"""Gets the date of this HeadObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this HeadObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this HeadObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this HeadObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def version_id(self):
        r"""Gets the version_id of this HeadObjectRequest.

        Version ID of the object.

        :return: The version_id of this HeadObjectRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this HeadObjectRequest.

        Version ID of the object.

        :param version_id: The version_id of this HeadObjectRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def origin(self):
        r"""Gets the origin of this HeadObjectRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request).

        :return: The origin of this HeadObjectRequest.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this HeadObjectRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request).

        :param origin: The origin of this HeadObjectRequest.
        :type origin: str
        """
        self._origin = origin

    @property
    def access_control_request_headers(self):
        r"""Gets the access_control_request_headers of this HeadObjectRequest.

        HTTP headers that can be contained in a request.

        :return: The access_control_request_headers of this HeadObjectRequest.
        :rtype: str
        """
        return self._access_control_request_headers

    @access_control_request_headers.setter
    def access_control_request_headers(self, access_control_request_headers):
        r"""Sets the access_control_request_headers of this HeadObjectRequest.

        HTTP headers that can be contained in a request.

        :param access_control_request_headers: The access_control_request_headers of this HeadObjectRequest.
        :type access_control_request_headers: str
        """
        self._access_control_request_headers = access_control_request_headers

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this HeadObjectRequest.

        The decryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_algorithm of this HeadObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this HeadObjectRequest.

        The decryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this HeadObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_server_side_encryption_customer_key of this HeadObjectRequest.

        Decryption key used for SSE-C.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_key of this HeadObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        r"""Sets the x_obs_server_side_encryption_customer_key of this HeadObjectRequest.

        Decryption key used for SSE-C.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this HeadObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this HeadObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. An MD5 value is used to ensure that there is no error during the key transmission.Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this HeadObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this HeadObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. An MD5 value is used to ensure that there is no error during the key transmission.Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this HeadObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    def to_dict(self):
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
        if not isinstance(other, HeadObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
