# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalParamsResp:

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
        'security_group_id': 'str',
        'ciphering_algorithm': 'str',
        'forwarding_info': 'ForwardingInfo'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'ciphering_algorithm': 'ciphering_algorithm',
        'forwarding_info': 'forwarding_info'
    }

    def __init__(self, vpc_id=None, subnet_id=None, security_group_id=None, ciphering_algorithm=None, forwarding_info=None):
        r"""AdditionalParamsResp

        The model defined in huaweicloud sdk

        :param vpc_id: **参数说明**：企业版实例的VPCID 
        :type vpc_id: str
        :param subnet_id: **参数说明**：企业版实例的子网ID 
        :type subnet_id: str
        :param security_group_id: **参数说明**：企业版实例的安全组ID 
        :type security_group_id: str
        :param ciphering_algorithm: **参数说明**：实例支持的加密算法 **取值范围**： - COMMON_ALGORITHM: 通用加密算法（支持RSA，SHA256等国际通用的密码算法） - SM_ALGORITHM: 支持SM系列商密算法（支持SM2，SM3，SM4等国密算法） 
        :type ciphering_algorithm: str
        :param forwarding_info: 
        :type forwarding_info: :class:`huaweicloudsdkiotdm.v5.ForwardingInfo`
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._ciphering_algorithm = None
        self._forwarding_info = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if ciphering_algorithm is not None:
            self.ciphering_algorithm = ciphering_algorithm
        if forwarding_info is not None:
            self.forwarding_info = forwarding_info

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的VPCID 

        :return: The vpc_id of this AdditionalParamsResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的VPCID 

        :param vpc_id: The vpc_id of this AdditionalParamsResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的子网ID 

        :return: The subnet_id of this AdditionalParamsResp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的子网ID 

        :param subnet_id: The subnet_id of this AdditionalParamsResp.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的安全组ID 

        :return: The security_group_id of this AdditionalParamsResp.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this AdditionalParamsResp.

        **参数说明**：企业版实例的安全组ID 

        :param security_group_id: The security_group_id of this AdditionalParamsResp.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def ciphering_algorithm(self):
        r"""Gets the ciphering_algorithm of this AdditionalParamsResp.

        **参数说明**：实例支持的加密算法 **取值范围**： - COMMON_ALGORITHM: 通用加密算法（支持RSA，SHA256等国际通用的密码算法） - SM_ALGORITHM: 支持SM系列商密算法（支持SM2，SM3，SM4等国密算法） 

        :return: The ciphering_algorithm of this AdditionalParamsResp.
        :rtype: str
        """
        return self._ciphering_algorithm

    @ciphering_algorithm.setter
    def ciphering_algorithm(self, ciphering_algorithm):
        r"""Sets the ciphering_algorithm of this AdditionalParamsResp.

        **参数说明**：实例支持的加密算法 **取值范围**： - COMMON_ALGORITHM: 通用加密算法（支持RSA，SHA256等国际通用的密码算法） - SM_ALGORITHM: 支持SM系列商密算法（支持SM2，SM3，SM4等国密算法） 

        :param ciphering_algorithm: The ciphering_algorithm of this AdditionalParamsResp.
        :type ciphering_algorithm: str
        """
        self._ciphering_algorithm = ciphering_algorithm

    @property
    def forwarding_info(self):
        r"""Gets the forwarding_info of this AdditionalParamsResp.

        :return: The forwarding_info of this AdditionalParamsResp.
        :rtype: :class:`huaweicloudsdkiotdm.v5.ForwardingInfo`
        """
        return self._forwarding_info

    @forwarding_info.setter
    def forwarding_info(self, forwarding_info):
        r"""Sets the forwarding_info of this AdditionalParamsResp.

        :param forwarding_info: The forwarding_info of this AdditionalParamsResp.
        :type forwarding_info: :class:`huaweicloudsdkiotdm.v5.ForwardingInfo`
        """
        self._forwarding_info = forwarding_info

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
        if not isinstance(other, AdditionalParamsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
