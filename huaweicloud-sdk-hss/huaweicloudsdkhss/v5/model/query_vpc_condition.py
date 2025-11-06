# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVpcCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'vpc_id_list': 'list[str]'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'vpc_id_list': 'vpc_id_list'
    }

    def __init__(self, host_id_list=None, vpc_id_list=None):
        r"""QueryVpcCondition

        The model defined in huaweicloud sdk

        :param host_id_list: **参数解释**: 主机id列表 **取值范围**: 字符长度1-64位 
        :type host_id_list: list[str]
        :param vpc_id_list: **参数解释**: VpcId列表 **取值范围**: 字符长度1-64位 
        :type vpc_id_list: list[str]
        """
        
        

        self._host_id_list = None
        self._vpc_id_list = None
        self.discriminator = None

        if host_id_list is not None:
            self.host_id_list = host_id_list
        if vpc_id_list is not None:
            self.vpc_id_list = vpc_id_list

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this QueryVpcCondition.

        **参数解释**: 主机id列表 **取值范围**: 字符长度1-64位 

        :return: The host_id_list of this QueryVpcCondition.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this QueryVpcCondition.

        **参数解释**: 主机id列表 **取值范围**: 字符长度1-64位 

        :param host_id_list: The host_id_list of this QueryVpcCondition.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def vpc_id_list(self):
        r"""Gets the vpc_id_list of this QueryVpcCondition.

        **参数解释**: VpcId列表 **取值范围**: 字符长度1-64位 

        :return: The vpc_id_list of this QueryVpcCondition.
        :rtype: list[str]
        """
        return self._vpc_id_list

    @vpc_id_list.setter
    def vpc_id_list(self, vpc_id_list):
        r"""Sets the vpc_id_list of this QueryVpcCondition.

        **参数解释**: VpcId列表 **取值范围**: 字符长度1-64位 

        :param vpc_id_list: The vpc_id_list of this QueryVpcCondition.
        :type vpc_id_list: list[str]
        """
        self._vpc_id_list = vpc_id_list

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
        if not isinstance(other, QueryVpcCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
