# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigurationParamVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_id': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'node_id': 'str',
        'param': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'node_id': 'node_id',
        'param': 'param',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, configuration_id=None, file_name=None, file_type=None, node_id=None, param=None, type=None, version=None):
        r"""ComponentConfigurationParamVo

        The model defined in huaweicloud sdk

        :param configuration_id: id
        :type configuration_id: str
        :param file_name: 文件名
        :type file_name: str
        :param file_type: 文件类型
        :type file_type: str
        :param node_id: 节点id
        :type node_id: str
        :param param: 参数
        :type param: str
        :param type: 类型
        :type type: str
        :param version: 版本
        :type version: str
        """
        
        

        self._configuration_id = None
        self._file_name = None
        self._file_type = None
        self._node_id = None
        self._param = None
        self._type = None
        self._version = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if node_id is not None:
            self.node_id = node_id
        if param is not None:
            self.param = param
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this ComponentConfigurationParamVo.

        id

        :return: The configuration_id of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this ComponentConfigurationParamVo.

        id

        :param configuration_id: The configuration_id of this ComponentConfigurationParamVo.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ComponentConfigurationParamVo.

        文件名

        :return: The file_name of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ComponentConfigurationParamVo.

        文件名

        :param file_name: The file_name of this ComponentConfigurationParamVo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this ComponentConfigurationParamVo.

        文件类型

        :return: The file_type of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ComponentConfigurationParamVo.

        文件类型

        :param file_type: The file_type of this ComponentConfigurationParamVo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ComponentConfigurationParamVo.

        节点id

        :return: The node_id of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ComponentConfigurationParamVo.

        节点id

        :param node_id: The node_id of this ComponentConfigurationParamVo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def param(self):
        r"""Gets the param of this ComponentConfigurationParamVo.

        参数

        :return: The param of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this ComponentConfigurationParamVo.

        参数

        :param param: The param of this ComponentConfigurationParamVo.
        :type param: str
        """
        self._param = param

    @property
    def type(self):
        r"""Gets the type of this ComponentConfigurationParamVo.

        类型

        :return: The type of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ComponentConfigurationParamVo.

        类型

        :param type: The type of this ComponentConfigurationParamVo.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ComponentConfigurationParamVo.

        版本

        :return: The version of this ComponentConfigurationParamVo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentConfigurationParamVo.

        版本

        :param version: The version of this ComponentConfigurationParamVo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ComponentConfigurationParamVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
