# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetObjectMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetObjectMetadataRequest"

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
        'x_obs_server_side_encryption_customer_key_md5': 'str',
        'success_action_redirect': 'str',
        'x_obs_expires': 'int'
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
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'success_action_redirect': 'success-action-redirect',
        'x_obs_expires': 'x-obs-expires'
    }

    def __init__(self, bucket_name=None, object_key=None, date=None, version_id=None, origin=None, access_control_request_headers=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_server_side_encryption_customer_key=None, x_obs_server_side_encryption_customer_key_md5=None, success_action_redirect=None, x_obs_expires=None):
        r"""GetObjectMetadataRequest

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
        :param success_action_redirect: The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.
        :type success_action_redirect: str
        :param x_obs_expires: When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified.  This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3
        :type x_obs_expires: int
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
        self._success_action_redirect = None
        self._x_obs_expires = None
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
        if success_action_redirect is not None:
            self.success_action_redirect = success_action_redirect
        if x_obs_expires is not None:
            self.x_obs_expires = x_obs_expires

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetObjectMetadataRequest.

        Name of the bucket.

        :return: The bucket_name of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetObjectMetadataRequest.

        Name of the bucket.

        :param bucket_name: The bucket_name of this GetObjectMetadataRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this GetObjectMetadataRequest.

        Name of the object whose metadata will be returned.

        :return: The object_key of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this GetObjectMetadataRequest.

        Name of the object whose metadata will be returned.

        :param object_key: The object_key of this GetObjectMetadataRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        r"""Gets the date of this GetObjectMetadataRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetObjectMetadataRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this GetObjectMetadataRequest.
        :type date: str
        """
        self._date = date

    @property
    def version_id(self):
        r"""Gets the version_id of this GetObjectMetadataRequest.

        Version ID of the object.

        :return: The version_id of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this GetObjectMetadataRequest.

        Version ID of the object.

        :param version_id: The version_id of this GetObjectMetadataRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def origin(self):
        r"""Gets the origin of this GetObjectMetadataRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request).

        :return: The origin of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this GetObjectMetadataRequest.

        Origin (usually a domain name) specified by the pre-request (a cross-origin request).

        :param origin: The origin of this GetObjectMetadataRequest.
        :type origin: str
        """
        self._origin = origin

    @property
    def access_control_request_headers(self):
        r"""Gets the access_control_request_headers of this GetObjectMetadataRequest.

        HTTP headers that can be contained in a request.

        :return: The access_control_request_headers of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._access_control_request_headers

    @access_control_request_headers.setter
    def access_control_request_headers(self, access_control_request_headers):
        r"""Sets the access_control_request_headers of this GetObjectMetadataRequest.

        HTTP headers that can be contained in a request.

        :param access_control_request_headers: The access_control_request_headers of this GetObjectMetadataRequest.
        :type access_control_request_headers: str
        """
        self._access_control_request_headers = access_control_request_headers

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.

        The decryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.

        The decryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.

        Decryption key used for SSE-C.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        r"""Sets the x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.

        Decryption key used for SSE-C.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. An MD5 value is used to ensure that there is no error during the key transmission.Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. An MD5 value is used to ensure that there is no error during the key transmission.Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        r"""Gets the success_action_redirect of this GetObjectMetadataRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.

        :return: The success_action_redirect of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        r"""Sets the success_action_redirect of this GetObjectMetadataRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.

        :param success_action_redirect: The success_action_redirect of this GetObjectMetadataRequest.
        :type success_action_redirect: str
        """
        self._success_action_redirect = success_action_redirect

    @property
    def x_obs_expires(self):
        r"""Gets the x_obs_expires of this GetObjectMetadataRequest.

        When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified.  This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3

        :return: The x_obs_expires of this GetObjectMetadataRequest.
        :rtype: int
        """
        return self._x_obs_expires

    @x_obs_expires.setter
    def x_obs_expires(self, x_obs_expires):
        r"""Sets the x_obs_expires of this GetObjectMetadataRequest.

        When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified.  This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3

        :param x_obs_expires: The x_obs_expires of this GetObjectMetadataRequest.
        :type x_obs_expires: int
        """
        self._x_obs_expires = x_obs_expires

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
        if not isinstance(other, GetObjectMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
