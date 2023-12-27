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
        """CopyObjectRequest

        The model defined in huaweicloud sdk

        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param bucket_name: 请求的桶名称。 
        :type bucket_name: str
        :param object_key: 目标对象名称。 
        :type object_key: str
        :param x_obs_acl: 复制对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策略，包括：private；public-read；public-read-write（各策略详细说明见ACL章节的“使用头域设置ACL”）。 示例：x-obs-acl: acl 
        :type x_obs_acl: str
        :param x_obs_grant_read: 创建对象时，使用此头域授权domain下所有用户有读对象和获取对象元数据的权限 
        :type x_obs_grant_read: str
        :param x_obs_grant_read_acp: 创建对象时，使用此头域授权domain下所有用户有获取对象ACL的权限。 
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: 创建对象时，使用此头域授权domain下所有用户有写对象ACL的权限。 
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: 创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限。 
        :type x_obs_grant_full_control: str
        :param x_obs_copy_source: 用来指定复制对象操作的源桶名以及源对象名。当源对象存在多个版本时，通过versionId参数指定版本源对象。 约束：中文字符，需要进行URLEncode 示例：x-obs-copy-source: /source_bucket/sourceObject 
        :type x_obs_copy_source: str
        :param x_obs_metadata_directive: 此参数用来指定新对象的元数据是从源对象中复制，还是用请求中的元数据替换。  有效取值：COPY或REPLACE。  默认值：COPY。  示例：x-obs-metadata-directive: metadata_directive  约束条件：如果此参数的值不是COPY或REPLACE，则OBS立即返回400错误；如果用户进行修改元数据操作（源对象与目标对象相同），则此参数只能为REPLACE，否则此请求作为无效请求，服务端响应400。此参数不支持将加密的对象更改成非加密对象（源对象与目标对象相同）。如果用户使用此参数更改加密的对象，系统将返回400。 
        :type x_obs_metadata_directive: str
        :param x_obs_copy_source_if_match: 只有当源对象的Etag与此参数指定的值相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-match: etag  约束条件：此参数可与x-obs-copy-source-if-unmodified-since一起使用，但不能与其它条件复制参数一起使用。 
        :type x_obs_copy_source_if_match: str
        :param x_obs_copy_source_if_none_match: 只有当源对象的Etag与此参数指定的值不相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-none-match: etag  约束条件：此参数可与x-obs-copy-source-if-modified-since一起使用，但不能与其它条件复制参数一起使用。 
        :type x_obs_copy_source_if_none_match: str
        :param x_obs_copy_source_if_unmodified_since: 只有当源对象在此参数指定的时间之后没有修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-unmodified -since: time-sta 
        :type x_obs_copy_source_if_unmodified_since: str
        :param x_obs_copy_source_if_modified_since: 只有当源对象在此参数指定的时间之后修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-none-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-modified-since: time-sta 
        :type x_obs_copy_source_if_modified_since: str
        :param x_obs_storage_class: 复制对象时，可以加上此头域设置目的对象的存储类型。如果未设置此头域，则以目的对象所在桶的默认存储类型作为对象的存储类型。  类型：字符串  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 
        :type x_obs_storage_class: str
        :param x_obs_persistent_headers: 复制对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取目标对象或查询目标对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。  类型：字符串。  格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例：x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  在下载目标对象或获取目标对象元数据时：返回两个头域为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回  5. 如果源对象中已经存在自定义响应头，复制的时候不会拷贝到目标对象中 
        :type x_obs_persistent_headers: str
        :param x_obs_website_redirect_location: 当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  类型：字符串  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2K。 
        :type x_obs_website_redirect_location: str
        :param x_obs_server_side_encryption: 使用该头域表示服务端加密是SSE-KMS方式。目标对象使用SSE-KMS方式加密。  类型：字符串  示例：x-obs-server-side-encryption: kms  当使用SSE-KMS方式时，必选。 
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_encryption_kms_key_id: SSE-KMS方式下使用该头域，该头域表示加密目标对象使用的主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。  类型：字符串  支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 
        :type x_obs_server_side_encryption_kms_key_id: str
        :param x_obs_server_side_encryption_customer_algorithm: SSE-C方式下使用该头域，该头域表示加密目标对象使用的算法。  类型：字符串  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥。  类型：字符串  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。  当使用SSE-C方式时，必选。 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param x_obs_copy_source_server_side_encryption_customer_algorithm: SSE-C方式下使用该头域，该头域表示解密源对象使用的算法。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-copy-source-server-side-encryption-customer-key，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 
        :type x_obs_copy_source_server_side_encryption_customer_algorithm: str
        :param x_obs_copy_source_server_side_encryption_customer_key: SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥。用于解密源对象。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 
        :type x_obs_copy_source_server_side_encryption_customer_key: str
        :param x_obs_copy_source_server_side_encryption_customer_key_md5: SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key一起使用。  当拷贝源对象使用SSE-C方式时，必选。 
        :type x_obs_copy_source_server_side_encryption_customer_key_md5: str
        :param success_action_redirect: 此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 类型：字符串。 
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
        """Gets the date of this CopyObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this CopyObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CopyObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this CopyObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CopyObjectRequest.

        请求的桶名称。 

        :return: The bucket_name of this CopyObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CopyObjectRequest.

        请求的桶名称。 

        :param bucket_name: The bucket_name of this CopyObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this CopyObjectRequest.

        目标对象名称。 

        :return: The object_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this CopyObjectRequest.

        目标对象名称。 

        :param object_key: The object_key of this CopyObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def x_obs_acl(self):
        """Gets the x_obs_acl of this CopyObjectRequest.

        复制对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策略，包括：private；public-read；public-read-write（各策略详细说明见ACL章节的“使用头域设置ACL”）。 示例：x-obs-acl: acl 

        :return: The x_obs_acl of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        """Sets the x_obs_acl of this CopyObjectRequest.

        复制对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策略，包括：private；public-read；public-read-write（各策略详细说明见ACL章节的“使用头域设置ACL”）。 示例：x-obs-acl: acl 

        :param x_obs_acl: The x_obs_acl of this CopyObjectRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_grant_read(self):
        """Gets the x_obs_grant_read of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象和获取对象元数据的权限 

        :return: The x_obs_grant_read of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        """Sets the x_obs_grant_read of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象和获取对象元数据的权限 

        :param x_obs_grant_read: The x_obs_grant_read of this CopyObjectRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_read_acp(self):
        """Gets the x_obs_grant_read_acp of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有获取对象ACL的权限。 

        :return: The x_obs_grant_read_acp of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        """Sets the x_obs_grant_read_acp of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有获取对象ACL的权限。 

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this CopyObjectRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        """Gets the x_obs_grant_write_acp of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有写对象ACL的权限。 

        :return: The x_obs_grant_write_acp of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        """Sets the x_obs_grant_write_acp of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有写对象ACL的权限。 

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this CopyObjectRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        """Gets the x_obs_grant_full_control of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限。 

        :return: The x_obs_grant_full_control of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        """Sets the x_obs_grant_full_control of this CopyObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限。 

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this CopyObjectRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_copy_source(self):
        """Gets the x_obs_copy_source of this CopyObjectRequest.

        用来指定复制对象操作的源桶名以及源对象名。当源对象存在多个版本时，通过versionId参数指定版本源对象。 约束：中文字符，需要进行URLEncode 示例：x-obs-copy-source: /source_bucket/sourceObject 

        :return: The x_obs_copy_source of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source

    @x_obs_copy_source.setter
    def x_obs_copy_source(self, x_obs_copy_source):
        """Sets the x_obs_copy_source of this CopyObjectRequest.

        用来指定复制对象操作的源桶名以及源对象名。当源对象存在多个版本时，通过versionId参数指定版本源对象。 约束：中文字符，需要进行URLEncode 示例：x-obs-copy-source: /source_bucket/sourceObject 

        :param x_obs_copy_source: The x_obs_copy_source of this CopyObjectRequest.
        :type x_obs_copy_source: str
        """
        self._x_obs_copy_source = x_obs_copy_source

    @property
    def x_obs_metadata_directive(self):
        """Gets the x_obs_metadata_directive of this CopyObjectRequest.

        此参数用来指定新对象的元数据是从源对象中复制，还是用请求中的元数据替换。  有效取值：COPY或REPLACE。  默认值：COPY。  示例：x-obs-metadata-directive: metadata_directive  约束条件：如果此参数的值不是COPY或REPLACE，则OBS立即返回400错误；如果用户进行修改元数据操作（源对象与目标对象相同），则此参数只能为REPLACE，否则此请求作为无效请求，服务端响应400。此参数不支持将加密的对象更改成非加密对象（源对象与目标对象相同）。如果用户使用此参数更改加密的对象，系统将返回400。 

        :return: The x_obs_metadata_directive of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_metadata_directive

    @x_obs_metadata_directive.setter
    def x_obs_metadata_directive(self, x_obs_metadata_directive):
        """Sets the x_obs_metadata_directive of this CopyObjectRequest.

        此参数用来指定新对象的元数据是从源对象中复制，还是用请求中的元数据替换。  有效取值：COPY或REPLACE。  默认值：COPY。  示例：x-obs-metadata-directive: metadata_directive  约束条件：如果此参数的值不是COPY或REPLACE，则OBS立即返回400错误；如果用户进行修改元数据操作（源对象与目标对象相同），则此参数只能为REPLACE，否则此请求作为无效请求，服务端响应400。此参数不支持将加密的对象更改成非加密对象（源对象与目标对象相同）。如果用户使用此参数更改加密的对象，系统将返回400。 

        :param x_obs_metadata_directive: The x_obs_metadata_directive of this CopyObjectRequest.
        :type x_obs_metadata_directive: str
        """
        self._x_obs_metadata_directive = x_obs_metadata_directive

    @property
    def x_obs_copy_source_if_match(self):
        """Gets the x_obs_copy_source_if_match of this CopyObjectRequest.

        只有当源对象的Etag与此参数指定的值相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-match: etag  约束条件：此参数可与x-obs-copy-source-if-unmodified-since一起使用，但不能与其它条件复制参数一起使用。 

        :return: The x_obs_copy_source_if_match of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_match

    @x_obs_copy_source_if_match.setter
    def x_obs_copy_source_if_match(self, x_obs_copy_source_if_match):
        """Sets the x_obs_copy_source_if_match of this CopyObjectRequest.

        只有当源对象的Etag与此参数指定的值相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-match: etag  约束条件：此参数可与x-obs-copy-source-if-unmodified-since一起使用，但不能与其它条件复制参数一起使用。 

        :param x_obs_copy_source_if_match: The x_obs_copy_source_if_match of this CopyObjectRequest.
        :type x_obs_copy_source_if_match: str
        """
        self._x_obs_copy_source_if_match = x_obs_copy_source_if_match

    @property
    def x_obs_copy_source_if_none_match(self):
        """Gets the x_obs_copy_source_if_none_match of this CopyObjectRequest.

        只有当源对象的Etag与此参数指定的值不相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-none-match: etag  约束条件：此参数可与x-obs-copy-source-if-modified-since一起使用，但不能与其它条件复制参数一起使用。 

        :return: The x_obs_copy_source_if_none_match of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_none_match

    @x_obs_copy_source_if_none_match.setter
    def x_obs_copy_source_if_none_match(self, x_obs_copy_source_if_none_match):
        """Sets the x_obs_copy_source_if_none_match of this CopyObjectRequest.

        只有当源对象的Etag与此参数指定的值不相等时才进行复制对象操作，否则返回412（前置条件不满足）。  示例：x-obs-copy-source-if-none-match: etag  约束条件：此参数可与x-obs-copy-source-if-modified-since一起使用，但不能与其它条件复制参数一起使用。 

        :param x_obs_copy_source_if_none_match: The x_obs_copy_source_if_none_match of this CopyObjectRequest.
        :type x_obs_copy_source_if_none_match: str
        """
        self._x_obs_copy_source_if_none_match = x_obs_copy_source_if_none_match

    @property
    def x_obs_copy_source_if_unmodified_since(self):
        """Gets the x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.

        只有当源对象在此参数指定的时间之后没有修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-unmodified -since: time-sta 

        :return: The x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_unmodified_since

    @x_obs_copy_source_if_unmodified_since.setter
    def x_obs_copy_source_if_unmodified_since(self, x_obs_copy_source_if_unmodified_since):
        """Sets the x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.

        只有当源对象在此参数指定的时间之后没有修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-unmodified -since: time-sta 

        :param x_obs_copy_source_if_unmodified_since: The x_obs_copy_source_if_unmodified_since of this CopyObjectRequest.
        :type x_obs_copy_source_if_unmodified_since: str
        """
        self._x_obs_copy_source_if_unmodified_since = x_obs_copy_source_if_unmodified_since

    @property
    def x_obs_copy_source_if_modified_since(self):
        """Gets the x_obs_copy_source_if_modified_since of this CopyObjectRequest.

        只有当源对象在此参数指定的时间之后修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-none-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-modified-since: time-sta 

        :return: The x_obs_copy_source_if_modified_since of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_if_modified_since

    @x_obs_copy_source_if_modified_since.setter
    def x_obs_copy_source_if_modified_since(self, x_obs_copy_source_if_modified_since):
        """Sets the x_obs_copy_source_if_modified_since of this CopyObjectRequest.

        只有当源对象在此参数指定的时间之后修改过才进行复制对象操作，否则返回412（前置条件不满足），此参数可与x-obs-copy-source-if-none-match一起使用，但不能与其它条件复制参数一起使用。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。  示例：x-obs-copy-source-if-modified-since: time-sta 

        :param x_obs_copy_source_if_modified_since: The x_obs_copy_source_if_modified_since of this CopyObjectRequest.
        :type x_obs_copy_source_if_modified_since: str
        """
        self._x_obs_copy_source_if_modified_since = x_obs_copy_source_if_modified_since

    @property
    def x_obs_storage_class(self):
        """Gets the x_obs_storage_class of this CopyObjectRequest.

        复制对象时，可以加上此头域设置目的对象的存储类型。如果未设置此头域，则以目的对象所在桶的默认存储类型作为对象的存储类型。  类型：字符串  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 

        :return: The x_obs_storage_class of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        """Sets the x_obs_storage_class of this CopyObjectRequest.

        复制对象时，可以加上此头域设置目的对象的存储类型。如果未设置此头域，则以目的对象所在桶的默认存储类型作为对象的存储类型。  类型：字符串  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 

        :param x_obs_storage_class: The x_obs_storage_class of this CopyObjectRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_persistent_headers(self):
        """Gets the x_obs_persistent_headers of this CopyObjectRequest.

        复制对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取目标对象或查询目标对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。  类型：字符串。  格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例：x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  在下载目标对象或获取目标对象元数据时：返回两个头域为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回  5. 如果源对象中已经存在自定义响应头，复制的时候不会拷贝到目标对象中 

        :return: The x_obs_persistent_headers of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_persistent_headers

    @x_obs_persistent_headers.setter
    def x_obs_persistent_headers(self, x_obs_persistent_headers):
        """Sets the x_obs_persistent_headers of this CopyObjectRequest.

        复制对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取目标对象或查询目标对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。  类型：字符串。  格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例：x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  在下载目标对象或获取目标对象元数据时：返回两个头域为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回  5. 如果源对象中已经存在自定义响应头，复制的时候不会拷贝到目标对象中 

        :param x_obs_persistent_headers: The x_obs_persistent_headers of this CopyObjectRequest.
        :type x_obs_persistent_headers: str
        """
        self._x_obs_persistent_headers = x_obs_persistent_headers

    @property
    def x_obs_website_redirect_location(self):
        """Gets the x_obs_website_redirect_location of this CopyObjectRequest.

        当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  类型：字符串  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2K。 

        :return: The x_obs_website_redirect_location of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_website_redirect_location

    @x_obs_website_redirect_location.setter
    def x_obs_website_redirect_location(self, x_obs_website_redirect_location):
        """Sets the x_obs_website_redirect_location of this CopyObjectRequest.

        当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  类型：字符串  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2K。 

        :param x_obs_website_redirect_location: The x_obs_website_redirect_location of this CopyObjectRequest.
        :type x_obs_website_redirect_location: str
        """
        self._x_obs_website_redirect_location = x_obs_website_redirect_location

    @property
    def x_obs_server_side_encryption(self):
        """Gets the x_obs_server_side_encryption of this CopyObjectRequest.

        使用该头域表示服务端加密是SSE-KMS方式。目标对象使用SSE-KMS方式加密。  类型：字符串  示例：x-obs-server-side-encryption: kms  当使用SSE-KMS方式时，必选。 

        :return: The x_obs_server_side_encryption of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        """Sets the x_obs_server_side_encryption of this CopyObjectRequest.

        使用该头域表示服务端加密是SSE-KMS方式。目标对象使用SSE-KMS方式加密。  类型：字符串  示例：x-obs-server-side-encryption: kms  当使用SSE-KMS方式时，必选。 

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this CopyObjectRequest.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        """Gets the x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.

        SSE-KMS方式下使用该头域，该头域表示加密目标对象使用的主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。  类型：字符串  支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 

        :return: The x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        """Sets the x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.

        SSE-KMS方式下使用该头域，该头域表示加密目标对象使用的主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。  类型：字符串  支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this CopyObjectRequest.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        """Gets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的算法。  类型：字符串  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 

        :return: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        """Sets the x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的算法。  类型：字符串  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        """Gets the x_obs_server_side_encryption_customer_key of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥。  类型：字符串  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 

        :return: The x_obs_server_side_encryption_customer_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        """Sets the x_obs_server_side_encryption_customer_key of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥。  类型：字符串  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。  当使用SSE-C方式时，必选。 

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        """Gets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。  当使用SSE-C方式时，必选。 

        :return: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        """Sets the x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密目标对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。  当使用SSE-C方式时，必选。 

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def x_obs_copy_source_server_side_encryption_customer_algorithm(self):
        """Gets the x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的算法。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-copy-source-server-side-encryption-customer-key，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :return: The x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_algorithm

    @x_obs_copy_source_server_side_encryption_customer_algorithm.setter
    def x_obs_copy_source_server_side_encryption_customer_algorithm(self, x_obs_copy_source_server_side_encryption_customer_algorithm):
        """Sets the x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的算法。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-copy-source-server-side-encryption-customer-key，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :param x_obs_copy_source_server_side_encryption_customer_algorithm: The x_obs_copy_source_server_side_encryption_customer_algorithm of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_algorithm = x_obs_copy_source_server_side_encryption_customer_algorithm

    @property
    def x_obs_copy_source_server_side_encryption_customer_key(self):
        """Gets the x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥。用于解密源对象。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :return: The x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_key

    @x_obs_copy_source_server_side_encryption_customer_key.setter
    def x_obs_copy_source_server_side_encryption_customer_key(self, x_obs_copy_source_server_side_encryption_customer_key):
        """Sets the x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥。用于解密源对象。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key: K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key-MD5一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :param x_obs_copy_source_server_side_encryption_customer_key: The x_obs_copy_source_server_side_encryption_customer_key of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_key: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_key = x_obs_copy_source_server_side_encryption_customer_key

    @property
    def x_obs_copy_source_server_side_encryption_customer_key_md5(self):
        """Gets the x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :return: The x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :rtype: str
        """
        return self._x_obs_copy_source_server_side_encryption_customer_key_md5

    @x_obs_copy_source_server_side_encryption_customer_key_md5.setter
    def x_obs_copy_source_server_side_encryption_customer_key_md5(self, x_obs_copy_source_server_side_encryption_customer_key_md5):
        """Sets the x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.

        SSE-C方式下使用该头域，该头域表示解密源对象使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  类型：字符串  示例：x-obs-copy-source-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-copy-source-server-side-encryption-customer-algorithm，x-obs-copy-source-server-side-encryption-customer-key一起使用。  当拷贝源对象使用SSE-C方式时，必选。 

        :param x_obs_copy_source_server_side_encryption_customer_key_md5: The x_obs_copy_source_server_side_encryption_customer_key_md5 of this CopyObjectRequest.
        :type x_obs_copy_source_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_copy_source_server_side_encryption_customer_key_md5 = x_obs_copy_source_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        """Gets the success_action_redirect of this CopyObjectRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 类型：字符串。 

        :return: The success_action_redirect of this CopyObjectRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        """Sets the success_action_redirect of this CopyObjectRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 类型：字符串。 

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
