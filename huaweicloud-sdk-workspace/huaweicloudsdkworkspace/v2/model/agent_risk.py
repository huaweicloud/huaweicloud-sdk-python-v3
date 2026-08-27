# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentRisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'username': 'str',
        'create_time': 'datetime',
        'type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'username': 'username',
        'create_time': 'create_time',
        'type': 'type'
    }

    def __init__(self, agent_id=None, username=None, create_time=None, type=None):
        r"""AgentRisk

        The model defined in huaweicloud sdk

        :param agent_id: Agent 实例 ID
        :type agent_id: str
        :param username: 用户名
        :type username: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param type: 风险类型
        :type type: str
        """
        
        

        self._agent_id = None
        self._username = None
        self._create_time = None
        self._type = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if username is not None:
            self.username = username
        if create_time is not None:
            self.create_time = create_time
        if type is not None:
            self.type = type

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AgentRisk.

        Agent 实例 ID

        :return: The agent_id of this AgentRisk.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AgentRisk.

        Agent 实例 ID

        :param agent_id: The agent_id of this AgentRisk.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def username(self):
        r"""Gets the username of this AgentRisk.

        用户名

        :return: The username of this AgentRisk.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this AgentRisk.

        用户名

        :param username: The username of this AgentRisk.
        :type username: str
        """
        self._username = username

    @property
    def create_time(self):
        r"""Gets the create_time of this AgentRisk.

        创建时间

        :return: The create_time of this AgentRisk.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AgentRisk.

        创建时间

        :param create_time: The create_time of this AgentRisk.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def type(self):
        r"""Gets the type of this AgentRisk.

        风险类型

        :return: The type of this AgentRisk.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AgentRisk.

        风险类型

        :param type: The type of this AgentRisk.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgentRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
