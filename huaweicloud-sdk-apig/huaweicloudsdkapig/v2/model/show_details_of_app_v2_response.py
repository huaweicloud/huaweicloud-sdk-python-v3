# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowDetailsOfAppV2Response(SdkResponse):


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
        'app_type': 'str'
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
        'app_type': 'app_type'
    }

    def __init__(self, creator=None, update_time=None, app_key=None, name=None, remark=None, id=None, app_secret=None, register_time=None, status=None, app_type=None):
        """ShowDetailsOfAppV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._creator = None
        self._update_time = None
        self._app_key = None
        self._name = None
        self._remark = None
        self._id = None
        self._app_secret = None
        self._register_time = None
        self._status = None
        self._app_type = None
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
        if app_type is not None:
            self.app_type = app_type

    @property
    def creator(self):
        """Gets the creator of this ShowDetailsOfAppV2Response.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配

        :return: The creator of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowDetailsOfAppV2Response.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配

        :param creator: The creator of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._creator = creator

    @property
    def update_time(self):
        """Gets the update_time of this ShowDetailsOfAppV2Response.

        更新时间

        :return: The update_time of this ShowDetailsOfAppV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowDetailsOfAppV2Response.

        更新时间

        :param update_time: The update_time of this ShowDetailsOfAppV2Response.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def app_key(self):
        """Gets the app_key of this ShowDetailsOfAppV2Response.

        APP的key

        :return: The app_key of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ShowDetailsOfAppV2Response.

        APP的key

        :param app_key: The app_key of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._app_key = app_key

    @property
    def name(self):
        """Gets the name of this ShowDetailsOfAppV2Response.

        名称

        :return: The name of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDetailsOfAppV2Response.

        名称

        :param name: The name of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this ShowDetailsOfAppV2Response.

        描述

        :return: The remark of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ShowDetailsOfAppV2Response.

        描述

        :param remark: The remark of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._remark = remark

    @property
    def id(self):
        """Gets the id of this ShowDetailsOfAppV2Response.

        编号

        :return: The id of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailsOfAppV2Response.

        编号

        :param id: The id of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._id = id

    @property
    def app_secret(self):
        """Gets the app_secret of this ShowDetailsOfAppV2Response.

        密钥

        :return: The app_secret of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this ShowDetailsOfAppV2Response.

        密钥

        :param app_secret: The app_secret of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._app_secret = app_secret

    @property
    def register_time(self):
        """Gets the register_time of this ShowDetailsOfAppV2Response.

        注册时间

        :return: The register_time of this ShowDetailsOfAppV2Response.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this ShowDetailsOfAppV2Response.

        注册时间

        :param register_time: The register_time of this ShowDetailsOfAppV2Response.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def status(self):
        """Gets the status of this ShowDetailsOfAppV2Response.

        状态

        :return: The status of this ShowDetailsOfAppV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDetailsOfAppV2Response.

        状态

        :param status: The status of this ShowDetailsOfAppV2Response.
        :type: int
        """
        self._status = status

    @property
    def app_type(self):
        """Gets the app_type of this ShowDetailsOfAppV2Response.

        APP的类型  默认为apig，暂不支持其他类型

        :return: The app_type of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ShowDetailsOfAppV2Response.

        APP的类型  默认为apig，暂不支持其他类型

        :param app_type: The app_type of this ShowDetailsOfAppV2Response.
        :type: str
        """
        self._app_type = app_type

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
        if not isinstance(other, ShowDetailsOfAppV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
