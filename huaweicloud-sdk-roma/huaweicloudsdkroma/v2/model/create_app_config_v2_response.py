# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppConfigV2Response(SdkResponse):

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
        'app_id': 'str',
        'config_type': 'str',
        'config_name': 'str',
        'config_value': 'str',
        'update_time': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'app_id',
        'config_type': 'config_type',
        'config_name': 'config_name',
        'config_value': 'config_value',
        'update_time': 'update_time',
        'description': 'description'
    }

    def __init__(self, id=None, app_id=None, config_type=None, config_name=None, config_value=None, update_time=None, description=None):
        """CreateAppConfigV2Response

        The model defined in huaweicloud sdk

        :param id: 应用配置编号
        :type id: str
        :param app_id: 应用编号
        :type app_id: str
        :param config_type: 应用配置类型
        :type config_type: str
        :param config_name: 应用配置名称
        :type config_name: str
        :param config_value: 应用配置值
        :type config_value: str
        :param update_time: 应用配置更新时间
        :type update_time: datetime
        :param description: 应用配置描述
        :type description: str
        """
        
        super(CreateAppConfigV2Response, self).__init__()

        self._id = None
        self._app_id = None
        self._config_type = None
        self._config_name = None
        self._config_value = None
        self._update_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if config_type is not None:
            self.config_type = config_type
        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this CreateAppConfigV2Response.

        应用配置编号

        :return: The id of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAppConfigV2Response.

        应用配置编号

        :param id: The id of this CreateAppConfigV2Response.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this CreateAppConfigV2Response.

        应用编号

        :return: The app_id of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateAppConfigV2Response.

        应用编号

        :param app_id: The app_id of this CreateAppConfigV2Response.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def config_type(self):
        """Gets the config_type of this CreateAppConfigV2Response.

        应用配置类型

        :return: The config_type of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this CreateAppConfigV2Response.

        应用配置类型

        :param config_type: The config_type of this CreateAppConfigV2Response.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def config_name(self):
        """Gets the config_name of this CreateAppConfigV2Response.

        应用配置名称

        :return: The config_name of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this CreateAppConfigV2Response.

        应用配置名称

        :param config_name: The config_name of this CreateAppConfigV2Response.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        """Gets the config_value of this CreateAppConfigV2Response.

        应用配置值

        :return: The config_value of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this CreateAppConfigV2Response.

        应用配置值

        :param config_value: The config_value of this CreateAppConfigV2Response.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def update_time(self):
        """Gets the update_time of this CreateAppConfigV2Response.

        应用配置更新时间

        :return: The update_time of this CreateAppConfigV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateAppConfigV2Response.

        应用配置更新时间

        :param update_time: The update_time of this CreateAppConfigV2Response.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def description(self):
        """Gets the description of this CreateAppConfigV2Response.

        应用配置描述

        :return: The description of this CreateAppConfigV2Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAppConfigV2Response.

        应用配置描述

        :param description: The description of this CreateAppConfigV2Response.
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
        if not isinstance(other, CreateAppConfigV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
