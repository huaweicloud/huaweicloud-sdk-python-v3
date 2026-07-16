# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInfo:

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
        'name': 'str',
        'agent_type': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'name': 'name',
        'agent_type': 'agent_type',
        'create_time': 'create_time'
    }

    def __init__(self, agent_id=None, name=None, agent_type=None, create_time=None):
        r"""AgentInfo

        The model defined in huaweicloud sdk

        :param agent_id: 智能体id
        :type agent_id: str
        :param name: 智能体名称
        :type name: str
        :param agent_type: 智能体类型
        :type agent_type: str
        :param create_time: 创建时间
        :type create_time: int
        """
        
        

        self._agent_id = None
        self._name = None
        self._agent_type = None
        self._create_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if name is not None:
            self.name = name
        if agent_type is not None:
            self.agent_type = agent_type
        if create_time is not None:
            self.create_time = create_time

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AgentInfo.

        智能体id

        :return: The agent_id of this AgentInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AgentInfo.

        智能体id

        :param agent_id: The agent_id of this AgentInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def name(self):
        r"""Gets the name of this AgentInfo.

        智能体名称

        :return: The name of this AgentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AgentInfo.

        智能体名称

        :param name: The name of this AgentInfo.
        :type name: str
        """
        self._name = name

    @property
    def agent_type(self):
        r"""Gets the agent_type of this AgentInfo.

        智能体类型

        :return: The agent_type of this AgentInfo.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this AgentInfo.

        智能体类型

        :param agent_type: The agent_type of this AgentInfo.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def create_time(self):
        r"""Gets the create_time of this AgentInfo.

        创建时间

        :return: The create_time of this AgentInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AgentInfo.

        创建时间

        :param create_time: The create_time of this AgentInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AgentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
