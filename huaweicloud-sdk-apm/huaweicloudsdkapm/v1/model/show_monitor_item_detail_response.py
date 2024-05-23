# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorItemDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval': 'int',
        'collector_id': 'int',
        'config_item_list': 'list[ConfigItemValue]'
    }

    attribute_map = {
        'interval': 'interval',
        'collector_id': 'collector_id',
        'config_item_list': 'config_item_list'
    }

    def __init__(self, interval=None, collector_id=None, config_item_list=None):
        """ShowMonitorItemDetailResponse

        The model defined in huaweicloud sdk

        :param interval: 采集间隔
        :type interval: int
        :param collector_id: 采集器ID
        :type collector_id: int
        :param config_item_list: 采集参数配置列表
        :type config_item_list: list[:class:`huaweicloudsdkapm.v1.ConfigItemValue`]
        """
        
        super(ShowMonitorItemDetailResponse, self).__init__()

        self._interval = None
        self._collector_id = None
        self._config_item_list = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if collector_id is not None:
            self.collector_id = collector_id
        if config_item_list is not None:
            self.config_item_list = config_item_list

    @property
    def interval(self):
        """Gets the interval of this ShowMonitorItemDetailResponse.

        采集间隔

        :return: The interval of this ShowMonitorItemDetailResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowMonitorItemDetailResponse.

        采集间隔

        :param interval: The interval of this ShowMonitorItemDetailResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def collector_id(self):
        """Gets the collector_id of this ShowMonitorItemDetailResponse.

        采集器ID

        :return: The collector_id of this ShowMonitorItemDetailResponse.
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this ShowMonitorItemDetailResponse.

        采集器ID

        :param collector_id: The collector_id of this ShowMonitorItemDetailResponse.
        :type collector_id: int
        """
        self._collector_id = collector_id

    @property
    def config_item_list(self):
        """Gets the config_item_list of this ShowMonitorItemDetailResponse.

        采集参数配置列表

        :return: The config_item_list of this ShowMonitorItemDetailResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ConfigItemValue`]
        """
        return self._config_item_list

    @config_item_list.setter
    def config_item_list(self, config_item_list):
        """Sets the config_item_list of this ShowMonitorItemDetailResponse.

        采集参数配置列表

        :param config_item_list: The config_item_list of this ShowMonitorItemDetailResponse.
        :type config_item_list: list[:class:`huaweicloudsdkapm.v1.ConfigItemValue`]
        """
        self._config_item_list = config_item_list

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
        if not isinstance(other, ShowMonitorItemDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
