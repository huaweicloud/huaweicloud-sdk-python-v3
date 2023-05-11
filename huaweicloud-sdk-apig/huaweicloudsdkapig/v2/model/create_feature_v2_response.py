# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFeatureV2Response(SdkResponse):

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
        'enable': 'bool',
        'config': 'str',
        'instance_id': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enable': 'enable',
        'config': 'config',
        'instance_id': 'instance_id',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, enable=None, config=None, instance_id=None, update_time=None):
        """CreateFeatureV2Response

        The model defined in huaweicloud sdk

        :param id: 特性编号
        :type id: str
        :param name: 特性名称
        :type name: str
        :param enable: 是否开启特性
        :type enable: bool
        :param config: 特性参数配置
        :type config: str
        :param instance_id: 实例编号
        :type instance_id: str
        :param update_time: 实例特性更新时间
        :type update_time: datetime
        """
        
        super(CreateFeatureV2Response, self).__init__()

        self._id = None
        self._name = None
        self._enable = None
        self._config = None
        self._instance_id = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable
        if config is not None:
            self.config = config
        if instance_id is not None:
            self.instance_id = instance_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this CreateFeatureV2Response.

        特性编号

        :return: The id of this CreateFeatureV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateFeatureV2Response.

        特性编号

        :param id: The id of this CreateFeatureV2Response.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateFeatureV2Response.

        特性名称

        :return: The name of this CreateFeatureV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFeatureV2Response.

        特性名称

        :param name: The name of this CreateFeatureV2Response.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        """Gets the enable of this CreateFeatureV2Response.

        是否开启特性

        :return: The enable of this CreateFeatureV2Response.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateFeatureV2Response.

        是否开启特性

        :param enable: The enable of this CreateFeatureV2Response.
        :type enable: bool
        """
        self._enable = enable

    @property
    def config(self):
        """Gets the config of this CreateFeatureV2Response.

        特性参数配置

        :return: The config of this CreateFeatureV2Response.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateFeatureV2Response.

        特性参数配置

        :param config: The config of this CreateFeatureV2Response.
        :type config: str
        """
        self._config = config

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateFeatureV2Response.

        实例编号

        :return: The instance_id of this CreateFeatureV2Response.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateFeatureV2Response.

        实例编号

        :param instance_id: The instance_id of this CreateFeatureV2Response.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def update_time(self):
        """Gets the update_time of this CreateFeatureV2Response.

        实例特性更新时间

        :return: The update_time of this CreateFeatureV2Response.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateFeatureV2Response.

        实例特性更新时间

        :param update_time: The update_time of this CreateFeatureV2Response.
        :type update_time: datetime
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
        if not isinstance(other, CreateFeatureV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
