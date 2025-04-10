# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StagePluginsQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_condition': 'str',
        'comp_id': 'str',
        'comp_name': 'str',
        'cloud_id': 'str',
        'strategy_id': 'str',
        'category': 'str',
        'publish_tab': 'str',
        'platform': 'str',
        'comp_extend_type': 'str',
        'deploy_type': 'str'
    }

    attribute_map = {
        'use_condition': 'use_condition',
        'comp_id': 'comp_id',
        'comp_name': 'comp_name',
        'cloud_id': 'cloud_id',
        'strategy_id': 'strategy_id',
        'category': 'category',
        'publish_tab': 'publish_tab',
        'platform': 'platform',
        'comp_extend_type': 'comp_extend_type',
        'deploy_type': 'deploy_type'
    }

    def __init__(self, use_condition=None, comp_id=None, comp_name=None, cloud_id=None, strategy_id=None, category=None, publish_tab=None, platform=None, comp_extend_type=None, deploy_type=None):
        r"""StagePluginsQueryDTO

        The model defined in huaweicloud sdk

        :param use_condition: 用于区分插件为流水线可使用/模板可使用
        :type use_condition: str
        :param comp_id: 微服务ID
        :type comp_id: str
        :param comp_name: 微服务名
        :type comp_name: str
        :param cloud_id: 局点ID
        :type cloud_id: str
        :param strategy_id: 策略ID
        :type strategy_id: str
        :param category: 流水线类型
        :type category: str
        :param publish_tab: 是否发布流水线
        :type publish_tab: str
        :param platform: 部署平台
        :type platform: str
        :param comp_extend_type: 组件类型
        :type comp_extend_type: str
        :param deploy_type: 部署类型
        :type deploy_type: str
        """
        
        

        self._use_condition = None
        self._comp_id = None
        self._comp_name = None
        self._cloud_id = None
        self._strategy_id = None
        self._category = None
        self._publish_tab = None
        self._platform = None
        self._comp_extend_type = None
        self._deploy_type = None
        self.discriminator = None

        if use_condition is not None:
            self.use_condition = use_condition
        if comp_id is not None:
            self.comp_id = comp_id
        if comp_name is not None:
            self.comp_name = comp_name
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if strategy_id is not None:
            self.strategy_id = strategy_id
        if category is not None:
            self.category = category
        if publish_tab is not None:
            self.publish_tab = publish_tab
        if platform is not None:
            self.platform = platform
        if comp_extend_type is not None:
            self.comp_extend_type = comp_extend_type
        if deploy_type is not None:
            self.deploy_type = deploy_type

    @property
    def use_condition(self):
        r"""Gets the use_condition of this StagePluginsQueryDTO.

        用于区分插件为流水线可使用/模板可使用

        :return: The use_condition of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._use_condition

    @use_condition.setter
    def use_condition(self, use_condition):
        r"""Sets the use_condition of this StagePluginsQueryDTO.

        用于区分插件为流水线可使用/模板可使用

        :param use_condition: The use_condition of this StagePluginsQueryDTO.
        :type use_condition: str
        """
        self._use_condition = use_condition

    @property
    def comp_id(self):
        r"""Gets the comp_id of this StagePluginsQueryDTO.

        微服务ID

        :return: The comp_id of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._comp_id

    @comp_id.setter
    def comp_id(self, comp_id):
        r"""Sets the comp_id of this StagePluginsQueryDTO.

        微服务ID

        :param comp_id: The comp_id of this StagePluginsQueryDTO.
        :type comp_id: str
        """
        self._comp_id = comp_id

    @property
    def comp_name(self):
        r"""Gets the comp_name of this StagePluginsQueryDTO.

        微服务名

        :return: The comp_name of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._comp_name

    @comp_name.setter
    def comp_name(self, comp_name):
        r"""Sets the comp_name of this StagePluginsQueryDTO.

        微服务名

        :param comp_name: The comp_name of this StagePluginsQueryDTO.
        :type comp_name: str
        """
        self._comp_name = comp_name

    @property
    def cloud_id(self):
        r"""Gets the cloud_id of this StagePluginsQueryDTO.

        局点ID

        :return: The cloud_id of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        r"""Sets the cloud_id of this StagePluginsQueryDTO.

        局点ID

        :param cloud_id: The cloud_id of this StagePluginsQueryDTO.
        :type cloud_id: str
        """
        self._cloud_id = cloud_id

    @property
    def strategy_id(self):
        r"""Gets the strategy_id of this StagePluginsQueryDTO.

        策略ID

        :return: The strategy_id of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        r"""Sets the strategy_id of this StagePluginsQueryDTO.

        策略ID

        :param strategy_id: The strategy_id of this StagePluginsQueryDTO.
        :type strategy_id: str
        """
        self._strategy_id = strategy_id

    @property
    def category(self):
        r"""Gets the category of this StagePluginsQueryDTO.

        流水线类型

        :return: The category of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this StagePluginsQueryDTO.

        流水线类型

        :param category: The category of this StagePluginsQueryDTO.
        :type category: str
        """
        self._category = category

    @property
    def publish_tab(self):
        r"""Gets the publish_tab of this StagePluginsQueryDTO.

        是否发布流水线

        :return: The publish_tab of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._publish_tab

    @publish_tab.setter
    def publish_tab(self, publish_tab):
        r"""Sets the publish_tab of this StagePluginsQueryDTO.

        是否发布流水线

        :param publish_tab: The publish_tab of this StagePluginsQueryDTO.
        :type publish_tab: str
        """
        self._publish_tab = publish_tab

    @property
    def platform(self):
        r"""Gets the platform of this StagePluginsQueryDTO.

        部署平台

        :return: The platform of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this StagePluginsQueryDTO.

        部署平台

        :param platform: The platform of this StagePluginsQueryDTO.
        :type platform: str
        """
        self._platform = platform

    @property
    def comp_extend_type(self):
        r"""Gets the comp_extend_type of this StagePluginsQueryDTO.

        组件类型

        :return: The comp_extend_type of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._comp_extend_type

    @comp_extend_type.setter
    def comp_extend_type(self, comp_extend_type):
        r"""Sets the comp_extend_type of this StagePluginsQueryDTO.

        组件类型

        :param comp_extend_type: The comp_extend_type of this StagePluginsQueryDTO.
        :type comp_extend_type: str
        """
        self._comp_extend_type = comp_extend_type

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this StagePluginsQueryDTO.

        部署类型

        :return: The deploy_type of this StagePluginsQueryDTO.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this StagePluginsQueryDTO.

        部署类型

        :param deploy_type: The deploy_type of this StagePluginsQueryDTO.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

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
        if not isinstance(other, StagePluginsQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
