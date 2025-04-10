# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyObjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CopyObjectRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'object_key': 'str',
        'x_obs_acl': 'str',
        'x_obs_grant_read': 'str',
        'x_obs_grant_read_acp': 'str',
        'x_obs_grant_write_acp': 'str',
        'x_obs_grant_full_control': 'str',
        'x_obs_copy_source': 'str',
        'x_obs_metadata_directive': 'str',
        'x_obs_copy_source_if_match': 'str',
        'x_obs_copy_source_if_none_match': 'str',
        'x_obs_copy_source_if_unmodified_since': 'str',
        'x_obs_copy_source_if_modified_since': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_persistent_headers': 'str',
        'x_obs_website_redirect_location': 'str',
        'x_obs_server_side_encryption': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
        'x_obs_server_side_encryption_customer_algorithm': 'str',
        'x_obs_server_side_encryption_customer_key': 'str',
        'x_obs_server_side_encryption_customer_key_md5': 'str',
        'x_obs_copy_source_server_side_encryption_customer_algorithm': 'str',
        'x_obs_copy_source_server_side_encryption_customer_key': 'str',
        'x_obs_copy_source_server_side_encryption_customer_key_md5': 'str',
        'success_action_redirect': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'object_key': 'object_key',
        'x_obs_acl': 'x-obs-acl',
        'x_obs_grant_read': 'x-obs-grant-read',
        'x_obs_grant_read_acp': 'x-obs-grant-read-acp',
        'x_obs_grant_write_acp': 'x-obs-grant-write-acp',
        'x_obs_grant_full_control': 'x-obs-grant-full-control',
        'x_obs_copy_source': 'x-obs-copy-source',
        'x_obs_metadata_directive': 'x-obs-metadata-directive',
        'x_obs_copy_source_if_match': 'x-obs-copy-source-if-match',
        'x_obs_copy_source_if_none_match': 'x-obs-copy-source-if-none-match',
        'x_obs_copy_source_if_unmodified_since': 'x-obs-copy-source-if-unmodified-since',
        'x_obs_copy_source_if_modified_since': 'x-obs-copy-source-if-modified-since',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_persistent_headers': 'x-obs-persistent-headers',
        'x_obs_website_redirect_location': 'x-obs-website-redirect-location',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'x_obs_server_side_encryption_customer_algorithm': 'x-obs-server-side-encryption-customer-algorithm',
        'x_obs_server_side_encryption_customer_key': 'x-obs-server-side-encryption-customer-key',
        'x_obs_server_side_encryption_customer_key_md5': 'x-obs-server-side-encryption-customer-key-MD5',
        'x_obs_copy_source_server_side_encryption_customer_algorithm': 'x-obs-copy-source-server-side-encryption-customer-algorithm',
        'x_obs_copy_source_server_side_encryption_customer_key': 'x-obs-copy-source-server-side-encryption-customer-key',
        'x_obs_copy_source_server_side_encryption_customer_key_md5': 'x-obs-copy-source-server-side-encryption-customer-key-MD5',
        'success_action_redirect': 'success_action_redirect'
    }

    def __init__(self, date=None, bucket_name=None, object_key=None, x_obs_acl=None, x_obs_grant_read=None, x_obs_grant_read_acp=None, x_obs_grant_write_acp=None, x_obs_grant_full_control=None, x_obs_copy_source=None, x_obs_metadata_directive=None, x_obs_copy_source_if_match=None, x_obs_copy_source_if_none_match=None, x_obs_copy_source_if_unmodified_since=None, x_obs_copy_source_if_modified_since=None, x_obs_storage_class=None, x_obs_persistent_headers=None, x_obs_website_redirect_location=None, x_obs_server_side_encryption=None, x_obs_server_side_encryption_kms_key_id=None, x_obs_server_side_encryption_customer_algorithm=None, x_obs_server_side_encryption_customer_key=None, x_obs_server_side_encryption_customer_key_md5=None, x_obs_copy_source_server_side_encryption_customer_algorithm=None, x_obs_copy_source_server_side_encryption_customer_key=None, x_obs_copy_source_server_side_encryption_customer_key_md5=None, success_action_redirect=None):
        r"""CopyObjectRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param object_key: Name of the object copy.
        :type object_key: str
        :param x_obs_acl: When copying the object, you can add this header to configure access control policies for the object. The frequently used predefined policies include **private**, **public-read**, and **public-read-write**. For more information, see the ACL configuration using header fields in the ACLs section. Example: x-obs-acl: acl
        :type x_obs_acl: str
        :param x_obs_grant_read: When creating an object, you can use this header to grant all users in a domain the permissions to read the object and obtain object metadata.
        :type x_obs_grant_read: str
        :param x_obs_grant_read_acp: When creating an object, you can use this header to grant all users in a domain the permissions to obtain the object ACL.
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: When creating an object, you can use this header to grant all users in a domain the permissions to write the object ACL.
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.
        :type x_obs_grant_full_control: str
        :param x_obs_copy_source: Indicates names of the source bucket and object in a copy request. If the source object has multiple versions, use the **versionId** parameter to specify an object version. Restriction: URL encoding is required for handling Chinese characters. Example: x-obs-copy-source: /source_bucket/sourceObject
        :type x_obs_copy_source: str
        :param x_obs_metadata_directive: Indicates whether the metadata of the target object is copied from the source object or replaced with the metadata provided in the request.  Valid values: **COPY** and **REPLACE**  Default value: **COPY**  Example: x-obs-metadata-directive: metadata_directive  Restriction: Values other than **COPY** or **REPLACE** result in an immediate 400-based error response. If you need to modify the metadata (for both the source and target objects), this parameter must be set to **REPLACE**, otherwise, the request is invalid and the server returns a 400 error. This parameter cannot change an encrypted object to a non-encrypted one (for both the source and target objects). If you use this parameter to change the encrypted object, OBS returns a 400 error.
        :type x_obs_metadata_directive: str
        :param x_obs_copy_source_if_match: Copies the source object only if its ETag matches the one specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-unmodified-since** but not other conditional copy parameters.
        :type x_obs_copy_source_if_match: str
        :param x_obs_copy_source_if_none_match: Copies the object only if its ETag does not match the one specified in this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-none-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-modified-since** but not other conditional copy parameters.
        :type x_obs_copy_source_if_none_match: str
        :param x_obs_copy_source_if_unmodified_since: Copies the source object only if it has not been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-unmodified -since: time-sta
        :type x_obs_copy_source_if_unmodified_since: str
        :param x_obs_copy_source_if_modified_since: Copies the source object only if it has been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-none-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-modified-since: time-sta
        :type x_obs_copy_source_if_modified_since: str
        :param x_obs_storage_class: When copying an object, you can use this header to specify a storage class for the target object. If you do not have this header configured, the target object inherits the default storage class of the bucket.  Type: string  Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.  Example: x-obs-storage-class: STANDARD
        :type x_obs_storage_class: str
        :param x_obs_persistent_headers: When copying an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the target object or query the object metadata, the custom headers will be returned in the response message.  Type: string  Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**  Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.  Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  When you download the target object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.  Restrictions:  + Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.  + Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.  + The total length of this header and the custom metadata cannot exceed 8 KB.  + If the same keys are transferred, values are separated with commas (,) and then returned in one key.  + If the source object already has custom response headers, such response headers will not be copied to the target object.
        :type x_obs_persistent_headers: str
        :param x_obs_website_redirect_location: If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.  Type: string  Default value: none  Restriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.
        :type x_obs_website_redirect_location: str
        :param x_obs_server_side_encryption: Indicates that SSE-KMS is used. The target object is encrypted using SSE-KMS.  Type: string  Example: x-obs-server-side-encryption: kms  This header is required when SSE-KMS is used.
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_encryption_kms_key_id: The master key ID used to encrypt the target object when SSE-KMS is used. If the customer does not provide this ID, the default master key ID will be used.  Type: string  Supported formats:  + *regionID***:***domainID***:key/***key_id*     + *key_id*.  *regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created on DEW.  Examples:  + x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0   + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0
        :type x_obs_server_side_encryption_kms_key_id: str
        :param x_obs_server_side_encryption_customer_algorithm: The algorithm used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: The key used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: The MD5 value of a key used to encrypt a target object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.  This header is required when SSE-C is used.
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param x_obs_copy_source_server_side_encryption_customer_algorithm: The algorithm used to decrypt the source object when SSE-C is used.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-copy-source-server-side-encryption-customer-key** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.
        :type x_obs_copy_source_server_side_encryption_customer_algorithm: str
        :param x_obs_copy_source_server_side_encryption_customer_key: The key used to decrypt the source object when SSE-C is used. This header decrypts the source object.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.
        :type x_obs_copy_source_server_side_encryption_customer_key: str
        :param x_obs_copy_source_server_side_encryption_customer_key_md5: The MD5 value of the key used to decrypt the source object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key**.  This header is required when SSE-C is used during the copy of the source object.
        :type x_obs_copy_source_server_side_encryption_customer_key_md5: str
        :param success_action_redirect: The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address. Type: string
        :type success_action_redirect: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._object_key = None
        self._x_obs_acl = None
        self._x_obs_grant_read = None
        self._x_obs_grant_read_acp = None
        self._x_obs_grant_write_acp = None
        self._x_obs_grant_full_control = None
        self._x_obs_copy_source = None
        self._x_obs_metadata_directive = None
        self._x_obs_copy_source_if_match = None
        self._x_obs_copy_source_if_none_match = None
        self._x_obs_copy_source_if_unmodified_since = None
        self._x_obs_copy_source_if_modified_since = None
        self._x_obs_storage_class = None
        self._x_obs_persistent_headers = None
        self._x_obs_website_redirect_location = None
        self._x_obs_server_side_encryption = None
        self._x_obs_server_side_encryption_kms_key_id = None
        self._x_obs_server_side_encryption_customer_algorithm = None
        self._x_obs_server_side_encryption_customer_key = None
        self._x_obs_server_side_encryption_customer_key_md5 = None
        self._x_obs_copy_source_server_side_encryption_customer_algorithm = None
        self._x_obs_copy_source_server_side_encryption_customer_key = None
        self._x_obs_copy_source_server_side_encryption_customer_key_md5 = None
        self._success_action_redirect = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.object_key = object_key
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
        self.x_obs_copy_source = x_obs_copy_source
        if x_obs_metadata_directive is not None:
            self.x_obs_metadata_directive = x_obs_metadata_directive
        if x_obs_copy_source_if_match is not None:
            self.x_obs_copy_source_if_match = x_obs_copy_source_if_match
        if x_obs_copy_source_if_none_match is not None:
            self.x_obs_copy_source_if_none_match = x_obs_copy_source_if_none_match
        if x_obs_copy_source_if_unmodified_since is not None:
            self.x_obs_copy_source_if_unmodified_since = x_obs_copy_source_if_unmodified_since
        if x_obs_copy_source_if_modified_since is not None:
            self.x_obs_copy_source_if_modified_since = x_obs_copy_source_if_modified_since
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
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
        if x_obs_copy_source_server_side_encryption_customer_algorithm is not None:
            self.x_obs_copy_source_server_side_encryption_customer_algorithm = x_obs_copy_source_server_side_encryption_customer_algorithm
        if x_obs_copy_source_server_side_encryption_customer_key is not None:
            self.x_obs_copy_source_server_side_encryption_customer_key = x_obs_copy_source_server_side_encryption_customer_key
        if x_obs_copy_source_server_side_encryption_customer_key_md5 is not None:
            self.x_obs_copy_source_server_side_encryption_customer_key_md5 = x_obs_copy_source_server_side_encryption_customer_key_md5
        if success_action_redirect is not None:
            self.success_action_redirect = success_action_redirect

    @property
    def date(self):
        r"""Gets the date of this CopyObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this CopyObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this CopyObjectRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this CopyObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CopyObjectRequest.

        Name of the requested bucket

        :return: The bucket_name of this CopyObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CopyObjectRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this CopyObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        r"""Gets the object_key of this CopyObjectRequest.

        Name of the object copy.

        :return: The object_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this CopyObjectRequest.

        Name of the object copy.

        :param object_key: The object_key of this CopyObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def x_obs_acl(self):
        r"""Gets the x_obs_acl of this CopyObjectRequest.

        When copying the object, you can add this header to configure access control policies for the object. The frequently used predefined policies include **private**, **public-read**, and **public-read-write**. For more information, see the ACL configuration using header fields in the ACLs section. Example: x-obs-acl: acl

        :return: The x_obs_acl of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        r"""Sets the x_obs_acl of this CopyObjectRequest.

        When copying the object, you can add this header to configure access control policies for the object. The frequently used predefined policies include **private**, **public-read**, and **public-read-write**. For more information, see the ACL configuration using header fields in the ACLs section. Example: x-obs-acl: acl

        :param x_obs_acl: The x_obs_acl of this CopyObjectRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_grant_read(self):
        r"""Gets the x_obs_grant_read of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object and obtain object metadata.

        :return: The x_obs_grant_read of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        r"""Sets the x_obs_grant_read of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object and obtain object metadata.

        :param x_obs_grant_read: The x_obs_grant_read of this CopyObjectRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_read_acp(self):
        r"""Gets the x_obs_grant_read_acp of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to obtain the object ACL.

        :return: The x_obs_grant_read_acp of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        r"""Sets the x_obs_grant_read_acp of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to obtain the object ACL.

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this CopyObjectRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        r"""Gets the x_obs_grant_write_acp of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to write the object ACL.

        :return: The x_obs_grant_write_acp of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        r"""Sets the x_obs_grant_write_acp of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to write the object ACL.

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this CopyObjectRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        r"""Gets the x_obs_grant_full_control of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.

        :return: The x_obs_grant_full_control of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        r"""Sets the x_obs_grant_full_control of this CopyObjectRequest.

        When creating an object, you can use this header to grant all users in a domain the permissions to read the object, to obtain the object metadata and ACL, and to write the object ACL.

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this CopyObjectRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_copy_source(self):
        r"""Gets the x_obs_copy_source of this CopyObjectRequest.

        Indicates names of the source bucket and object in a copy request. If the source object has multiple versions, use the **versionId** parameter to specify an object version. Restriction: URL encoding is required for handling Chinese characters. Example: x-obs-copy-source: /source_bucket/sourceObject

        :return: The x_obs_copy_source of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source

    @x_obs_copy_source.setter
    def x_obs_copy_source(self, x_obs_copy_source):
        r"""Sets the x_obs_copy_source of this CopyObjectRequest.

        Indicates names of the source bucket and object in a copy request. If the source object has multiple versions, use the **versionId** parameter to specify an object version. Restriction: URL encoding is required for handling Chinese characters. Example: x-obs-copy-source: /source_bucket/sourceObject

        :param x_obs_copy_source: The x_obs_copy_source of this CopyObjectRequest.
        :type x_obs_copy_source: str
        """
        self._x_obs_copy_source = x_obs_copy_source

    @property
    def x_obs_metadata_directive(self):
        r"""Gets the x_obs_metadata_directive of this CopyObjectRequest.

        Indicates whether the metadata of the target object is copied from the source object or replaced with the metadata provided in the request.  Valid values: **COPY** and **REPLACE**  Default value: **COPY**  Example: x-obs-metadata-directive: metadata_directive  Restriction: Values other than **COPY** or **REPLACE** result in an immediate 400-based error response. If you need to modify the metadata (for both the source and target objects), this parameter must be set to **REPLACE**, otherwise, the request is invalid and the server returns a 400 error. This parameter cannot change an encrypted object to a non-encrypted one (for both the source and target objects). If you use this parameter to change the encrypted object, OBS returns a 400 error.

        :return: The x_obs_metadata_directive of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_metadata_directive

    @x_obs_metadata_directive.setter
    def x_obs_metadata_directive(self, x_obs_metadata_directive):
        r"""Sets the x_obs_metadata_directive of this CopyObjectRequest.

        Indicates whether the metadata of the target object is copied from the source object or replaced with the metadata provided in the request.  Valid values: **COPY** and **REPLACE**  Default value: **COPY**  Example: x-obs-metadata-directive: metadata_directive  Restriction: Values other than **COPY** or **REPLACE** result in an immediate 400-based error response. If you need to modify the metadata (for both the source and target objects), this parameter must be set to **REPLACE**, otherwise, the request is invalid and the server returns a 400 error. This parameter cannot change an encrypted object to a non-encrypted one (for both the source and target objects). If you use this parameter to change the encrypted object, OBS returns a 400 error.

        :param x_obs_metadata_directive: The x_obs_metadata_directive of this CopyObjectRequest.
        :type x_obs_metadata_directive: str
        """
        self._x_obs_metadata_directive = x_obs_metadata_directive

    @property
    def x_obs_copy_source_if_match(self):
        r"""Gets the x_obs_copy_source_if_match of this CopyObjectRequest.

        Copies the source object only if its ETag matches the one specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-unmodified-since** but not other conditional copy parameters.

        :return: The x_obs_copy_source_if_match of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_match

    @x_obs_copy_source_if_match.setter
    def x_obs_copy_source_if_match(self, x_obs_copy_source_if_match):
        r"""Sets the x_obs_copy_source_if_match of this CopyObjectRequest.

        Copies the source object only if its ETag matches the one specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-unmodified-since** but not other conditional copy parameters.

        :param x_obs_copy_source_if_match: The x_obs_copy_source_if_match of this CopyObjectRequest.
        :type x_obs_copy_source_if_match: str
        """
        self._x_obs_copy_source_if_match = x_obs_copy_source_if_match

    @property
    def x_obs_copy_source_if_none_match(self):
        r"""Gets the x_obs_copy_source_if_none_match of this CopyObjectRequest.

        Copies the object only if its ETag does not match the one specified in this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-none-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-modified-since** but not other conditional copy parameters.

        :return: The x_obs_copy_source_if_none_match of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_none_match

    @x_obs_copy_source_if_none_match.setter
    def x_obs_copy_source_if_none_match(self, x_obs_copy_source_if_none_match):
        r"""Sets the x_obs_copy_source_if_none_match of this CopyObjectRequest.

        Copies the object only if its ETag does not match the one specified in this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned.  Example: x-obs-copy-source-if-none-match: etag  Restriction: This parameter can be used with **x-obs-copy-source-if-modified-since** but not other conditional copy parameters.

        :param x_obs_copy_source_if_none_match: The x_obs_copy_source_if_none_match of this CopyObjectRequest.
        :type x_obs_copy_source_if_none_match: str
        """
        self._x_obs_copy_source_if_none_match = x_obs_copy_source_if_none_match

    @property
    def x_obs_copy_source_if_unmodified_since(self):
        r"""Gets the x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.

        Copies the source object only if it has not been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-unmodified -since: time-sta

        :return: The x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_unmodified_since

    @x_obs_copy_source_if_unmodified_since.setter
    def x_obs_copy_source_if_unmodified_since(self, x_obs_copy_source_if_unmodified_since):
        r"""Sets the x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.

        Copies the source object only if it has not been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-unmodified -since: time-sta

        :param x_obs_copy_source_if_unmodified_since: The x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.
        :type x_obs_copy_source_if_unmodified_since: str
        """
        self._x_obs_copy_source_if_unmodified_since = x_obs_copy_source_if_unmodified_since

    @property
    def x_obs_copy_source_if_modified_since(self):
        r"""Gets the x_obs_copy_source_if_modified_since of this CopyObjectRequest.

        Copies the source object only if it has been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-none-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-modified-since: time-sta

        :return: The x_obs_copy_source_if_modified_since of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_modified_since

    @x_obs_copy_source_if_modified_since.setter
    def x_obs_copy_source_if_modified_since(self, x_obs_copy_source_if_modified_since):
        r"""Sets the x_obs_copy_source_if_modified_since of this CopyObjectRequest.

        Copies the source object only if it has been modified since the time specified by this header. Otherwise, a 412 HTTP status code error (failed precondition) is returned. This header can be used with **x-obs-copy-source-if-none-match**, but cannot be used with other conditional copy headers.  Type: HTTP time string complying with the format specified at **http://www.ietf.org/rfc/rfc2616.txt**  Example: x-obs-copy-source-if-modified-since: time-sta

        :param x_obs_copy_source_if_modified_since: The x_obs_copy_source_if_modified_since of this CopyObjectRequest.
        :type x_obs_copy_source_if_modified_since: str
        """
        self._x_obs_copy_source_if_modified_since = x_obs_copy_source_if_modified_since

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this CopyObjectRequest.

        When copying an object, you can use this header to specify a storage class for the target object. If you do not have this header configured, the target object inherits the default storage class of the bucket.  Type: string  Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.  Example: x-obs-storage-class: STANDARD

        :return: The x_obs_storage_class of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this CopyObjectRequest.

        When copying an object, you can use this header to specify a storage class for the target object. If you do not have this header configured, the target object inherits the default storage class of the bucket.  Type: string  Note: There are three storage classes: Standard (STANDARD), Infrequent Access (WARM), and Archive (COLD), so the value can be **STANDARD**, **WARM**, or **COLD**. The value is case sensitive.  Example: x-obs-storage-class: STANDARD

        :param x_obs_storage_class: The x_obs_storage_class of this CopyObjectRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_persistent_headers(self):
        r"""Gets the x_obs_persistent_headers of this CopyObjectRequest.

        When copying an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the target object or query the object metadata, the custom headers will be returned in the response message.  Type: string  Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**  Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.  Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  When you download the target object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.  Restrictions:  + Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.  + Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.  + The total length of this header and the custom metadata cannot exceed 8 KB.  + If the same keys are transferred, values are separated with commas (,) and then returned in one key.  + If the source object already has custom response headers, such response headers will not be copied to the target object.

        :return: The x_obs_persistent_headers of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_persistent_headers

    @x_obs_persistent_headers.setter
    def x_obs_persistent_headers(self, x_obs_persistent_headers):
        r"""Sets the x_obs_persistent_headers of this CopyObjectRequest.

        When copying an object, you can add the **x-obs-persistent-headers** header in an HTTP request to customize one or more response headers. When you retrieve the target object or query the object metadata, the custom headers will be returned in the response message.  Type: string  Format: **x-obs-persistent-headers: ****key1:base64_encode(***value1***),****key2:base64_encode(***value2***)...**  Note: Items, such as **key1** and **key2**, are user-defined headers. If they contain non-ASCII or unrecognizable characters, they can be encoded using URL or Base64. The server processes these headers as strings, but does not decode them. Items, such as *value1* and *value2* are the values of the corresponding headers. **base64_encode** indicates that the value is encoded using Base64. A user-defined header and its Base64-encoded value are connected using a colon (:) to form a key-value pair. All key-value pairs are separated with a comma (,) and are placed in the **x-obs-persistent-headers** header. The server then decodes the uploaded value.  Example: x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  When you download the target object or obtain the object metadata, headers **key1:***value1* and **key2:***value2* will be returned.  Restrictions:  + Response headers customized in this way cannot be prefixed with **x-obs-**. For example, you should use **key1**, instead of **x-obs-key1**.  + Standard HTTP headers, such as **host**, **content-md5**, **origin**, **range**, and **Content-Disposition**, cannot be specified as custom headers.  + The total length of this header and the custom metadata cannot exceed 8 KB.  + If the same keys are transferred, values are separated with commas (,) and then returned in one key.  + If the source object already has custom response headers, such response headers will not be copied to the target object.

        :param x_obs_persistent_headers: The x_obs_persistent_headers of this CopyObjectRequest.
        :type x_obs_persistent_headers: str
        """
        self._x_obs_persistent_headers = x_obs_persistent_headers

    @property
    def x_obs_website_redirect_location(self):
        r"""Gets the x_obs_website_redirect_location of this CopyObjectRequest.

        If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.  Type: string  Default value: none  Restriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.

        :return: The x_obs_website_redirect_location of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_website_redirect_location

    @x_obs_website_redirect_location.setter
    def x_obs_website_redirect_location(self, x_obs_website_redirect_location):
        r"""Sets the x_obs_website_redirect_location of this CopyObjectRequest.

        If static website hosting has been configured for a bucket, you can configure this parameter to redirect requests for an object in this bucket to another object in the same bucket or to an external URL. OBS stores the value of this header in the object metadata.  Type: string  Default value: none  Restriction: The value must start with a slash (/), **http://**, or **https://**, with a length of no more than 2 KB.

        :param x_obs_website_redirect_location: The x_obs_website_redirect_location of this CopyObjectRequest.
        :type x_obs_website_redirect_location: str
        """
        self._x_obs_website_redirect_location = x_obs_website_redirect_location

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this CopyObjectRequest.

        Indicates that SSE-KMS is used. The target object is encrypted using SSE-KMS.  Type: string  Example: x-obs-server-side-encryption: kms  This header is required when SSE-KMS is used.

        :return: The x_obs_server_side_encryption of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this CopyObjectRequest.

        Indicates that SSE-KMS is used. The target object is encrypted using SSE-KMS.  Type: string  Example: x-obs-server-side-encryption: kms  This header is required when SSE-KMS is used.

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this CopyObjectRequest.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.

        The master key ID used to encrypt the target object when SSE-KMS is used. If the customer does not provide this ID, the default master key ID will be used.  Type: string  Supported formats:  + *regionID***:***domainID***:key/***key_id*     + *key_id*.  *regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created on DEW.  Examples:  + x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0   + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0

        :return: The x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.

        The master key ID used to encrypt the target object when SSE-KMS is used. If the customer does not provide this ID, the default master key ID will be used.  Type: string  Supported formats:  + *regionID***:***domainID***:key/***key_id*     + *key_id*.  *regionID* is the ID of the region to which the key belongs. *domainID* is the account ID of the tenant to which the key belongs. *key_id* is the key ID created on DEW.  Examples:  + x-obs-server-side-encryption-kms-key-id:cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0   + x-obs-server-side-encryption-kms-key-id:4f1cd4de-ab64-4807-920a-47fc42e7f0d0

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        The algorithm used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.

        :return: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        The algorithm used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-server-side-encryption-customer-key** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_server_side_encryption_customer_key of this CopyObjectRequest.

        The key used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.

        :return: The x_obs_server_side_encryption_customer_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        r"""Sets the x_obs_server_side_encryption_customer_key of this CopyObjectRequest.

        The key used to encrypt a target object when SSE-C is used.  Type: string  Example: x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used.

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        The MD5 value of a key used to encrypt a target object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.  This header is required when SSE-C is used.

        :return: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        The MD5 value of a key used to encrypt a target object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-server-side-encryption-customer-algorithm** and **x-obs-server-side-encryption-customer-key**.  This header is required when SSE-C is used.

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def x_obs_copy_source_server_side_encryption_customer_algorithm(self):
        r"""Gets the x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        The algorithm used to decrypt the source object when SSE-C is used.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-copy-source-server-side-encryption-customer-key** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.

        :return: The x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_algorithm

    @x_obs_copy_source_server_side_encryption_customer_algorithm.setter
    def x_obs_copy_source_server_side_encryption_customer_algorithm(self, x_obs_copy_source_server_side_encryption_customer_algorithm):
        r"""Sets the x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        The algorithm used to decrypt the source object when SSE-C is used.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  Restriction: This header must be used together with **x-obs-copy-source-server-side-encryption-customer-key** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.

        :param x_obs_copy_source_server_side_encryption_customer_algorithm: The x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_algorithm = x_obs_copy_source_server_side_encryption_customer_algorithm

    @property
    def x_obs_copy_source_server_side_encryption_customer_key(self):
        r"""Gets the x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.

        The key used to decrypt the source object when SSE-C is used. This header decrypts the source object.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.

        :return: The x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_key

    @x_obs_copy_source_server_side_encryption_customer_key.setter
    def x_obs_copy_source_server_side_encryption_customer_key(self, x_obs_copy_source_server_side_encryption_customer_key):
        r"""Sets the x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.

        The key used to decrypt the source object when SSE-C is used. This header decrypts the source object.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  Restriction: This header is a Base64-encoded 256-bit key and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key-MD5**.  This header is required when SSE-C is used during the copy of the source object.

        :param x_obs_copy_source_server_side_encryption_customer_key: The x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_key: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_key = x_obs_copy_source_server_side_encryption_customer_key

    @property
    def x_obs_copy_source_server_side_encryption_customer_key_md5(self):
        r"""Gets the x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        The MD5 value of the key used to decrypt the source object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key**.  This header is required when SSE-C is used during the copy of the source object.

        :return: The x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_key_md5

    @x_obs_copy_source_server_side_encryption_customer_key_md5.setter
    def x_obs_copy_source_server_side_encryption_customer_key_md5(self, x_obs_copy_source_server_side_encryption_customer_key_md5):
        r"""Sets the x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        The MD5 value of the key used to decrypt the source object when SSE-C is used. An MD5 value is used to ensure that there is no error during the key transmission.  Type: string  Example: x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  Restriction: This header is a Base64-encoded 128-bit MD5 value and must be used together with **x-obs-copy-source-server-side-encryption-customer-algorithm** and **x-obs-copy-source-server-side-encryption-customer-key**.  This header is required when SSE-C is used during the copy of the source object.

        :param x_obs_copy_source_server_side_encryption_customer_key_md5: The x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_key_md5 = x_obs_copy_source_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        r"""Gets the success_action_redirect of this CopyObjectRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address. Type: string

        :return: The success_action_redirect of this CopyObjectRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        r"""Sets the success_action_redirect of this CopyObjectRequest.

        The address (a URL) which a successfully responded request is redirected to.  If this parameter value is valid and the request succeeds, OBS returns status code 303. The **Location** header consists of **success_action_redirect** as well as the bucket name, object name, and object ETag. If this parameter is invalid, OBS ignores this parameter and returns status code 204. In such case, the **Location** header is the object address. Type: string

        :param success_action_redirect: The success_action_redirect of this CopyObjectRequest.
        :type success_action_redirect: str
        """
        self._success_action_redirect = success_action_redirect

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
        if not isinstance(other, CopyObjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
