# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'view_config': 'TrendView',
        'instance_id': 'int',
        'monitor_item_id': 'int',
        'env_id': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'view_config': 'view_config',
        'instance_id': 'instance_id',
        'monitor_item_id': 'monitor_item_id',
        'env_id': 'env_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, view_config=None, instance_id=None, monitor_item_id=None, env_id=None, start_time=None, end_time=None):
        """TrendParam

        The model defined in huaweicloud sdk

        :param view_config: 
        :type view_config: :class:`huaweicloudsdkapm.v1.TrendView`
        :param instance_id: 实例id
        :type instance_id: int
        :param monitor_item_id: 监控项id
        :type monitor_item_id: int
        :param env_id: 环境id
        :type env_id: int
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._view_config = None
        self._instance_id = None
        self._monitor_item_id = None
        self._env_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if view_config is not None:
            self.view_config = view_config
        if instance_id is not None:
            self.instance_id = instance_id
        if monitor_item_id is not None:
            self.monitor_item_id = monitor_item_id
        if env_id is not None:
            self.env_id = env_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def view_config(self):
        """Gets the view_config of this TrendParam.


        :return: The view_config of this TrendParam.
        :rtype: :class:`huaweicloudsdkapm.v1.TrendView`
        """
        return self._view_config

    @view_config.setter
    def view_config(self, view_config):
        """Sets the view_config of this TrendParam.


        :param view_config: The view_config of this TrendParam.
        :type view_config: :class:`huaweicloudsdkapm.v1.TrendView`
        """
        self._view_config = view_config

    @property
    def instance_id(self):
        """Gets the instance_id of this TrendParam.

        实例id

        :return: The instance_id of this TrendParam.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this TrendParam.

        实例id

        :param instance_id: The instance_id of this TrendParam.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def monitor_item_id(self):
        """Gets the monitor_item_id of this TrendParam.

        监控项id

        :return: The monitor_item_id of this TrendParam.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        """Sets the monitor_item_id of this TrendParam.

        监控项id

        :param monitor_item_id: The monitor_item_id of this TrendParam.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def env_id(self):
        """Gets the env_id of this TrendParam.

        环境id

        :return: The env_id of this TrendParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TrendParam.

        环境id

        :param env_id: The env_id of this TrendParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def start_time(self):
        """Gets the start_time of this TrendParam.

        开始时间

        :return: The start_time of this TrendParam.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TrendParam.

        开始时间

        :param start_time: The start_time of this TrendParam.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TrendParam.

        结束时间

        :return: The end_time of this TrendParam.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TrendParam.

        结束时间

        :param end_time: The end_time of this TrendParam.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, TrendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
