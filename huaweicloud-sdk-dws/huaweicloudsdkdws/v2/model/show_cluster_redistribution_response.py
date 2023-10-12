# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRedistributionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redis_info': 'RdsRedisInfo',
        'schedule_mode': 'bool',
        'pause_enable': 'bool',
        'recover_enable': 'bool',
        'retry_enable': 'bool',
        'update_enable': 'bool',
        'control_enable': 'bool'
    }

    attribute_map = {
        'redis_info': 'redis_info',
        'schedule_mode': 'schedule_mode',
        'pause_enable': 'pause_enable',
        'recover_enable': 'recover_enable',
        'retry_enable': 'retry_enable',
        'update_enable': 'update_enable',
        'control_enable': 'control_enable'
    }

    def __init__(self, redis_info=None, schedule_mode=None, pause_enable=None, recover_enable=None, retry_enable=None, update_enable=None, control_enable=None):
        """ShowClusterRedistributionResponse

        The model defined in huaweicloud sdk

        :param redis_info: 
        :type redis_info: :class:`huaweicloudsdkdws.v2.RdsRedisInfo`
        :param schedule_mode: 调度模式
        :type schedule_mode: bool
        :param pause_enable: 是否允许暂停
        :type pause_enable: bool
        :param recover_enable: 是否允许恢复
        :type recover_enable: bool
        :param retry_enable: 是否允许重试
        :type retry_enable: bool
        :param update_enable: 是否允许更新
        :type update_enable: bool
        :param control_enable: 是否允许控制
        :type control_enable: bool
        """
        
        super(ShowClusterRedistributionResponse, self).__init__()

        self._redis_info = None
        self._schedule_mode = None
        self._pause_enable = None
        self._recover_enable = None
        self._retry_enable = None
        self._update_enable = None
        self._control_enable = None
        self.discriminator = None

        if redis_info is not None:
            self.redis_info = redis_info
        if schedule_mode is not None:
            self.schedule_mode = schedule_mode
        if pause_enable is not None:
            self.pause_enable = pause_enable
        if recover_enable is not None:
            self.recover_enable = recover_enable
        if retry_enable is not None:
            self.retry_enable = retry_enable
        if update_enable is not None:
            self.update_enable = update_enable
        if control_enable is not None:
            self.control_enable = control_enable

    @property
    def redis_info(self):
        """Gets the redis_info of this ShowClusterRedistributionResponse.

        :return: The redis_info of this ShowClusterRedistributionResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.RdsRedisInfo`
        """
        return self._redis_info

    @redis_info.setter
    def redis_info(self, redis_info):
        """Sets the redis_info of this ShowClusterRedistributionResponse.

        :param redis_info: The redis_info of this ShowClusterRedistributionResponse.
        :type redis_info: :class:`huaweicloudsdkdws.v2.RdsRedisInfo`
        """
        self._redis_info = redis_info

    @property
    def schedule_mode(self):
        """Gets the schedule_mode of this ShowClusterRedistributionResponse.

        调度模式

        :return: The schedule_mode of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._schedule_mode

    @schedule_mode.setter
    def schedule_mode(self, schedule_mode):
        """Sets the schedule_mode of this ShowClusterRedistributionResponse.

        调度模式

        :param schedule_mode: The schedule_mode of this ShowClusterRedistributionResponse.
        :type schedule_mode: bool
        """
        self._schedule_mode = schedule_mode

    @property
    def pause_enable(self):
        """Gets the pause_enable of this ShowClusterRedistributionResponse.

        是否允许暂停

        :return: The pause_enable of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._pause_enable

    @pause_enable.setter
    def pause_enable(self, pause_enable):
        """Sets the pause_enable of this ShowClusterRedistributionResponse.

        是否允许暂停

        :param pause_enable: The pause_enable of this ShowClusterRedistributionResponse.
        :type pause_enable: bool
        """
        self._pause_enable = pause_enable

    @property
    def recover_enable(self):
        """Gets the recover_enable of this ShowClusterRedistributionResponse.

        是否允许恢复

        :return: The recover_enable of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._recover_enable

    @recover_enable.setter
    def recover_enable(self, recover_enable):
        """Sets the recover_enable of this ShowClusterRedistributionResponse.

        是否允许恢复

        :param recover_enable: The recover_enable of this ShowClusterRedistributionResponse.
        :type recover_enable: bool
        """
        self._recover_enable = recover_enable

    @property
    def retry_enable(self):
        """Gets the retry_enable of this ShowClusterRedistributionResponse.

        是否允许重试

        :return: The retry_enable of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._retry_enable

    @retry_enable.setter
    def retry_enable(self, retry_enable):
        """Sets the retry_enable of this ShowClusterRedistributionResponse.

        是否允许重试

        :param retry_enable: The retry_enable of this ShowClusterRedistributionResponse.
        :type retry_enable: bool
        """
        self._retry_enable = retry_enable

    @property
    def update_enable(self):
        """Gets the update_enable of this ShowClusterRedistributionResponse.

        是否允许更新

        :return: The update_enable of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._update_enable

    @update_enable.setter
    def update_enable(self, update_enable):
        """Sets the update_enable of this ShowClusterRedistributionResponse.

        是否允许更新

        :param update_enable: The update_enable of this ShowClusterRedistributionResponse.
        :type update_enable: bool
        """
        self._update_enable = update_enable

    @property
    def control_enable(self):
        """Gets the control_enable of this ShowClusterRedistributionResponse.

        是否允许控制

        :return: The control_enable of this ShowClusterRedistributionResponse.
        :rtype: bool
        """
        return self._control_enable

    @control_enable.setter
    def control_enable(self, control_enable):
        """Sets the control_enable of this ShowClusterRedistributionResponse.

        是否允许控制

        :param control_enable: The control_enable of this ShowClusterRedistributionResponse.
        :type control_enable: bool
        """
        self._control_enable = control_enable

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
        if not isinstance(other, ShowClusterRedistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
