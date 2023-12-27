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
        """PutObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称 
        :type bucket_name: str
        :param object_key: 通过此请求创建的对象名称。 
        :type object_key: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param content_md5: 按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串  示例：n58IG6hfM7vqI4K0vnWpog&#x3D;&#x3D;。 
        :type content_md5: str
        :param x_obs_acl: 创建对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策  示例：x-obs-acl: public-read。 
        :type x_obs_acl: str
        :param x_obs_grant_read: 创建对象时，使用此头域授权租户下所有用户有读对象和获取对象元数据的权限  示例：x-obs-grant-read: id&#x3D;domainID。如果授权给多个租户，需要通过&#39;,&#39;分割。 
        :type x_obs_grant_read: str
        :param x_obs_grant_read_acp: 创建对象时，使用此头域授权租户下所有用户有获取对象ACL的权限  示例：x-obs-grant-read-acp: id&#x3D;domainID。如果授权给多个租户，需要通过&#39;,&#39;分割。 
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: 创建对象时，使用此头域授权租户下所有用户有写对象ACL的权  示例：x-obs-grant-write-acp: id&#x3D;domainID。如果授权给多个租户，需要通过&#39;,&#39;分割。 
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: 创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限  示例：x-obs-grant-full-control: id&#x3D;domainID。如果授权给多个租户，需要通过&#39;,&#39;分割。 
        :type x_obs_grant_full_control: str
        :param x_obs_storage_class: 创建对象时，可以加上此头域设置对象的存储类型。如果未设置此头域，则以桶的默认存储类型作为对象的存储类型  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 
        :type x_obs_storage_class: str
        :param x_obs_meta_xxx: 用户自定义元数据  示例：x-obs-meta-test: test metadata 
        :type x_obs_meta_xxx: str
        :param x_obs_persistent_headers: 创建对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取此对象或查询此对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。 格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例： x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  下载此对象或获取此对象元数据时：返回两个头域分别为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回 
        :type x_obs_persistent_headers: str
        :param x_obs_website_redirect_location: 当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  例如，重定向请求到桶内另一对象：  x-obs-website-redirect-location:/anotherPage.html  或重定向请求到一个外部URL：  x-obs-website-redirect-location:http://www.example.com/  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2KB。 
        :type x_obs_website_redirect_location: str
        :param x_obs_server_side_encryption: 使用该头域表示服务端加密是SSE-KMS方式。  示例：x-obs-server-side-encryption: kms 
        :type x_obs_server_side_encryption: str
        :param x_obs_server_side_encryption_kms_key_id: SSE-KMS方式下使用该头域，该头域表示主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。 支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 
        :type x_obs_server_side_encryption_kms_key_id: str
        :param x_obs_server_side_encryption_customer_algorithm: SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于加密对象  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param success_action_redirect: 此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 
        :type success_action_redirect: str
        :param x_obs_expires: 表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算） 此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 
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
        """Gets the bucket_name of this PutObjectRequest.

        桶名称 

        :return: The bucket_name of this PutObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this PutObjectRequest.

        桶名称 

        :param bucket_name: The bucket_name of this PutObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this PutObjectRequest.

        通过此请求创建的对象名称。 

        :return: The object_key of this PutObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this PutObjectRequest.

        通过此请求创建的对象名称。 

        :param object_key: The object_key of this PutObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        """Gets the date of this PutObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this PutObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this PutObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def content_md5(self):
        """Gets the content_md5 of this PutObjectRequest.

        按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串  示例：n58IG6hfM7vqI4K0vnWpog==。 

        :return: The content_md5 of this PutObjectRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        """Sets the content_md5 of this PutObjectRequest.

        按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串  示例：n58IG6hfM7vqI4K0vnWpog==。 

        :param content_md5: The content_md5 of this PutObjectRequest.
        :type content_md5: str
        """
        self._content_md5 = content_md5

    @property
    def x_obs_acl(self):
        """Gets the x_obs_acl of this PutObjectRequest.

        创建对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策  示例：x-obs-acl: public-read。 

        :return: The x_obs_acl of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        """Sets the x_obs_acl of this PutObjectRequest.

        创建对象时，可以加上此消息头设置对象的权限控制策略，使用的策略为预定义的常用策  示例：x-obs-acl: public-read。 

        :param x_obs_acl: The x_obs_acl of this PutObjectRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_grant_read(self):
        """Gets the x_obs_grant_read of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有读对象和获取对象元数据的权限  示例：x-obs-grant-read: id=domainID。如果授权给多个租户，需要通过','分割。 

        :return: The x_obs_grant_read of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        """Sets the x_obs_grant_read of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有读对象和获取对象元数据的权限  示例：x-obs-grant-read: id=domainID。如果授权给多个租户，需要通过','分割。 

        :param x_obs_grant_read: The x_obs_grant_read of this PutObjectRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_read_acp(self):
        """Gets the x_obs_grant_read_acp of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有获取对象ACL的权限  示例：x-obs-grant-read-acp: id=domainID。如果授权给多个租户，需要通过','分割。 

        :return: The x_obs_grant_read_acp of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        """Sets the x_obs_grant_read_acp of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有获取对象ACL的权限  示例：x-obs-grant-read-acp: id=domainID。如果授权给多个租户，需要通过','分割。 

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this PutObjectRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        """Gets the x_obs_grant_write_acp of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有写对象ACL的权  示例：x-obs-grant-write-acp: id=domainID。如果授权给多个租户，需要通过','分割。 

        :return: The x_obs_grant_write_acp of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        """Sets the x_obs_grant_write_acp of this PutObjectRequest.

        创建对象时，使用此头域授权租户下所有用户有写对象ACL的权  示例：x-obs-grant-write-acp: id=domainID。如果授权给多个租户，需要通过','分割。 

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this PutObjectRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        """Gets the x_obs_grant_full_control of this PutObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限  示例：x-obs-grant-full-control: id=domainID。如果授权给多个租户，需要通过','分割。 

        :return: The x_obs_grant_full_control of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        """Sets the x_obs_grant_full_control of this PutObjectRequest.

        创建对象时，使用此头域授权domain下所有用户有读对象、获取对象元数据、获取对象ACL、写对象ACL的权限  示例：x-obs-grant-full-control: id=domainID。如果授权给多个租户，需要通过','分割。 

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this PutObjectRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_storage_class(self):
        """Gets the x_obs_storage_class of this PutObjectRequest.

        创建对象时，可以加上此头域设置对象的存储类型。如果未设置此头域，则以桶的默认存储类型作为对象的存储类型  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 

        :return: The x_obs_storage_class of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        """Sets the x_obs_storage_class of this PutObjectRequest.

        创建对象时，可以加上此头域设置对象的存储类型。如果未设置此头域，则以桶的默认存储类型作为对象的存储类型  说明：存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）。因此这里可配置的值有：STANDARD、WARM和COLD，注意大小写敏感。  示例：x-obs-storage-class: STANDARD 

        :param x_obs_storage_class: The x_obs_storage_class of this PutObjectRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_meta_xxx(self):
        """Gets the x_obs_meta_xxx of this PutObjectRequest.

        用户自定义元数据  示例：x-obs-meta-test: test metadata 

        :return: The x_obs_meta_xxx of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_meta_xxx

    @x_obs_meta_xxx.setter
    def x_obs_meta_xxx(self, x_obs_meta_xxx):
        """Sets the x_obs_meta_xxx of this PutObjectRequest.

        用户自定义元数据  示例：x-obs-meta-test: test metadata 

        :param x_obs_meta_xxx: The x_obs_meta_xxx of this PutObjectRequest.
        :type x_obs_meta_xxx: str
        """
        self._x_obs_meta_xxx = x_obs_meta_xxx

    @property
    def x_obs_persistent_headers(self):
        """Gets the x_obs_persistent_headers of this PutObjectRequest.

        创建对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取此对象或查询此对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。 格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例： x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  下载此对象或获取此对象元数据时：返回两个头域分别为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回 

        :return: The x_obs_persistent_headers of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_persistent_headers

    @x_obs_persistent_headers.setter
    def x_obs_persistent_headers(self, x_obs_persistent_headers):
        """Sets the x_obs_persistent_headers of this PutObjectRequest.

        创建对象时，可以在HTTP请求中加入“x-obs-persistent-headers”消息头，用来加入一个或多个自定义的响应头，当用户获取此对象或查询此对象元数据时，加入的自定义响应头将会在返回消息的头域中出现。 格式：x-obs-persistent-headers: key1:base64_encode(value1),key2:base64_encode(value2)....  说明：其中key1/key2等为自定义header，若含有非ASCII码或不可识别字符，可以采用URL编码或者Base64编码，服务端只会作为字符串处理，不会做解码。value1/value2等为对应自定义header的值，base64_encode指做base64编码，即将自定义header和对应值的base64编码作为一个key-value对用“:”连接，然后用“,”将所有的key-value对连接起来，放在x-obs-persistent-headers这个header中即可，服务端会对上传的value做解码处理。  示例： x-obs-persistent-headers: key1:dmFsdWUx,key2:dmFsdWUy  下载此对象或获取此对象元数据时：返回两个头域分别为“key1:value1”与“key2:value2”  约束：  1. 通过该方式指定的自定义响应头不能以“x-obs-”为前缀，比如可以指定“key1”，但是不能指定“x-obs-key1”  2. 不能指定http标准头，例如host/content-md5/origin/range/Content-Disposition等  3. 此头域和自定义元数据总长度不能超过8KB  4. 如果传入相同key，将value以“,”拼接后放入同一个key中返回 

        :param x_obs_persistent_headers: The x_obs_persistent_headers of this PutObjectRequest.
        :type x_obs_persistent_headers: str
        """
        self._x_obs_persistent_headers = x_obs_persistent_headers

    @property
    def x_obs_website_redirect_location(self):
        """Gets the x_obs_website_redirect_location of this PutObjectRequest.

        当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  例如，重定向请求到桶内另一对象：  x-obs-website-redirect-location:/anotherPage.html  或重定向请求到一个外部URL：  x-obs-website-redirect-location:http://www.example.com/  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2KB。 

        :return: The x_obs_website_redirect_location of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_website_redirect_location

    @x_obs_website_redirect_location.setter
    def x_obs_website_redirect_location(self, x_obs_website_redirect_location):
        """Sets the x_obs_website_redirect_location of this PutObjectRequest.

        当桶设置了Website配置，可以将获取这个对象的请求重定向到桶内另一个对象或一个外部的URL，OBS将这个值从头域中取出，保存在对象的元数据中。  例如，重定向请求到桶内另一对象：  x-obs-website-redirect-location:/anotherPage.html  或重定向请求到一个外部URL：  x-obs-website-redirect-location:http://www.example.com/  默认值：无  约束：必须以“/”、“http://”或“https://”开头，长度不超过2KB。 

        :param x_obs_website_redirect_location: The x_obs_website_redirect_location of this PutObjectRequest.
        :type x_obs_website_redirect_location: str
        """
        self._x_obs_website_redirect_location = x_obs_website_redirect_location

    @property
    def x_obs_server_side_encryption(self):
        """Gets the x_obs_server_side_encryption of this PutObjectRequest.

        使用该头域表示服务端加密是SSE-KMS方式。  示例：x-obs-server-side-encryption: kms 

        :return: The x_obs_server_side_encryption of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption

    @x_obs_server_side_encryption.setter
    def x_obs_server_side_encryption(self, x_obs_server_side_encryption):
        """Sets the x_obs_server_side_encryption of this PutObjectRequest.

        使用该头域表示服务端加密是SSE-KMS方式。  示例：x-obs-server-side-encryption: kms 

        :param x_obs_server_side_encryption: The x_obs_server_side_encryption of this PutObjectRequest.
        :type x_obs_server_side_encryption: str
        """
        self._x_obs_server_side_encryption = x_obs_server_side_encryption

    @property
    def x_obs_server_side_encryption_kms_key_id(self):
        """Gets the x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.

        SSE-KMS方式下使用该头域，该头域表示主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。 支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 

        :return: The x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_kms_key_id

    @x_obs_server_side_encryption_kms_key_id.setter
    def x_obs_server_side_encryption_kms_key_id(self, x_obs_server_side_encryption_kms_key_id):
        """Sets the x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.

        SSE-KMS方式下使用该头域，该头域表示主密钥，如果用户没有提供该头域，那么默认的主密钥将会被使用。 支持两种格式的描述方式：  1. regionID:domainID(租户ID):key/key_id  或者  2.key_id  其中regionID是使用密钥所属region的ID；domainID是使用密钥所属租户的租户ID；key_id是从数据加密服务创建的密钥ID。  示例：  1. x-obs-server-side-encryption-kms-key-id: cn-north-4:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0 或者  2. x-obs-server-side-encryption-kms-key-id: 4f1cd4de-ab64-4807-920a-47fc42e7f0d0 

        :param x_obs_server_side_encryption_kms_key_id: The x_obs_server_side_encryption_kms_key_id of this PutObjectRequest.
        :type x_obs_server_side_encryption_kms_key_id: str
        """
        self._x_obs_server_side_encryption_kms_key_id = x_obs_server_side_encryption_kms_key_id

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        """Gets the x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        """Sets the x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm: AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        """Gets the x_obs_server_side_encryption_customer_key of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于加密对象  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_key of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        """Sets the x_obs_server_side_encryption_customer_key of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于加密对象  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        """Gets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

        :return: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        """Sets the x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this PutObjectRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        """Gets the success_action_redirect of this PutObjectRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 

        :return: The success_action_redirect of this PutObjectRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        """Sets the success_action_redirect of this PutObjectRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 

        :param success_action_redirect: The success_action_redirect of this PutObjectRequest.
        :type success_action_redirect: str
        """
        self._success_action_redirect = success_action_redirect

    @property
    def x_obs_expires(self):
        """Gets the x_obs_expires of this PutObjectRequest.

        表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算） 此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 

        :return: The x_obs_expires of this PutObjectRequest.
        :rtype: int
        """
        return self._x_obs_expires

    @x_obs_expires.setter
    def x_obs_expires(self, x_obs_expires):
        """Sets the x_obs_expires of this PutObjectRequest.

        表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算） 此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 

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
