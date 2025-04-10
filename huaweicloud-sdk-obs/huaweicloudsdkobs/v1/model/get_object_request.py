# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetObjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetObjectRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_key': 'str',
        'date': 'str',
        'response_content_type': 'str',
        'response_content_language': 'str',
        'response_expires': 'str',
        'response_cache_control': 'str',
        'response_content_disposition': 'str',
        'response_content_encoding': 'str',
        'version_id': 'str',
        'x_image_process': 'str',
        'attname': 'str',
        'range': 'str',
        'if_modified_since': 'str',
        'if_unmodified_since': 'str',
        'if_match': 'str',
        'if_none_match': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_server_side_encryption_customer_key': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'date': 'Date',
        'response_content_type': 'response-content-type',
        'response_content_language': 'response-content-language',
        'response_expires': 'response-expires',
        'response_cache_control': 'response-cache-control',
        'response_content_disposition': 'response-content-disposition',
        'response_content_encoding': 'response-content-encoding',
        'version_id': 'versionId',
        'x_image_process': 'x-image-process',
        'attname': 'attname',
        'range': 'Range',
        'if_modified_since': 'If-Modified-Since',
        'if_unmodified_since': 'If-Unmodified-Since',
        'if_match': 'If-Match',
        'if_none_match': 'If-None-Match',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_server_side_encryption_customer_key': 'x-obs-server-side-encryption-customer-key',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5'
    }

    def __init__(self, bucket_name=None, object_key=None, date=None, response_content_type=None, response_content_language=None, response_expires=None, response_cache_control=None, response_content_disposition=None, response_content_encoding=None, version_id=None, x_image_process=None, attname=None, range=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_server_side_encryption_customer_key=None, x_obs_server_side_encryption_customer_key_md5=None):
        r"""GetObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: Name of the bucket.
        :type bucket_name: str
        :param object_key: Object key for which this operation was initiated.
        :type object_key: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param response_content_type: Overrides the **Content-Type** header in the response.
        :type response_content_type: str
        :param response_content_language: Overrides the **Content-Language** header in the response.
        :type response_content_language: str
        :param response_expires: Overrides the **Expires** header in the response.
        :type response_expires: str
        :param response_cache_control: Overrides the **Cache-Control** header in the response.
        :type response_cache_control: str
        :param response_content_disposition: Overrides the **Content-Disposition** header in the response.  Example: response-content-disposition&#x3D;attachment; filename*&#x3D;utf-8&#39;&#39;name1  In this example, the downloaded object is renamed **name1**. If **name1** contains Chinese characters, the Chinese characters must be URL-encoded.
        :type response_content_disposition: str
        :param response_content_encoding: Overrides the **Content-Encoding** header in the response.
        :type response_content_encoding: str
        :param version_id: Version ID of the object you want to download.
        :type version_id: str
        :param x_image_process: Image processing service.Examples:Command: x-image-process&#x3D;image/commandsStyle: x-image-process&#x3D;style/stylenameFor details, see the [Image Processing Feature Guide](https://support.huaweicloud.com/intl/en-us/fg-obs/obs_01_0001.html).
        :type x_image_process: str
        :param attname: Overrides the **Content-Disposition** header in the response.  Example: attname&#x3D;name1  The downloaded object is renamed **name1**.
        :type attname: str
        :param range: Obtains the content within the scope defined by **Range**. If the **Range** header is invalid, the entire object is obtained.**Range** consists of a start value and an end value. Its start value is mandatory and ranges from 0 to the object length minus 1. If **Range** contains only a start value, the object content from the start value to the default maximum start value is obtained.With the **Range** header carried, the ETag in the response is still the ETag of the object, instead of that of the object content defined by the **Range** header.bytes&#x3D;byte_rangeExample 1: bytes&#x3D;0-4Example 2: bytes&#x3D;1024Example 3: bytes&#x3D;10-20,30-40 (multiple ranges)
        :type range: str
        :param if_modified_since: Returns the object only if it has been modified since the time specified in the request, or **304 Not Modified** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**
        :type if_modified_since: str
        :param if_unmodified_since: Returns the object only if it has not been modified since the time specified in the request, or **412 Precondition Failed** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**
        :type if_unmodified_since: str
        :param if_match: Returns the object only if its ETag is the same as the one specified in the request, or **412 Precondition Failed** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)
        :type if_match: str
        :param if_none_match: Returns the object only if its ETag is different from the one specified in the request, or **304 Not Modified** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)
        :type if_none_match: str
        :param x_obs_server_side_encryption_customer_algorithm: The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: Encryption key used for SSE-C. This key is used to decrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        
        

        self._bucket_name = None
        self._object_key = None
        self._date = None
        self._response_content_type = None
        self._response_content_language = None
        self._response_expires = None
        self._response_cache_control = None
        self._response_content_disposition = None
        self._response_content_encoding = None
        self._version_id = None
        self._x_image_process = None
        self._attname = None
        self._range = None
        self._if_modified_since = None
        self._if_unmodified_since = None
        self._if_match = None
        self._if_none_match = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_server_side_encryption_customer_key = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.object_key = object_key
        if date is not None:
            self.date = date
        if response_content_type is not None:
            self.response_content_type = response_content_type
        if response_content_language is not None:
            self.response_content_language = response_content_language
        if response_expires is not None:
            self.response_expires = response_expires
        if response_cache_control is not None:
            self.response_cache_control = response_cache_control
        if response_content_disposition is not None:
            self.response_content_disposition = response_content_disposition
        if response_content_encoding is not None:
            self.response_content_encoding = response_content_encoding
        if version_id is not None:
            self.version_id = version_id
        if x_image_process is not None:
            self.x_image_process = x_image_process
        if attname is not None:
            self.attname = attname
        if range is not None:
            self.range = range
        if if_modified_since is not None:
            self.if_modified_since = if_modified_since
        if if_unmodified_since is not None:
            self.if_unmodified_since = if_unmodified_since
        if if_match is not None:
            self.if_match = if_match
        if if_none_match is not None:
            self.if_none_match = if_none_match
        if x_obs_server_side_encryption_customer_algorithm is not None:
            self.x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm
        if x_obs_server_side_encryption_customer_key is not None:
            self.x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key
        if x_obs_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetObjectRequest.

        Name of the bucket.

        :return: The bucket_name of this GetObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetObjectRequest.

        Name of the bucket.

        :param bucket_name: The bucket_name of this GetObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this GetObjectRequest.

        Object key for which this operation was initiated.

        :return: The object_key of this GetObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this GetObjectRequest.

        Object key for which this operation was initiated.

        :param object_key: The object_key of this GetObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        r"""Gets the date of this GetObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this GetObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this GetObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def response_content_type(self):
        r"""Gets the response_content_type of this GetObjectRequest.

        Overrides the **Content-Type** header in the response.

        :return: The response_content_type of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_type

    @response_content_type.setter
    def response_content_type(self, response_content_type):
        r"""Sets the response_content_type of this GetObjectRequest.

        Overrides the **Content-Type** header in the response.

        :param response_content_type: The response_content_type of this GetObjectRequest.
        :type response_content_type: str
        """
        self._response_content_type = response_content_type

    @property
    def response_content_language(self):
        r"""Gets the response_content_language of this GetObjectRequest.

        Overrides the **Content-Language** header in the response.

        :return: The response_content_language of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_language

    @response_content_language.setter
    def response_content_language(self, response_content_language):
        r"""Sets the response_content_language of this GetObjectRequest.

        Overrides the **Content-Language** header in the response.

        :param response_content_language: The response_content_language of this GetObjectRequest.
        :type response_content_language: str
        """
        self._response_content_language = response_content_language

    @property
    def response_expires(self):
        r"""Gets the response_expires of this GetObjectRequest.

        Overrides the **Expires** header in the response.

        :return: The response_expires of this GetObjectRequest.
        :rtype: str
        """
        return self._response_expires

    @response_expires.setter
    def response_expires(self, response_expires):
        r"""Sets the response_expires of this GetObjectRequest.

        Overrides the **Expires** header in the response.

        :param response_expires: The response_expires of this GetObjectRequest.
        :type response_expires: str
        """
        self._response_expires = response_expires

    @property
    def response_cache_control(self):
        r"""Gets the response_cache_control of this GetObjectRequest.

        Overrides the **Cache-Control** header in the response.

        :return: The response_cache_control of this GetObjectRequest.
        :rtype: str
        """
        return self._response_cache_control

    @response_cache_control.setter
    def response_cache_control(self, response_cache_control):
        r"""Sets the response_cache_control of this GetObjectRequest.

        Overrides the **Cache-Control** header in the response.

        :param response_cache_control: The response_cache_control of this GetObjectRequest.
        :type response_cache_control: str
        """
        self._response_cache_control = response_cache_control

    @property
    def response_content_disposition(self):
        r"""Gets the response_content_disposition of this GetObjectRequest.

        Overrides the **Content-Disposition** header in the response.  Example: response-content-disposition=attachment; filename*=utf-8''name1  In this example, the downloaded object is renamed **name1**. If **name1** contains Chinese characters, the Chinese characters must be URL-encoded.

        :return: The response_content_disposition of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_disposition

    @response_content_disposition.setter
    def response_content_disposition(self, response_content_disposition):
        r"""Sets the response_content_disposition of this GetObjectRequest.

        Overrides the **Content-Disposition** header in the response.  Example: response-content-disposition=attachment; filename*=utf-8''name1  In this example, the downloaded object is renamed **name1**. If **name1** contains Chinese characters, the Chinese characters must be URL-encoded.

        :param response_content_disposition: The response_content_disposition of this GetObjectRequest.
        :type response_content_disposition: str
        """
        self._response_content_disposition = response_content_disposition

    @property
    def response_content_encoding(self):
        r"""Gets the response_content_encoding of this GetObjectRequest.

        Overrides the **Content-Encoding** header in the response.

        :return: The response_content_encoding of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_encoding

    @response_content_encoding.setter
    def response_content_encoding(self, response_content_encoding):
        r"""Sets the response_content_encoding of this GetObjectRequest.

        Overrides the **Content-Encoding** header in the response.

        :param response_content_encoding: The response_content_encoding of this GetObjectRequest.
        :type response_content_encoding: str
        """
        self._response_content_encoding = response_content_encoding

    @property
    def version_id(self):
        r"""Gets the version_id of this GetObjectRequest.

        Version ID of the object you want to download.

        :return: The version_id of this GetObjectRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this GetObjectRequest.

        Version ID of the object you want to download.

        :param version_id: The version_id of this GetObjectRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def x_image_process(self):
        r"""Gets the x_image_process of this GetObjectRequest.

        Image processing service.Examples:Command: x-image-process=image/commandsStyle: x-image-process=style/stylenameFor details, see the [Image Processing Feature Guide](https://support.huaweicloud.com/intl/en-us/fg-obs/obs_01_0001.html).

        :return: The x_image_process of this GetObjectRequest.
        :rtype: str
        """
        return self._x_image_process

    @x_image_process.setter
    def x_image_process(self, x_image_process):
        r"""Sets the x_image_process of this GetObjectRequest.

        Image processing service.Examples:Command: x-image-process=image/commandsStyle: x-image-process=style/stylenameFor details, see the [Image Processing Feature Guide](https://support.huaweicloud.com/intl/en-us/fg-obs/obs_01_0001.html).

        :param x_image_process: The x_image_process of this GetObjectRequest.
        :type x_image_process: str
        """
        self._x_image_process = x_image_process

    @property
    def attname(self):
        r"""Gets the attname of this GetObjectRequest.

        Overrides the **Content-Disposition** header in the response.  Example: attname=name1  The downloaded object is renamed **name1**.

        :return: The attname of this GetObjectRequest.
        :rtype: str
        """
        return self._attname

    @attname.setter
    def attname(self, attname):
        r"""Sets the attname of this GetObjectRequest.

        Overrides the **Content-Disposition** header in the response.  Example: attname=name1  The downloaded object is renamed **name1**.

        :param attname: The attname of this GetObjectRequest.
        :type attname: str
        """
        self._attname = attname

    @property
    def range(self):
        r"""Gets the range of this GetObjectRequest.

        Obtains the content within the scope defined by **Range**. If the **Range** header is invalid, the entire object is obtained.**Range** consists of a start value and an end value. Its start value is mandatory and ranges from 0 to the object length minus 1. If **Range** contains only a start value, the object content from the start value to the default maximum start value is obtained.With the **Range** header carried, the ETag in the response is still the ETag of the object, instead of that of the object content defined by the **Range** header.bytes=byte_rangeExample 1: bytes=0-4Example 2: bytes=1024Example 3: bytes=10-20,30-40 (multiple ranges)

        :return: The range of this GetObjectRequest.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this GetObjectRequest.

        Obtains the content within the scope defined by **Range**. If the **Range** header is invalid, the entire object is obtained.**Range** consists of a start value and an end value. Its start value is mandatory and ranges from 0 to the object length minus 1. If **Range** contains only a start value, the object content from the start value to the default maximum start value is obtained.With the **Range** header carried, the ETag in the response is still the ETag of the object, instead of that of the object content defined by the **Range** header.bytes=byte_rangeExample 1: bytes=0-4Example 2: bytes=1024Example 3: bytes=10-20,30-40 (multiple ranges)

        :param range: The range of this GetObjectRequest.
        :type range: str
        """
        self._range = range

    @property
    def if_modified_since(self):
        r"""Gets the if_modified_since of this GetObjectRequest.

        Returns the object only if it has been modified since the time specified in the request, or **304 Not Modified** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**

        :return: The if_modified_since of this GetObjectRequest.
        :rtype: str
        """
        return self._if_modified_since

    @if_modified_since.setter
    def if_modified_since(self, if_modified_since):
        r"""Sets the if_modified_since of this GetObjectRequest.

        Returns the object only if it has been modified since the time specified in the request, or **304 Not Modified** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**

        :param if_modified_since: The if_modified_since of this GetObjectRequest.
        :type if_modified_since: str
        """
        self._if_modified_since = if_modified_since

    @property
    def if_unmodified_since(self):
        r"""Gets the if_unmodified_since of this GetObjectRequest.

        Returns the object only if it has not been modified since the time specified in the request, or **412 Precondition Failed** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**

        :return: The if_unmodified_since of this GetObjectRequest.
        :rtype: str
        """
        return self._if_unmodified_since

    @if_unmodified_since.setter
    def if_unmodified_since(self, if_unmodified_since):
        r"""Sets the if_unmodified_since of this GetObjectRequest.

        Returns the object only if it has not been modified since the time specified in the request, or **412 Precondition Failed** is returned.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**

        :param if_unmodified_since: The if_unmodified_since of this GetObjectRequest.
        :type if_unmodified_since: str
        """
        self._if_unmodified_since = if_unmodified_since

    @property
    def if_match(self):
        r"""Gets the if_match of this GetObjectRequest.

        Returns the object only if its ETag is the same as the one specified in the request, or **412 Precondition Failed** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)

        :return: The if_match of this GetObjectRequest.
        :rtype: str
        """
        return self._if_match

    @if_match.setter
    def if_match(self, if_match):
        r"""Sets the if_match of this GetObjectRequest.

        Returns the object only if its ETag is the same as the one specified in the request, or **412 Precondition Failed** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)

        :param if_match: The if_match of this GetObjectRequest.
        :type if_match: str
        """
        self._if_match = if_match

    @property
    def if_none_match(self):
        r"""Gets the if_none_match of this GetObjectRequest.

        Returns the object only if its ETag is different from the one specified in the request, or **304 Not Modified** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)

        :return: The if_none_match of this GetObjectRequest.
        :rtype: str
        """
        return self._if_none_match

    @if_none_match.setter
    def if_none_match(self, if_none_match):
        r"""Sets the if_none_match of this GetObjectRequest.

        Returns the object only if its ETag is different from the one specified in the request, or **304 Not Modified** is returned.  (ETag example: 0f64741bf7cb1089e988e4585d0d3434)

        :param if_none_match: The if_none_match of this GetObjectRequest.
        :type if_none_match: str
        """
        self._if_none_match = if_none_match

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.

        The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.

        The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_server_side_encryption_customer_key of this GetObjectRequest.

        Encryption key used for SSE-C. This key is used to decrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_key of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        r"""Sets the x_obs_server_side_encryption_customer_key of this GetObjectRequest.

        Encryption key used for SSE-C. This key is used to decrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this GetObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

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
        if not isinstance(other, GetObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
