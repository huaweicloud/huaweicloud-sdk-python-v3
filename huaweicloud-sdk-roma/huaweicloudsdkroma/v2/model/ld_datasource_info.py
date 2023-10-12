# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdDatasourceInfo:

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
        'remotepath': 'str',
        'id': 'str',
        'status': 'str',
        'created_time': 'datetime',
        'modified_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'url': 'url',
        'user': 'user',
        'password': 'password',
        'remotepath': 'remotepath',
        'id': 'id',
        'status': 'status',
        'created_time': 'created_time',
        'modified_time': 'modified_time'
    }

    def __init__(self, name=None, type=None, description=None, url=None, user=None, password=None, remotepath=None, id=None, status=None, created_time=None, modified_time=None):
        """LdDatasourceInfo

        The model defined in huaweicloud sdk

        :param name: 数据源名称
        :type name: str
        :param type: 数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型
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
        :param id: 数据源ID
        :type id: str
        :param status: 数据源状态： - old：存量数据源 - new：roma数据源
        :type status: str
        :param created_time: 数据源创建时间
        :type created_time: datetime
        :param modified_time: 数据源更新时间
        :type modified_time: datetime
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._url = None
        self._user = None
        self._password = None
        self._remotepath = None
        self._id = None
        self._status = None
        self._created_time = None
        self._modified_time = None
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
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def name(self):
        """Gets the name of this LdDatasourceInfo.

        数据源名称

        :return: The name of this LdDatasourceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LdDatasourceInfo.

        数据源名称

        :param name: The name of this LdDatasourceInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this LdDatasourceInfo.

        数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型

        :return: The type of this LdDatasourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LdDatasourceInfo.

        数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型

        :param type: The type of this LdDatasourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this LdDatasourceInfo.

        数据源描述

        :return: The description of this LdDatasourceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LdDatasourceInfo.

        数据源描述

        :param description: The description of this LdDatasourceInfo.
        :type description: str
        """
        self._description = description

    @property
    def url(self):
        """Gets the url of this LdDatasourceInfo.

        数据源连接字符串

        :return: The url of this LdDatasourceInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LdDatasourceInfo.

        数据源连接字符串

        :param url: The url of this LdDatasourceInfo.
        :type url: str
        """
        self._url = url

    @property
    def user(self):
        """Gets the user of this LdDatasourceInfo.

        用户名

        :return: The user of this LdDatasourceInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LdDatasourceInfo.

        用户名

        :param user: The user of this LdDatasourceInfo.
        :type user: str
        """
        self._user = user

    @property
    def password(self):
        """Gets the password of this LdDatasourceInfo.

        密码。  敏感信息不作为响应返回

        :return: The password of this LdDatasourceInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LdDatasourceInfo.

        密码。  敏感信息不作为响应返回

        :param password: The password of this LdDatasourceInfo.
        :type password: str
        """
        self._password = password

    @property
    def remotepath(self):
        """Gets the remotepath of this LdDatasourceInfo.

        ftp上传路径  预留字段，暂不支持。

        :return: The remotepath of this LdDatasourceInfo.
        :rtype: str
        """
        return self._remotepath

    @remotepath.setter
    def remotepath(self, remotepath):
        """Sets the remotepath of this LdDatasourceInfo.

        ftp上传路径  预留字段，暂不支持。

        :param remotepath: The remotepath of this LdDatasourceInfo.
        :type remotepath: str
        """
        self._remotepath = remotepath

    @property
    def id(self):
        """Gets the id of this LdDatasourceInfo.

        数据源ID

        :return: The id of this LdDatasourceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LdDatasourceInfo.

        数据源ID

        :param id: The id of this LdDatasourceInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this LdDatasourceInfo.

        数据源状态： - old：存量数据源 - new：roma数据源

        :return: The status of this LdDatasourceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LdDatasourceInfo.

        数据源状态： - old：存量数据源 - new：roma数据源

        :param status: The status of this LdDatasourceInfo.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        """Gets the created_time of this LdDatasourceInfo.

        数据源创建时间

        :return: The created_time of this LdDatasourceInfo.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this LdDatasourceInfo.

        数据源创建时间

        :param created_time: The created_time of this LdDatasourceInfo.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this LdDatasourceInfo.

        数据源更新时间

        :return: The modified_time of this LdDatasourceInfo.
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this LdDatasourceInfo.

        数据源更新时间

        :param modified_time: The modified_time of this LdDatasourceInfo.
        :type modified_time: datetime
        """
        self._modified_time = modified_time

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
        if not isinstance(other, LdDatasourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
