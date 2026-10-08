# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDisassociateModelProxiesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unbindings': 'list[CoreModelProxyDetails]'
    }

    attribute_map = {
        'unbindings': 'unbindings'
    }

    def __init__(self, unbindings=None):
        r"""BatchDisassociateModelProxiesRequestBody

        The model defined in huaweicloud sdk

        :param unbindings: **参数解释：** 模型提供商和模型代理解绑详情。 **取值范围：** 不涉及。 
        :type unbindings: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        """
        
        

        self._unbindings = None
        self.discriminator = None

        self.unbindings = unbindings

    @property
    def unbindings(self):
        r"""Gets the unbindings of this BatchDisassociateModelProxiesRequestBody.

        **参数解释：** 模型提供商和模型代理解绑详情。 **取值范围：** 不涉及。 

        :return: The unbindings of this BatchDisassociateModelProxiesRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        """
        return self._unbindings

    @unbindings.setter
    def unbindings(self, unbindings):
        r"""Sets the unbindings of this BatchDisassociateModelProxiesRequestBody.

        **参数解释：** 模型提供商和模型代理解绑详情。 **取值范围：** 不涉及。 

        :param unbindings: The unbindings of this BatchDisassociateModelProxiesRequestBody.
        :type unbindings: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProxyDetails`]
        """
        self._unbindings = unbindings

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
        if not isinstance(other, BatchDisassociateModelProxiesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
