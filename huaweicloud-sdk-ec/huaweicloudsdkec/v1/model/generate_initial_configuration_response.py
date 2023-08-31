# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateInitialConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('config_content')

    openapi_types = {
        'equipment_id': 'str',
        'config_content': 'str',
        'expire_at': 'str'
    }

    attribute_map = {
        'equipment_id': 'equipment_id',
        'config_content': 'config_content',
        'expire_at': 'expire_at'
    }

    def __init__(self, equipment_id=None, config_content=None, expire_at=None):
        """GenerateInitialConfigurationResponse

        The model defined in huaweicloud sdk

        :param equipment_id: 智能企业网关设备ID
        :type equipment_id: str
        :param config_content: 初始配置URL
        :type config_content: str
        :param expire_at: URL失效时间
        :type expire_at: str
        """
        
        super(GenerateInitialConfigurationResponse, self).__init__()

        self._equipment_id = None
        self._config_content = None
        self._expire_at = None
        self.discriminator = None

        if equipment_id is not None:
            self.equipment_id = equipment_id
        if config_content is not None:
            self.config_content = config_content
        if expire_at is not None:
            self.expire_at = expire_at

    @property
    def equipment_id(self):
        """Gets the equipment_id of this GenerateInitialConfigurationResponse.

        智能企业网关设备ID

        :return: The equipment_id of this GenerateInitialConfigurationResponse.
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        """Sets the equipment_id of this GenerateInitialConfigurationResponse.

        智能企业网关设备ID

        :param equipment_id: The equipment_id of this GenerateInitialConfigurationResponse.
        :type equipment_id: str
        """
        self._equipment_id = equipment_id

    @property
    def config_content(self):
        """Gets the config_content of this GenerateInitialConfigurationResponse.

        初始配置URL

        :return: The config_content of this GenerateInitialConfigurationResponse.
        :rtype: str
        """
        return self._config_content

    @config_content.setter
    def config_content(self, config_content):
        """Sets the config_content of this GenerateInitialConfigurationResponse.

        初始配置URL

        :param config_content: The config_content of this GenerateInitialConfigurationResponse.
        :type config_content: str
        """
        self._config_content = config_content

    @property
    def expire_at(self):
        """Gets the expire_at of this GenerateInitialConfigurationResponse.

        URL失效时间

        :return: The expire_at of this GenerateInitialConfigurationResponse.
        :rtype: str
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this GenerateInitialConfigurationResponse.

        URL失效时间

        :param expire_at: The expire_at of this GenerateInitialConfigurationResponse.
        :type expire_at: str
        """
        self._expire_at = expire_at

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
        if not isinstance(other, GenerateInitialConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
