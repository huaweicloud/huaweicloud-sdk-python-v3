# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletePoolsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pools': 'list[str]'
    }

    attribute_map = {
        'pools': 'pools'
    }

    def __init__(self, pools=None):
        r"""BatchDeletePoolsRequestBody

        The model defined in huaweicloud sdk

        :param pools: 待删除的后端服务器组id列表。
        :type pools: list[str]
        """
        
        

        self._pools = None
        self.discriminator = None

        self.pools = pools

    @property
    def pools(self):
        r"""Gets the pools of this BatchDeletePoolsRequestBody.

        待删除的后端服务器组id列表。

        :return: The pools of this BatchDeletePoolsRequestBody.
        :rtype: list[str]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this BatchDeletePoolsRequestBody.

        待删除的后端服务器组id列表。

        :param pools: The pools of this BatchDeletePoolsRequestBody.
        :type pools: list[str]
        """
        self._pools = pools

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
        if not isinstance(other, BatchDeletePoolsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
