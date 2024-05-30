# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewalResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'period_type': 'int',
        'period_num': 'int',
        'expire_policy': 'int',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'expire_policy': 'expire_policy',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, resource_ids=None, period_type=None, period_num=None, expire_policy=None, is_auto_pay=None):
        """RenewalResourcesReq

        The model defined in huaweicloud sdk

        :param resource_ids: 资源ID列表。 只支持传入主资源ID，最多10个资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。
        :type resource_ids: list[str]
        :param period_type: 周期类型： 2：月3：年
        :type period_type: int
        :param period_num: 周期数目： 如果是月，目前支持1-11如果是年，目前支持1-3
        :type period_num: int
        :param expire_policy: 到期策略（字段已废弃，请勿使用该字段。此字段必填，需携带，但携带的枚举实际并不生效）： 0：进入宽限期/保留期1：转按需2：自动退订3：自动续订
        :type expire_policy: int
        :param is_auto_pay: 是否自动支付。 0：否1：是 此参数不携带或携带值为null时，默认值为“0：否”，即不自动支付。
        :type is_auto_pay: int
        """
        
        

        self._resource_ids = None
        self._period_type = None
        self._period_num = None
        self._expire_policy = None
        self._is_auto_pay = None
        self.discriminator = None

        self.resource_ids = resource_ids
        self.period_type = period_type
        self.period_num = period_num
        self.expire_policy = expire_policy
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def resource_ids(self):
        """Gets the resource_ids of this RenewalResourcesReq.

        资源ID列表。 只支持传入主资源ID，最多10个资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。

        :return: The resource_ids of this RenewalResourcesReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this RenewalResourcesReq.

        资源ID列表。 只支持传入主资源ID，最多10个资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。

        :param resource_ids: The resource_ids of this RenewalResourcesReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def period_type(self):
        """Gets the period_type of this RenewalResourcesReq.

        周期类型： 2：月3：年

        :return: The period_type of this RenewalResourcesReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this RenewalResourcesReq.

        周期类型： 2：月3：年

        :param period_type: The period_type of this RenewalResourcesReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this RenewalResourcesReq.

        周期数目： 如果是月，目前支持1-11如果是年，目前支持1-3

        :return: The period_num of this RenewalResourcesReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this RenewalResourcesReq.

        周期数目： 如果是月，目前支持1-11如果是年，目前支持1-3

        :param period_num: The period_num of this RenewalResourcesReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def expire_policy(self):
        """Gets the expire_policy of this RenewalResourcesReq.

        到期策略（字段已废弃，请勿使用该字段。此字段必填，需携带，但携带的枚举实际并不生效）： 0：进入宽限期/保留期1：转按需2：自动退订3：自动续订

        :return: The expire_policy of this RenewalResourcesReq.
        :rtype: int
        """
        return self._expire_policy

    @expire_policy.setter
    def expire_policy(self, expire_policy):
        """Sets the expire_policy of this RenewalResourcesReq.

        到期策略（字段已废弃，请勿使用该字段。此字段必填，需携带，但携带的枚举实际并不生效）： 0：进入宽限期/保留期1：转按需2：自动退订3：自动续订

        :param expire_policy: The expire_policy of this RenewalResourcesReq.
        :type expire_policy: int
        """
        self._expire_policy = expire_policy

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this RenewalResourcesReq.

        是否自动支付。 0：否1：是 此参数不携带或携带值为null时，默认值为“0：否”，即不自动支付。

        :return: The is_auto_pay of this RenewalResourcesReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this RenewalResourcesReq.

        是否自动支付。 0：否1：是 此参数不携带或携带值为null时，默认值为“0：否”，即不自动支付。

        :param is_auto_pay: The is_auto_pay of this RenewalResourcesReq.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, RenewalResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
