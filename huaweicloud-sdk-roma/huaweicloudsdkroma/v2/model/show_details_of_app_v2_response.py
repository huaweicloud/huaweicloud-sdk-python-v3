# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'id': 'str',
        'name': 'str',
        'remark': 'str',
        'creator': 'str',
        'update_time': 'datetime',
        'app_key': 'str',
        'app_secret': 'str',
        'register_time': 'datetime',
        'status': 'int',
        'app_type': 'str',
        'roma_app_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'creator': 'creator',
        'update_time': 'update_time',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'register_time': 'register_time',
        'status': 'status',
        'app_type': 'app_type',
        'roma_app_type': 'roma_app_type'
    }

    def __init__(self, id=None, name=None, remark=None, creator=None, update_time=None, app_key=None, app_secret=None, register_time=None, status=None, app_type=None, roma_app_type=None):
        """ShowDetailsOfAppV2Response

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param name: 名称
        :type name: str
        :param remark: 描述
        :type remark: str
        :param creator: APP的创建者 - USER：用户自行创建 - MARKET：云市场分配  暂不支持MARKET
        :type creator: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param app_key: APP的key
        :type app_key: str
        :param app_secret: 密钥
        :type app_secret: str
        :param register_time: 注册时间
        :type register_time: datetime
        :param status: 状态   - 1： 有效
        :type status: int
        :param app_type: APP的类型： - apig：存量apig应用，不推荐使用 - roma：roma集成应用
        :type app_type: str
        :param roma_app_type: ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用
        :type roma_app_type: str
        """
        
        super(ShowDetailsOfAppV2Response, self).__init__()

        self._id = None
        self._name = None
        self._remark = None
        self._creator = None
        self._update_time = None
        self._app_key = None
        self._app_secret = None
        self._register_time = None
        self._status = None
        self._app_type = None
        self._roma_app_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if creator is not None:
            self.creator = creator
        if update_time is not None:
            self.update_time = update_time
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret
        if register_time is not None:
            self.register_time = register_time
        if status is not None:
            self.status = status
        if app_type is not None:
            self.app_type = app_type
        if roma_app_type is not None:
            self.roma_app_type = roma_app_type

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
        :type id: str
        """
        self._id = id

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
        :type name: str
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
        :type remark: str
        """
        self._remark = remark

    @property
    def creator(self):
        """Gets the creator of this ShowDetailsOfAppV2Response.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配  暂不支持MARKET

        :return: The creator of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowDetailsOfAppV2Response.

        APP的创建者 - USER：用户自行创建 - MARKET：云市场分配  暂不支持MARKET

        :param creator: The creator of this ShowDetailsOfAppV2Response.
        :type creator: str
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
        :type update_time: datetime
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
        :type app_key: str
        """
        self._app_key = app_key

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
        :type app_secret: str
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
        :type register_time: datetime
        """
        self._register_time = register_time

    @property
    def status(self):
        """Gets the status of this ShowDetailsOfAppV2Response.

        状态   - 1： 有效

        :return: The status of this ShowDetailsOfAppV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDetailsOfAppV2Response.

        状态   - 1： 有效

        :param status: The status of this ShowDetailsOfAppV2Response.
        :type status: int
        """
        self._status = status

    @property
    def app_type(self):
        """Gets the app_type of this ShowDetailsOfAppV2Response.

        APP的类型： - apig：存量apig应用，不推荐使用 - roma：roma集成应用

        :return: The app_type of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ShowDetailsOfAppV2Response.

        APP的类型： - apig：存量apig应用，不推荐使用 - roma：roma集成应用

        :param app_type: The app_type of this ShowDetailsOfAppV2Response.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def roma_app_type(self):
        """Gets the roma_app_type of this ShowDetailsOfAppV2Response.

        ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用

        :return: The roma_app_type of this ShowDetailsOfAppV2Response.
        :rtype: str
        """
        return self._roma_app_type

    @roma_app_type.setter
    def roma_app_type(self, roma_app_type):
        """Sets the roma_app_type of this ShowDetailsOfAppV2Response.

        ROMA_APP的类型： - subscription：订阅应用 - integration：集成应用

        :param roma_app_type: The roma_app_type of this ShowDetailsOfAppV2Response.
        :type roma_app_type: str
        """
        self._roma_app_type = roma_app_type

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
        if not isinstance(other, ShowDetailsOfAppV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
