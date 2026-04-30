# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoRenewalResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_renew_times': 'int',
        'period_type': 'str'
    }

    attribute_map = {
        'auto_renew_times': 'auto_renew_times',
        'period_type': 'period_type'
    }

    def __init__(self, auto_renew_times=None, period_type=None):
        r"""AutoRenewalResourcesReq

        The model defined in huaweicloud sdk

        :param auto_renew_times: |参数名称：自动续费次数| |参数的约束及描述：该参数非必填，范围限制：0-99，0代表不限制次数。 首次开通自动续费，此参数不携带或携带值为null时，默认为不限制次数 已开通自动续费，重置自动续费次数时此参数必填，否则不做处理，不进行修改|
        :type auto_renew_times: int
        :param period_type: |参数名称：自动续费的周期类型| |参数的约束及描述：该参数非必填，自动续费的周期类型，支持枚举| |MONTH：包月，YEAR：包年。此参数不携带或携带值为null时，按照如下规则处理。购买时，未设置自动续费功能，默认与设置资源的最后一个订单的订购周期类型一致。|
        :type period_type: str
        """
        
        

        self._auto_renew_times = None
        self._period_type = None
        self.discriminator = None

        if auto_renew_times is not None:
            self.auto_renew_times = auto_renew_times
        if period_type is not None:
            self.period_type = period_type

    @property
    def auto_renew_times(self):
        r"""Gets the auto_renew_times of this AutoRenewalResourcesReq.

        |参数名称：自动续费次数| |参数的约束及描述：该参数非必填，范围限制：0-99，0代表不限制次数。 首次开通自动续费，此参数不携带或携带值为null时，默认为不限制次数 已开通自动续费，重置自动续费次数时此参数必填，否则不做处理，不进行修改|

        :return: The auto_renew_times of this AutoRenewalResourcesReq.
        :rtype: int
        """
        return self._auto_renew_times

    @auto_renew_times.setter
    def auto_renew_times(self, auto_renew_times):
        r"""Sets the auto_renew_times of this AutoRenewalResourcesReq.

        |参数名称：自动续费次数| |参数的约束及描述：该参数非必填，范围限制：0-99，0代表不限制次数。 首次开通自动续费，此参数不携带或携带值为null时，默认为不限制次数 已开通自动续费，重置自动续费次数时此参数必填，否则不做处理，不进行修改|

        :param auto_renew_times: The auto_renew_times of this AutoRenewalResourcesReq.
        :type auto_renew_times: int
        """
        self._auto_renew_times = auto_renew_times

    @property
    def period_type(self):
        r"""Gets the period_type of this AutoRenewalResourcesReq.

        |参数名称：自动续费的周期类型| |参数的约束及描述：该参数非必填，自动续费的周期类型，支持枚举| |MONTH：包月，YEAR：包年。此参数不携带或携带值为null时，按照如下规则处理。购买时，未设置自动续费功能，默认与设置资源的最后一个订单的订购周期类型一致。|

        :return: The period_type of this AutoRenewalResourcesReq.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this AutoRenewalResourcesReq.

        |参数名称：自动续费的周期类型| |参数的约束及描述：该参数非必填，自动续费的周期类型，支持枚举| |MONTH：包月，YEAR：包年。此参数不携带或携带值为null时，按照如下规则处理。购买时，未设置自动续费功能，默认与设置资源的最后一个订单的订购周期类型一致。|

        :param period_type: The period_type of this AutoRenewalResourcesReq.
        :type period_type: str
        """
        self._period_type = period_type

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
        if not isinstance(other, AutoRenewalResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
