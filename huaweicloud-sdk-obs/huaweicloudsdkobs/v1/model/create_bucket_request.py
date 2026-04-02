# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBucketRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CreateBucketRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'date': 'str',
        'x_obs_acl': 'str',
        'x_obs_server_side_encryption': 'str',
        'x_obs_server_side_data_encryption': 'str',
        'x_obs_server_side_encryption_kms_key_id': 'str',
        'x_obs_server_side_encryption_bucket_key_enabled': 'str',
        'x_obs_sse_kms_key_project_id': 'str',
        'x_obs_bucket_object_lock_enabled': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_grant_read': 'str',
        'x_obs_grant_write': 'str',
        'x_obs_grant_read_acp': 'str',
        'x_obs_grant_write_acp': 'str',
        'x_obs_grant_full_control': 'str',
        'x_obs_grant_read_delivered': 'str',
        'x_obs_grant_full_control_delivered': 'str',
        'x_obs_az_redundancy': 'str',
        'x_obs_fs_file_interface': 'str',
        'x_obs_epid': 'str',
        'x_obs_ies_location': 'str',
        'body': 'CreateBucketRequestBody'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'date': 'Date',
        'x_obs_acl': 'x-obs-acl',
        'x_obs_server_side_encryption': 'x-obs-server-side-encryption',
        'x_obs_server_side_data_encryption': 'x-obs-server-side-data-encryption',
        'x_obs_server_side_encryption_kms_key_id': 'x-obs-server-side-encryption-kms-key-id',
        'x_obs_server_side_encryption_bucket_key_enabled': 'x-obs-server-side-encryption-bucket-key-enabled',
        'x_obs_sse_kms_key_project_id': 'x-obs-sse-kms-key-project-id',
        'x_obs_bucket_object_lock_enabled': 'x-obs-bucket-object-lock-enabled',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_grant_read': 'x-obs-grant-read',
        'x_obs_grant_write': 'x-obs-grant-write',
        'x_obs_grant_read_acp': 'x-obs-grant-read-acp',
        'x_obs_grant_write_acp': 'x-obs-grant-write-acp',
        'x_obs_grant_full_control': 'x-obs-grant-full-control',
        'x_obs_grant_read_delivered': 'x-obs-grant-read-delivered',
        'x_obs_grant_full_control_delivered': 'x-obs-grant-full-control-delivered',
        'x_obs_az_redundancy': 'x-obs-az-redundancy',
        'x_obs_fs_file_interface': 'x-obs-fs-file-interface',
        'x_obs_epid': 'x-obs-epid',
        'x_obs_ies_location': 'x-obs-ies-location',
        'body': 'body'
    }

    def __init__(self, bucket_name=None, date=None, x_obs_acl=None, x_obs_server_side_encryption=None, x_obs_server_side_data_encryption=None, x_obs_server_side_encryption_kms_key_id=None, x_obs_server_side_encryption_bucket_key_enabled=None, x_obs_sse_kms_key_project_id=None, x_obs_bucket_object_lock_enabled=None, x_obs_storage_class=None, x_obs_grant_read=None, x_obs_grant_write=None, x_obs_grant_read_acp=None, x_obs_grant_write_acp=None, x_obs_grant_full_control=None, x_obs_grant_read_delivered=None, x_obs_grant_full_control_delivered=None, x_obs_az_redundancy=None, x_obs_fs_file_interface=None, x_obs_epid=None, x_obs_ies_location=None, body=None):
        r"""CreateBucketRequest

        The model defined in huaweicloud sdk

        :param bucket_name: A bucket name is part of the access domain name and needs to be resolved. The bucket name must conform to the DNS domain naming rules. When receiving a bucket creation request, OBS strictly checks the bucket name based on the following rules: + A bucket name must be unique across all accounts and regions. + The name of a deleted bucket can be reused for another bucket or a parallel file system at least 30 minutes later after the deletion. + A bucket name must be 3 to 63 characters long. Only lowercase letters, digits, hyphens (-), and periods (.) are allowed. + A bucket name cannot start or end with a period (.) or hyphen (-), and cannot contain two consecutive periods (..) or contain a period (.) and a hyphen (-) adjacent to each other. + A bucket name cannot be formatted as an IP address. Note: The SSL wildcard certificate matches only buckets without periods (.) in their names when HTTPS is used for OBS access. If you use a bucket with periods (.) in its name to access OBS, the client will display a message indicating that the bucket is risky, for example, a red alarm may be displayed in the browser security prompt. We recommend that you avoid using periods (.) in bucket names.
        :type bucket_name: str
        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param x_obs_acl: When creating a bucket, you can add this header to configure access control policies (predefined common policies) for a bucket. Such policies include **private**, **public-read**, **public-read-write**, **public-read-delivered**, **public-read-write-delivered**, and **bucket-owner-full-control**. For details about each policy, see the ACL configuration using headers in section ACLs.
        :type x_obs_acl: str
        :param x_obs_server_side_encryption: When creating a bucket, you can use this header to specify an encryption method for the bucket.  Example: x-obs-server-side-encryption: kms
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_data_encryption: When creating a bucket, you can use this header to specify an encryption algorithm for server-side encryption. Example: x-obs-server-side-data-encryption: AES256
        :type x_obs_server_side_data_encryption: str
        :param x_obs_server_side_encryption_kms_key_id: ID of a specified key used for SSE-KMS encryption. For details about how to obtain a key ID Constraints: This header can only be used when you specify kms for the x-obs-server-side-encryption header.
        :type x_obs_server_side_encryption_kms_key_id: str
        :param x_obs_server_side_encryption_bucket_key_enabled: Whether to enable the SSE-KMS bucket key feature. Constraints: If you set this header to true, you must also specify x-obs-server-side-encryption-kms-key-id to specify the key ID.
        :type x_obs_server_side_encryption_bucket_key_enabled: str
        :param x_obs_sse_kms_key_project_id: ID of the project (not an enterprise project) where the KMS CMK belongs when SSE-KMS is used
        :type x_obs_sse_kms_key_project_id: str
        :param x_obs_bucket_object_lock_enabled: When creating a bucket, you can use this header to enable WORM for the bucket. Example: x-obs-bucket-object-lock-enabled:true
        :type x_obs_bucket_object_lock_enabled: str
        :param x_obs_storage_class: When creating a bucket, you can add this header to configure a default storage class for a bucket. The storage classes include Standard (STANDARD), Infrequent Access (WARM), Archive (COLD), and Deep Archive storage (DEEP_ARCHIVE). If this header is not included, the bucket is created in the Standard storage class.
        :type x_obs_storage_class: str
        :param x_obs_grant_read: Grants the read permission to all users under an account. The read permission allows you to list objects, multipart uploads, and object versions in a bucket, as well as to obtain bucket metadata.
        :type x_obs_grant_read: str
        :param x_obs_grant_write: Grants the write permission to all users under an account. The write permission allows you to create, delete, or overwrite all objects in a bucket, and to initialize, upload, copy, and merge parts, as well as to cancel multipart uploads.
        :type x_obs_grant_write: str
        :param x_obs_grant_read_acp: Grants the ACL read permission to all users under an account. The ACL read permission allows you to read the bucket ACL.
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: Grants the ACL write permission to all users under an account. The ACL write permission allows you to modify the bucket ACL.
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: Grants the full control access to all users under an account.
        :type x_obs_grant_full_control: str
        :param x_obs_grant_read_delivered: Grants the read permission to all users under an account. By default, the read permission is applied to all objects in the bucket.
        :type x_obs_grant_read_delivered: str
        :param x_obs_grant_full_control_delivered: Grants the full control access to all users under an account. By default, the full control access is applied to all objects in the bucket.
        :type x_obs_grant_full_control_delivered: str
        :param x_obs_az_redundancy: Add this header in a bucket creation request to enable the multi-AZ storage for the bucket. If this header is not carried, single-AZ storage is used for the bucket by default. If the region where you are creating the bucket does not support multi-AZ storage, even if you add this header in the request, the bucket still uses the single-AZ storage.
        :type x_obs_az_redundancy: str
        :param x_obs_fs_file_interface: Specifies a parallel file system during bucket creation.
        :type x_obs_fs_file_interface: str
        :param x_obs_epid: Enterprise project ID in **UUID** format. If you have enabled the enterprise project function, you can obtain this ID from the enterprise project service. To use the default project, set this header to **0** or do not contain this header in the request. This header is not needed if you do not enable the enterprise project function.
        :type x_obs_epid: str
        :param x_obs_ies_location: ID of the AZ of the IES site where a bucket is created. This parameter cannot coexist with **x-obs-cluster-type**.
        :type x_obs_ies_location: str
        :param body: Body of the CreateBucketRequest
        :type body: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        
        

        self._bucket_name = None
        self._date = None
        self._x_obs_acl = None
        self._x_obs_server_side_encryption = None
        self._x_obs_server_side_data_encryption = None
        self._x_obs_server_side_encryption_kms_key_id = None
        self._x_obs_server_side_encryption_bucket_key_enabled = None
        self._x_obs_sse_kms_key_project_id = None
        self._x_obs_bucket_object_lock_enabled = None
        self._x_obs_storage_class = None
        self._x_obs_grant_read = None
        self._x_obs_grant_write = None
        self._x_obs_grant_read_acp = None
        self._x_obs_grant_write_acp = None
        self._x_obs_grant_full_control = None
        self._x_obs_grant_read_delivered = None
        self._x_obs_grant_full_control_delivered = None
        self._x_obs_az_redundancy = None
        self._x_obs_fs_file_interface = None
        self._x_obs_epid = None
        self._x_obs_ies_location = None
        self._body = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if date is not None:
            self.date = date
        if x_obs_acl is not None:
            self.x_obs_acl = x_obs_acl
        if x_obs_server_side_encryption is not None:
            self.x_obs_server_side_encryption = x_obs_server_side_encryption
        if x_obs_server_side_data_encryption is not None:
            self.x_obs_server_side_data_encryption = x_obs_server_side_data_encryption
        if x_obs_server_side_encryption_kms_key_id is not None:
            self.x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id
        if x_obs_server_side_encryption_bucket_key_enabled is not None:
            self.x_obs_server_side_encryption_bucket_key_enabled = x_obs_server_side_encryption_bucket_key_enabled
        if x_obs_sse_kms_key_project_id is not None:
            self.x_obs_sse_kms_key_project_id = x_obs_sse_kms_key_project_id
        if x_obs_bucket_object_lock_enabled is not None:
            self.x_obs_bucket_object_lock_enabled = x_obs_bucket_object_lock_enabled
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_grant_read is not None:
            self.x_obs_grant_read = x_obs_grant_read
        if x_obs_grant_write is not None:
            self.x_obs_grant_write = x_obs_grant_write
        if x_obs_grant_read_acp is not None:
            self.x_obs_grant_read_acp = x_obs_grant_read_acp
        if x_obs_grant_write_acp is not None:
            self.x_obs_grant_write_acp = x_obs_grant_write_acp
        if x_obs_grant_full_control is not None:
            self.x_obs_grant_full_control = x_obs_grant_full_control
        if x_obs_grant_read_delivered is not None:
            self.x_obs_grant_read_delivered = x_obs_grant_read_delivered
        if x_obs_grant_full_control_delivered is not None:
            self.x_obs_grant_full_control_delivered = x_obs_grant_full_control_delivered
        if x_obs_az_redundancy is not None:
            self.x_obs_az_redundancy = x_obs_az_redundancy
        if x_obs_fs_file_interface is not None:
            self.x_obs_fs_file_interface = x_obs_fs_file_interface
        if x_obs_epid is not None:
            self.x_obs_epid = x_obs_epid
        if x_obs_ies_location is not None:
            self.x_obs_ies_location = x_obs_ies_location
        if body is not None:
            self.body = body

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateBucketRequest.

        A bucket name is part of the access domain name and needs to be resolved. The bucket name must conform to the DNS domain naming rules. When receiving a bucket creation request, OBS strictly checks the bucket name based on the following rules: + A bucket name must be unique across all accounts and regions. + The name of a deleted bucket can be reused for another bucket or a parallel file system at least 30 minutes later after the deletion. + A bucket name must be 3 to 63 characters long. Only lowercase letters, digits, hyphens (-), and periods (.) are allowed. + A bucket name cannot start or end with a period (.) or hyphen (-), and cannot contain two consecutive periods (..) or contain a period (.) and a hyphen (-) adjacent to each other. + A bucket name cannot be formatted as an IP address. Note: The SSL wildcard certificate matches only buckets without periods (.) in their names when HTTPS is used for OBS access. If you use a bucket with periods (.) in its name to access OBS, the client will display a message indicating that the bucket is risky, for example, a red alarm may be displayed in the browser security prompt. We recommend that you avoid using periods (.) in bucket names.

        :return: The bucket_name of this CreateBucketRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateBucketRequest.

        A bucket name is part of the access domain name and needs to be resolved. The bucket name must conform to the DNS domain naming rules. When receiving a bucket creation request, OBS strictly checks the bucket name based on the following rules: + A bucket name must be unique across all accounts and regions. + The name of a deleted bucket can be reused for another bucket or a parallel file system at least 30 minutes later after the deletion. + A bucket name must be 3 to 63 characters long. Only lowercase letters, digits, hyphens (-), and periods (.) are allowed. + A bucket name cannot start or end with a period (.) or hyphen (-), and cannot contain two consecutive periods (..) or contain a period (.) and a hyphen (-) adjacent to each other. + A bucket name cannot be formatted as an IP address. Note: The SSL wildcard certificate matches only buckets without periods (.) in their names when HTTPS is used for OBS access. If you use a bucket with periods (.) in its name to access OBS, the client will display a message indicating that the bucket is risky, for example, a red alarm may be displayed in the browser security prompt. We recommend that you avoid using periods (.) in bucket names.

        :param bucket_name: The bucket_name of this CreateBucketRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def date(self):
        r"""Gets the date of this CreateBucketRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this CreateBucketRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this CreateBucketRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this CreateBucketRequest.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_acl(self):
        r"""Gets the x_obs_acl of this CreateBucketRequest.

        When creating a bucket, you can add this header to configure access control policies (predefined common policies) for a bucket. Such policies include **private**, **public-read**, **public-read-write**, **public-read-delivered**, **public-read-write-delivered**, and **bucket-owner-full-control**. For details about each policy, see the ACL configuration using headers in section ACLs.

        :return: The x_obs_acl of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        r"""Sets the x_obs_acl of this CreateBucketRequest.

        When creating a bucket, you can add this header to configure access control policies (predefined common policies) for a bucket. Such policies include **private**, **public-read**, **public-read-write**, **public-read-delivered**, **public-read-write-delivered**, and **bucket-owner-full-control**. For details about each policy, see the ACL configuration using headers in section ACLs.

        :param x_obs_acl: The x_obs_acl of this CreateBucketRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_server_side_encryption(self):
        r"""Gets the x_obs_server_side_encryption of this CreateBucketRequest.

        When creating a bucket, you can use this header to specify an encryption method for the bucket.  Example: x-obs-server-side-encryption: kms

        :return: The x_obs_server_side_encryption of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        r"""Sets the x_obs_server_side_encryption of this CreateBucketRequest.

        When creating a bucket, you can use this header to specify an encryption method for the bucket.  Example: x-obs-server-side-encryption: kms

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this CreateBucketRequest.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_data_encryption(self):
        r"""Gets the x_obs_server_side_data_encryption of this CreateBucketRequest.

        When creating a bucket, you can use this header to specify an encryption algorithm for server-side encryption. Example: x-obs-server-side-data-encryption: AES256

        :return: The x_obs_server_side_data_encryption of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_server_side_data_encryption

    @x_obs_server_side_data_encryption.setter
    def x_obs_server_side_data_encryption(self, x_obs_server_side_data_encryption):
        r"""Sets the x_obs_server_side_data_encryption of this CreateBucketRequest.

        When creating a bucket, you can use this header to specify an encryption algorithm for server-side encryption. Example: x-obs-server-side-data-encryption: AES256

        :param x_obs_server_side_data_encryption: The x_obs_server_side_data_encryption of this CreateBucketRequest.
        :type x_obs_server_side_data_encryption: str
        """
        self._x_obs_server_side_data_encryption = x_obs_server_side_data_encryption

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        r"""Gets the x_obs_server_side_encryption_kms_key_id of this CreateBucketRequest.

        ID of a specified key used for SSE-KMS encryption. For details about how to obtain a key ID Constraints: This header can only be used when you specify kms for the x-obs-server-side-encryption header.

        :return: The x_obs_server_side_encryption_kms_key_id of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        r"""Sets the x_obs_server_side_encryption_kms_key_id of this CreateBucketRequest.

        ID of a specified key used for SSE-KMS encryption. For details about how to obtain a key ID Constraints: This header can only be used when you specify kms for the x-obs-server-side-encryption header.

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this CreateBucketRequest.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def x_obs_server_side_encryption_bucket_key_enabled(self):
        r"""Gets the x_obs_server_side_encryption_bucket_key_enabled of this CreateBucketRequest.

        Whether to enable the SSE-KMS bucket key feature. Constraints: If you set this header to true, you must also specify x-obs-server-side-encryption-kms-key-id to specify the key ID.

        :return: The x_obs_server_side_encryption_bucket_key_enabled of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_bucket_key_enabled

    @x_obs_server_side_encryption_bucket_key_enabled.setter
    def x_obs_server_side_encryption_bucket_key_enabled(self, x_obs_server_side_encryption_bucket_key_enabled):
        r"""Sets the x_obs_server_side_encryption_bucket_key_enabled of this CreateBucketRequest.

        Whether to enable the SSE-KMS bucket key feature. Constraints: If you set this header to true, you must also specify x-obs-server-side-encryption-kms-key-id to specify the key ID.

        :param x_obs_server_side_encryption_bucket_key_enabled: The x_obs_server_side_encryption_bucket_key_enabled of this CreateBucketRequest.
        :type x_obs_server_side_encryption_bucket_key_enabled: str
        """
        self._x_obs_server_side_encryption_bucket_key_enabled = x_obs_server_side_encryption_bucket_key_enabled

    @property
    def x_obs_sse_kms_key_project_id(self):
        r"""Gets the x_obs_sse_kms_key_project_id of this CreateBucketRequest.

        ID of the project (not an enterprise project) where the KMS CMK belongs when SSE-KMS is used

        :return: The x_obs_sse_kms_key_project_id of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_sse_kms_key_project_id

    @x_obs_sse_kms_key_project_id.setter
    def x_obs_sse_kms_key_project_id(self, x_obs_sse_kms_key_project_id):
        r"""Sets the x_obs_sse_kms_key_project_id of this CreateBucketRequest.

        ID of the project (not an enterprise project) where the KMS CMK belongs when SSE-KMS is used

        :param x_obs_sse_kms_key_project_id: The x_obs_sse_kms_key_project_id of this CreateBucketRequest.
        :type x_obs_sse_kms_key_project_id: str
        """
        self._x_obs_sse_kms_key_project_id = x_obs_sse_kms_key_project_id

    @property
    def x_obs_bucket_object_lock_enabled(self):
        r"""Gets the x_obs_bucket_object_lock_enabled of this CreateBucketRequest.

        When creating a bucket, you can use this header to enable WORM for the bucket. Example: x-obs-bucket-object-lock-enabled:true

        :return: The x_obs_bucket_object_lock_enabled of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_bucket_object_lock_enabled

    @x_obs_bucket_object_lock_enabled.setter
    def x_obs_bucket_object_lock_enabled(self, x_obs_bucket_object_lock_enabled):
        r"""Sets the x_obs_bucket_object_lock_enabled of this CreateBucketRequest.

        When creating a bucket, you can use this header to enable WORM for the bucket. Example: x-obs-bucket-object-lock-enabled:true

        :param x_obs_bucket_object_lock_enabled: The x_obs_bucket_object_lock_enabled of this CreateBucketRequest.
        :type x_obs_bucket_object_lock_enabled: str
        """
        self._x_obs_bucket_object_lock_enabled = x_obs_bucket_object_lock_enabled

    @property
    def x_obs_storage_class(self):
        r"""Gets the x_obs_storage_class of this CreateBucketRequest.

        When creating a bucket, you can add this header to configure a default storage class for a bucket. The storage classes include Standard (STANDARD), Infrequent Access (WARM), Archive (COLD), and Deep Archive storage (DEEP_ARCHIVE). If this header is not included, the bucket is created in the Standard storage class.

        :return: The x_obs_storage_class of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        r"""Sets the x_obs_storage_class of this CreateBucketRequest.

        When creating a bucket, you can add this header to configure a default storage class for a bucket. The storage classes include Standard (STANDARD), Infrequent Access (WARM), Archive (COLD), and Deep Archive storage (DEEP_ARCHIVE). If this header is not included, the bucket is created in the Standard storage class.

        :param x_obs_storage_class: The x_obs_storage_class of this CreateBucketRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_grant_read(self):
        r"""Gets the x_obs_grant_read of this CreateBucketRequest.

        Grants the read permission to all users under an account. The read permission allows you to list objects, multipart uploads, and object versions in a bucket, as well as to obtain bucket metadata.

        :return: The x_obs_grant_read of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        r"""Sets the x_obs_grant_read of this CreateBucketRequest.

        Grants the read permission to all users under an account. The read permission allows you to list objects, multipart uploads, and object versions in a bucket, as well as to obtain bucket metadata.

        :param x_obs_grant_read: The x_obs_grant_read of this CreateBucketRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_write(self):
        r"""Gets the x_obs_grant_write of this CreateBucketRequest.

        Grants the write permission to all users under an account. The write permission allows you to create, delete, or overwrite all objects in a bucket, and to initialize, upload, copy, and merge parts, as well as to cancel multipart uploads.

        :return: The x_obs_grant_write of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_write

    @x_obs_grant_write.setter
    def x_obs_grant_write(self, x_obs_grant_write):
        r"""Sets the x_obs_grant_write of this CreateBucketRequest.

        Grants the write permission to all users under an account. The write permission allows you to create, delete, or overwrite all objects in a bucket, and to initialize, upload, copy, and merge parts, as well as to cancel multipart uploads.

        :param x_obs_grant_write: The x_obs_grant_write of this CreateBucketRequest.
        :type x_obs_grant_write: str
        """
        self._x_obs_grant_write = x_obs_grant_write

    @property
    def x_obs_grant_read_acp(self):
        r"""Gets the x_obs_grant_read_acp of this CreateBucketRequest.

        Grants the ACL read permission to all users under an account. The ACL read permission allows you to read the bucket ACL.

        :return: The x_obs_grant_read_acp of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        r"""Sets the x_obs_grant_read_acp of this CreateBucketRequest.

        Grants the ACL read permission to all users under an account. The ACL read permission allows you to read the bucket ACL.

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this CreateBucketRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        r"""Gets the x_obs_grant_write_acp of this CreateBucketRequest.

        Grants the ACL write permission to all users under an account. The ACL write permission allows you to modify the bucket ACL.

        :return: The x_obs_grant_write_acp of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        r"""Sets the x_obs_grant_write_acp of this CreateBucketRequest.

        Grants the ACL write permission to all users under an account. The ACL write permission allows you to modify the bucket ACL.

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this CreateBucketRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        r"""Gets the x_obs_grant_full_control of this CreateBucketRequest.

        Grants the full control access to all users under an account.

        :return: The x_obs_grant_full_control of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        r"""Sets the x_obs_grant_full_control of this CreateBucketRequest.

        Grants the full control access to all users under an account.

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this CreateBucketRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_grant_read_delivered(self):
        r"""Gets the x_obs_grant_read_delivered of this CreateBucketRequest.

        Grants the read permission to all users under an account. By default, the read permission is applied to all objects in the bucket.

        :return: The x_obs_grant_read_delivered of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_delivered

    @x_obs_grant_read_delivered.setter
    def x_obs_grant_read_delivered(self, x_obs_grant_read_delivered):
        r"""Sets the x_obs_grant_read_delivered of this CreateBucketRequest.

        Grants the read permission to all users under an account. By default, the read permission is applied to all objects in the bucket.

        :param x_obs_grant_read_delivered: The x_obs_grant_read_delivered of this CreateBucketRequest.
        :type x_obs_grant_read_delivered: str
        """
        self._x_obs_grant_read_delivered = x_obs_grant_read_delivered

    @property
    def x_obs_grant_full_control_delivered(self):
        r"""Gets the x_obs_grant_full_control_delivered of this CreateBucketRequest.

        Grants the full control access to all users under an account. By default, the full control access is applied to all objects in the bucket.

        :return: The x_obs_grant_full_control_delivered of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control_delivered

    @x_obs_grant_full_control_delivered.setter
    def x_obs_grant_full_control_delivered(self, x_obs_grant_full_control_delivered):
        r"""Sets the x_obs_grant_full_control_delivered of this CreateBucketRequest.

        Grants the full control access to all users under an account. By default, the full control access is applied to all objects in the bucket.

        :param x_obs_grant_full_control_delivered: The x_obs_grant_full_control_delivered of this CreateBucketRequest.
        :type x_obs_grant_full_control_delivered: str
        """
        self._x_obs_grant_full_control_delivered = x_obs_grant_full_control_delivered

    @property
    def x_obs_az_redundancy(self):
        r"""Gets the x_obs_az_redundancy of this CreateBucketRequest.

        Add this header in a bucket creation request to enable the multi-AZ storage for the bucket. If this header is not carried, single-AZ storage is used for the bucket by default. If the region where you are creating the bucket does not support multi-AZ storage, even if you add this header in the request, the bucket still uses the single-AZ storage.

        :return: The x_obs_az_redundancy of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_az_redundancy

    @x_obs_az_redundancy.setter
    def x_obs_az_redundancy(self, x_obs_az_redundancy):
        r"""Sets the x_obs_az_redundancy of this CreateBucketRequest.

        Add this header in a bucket creation request to enable the multi-AZ storage for the bucket. If this header is not carried, single-AZ storage is used for the bucket by default. If the region where you are creating the bucket does not support multi-AZ storage, even if you add this header in the request, the bucket still uses the single-AZ storage.

        :param x_obs_az_redundancy: The x_obs_az_redundancy of this CreateBucketRequest.
        :type x_obs_az_redundancy: str
        """
        self._x_obs_az_redundancy = x_obs_az_redundancy

    @property
    def x_obs_fs_file_interface(self):
        r"""Gets the x_obs_fs_file_interface of this CreateBucketRequest.

        Specifies a parallel file system during bucket creation.

        :return: The x_obs_fs_file_interface of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_fs_file_interface

    @x_obs_fs_file_interface.setter
    def x_obs_fs_file_interface(self, x_obs_fs_file_interface):
        r"""Sets the x_obs_fs_file_interface of this CreateBucketRequest.

        Specifies a parallel file system during bucket creation.

        :param x_obs_fs_file_interface: The x_obs_fs_file_interface of this CreateBucketRequest.
        :type x_obs_fs_file_interface: str
        """
        self._x_obs_fs_file_interface = x_obs_fs_file_interface

    @property
    def x_obs_epid(self):
        r"""Gets the x_obs_epid of this CreateBucketRequest.

        Enterprise project ID in **UUID** format. If you have enabled the enterprise project function, you can obtain this ID from the enterprise project service. To use the default project, set this header to **0** or do not contain this header in the request. This header is not needed if you do not enable the enterprise project function.

        :return: The x_obs_epid of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_epid

    @x_obs_epid.setter
    def x_obs_epid(self, x_obs_epid):
        r"""Sets the x_obs_epid of this CreateBucketRequest.

        Enterprise project ID in **UUID** format. If you have enabled the enterprise project function, you can obtain this ID from the enterprise project service. To use the default project, set this header to **0** or do not contain this header in the request. This header is not needed if you do not enable the enterprise project function.

        :param x_obs_epid: The x_obs_epid of this CreateBucketRequest.
        :type x_obs_epid: str
        """
        self._x_obs_epid = x_obs_epid

    @property
    def x_obs_ies_location(self):
        r"""Gets the x_obs_ies_location of this CreateBucketRequest.

        ID of the AZ of the IES site where a bucket is created. This parameter cannot coexist with **x-obs-cluster-type**.

        :return: The x_obs_ies_location of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_ies_location

    @x_obs_ies_location.setter
    def x_obs_ies_location(self, x_obs_ies_location):
        r"""Sets the x_obs_ies_location of this CreateBucketRequest.

        ID of the AZ of the IES site where a bucket is created. This parameter cannot coexist with **x-obs-cluster-type**.

        :param x_obs_ies_location: The x_obs_ies_location of this CreateBucketRequest.
        :type x_obs_ies_location: str
        """
        self._x_obs_ies_location = x_obs_ies_location

    @property
    def body(self):
        r"""Gets the body of this CreateBucketRequest.

        :return: The body of this CreateBucketRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateBucketRequest.

        :param body: The body of this CreateBucketRequest.
        :type body: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateBucketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
