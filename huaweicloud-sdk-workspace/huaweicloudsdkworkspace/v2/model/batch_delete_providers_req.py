# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteProvidersReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_ids': 'list[str]'
    }

    attribute_map = {
        'provider_ids': 'provider_ids'
    }

    def __init__(self, provider_ids=None):
        r"""BatchDeleteProvidersReq

        The model defined in huaweicloud sdk

        :param provider_ids: 供应商id列表。
        :type provider_ids: list[str]
        """
        
        

        self._provider_ids = None
        self.discriminator = None

        self.provider_ids = provider_ids

    @property
    def provider_ids(self):
        r"""Gets the provider_ids of this BatchDeleteProvidersReq.

        供应商id列表。

        :return: The provider_ids of this BatchDeleteProvidersReq.
        :rtype: list[str]
        """
        return self._provider_ids

    @provider_ids.setter
    def provider_ids(self, provider_ids):
        r"""Sets the provider_ids of this BatchDeleteProvidersReq.

        供应商id列表。

        :param provider_ids: The provider_ids of this BatchDeleteProvidersReq.
        :type provider_ids: list[str]
        """
        self._provider_ids = provider_ids

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
        if not isinstance(other, BatchDeleteProvidersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
