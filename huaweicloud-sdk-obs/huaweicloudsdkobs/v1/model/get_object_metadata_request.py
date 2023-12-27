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
        """GetObjectMetadataRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称 
        :type bucket_name: str
        :param object_key: 通过此请求获取元数据的对象名称。 
        :type object_key: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param version_id: 对象的版本号。 
        :type version_id: str
        :param origin: 预请求指定的跨域请求Origin（通常为域名）。 
        :type origin: str
        :param access_control_request_headers: 实际请求可以带的HTTP头域，可以带多个头域。 
        :type access_control_request_headers: str
        :param x_obs_server_side_encryption_customer_algorithm: SSE-C方式下使用该头域，该头域表示解密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: SSE-C方式下使用该头域，该头域表示解密使用的密钥。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 
        :type x_obs_server_side_encryption_customer_key_md5: str
        :param success_action_redirect: 此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 
        :type success_action_redirect: str
        :param x_obs_expires: 表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算）  此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 
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
        """Gets the bucket_name of this GetObjectMetadataRequest.

        桶名称 

        :return: The bucket_name of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this GetObjectMetadataRequest.

        桶名称 

        :param bucket_name: The bucket_name of this GetObjectMetadataRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this GetObjectMetadataRequest.

        通过此请求获取元数据的对象名称。 

        :return: The object_key of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this GetObjectMetadataRequest.

        通过此请求获取元数据的对象名称。 

        :param object_key: The object_key of this GetObjectMetadataRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        """Gets the date of this GetObjectMetadataRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this GetObjectMetadataRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this GetObjectMetadataRequest.
        :type date: str
        """
        self._date = date

    @property
    def version_id(self):
        """Gets the version_id of this GetObjectMetadataRequest.

        对象的版本号。 

        :return: The version_id of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this GetObjectMetadataRequest.

        对象的版本号。 

        :param version_id: The version_id of this GetObjectMetadataRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def origin(self):
        """Gets the origin of this GetObjectMetadataRequest.

        预请求指定的跨域请求Origin（通常为域名）。 

        :return: The origin of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this GetObjectMetadataRequest.

        预请求指定的跨域请求Origin（通常为域名）。 

        :param origin: The origin of this GetObjectMetadataRequest.
        :type origin: str
        """
        self._origin = origin

    @property
    def access_control_request_headers(self):
        """Gets the access_control_request_headers of this GetObjectMetadataRequest.

        实际请求可以带的HTTP头域，可以带多个头域。 

        :return: The access_control_request_headers of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._access_control_request_headers

    @access_control_request_headers.setter
    def access_control_request_headers(self, access_control_request_headers):
        """Sets the access_control_request_headers of this GetObjectMetadataRequest.

        实际请求可以带的HTTP头域，可以带多个头域。 

        :param access_control_request_headers: The access_control_request_headers of this GetObjectMetadataRequest.
        :type access_control_request_headers: str
        """
        self._access_control_request_headers = access_control_request_headers

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        """Gets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示解密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        """Sets the x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示解密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        """Gets the x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示解密使用的密钥。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        """Sets the x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示解密使用的密钥。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        """Gets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

        :return: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        """Sets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束: 该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

        :param x_obs_server_side_encryption_customer_key_md5: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectMetadataRequest.
        :type x_obs_server_side_encryption_customer_key_md5: str
        """
        self._x_obs_server_side_encryption_customer_key_md5 = x_obs_server_side_encryption_customer_key_md5

    @property
    def success_action_redirect(self):
        """Gets the success_action_redirect of this GetObjectMetadataRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 

        :return: The success_action_redirect of this GetObjectMetadataRequest.
        :rtype: str
        """
        return self._success_action_redirect

    @success_action_redirect.setter
    def success_action_redirect(self, success_action_redirect):
        """Sets the success_action_redirect of this GetObjectMetadataRequest.

        此参数的值是一个URL，用于指定当此次请求操作成功响应后的重定向的地址。  如果此参数值有效且操作成功，响应码为303，Location头域由此参数以及桶名、对象名、对象的ETag组成。 如果此参数值无效，则OBS忽略此参数的作用，响应码为204，Location头域为对象地址。 

        :param success_action_redirect: The success_action_redirect of this GetObjectMetadataRequest.
        :type success_action_redirect: str
        """
        self._success_action_redirect = success_action_redirect

    @property
    def x_obs_expires(self):
        """Gets the x_obs_expires of this GetObjectMetadataRequest.

        表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算）  此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 

        :return: The x_obs_expires of this GetObjectMetadataRequest.
        :rtype: int
        """
        return self._x_obs_expires

    @x_obs_expires.setter
    def x_obs_expires(self, x_obs_expires):
        """Sets the x_obs_expires of this GetObjectMetadataRequest.

        表示对象的过期时间，单位是天。过期之后对象会被自动删除。（从对象最后修改时间开始计算）  此字段对于每个对象仅支持上传时配置，不支持后期通过修改元数据接口修改。  示例：x-obs-expires:3 

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
