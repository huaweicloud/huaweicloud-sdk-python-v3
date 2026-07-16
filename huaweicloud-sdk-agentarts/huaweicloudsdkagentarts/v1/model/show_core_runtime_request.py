# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCoreRuntimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'version': 'version'
    }

    def __init__(self, runtime_id=None, version=None):
        r"""ShowCoreRuntimeRequest

        The model defined in huaweicloud sdk

        :param runtime_id: 运行时ID，用于唯一标识一个Agent运行时实例。
        :type runtime_id: str
        :param version: **参数解释**:  版本名称，不指定则返回最新版本。 **取值范围**: 长度 1 - 24 个字符，必须以字母开头和结尾。
        :type version: str
        """
        
        

        self._runtime_id = None
        self._version = None
        self.discriminator = None

        self.runtime_id = runtime_id
        if version is not None:
            self.version = version

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this ShowCoreRuntimeRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :return: The runtime_id of this ShowCoreRuntimeRequest.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ShowCoreRuntimeRequest.

        运行时ID，用于唯一标识一个Agent运行时实例。

        :param runtime_id: The runtime_id of this ShowCoreRuntimeRequest.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def version(self):
        r"""Gets the version of this ShowCoreRuntimeRequest.

        **参数解释**:  版本名称，不指定则返回最新版本。 **取值范围**: 长度 1 - 24 个字符，必须以字母开头和结尾。

        :return: The version of this ShowCoreRuntimeRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowCoreRuntimeRequest.

        **参数解释**:  版本名称，不指定则返回最新版本。 **取值范围**: 长度 1 - 24 个字符，必须以字母开头和结尾。

        :param version: The version of this ShowCoreRuntimeRequest.
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
        if not isinstance(other, ShowCoreRuntimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
