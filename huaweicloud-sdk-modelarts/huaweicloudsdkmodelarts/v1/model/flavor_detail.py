# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_type': 'str',
        'billing': 'BillingInfo',
        'flavor_info': 'FlavorInfo'
    }

    attribute_map = {
        'flavor_type': 'flavor_type',
        'billing': 'billing',
        'flavor_info': 'flavor_info'
    }

    def __init__(self, flavor_type=None, billing=None, flavor_info=None):
        r"""FlavorDetail

        The model defined in huaweicloud sdk

        :param flavor_type: 资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)
        :type flavor_type: str
        :param billing: 
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        :param flavor_info: 
        :type flavor_info: :class:`huaweicloudsdkmodelarts.v1.FlavorInfo`
        """
        
        

        self._flavor_type = None
        self._billing = None
        self._flavor_info = None
        self.discriminator = None

        if flavor_type is not None:
            self.flavor_type = flavor_type
        if billing is not None:
            self.billing = billing
        if flavor_info is not None:
            self.flavor_info = flavor_info

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this FlavorDetail.

        资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)

        :return: The flavor_type of this FlavorDetail.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this FlavorDetail.

        资源规格的类型。可选值如下： - CPU - GPU - [Ascend](tag:hc,hk,fcs_super)

        :param flavor_type: The flavor_type of this FlavorDetail.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def billing(self):
        r"""Gets the billing of this FlavorDetail.

        :return: The billing of this FlavorDetail.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this FlavorDetail.

        :param billing: The billing of this FlavorDetail.
        :type billing: :class:`huaweicloudsdkmodelarts.v1.BillingInfo`
        """
        self._billing = billing

    @property
    def flavor_info(self):
        r"""Gets the flavor_info of this FlavorDetail.

        :return: The flavor_info of this FlavorDetail.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.FlavorInfo`
        """
        return self._flavor_info

    @flavor_info.setter
    def flavor_info(self, flavor_info):
        r"""Sets the flavor_info of this FlavorDetail.

        :param flavor_info: The flavor_info of this FlavorDetail.
        :type flavor_info: :class:`huaweicloudsdkmodelarts.v1.FlavorInfo`
        """
        self._flavor_info = flavor_info

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
        if not isinstance(other, FlavorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
