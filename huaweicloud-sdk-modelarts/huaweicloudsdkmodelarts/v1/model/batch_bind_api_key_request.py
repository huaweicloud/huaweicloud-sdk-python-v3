# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBindApiKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_ids': 'list[BatchBindApiKeyRequestKeyIds]'
    }

    attribute_map = {
        'key_ids': 'key_ids'
    }

    def __init__(self, key_ids=None):
        r"""BatchBindApiKeyRequest

        The model defined in huaweicloud sdk

        :param key_ids: **参数解释：** 请求批量绑定的api-key的id数组。 **约束限制：** 请求批量绑定api-key的id个数不超过10个。
        :type key_ids: list[:class:`huaweicloudsdkmodelarts.v1.BatchBindApiKeyRequestKeyIds`]
        """
        
        

        self._key_ids = None
        self.discriminator = None

        self.key_ids = key_ids

    @property
    def key_ids(self):
        r"""Gets the key_ids of this BatchBindApiKeyRequest.

        **参数解释：** 请求批量绑定的api-key的id数组。 **约束限制：** 请求批量绑定api-key的id个数不超过10个。

        :return: The key_ids of this BatchBindApiKeyRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.BatchBindApiKeyRequestKeyIds`]
        """
        return self._key_ids

    @key_ids.setter
    def key_ids(self, key_ids):
        r"""Sets the key_ids of this BatchBindApiKeyRequest.

        **参数解释：** 请求批量绑定的api-key的id数组。 **约束限制：** 请求批量绑定api-key的id个数不超过10个。

        :param key_ids: The key_ids of this BatchBindApiKeyRequest.
        :type key_ids: list[:class:`huaweicloudsdkmodelarts.v1.BatchBindApiKeyRequestKeyIds`]
        """
        self._key_ids = key_ids

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
        if not isinstance(other, BatchBindApiKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
