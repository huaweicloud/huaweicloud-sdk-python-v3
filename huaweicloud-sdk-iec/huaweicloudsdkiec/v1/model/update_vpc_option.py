# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cidr': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cidr': 'cidr'
    }

    def __init__(self, name=None, cidr=None):
        """UpdateVpcOption

        The model defined in huaweicloud sdk

        :param name: 虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的VPC不允许重名
        :type name: str
        :param cidr: 虚拟私有云下可用子网的范围。  约束条件：  SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)
        :type cidr: str
        """
        
        

        self._name = None
        self._cidr = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cidr is not None:
            self.cidr = cidr

    @property
    def name(self):
        """Gets the name of this UpdateVpcOption.

        虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的VPC不允许重名

        :return: The name of this UpdateVpcOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVpcOption.

        虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的VPC不允许重名

        :param name: The name of this UpdateVpcOption.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this UpdateVpcOption.

        虚拟私有云下可用子网的范围。  约束条件：  SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)

        :return: The cidr of this UpdateVpcOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this UpdateVpcOption.

        虚拟私有云下可用子网的范围。  约束条件：  SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)

        :param cidr: The cidr of this UpdateVpcOption.
        :type cidr: str
        """
        self._cidr = cidr

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
        if not isinstance(other, UpdateVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
