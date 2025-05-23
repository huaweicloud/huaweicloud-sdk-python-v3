# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigMapRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_map_id': 'str',
        'body': 'ConfigMapModelBoxDTO'
    }

    attribute_map = {
        'config_map_id': 'config_map_id',
        'body': 'body'
    }

    def __init__(self, config_map_id=None, body=None):
        r"""UpdateConfigMapRequest

        The model defined in huaweicloud sdk

        :param config_map_id: 配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取
        :type config_map_id: str
        :param body: Body of the UpdateConfigMapRequest
        :type body: :class:`huaweicloudsdkhilens.v3.ConfigMapModelBoxDTO`
        """
        
        

        self._config_map_id = None
        self._body = None
        self.discriminator = None

        self.config_map_id = config_map_id
        if body is not None:
            self.body = body

    @property
    def config_map_id(self):
        r"""Gets the config_map_id of this UpdateConfigMapRequest.

        配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取

        :return: The config_map_id of this UpdateConfigMapRequest.
        :rtype: str
        """
        return self._config_map_id

    @config_map_id.setter
    def config_map_id(self, config_map_id):
        r"""Sets the config_map_id of this UpdateConfigMapRequest.

        配置项ID，从专业版HiLens控制台配置项管理[获取配置项列表](listConfigMapUsingGET.xml)获取

        :param config_map_id: The config_map_id of this UpdateConfigMapRequest.
        :type config_map_id: str
        """
        self._config_map_id = config_map_id

    @property
    def body(self):
        r"""Gets the body of this UpdateConfigMapRequest.

        :return: The body of this UpdateConfigMapRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.ConfigMapModelBoxDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateConfigMapRequest.

        :param body: The body of this UpdateConfigMapRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.ConfigMapModelBoxDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateConfigMapRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
