# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWarmPoolNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'warm_pool': 'WarmPoolInfo'
    }

    attribute_map = {
        'warm_pool': 'warm_pool'
    }

    def __init__(self, warm_pool=None):
        r"""ShowWarmPoolNewResponse

        The model defined in huaweicloud sdk

        :param warm_pool: 
        :type warm_pool: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        
        super().__init__()

        self._warm_pool = None
        self.discriminator = None

        if warm_pool is not None:
            self.warm_pool = warm_pool

    @property
    def warm_pool(self):
        r"""Gets the warm_pool of this ShowWarmPoolNewResponse.

        :return: The warm_pool of this ShowWarmPoolNewResponse.
        :rtype: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        return self._warm_pool

    @warm_pool.setter
    def warm_pool(self, warm_pool):
        r"""Sets the warm_pool of this ShowWarmPoolNewResponse.

        :param warm_pool: The warm_pool of this ShowWarmPoolNewResponse.
        :type warm_pool: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        self._warm_pool = warm_pool

    def to_dict(self):
        import warnings
        warnings.warn("ShowWarmPoolNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowWarmPoolNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
