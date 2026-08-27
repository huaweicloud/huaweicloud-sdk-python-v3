# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveImChannelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_ids': 'list[str]'
    }

    attribute_map = {
        'config_ids': 'config_ids'
    }

    def __init__(self, config_ids=None):
        r"""SaveImChannelsResponse

        The model defined in huaweicloud sdk

        :param config_ids: 配置 ID 列表
        :type config_ids: list[str]
        """
        
        super().__init__()

        self._config_ids = None
        self.discriminator = None

        if config_ids is not None:
            self.config_ids = config_ids

    @property
    def config_ids(self):
        r"""Gets the config_ids of this SaveImChannelsResponse.

        配置 ID 列表

        :return: The config_ids of this SaveImChannelsResponse.
        :rtype: list[str]
        """
        return self._config_ids

    @config_ids.setter
    def config_ids(self, config_ids):
        r"""Sets the config_ids of this SaveImChannelsResponse.

        配置 ID 列表

        :param config_ids: The config_ids of this SaveImChannelsResponse.
        :type config_ids: list[str]
        """
        self._config_ids = config_ids

    def to_dict(self):
        import warnings
        warnings.warn("SaveImChannelsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, SaveImChannelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
