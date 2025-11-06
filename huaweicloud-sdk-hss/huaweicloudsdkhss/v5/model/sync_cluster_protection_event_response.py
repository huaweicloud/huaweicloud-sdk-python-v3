# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncClusterProtectionEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'synched': 'bool'
    }

    attribute_map = {
        'synched': 'synched'
    }

    def __init__(self, synched=None):
        r"""SyncClusterProtectionEventResponse

        The model defined in huaweicloud sdk

        :param synched: 创建同步任务是否成功
        :type synched: bool
        """
        
        super().__init__()

        self._synched = None
        self.discriminator = None

        if synched is not None:
            self.synched = synched

    @property
    def synched(self):
        r"""Gets the synched of this SyncClusterProtectionEventResponse.

        创建同步任务是否成功

        :return: The synched of this SyncClusterProtectionEventResponse.
        :rtype: bool
        """
        return self._synched

    @synched.setter
    def synched(self, synched):
        r"""Sets the synched of this SyncClusterProtectionEventResponse.

        创建同步任务是否成功

        :param synched: The synched of this SyncClusterProtectionEventResponse.
        :type synched: bool
        """
        self._synched = synched

    def to_dict(self):
        import warnings
        warnings.warn("SyncClusterProtectionEventResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SyncClusterProtectionEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
