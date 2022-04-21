# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdDatasourceCreate:

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
        'type': 'str',
        'description': 'str',
        'url': 'str',
        'user': 'str',
        'password': 'str',
        'remotepath': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'url': 'url',
        'user': 'user',
        'password': 'password',
        'remotepath': 'remotepath'
    }

    def __init__(self, name=None, type=None, description=None, url=None, user=None, password=None, remotepath=None):
        """LdDatasourceCreate

        The model defined in huaweicloud sdk

        :param name: 数据源名称
        :type name: str
        :param type: 数据源类型： - oracle：oracle数据源类型 - mysql：mysql数据源类型 - mongodb：mongodb数据源类型 - redis：redis数据源类型 - postgresql：postgresql数据源类型 - hive：hive数据源类型 - mssql：sqlserver数据源类型 - sqlserver：sqlserver数据源类型 - gauss200：gauss200数据源类型 - dws：dws数据源类型 - gauss100：gauss100数据源类型 - zenith：zenith数据源类型
        :type type: str
        :param description: 数据源描述
        :type description: str
        :param url: 数据源连接字符串
        :type url: str
        :param user: 用户名
        :type user: str
        :param password: 密码。  敏感信息不作为响应返回
        :type password: str
        :param remotepath: ftp上传路径  预留字段，暂不支持。
        :type remotepath: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._url = None
        self._user = None
        self._password = None
        self._remotepath = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if remotepath is not None:
            self.remotepath = remotepath

    @property
    def name(self):
        """Gets the name of this LdDatasourceCreate.

        数据源名称

        :return: The name of this LdDatasourceCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LdDatasourceCreate.

        数据源名称

        :param name: The name of this LdDatasourceCreate.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this LdDatasourceCreate.

        数据源类型： - oracle：oracle数据源类型 - mysql：mysql数据源类型 - mongodb：mongodb数据源类型 - redis：redis数据源类型 - postgresql：postgresql数据源类型 - hive：hive数据源类型 - mssql：sqlserver数据源类型 - sqlserver：sqlserver数据源类型 - gauss200：gauss200数据源类型 - dws：dws数据源类型 - gauss100：gauss100数据源类型 - zenith：zenith数据源类型

        :return: The type of this LdDatasourceCreate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LdDatasourceCreate.

        数据源类型： - oracle：oracle数据源类型 - mysql：mysql数据源类型 - mongodb：mongodb数据源类型 - redis：redis数据源类型 - postgresql：postgresql数据源类型 - hive：hive数据源类型 - mssql：sqlserver数据源类型 - sqlserver：sqlserver数据源类型 - gauss200：gauss200数据源类型 - dws：dws数据源类型 - gauss100：gauss100数据源类型 - zenith：zenith数据源类型

        :param type: The type of this LdDatasourceCreate.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this LdDatasourceCreate.

        数据源描述

        :return: The description of this LdDatasourceCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LdDatasourceCreate.

        数据源描述

        :param description: The description of this LdDatasourceCreate.
        :type description: str
        """
        self._description = description

    @property
    def url(self):
        """Gets the url of this LdDatasourceCreate.

        数据源连接字符串

        :return: The url of this LdDatasourceCreate.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LdDatasourceCreate.

        数据源连接字符串

        :param url: The url of this LdDatasourceCreate.
        :type url: str
        """
        self._url = url

    @property
    def user(self):
        """Gets the user of this LdDatasourceCreate.

        用户名

        :return: The user of this LdDatasourceCreate.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LdDatasourceCreate.

        用户名

        :param user: The user of this LdDatasourceCreate.
        :type user: str
        """
        self._user = user

    @property
    def password(self):
        """Gets the password of this LdDatasourceCreate.

        密码。  敏感信息不作为响应返回

        :return: The password of this LdDatasourceCreate.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LdDatasourceCreate.

        密码。  敏感信息不作为响应返回

        :param password: The password of this LdDatasourceCreate.
        :type password: str
        """
        self._password = password

    @property
    def remotepath(self):
        """Gets the remotepath of this LdDatasourceCreate.

        ftp上传路径  预留字段，暂不支持。

        :return: The remotepath of this LdDatasourceCreate.
        :rtype: str
        """
        return self._remotepath

    @remotepath.setter
    def remotepath(self, remotepath):
        """Sets the remotepath of this LdDatasourceCreate.

        ftp上传路径  预留字段，暂不支持。

        :param remotepath: The remotepath of this LdDatasourceCreate.
        :type remotepath: str
        """
        self._remotepath = remotepath

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
        if not isinstance(other, LdDatasourceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
