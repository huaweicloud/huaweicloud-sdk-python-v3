# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFilePathWhiteDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_path': 'list[str]',
        'customized_path': 'list[str]'
    }

    attribute_map = {
        'default_path': 'default_path',
        'customized_path': 'customized_path'
    }

    def __init__(self, default_path=None, customized_path=None):
        r"""ShowFilePathWhiteDetailResponse

        The model defined in huaweicloud sdk

        :param default_path: **参数解释**: 默认路径，不可编辑 **取值范围**: 最小值0，最大值20000 
        :type default_path: list[str]
        :param customized_path: **参数解释**: 自定义路径，选填，可编辑 **取值范围**: 最小值0，最大值20000 
        :type customized_path: list[str]
        """
        
        super().__init__()

        self._default_path = None
        self._customized_path = None
        self.discriminator = None

        if default_path is not None:
            self.default_path = default_path
        if customized_path is not None:
            self.customized_path = customized_path

    @property
    def default_path(self):
        r"""Gets the default_path of this ShowFilePathWhiteDetailResponse.

        **参数解释**: 默认路径，不可编辑 **取值范围**: 最小值0，最大值20000 

        :return: The default_path of this ShowFilePathWhiteDetailResponse.
        :rtype: list[str]
        """
        return self._default_path

    @default_path.setter
    def default_path(self, default_path):
        r"""Sets the default_path of this ShowFilePathWhiteDetailResponse.

        **参数解释**: 默认路径，不可编辑 **取值范围**: 最小值0，最大值20000 

        :param default_path: The default_path of this ShowFilePathWhiteDetailResponse.
        :type default_path: list[str]
        """
        self._default_path = default_path

    @property
    def customized_path(self):
        r"""Gets the customized_path of this ShowFilePathWhiteDetailResponse.

        **参数解释**: 自定义路径，选填，可编辑 **取值范围**: 最小值0，最大值20000 

        :return: The customized_path of this ShowFilePathWhiteDetailResponse.
        :rtype: list[str]
        """
        return self._customized_path

    @customized_path.setter
    def customized_path(self, customized_path):
        r"""Sets the customized_path of this ShowFilePathWhiteDetailResponse.

        **参数解释**: 自定义路径，选填，可编辑 **取值范围**: 最小值0，最大值20000 

        :param customized_path: The customized_path of this ShowFilePathWhiteDetailResponse.
        :type customized_path: list[str]
        """
        self._customized_path = customized_path

    def to_dict(self):
        import warnings
        warnings.warn("ShowFilePathWhiteDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFilePathWhiteDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
