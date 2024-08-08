# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForwardingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip': 'str',
        'enable_snat': 'bool'
    }

    attribute_map = {
        'eip': 'eip',
        'enable_snat': 'enable_snat'
    }

    def __init__(self, eip=None, enable_snat=None):
        """ForwardingInfo

        The model defined in huaweicloud sdk

        :param eip: **参数说明**：NAT网关绑定的EIP 
        :type eip: str
        :param enable_snat: **参数说明**：是否启用SNAT配置 **取值范围**： - true: SNAT配置已启用 - false: SNAT配置未启用 
        :type enable_snat: bool
        """
        
        

        self._eip = None
        self._enable_snat = None
        self.discriminator = None

        if eip is not None:
            self.eip = eip
        if enable_snat is not None:
            self.enable_snat = enable_snat

    @property
    def eip(self):
        """Gets the eip of this ForwardingInfo.

        **参数说明**：NAT网关绑定的EIP 

        :return: The eip of this ForwardingInfo.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this ForwardingInfo.

        **参数说明**：NAT网关绑定的EIP 

        :param eip: The eip of this ForwardingInfo.
        :type eip: str
        """
        self._eip = eip

    @property
    def enable_snat(self):
        """Gets the enable_snat of this ForwardingInfo.

        **参数说明**：是否启用SNAT配置 **取值范围**： - true: SNAT配置已启用 - false: SNAT配置未启用 

        :return: The enable_snat of this ForwardingInfo.
        :rtype: bool
        """
        return self._enable_snat

    @enable_snat.setter
    def enable_snat(self, enable_snat):
        """Sets the enable_snat of this ForwardingInfo.

        **参数说明**：是否启用SNAT配置 **取值范围**： - true: SNAT配置已启用 - false: SNAT配置未启用 

        :param enable_snat: The enable_snat of this ForwardingInfo.
        :type enable_snat: bool
        """
        self._enable_snat = enable_snat

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
        if not isinstance(other, ForwardingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
