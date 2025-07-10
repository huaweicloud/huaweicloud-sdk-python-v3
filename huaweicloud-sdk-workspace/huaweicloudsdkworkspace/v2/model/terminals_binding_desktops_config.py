# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TerminalsBindingDesktopsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tc_bind_switch': 'str',
        'tc_auto_bind_switch': 'str',
        'tc_auto_bind_max': 'int'
    }

    attribute_map = {
        'tc_bind_switch': 'tc_bind_switch',
        'tc_auto_bind_switch': 'tc_auto_bind_switch',
        'tc_auto_bind_max': 'tc_auto_bind_max'
    }

    def __init__(self, tc_bind_switch=None, tc_auto_bind_switch=None, tc_auto_bind_max=None):
        r"""TerminalsBindingDesktopsConfig

        The model defined in huaweicloud sdk

        :param tc_bind_switch: 绑定开关，只取值ON或OFF。
        :type tc_bind_switch: str
        :param tc_auto_bind_switch: 自动绑定开关，只取值ON或OFF。
        :type tc_auto_bind_switch: str
        :param tc_auto_bind_max: 最大绑定数量，默认值为1。
        :type tc_auto_bind_max: int
        """
        
        

        self._tc_bind_switch = None
        self._tc_auto_bind_switch = None
        self._tc_auto_bind_max = None
        self.discriminator = None

        self.tc_bind_switch = tc_bind_switch
        if tc_auto_bind_switch is not None:
            self.tc_auto_bind_switch = tc_auto_bind_switch
        if tc_auto_bind_max is not None:
            self.tc_auto_bind_max = tc_auto_bind_max

    @property
    def tc_bind_switch(self):
        r"""Gets the tc_bind_switch of this TerminalsBindingDesktopsConfig.

        绑定开关，只取值ON或OFF。

        :return: The tc_bind_switch of this TerminalsBindingDesktopsConfig.
        :rtype: str
        """
        return self._tc_bind_switch

    @tc_bind_switch.setter
    def tc_bind_switch(self, tc_bind_switch):
        r"""Sets the tc_bind_switch of this TerminalsBindingDesktopsConfig.

        绑定开关，只取值ON或OFF。

        :param tc_bind_switch: The tc_bind_switch of this TerminalsBindingDesktopsConfig.
        :type tc_bind_switch: str
        """
        self._tc_bind_switch = tc_bind_switch

    @property
    def tc_auto_bind_switch(self):
        r"""Gets the tc_auto_bind_switch of this TerminalsBindingDesktopsConfig.

        自动绑定开关，只取值ON或OFF。

        :return: The tc_auto_bind_switch of this TerminalsBindingDesktopsConfig.
        :rtype: str
        """
        return self._tc_auto_bind_switch

    @tc_auto_bind_switch.setter
    def tc_auto_bind_switch(self, tc_auto_bind_switch):
        r"""Sets the tc_auto_bind_switch of this TerminalsBindingDesktopsConfig.

        自动绑定开关，只取值ON或OFF。

        :param tc_auto_bind_switch: The tc_auto_bind_switch of this TerminalsBindingDesktopsConfig.
        :type tc_auto_bind_switch: str
        """
        self._tc_auto_bind_switch = tc_auto_bind_switch

    @property
    def tc_auto_bind_max(self):
        r"""Gets the tc_auto_bind_max of this TerminalsBindingDesktopsConfig.

        最大绑定数量，默认值为1。

        :return: The tc_auto_bind_max of this TerminalsBindingDesktopsConfig.
        :rtype: int
        """
        return self._tc_auto_bind_max

    @tc_auto_bind_max.setter
    def tc_auto_bind_max(self, tc_auto_bind_max):
        r"""Sets the tc_auto_bind_max of this TerminalsBindingDesktopsConfig.

        最大绑定数量，默认值为1。

        :param tc_auto_bind_max: The tc_auto_bind_max of this TerminalsBindingDesktopsConfig.
        :type tc_auto_bind_max: int
        """
        self._tc_auto_bind_max = tc_auto_bind_max

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
        if not isinstance(other, TerminalsBindingDesktopsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
