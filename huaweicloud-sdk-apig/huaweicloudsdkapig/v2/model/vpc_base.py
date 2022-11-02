# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcBase:

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
        'port': 'int',
        'balance_strategy': 'int',
        'member_type': 'str',
        'dict_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'balance_strategy': 'balance_strategy',
        'member_type': 'member_type',
        'dict_code': 'dict_code'
    }

    def __init__(self, name=None, port=None, balance_strategy=None, member_type=None, dict_code=None):
        """VpcBase

        The model defined in huaweicloud sdk

        :param name: VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param port: VPC通道中主机的端口号。  取值范围1 ~ 65535。
        :type port: int
        :param balance_strategy: 分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）
        :type balance_strategy: int
        :param member_type: VPC通道的成员类型。 - ip - ecs
        :type member_type: str
        :param dict_code: VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
        """
        
        

        self._name = None
        self._port = None
        self._balance_strategy = None
        self._member_type = None
        self._dict_code = None
        self.discriminator = None

        self.name = name
        self.port = port
        self.balance_strategy = balance_strategy
        self.member_type = member_type
        if dict_code is not None:
            self.dict_code = dict_code

    @property
    def name(self):
        """Gets the name of this VpcBase.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this VpcBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpcBase.

        VPC通道的名称。  长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、中划线、下划线组成，且只能以英文或中文开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this VpcBase.
        :type name: str
        """
        self._name = name

    @property
    def port(self):
        """Gets the port of this VpcBase.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :return: The port of this VpcBase.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VpcBase.

        VPC通道中主机的端口号。  取值范围1 ~ 65535。

        :param port: The port of this VpcBase.
        :type port: int
        """
        self._port = port

    @property
    def balance_strategy(self):
        """Gets the balance_strategy of this VpcBase.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :return: The balance_strategy of this VpcBase.
        :rtype: int
        """
        return self._balance_strategy

    @balance_strategy.setter
    def balance_strategy(self, balance_strategy):
        """Sets the balance_strategy of this VpcBase.

        分发算法。 - 1：加权轮询（wrr） - 2：加权最少连接（wleastconn） - 3：源地址哈希（source） - 4：URI哈希（uri）

        :param balance_strategy: The balance_strategy of this VpcBase.
        :type balance_strategy: int
        """
        self._balance_strategy = balance_strategy

    @property
    def member_type(self):
        """Gets the member_type of this VpcBase.

        VPC通道的成员类型。 - ip - ecs

        :return: The member_type of this VpcBase.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this VpcBase.

        VPC通道的成员类型。 - ip - ecs

        :param member_type: The member_type of this VpcBase.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def dict_code(self):
        """Gets the dict_code of this VpcBase.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this VpcBase.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        """Sets the dict_code of this VpcBase.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this VpcBase.
        :type dict_code: str
        """
        self._dict_code = dict_code

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
        if not isinstance(other, VpcBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
