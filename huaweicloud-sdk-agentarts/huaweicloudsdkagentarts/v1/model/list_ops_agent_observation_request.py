# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsAgentObservationRequest:

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
        'page': 'int',
        'page_size': 'int',
        'agent_name': 'str',
        'agent_type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'page': 'page',
        'page_size': 'page_size',
        'agent_name': 'agent_name',
        'agent_type': 'agent_type'
    }

    def __init__(self, agent_id=None, page=None, page_size=None, agent_name=None, agent_type=None):
        r"""ListOpsAgentObservationRequest

        The model defined in huaweicloud sdk

        :param agent_id: 智能体id
        :type agent_id: str
        :param page: 查询页面，最小为1
        :type page: int
        :param page_size: 查询结果每页最多显示的条数
        :type page_size: int
        :param agent_name: 智能体名称
        :type agent_name: str
        :param agent_type: 智能体类型,agent单智能体,multiagents多智能体,workflow工作流,all全部
        :type agent_type: str
        """
        
        

        self._agent_id = None
        self._page = None
        self._page_size = None
        self._agent_name = None
        self._agent_type = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        self.page = page
        self.page_size = page_size
        if agent_name is not None:
            self.agent_name = agent_name
        if agent_type is not None:
            self.agent_type = agent_type

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListOpsAgentObservationRequest.

        智能体id

        :return: The agent_id of this ListOpsAgentObservationRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListOpsAgentObservationRequest.

        智能体id

        :param agent_id: The agent_id of this ListOpsAgentObservationRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def page(self):
        r"""Gets the page of this ListOpsAgentObservationRequest.

        查询页面，最小为1

        :return: The page of this ListOpsAgentObservationRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListOpsAgentObservationRequest.

        查询页面，最小为1

        :param page: The page of this ListOpsAgentObservationRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsAgentObservationRequest.

        查询结果每页最多显示的条数

        :return: The page_size of this ListOpsAgentObservationRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsAgentObservationRequest.

        查询结果每页最多显示的条数

        :param page_size: The page_size of this ListOpsAgentObservationRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ListOpsAgentObservationRequest.

        智能体名称

        :return: The agent_name of this ListOpsAgentObservationRequest.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ListOpsAgentObservationRequest.

        智能体名称

        :param agent_name: The agent_name of this ListOpsAgentObservationRequest.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListOpsAgentObservationRequest.

        智能体类型,agent单智能体,multiagents多智能体,workflow工作流,all全部

        :return: The agent_type of this ListOpsAgentObservationRequest.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListOpsAgentObservationRequest.

        智能体类型,agent单智能体,multiagents多智能体,workflow工作流,all全部

        :param agent_type: The agent_type of this ListOpsAgentObservationRequest.
        :type agent_type: str
        """
        self._agent_type = agent_type

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
        if not isinstance(other, ListOpsAgentObservationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
