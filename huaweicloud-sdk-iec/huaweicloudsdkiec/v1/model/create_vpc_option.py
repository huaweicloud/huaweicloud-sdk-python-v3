# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcOption:

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
        'cidr': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cidr': 'cidr',
        'mode': 'mode'
    }

    def __init__(self, name=None, cidr=None, mode=None):
        """CreateVpcOption

        The model defined in huaweicloud sdk

        :param name: 虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复
        :type name: str
        :param cidr: 虚拟私有云下可用子网的范围。  约束： SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)
        :type cidr: str
        :param mode: 虚拟私有云的模式，支持的取值范围如下：  SYSTEM：该类型网络，系统会自动按照实际需要创建足够的子网。 [CUSTOMER：该类型网络，用户需要完全按照自己站点的需要，去申请足够的子网。](tag:internal)
        :type mode: str
        """
        
        

        self._name = None
        self._cidr = None
        self._mode = None
        self.discriminator = None

        self.name = name
        self.cidr = cidr
        self.mode = mode

    @property
    def name(self):
        """Gets the name of this CreateVpcOption.

        虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复

        :return: The name of this CreateVpcOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcOption.

        虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复

        :param name: The name of this CreateVpcOption.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this CreateVpcOption.

        虚拟私有云下可用子网的范围。  约束： SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)

        :return: The cidr of this CreateVpcOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateVpcOption.

        虚拟私有云下可用子网的范围。  约束： SYSTEM模式，cidr取值范围：10.0.0.0/8~10.255.0.0/16或者172.16.0.0/12 ~ 172.31.0.0/16或者192.168.0.0/16 。 [CUSTOMER模式，cidr的取值范围：10.0.0.0/8~10.255.255.0/24或者172.16.0.0/12 ~ 172.32.255.0/24或者192.168.0.0/16~192.168.255.0/24。](tag:internal)

        :param cidr: The cidr of this CreateVpcOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def mode(self):
        """Gets the mode of this CreateVpcOption.

        虚拟私有云的模式，支持的取值范围如下：  SYSTEM：该类型网络，系统会自动按照实际需要创建足够的子网。 [CUSTOMER：该类型网络，用户需要完全按照自己站点的需要，去申请足够的子网。](tag:internal)

        :return: The mode of this CreateVpcOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateVpcOption.

        虚拟私有云的模式，支持的取值范围如下：  SYSTEM：该类型网络，系统会自动按照实际需要创建足够的子网。 [CUSTOMER：该类型网络，用户需要完全按照自己站点的需要，去申请足够的子网。](tag:internal)

        :param mode: The mode of this CreateVpcOption.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, CreateVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
