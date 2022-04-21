# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpireVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expiration': 'int',
        'instance_id': 'str',
        'interval': 'int'
    }

    attribute_map = {
        'expiration': 'expiration',
        'instance_id': 'instance_id',
        'interval': 'interval'
    }

    def __init__(self, expiration=None, instance_id=None, interval=None):
        """ExpireVo

        The model defined in huaweicloud sdk

        :param expiration: 过期时间。UNIX时间戳，单位毫秒。eg:1635905480465
        :type expiration: int
        :param instance_id: CloudIDE实例id
        :type instance_id: str
        :param interval: CloudIDE实例自动休眠时长，单位‘分钟’
        :type interval: int
        """
        
        

        self._expiration = None
        self._instance_id = None
        self._interval = None
        self.discriminator = None

        if expiration is not None:
            self.expiration = expiration
        if instance_id is not None:
            self.instance_id = instance_id
        if interval is not None:
            self.interval = interval

    @property
    def expiration(self):
        """Gets the expiration of this ExpireVo.

        过期时间。UNIX时间戳，单位毫秒。eg:1635905480465

        :return: The expiration of this ExpireVo.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this ExpireVo.

        过期时间。UNIX时间戳，单位毫秒。eg:1635905480465

        :param expiration: The expiration of this ExpireVo.
        :type expiration: int
        """
        self._expiration = expiration

    @property
    def instance_id(self):
        """Gets the instance_id of this ExpireVo.

        CloudIDE实例id

        :return: The instance_id of this ExpireVo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExpireVo.

        CloudIDE实例id

        :param instance_id: The instance_id of this ExpireVo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def interval(self):
        """Gets the interval of this ExpireVo.

        CloudIDE实例自动休眠时长，单位‘分钟’

        :return: The interval of this ExpireVo.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ExpireVo.

        CloudIDE实例自动休眠时长，单位‘分钟’

        :param interval: The interval of this ExpireVo.
        :type interval: int
        """
        self._interval = interval

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
        if not isinstance(other, ExpireVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
