# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'region_id': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'region_id': 'regionID',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, charging_mode=None, region_id=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, enterprise_project_id=None):
        r"""ExtendParam

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式。取值范围：prePaid：预付费，即包年包月; postPaid-后付费，即按需付费。默认值是prePaid。
        :type charging_mode: str
        :param region_id: 裸金属服务器所在区域ID。请参考地区和终端节点获取。
        :type region_id: str
        :param period_type: 订购周期类型。取值范围：month：月year：年 说明：chargingMode为prePaid时生效，且为必选值。
        :type period_type: str
        :param period_num: 订购周期数。取值范围：periodType&#x3D;month（周期类型为月）时，取值为[1-9]。periodType&#x3D;year（周期类型为年）时，取值为1。 说明：chargingMode为prePaid时生效，且为必选值。
        :type period_num: int
        :param is_auto_renew: 是否自动续订。true：自动续订false：不自动续订 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为不自动续订。
        :type is_auto_renew: str
        :param is_auto_pay: 下单订购后，是否自动从客户的帐户中支付，而不需要客户手动去支付。true：是（自动支付）false：否（需要客户手动支付） 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为客户手动支付。
        :type is_auto_pay: str
        :param enterprise_project_id: 企业项目ID。该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。 说明：关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理API参考》。
        :type enterprise_project_id: str
        """
        
        

        self._charging_mode = None
        self._region_id = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._enterprise_project_id = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if region_id is not None:
            self.region_id = region_id
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ExtendParam.

        计费模式。取值范围：prePaid：预付费，即包年包月; postPaid-后付费，即按需付费。默认值是prePaid。

        :return: The charging_mode of this ExtendParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ExtendParam.

        计费模式。取值范围：prePaid：预付费，即包年包月; postPaid-后付费，即按需付费。默认值是prePaid。

        :param charging_mode: The charging_mode of this ExtendParam.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def region_id(self):
        r"""Gets the region_id of this ExtendParam.

        裸金属服务器所在区域ID。请参考地区和终端节点获取。

        :return: The region_id of this ExtendParam.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ExtendParam.

        裸金属服务器所在区域ID。请参考地区和终端节点获取。

        :param region_id: The region_id of this ExtendParam.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def period_type(self):
        r"""Gets the period_type of this ExtendParam.

        订购周期类型。取值范围：month：月year：年 说明：chargingMode为prePaid时生效，且为必选值。

        :return: The period_type of this ExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ExtendParam.

        订购周期类型。取值范围：month：月year：年 说明：chargingMode为prePaid时生效，且为必选值。

        :param period_type: The period_type of this ExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ExtendParam.

        订购周期数。取值范围：periodType=month（周期类型为月）时，取值为[1-9]。periodType=year（周期类型为年）时，取值为1。 说明：chargingMode为prePaid时生效，且为必选值。

        :return: The period_num of this ExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ExtendParam.

        订购周期数。取值范围：periodType=month（周期类型为月）时，取值为[1-9]。periodType=year（周期类型为年）时，取值为1。 说明：chargingMode为prePaid时生效，且为必选值。

        :param period_num: The period_num of this ExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ExtendParam.

        是否自动续订。true：自动续订false：不自动续订 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为不自动续订。

        :return: The is_auto_renew of this ExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ExtendParam.

        是否自动续订。true：自动续订false：不自动续订 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为不自动续订。

        :param is_auto_renew: The is_auto_renew of this ExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ExtendParam.

        下单订购后，是否自动从客户的帐户中支付，而不需要客户手动去支付。true：是（自动支付）false：否（需要客户手动支付） 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为客户手动支付。

        :return: The is_auto_pay of this ExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ExtendParam.

        下单订购后，是否自动从客户的帐户中支付，而不需要客户手动去支付。true：是（自动支付）false：否（需要客户手动支付） 说明：chargingMode为prePaid时生效，不指定该参数或者该参数值为空时默认为客户手动支付。

        :param is_auto_pay: The is_auto_pay of this ExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExtendParam.

        企业项目ID。该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。 说明：关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理API参考》。

        :return: The enterprise_project_id of this ExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExtendParam.

        企业项目ID。该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。 说明：关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理API参考》。

        :param enterprise_project_id: The enterprise_project_id of this ExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
