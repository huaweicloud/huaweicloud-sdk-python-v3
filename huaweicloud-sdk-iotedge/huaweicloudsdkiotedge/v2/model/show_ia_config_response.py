# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIaConfigResponse(SdkResponse):

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
        'value': 'str',
        'description': 'str',
        'version': 'int',
        'state': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'version': 'version',
        'state': 'state',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, value=None, description=None, version=None, state=None, create_time=None, update_time=None):
        """ShowIaConfigResponse

        The model defined in huaweicloud sdk

        :param id: 配置ID
        :type id: str
        :param name: 配置项名称
        :type name: str
        :param value: 配置项详情
        :type value: str
        :param description: 配置项描述
        :type description: str
        :param version: 版本号
        :type version: int
        :param state: 下发状态
        :type state: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super(ShowIaConfigResponse, self).__init__()

        self._id = None
        self._name = None
        self._value = None
        self._description = None
        self._version = None
        self._state = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if state is not None:
            self.state = state
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ShowIaConfigResponse.

        配置ID

        :return: The id of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowIaConfigResponse.

        配置ID

        :param id: The id of this ShowIaConfigResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowIaConfigResponse.

        配置项名称

        :return: The name of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowIaConfigResponse.

        配置项名称

        :param name: The name of this ShowIaConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ShowIaConfigResponse.

        配置项详情

        :return: The value of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowIaConfigResponse.

        配置项详情

        :param value: The value of this ShowIaConfigResponse.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        """Gets the description of this ShowIaConfigResponse.

        配置项描述

        :return: The description of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowIaConfigResponse.

        配置项描述

        :param description: The description of this ShowIaConfigResponse.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        """Gets the version of this ShowIaConfigResponse.

        版本号

        :return: The version of this ShowIaConfigResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowIaConfigResponse.

        版本号

        :param version: The version of this ShowIaConfigResponse.
        :type version: int
        """
        self._version = version

    @property
    def state(self):
        """Gets the state of this ShowIaConfigResponse.

        下发状态

        :return: The state of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowIaConfigResponse.

        下发状态

        :param state: The state of this ShowIaConfigResponse.
        :type state: str
        """
        self._state = state

    @property
    def create_time(self):
        """Gets the create_time of this ShowIaConfigResponse.

        创建时间

        :return: The create_time of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowIaConfigResponse.

        创建时间

        :param create_time: The create_time of this ShowIaConfigResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowIaConfigResponse.

        更新时间

        :return: The update_time of this ShowIaConfigResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowIaConfigResponse.

        更新时间

        :param update_time: The update_time of this ShowIaConfigResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowIaConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
