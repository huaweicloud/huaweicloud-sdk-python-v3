# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtDataSourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_source_id': 'str',
        'type': 'str',
        'data_source_name': 'str',
        'user_name': 'str',
        'user_pwd': 'str',
        'description': 'str',
        'reboot': 'bool',
        'connect_info': 'str'
    }

    attribute_map = {
        'data_source_id': 'data_source_id',
        'type': 'type',
        'data_source_name': 'data_source_name',
        'user_name': 'user_name',
        'user_pwd': 'user_pwd',
        'description': 'description',
        'reboot': 'reboot',
        'connect_info': 'connect_info'
    }

    def __init__(self, data_source_id=None, type=None, data_source_name=None, user_name=None, user_pwd=None, description=None, reboot=None, connect_info=None):
        """ExtDataSourceReq

        The model defined in huaweicloud sdk

        :param data_source_id: 数据源id
        :type data_source_id: str
        :param type: 类型
        :type type: str
        :param data_source_name: 数据源名称
        :type data_source_name: str
        :param user_name: 用户名
        :type user_name: str
        :param user_pwd: 密码
        :type user_pwd: str
        :param description: 描述
        :type description: str
        :param reboot: 重启
        :type reboot: bool
        :param connect_info: 数据库
        :type connect_info: str
        """
        
        

        self._data_source_id = None
        self._type = None
        self._data_source_name = None
        self._user_name = None
        self._user_pwd = None
        self._description = None
        self._reboot = None
        self._connect_info = None
        self.discriminator = None

        if data_source_id is not None:
            self.data_source_id = data_source_id
        self.type = type
        self.data_source_name = data_source_name
        self.user_name = user_name
        if user_pwd is not None:
            self.user_pwd = user_pwd
        if description is not None:
            self.description = description
        if reboot is not None:
            self.reboot = reboot
        if connect_info is not None:
            self.connect_info = connect_info

    @property
    def data_source_id(self):
        """Gets the data_source_id of this ExtDataSourceReq.

        数据源id

        :return: The data_source_id of this ExtDataSourceReq.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this ExtDataSourceReq.

        数据源id

        :param data_source_id: The data_source_id of this ExtDataSourceReq.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

    @property
    def type(self):
        """Gets the type of this ExtDataSourceReq.

        类型

        :return: The type of this ExtDataSourceReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExtDataSourceReq.

        类型

        :param type: The type of this ExtDataSourceReq.
        :type type: str
        """
        self._type = type

    @property
    def data_source_name(self):
        """Gets the data_source_name of this ExtDataSourceReq.

        数据源名称

        :return: The data_source_name of this ExtDataSourceReq.
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this ExtDataSourceReq.

        数据源名称

        :param data_source_name: The data_source_name of this ExtDataSourceReq.
        :type data_source_name: str
        """
        self._data_source_name = data_source_name

    @property
    def user_name(self):
        """Gets the user_name of this ExtDataSourceReq.

        用户名

        :return: The user_name of this ExtDataSourceReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ExtDataSourceReq.

        用户名

        :param user_name: The user_name of this ExtDataSourceReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_pwd(self):
        """Gets the user_pwd of this ExtDataSourceReq.

        密码

        :return: The user_pwd of this ExtDataSourceReq.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        """Sets the user_pwd of this ExtDataSourceReq.

        密码

        :param user_pwd: The user_pwd of this ExtDataSourceReq.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def description(self):
        """Gets the description of this ExtDataSourceReq.

        描述

        :return: The description of this ExtDataSourceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtDataSourceReq.

        描述

        :param description: The description of this ExtDataSourceReq.
        :type description: str
        """
        self._description = description

    @property
    def reboot(self):
        """Gets the reboot of this ExtDataSourceReq.

        重启

        :return: The reboot of this ExtDataSourceReq.
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this ExtDataSourceReq.

        重启

        :param reboot: The reboot of this ExtDataSourceReq.
        :type reboot: bool
        """
        self._reboot = reboot

    @property
    def connect_info(self):
        """Gets the connect_info of this ExtDataSourceReq.

        数据库

        :return: The connect_info of this ExtDataSourceReq.
        :rtype: str
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        """Sets the connect_info of this ExtDataSourceReq.

        数据库

        :param connect_info: The connect_info of this ExtDataSourceReq.
        :type connect_info: str
        """
        self._connect_info = connect_info

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
        if not isinstance(other, ExtDataSourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
