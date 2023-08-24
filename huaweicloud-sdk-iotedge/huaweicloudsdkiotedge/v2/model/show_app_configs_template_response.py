# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppConfigsTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'name': 'str',
        'description': 'str',
        'config_tabs': 'object',
        'default_values': 'object',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'name': 'name',
        'description': 'description',
        'config_tabs': 'config_tabs',
        'default_values': 'default_values',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, tpl_id=None, name=None, description=None, config_tabs=None, default_values=None, create_time=None, update_time=None):
        """ShowAppConfigsTemplateResponse

        The model defined in huaweicloud sdk

        :param tpl_id: 模板id
        :type tpl_id: str
        :param name: 模板名称
        :type name: str
        :param description: 描述
        :type description: str
        :param config_tabs: 配置项数据
        :type config_tabs: object
        :param default_values: 默认数据
        :type default_values: object
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        super(ShowAppConfigsTemplateResponse, self).__init__()

        self._tpl_id = None
        self._name = None
        self._description = None
        self._config_tabs = None
        self._default_values = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if config_tabs is not None:
            self.config_tabs = config_tabs
        if default_values is not None:
            self.default_values = default_values
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def tpl_id(self):
        """Gets the tpl_id of this ShowAppConfigsTemplateResponse.

        模板id

        :return: The tpl_id of this ShowAppConfigsTemplateResponse.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this ShowAppConfigsTemplateResponse.

        模板id

        :param tpl_id: The tpl_id of this ShowAppConfigsTemplateResponse.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def name(self):
        """Gets the name of this ShowAppConfigsTemplateResponse.

        模板名称

        :return: The name of this ShowAppConfigsTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAppConfigsTemplateResponse.

        模板名称

        :param name: The name of this ShowAppConfigsTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowAppConfigsTemplateResponse.

        描述

        :return: The description of this ShowAppConfigsTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAppConfigsTemplateResponse.

        描述

        :param description: The description of this ShowAppConfigsTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def config_tabs(self):
        """Gets the config_tabs of this ShowAppConfigsTemplateResponse.

        配置项数据

        :return: The config_tabs of this ShowAppConfigsTemplateResponse.
        :rtype: object
        """
        return self._config_tabs

    @config_tabs.setter
    def config_tabs(self, config_tabs):
        """Sets the config_tabs of this ShowAppConfigsTemplateResponse.

        配置项数据

        :param config_tabs: The config_tabs of this ShowAppConfigsTemplateResponse.
        :type config_tabs: object
        """
        self._config_tabs = config_tabs

    @property
    def default_values(self):
        """Gets the default_values of this ShowAppConfigsTemplateResponse.

        默认数据

        :return: The default_values of this ShowAppConfigsTemplateResponse.
        :rtype: object
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this ShowAppConfigsTemplateResponse.

        默认数据

        :param default_values: The default_values of this ShowAppConfigsTemplateResponse.
        :type default_values: object
        """
        self._default_values = default_values

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppConfigsTemplateResponse.

        创建时间

        :return: The create_time of this ShowAppConfigsTemplateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppConfigsTemplateResponse.

        创建时间

        :param create_time: The create_time of this ShowAppConfigsTemplateResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowAppConfigsTemplateResponse.

        最后一次修改时间

        :return: The update_time of this ShowAppConfigsTemplateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAppConfigsTemplateResponse.

        最后一次修改时间

        :param update_time: The update_time of this ShowAppConfigsTemplateResponse.
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
        if not isinstance(other, ShowAppConfigsTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
