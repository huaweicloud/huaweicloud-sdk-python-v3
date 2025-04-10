# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataconnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_name': 'str',
        'dw_type': 'str',
        'dw_config': 'object',
        'agent_id': 'str',
        'agent_name': 'str',
        'env_type': 'int',
        'qualified_name': 'str',
        'dw_id': 'str',
        'create_user': 'str',
        'create_time': 'float',
        'dw_catagory': 'str',
        'description': 'str',
        'update_type': 'int'
    }

    attribute_map = {
        'dw_name': 'dw_name',
        'dw_type': 'dw_type',
        'dw_config': 'dw_config',
        'agent_id': 'agent_id',
        'agent_name': 'agent_name',
        'env_type': 'env_type',
        'qualified_name': 'qualified_name',
        'dw_id': 'dw_id',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'dw_catagory': 'dw_catagory',
        'description': 'description',
        'update_type': 'update_type'
    }

    def __init__(self, dw_name=None, dw_type=None, dw_config=None, agent_id=None, agent_name=None, env_type=None, qualified_name=None, dw_id=None, create_user=None, create_time=None, dw_catagory=None, description=None, update_type=None):
        r"""ShowDataconnectionResponse

        The model defined in huaweicloud sdk

        :param dw_name: 数据连接名称
        :type dw_name: str
        :param dw_type: 数据连接类型
        :type dw_type: str
        :param dw_config: 连接动态变化配置项，每种连接略有区别，建议在界面进行调试
        :type dw_config: object
        :param agent_id: 代理id
        :type agent_id: str
        :param agent_name: 代理名称
        :type agent_name: str
        :param env_type: 0：开发模式 1：生产模式。默认为0
        :type env_type: int
        :param qualified_name: 数据连接限定名称
        :type qualified_name: str
        :param dw_id: 数据连接id
        :type dw_id: str
        :param create_user: 数据连接创建者
        :type create_user: str
        :param create_time: 数据连接创建时间，时间戳
        :type create_time: float
        :param dw_catagory: 数据连接类别
        :type dw_catagory: str
        :param description: 连接描述信息
        :type description: str
        :param update_type: 0：创建 1：更新。默认为0
        :type update_type: int
        """
        
        super(ShowDataconnectionResponse, self).__init__()

        self._dw_name = None
        self._dw_type = None
        self._dw_config = None
        self._agent_id = None
        self._agent_name = None
        self._env_type = None
        self._qualified_name = None
        self._dw_id = None
        self._create_user = None
        self._create_time = None
        self._dw_catagory = None
        self._description = None
        self._update_type = None
        self.discriminator = None

        if dw_name is not None:
            self.dw_name = dw_name
        if dw_type is not None:
            self.dw_type = dw_type
        if dw_config is not None:
            self.dw_config = dw_config
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if env_type is not None:
            self.env_type = env_type
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if dw_id is not None:
            self.dw_id = dw_id
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if dw_catagory is not None:
            self.dw_catagory = dw_catagory
        if description is not None:
            self.description = description
        if update_type is not None:
            self.update_type = update_type

    @property
    def dw_name(self):
        r"""Gets the dw_name of this ShowDataconnectionResponse.

        数据连接名称

        :return: The dw_name of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this ShowDataconnectionResponse.

        数据连接名称

        :param dw_name: The dw_name of this ShowDataconnectionResponse.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def dw_type(self):
        r"""Gets the dw_type of this ShowDataconnectionResponse.

        数据连接类型

        :return: The dw_type of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this ShowDataconnectionResponse.

        数据连接类型

        :param dw_type: The dw_type of this ShowDataconnectionResponse.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def dw_config(self):
        r"""Gets the dw_config of this ShowDataconnectionResponse.

        连接动态变化配置项，每种连接略有区别，建议在界面进行调试

        :return: The dw_config of this ShowDataconnectionResponse.
        :rtype: object
        """
        return self._dw_config

    @dw_config.setter
    def dw_config(self, dw_config):
        r"""Sets the dw_config of this ShowDataconnectionResponse.

        连接动态变化配置项，每种连接略有区别，建议在界面进行调试

        :param dw_config: The dw_config of this ShowDataconnectionResponse.
        :type dw_config: object
        """
        self._dw_config = dw_config

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ShowDataconnectionResponse.

        代理id

        :return: The agent_id of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ShowDataconnectionResponse.

        代理id

        :param agent_id: The agent_id of this ShowDataconnectionResponse.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ShowDataconnectionResponse.

        代理名称

        :return: The agent_name of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ShowDataconnectionResponse.

        代理名称

        :param agent_name: The agent_name of this ShowDataconnectionResponse.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def env_type(self):
        r"""Gets the env_type of this ShowDataconnectionResponse.

        0：开发模式 1：生产模式。默认为0

        :return: The env_type of this ShowDataconnectionResponse.
        :rtype: int
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this ShowDataconnectionResponse.

        0：开发模式 1：生产模式。默认为0

        :param env_type: The env_type of this ShowDataconnectionResponse.
        :type env_type: int
        """
        self._env_type = env_type

    @property
    def qualified_name(self):
        r"""Gets the qualified_name of this ShowDataconnectionResponse.

        数据连接限定名称

        :return: The qualified_name of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        r"""Sets the qualified_name of this ShowDataconnectionResponse.

        数据连接限定名称

        :param qualified_name: The qualified_name of this ShowDataconnectionResponse.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def dw_id(self):
        r"""Gets the dw_id of this ShowDataconnectionResponse.

        数据连接id

        :return: The dw_id of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this ShowDataconnectionResponse.

        数据连接id

        :param dw_id: The dw_id of this ShowDataconnectionResponse.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowDataconnectionResponse.

        数据连接创建者

        :return: The create_user of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowDataconnectionResponse.

        数据连接创建者

        :param create_user: The create_user of this ShowDataconnectionResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDataconnectionResponse.

        数据连接创建时间，时间戳

        :return: The create_time of this ShowDataconnectionResponse.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDataconnectionResponse.

        数据连接创建时间，时间戳

        :param create_time: The create_time of this ShowDataconnectionResponse.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def dw_catagory(self):
        r"""Gets the dw_catagory of this ShowDataconnectionResponse.

        数据连接类别

        :return: The dw_catagory of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._dw_catagory

    @dw_catagory.setter
    def dw_catagory(self, dw_catagory):
        r"""Sets the dw_catagory of this ShowDataconnectionResponse.

        数据连接类别

        :param dw_catagory: The dw_catagory of this ShowDataconnectionResponse.
        :type dw_catagory: str
        """
        self._dw_catagory = dw_catagory

    @property
    def description(self):
        r"""Gets the description of this ShowDataconnectionResponse.

        连接描述信息

        :return: The description of this ShowDataconnectionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDataconnectionResponse.

        连接描述信息

        :param description: The description of this ShowDataconnectionResponse.
        :type description: str
        """
        self._description = description

    @property
    def update_type(self):
        r"""Gets the update_type of this ShowDataconnectionResponse.

        0：创建 1：更新。默认为0

        :return: The update_type of this ShowDataconnectionResponse.
        :rtype: int
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this ShowDataconnectionResponse.

        0：创建 1：更新。默认为0

        :param update_type: The update_type of this ShowDataconnectionResponse.
        :type update_type: int
        """
        self._update_type = update_type

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
        if not isinstance(other, ShowDataconnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
