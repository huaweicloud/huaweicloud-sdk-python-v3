# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'component_id': 'str',
        'component_version_id': 'str',
        'config': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'component_id': 'component_id',
        'component_version_id': 'component_version_id',
        'config': 'config'
    }

    def __init__(self, name=None, description=None, component_id=None, component_version_id=None, config=None):
        r"""CreateAssetsRequestBody

        The model defined in huaweicloud sdk

        :param name: 操作连接的名称
        :type name: str
        :param description: 操作连接的描述信息
        :type description: str
        :param component_id: 操作连接所属的插件id
        :type component_id: str
        :param component_version_id: 操作连接所属的插件版本id
        :type component_version_id: str
        :param config: 具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值
        :type config: str
        """
        
        

        self._name = None
        self._description = None
        self._component_id = None
        self._component_version_id = None
        self._config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.component_id = component_id
        self.component_version_id = component_version_id
        self.config = config

    @property
    def name(self):
        r"""Gets the name of this CreateAssetsRequestBody.

        操作连接的名称

        :return: The name of this CreateAssetsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAssetsRequestBody.

        操作连接的名称

        :param name: The name of this CreateAssetsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateAssetsRequestBody.

        操作连接的描述信息

        :return: The description of this CreateAssetsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAssetsRequestBody.

        操作连接的描述信息

        :param description: The description of this CreateAssetsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def component_id(self):
        r"""Gets the component_id of this CreateAssetsRequestBody.

        操作连接所属的插件id

        :return: The component_id of this CreateAssetsRequestBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CreateAssetsRequestBody.

        操作连接所属的插件id

        :param component_id: The component_id of this CreateAssetsRequestBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_version_id(self):
        r"""Gets the component_version_id of this CreateAssetsRequestBody.

        操作连接所属的插件版本id

        :return: The component_version_id of this CreateAssetsRequestBody.
        :rtype: str
        """
        return self._component_version_id

    @component_version_id.setter
    def component_version_id(self, component_version_id):
        r"""Sets the component_version_id of this CreateAssetsRequestBody.

        操作连接所属的插件版本id

        :param component_version_id: The component_version_id of this CreateAssetsRequestBody.
        :type component_version_id: str
        """
        self._component_version_id = component_version_id

    @property
    def config(self):
        r"""Gets the config of this CreateAssetsRequestBody.

        具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值

        :return: The config of this CreateAssetsRequestBody.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this CreateAssetsRequestBody.

        具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值

        :param config: The config of this CreateAssetsRequestBody.
        :type config: str
        """
        self._config = config

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
        if not isinstance(other, CreateAssetsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
