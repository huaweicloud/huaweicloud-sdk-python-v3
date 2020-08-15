# coding: utf-8

import pprint
import re

import six





class AppInfoWithBindNumResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'creator': 'str',
        'update_time': 'datetime',
        'app_key': 'str',
        'name': 'str',
        'remark': 'str',
        'id': 'str',
        'app_secret': 'str',
        'register_time': 'datetime',
        'status': 'int',
        'bind_num': 'int'
    }

    attribute_map = {
        'creator': 'creator',
        'update_time': 'update_time',
        'app_key': 'app_key',
        'name': 'name',
        'remark': 'remark',
        'id': 'id',
        'app_secret': 'app_secret',
        'register_time': 'register_time',
        'status': 'status',
        'bind_num': 'bind_num'
    }

    def __init__(self, creator=None, update_time=None, app_key=None, name=None, remark=None, id=None, app_secret=None, register_time=None, status=None, bind_num=None):
        """AppInfoWithBindNumResp - a model defined in huaweicloud sdk"""
        
        

        self._creator = None
        self._update_time = None
        self._app_key = None
        self._name = None
        self._remark = None
        self._id = None
        self._app_secret = None
        self._register_time = None
        self._status = None
        self._bind_num = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if update_time is not None:
            self.update_time = update_time
        if app_key is not None:
            self.app_key = app_key
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if id is not None:
            self.id = id
        if app_secret is not None:
            self.app_secret = app_secret
        if register_time is not None:
            self.register_time = register_time
        if status is not None:
            self.status = status
        if bind_num is not None:
            self.bind_num = bind_num

    @property
    def creator(self):
        """Gets the creator of this AppInfoWithBindNumResp.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配

        :return: The creator of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AppInfoWithBindNumResp.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配

        :param creator: The creator of this AppInfoWithBindNumResp.
        :type: str
        """
        self._creator = creator

    @property
    def update_time(self):
        """Gets the update_time of this AppInfoWithBindNumResp.

        更新时间

        :return: The update_time of this AppInfoWithBindNumResp.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppInfoWithBindNumResp.

        更新时间

        :param update_time: The update_time of this AppInfoWithBindNumResp.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def app_key(self):
        """Gets the app_key of this AppInfoWithBindNumResp.

        APP的key

        :return: The app_key of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this AppInfoWithBindNumResp.

        APP的key

        :param app_key: The app_key of this AppInfoWithBindNumResp.
        :type: str
        """
        self._app_key = app_key

    @property
    def name(self):
        """Gets the name of this AppInfoWithBindNumResp.

        名称

        :return: The name of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppInfoWithBindNumResp.

        名称

        :param name: The name of this AppInfoWithBindNumResp.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this AppInfoWithBindNumResp.

        描述

        :return: The remark of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AppInfoWithBindNumResp.

        描述

        :param remark: The remark of this AppInfoWithBindNumResp.
        :type: str
        """
        self._remark = remark

    @property
    def id(self):
        """Gets the id of this AppInfoWithBindNumResp.

        编号

        :return: The id of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppInfoWithBindNumResp.

        编号

        :param id: The id of this AppInfoWithBindNumResp.
        :type: str
        """
        self._id = id

    @property
    def app_secret(self):
        """Gets the app_secret of this AppInfoWithBindNumResp.

        密钥

        :return: The app_secret of this AppInfoWithBindNumResp.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this AppInfoWithBindNumResp.

        密钥

        :param app_secret: The app_secret of this AppInfoWithBindNumResp.
        :type: str
        """
        self._app_secret = app_secret

    @property
    def register_time(self):
        """Gets the register_time of this AppInfoWithBindNumResp.

        注册时间

        :return: The register_time of this AppInfoWithBindNumResp.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this AppInfoWithBindNumResp.

        注册时间

        :param register_time: The register_time of this AppInfoWithBindNumResp.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def status(self):
        """Gets the status of this AppInfoWithBindNumResp.

        状态

        :return: The status of this AppInfoWithBindNumResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AppInfoWithBindNumResp.

        状态

        :param status: The status of this AppInfoWithBindNumResp.
        :type: int
        """
        self._status = status

    @property
    def bind_num(self):
        """Gets the bind_num of this AppInfoWithBindNumResp.

        绑定的API数量

        :return: The bind_num of this AppInfoWithBindNumResp.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this AppInfoWithBindNumResp.

        绑定的API数量

        :param bind_num: The bind_num of this AppInfoWithBindNumResp.
        :type: int
        """
        self._bind_num = bind_num

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppInfoWithBindNumResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
