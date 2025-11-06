# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyInstancePortRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int'
    }

    attribute_map = {
        'port': 'port'
    }

    def __init__(self, port=None):
        r"""ModifyInstancePortRequestBody

        The model defined in huaweicloud sdk

        :param port: **参数解释**: 实例设置的数据库端口号。 **约束限制**: 不涉及。 **取值范围**: 1024~39998（其中2378、2379、2380、4999、5000、5999、6000、60001、8097、8098、12016、12017、20049、20050、21731、21732、32122、32123和32124被系统占用不可设置）。 **默认取值**: 不涉及。
        :type port: int
        """
        
        

        self._port = None
        self.discriminator = None

        self.port = port

    @property
    def port(self):
        r"""Gets the port of this ModifyInstancePortRequestBody.

        **参数解释**: 实例设置的数据库端口号。 **约束限制**: 不涉及。 **取值范围**: 1024~39998（其中2378、2379、2380、4999、5000、5999、6000、60001、8097、8098、12016、12017、20049、20050、21731、21732、32122、32123和32124被系统占用不可设置）。 **默认取值**: 不涉及。

        :return: The port of this ModifyInstancePortRequestBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ModifyInstancePortRequestBody.

        **参数解释**: 实例设置的数据库端口号。 **约束限制**: 不涉及。 **取值范围**: 1024~39998（其中2378、2379、2380、4999、5000、5999、6000、60001、8097、8098、12016、12017、20049、20050、21731、21732、32122、32123和32124被系统占用不可设置）。 **默认取值**: 不涉及。

        :param port: The port of this ModifyInstancePortRequestBody.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, ModifyInstancePortRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
