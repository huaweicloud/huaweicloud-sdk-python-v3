# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConfigMapRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_map_id': 'str'
    }

    attribute_map = {
        'config_map_id': 'config_map_id'
    }

    def __init__(self, config_map_id=None):
        """DeleteConfigMapRequest

        The model defined in huaweicloud sdk

        :param config_map_id: 配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取
        :type config_map_id: str
        """
        
        

        self._config_map_id = None
        self.discriminator = None

        self.config_map_id = config_map_id

    @property
    def config_map_id(self):
        """Gets the config_map_id of this DeleteConfigMapRequest.

        配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取

        :return: The config_map_id of this DeleteConfigMapRequest.
        :rtype: str
        """
        return self._config_map_id

    @config_map_id.setter
    def config_map_id(self, config_map_id):
        """Sets the config_map_id of this DeleteConfigMapRequest.

        配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取

        :param config_map_id: The config_map_id of this DeleteConfigMapRequest.
        :type config_map_id: str
        """
        self._config_map_id = config_map_id

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
        if not isinstance(other, DeleteConfigMapRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
