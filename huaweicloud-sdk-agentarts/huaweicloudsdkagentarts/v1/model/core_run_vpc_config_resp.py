# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunVpcConfigResp:

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
        'subnet_id': 'str',
        'security_group_ids': 'list[str]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_ids': 'security_group_ids'
    }

    def __init__(self, vpc_id=None, subnet_id=None, security_group_ids=None):
        r"""CoreRunVpcConfigResp

        The model defined in huaweicloud sdk

        :param vpc_id: **参数解释**: VPC ID。 **取值范围**: 匹配标准的UUID格式。 
        :type vpc_id: str
        :param subnet_id: **参数解释**: 子网ID。 **取值范围**: 匹配标准的UUID格式。 
        :type subnet_id: str
        :param security_group_ids: **参数解释**: VPC关联的安全组ID列表。 **取值范围**: 元素个数0-10个，每个安全组值的长度为 1 - 36 个字符。 
        :type security_group_ids: list[str]
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._security_group_ids = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CoreRunVpcConfigResp.

        **参数解释**: VPC ID。 **取值范围**: 匹配标准的UUID格式。 

        :return: The vpc_id of this CoreRunVpcConfigResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CoreRunVpcConfigResp.

        **参数解释**: VPC ID。 **取值范围**: 匹配标准的UUID格式。 

        :param vpc_id: The vpc_id of this CoreRunVpcConfigResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CoreRunVpcConfigResp.

        **参数解释**: 子网ID。 **取值范围**: 匹配标准的UUID格式。 

        :return: The subnet_id of this CoreRunVpcConfigResp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CoreRunVpcConfigResp.

        **参数解释**: 子网ID。 **取值范围**: 匹配标准的UUID格式。 

        :param subnet_id: The subnet_id of this CoreRunVpcConfigResp.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this CoreRunVpcConfigResp.

        **参数解释**: VPC关联的安全组ID列表。 **取值范围**: 元素个数0-10个，每个安全组值的长度为 1 - 36 个字符。 

        :return: The security_group_ids of this CoreRunVpcConfigResp.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this CoreRunVpcConfigResp.

        **参数解释**: VPC关联的安全组ID列表。 **取值范围**: 元素个数0-10个，每个安全组值的长度为 1 - 36 个字符。 

        :param security_group_ids: The security_group_ids of this CoreRunVpcConfigResp.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

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
        if not isinstance(other, CoreRunVpcConfigResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
