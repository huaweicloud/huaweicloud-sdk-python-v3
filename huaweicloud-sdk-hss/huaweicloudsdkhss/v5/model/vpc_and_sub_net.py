# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcAndSubNet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id_list': 'list[str]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id_list': 'subnet_id_list'
    }

    def __init__(self, vpc_id=None, subnet_id_list=None):
        r"""VpcAndSubNet

        The model defined in huaweicloud sdk

        :param vpc_id: **参数解释** Vpc标识ID **约束限制**: 不涉及 **取值范围** 字符长度1-256位 **默认取值**: 不涉及 
        :type vpc_id: str
        :param subnet_id_list: **参数解释** 子网id的列表 **约束限制**: 不涉及 
        :type subnet_id_list: list[str]
        """
        
        

        self._vpc_id = None
        self._subnet_id_list = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id_list = subnet_id_list

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VpcAndSubNet.

        **参数解释** Vpc标识ID **约束限制**: 不涉及 **取值范围** 字符长度1-256位 **默认取值**: 不涉及 

        :return: The vpc_id of this VpcAndSubNet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VpcAndSubNet.

        **参数解释** Vpc标识ID **约束限制**: 不涉及 **取值范围** 字符长度1-256位 **默认取值**: 不涉及 

        :param vpc_id: The vpc_id of this VpcAndSubNet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id_list(self):
        r"""Gets the subnet_id_list of this VpcAndSubNet.

        **参数解释** 子网id的列表 **约束限制**: 不涉及 

        :return: The subnet_id_list of this VpcAndSubNet.
        :rtype: list[str]
        """
        return self._subnet_id_list

    @subnet_id_list.setter
    def subnet_id_list(self, subnet_id_list):
        r"""Sets the subnet_id_list of this VpcAndSubNet.

        **参数解释** 子网id的列表 **约束限制**: 不涉及 

        :param subnet_id_list: The subnet_id_list of this VpcAndSubNet.
        :type subnet_id_list: list[str]
        """
        self._subnet_id_list = subnet_id_list

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
        if not isinstance(other, VpcAndSubNet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
