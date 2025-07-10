# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HourPackageResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'used_up_policy': 'str',
        'create_desktops': 'CreateDesktopReq'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'used_up_policy': 'used_up_policy',
        'create_desktops': 'create_desktops'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_renew=None, used_up_policy=None, create_desktops=None):
        r"""HourPackageResource

        The model defined in huaweicloud sdk

        :param period_type: 订购周期类型：2：月；3：年;必填。
        :type period_type: int
        :param period_num: 订购周期数。
        :type period_num: int
        :param is_auto_renew: 是否自动续订。
        :type is_auto_renew: int
        :param used_up_policy: 时长用尽策略：   - SHUTDOWN_OR_HIBERNATE：自动关机/休眠。 - PAY_PER_USE：自动按需计费。
        :type used_up_policy: str
        :param create_desktops: 
        :type create_desktops: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._used_up_policy = None
        self._create_desktops = None
        self.discriminator = None

        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if used_up_policy is not None:
            self.used_up_policy = used_up_policy
        if create_desktops is not None:
            self.create_desktops = create_desktops

    @property
    def period_type(self):
        r"""Gets the period_type of this HourPackageResource.

        订购周期类型：2：月；3：年;必填。

        :return: The period_type of this HourPackageResource.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this HourPackageResource.

        订购周期类型：2：月；3：年;必填。

        :param period_type: The period_type of this HourPackageResource.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this HourPackageResource.

        订购周期数。

        :return: The period_num of this HourPackageResource.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this HourPackageResource.

        订购周期数。

        :param period_num: The period_num of this HourPackageResource.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this HourPackageResource.

        是否自动续订。

        :return: The is_auto_renew of this HourPackageResource.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this HourPackageResource.

        是否自动续订。

        :param is_auto_renew: The is_auto_renew of this HourPackageResource.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def used_up_policy(self):
        r"""Gets the used_up_policy of this HourPackageResource.

        时长用尽策略：   - SHUTDOWN_OR_HIBERNATE：自动关机/休眠。 - PAY_PER_USE：自动按需计费。

        :return: The used_up_policy of this HourPackageResource.
        :rtype: str
        """
        return self._used_up_policy

    @used_up_policy.setter
    def used_up_policy(self, used_up_policy):
        r"""Sets the used_up_policy of this HourPackageResource.

        时长用尽策略：   - SHUTDOWN_OR_HIBERNATE：自动关机/休眠。 - PAY_PER_USE：自动按需计费。

        :param used_up_policy: The used_up_policy of this HourPackageResource.
        :type used_up_policy: str
        """
        self._used_up_policy = used_up_policy

    @property
    def create_desktops(self):
        r"""Gets the create_desktops of this HourPackageResource.

        :return: The create_desktops of this HourPackageResource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        """
        return self._create_desktops

    @create_desktops.setter
    def create_desktops(self, create_desktops):
        r"""Sets the create_desktops of this HourPackageResource.

        :param create_desktops: The create_desktops of this HourPackageResource.
        :type create_desktops: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        """
        self._create_desktops = create_desktops

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
        if not isinstance(other, HourPackageResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
