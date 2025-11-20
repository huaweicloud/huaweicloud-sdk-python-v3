# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransAcceptResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_need_billing': 'bool',
        'required_resources': 'list[BillResources]'
    }

    attribute_map = {
        'is_need_billing': 'is_need_billing',
        'required_resources': 'required_resources'
    }

    def __init__(self, is_need_billing=None, required_resources=None):
        r"""TransAcceptResponse

        The model defined in huaweicloud sdk

        :param is_need_billing: 资产转移时，是否需要从接收方扣减资源（产生计费话单)
        :type is_need_billing: bool
        :param required_resources: 需要扣减的资源列表。
        :type required_resources: list[:class:`huaweicloudsdkmetastudio.v1.BillResources`]
        """
        
        

        self._is_need_billing = None
        self._required_resources = None
        self.discriminator = None

        if is_need_billing is not None:
            self.is_need_billing = is_need_billing
        if required_resources is not None:
            self.required_resources = required_resources

    @property
    def is_need_billing(self):
        r"""Gets the is_need_billing of this TransAcceptResponse.

        资产转移时，是否需要从接收方扣减资源（产生计费话单)

        :return: The is_need_billing of this TransAcceptResponse.
        :rtype: bool
        """
        return self._is_need_billing

    @is_need_billing.setter
    def is_need_billing(self, is_need_billing):
        r"""Sets the is_need_billing of this TransAcceptResponse.

        资产转移时，是否需要从接收方扣减资源（产生计费话单)

        :param is_need_billing: The is_need_billing of this TransAcceptResponse.
        :type is_need_billing: bool
        """
        self._is_need_billing = is_need_billing

    @property
    def required_resources(self):
        r"""Gets the required_resources of this TransAcceptResponse.

        需要扣减的资源列表。

        :return: The required_resources of this TransAcceptResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.BillResources`]
        """
        return self._required_resources

    @required_resources.setter
    def required_resources(self, required_resources):
        r"""Sets the required_resources of this TransAcceptResponse.

        需要扣减的资源列表。

        :param required_resources: The required_resources of this TransAcceptResponse.
        :type required_resources: list[:class:`huaweicloudsdkmetastudio.v1.BillResources`]
        """
        self._required_resources = required_resources

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
        if not isinstance(other, TransAcceptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
