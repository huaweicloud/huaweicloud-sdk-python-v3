# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvTopoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_env_id': 'int',
        'direction': 'str',
        'end_time': 'str',
        'start_time': 'str',
        'filter_user': 'bool'
    }

    attribute_map = {
        'target_env_id': 'target_env_id',
        'direction': 'direction',
        'end_time': 'end_time',
        'start_time': 'start_time',
        'filter_user': 'filter_user'
    }

    def __init__(self, target_env_id=None, direction=None, end_time=None, start_time=None, filter_user=None):
        """EnvTopoRequest

        The model defined in huaweicloud sdk

        :param target_env_id: 环境id。
        :type target_env_id: int
        :param direction: 方向，可为空。
        :type direction: str
        :param end_time: 结束时间。
        :type end_time: str
        :param start_time: 开始时间。
        :type start_time: str
        :param filter_user: 过滤。
        :type filter_user: bool
        """
        
        

        self._target_env_id = None
        self._direction = None
        self._end_time = None
        self._start_time = None
        self._filter_user = None
        self.discriminator = None

        self.target_env_id = target_env_id
        if direction is not None:
            self.direction = direction
        self.end_time = end_time
        self.start_time = start_time
        if filter_user is not None:
            self.filter_user = filter_user

    @property
    def target_env_id(self):
        """Gets the target_env_id of this EnvTopoRequest.

        环境id。

        :return: The target_env_id of this EnvTopoRequest.
        :rtype: int
        """
        return self._target_env_id

    @target_env_id.setter
    def target_env_id(self, target_env_id):
        """Sets the target_env_id of this EnvTopoRequest.

        环境id。

        :param target_env_id: The target_env_id of this EnvTopoRequest.
        :type target_env_id: int
        """
        self._target_env_id = target_env_id

    @property
    def direction(self):
        """Gets the direction of this EnvTopoRequest.

        方向，可为空。

        :return: The direction of this EnvTopoRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this EnvTopoRequest.

        方向，可为空。

        :param direction: The direction of this EnvTopoRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def end_time(self):
        """Gets the end_time of this EnvTopoRequest.

        结束时间。

        :return: The end_time of this EnvTopoRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EnvTopoRequest.

        结束时间。

        :param end_time: The end_time of this EnvTopoRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this EnvTopoRequest.

        开始时间。

        :return: The start_time of this EnvTopoRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EnvTopoRequest.

        开始时间。

        :param start_time: The start_time of this EnvTopoRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def filter_user(self):
        """Gets the filter_user of this EnvTopoRequest.

        过滤。

        :return: The filter_user of this EnvTopoRequest.
        :rtype: bool
        """
        return self._filter_user

    @filter_user.setter
    def filter_user(self, filter_user):
        """Sets the filter_user of this EnvTopoRequest.

        过滤。

        :param filter_user: The filter_user of this EnvTopoRequest.
        :type filter_user: bool
        """
        self._filter_user = filter_user

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
        if not isinstance(other, EnvTopoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
