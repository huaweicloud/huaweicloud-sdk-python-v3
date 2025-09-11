# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HbaConfOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'database': 'str',
        'user': 'str',
        'address': 'str',
        'method': 'str'
    }

    attribute_map = {
        'type': 'type',
        'database': 'database',
        'user': 'user',
        'address': 'address',
        'method': 'method'
    }

    def __init__(self, type=None, database=None, user=None, address=None, method=None):
        r"""HbaConfOption

        The model defined in huaweicloud sdk

        :param type: **参数解释** 客户端连接类型。 **约束限制**: 不涉及。 **取值范围** - host：表示这条记录既接受一个普通的TCP/IP套接字连接，也接受一个经过SSL加密的TCP/IP套接字连接。 - hostssl：表示这条记录只接受一个经过SSL加密的TCP/IP套接字连接。 - hostnossl：表示这条记录只接受一个普通的TCP/IP套接字连接。  **默认取值**: 不涉及。 
        :type type: str
        :param database: **参数解释** 声明记录所匹配且允许访问的数据库，多租特性场景下该参数声明记录所匹配且允许访问的PDB。 - 值replication表示如果请求一个复制连接，则匹配，但复制连接不表示任何特定的数据库。如需使用名为replication的数据库，需在database列使用记录“replication”作为数据库名。 - 多租数据库下， 值replication_pdb1表示如果请求一个名为pdb1数据库的复制连接，则匹配成功。值replication方式只生效Non-PDB。 - PDB复制连接生效配置方式为replication_[pdbname]，pdbname为用户创建PDB数据库时候的名字。 - 如需使用名为replication_pdb1的数据库，需在database列使用记录“replication_pdb1”作为数据库名。  **约束限制**: 不涉及。 **取值范围** - all：表示该记录匹配所有数据库。 - 特定的数据库名称或者用逗号分隔的数据库列表。  **默认取值**: 不涉及。 
        :type database: str
        :param user: **参数解释** 声明记录所匹配且允许访问的数据库用户。 **约束限制** 不支持系统用户。 **取值范围** - all：表明该记录匹配所有用户。 - 特定的数据库用户名或者用逗号分隔的用户列表。 **默认取值**: 不涉及。 
        :type user: str
        :param address: **参数解释** 指定与记录匹配且允许访问的IP地址范围。 **约束限制** 当前仅支持IP地址/掩码长度格式。 数据库引擎版本为V2.0-8.1.0及以上支持address配置IPv6的IP。 **取值范围** 支持IPv4和IPv6，可以使用如下形式来表示： IP地址/掩码长度。例如，10.10.0.0/24、2001:250:250:250:250:250:250:175/128。 **默认取值**: 不涉及。 
        :type address: str
        :param method: **参数解释** 声明连接时使用的认证方法。 **约束限制**: 不涉及。 **取值范围** - reject：无条件地拒绝连接。常用于过滤某些主机。 - md5：MD5加密算法安全性低，存在安全风险，不推荐使用，建议使用更安全的加密算法。默认不支持，可通过password_encryption_type参数配置。 - sha256：要求客户端提供一个sha256算法加密的口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sha256加密，增强了安全性。 - sm3：要求客户端提供一个sm3算法加密口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sm3加密，增加了安全性。 - cert：客户端证书认证模式，此模式需进行SSL连接配置且需要客户端提供有效的SSL证书，不需要提供用户密码。cert认证方式只支持hostssl类型的规则。  **默认取值**: 不涉及。 
        :type method: str
        """
        
        

        self._type = None
        self._database = None
        self._user = None
        self._address = None
        self._method = None
        self.discriminator = None

        self.type = type
        self.database = database
        self.user = user
        self.address = address
        self.method = method

    @property
    def type(self):
        r"""Gets the type of this HbaConfOption.

        **参数解释** 客户端连接类型。 **约束限制**: 不涉及。 **取值范围** - host：表示这条记录既接受一个普通的TCP/IP套接字连接，也接受一个经过SSL加密的TCP/IP套接字连接。 - hostssl：表示这条记录只接受一个经过SSL加密的TCP/IP套接字连接。 - hostnossl：表示这条记录只接受一个普通的TCP/IP套接字连接。  **默认取值**: 不涉及。 

        :return: The type of this HbaConfOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HbaConfOption.

        **参数解释** 客户端连接类型。 **约束限制**: 不涉及。 **取值范围** - host：表示这条记录既接受一个普通的TCP/IP套接字连接，也接受一个经过SSL加密的TCP/IP套接字连接。 - hostssl：表示这条记录只接受一个经过SSL加密的TCP/IP套接字连接。 - hostnossl：表示这条记录只接受一个普通的TCP/IP套接字连接。  **默认取值**: 不涉及。 

        :param type: The type of this HbaConfOption.
        :type type: str
        """
        self._type = type

    @property
    def database(self):
        r"""Gets the database of this HbaConfOption.

        **参数解释** 声明记录所匹配且允许访问的数据库，多租特性场景下该参数声明记录所匹配且允许访问的PDB。 - 值replication表示如果请求一个复制连接，则匹配，但复制连接不表示任何特定的数据库。如需使用名为replication的数据库，需在database列使用记录“replication”作为数据库名。 - 多租数据库下， 值replication_pdb1表示如果请求一个名为pdb1数据库的复制连接，则匹配成功。值replication方式只生效Non-PDB。 - PDB复制连接生效配置方式为replication_[pdbname]，pdbname为用户创建PDB数据库时候的名字。 - 如需使用名为replication_pdb1的数据库，需在database列使用记录“replication_pdb1”作为数据库名。  **约束限制**: 不涉及。 **取值范围** - all：表示该记录匹配所有数据库。 - 特定的数据库名称或者用逗号分隔的数据库列表。  **默认取值**: 不涉及。 

        :return: The database of this HbaConfOption.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this HbaConfOption.

        **参数解释** 声明记录所匹配且允许访问的数据库，多租特性场景下该参数声明记录所匹配且允许访问的PDB。 - 值replication表示如果请求一个复制连接，则匹配，但复制连接不表示任何特定的数据库。如需使用名为replication的数据库，需在database列使用记录“replication”作为数据库名。 - 多租数据库下， 值replication_pdb1表示如果请求一个名为pdb1数据库的复制连接，则匹配成功。值replication方式只生效Non-PDB。 - PDB复制连接生效配置方式为replication_[pdbname]，pdbname为用户创建PDB数据库时候的名字。 - 如需使用名为replication_pdb1的数据库，需在database列使用记录“replication_pdb1”作为数据库名。  **约束限制**: 不涉及。 **取值范围** - all：表示该记录匹配所有数据库。 - 特定的数据库名称或者用逗号分隔的数据库列表。  **默认取值**: 不涉及。 

        :param database: The database of this HbaConfOption.
        :type database: str
        """
        self._database = database

    @property
    def user(self):
        r"""Gets the user of this HbaConfOption.

        **参数解释** 声明记录所匹配且允许访问的数据库用户。 **约束限制** 不支持系统用户。 **取值范围** - all：表明该记录匹配所有用户。 - 特定的数据库用户名或者用逗号分隔的用户列表。 **默认取值**: 不涉及。 

        :return: The user of this HbaConfOption.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this HbaConfOption.

        **参数解释** 声明记录所匹配且允许访问的数据库用户。 **约束限制** 不支持系统用户。 **取值范围** - all：表明该记录匹配所有用户。 - 特定的数据库用户名或者用逗号分隔的用户列表。 **默认取值**: 不涉及。 

        :param user: The user of this HbaConfOption.
        :type user: str
        """
        self._user = user

    @property
    def address(self):
        r"""Gets the address of this HbaConfOption.

        **参数解释** 指定与记录匹配且允许访问的IP地址范围。 **约束限制** 当前仅支持IP地址/掩码长度格式。 数据库引擎版本为V2.0-8.1.0及以上支持address配置IPv6的IP。 **取值范围** 支持IPv4和IPv6，可以使用如下形式来表示： IP地址/掩码长度。例如，10.10.0.0/24、2001:250:250:250:250:250:250:175/128。 **默认取值**: 不涉及。 

        :return: The address of this HbaConfOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this HbaConfOption.

        **参数解释** 指定与记录匹配且允许访问的IP地址范围。 **约束限制** 当前仅支持IP地址/掩码长度格式。 数据库引擎版本为V2.0-8.1.0及以上支持address配置IPv6的IP。 **取值范围** 支持IPv4和IPv6，可以使用如下形式来表示： IP地址/掩码长度。例如，10.10.0.0/24、2001:250:250:250:250:250:250:175/128。 **默认取值**: 不涉及。 

        :param address: The address of this HbaConfOption.
        :type address: str
        """
        self._address = address

    @property
    def method(self):
        r"""Gets the method of this HbaConfOption.

        **参数解释** 声明连接时使用的认证方法。 **约束限制**: 不涉及。 **取值范围** - reject：无条件地拒绝连接。常用于过滤某些主机。 - md5：MD5加密算法安全性低，存在安全风险，不推荐使用，建议使用更安全的加密算法。默认不支持，可通过password_encryption_type参数配置。 - sha256：要求客户端提供一个sha256算法加密的口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sha256加密，增强了安全性。 - sm3：要求客户端提供一个sm3算法加密口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sm3加密，增加了安全性。 - cert：客户端证书认证模式，此模式需进行SSL连接配置且需要客户端提供有效的SSL证书，不需要提供用户密码。cert认证方式只支持hostssl类型的规则。  **默认取值**: 不涉及。 

        :return: The method of this HbaConfOption.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this HbaConfOption.

        **参数解释** 声明连接时使用的认证方法。 **约束限制**: 不涉及。 **取值范围** - reject：无条件地拒绝连接。常用于过滤某些主机。 - md5：MD5加密算法安全性低，存在安全风险，不推荐使用，建议使用更安全的加密算法。默认不支持，可通过password_encryption_type参数配置。 - sha256：要求客户端提供一个sha256算法加密的口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sha256加密，增强了安全性。 - sm3：要求客户端提供一个sm3算法加密口令进行认证，该口令在传送过程中结合salt（服务器发送给客户端的随机数）的单向sm3加密，增加了安全性。 - cert：客户端证书认证模式，此模式需进行SSL连接配置且需要客户端提供有效的SSL证书，不需要提供用户密码。cert认证方式只支持hostssl类型的规则。  **默认取值**: 不涉及。 

        :param method: The method of this HbaConfOption.
        :type method: str
        """
        self._method = method

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
        if not isinstance(other, HbaConfOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
