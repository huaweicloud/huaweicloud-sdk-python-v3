# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewInquiryResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'amount': 'amount'
    }

    def __init__(self, resource_id=None, amount=None):
        r"""RenewInquiryResultInfo

        The model defined in huaweicloud sdk

        :param resource_id: |参数名称：资源ID。| |参数约束及描述：资源ID。|
        :type resource_id: str
        :param amount: |参数名称：主资源（包含从资源）续订金额。单位为元| |参数约束及描述：主资源（包含从资源）续订金额。单位为元|
        :type amount: str
        """
        
        

        self._resource_id = None
        self._amount = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if amount is not None:
            self.amount = amount

    @property
    def resource_id(self):
        r"""Gets the resource_id of this RenewInquiryResultInfo.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :return: The resource_id of this RenewInquiryResultInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this RenewInquiryResultInfo.

        |参数名称：资源ID。| |参数约束及描述：资源ID。|

        :param resource_id: The resource_id of this RenewInquiryResultInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def amount(self):
        r"""Gets the amount of this RenewInquiryResultInfo.

        |参数名称：主资源（包含从资源）续订金额。单位为元| |参数约束及描述：主资源（包含从资源）续订金额。单位为元|

        :return: The amount of this RenewInquiryResultInfo.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this RenewInquiryResultInfo.

        |参数名称：主资源（包含从资源）续订金额。单位为元| |参数约束及描述：主资源（包含从资源）续订金额。单位为元|

        :param amount: The amount of this RenewInquiryResultInfo.
        :type amount: str
        """
        self._amount = amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenewInquiryResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
