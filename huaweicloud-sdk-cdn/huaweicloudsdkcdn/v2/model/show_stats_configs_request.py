# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatsConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'int'
    }

    attribute_map = {
        'config_type': 'config_type'
    }

    def __init__(self, config_type=None):
        r"""ShowStatsConfigsRequest

        The model defined in huaweicloud sdk

        :param config_type: - 配置类型 - 目前支持0：热点统计，1：ces上报
        :type config_type: int
        """
        
        

        self._config_type = None
        self.discriminator = None

        self.config_type = config_type

    @property
    def config_type(self):
        r"""Gets the config_type of this ShowStatsConfigsRequest.

        - 配置类型 - 目前支持0：热点统计，1：ces上报

        :return: The config_type of this ShowStatsConfigsRequest.
        :rtype: int
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this ShowStatsConfigsRequest.

        - 配置类型 - 目前支持0：热点统计，1：ces上报

        :param config_type: The config_type of this ShowStatsConfigsRequest.
        :type config_type: int
        """
        self._config_type = config_type

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
        if not isinstance(other, ShowStatsConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
