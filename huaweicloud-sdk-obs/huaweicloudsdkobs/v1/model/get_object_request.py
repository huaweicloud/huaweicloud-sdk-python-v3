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
        """GetObjectRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称 
        :type bucket_name: str
        :param object_key: 通过此请求下载的对象名称。 
        :type object_key: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param response_content_type: 重写响应中的Content-Type头。 
        :type response_content_type: str
        :param response_content_language: 重写响应中的Content-Language头。 
        :type response_content_language: str
        :param response_expires: 重写响应中的Expires头。 
        :type response_expires: str
        :param response_cache_control: 重写响应中的Cache-Control头。 
        :type response_cache_control: str
        :param response_content_disposition: 重写响应中的Content-Disposition头。  示例：response-content-disposition&#x3D;attachment; filename*&#x3D;utf-8&#39;&#39;name1  下载对象重命名为“name1”，如果name1中存在中文，需要将中文进行URL编码。 
        :type response_content_disposition: str
        :param response_content_encoding: 重写响应中的Content-Encoding头。 
        :type response_content_encoding: str
        :param version_id: 指定获取对象的版本号。 
        :type version_id: str
        :param x_image_process: 图片处理服务。  示例：  命令方式：x-image-process&#x3D;image/commands  样式方式：x-image-process&#x3D;style/stylename  详见[《图片处理特性指南》](https://support.huaweicloud.com/fg-obs/obs_01_0001.html)。 
        :type x_image_process: str
        :param attname: 重写响应中的Content-Disposition头。  示例：attname&#x3D;name1  下载对象重命名为“name1”。 
        :type attname: str
        :param range: 获取对象时，获取在Range范围内的对象内容。如果Range不合法则忽略此字段获取整个对象。  Range是一个范围，它的起始值最小为0，最大为对象长度减1。Range范围的起始值为必填项，如果Range只包含起始值，表示获取起始值到对象长度减1这个区间的对象内容。  携带Range头域后，响应消息的ETag仍是对象的ETag，而不是Range范围内对象的ETag。  bytes&#x3D;byte_range  示例1：bytes&#x3D;0-4 示例2：bytes&#x3D;1024 示例3：bytes&#x3D;10-20,30-40（表示多个区间） 
        :type range: str
        :param if_modified_since: 如果对象在请求中指定的时间之后有修改，则返回对象内容；否则的话返回304（not modified）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 
        :type if_modified_since: str
        :param if_unmodified_since: 如果对象在请求中指定的时间之后没有修改，则返回对象内容；否则的话返回412（precondition failed）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 
        :type if_unmodified_since: str
        :param if_match: 如果对象的ETag和请求中指定的ETag相同，则返回对象内容，否则的话返回412（precondition failed）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 
        :type if_match: str
        :param if_none_match: 如果对象的ETag和请求中指定的ETag不相同，则返回对象内容，否则的话返回304（not modified）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 
        :type if_none_match: str
        :param x_obs_server_side_encryption_customer_algorithm: SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_algorithm: str
        :param x_obs_server_side_encryption_customer_key: SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于解密对象。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw&#x3D;  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 
        :type x_obs_server_side_encryption_customer_key: str
        :param x_obs_server_side_encryption_customer_key_md5: SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ&#x3D;&#x3D;  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 
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
        """Gets the bucket_name of this GetObjectRequest.

        桶名称 

        :return: The bucket_name of this GetObjectRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this GetObjectRequest.

        桶名称 

        :param bucket_name: The bucket_name of this GetObjectRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_key(self):
        """Gets the object_key of this GetObjectRequest.

        通过此请求下载的对象名称。 

        :return: The object_key of this GetObjectRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this GetObjectRequest.

        通过此请求下载的对象名称。 

        :param object_key: The object_key of this GetObjectRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def date(self):
        """Gets the date of this GetObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this GetObjectRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this GetObjectRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this GetObjectRequest.
        :type date: str
        """
        self._date = date

    @property
    def response_content_type(self):
        """Gets the response_content_type of this GetObjectRequest.

        重写响应中的Content-Type头。 

        :return: The response_content_type of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_type

    @response_content_type.setter
    def response_content_type(self, response_content_type):
        """Sets the response_content_type of this GetObjectRequest.

        重写响应中的Content-Type头。 

        :param response_content_type: The response_content_type of this GetObjectRequest.
        :type response_content_type: str
        """
        self._response_content_type = response_content_type

    @property
    def response_content_language(self):
        """Gets the response_content_language of this GetObjectRequest.

        重写响应中的Content-Language头。 

        :return: The response_content_language of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_language

    @response_content_language.setter
    def response_content_language(self, response_content_language):
        """Sets the response_content_language of this GetObjectRequest.

        重写响应中的Content-Language头。 

        :param response_content_language: The response_content_language of this GetObjectRequest.
        :type response_content_language: str
        """
        self._response_content_language = response_content_language

    @property
    def response_expires(self):
        """Gets the response_expires of this GetObjectRequest.

        重写响应中的Expires头。 

        :return: The response_expires of this GetObjectRequest.
        :rtype: str
        """
        return self._response_expires

    @response_expires.setter
    def response_expires(self, response_expires):
        """Sets the response_expires of this GetObjectRequest.

        重写响应中的Expires头。 

        :param response_expires: The response_expires of this GetObjectRequest.
        :type response_expires: str
        """
        self._response_expires = response_expires

    @property
    def response_cache_control(self):
        """Gets the response_cache_control of this GetObjectRequest.

        重写响应中的Cache-Control头。 

        :return: The response_cache_control of this GetObjectRequest.
        :rtype: str
        """
        return self._response_cache_control

    @response_cache_control.setter
    def response_cache_control(self, response_cache_control):
        """Sets the response_cache_control of this GetObjectRequest.

        重写响应中的Cache-Control头。 

        :param response_cache_control: The response_cache_control of this GetObjectRequest.
        :type response_cache_control: str
        """
        self._response_cache_control = response_cache_control

    @property
    def response_content_disposition(self):
        """Gets the response_content_disposition of this GetObjectRequest.

        重写响应中的Content-Disposition头。  示例：response-content-disposition=attachment; filename*=utf-8''name1  下载对象重命名为“name1”，如果name1中存在中文，需要将中文进行URL编码。 

        :return: The response_content_disposition of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_disposition

    @response_content_disposition.setter
    def response_content_disposition(self, response_content_disposition):
        """Sets the response_content_disposition of this GetObjectRequest.

        重写响应中的Content-Disposition头。  示例：response-content-disposition=attachment; filename*=utf-8''name1  下载对象重命名为“name1”，如果name1中存在中文，需要将中文进行URL编码。 

        :param response_content_disposition: The response_content_disposition of this GetObjectRequest.
        :type response_content_disposition: str
        """
        self._response_content_disposition = response_content_disposition

    @property
    def response_content_encoding(self):
        """Gets the response_content_encoding of this GetObjectRequest.

        重写响应中的Content-Encoding头。 

        :return: The response_content_encoding of this GetObjectRequest.
        :rtype: str
        """
        return self._response_content_encoding

    @response_content_encoding.setter
    def response_content_encoding(self, response_content_encoding):
        """Sets the response_content_encoding of this GetObjectRequest.

        重写响应中的Content-Encoding头。 

        :param response_content_encoding: The response_content_encoding of this GetObjectRequest.
        :type response_content_encoding: str
        """
        self._response_content_encoding = response_content_encoding

    @property
    def version_id(self):
        """Gets the version_id of this GetObjectRequest.

        指定获取对象的版本号。 

        :return: The version_id of this GetObjectRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this GetObjectRequest.

        指定获取对象的版本号。 

        :param version_id: The version_id of this GetObjectRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def x_image_process(self):
        """Gets the x_image_process of this GetObjectRequest.

        图片处理服务。  示例：  命令方式：x-image-process=image/commands  样式方式：x-image-process=style/stylename  详见[《图片处理特性指南》](https://support.huaweicloud.com/fg-obs/obs_01_0001.html)。 

        :return: The x_image_process of this GetObjectRequest.
        :rtype: str
        """
        return self._x_image_process

    @x_image_process.setter
    def x_image_process(self, x_image_process):
        """Sets the x_image_process of this GetObjectRequest.

        图片处理服务。  示例：  命令方式：x-image-process=image/commands  样式方式：x-image-process=style/stylename  详见[《图片处理特性指南》](https://support.huaweicloud.com/fg-obs/obs_01_0001.html)。 

        :param x_image_process: The x_image_process of this GetObjectRequest.
        :type x_image_process: str
        """
        self._x_image_process = x_image_process

    @property
    def attname(self):
        """Gets the attname of this GetObjectRequest.

        重写响应中的Content-Disposition头。  示例：attname=name1  下载对象重命名为“name1”。 

        :return: The attname of this GetObjectRequest.
        :rtype: str
        """
        return self._attname

    @attname.setter
    def attname(self, attname):
        """Sets the attname of this GetObjectRequest.

        重写响应中的Content-Disposition头。  示例：attname=name1  下载对象重命名为“name1”。 

        :param attname: The attname of this GetObjectRequest.
        :type attname: str
        """
        self._attname = attname

    @property
    def range(self):
        """Gets the range of this GetObjectRequest.

        获取对象时，获取在Range范围内的对象内容。如果Range不合法则忽略此字段获取整个对象。  Range是一个范围，它的起始值最小为0，最大为对象长度减1。Range范围的起始值为必填项，如果Range只包含起始值，表示获取起始值到对象长度减1这个区间的对象内容。  携带Range头域后，响应消息的ETag仍是对象的ETag，而不是Range范围内对象的ETag。  bytes=byte_range  示例1：bytes=0-4 示例2：bytes=1024 示例3：bytes=10-20,30-40（表示多个区间） 

        :return: The range of this GetObjectRequest.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetObjectRequest.

        获取对象时，获取在Range范围内的对象内容。如果Range不合法则忽略此字段获取整个对象。  Range是一个范围，它的起始值最小为0，最大为对象长度减1。Range范围的起始值为必填项，如果Range只包含起始值，表示获取起始值到对象长度减1这个区间的对象内容。  携带Range头域后，响应消息的ETag仍是对象的ETag，而不是Range范围内对象的ETag。  bytes=byte_range  示例1：bytes=0-4 示例2：bytes=1024 示例3：bytes=10-20,30-40（表示多个区间） 

        :param range: The range of this GetObjectRequest.
        :type range: str
        """
        self._range = range

    @property
    def if_modified_since(self):
        """Gets the if_modified_since of this GetObjectRequest.

        如果对象在请求中指定的时间之后有修改，则返回对象内容；否则的话返回304（not modified）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 

        :return: The if_modified_since of this GetObjectRequest.
        :rtype: str
        """
        return self._if_modified_since

    @if_modified_since.setter
    def if_modified_since(self, if_modified_since):
        """Sets the if_modified_since of this GetObjectRequest.

        如果对象在请求中指定的时间之后有修改，则返回对象内容；否则的话返回304（not modified）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 

        :param if_modified_since: The if_modified_since of this GetObjectRequest.
        :type if_modified_since: str
        """
        self._if_modified_since = if_modified_since

    @property
    def if_unmodified_since(self):
        """Gets the if_unmodified_since of this GetObjectRequest.

        如果对象在请求中指定的时间之后没有修改，则返回对象内容；否则的话返回412（precondition failed）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 

        :return: The if_unmodified_since of this GetObjectRequest.
        :rtype: str
        """
        return self._if_unmodified_since

    @if_unmodified_since.setter
    def if_unmodified_since(self, if_unmodified_since):
        """Sets the if_unmodified_since of this GetObjectRequest.

        如果对象在请求中指定的时间之后没有修改，则返回对象内容；否则的话返回412（precondition failed）。  类型：符合http://www.ietf.org/rfc/rfc2616.txt规定格式的HTTP时间字符串。 

        :param if_unmodified_since: The if_unmodified_since of this GetObjectRequest.
        :type if_unmodified_since: str
        """
        self._if_unmodified_since = if_unmodified_since

    @property
    def if_match(self):
        """Gets the if_match of this GetObjectRequest.

        如果对象的ETag和请求中指定的ETag相同，则返回对象内容，否则的话返回412（precondition failed）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 

        :return: The if_match of this GetObjectRequest.
        :rtype: str
        """
        return self._if_match

    @if_match.setter
    def if_match(self, if_match):
        """Sets the if_match of this GetObjectRequest.

        如果对象的ETag和请求中指定的ETag相同，则返回对象内容，否则的话返回412（precondition failed）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 

        :param if_match: The if_match of this GetObjectRequest.
        :type if_match: str
        """
        self._if_match = if_match

    @property
    def if_none_match(self):
        """Gets the if_none_match of this GetObjectRequest.

        如果对象的ETag和请求中指定的ETag不相同，则返回对象内容，否则的话返回304（not modified）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 

        :return: The if_none_match of this GetObjectRequest.
        :rtype: str
        """
        return self._if_none_match

    @if_none_match.setter
    def if_none_match(self, if_none_match):
        """Sets the if_none_match of this GetObjectRequest.

        如果对象的ETag和请求中指定的ETag不相同，则返回对象内容，否则的话返回304（not modified）。  （ETag值，例：0f64741bf7cb1089e988e4585d0d3434。） 

        :param if_none_match: The if_none_match of this GetObjectRequest.
        :type if_none_match: str
        """
        self._if_none_match = if_none_match

    @property
    def x_obs_server_side_encryption_customer_algorithm(self):
        """Gets the x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_algorithm

    @x_obs_server_side_encryption_customer_algorithm.setter
    def x_obs_server_side_encryption_customer_algorithm(self, x_obs_server_side_encryption_customer_algorithm):
        """Sets the x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的算法。  示例：x-obs-server-side-encryption-customer-algorithm：AES256  约束：需要和x-obs-server-side-encryption-customer-key， x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_algorithm: The x_obs_server_side_encryption_customer_algorithm of this GetObjectRequest.
        :type x_obs_server_side_encryption_customer_algorithm: str
        """
        self._x_obs_server_side_encryption_customer_algorithm = x_obs_server_side_encryption_customer_algorithm

    @property
    def x_obs_server_side_encryption_customer_key(self):
        """Gets the x_obs_server_side_encryption_customer_key of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于解密对象。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :return: The x_obs_server_side_encryption_customer_key of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key

    @x_obs_server_side_encryption_customer_key.setter
    def x_obs_server_side_encryption_customer_key(self, x_obs_server_side_encryption_customer_key):
        """Sets the x_obs_server_side_encryption_customer_key of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥。该密钥用于解密对象。  示例：x-obs-server-side-encryption-customer-key:K7QkYpBkM5+hca27fsNkUnNVaobncnLht/rCB2o/9Cw=  约束：该头域由256-bit的密钥经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key-MD5一起使用。 

        :param x_obs_server_side_encryption_customer_key: The x_obs_server_side_encryption_customer_key of this GetObjectRequest.
        :type x_obs_server_side_encryption_customer_key: str
        """
        self._x_obs_server_side_encryption_customer_key = x_obs_server_side_encryption_customer_key

    @property
    def x_obs_server_side_encryption_customer_key_md5(self):
        """Gets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

        :return: The x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.
        :rtype: str
        """
        return self._x_obs_server_side_encryption_customer_key_md5

    @x_obs_server_side_encryption_customer_key_md5.setter
    def x_obs_server_side_encryption_customer_key_md5(self, x_obs_server_side_encryption_customer_key_md5):
        """Sets the x_obs_server_side_encryption_customer_key_md5 of this GetObjectRequest.

        SSE-C方式下使用该头域，该头域表示加密使用的密钥的MD5值。MD5值用于验证密钥传输过程中没有出错。  示例：x-obs-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==  约束：该头域由密钥的128-bit MD5值经过base64-encoded得到，需要和x-obs-server-side-encryption-customer-algorithm，x-obs-server-side-encryption-customer-key一起使用。 

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
