# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectoryTraversalProtectionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'PolicyAction',
        'time_range': 'int',
        'num_requests': 'int',
        'not_found_status_percentage': 'int',
        'num_non_existent_directories': 'int',
        'blocking_period': 'int'
    }

    attribute_map = {
        'action': 'action',
        'time_range': 'time_range',
        'num_requests': 'num_requests',
        'not_found_status_percentage': 'not_found_status_percentage',
        'num_non_existent_directories': 'num_non_existent_directories',
        'blocking_period': 'blocking_period'
    }

    def __init__(self, action=None, time_range=None, num_requests=None, not_found_status_percentage=None, num_non_existent_directories=None, blocking_period=None):
        r"""DirectoryTraversalProtectionConfig

        The model defined in huaweicloud sdk

        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        :param time_range: 检测时间范围，单位秒
        :type time_range: int
        :param num_requests: 请求数阈值，在检测时间内请求数超过该值则触发防护
        :type num_requests: int
        :param not_found_status_percentage: 404状态码占比阈值，单位为百分比
        :type not_found_status_percentage: int
        :param num_non_existent_directories: 不存在目录数阈值，在检测时间内探测到不存在目录的数量达到该值时触发防护
        :type num_non_existent_directories: int
        :param blocking_period: 封禁周期，单位秒
        :type blocking_period: int
        """
        
        

        self._action = None
        self._time_range = None
        self._num_requests = None
        self._not_found_status_percentage = None
        self._num_non_existent_directories = None
        self._blocking_period = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if time_range is not None:
            self.time_range = time_range
        if num_requests is not None:
            self.num_requests = num_requests
        if not_found_status_percentage is not None:
            self.not_found_status_percentage = not_found_status_percentage
        if num_non_existent_directories is not None:
            self.num_non_existent_directories = num_non_existent_directories
        if blocking_period is not None:
            self.blocking_period = blocking_period

    @property
    def action(self):
        r"""Gets the action of this DirectoryTraversalProtectionConfig.

        :return: The action of this DirectoryTraversalProtectionConfig.
        :rtype: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this DirectoryTraversalProtectionConfig.

        :param action: The action of this DirectoryTraversalProtectionConfig.
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        self._action = action

    @property
    def time_range(self):
        r"""Gets the time_range of this DirectoryTraversalProtectionConfig.

        检测时间范围，单位秒

        :return: The time_range of this DirectoryTraversalProtectionConfig.
        :rtype: int
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this DirectoryTraversalProtectionConfig.

        检测时间范围，单位秒

        :param time_range: The time_range of this DirectoryTraversalProtectionConfig.
        :type time_range: int
        """
        self._time_range = time_range

    @property
    def num_requests(self):
        r"""Gets the num_requests of this DirectoryTraversalProtectionConfig.

        请求数阈值，在检测时间内请求数超过该值则触发防护

        :return: The num_requests of this DirectoryTraversalProtectionConfig.
        :rtype: int
        """
        return self._num_requests

    @num_requests.setter
    def num_requests(self, num_requests):
        r"""Sets the num_requests of this DirectoryTraversalProtectionConfig.

        请求数阈值，在检测时间内请求数超过该值则触发防护

        :param num_requests: The num_requests of this DirectoryTraversalProtectionConfig.
        :type num_requests: int
        """
        self._num_requests = num_requests

    @property
    def not_found_status_percentage(self):
        r"""Gets the not_found_status_percentage of this DirectoryTraversalProtectionConfig.

        404状态码占比阈值，单位为百分比

        :return: The not_found_status_percentage of this DirectoryTraversalProtectionConfig.
        :rtype: int
        """
        return self._not_found_status_percentage

    @not_found_status_percentage.setter
    def not_found_status_percentage(self, not_found_status_percentage):
        r"""Sets the not_found_status_percentage of this DirectoryTraversalProtectionConfig.

        404状态码占比阈值，单位为百分比

        :param not_found_status_percentage: The not_found_status_percentage of this DirectoryTraversalProtectionConfig.
        :type not_found_status_percentage: int
        """
        self._not_found_status_percentage = not_found_status_percentage

    @property
    def num_non_existent_directories(self):
        r"""Gets the num_non_existent_directories of this DirectoryTraversalProtectionConfig.

        不存在目录数阈值，在检测时间内探测到不存在目录的数量达到该值时触发防护

        :return: The num_non_existent_directories of this DirectoryTraversalProtectionConfig.
        :rtype: int
        """
        return self._num_non_existent_directories

    @num_non_existent_directories.setter
    def num_non_existent_directories(self, num_non_existent_directories):
        r"""Sets the num_non_existent_directories of this DirectoryTraversalProtectionConfig.

        不存在目录数阈值，在检测时间内探测到不存在目录的数量达到该值时触发防护

        :param num_non_existent_directories: The num_non_existent_directories of this DirectoryTraversalProtectionConfig.
        :type num_non_existent_directories: int
        """
        self._num_non_existent_directories = num_non_existent_directories

    @property
    def blocking_period(self):
        r"""Gets the blocking_period of this DirectoryTraversalProtectionConfig.

        封禁周期，单位秒

        :return: The blocking_period of this DirectoryTraversalProtectionConfig.
        :rtype: int
        """
        return self._blocking_period

    @blocking_period.setter
    def blocking_period(self, blocking_period):
        r"""Sets the blocking_period of this DirectoryTraversalProtectionConfig.

        封禁周期，单位秒

        :param blocking_period: The blocking_period of this DirectoryTraversalProtectionConfig.
        :type blocking_period: int
        """
        self._blocking_period = blocking_period

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DirectoryTraversalProtectionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
