# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateResponse(SdkResponse):

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
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'expire_time': 'expire_time',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, name=None, expire_time=None, timestamp=None):
        """UpdateCertificateResponse

        The model defined in huaweicloud sdk

        :param id: 证书ID
        :type id: str
        :param name: 证书名
        :type name: str
        :param expire_time: 证书过期时间戳
        :type expire_time: int
        :param timestamp: 时间戳
        :type timestamp: int
        """
        
        super(UpdateCertificateResponse, self).__init__()

        self._id = None
        self._name = None
        self._expire_time = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if expire_time is not None:
            self.expire_time = expire_time
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this UpdateCertificateResponse.

        证书ID

        :return: The id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateCertificateResponse.

        证书ID

        :param id: The id of this UpdateCertificateResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateCertificateResponse.

        证书名

        :return: The name of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateResponse.

        证书名

        :param name: The name of this UpdateCertificateResponse.
        :type name: str
        """
        self._name = name

    @property
    def expire_time(self):
        """Gets the expire_time of this UpdateCertificateResponse.

        证书过期时间戳

        :return: The expire_time of this UpdateCertificateResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UpdateCertificateResponse.

        证书过期时间戳

        :param expire_time: The expire_time of this UpdateCertificateResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateCertificateResponse.

        时间戳

        :return: The timestamp of this UpdateCertificateResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateCertificateResponse.

        时间戳

        :param timestamp: The timestamp of this UpdateCertificateResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, UpdateCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
