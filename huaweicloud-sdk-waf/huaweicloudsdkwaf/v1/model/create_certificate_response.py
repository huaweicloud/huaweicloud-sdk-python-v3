# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'content': 'str',
        'key': 'str',
        'expire_time': 'int',
        'exp_status': 'int',
        'timestamp': 'int',
        'bind_host': 'list[BindHost]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'content': 'content',
        'key': 'key',
        'expire_time': 'expire_time',
        'exp_status': 'exp_status',
        'timestamp': 'timestamp',
        'bind_host': 'bind_host'
    }

    def __init__(self, id=None, name=None, content=None, key=None, expire_time=None, exp_status=None, timestamp=None, bind_host=None):
        """CreateCertificateResponse

        The model defined in huaweicloud sdk

        :param id: 证书ID
        :type id: str
        :param name: 证书名
        :type name: str
        :param content: 证书文件，PEM编码
        :type content: str
        :param key: 证书私钥，PEM编码
        :type key: str
        :param expire_time: 证书过期时间戳
        :type expire_time: int
        :param exp_status: 证书过期状态，0-未过期，1-已过期，2-即将过期
        :type exp_status: int
        :param timestamp: 证书上传时间戳
        :type timestamp: int
        :param bind_host: 证书关联的域名信息
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        
        super(CreateCertificateResponse, self).__init__()

        self._id = None
        self._name = None
        self._content = None
        self._key = None
        self._expire_time = None
        self._exp_status = None
        self._timestamp = None
        self._bind_host = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if key is not None:
            self.key = key
        if expire_time is not None:
            self.expire_time = expire_time
        if exp_status is not None:
            self.exp_status = exp_status
        if timestamp is not None:
            self.timestamp = timestamp
        if bind_host is not None:
            self.bind_host = bind_host

    @property
    def id(self):
        """Gets the id of this CreateCertificateResponse.

        证书ID

        :return: The id of this CreateCertificateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCertificateResponse.

        证书ID

        :param id: The id of this CreateCertificateResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateCertificateResponse.

        证书名

        :return: The name of this CreateCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCertificateResponse.

        证书名

        :param name: The name of this CreateCertificateResponse.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this CreateCertificateResponse.

        证书文件，PEM编码

        :return: The content of this CreateCertificateResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateCertificateResponse.

        证书文件，PEM编码

        :param content: The content of this CreateCertificateResponse.
        :type content: str
        """
        self._content = content

    @property
    def key(self):
        """Gets the key of this CreateCertificateResponse.

        证书私钥，PEM编码

        :return: The key of this CreateCertificateResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateCertificateResponse.

        证书私钥，PEM编码

        :param key: The key of this CreateCertificateResponse.
        :type key: str
        """
        self._key = key

    @property
    def expire_time(self):
        """Gets the expire_time of this CreateCertificateResponse.

        证书过期时间戳

        :return: The expire_time of this CreateCertificateResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CreateCertificateResponse.

        证书过期时间戳

        :param expire_time: The expire_time of this CreateCertificateResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def exp_status(self):
        """Gets the exp_status of this CreateCertificateResponse.

        证书过期状态，0-未过期，1-已过期，2-即将过期

        :return: The exp_status of this CreateCertificateResponse.
        :rtype: int
        """
        return self._exp_status

    @exp_status.setter
    def exp_status(self, exp_status):
        """Sets the exp_status of this CreateCertificateResponse.

        证书过期状态，0-未过期，1-已过期，2-即将过期

        :param exp_status: The exp_status of this CreateCertificateResponse.
        :type exp_status: int
        """
        self._exp_status = exp_status

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateCertificateResponse.

        证书上传时间戳

        :return: The timestamp of this CreateCertificateResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateCertificateResponse.

        证书上传时间戳

        :param timestamp: The timestamp of this CreateCertificateResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def bind_host(self):
        """Gets the bind_host of this CreateCertificateResponse.

        证书关联的域名信息

        :return: The bind_host of this CreateCertificateResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this CreateCertificateResponse.

        证书关联的域名信息

        :param bind_host: The bind_host of this CreateCertificateResponse.
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        self._bind_host = bind_host

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
        if not isinstance(other, CreateCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
