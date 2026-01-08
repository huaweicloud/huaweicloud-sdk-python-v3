# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_config_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'auth_config_id': 'auth_config_id',
        'type': 'type'
    }

    def __init__(self, auth_config_id=None, type=None):
        r"""DownloadMetadataRequest

        The model defined in huaweicloud sdk

        :param auth_config_id: 认证配置id。
        :type auth_config_id: str
        :param type: 元数据类型。 - IDP：身份认证提供方 - SP：服务提供方
        :type type: str
        """
        
        

        self._auth_config_id = None
        self._type = None
        self.discriminator = None

        self.auth_config_id = auth_config_id
        self.type = type

    @property
    def auth_config_id(self):
        r"""Gets the auth_config_id of this DownloadMetadataRequest.

        认证配置id。

        :return: The auth_config_id of this DownloadMetadataRequest.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        r"""Sets the auth_config_id of this DownloadMetadataRequest.

        认证配置id。

        :param auth_config_id: The auth_config_id of this DownloadMetadataRequest.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def type(self):
        r"""Gets the type of this DownloadMetadataRequest.

        元数据类型。 - IDP：身份认证提供方 - SP：服务提供方

        :return: The type of this DownloadMetadataRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DownloadMetadataRequest.

        元数据类型。 - IDP：身份认证提供方 - SP：服务提供方

        :param type: The type of this DownloadMetadataRequest.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DownloadMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
