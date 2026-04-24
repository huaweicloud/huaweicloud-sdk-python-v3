# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncExternalUserRequest:

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
        'domain_id': 'str',
        'enterprise_id': 'str'
    }

    attribute_map = {
        'auth_config_id': 'auth_config_id',
        'domain_id': 'domain_id',
        'enterprise_id': 'enterprise_id'
    }

    def __init__(self, auth_config_id=None, domain_id=None, enterprise_id=None):
        r"""SyncExternalUserRequest

        The model defined in huaweicloud sdk

        :param auth_config_id: 认证配置id。
        :type auth_config_id: str
        :param domain_id: 域控id。
        :type domain_id: str
        :param enterprise_id: 待同步的用户归属的企业项目id。
        :type enterprise_id: str
        """
        
        

        self._auth_config_id = None
        self._domain_id = None
        self._enterprise_id = None
        self.discriminator = None

        self.auth_config_id = auth_config_id
        self.domain_id = domain_id
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id

    @property
    def auth_config_id(self):
        r"""Gets the auth_config_id of this SyncExternalUserRequest.

        认证配置id。

        :return: The auth_config_id of this SyncExternalUserRequest.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        r"""Sets the auth_config_id of this SyncExternalUserRequest.

        认证配置id。

        :param auth_config_id: The auth_config_id of this SyncExternalUserRequest.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SyncExternalUserRequest.

        域控id。

        :return: The domain_id of this SyncExternalUserRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SyncExternalUserRequest.

        域控id。

        :param domain_id: The domain_id of this SyncExternalUserRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this SyncExternalUserRequest.

        待同步的用户归属的企业项目id。

        :return: The enterprise_id of this SyncExternalUserRequest.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this SyncExternalUserRequest.

        待同步的用户归属的企业项目id。

        :param enterprise_id: The enterprise_id of this SyncExternalUserRequest.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

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
        if not isinstance(other, SyncExternalUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
