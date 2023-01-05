# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNet2CloudPhoneServerRequestBodyExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_pay': 'int',
        'is_auto_renew': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_pay': 'is_auto_pay',
        'is_auto_renew': 'is_auto_renew',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, charging_mode=None, period_type=None, period_num=None, is_auto_pay=None, is_auto_renew=None, enterprise_project_id=None):
        """CreateNet2CloudPhoneServerRequestBodyExtendParam

        The model defined in huaweicloud sdk

        :param charging_mode: 计费类型  0 表示包周期
        :type charging_mode: int
        :param period_type: 订购周期类型 2 表示月 3 表示年
        :type period_type: int
        :param period_num: 订购周期数 当订购周期为月时，取值范围[1, 9]。 当订购周期为年时，取值范围[1,10]
        :type period_num: int
        :param is_auto_pay: 是否自动付款。默认不自动付款。 1 表示自动付款 0 表示不自动付款
        :type is_auto_pay: int
        :param is_auto_renew: 是否自动续订。默认不自动续订。 1 表示自动续订 0 表示不自动续订
        :type is_auto_renew: int
        :param enterprise_project_id: 企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。
        :type enterprise_project_id: str
        """
        
        

        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_pay = None
        self._is_auto_renew = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        计费类型  0 表示包周期

        :return: The charging_mode of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        计费类型  0 表示包周期

        :param charging_mode: The charging_mode of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        订购周期类型 2 表示月 3 表示年

        :return: The period_type of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        订购周期类型 2 表示月 3 表示年

        :param period_type: The period_type of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        订购周期数 当订购周期为月时，取值范围[1, 9]。 当订购周期为年时，取值范围[1,10]

        :return: The period_num of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        订购周期数 当订购周期为月时，取值范围[1, 9]。 当订购周期为年时，取值范围[1,10]

        :param period_num: The period_num of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        是否自动付款。默认不自动付款。 1 表示自动付款 0 表示不自动付款

        :return: The is_auto_pay of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        是否自动付款。默认不自动付款。 1 表示自动付款 0 表示不自动付款

        :param is_auto_pay: The is_auto_pay of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        是否自动续订。默认不自动续订。 1 表示自动续订 0 表示不自动续订

        :return: The is_auto_renew of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        是否自动续订。默认不自动续订。 1 表示自动续订 0 表示不自动续订

        :param is_auto_renew: The is_auto_renew of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :return: The enterprise_project_id of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateNet2CloudPhoneServerRequestBodyExtendParam.

        企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateNet2CloudPhoneServerRequestBodyExtendParam.
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
        if not isinstance(other, CreateNet2CloudPhoneServerRequestBodyExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
