# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewResourceConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'config_value': 'str'
    }

    attribute_map = {
        'config_name': 'config_name',
        'config_value': 'config_value'
    }

    def __init__(self, config_name=None, config_value=None):
        r"""RenewResourceConfigReq

        The model defined in huaweicloud sdk

        :param config_name: |参数名称：续订资源设置属性类型| |参数的约束及描述：该参数必填，设置类型，支持枚举| |DEDUCTION_DATE：设置自动续费扣款日，EXPIRE_DATE：设置续费后资源统一到期日|
        :type config_name: str
        :param config_value: |参数名称：续订资源设置属性值| |参数约束及描述：该参数必填，当config_name值为DEDUCTION_DATE时，支持设置资源到期前2天至前7天自动扣款，config_value范围：2，3，4，5，6，7。 当config_name值为EXPIRE_DATE时，支持设置统一到期日为每个月的同一天（1~28号及每个月最后一天），config_value范围：1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23，24，25，26，27，28，-1|
        :type config_value: str
        """
        
        

        self._config_name = None
        self._config_value = None
        self.discriminator = None

        self.config_name = config_name
        self.config_value = config_value

    @property
    def config_name(self):
        r"""Gets the config_name of this RenewResourceConfigReq.

        |参数名称：续订资源设置属性类型| |参数的约束及描述：该参数必填，设置类型，支持枚举| |DEDUCTION_DATE：设置自动续费扣款日，EXPIRE_DATE：设置续费后资源统一到期日|

        :return: The config_name of this RenewResourceConfigReq.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this RenewResourceConfigReq.

        |参数名称：续订资源设置属性类型| |参数的约束及描述：该参数必填，设置类型，支持枚举| |DEDUCTION_DATE：设置自动续费扣款日，EXPIRE_DATE：设置续费后资源统一到期日|

        :param config_name: The config_name of this RenewResourceConfigReq.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        r"""Gets the config_value of this RenewResourceConfigReq.

        |参数名称：续订资源设置属性值| |参数约束及描述：该参数必填，当config_name值为DEDUCTION_DATE时，支持设置资源到期前2天至前7天自动扣款，config_value范围：2，3，4，5，6，7。 当config_name值为EXPIRE_DATE时，支持设置统一到期日为每个月的同一天（1~28号及每个月最后一天），config_value范围：1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23，24，25，26，27，28，-1|

        :return: The config_value of this RenewResourceConfigReq.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this RenewResourceConfigReq.

        |参数名称：续订资源设置属性值| |参数约束及描述：该参数必填，当config_name值为DEDUCTION_DATE时，支持设置资源到期前2天至前7天自动扣款，config_value范围：2，3，4，5，6，7。 当config_name值为EXPIRE_DATE时，支持设置统一到期日为每个月的同一天（1~28号及每个月最后一天），config_value范围：1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23，24，25，26，27，28，-1|

        :param config_value: The config_value of this RenewResourceConfigReq.
        :type config_value: str
        """
        self._config_value = config_value

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
        if not isinstance(other, RenewResourceConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
