# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInfoParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'ecs_id_list': 'list[str]',
        'agent_id_list': 'list[str]',
        'coc_cmdb_id_list': 'list[str]'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'ecs_id_list': 'ecs_id_list',
        'agent_id_list': 'agent_id_list',
        'coc_cmdb_id_list': 'coc_cmdb_id_list'
    }

    def __init__(self, page=None, page_size=None, ecs_id_list=None, agent_id_list=None, coc_cmdb_id_list=None):
        r"""AgentInfoParam

        The model defined in huaweicloud sdk

        :param page: 分页查询的起始页数（第几页）。默认值：1。
        :type page: int
        :param page_size: 每页查询数量，默认20。
        :type page_size: int
        :param ecs_id_list: ecs ID列表信息。
        :type ecs_id_list: list[str]
        :param agent_id_list: agent ID列表信息。
        :type agent_id_list: list[str]
        :param coc_cmdb_id_list: cmdb  ID列表信息。
        :type coc_cmdb_id_list: list[str]
        """
        
        

        self._page = None
        self._page_size = None
        self._ecs_id_list = None
        self._agent_id_list = None
        self._coc_cmdb_id_list = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if ecs_id_list is not None:
            self.ecs_id_list = ecs_id_list
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if coc_cmdb_id_list is not None:
            self.coc_cmdb_id_list = coc_cmdb_id_list

    @property
    def page(self):
        r"""Gets the page of this AgentInfoParam.

        分页查询的起始页数（第几页）。默认值：1。

        :return: The page of this AgentInfoParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this AgentInfoParam.

        分页查询的起始页数（第几页）。默认值：1。

        :param page: The page of this AgentInfoParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this AgentInfoParam.

        每页查询数量，默认20。

        :return: The page_size of this AgentInfoParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this AgentInfoParam.

        每页查询数量，默认20。

        :param page_size: The page_size of this AgentInfoParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def ecs_id_list(self):
        r"""Gets the ecs_id_list of this AgentInfoParam.

        ecs ID列表信息。

        :return: The ecs_id_list of this AgentInfoParam.
        :rtype: list[str]
        """
        return self._ecs_id_list

    @ecs_id_list.setter
    def ecs_id_list(self, ecs_id_list):
        r"""Sets the ecs_id_list of this AgentInfoParam.

        ecs ID列表信息。

        :param ecs_id_list: The ecs_id_list of this AgentInfoParam.
        :type ecs_id_list: list[str]
        """
        self._ecs_id_list = ecs_id_list

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this AgentInfoParam.

        agent ID列表信息。

        :return: The agent_id_list of this AgentInfoParam.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this AgentInfoParam.

        agent ID列表信息。

        :param agent_id_list: The agent_id_list of this AgentInfoParam.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def coc_cmdb_id_list(self):
        r"""Gets the coc_cmdb_id_list of this AgentInfoParam.

        cmdb  ID列表信息。

        :return: The coc_cmdb_id_list of this AgentInfoParam.
        :rtype: list[str]
        """
        return self._coc_cmdb_id_list

    @coc_cmdb_id_list.setter
    def coc_cmdb_id_list(self, coc_cmdb_id_list):
        r"""Sets the coc_cmdb_id_list of this AgentInfoParam.

        cmdb  ID列表信息。

        :param coc_cmdb_id_list: The coc_cmdb_id_list of this AgentInfoParam.
        :type coc_cmdb_id_list: list[str]
        """
        self._coc_cmdb_id_list = coc_cmdb_id_list

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
        if not isinstance(other, AgentInfoParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
