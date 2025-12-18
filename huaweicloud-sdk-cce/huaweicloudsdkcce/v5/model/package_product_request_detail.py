# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageProductRequestDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'subscription_num': 'int'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, resource_spec_code=None, subscription_num=None):
        r"""PackageProductRequestDetail

        The model defined in huaweicloud sdk

        :param resource_spec_code: **参数解释：** 套餐包规格，通过套餐包列表接口获取。 **约束限制：** 不涉及 **取值范围：** 只支持通过套餐包列表接口获取的套餐包规格。 **默认取值：** 不涉及 
        :type resource_spec_code: str
        :param subscription_num: **参数解释：** 套餐包订购数量。 **约束限制：** 不涉及 **取值范围：** [1-10] **默认取值：** 0 
        :type subscription_num: int
        """
        
        

        self._resource_spec_code = None
        self._subscription_num = None
        self.discriminator = None

        self.resource_spec_code = resource_spec_code
        self.subscription_num = subscription_num

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this PackageProductRequestDetail.

        **参数解释：** 套餐包规格，通过套餐包列表接口获取。 **约束限制：** 不涉及 **取值范围：** 只支持通过套餐包列表接口获取的套餐包规格。 **默认取值：** 不涉及 

        :return: The resource_spec_code of this PackageProductRequestDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this PackageProductRequestDetail.

        **参数解释：** 套餐包规格，通过套餐包列表接口获取。 **约束限制：** 不涉及 **取值范围：** 只支持通过套餐包列表接口获取的套餐包规格。 **默认取值：** 不涉及 

        :param resource_spec_code: The resource_spec_code of this PackageProductRequestDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this PackageProductRequestDetail.

        **参数解释：** 套餐包订购数量。 **约束限制：** 不涉及 **取值范围：** [1-10] **默认取值：** 0 

        :return: The subscription_num of this PackageProductRequestDetail.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this PackageProductRequestDetail.

        **参数解释：** 套餐包订购数量。 **约束限制：** 不涉及 **取值范围：** [1-10] **默认取值：** 0 

        :param subscription_num: The subscription_num of this PackageProductRequestDetail.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

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
        if not isinstance(other, PackageProductRequestDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
