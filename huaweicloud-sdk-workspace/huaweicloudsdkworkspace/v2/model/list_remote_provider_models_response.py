# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRemoteProviderModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'remote_models': 'list[BaseModeInfo]'
    }

    attribute_map = {
        'total': 'total',
        'remote_models': 'remote_models'
    }

    def __init__(self, total=None, remote_models=None):
        r"""ListRemoteProviderModelsResponse

        The model defined in huaweicloud sdk

        :param total: 远端模型总数。
        :type total: int
        :param remote_models: 远程模型列表。
        :type remote_models: list[:class:`huaweicloudsdkworkspace.v2.BaseModeInfo`]
        """
        
        super().__init__()

        self._total = None
        self._remote_models = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if remote_models is not None:
            self.remote_models = remote_models

    @property
    def total(self):
        r"""Gets the total of this ListRemoteProviderModelsResponse.

        远端模型总数。

        :return: The total of this ListRemoteProviderModelsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRemoteProviderModelsResponse.

        远端模型总数。

        :param total: The total of this ListRemoteProviderModelsResponse.
        :type total: int
        """
        self._total = total

    @property
    def remote_models(self):
        r"""Gets the remote_models of this ListRemoteProviderModelsResponse.

        远程模型列表。

        :return: The remote_models of this ListRemoteProviderModelsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.BaseModeInfo`]
        """
        return self._remote_models

    @remote_models.setter
    def remote_models(self, remote_models):
        r"""Sets the remote_models of this ListRemoteProviderModelsResponse.

        远程模型列表。

        :param remote_models: The remote_models of this ListRemoteProviderModelsResponse.
        :type remote_models: list[:class:`huaweicloudsdkworkspace.v2.BaseModeInfo`]
        """
        self._remote_models = remote_models

    def to_dict(self):
        import warnings
        warnings.warn("ListRemoteProviderModelsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRemoteProviderModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
