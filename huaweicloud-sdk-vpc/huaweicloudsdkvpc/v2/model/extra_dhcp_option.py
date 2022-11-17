# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtraDhcpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opt_name': 'str',
        'opt_value': 'str'
    }

    attribute_map = {
        'opt_name': 'opt_name',
        'opt_value': 'opt_value'
    }

    def __init__(self, opt_name=None, opt_value=None):
        """ExtraDhcpOption

        The model defined in huaweicloud sdk

        :param opt_name: 功能说明：子网配置的NTP地址名称或子网配置的租约到期名称。 约束：目前只支持字段“ntp”或“addresstime”
        :type opt_name: str
        :param opt_value: 功能说明：子网配置的NTP地址或子网配置的租约到期时间。 约束：opt_name配置为“ntp”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 该字段为null表示取消该子网NTP的设置，不能为””(空字符串)。 opt_name配置为“addresstime”，则该值表示是子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~30000，比如5h。
        :type opt_value: str
        """
        
        

        self._opt_name = None
        self._opt_value = None
        self.discriminator = None

        self.opt_name = opt_name
        if opt_value is not None:
            self.opt_value = opt_value

    @property
    def opt_name(self):
        """Gets the opt_name of this ExtraDhcpOption.

        功能说明：子网配置的NTP地址名称或子网配置的租约到期名称。 约束：目前只支持字段“ntp”或“addresstime”

        :return: The opt_name of this ExtraDhcpOption.
        :rtype: str
        """
        return self._opt_name

    @opt_name.setter
    def opt_name(self, opt_name):
        """Sets the opt_name of this ExtraDhcpOption.

        功能说明：子网配置的NTP地址名称或子网配置的租约到期名称。 约束：目前只支持字段“ntp”或“addresstime”

        :param opt_name: The opt_name of this ExtraDhcpOption.
        :type opt_name: str
        """
        self._opt_name = opt_name

    @property
    def opt_value(self):
        """Gets the opt_value of this ExtraDhcpOption.

        功能说明：子网配置的NTP地址或子网配置的租约到期时间。 约束：opt_name配置为“ntp”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 该字段为null表示取消该子网NTP的设置，不能为””(空字符串)。 opt_name配置为“addresstime”，则该值表示是子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~30000，比如5h。

        :return: The opt_value of this ExtraDhcpOption.
        :rtype: str
        """
        return self._opt_value

    @opt_value.setter
    def opt_value(self, opt_value):
        """Sets the opt_value of this ExtraDhcpOption.

        功能说明：子网配置的NTP地址或子网配置的租约到期时间。 约束：opt_name配置为“ntp”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 该字段为null表示取消该子网NTP的设置，不能为””(空字符串)。 opt_name配置为“addresstime”，则该值表示是子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~30000，比如5h。

        :param opt_value: The opt_value of this ExtraDhcpOption.
        :type opt_value: str
        """
        self._opt_value = opt_value

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
        if not isinstance(other, ExtraDhcpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
