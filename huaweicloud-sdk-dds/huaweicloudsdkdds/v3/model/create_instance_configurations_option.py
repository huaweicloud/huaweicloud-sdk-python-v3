# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceConfigurationsOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'configuration_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'configuration_id': 'configuration_id'
    }

    def __init__(self, type=None, configuration_id=None):
        r"""CreateInstanceConfigurationsOption

        The model defined in huaweicloud sdk

        :param type: 节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。
        :type type: str
        :param configuration_id: 参数组id。
        :type configuration_id: str
        """
        
        

        self._type = None
        self._configuration_id = None
        self.discriminator = None

        self.type = type
        self.configuration_id = configuration_id

    @property
    def type(self):
        r"""Gets the type of this CreateInstanceConfigurationsOption.

        节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。

        :return: The type of this CreateInstanceConfigurationsOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateInstanceConfigurationsOption.

        节点类型。 取值：   - 集群实例包含mongos、shard和config节点，各节点下该参数取值分别为“mongos”、“shard”和“config”。   - 副本集实例下该参数取值为“replica”。   - 单节点实例下该参数取值为“single”。

        :param type: The type of this CreateInstanceConfigurationsOption.
        :type type: str
        """
        self._type = type

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this CreateInstanceConfigurationsOption.

        参数组id。

        :return: The configuration_id of this CreateInstanceConfigurationsOption.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this CreateInstanceConfigurationsOption.

        参数组id。

        :param configuration_id: The configuration_id of this CreateInstanceConfigurationsOption.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

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
        if not isinstance(other, CreateInstanceConfigurationsOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
