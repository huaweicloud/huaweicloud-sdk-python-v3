# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'str',
        'config_value': 'str',
        'engine_type': 'str'
    }

    attribute_map = {
        'config_type': 'config_type',
        'config_value': 'config_value',
        'engine_type': 'engine_type'
    }

    def __init__(self, config_type=None, config_value=None, engine_type=None):
        r"""UpdateInstanceConfigRequestBody

        The model defined in huaweicloud sdk

        :param config_type: 配置类型。取值范围：metaLockWaitThreshold, innodbLockWaitThreshold
        :type config_type: str
        :param config_value: 配置的数值
        :type config_value: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        """
        
        

        self._config_type = None
        self._config_value = None
        self._engine_type = None
        self.discriminator = None

        self.config_type = config_type
        self.config_value = config_value
        self.engine_type = engine_type

    @property
    def config_type(self):
        r"""Gets the config_type of this UpdateInstanceConfigRequestBody.

        配置类型。取值范围：metaLockWaitThreshold, innodbLockWaitThreshold

        :return: The config_type of this UpdateInstanceConfigRequestBody.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this UpdateInstanceConfigRequestBody.

        配置类型。取值范围：metaLockWaitThreshold, innodbLockWaitThreshold

        :param config_type: The config_type of this UpdateInstanceConfigRequestBody.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def config_value(self):
        r"""Gets the config_value of this UpdateInstanceConfigRequestBody.

        配置的数值

        :return: The config_value of this UpdateInstanceConfigRequestBody.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this UpdateInstanceConfigRequestBody.

        配置的数值

        :param config_value: The config_value of this UpdateInstanceConfigRequestBody.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def engine_type(self):
        r"""Gets the engine_type of this UpdateInstanceConfigRequestBody.

        数据库引擎类型

        :return: The engine_type of this UpdateInstanceConfigRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this UpdateInstanceConfigRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this UpdateInstanceConfigRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

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
        if not isinstance(other, UpdateInstanceConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
