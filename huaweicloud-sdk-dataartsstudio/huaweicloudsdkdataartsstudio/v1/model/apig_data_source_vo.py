# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigDataSourceVo:

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
        'support_service': 'int',
        'dw_category': 'str',
        'description': 'str'
    }

    attribute_map = {
        'dw_name': 'dw_name',
        'dw_type': 'dw_type',
        'dw_config': 'dw_config',
        'agent_id': 'agent_id',
        'agent_name': 'agent_name',
        'env_type': 'env_type',
        'support_service': 'supportService',
        'dw_category': 'dw_category',
        'description': 'description'
    }

    def __init__(self, dw_name=None, dw_type=None, dw_config=None, agent_id=None, agent_name=None, env_type=None, support_service=None, dw_category=None, description=None):
        r"""ApigDataSourceVo

        The model defined in huaweicloud sdk

        :param dw_name: 数据连接名称
        :type dw_name: str
        :param dw_type: 数据连接类型
        :type dw_type: str
        :param dw_config: 连接动态变化配置项，每种连接略有区别，建议在界面进行调试
        :type dw_config: object
        :param agent_id: 代理id（若使用代理连接则必填）
        :type agent_id: str
        :param agent_name: 代理名称id（若使用代理连接则必填）
        :type agent_name: str
        :param env_type: 0：开发模式 1：生产模式。默认为0
        :type env_type: int
        :param support_service: 1：cdm 2：数据架构 4:数据开发 8：数据质量 16：数据目录 32：数据安全 64：数据服务
        :type support_service: int
        :param dw_category: 标签信息
        :type dw_category: str
        :param description: 连接描述信息
        :type description: str
        """
        
        

        self._dw_name = None
        self._dw_type = None
        self._dw_config = None
        self._agent_id = None
        self._agent_name = None
        self._env_type = None
        self._support_service = None
        self._dw_category = None
        self._description = None
        self.discriminator = None

        self.dw_name = dw_name
        self.dw_type = dw_type
        self.dw_config = dw_config
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if env_type is not None:
            self.env_type = env_type
        if support_service is not None:
            self.support_service = support_service
        if dw_category is not None:
            self.dw_category = dw_category
        if description is not None:
            self.description = description

    @property
    def dw_name(self):
        r"""Gets the dw_name of this ApigDataSourceVo.

        数据连接名称

        :return: The dw_name of this ApigDataSourceVo.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this ApigDataSourceVo.

        数据连接名称

        :param dw_name: The dw_name of this ApigDataSourceVo.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def dw_type(self):
        r"""Gets the dw_type of this ApigDataSourceVo.

        数据连接类型

        :return: The dw_type of this ApigDataSourceVo.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this ApigDataSourceVo.

        数据连接类型

        :param dw_type: The dw_type of this ApigDataSourceVo.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def dw_config(self):
        r"""Gets the dw_config of this ApigDataSourceVo.

        连接动态变化配置项，每种连接略有区别，建议在界面进行调试

        :return: The dw_config of this ApigDataSourceVo.
        :rtype: object
        """
        return self._dw_config

    @dw_config.setter
    def dw_config(self, dw_config):
        r"""Sets the dw_config of this ApigDataSourceVo.

        连接动态变化配置项，每种连接略有区别，建议在界面进行调试

        :param dw_config: The dw_config of this ApigDataSourceVo.
        :type dw_config: object
        """
        self._dw_config = dw_config

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ApigDataSourceVo.

        代理id（若使用代理连接则必填）

        :return: The agent_id of this ApigDataSourceVo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ApigDataSourceVo.

        代理id（若使用代理连接则必填）

        :param agent_id: The agent_id of this ApigDataSourceVo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ApigDataSourceVo.

        代理名称id（若使用代理连接则必填）

        :return: The agent_name of this ApigDataSourceVo.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ApigDataSourceVo.

        代理名称id（若使用代理连接则必填）

        :param agent_name: The agent_name of this ApigDataSourceVo.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def env_type(self):
        r"""Gets the env_type of this ApigDataSourceVo.

        0：开发模式 1：生产模式。默认为0

        :return: The env_type of this ApigDataSourceVo.
        :rtype: int
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this ApigDataSourceVo.

        0：开发模式 1：生产模式。默认为0

        :param env_type: The env_type of this ApigDataSourceVo.
        :type env_type: int
        """
        self._env_type = env_type

    @property
    def support_service(self):
        r"""Gets the support_service of this ApigDataSourceVo.

        1：cdm 2：数据架构 4:数据开发 8：数据质量 16：数据目录 32：数据安全 64：数据服务

        :return: The support_service of this ApigDataSourceVo.
        :rtype: int
        """
        return self._support_service

    @support_service.setter
    def support_service(self, support_service):
        r"""Sets the support_service of this ApigDataSourceVo.

        1：cdm 2：数据架构 4:数据开发 8：数据质量 16：数据目录 32：数据安全 64：数据服务

        :param support_service: The support_service of this ApigDataSourceVo.
        :type support_service: int
        """
        self._support_service = support_service

    @property
    def dw_category(self):
        r"""Gets the dw_category of this ApigDataSourceVo.

        标签信息

        :return: The dw_category of this ApigDataSourceVo.
        :rtype: str
        """
        return self._dw_category

    @dw_category.setter
    def dw_category(self, dw_category):
        r"""Sets the dw_category of this ApigDataSourceVo.

        标签信息

        :param dw_category: The dw_category of this ApigDataSourceVo.
        :type dw_category: str
        """
        self._dw_category = dw_category

    @property
    def description(self):
        r"""Gets the description of this ApigDataSourceVo.

        连接描述信息

        :return: The description of this ApigDataSourceVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApigDataSourceVo.

        连接描述信息

        :param description: The description of this ApigDataSourceVo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ApigDataSourceVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
