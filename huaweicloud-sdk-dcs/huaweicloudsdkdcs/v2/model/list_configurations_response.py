# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'config_time': 'str',
        'instance_id': 'str',
        'redis_config': 'list[QueryRedisConfig]',
        'config_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'config_time': 'config_time',
        'instance_id': 'instance_id',
        'redis_config': 'redis_config',
        'config_status': 'config_status',
        'status': 'status'
    }

    def __init__(self, config_time=None, instance_id=None, redis_config=None, config_status=None, status=None):
        """ListConfigurationsResponse

        The model defined in huaweicloud sdk

        :param config_time: 实例操作时间。格式为：2017-03-31T12:24:46.297Z
        :type config_time: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param redis_config: 实例配置项数组。
        :type redis_config: list[:class:`huaweicloudsdkdcs.v2.QueryRedisConfig`]
        :param config_status: 实例修改状态 - UPDATING - FAILURE - SUCCESS 
        :type config_status: str
        :param status: 实例运行状态。
        :type status: str
        """
        
        super(ListConfigurationsResponse, self).__init__()

        self._config_time = None
        self._instance_id = None
        self._redis_config = None
        self._config_status = None
        self._status = None
        self.discriminator = None

        if config_time is not None:
            self.config_time = config_time
        if instance_id is not None:
            self.instance_id = instance_id
        if redis_config is not None:
            self.redis_config = redis_config
        if config_status is not None:
            self.config_status = config_status
        if status is not None:
            self.status = status

    @property
    def config_time(self):
        """Gets the config_time of this ListConfigurationsResponse.

        实例操作时间。格式为：2017-03-31T12:24:46.297Z

        :return: The config_time of this ListConfigurationsResponse.
        :rtype: str
        """
        return self._config_time

    @config_time.setter
    def config_time(self, config_time):
        """Sets the config_time of this ListConfigurationsResponse.

        实例操作时间。格式为：2017-03-31T12:24:46.297Z

        :param config_time: The config_time of this ListConfigurationsResponse.
        :type config_time: str
        """
        self._config_time = config_time

    @property
    def instance_id(self):
        """Gets the instance_id of this ListConfigurationsResponse.

        实例ID。

        :return: The instance_id of this ListConfigurationsResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListConfigurationsResponse.

        实例ID。

        :param instance_id: The instance_id of this ListConfigurationsResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def redis_config(self):
        """Gets the redis_config of this ListConfigurationsResponse.

        实例配置项数组。

        :return: The redis_config of this ListConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.QueryRedisConfig`]
        """
        return self._redis_config

    @redis_config.setter
    def redis_config(self, redis_config):
        """Sets the redis_config of this ListConfigurationsResponse.

        实例配置项数组。

        :param redis_config: The redis_config of this ListConfigurationsResponse.
        :type redis_config: list[:class:`huaweicloudsdkdcs.v2.QueryRedisConfig`]
        """
        self._redis_config = redis_config

    @property
    def config_status(self):
        """Gets the config_status of this ListConfigurationsResponse.

        实例修改状态 - UPDATING - FAILURE - SUCCESS 

        :return: The config_status of this ListConfigurationsResponse.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this ListConfigurationsResponse.

        实例修改状态 - UPDATING - FAILURE - SUCCESS 

        :param config_status: The config_status of this ListConfigurationsResponse.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def status(self):
        """Gets the status of this ListConfigurationsResponse.

        实例运行状态。

        :return: The status of this ListConfigurationsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListConfigurationsResponse.

        实例运行状态。

        :param status: The status of this ListConfigurationsResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
