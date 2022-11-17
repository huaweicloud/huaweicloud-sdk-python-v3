# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'cidr': 'str',
        'mode': 'str',
        'subnet_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'mode': 'mode',
        'subnet_num': 'subnet_num'
    }

    def __init__(self, id=None, name=None, cidr=None, mode=None, subnet_num=None):
        """Vpc

        The model defined in huaweicloud sdk

        :param id: 虚拟私有云的ID。
        :type id: str
        :param name: 虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复
        :type name: str
        :param cidr: 虚拟私有云下可用子网的范围  取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24  约束：必须是cidr格式，例如:192.168.0.0/16
        :type cidr: str
        :param mode: 虚拟私有云的模式。
        :type mode: str
        :param subnet_num: 子网的数目。
        :type subnet_num: int
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self._mode = None
        self._subnet_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cidr is not None:
            self.cidr = cidr
        if mode is not None:
            self.mode = mode
        if subnet_num is not None:
            self.subnet_num = subnet_num

    @property
    def id(self):
        """Gets the id of this Vpc.

        虚拟私有云的ID。

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vpc.

        虚拟私有云的ID。

        :param id: The id of this Vpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vpc.

        虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vpc.

        虚拟私有云名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：同一个帐号下的名称不能重复

        :param name: The name of this Vpc.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this Vpc.

        虚拟私有云下可用子网的范围  取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24  约束：必须是cidr格式，例如:192.168.0.0/16

        :return: The cidr of this Vpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Vpc.

        虚拟私有云下可用子网的范围  取值范围： 10.0.0.0/8~24 172.16.0.0/12~24 192.168.0.0/16~24  约束：必须是cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this Vpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def mode(self):
        """Gets the mode of this Vpc.

        虚拟私有云的模式。

        :return: The mode of this Vpc.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Vpc.

        虚拟私有云的模式。

        :param mode: The mode of this Vpc.
        :type mode: str
        """
        self._mode = mode

    @property
    def subnet_num(self):
        """Gets the subnet_num of this Vpc.

        子网的数目。

        :return: The subnet_num of this Vpc.
        :rtype: int
        """
        return self._subnet_num

    @subnet_num.setter
    def subnet_num(self, subnet_num):
        """Sets the subnet_num of this Vpc.

        子网的数目。

        :param subnet_num: The subnet_num of this Vpc.
        :type subnet_num: int
        """
        self._subnet_num = subnet_num

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
