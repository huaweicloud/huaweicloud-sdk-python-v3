# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomConnectorInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_config': 'ApiConfig',
        'auth_content': 'AuthConfigA',
        'connector_created_type': 'str',
        'connector_type': 'str',
        'icon': 'str',
        'swagger': 'object'
    }

    attribute_map = {
        'api_config': 'api_config',
        'auth_content': 'auth_content',
        'connector_created_type': 'connector_created_type',
        'connector_type': 'connector_type',
        'icon': 'icon',
        'swagger': 'swagger'
    }

    def __init__(self, api_config=None, auth_content=None, connector_created_type=None, connector_type=None, icon=None, swagger=None):
        """CustomConnectorInfoV2

        The model defined in huaweicloud sdk

        :param api_config: 
        :type api_config: :class:`huaweicloudsdkmssi.v1.ApiConfig`
        :param auth_content: 
        :type auth_content: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        :param connector_created_type: 
        :type connector_created_type: str
        :param connector_type: 
        :type connector_type: str
        :param icon: logo base64编码
        :type icon: str
        :param swagger: swagger文档，大文本
        :type swagger: object
        """
        
        

        self._api_config = None
        self._auth_content = None
        self._connector_created_type = None
        self._connector_type = None
        self._icon = None
        self._swagger = None
        self.discriminator = None

        if api_config is not None:
            self.api_config = api_config
        if auth_content is not None:
            self.auth_content = auth_content
        if connector_created_type is not None:
            self.connector_created_type = connector_created_type
        if connector_type is not None:
            self.connector_type = connector_type
        if icon is not None:
            self.icon = icon
        if swagger is not None:
            self.swagger = swagger

    @property
    def api_config(self):
        """Gets the api_config of this CustomConnectorInfoV2.

        :return: The api_config of this CustomConnectorInfoV2.
        :rtype: :class:`huaweicloudsdkmssi.v1.ApiConfig`
        """
        return self._api_config

    @api_config.setter
    def api_config(self, api_config):
        """Sets the api_config of this CustomConnectorInfoV2.

        :param api_config: The api_config of this CustomConnectorInfoV2.
        :type api_config: :class:`huaweicloudsdkmssi.v1.ApiConfig`
        """
        self._api_config = api_config

    @property
    def auth_content(self):
        """Gets the auth_content of this CustomConnectorInfoV2.

        :return: The auth_content of this CustomConnectorInfoV2.
        :rtype: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        """
        return self._auth_content

    @auth_content.setter
    def auth_content(self, auth_content):
        """Sets the auth_content of this CustomConnectorInfoV2.

        :param auth_content: The auth_content of this CustomConnectorInfoV2.
        :type auth_content: :class:`huaweicloudsdkmssi.v1.AuthConfigA`
        """
        self._auth_content = auth_content

    @property
    def connector_created_type(self):
        """Gets the connector_created_type of this CustomConnectorInfoV2.

        :return: The connector_created_type of this CustomConnectorInfoV2.
        :rtype: str
        """
        return self._connector_created_type

    @connector_created_type.setter
    def connector_created_type(self, connector_created_type):
        """Sets the connector_created_type of this CustomConnectorInfoV2.

        :param connector_created_type: The connector_created_type of this CustomConnectorInfoV2.
        :type connector_created_type: str
        """
        self._connector_created_type = connector_created_type

    @property
    def connector_type(self):
        """Gets the connector_type of this CustomConnectorInfoV2.

        :return: The connector_type of this CustomConnectorInfoV2.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """Sets the connector_type of this CustomConnectorInfoV2.

        :param connector_type: The connector_type of this CustomConnectorInfoV2.
        :type connector_type: str
        """
        self._connector_type = connector_type

    @property
    def icon(self):
        """Gets the icon of this CustomConnectorInfoV2.

        logo base64编码

        :return: The icon of this CustomConnectorInfoV2.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this CustomConnectorInfoV2.

        logo base64编码

        :param icon: The icon of this CustomConnectorInfoV2.
        :type icon: str
        """
        self._icon = icon

    @property
    def swagger(self):
        """Gets the swagger of this CustomConnectorInfoV2.

        swagger文档，大文本

        :return: The swagger of this CustomConnectorInfoV2.
        :rtype: object
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this CustomConnectorInfoV2.

        swagger文档，大文本

        :param swagger: The swagger of this CustomConnectorInfoV2.
        :type swagger: object
        """
        self._swagger = swagger

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
        if not isinstance(other, CustomConnectorInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
