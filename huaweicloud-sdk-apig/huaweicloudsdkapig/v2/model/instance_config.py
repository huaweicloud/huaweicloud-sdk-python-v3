# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'config_name': 'str',
        'config_value': 'str',
        'config_time': 'datetime',
        'remark': 'str'
    }

    attribute_map = {
        'config_id': 'config_id',
        'config_name': 'config_name',
        'config_value': 'config_value',
        'config_time': 'config_time',
        'remark': 'remark'
    }

    def __init__(self, config_id=None, config_name=None, config_value=None, config_time=None, remark=None):
        """InstanceConfig

        The model defined in huaweicloud sdk

        :param config_id: 配额编号
        :type config_id: str
        :param config_name: 配额名称
        :type config_name: str
        :param config_value: 配额值  当前实例所在租户该配额对应的数量
        :type config_value: str
        :param config_time: 配额创建时间
        :type config_time: datetime
        :param remark: 配额描述 - INSTANCE_NUM_LIMIT：租户可以创建的实例个数限制
        :type remark: str
        """
        
        

        self._config_id = None
        self._config_name = None
        self._config_value = None
        self._config_time = None
        self._remark = None
        self.discriminator = None

        if config_id is not None:
            self.config_id = config_id
        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value
        if config_time is not None:
            self.config_time = config_time
        if remark is not None:
            self.remark = remark

    @property
    def config_id(self):
        """Gets the config_id of this InstanceConfig.

        配额编号

        :return: The config_id of this InstanceConfig.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this InstanceConfig.

        配额编号

        :param config_id: The config_id of this InstanceConfig.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def config_name(self):
        """Gets the config_name of this InstanceConfig.

        配额名称

        :return: The config_name of this InstanceConfig.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this InstanceConfig.

        配额名称

        :param config_name: The config_name of this InstanceConfig.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        """Gets the config_value of this InstanceConfig.

        配额值  当前实例所在租户该配额对应的数量

        :return: The config_value of this InstanceConfig.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this InstanceConfig.

        配额值  当前实例所在租户该配额对应的数量

        :param config_value: The config_value of this InstanceConfig.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def config_time(self):
        """Gets the config_time of this InstanceConfig.

        配额创建时间

        :return: The config_time of this InstanceConfig.
        :rtype: datetime
        """
        return self._config_time

    @config_time.setter
    def config_time(self, config_time):
        """Sets the config_time of this InstanceConfig.

        配额创建时间

        :param config_time: The config_time of this InstanceConfig.
        :type config_time: datetime
        """
        self._config_time = config_time

    @property
    def remark(self):
        """Gets the remark of this InstanceConfig.

        配额描述 - INSTANCE_NUM_LIMIT：租户可以创建的实例个数限制

        :return: The remark of this InstanceConfig.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this InstanceConfig.

        配额描述 - INSTANCE_NUM_LIMIT：租户可以创建的实例个数限制

        :param remark: The remark of this InstanceConfig.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, InstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
