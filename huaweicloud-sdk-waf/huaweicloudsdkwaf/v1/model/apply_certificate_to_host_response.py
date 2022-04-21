# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyCertificateToHostResponse(SdkResponse):

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
        'timestamp': 'int',
        'expire_time': 'int',
        'bind_host': 'list[CertificateBundingHostBody]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'timestamp': 'timestamp',
        'expire_time': 'expire_time',
        'bind_host': 'bind_host'
    }

    def __init__(self, id=None, name=None, timestamp=None, expire_time=None, bind_host=None):
        """ApplyCertificateToHostResponse

        The model defined in huaweicloud sdk

        :param id: 证书id
        :type id: str
        :param name: 证书名
        :type name: str
        :param timestamp: 时间戳
        :type timestamp: int
        :param expire_time: 过期时间
        :type expire_time: int
        :param bind_host: 绑定域名列表
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.CertificateBundingHostBody`]
        """
        
        super(ApplyCertificateToHostResponse, self).__init__()

        self._id = None
        self._name = None
        self._timestamp = None
        self._expire_time = None
        self._bind_host = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if timestamp is not None:
            self.timestamp = timestamp
        if expire_time is not None:
            self.expire_time = expire_time
        if bind_host is not None:
            self.bind_host = bind_host

    @property
    def id(self):
        """Gets the id of this ApplyCertificateToHostResponse.

        证书id

        :return: The id of this ApplyCertificateToHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplyCertificateToHostResponse.

        证书id

        :param id: The id of this ApplyCertificateToHostResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplyCertificateToHostResponse.

        证书名

        :return: The name of this ApplyCertificateToHostResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplyCertificateToHostResponse.

        证书名

        :param name: The name of this ApplyCertificateToHostResponse.
        :type name: str
        """
        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this ApplyCertificateToHostResponse.

        时间戳

        :return: The timestamp of this ApplyCertificateToHostResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApplyCertificateToHostResponse.

        时间戳

        :param timestamp: The timestamp of this ApplyCertificateToHostResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def expire_time(self):
        """Gets the expire_time of this ApplyCertificateToHostResponse.

        过期时间

        :return: The expire_time of this ApplyCertificateToHostResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this ApplyCertificateToHostResponse.

        过期时间

        :param expire_time: The expire_time of this ApplyCertificateToHostResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def bind_host(self):
        """Gets the bind_host of this ApplyCertificateToHostResponse.

        绑定域名列表

        :return: The bind_host of this ApplyCertificateToHostResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CertificateBundingHostBody`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this ApplyCertificateToHostResponse.

        绑定域名列表

        :param bind_host: The bind_host of this ApplyCertificateToHostResponse.
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.CertificateBundingHostBody`]
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
        if not isinstance(other, ApplyCertificateToHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
