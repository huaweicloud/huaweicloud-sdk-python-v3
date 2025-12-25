# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigurationDictionariesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_list': 'list[Dictionary]',
        'failed_list': 'list[Dictionary]'
    }

    attribute_map = {
        'success_list': 'success_list',
        'failed_list': 'failed_list'
    }

    def __init__(self, success_list=None, failed_list=None):
        r"""UpdateConfigurationDictionariesResponse

        The model defined in huaweicloud sdk

        :param success_list: 正常字典列表
        :type success_list: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        :param failed_list: 正常字典列表
        :type failed_list: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        """
        
        super().__init__()

        self._success_list = None
        self._failed_list = None
        self.discriminator = None

        if success_list is not None:
            self.success_list = success_list
        if failed_list is not None:
            self.failed_list = failed_list

    @property
    def success_list(self):
        r"""Gets the success_list of this UpdateConfigurationDictionariesResponse.

        正常字典列表

        :return: The success_list of this UpdateConfigurationDictionariesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        """
        return self._success_list

    @success_list.setter
    def success_list(self, success_list):
        r"""Sets the success_list of this UpdateConfigurationDictionariesResponse.

        正常字典列表

        :param success_list: The success_list of this UpdateConfigurationDictionariesResponse.
        :type success_list: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        """
        self._success_list = success_list

    @property
    def failed_list(self):
        r"""Gets the failed_list of this UpdateConfigurationDictionariesResponse.

        正常字典列表

        :return: The failed_list of this UpdateConfigurationDictionariesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        """
        return self._failed_list

    @failed_list.setter
    def failed_list(self, failed_list):
        r"""Sets the failed_list of this UpdateConfigurationDictionariesResponse.

        正常字典列表

        :param failed_list: The failed_list of this UpdateConfigurationDictionariesResponse.
        :type failed_list: list[:class:`huaweicloudsdksecmaster.v1.Dictionary`]
        """
        self._failed_list = failed_list

    def to_dict(self):
        import warnings
        warnings.warn("UpdateConfigurationDictionariesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateConfigurationDictionariesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
