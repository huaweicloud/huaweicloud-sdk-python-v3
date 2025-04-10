# coding: utf-8

import six

from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutObjectRequest(SdkStreamRequest):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "PutObjectRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_key': 'str',
        'date': 'str',
        'content_md5': 'str',
        'x_obs_acl': 'str',
        'x_obs_grant_read': 'str',
        'x_obs_grant_read_acp': 'str',
        'x_obs_grant_write_acp': 'str',
        'x_obs_grant_full_control': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_meta_xxx': 'str',
        'x_obs_persistent_headers': 'str',
        'x_obs_website_redirect_location': 'str',
        'x_obs_server_side_encryption': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
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
        'content_md5': 'Content-MD5',
        'x_obs_acl': 'x-obs-acl',
        'x_obs_grant_read': 'x-obs-grant-read',
        'x_obs_grant_read_acp': 'x-obs-grant-read-acp',
        'x_obs_grant_write_acp': 'x-obs-grant-write-acp',
        'x_obs_grant_full_control': 'x-obs-grant-full-control',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_meta_xxx': 'x-obs-meta-xxx',
        'x_obs_persistent_headers': 'x-obs-persistent-headers',
        'x_obs_website_redirect_location': 'x-obs-website-redirect-location',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_server_side_encryption_customer_key': 'x-obs-server-side-encryption-customer-key',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'success_action_redirect': 'success-action-redirect',
        'x_obs_expires': 'x-obs-expires'
    }

    def __init__(self, stream=None, bucket_name=None, object_key=None, date=None, content_md5=None, x_obs_acl=None, x_obs_grant_read=None, x_obs_grant_read_acp=None, x_obs_grant_write_acp=None, x_obs_grant_full_control=None, x_obs_storage_class=None, x_obs_meta_xxx=None, x_obs_persistent_headers=None, x_obs_website_redirect_location=None, x_obs_server_side_encryption=None, x_obs_server_side_encryption_kms_key_id=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_server_side_encryption_customer_key=None, x_obs_server_side_encryption_customer_key_md5=None, success_action_redirect=None, x_obs_expires=None):
        r"""PutObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: Name of the bucket.
        :type bucket_name: str
        :param object_key: Object key for which this operation was initiated.
        :type object_key: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param content_md5: Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.  Example: n58IG6hfM7vqI4K0vnWpog&#x3D;&#x3D;
        :type content_md5: str
        :param x_obs_acl: When creating a bucket, you can add this header to configure access control policies (predefined policies) for the bucket.  Example: x-obs-acl: public-read
        :type x_obs_acl: str
        :param x_obs_grant_read: When creating an object, you can use this header to grant all users under a tenant the permissions to read the object and obtain the object metadata.  Example: x-obs-grant-read: id&#x3D;domainID. If multiple tenants are authorized, separate them with commas (,).
        :type x_obs_grant_read: str
        :param x_obs_grant_read_acp: When creating an object, you can use this header to grant all users under a tenant the permissions to obtain the object ACL.  Example: x-obs-grant-read-acp: id&#x3D;domainID. If multiple tenants are authorized, separate them with commas (,).
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: When creating an object, you can use this header to grant all users under a tenant the permissions to write the object ACL.  Example: x-obs-grant-write-acp: id&#x3D;domainID. If multiple tenants are authorized, separate them with commas (,).
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.  Example: x-obs-grant-full-control: id&#x3D;domainID. If multiple tenants are authorized, separate them with commas (,).
        :type x_obs_grant_full_control: str
        :param x_obs_storage_class: When creating an object, you can use this header to specify a storage class for the object. If you do not have this header configured, the object inherits the default storage class of the bucket.Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.Example: x-obs-storage-class: STANDARD
        :type x_obs_storage_class: str
        :param x_obs_meta_xxx: User-defined metadata.  Example: x-obs-meta-test: test metadata
        :type x_obs_meta_xxx: str
        :param x_obs_persistent_headers: When creating an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the object or query the object metadata, the custom headers will be returned in the response message.Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUyWhen you download the object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.Restrictions:+ Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.+ Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.+ The total length of this header and the custom metadata cannot exceed 8 KB.+ If the same keys are transferred, values are separated with commas (,) and then returned in one key.
        :type x_obs_persistent_headers: str
        :param x_obs_website_redirect_location: If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.Example of redirecting requests to another object in the bucket:x-obs-website-redirect-location:/anotherPage.htmlExample of redirecting requests to an external URL:x-obs-website-redirect-location:http://www.example.com/Default value: noneRestriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.
        :type x_obs_website_redirect_location: str
        :param x_obs_server_side_encryption: Indicates that SSE-KMS is used.   Example: x-obs-server-side-encryption: kms
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_encryption_kms_key_id: Master key ID. This header is used for encryption with SSE-KMS. If the customer does not provide the master key ID, the default master key ID will be used.Supported formats:+ *regionID***:***domainID***:key/***key_id* + *key_id**regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created in DEW.Examples:+ x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0
        :type x_obs_server_side_encryption_kms_key_id: str
        :param x_obs_server_side_encryption_customer_algorithm: The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: Encryption key used for SSE-C. This key is used to encrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param success_action_redirect: The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.
        :type success_action_redirect: str
        :param x_obs_expires: When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified. This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3
        :type x_obs_expires: int
        """
        super(PutObjectRequest, self).__init__(stream)
        

        self._bucket_name = None
        self._object_key = None
        self._date = None
        self._content_md5 = None
        self._x_obs_acl = None
        self._x_obs_grant_read = None
        self._x_obs_grant_read_acp = None
        self._x_obs_grant_write_acp = None
        self._x_obs_grant_full_control = None
        self._x_obs_storage_class = None
        self._x_obs_meta_xxx = None
        self._x_obs_persistent_headers = None
        self._x_obs_website_redirect_location = None
        self._x_obs_server_side_encryption = None
        self._x_obs_server_side_encryption_kms_key_id = None
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
        if content_md5 is not None:
            self.content_md5 = content_md5
        if x_obs_acl is not None:
            self.x_obs_acl = x_obs_acl
        if x_obs_grant_read is not None:
            self.x_obs_grant_read = x_obs_grant_read
        if x_obs_grant_read_acp is not None:
            self.x_obs_grant_read_acp = x_obs_grant_read_acp
        if x_obs_grant_write_acp is not None:
            self.x_obs_grant_write_acp = x_obs_grant_write_acp
        if x_obs_grant_full_control is not None:
            self.x_obs_grant_full_control = x_obs_grant_full_control
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_meta_xxx is not None:
            self.x_obs_meta_xxx = x_obs_meta_xxx
        if x_obs_persistent_headers is not None:
            self.x_obs_persistent_headers = x_obs_persistent_headers
        if x_obs_website_redirect_location is not None:
            self.x_obs_website_redirect_location = x_obs_website_redirect_location
        if x_obs_server_side_encryption is not None:
            self.x_obs_server_side_encryption = x_obs_server_side_encryption
        if x_obs_server_side_encryption_kms_key_id is not None:
            self.x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id
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
        r"""Gets the bucket_name of this PutObjectRequest.

        Name of the bucket.

        :return: The bucket_name of this PutObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this PutObjectRequest.

        Name of the bucket.

        :param bucket_name: The bucket_name of this PutObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this PutObjectRequest.

        Object key for which this operation was initiated.

        :return: The object_key of this PutObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this PutObjectRequest.

        Object key for which this operation was initiated.

        :param object_key: The object_key of this PutObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        r"""Gets the date of this PutObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this PutObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this PutObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this PutObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def content_md5(self):
        r"""Gets the content_md5 of this PutObjectRequest.

        Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.  Example: n58IG6hfM7vqI4K0vnWpog==

        :return: The content_md5 of this PutObjectRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        r"""Sets the content_md5 of this PutObjectRequest.

        Base64-encoded 128-bit MD5 digest of the message according to RFC 1864.  Example: n58IG6hfM7vqI4K0vnWpog==

        :param content_md5: The content_md5 of this PutObjectRequest.
        :type content_md5: str
        """
        self._content_md5 = content_md5

    @property
    def x_obs_acl(self):
        r"""Gets the x_obs_acl of this PutObjectRequest.

        When creating a bucket, you can add this header to configure access control policies (predefined policies) for the bucket.  Example: x-obs-acl: public-read

        :return: The x_obs_acl of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        r"""Sets the x_obs_acl of this PutObjectRequest.

        When creating a bucket, you can add this header to configure access control policies (predefined policies) for the bucket.  Example: x-obs-acl: public-read

        :param x_obs_acl: The x_obs_acl of this PutObjectRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_grant_read(self):
        r"""Gets the x_obs_grant_read of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to read the object and obtain the object metadata.  Example: x-obs-grant-read: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :return: The x_obs_grant_read of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        r"""Sets the x_obs_grant_read of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to read the object and obtain the object metadata.  Example: x-obs-grant-read: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :param x_obs_grant_read: The x_obs_grant_read of this PutObjectRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_read_acp(self):
        r"""Gets the x_obs_grant_read_acp of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to obtain the object ACL.  Example: x-obs-grant-read-acp: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :return: The x_obs_grant_read_acp of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        r"""Sets the x_obs_grant_read_acp of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to obtain the object ACL.  Example: x-obs-grant-read-acp: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this PutObjectRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        r"""Gets the x_obs_grant_write_acp of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to write the object ACL.  Example: x-obs-grant-write-acp: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :return: The x_obs_grant_write_acp of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        r"""Sets the x_obs_grant_write_acp of this PutObjectRequest.

        When creating an object, you can use this header to grant all users under a tenant the permissions to write the object ACL.  Example: x-obs-grant-write-acp: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this PutObjectRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        r"""Gets the x_obs_grant_full_control of this PutObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.  Example: x-obs-grant-full-control: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :return: The x_obs_grant_full_control of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        r"""Sets the x_obs_grant_full_control of this PutObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.  Example: x-obs-grant-full-control: id=domainID. If multiple tenants are authorized, separate them with commas (,).

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this PutObjectRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this PutObjectRequest.

        When creating an object, you can use this header to specify a storage class for the object. If you do not have this header configured, the object inherits the default storage class of the bucket.Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.Example: x-obs-storage-class: STANDARD

        :return: The x_obs_storage_class of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this PutObjectRequest.

        When creating an object, you can use this header to specify a storage class for the object. If you do not have this header configured, the object inherits the default storage class of the bucket.Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.Example: x-obs-storage-class: STANDARD

        :param x_obs_storage_class: The x_obs_storage_class of this PutObjectRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_meta_xxx(self):
        r"""Gets the x_obs_meta_xxx of this PutObjectRequest.

        User-defined metadata.  Example: x-obs-meta-test: test metadata

        :return: The x_obs_meta_xxx of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_meta_xxx

    @x_obs_meta_xxx.setter
    def x_obs_meta_xxx(self, x_obs_meta_xxx):
        r"""Sets the x_obs_meta_xxx of this PutObjectRequest.

        User-defined metadata.  Example: x-obs-meta-test: test metadata

        :param x_obs_meta_xxx: The x_obs_meta_xxx of this PutObjectRequest.
        :type x_obs_meta_xxx: str
        """
        self._x_obs_meta_xxx = x_obs_meta_xxx

    @property
    def x_obs_persistent_headers(self):
        r"""Gets the x_obs_persistent_headers of this PutObjectRequest.

        When creating an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the object or query the object metadata, the custom headers will be returned in the response message.Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUyWhen you download the object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.Restrictions:+ Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.+ Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.+ The total length of this header and the custom metadata cannot exceed 8 KB.+ If the same keys are transferred, values are separated with commas (,) and then returned in one key.

        :return: The x_obs_persistent_headers of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_persistent_headers

    @x_obs_persistent_headers.setter
    def x_obs_persistent_headers(self, x_obs_persistent_headers):
        r"""Sets the x_obs_persistent_headers of this PutObjectRequest.

        When creating an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the object or query the object metadata, the custom headers will be returned in the response message.Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUyWhen you download the object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.Restrictions:+ Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.+ Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.+ The total length of this header and the custom metadata cannot exceed 8 KB.+ If the same keys are transferred, values are separated with commas (,) and then returned in one key.

        :param x_obs_persistent_headers: The x_obs_persistent_headers of this PutObjectRequest.
        :type x_obs_persistent_headers: str
        """
        self._x_obs_persistent_headers = x_obs_persistent_headers

    @property
    def x_obs_website_redirect_location(self):
        r"""Gets the x_obs_website_redirect_location of this PutObjectRequest.

        If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.Example of redirecting requests to another object in the bucket:x-obs-website-redirect-location:/anotherPage.htmlExample of redirecting requests to an external URL:x-obs-website-redirect-location:http://www.example.com/Default value: noneRestriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.

        :return: The x_obs_website_redirect_location of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_website_redirect_location

    @x_obs_website_redirect_location.setter
    def x_obs_website_redirect_location(self, x_obs_website_redirect_location):
        r"""Sets the x_obs_website_redirect_location of this PutObjectRequest.

        If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.Example of redirecting requests to another object in the bucket:x-obs-website-redirect-location:/anotherPage.htmlExample of redirecting requests to an external URL:x-obs-website-redirect-location:http://www.example.com/Default value: noneRestriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.

        :param x_obs_website_redirect_location: The x_obs_website_redirect_location of this PutObjectRequest.
        :type x_obs_website_redirect_location: str
        """
        self._x_obs_website_redirect_location = x_obs_website_redirect_location

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this PutObjectRequest.

        Indicates that SSE-KMS is used.   Example: x-obs-server-side-encryption: kms

        :return: The x_obs_server_side_encryption of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this PutObjectRequest.

        Indicates that SSE-KMS is used.   Example: x-obs-server-side-encryption: kms

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this PutObjectRequest.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.

        Master key ID. This header is used for encryption with SSE-KMS. If the customer does not provide the master key ID, the default master key ID will be used.Supported formats:+ *regionID***:***domainID***:key/***key_id* + *key_id**regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created in DEW.Examples:+ x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0

        :return: The x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.

        Master key ID. This header is used for encryption with SSE-KMS. If the customer does not provide the master key ID, the default master key ID will be used.Supported formats:+ *regionID***:***domainID***:key/***key_id* + *key_id**regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created in DEW.Examples:+ x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.

        The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.

        The encryption algorithm used for SSE-C.Example: x-obs-server-side-encryption-customer-algorithm:AES256Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_server_side_encryption_customer_key of this PutObjectRequest.

        Encryption key used for SSE-C. This key is used to encrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :return: The x_obs_server_side_encryption_customer_key of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        r"""Sets the x_obs_server_side_encryption_customer_key of this PutObjectRequest.

        Encryption key used for SSE-C. This key is used to encrypt objects.Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.

        MD5 value of the key used to encrypt objects in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key. Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        r"""Gets the success_action_redirect of this PutObjectRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.

        :return: The success_action_redirect of this PutObjectRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        r"""Sets the success_action_redirect of this PutObjectRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address.

        :param success_action_redirect: The success_action_redirect of this PutObjectRequest.
        :type success_action_redirect: str
        """
        self._success_action_redirect = success_action_redirect

    @property
    def x_obs_expires(self):
        r"""Gets the x_obs_expires of this PutObjectRequest.

        When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified. This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3

        :return: The x_obs_expires of this PutObjectRequest.
        :rtype: int
        """
        return self._x_obs_expires

    @x_obs_expires.setter
    def x_obs_expires(self, x_obs_expires):
        r"""Sets the x_obs_expires of this PutObjectRequest.

        When an object expires. It is measured in days. An object will be automatically deleted once it expires. The expiration is calculated from when the object was last modified. This header can be only configured during the object upload, and cannot be modified later by using the metadata API.  Example: x-obs-expires:3

        :param x_obs_expires: The x_obs_expires of this PutObjectRequest.
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
        if not isinstance(other, PutObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
