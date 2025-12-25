# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfigurationApplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_fail_list': 'list[ComponentConfiguration]',
        'apply_success_list': 'list[ComponentConfiguration]'
    }

    attribute_map = {
        'apply_fail_list': 'apply_fail_list',
        'apply_success_list': 'apply_success_list'
    }

    def __init__(self, apply_fail_list=None, apply_success_list=None):
        r"""CreateConfigurationApplicationResponse

        The model defined in huaweicloud sdk

        :param apply_fail_list: 创建失败实例列表
        :type apply_fail_list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        :param apply_success_list: 创建成功实例列表
        :type apply_success_list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        """
        
        super().__init__()

        self._apply_fail_list = None
        self._apply_success_list = None
        self.discriminator = None

        if apply_fail_list is not None:
            self.apply_fail_list = apply_fail_list
        if apply_success_list is not None:
            self.apply_success_list = apply_success_list

    @property
    def apply_fail_list(self):
        r"""Gets the apply_fail_list of this CreateConfigurationApplicationResponse.

        创建失败实例列表

        :return: The apply_fail_list of this CreateConfigurationApplicationResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        """
        return self._apply_fail_list

    @apply_fail_list.setter
    def apply_fail_list(self, apply_fail_list):
        r"""Sets the apply_fail_list of this CreateConfigurationApplicationResponse.

        创建失败实例列表

        :param apply_fail_list: The apply_fail_list of this CreateConfigurationApplicationResponse.
        :type apply_fail_list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        """
        self._apply_fail_list = apply_fail_list

    @property
    def apply_success_list(self):
        r"""Gets the apply_success_list of this CreateConfigurationApplicationResponse.

        创建成功实例列表

        :return: The apply_success_list of this CreateConfigurationApplicationResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        """
        return self._apply_success_list

    @apply_success_list.setter
    def apply_success_list(self, apply_success_list):
        r"""Sets the apply_success_list of this CreateConfigurationApplicationResponse.

        创建成功实例列表

        :param apply_success_list: The apply_success_list of this CreateConfigurationApplicationResponse.
        :type apply_success_list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfiguration`]
        """
        self._apply_success_list = apply_success_list

    def to_dict(self):
        import warnings
        warnings.warn("CreateConfigurationApplicationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateConfigurationApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
