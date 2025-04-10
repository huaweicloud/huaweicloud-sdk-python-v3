# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'timestamp': 'int',
        'user_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'time': 'time',
        'timestamp': 'timestamp',
        'user_id': 'user_id',
        'user_name': 'user_name'
    }

    def __init__(self, time=None, timestamp=None, user_id=None, user_name=None):
        r"""CreateInfoVo

        The model defined in huaweicloud sdk

        :param time: 创建时间
        :type time: str
        :param timestamp: 创建时间时间戳
        :type timestamp: int
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        """
        
        

        self._time = None
        self._timestamp = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if timestamp is not None:
            self.timestamp = timestamp
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def time(self):
        r"""Gets the time of this CreateInfoVo.

        创建时间

        :return: The time of this CreateInfoVo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this CreateInfoVo.

        创建时间

        :param time: The time of this CreateInfoVo.
        :type time: str
        """
        self._time = time

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateInfoVo.

        创建时间时间戳

        :return: The timestamp of this CreateInfoVo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateInfoVo.

        创建时间时间戳

        :param timestamp: The timestamp of this CreateInfoVo.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateInfoVo.

        用户ID

        :return: The user_id of this CreateInfoVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateInfoVo.

        用户ID

        :param user_id: The user_id of this CreateInfoVo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateInfoVo.

        用户名称

        :return: The user_name of this CreateInfoVo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateInfoVo.

        用户名称

        :param user_name: The user_name of this CreateInfoVo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, CreateInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
