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
    sensitive_list.append('url_config_content')
    sensitive_list.append('script_config_content')

    openapi_types = {
        'equipment_id': 'str',
        'url_config_content': 'str',
        'script_config_content': 'str',
        'expire_at': 'str'
    }

    attribute_map = {
        'equipment_id': 'equipment_id',
        'url_config_content': 'url_config_content',
        'script_config_content': 'script_config_content',
        'expire_at': 'expire_at'
    }

    def __init__(self, equipment_id=None, url_config_content=None, script_config_content=None, expire_at=None):
        """GenerateInitialConfigurationResponse

        The model defined in huaweicloud sdk

        :param equipment_id: 智能企业网关设备ID
        :type equipment_id: str
        :param url_config_content: 初始配置URL
        :type url_config_content: str
        :param script_config_content: 初始配置文件
        :type script_config_content: str
        :param expire_at: URL失效时间
        :type expire_at: str
        """
        
        super(GenerateInitialConfigurationResponse, self).__init__()

        self._equipment_id = None
        self._url_config_content = None
        self._script_config_content = None
        self._expire_at = None
        self.discriminator = None

        if equipment_id is not None:
            self.equipment_id = equipment_id
        if url_config_content is not None:
            self.url_config_content = url_config_content
        if script_config_content is not None:
            self.script_config_content = script_config_content
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
    def url_config_content(self):
        """Gets the url_config_content of this GenerateInitialConfigurationResponse.

        初始配置URL

        :return: The url_config_content of this GenerateInitialConfigurationResponse.
        :rtype: str
        """
        return self._url_config_content

    @url_config_content.setter
    def url_config_content(self, url_config_content):
        """Sets the url_config_content of this GenerateInitialConfigurationResponse.

        初始配置URL

        :param url_config_content: The url_config_content of this GenerateInitialConfigurationResponse.
        :type url_config_content: str
        """
        self._url_config_content = url_config_content

    @property
    def script_config_content(self):
        """Gets the script_config_content of this GenerateInitialConfigurationResponse.

        初始配置文件

        :return: The script_config_content of this GenerateInitialConfigurationResponse.
        :rtype: str
        """
        return self._script_config_content

    @script_config_content.setter
    def script_config_content(self, script_config_content):
        """Sets the script_config_content of this GenerateInitialConfigurationResponse.

        初始配置文件

        :param script_config_content: The script_config_content of this GenerateInitialConfigurationResponse.
        :type script_config_content: str
        """
        self._script_config_content = script_config_content

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
