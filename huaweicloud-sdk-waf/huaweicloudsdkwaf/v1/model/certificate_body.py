# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateBody:

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
        'expire_time': 'int',
        'exp_status': 'int',
        'timestamp': 'int',
        'bind_host': 'list[BindHost]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'expire_time': 'expire_time',
        'exp_status': 'exp_status',
        'timestamp': 'timestamp',
        'bind_host': 'bind_host'
    }

    def __init__(self, id=None, name=None, expire_time=None, exp_status=None, timestamp=None, bind_host=None):
        """CertificateBody

        The model defined in huaweicloud sdk

        :param id: 证书id
        :type id: str
        :param name: 证书名
        :type name: str
        :param expire_time: 证书过期时间戳
        :type expire_time: int
        :param exp_status: 证书过期状态，0-未过期，1-已过期，2-即将过期（一个月内即将过期）
        :type exp_status: int
        :param timestamp: 证书上传时间戳
        :type timestamp: int
        :param bind_host: 证书关联的域名信息
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        
        

        self._id = None
        self._name = None
        self._expire_time = None
        self._exp_status = None
        self._timestamp = None
        self._bind_host = None
        self.discriminator = None

        self.id = id
        self.name = name
        if expire_time is not None:
            self.expire_time = expire_time
        if exp_status is not None:
            self.exp_status = exp_status
        self.timestamp = timestamp
        if bind_host is not None:
            self.bind_host = bind_host

    @property
    def id(self):
        """Gets the id of this CertificateBody.

        证书id

        :return: The id of this CertificateBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateBody.

        证书id

        :param id: The id of this CertificateBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CertificateBody.

        证书名

        :return: The name of this CertificateBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateBody.

        证书名

        :param name: The name of this CertificateBody.
        :type name: str
        """
        self._name = name

    @property
    def expire_time(self):
        """Gets the expire_time of this CertificateBody.

        证书过期时间戳

        :return: The expire_time of this CertificateBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CertificateBody.

        证书过期时间戳

        :param expire_time: The expire_time of this CertificateBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def exp_status(self):
        """Gets the exp_status of this CertificateBody.

        证书过期状态，0-未过期，1-已过期，2-即将过期（一个月内即将过期）

        :return: The exp_status of this CertificateBody.
        :rtype: int
        """
        return self._exp_status

    @exp_status.setter
    def exp_status(self, exp_status):
        """Sets the exp_status of this CertificateBody.

        证书过期状态，0-未过期，1-已过期，2-即将过期（一个月内即将过期）

        :param exp_status: The exp_status of this CertificateBody.
        :type exp_status: int
        """
        self._exp_status = exp_status

    @property
    def timestamp(self):
        """Gets the timestamp of this CertificateBody.

        证书上传时间戳

        :return: The timestamp of this CertificateBody.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CertificateBody.

        证书上传时间戳

        :param timestamp: The timestamp of this CertificateBody.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def bind_host(self):
        """Gets the bind_host of this CertificateBody.

        证书关联的域名信息

        :return: The bind_host of this CertificateBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this CertificateBody.

        证书关联的域名信息

        :param bind_host: The bind_host of this CertificateBody.
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
        if not isinstance(other, CertificateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
