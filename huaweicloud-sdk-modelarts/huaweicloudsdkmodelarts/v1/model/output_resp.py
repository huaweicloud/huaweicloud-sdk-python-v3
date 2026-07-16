# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputResp:

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
        'local_dir': 'str',
        'access_method': 'str',
        'remote': 'RemoteResp'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'local_dir': 'local_dir',
        'access_method': 'access_method',
        'remote': 'remote'
    }

    def __init__(self, name=None, description=None, local_dir=None, access_method=None, remote=None):
        r"""OutputResp

        The model defined in huaweicloud sdk

        :param name: **参数解释**：数据输出通道名称。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：数据输出通道描述信息。 **取值范围**：不涉及。
        :type description: str
        :param local_dir: **参数解释**：数据输出通道映射的容器本地路径。 **取值范围**：不涉及。
        :type local_dir: str
        :param access_method: **参数解释**：数据输入通道路径（local_dir）的下发方式。 **取值范围**： - parameter：超参形式 - env：环境变量形式
        :type access_method: str
        :param remote: 
        :type remote: :class:`huaweicloudsdkmodelarts.v1.RemoteResp`
        """
        
        

        self._name = None
        self._description = None
        self._local_dir = None
        self._access_method = None
        self._remote = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if local_dir is not None:
            self.local_dir = local_dir
        if access_method is not None:
            self.access_method = access_method
        self.remote = remote

    @property
    def name(self):
        r"""Gets the name of this OutputResp.

        **参数解释**：数据输出通道名称。 **取值范围**：不涉及。

        :return: The name of this OutputResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OutputResp.

        **参数解释**：数据输出通道名称。 **取值范围**：不涉及。

        :param name: The name of this OutputResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OutputResp.

        **参数解释**：数据输出通道描述信息。 **取值范围**：不涉及。

        :return: The description of this OutputResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OutputResp.

        **参数解释**：数据输出通道描述信息。 **取值范围**：不涉及。

        :param description: The description of this OutputResp.
        :type description: str
        """
        self._description = description

    @property
    def local_dir(self):
        r"""Gets the local_dir of this OutputResp.

        **参数解释**：数据输出通道映射的容器本地路径。 **取值范围**：不涉及。

        :return: The local_dir of this OutputResp.
        :rtype: str
        """
        return self._local_dir

    @local_dir.setter
    def local_dir(self, local_dir):
        r"""Sets the local_dir of this OutputResp.

        **参数解释**：数据输出通道映射的容器本地路径。 **取值范围**：不涉及。

        :param local_dir: The local_dir of this OutputResp.
        :type local_dir: str
        """
        self._local_dir = local_dir

    @property
    def access_method(self):
        r"""Gets the access_method of this OutputResp.

        **参数解释**：数据输入通道路径（local_dir）的下发方式。 **取值范围**： - parameter：超参形式 - env：环境变量形式

        :return: The access_method of this OutputResp.
        :rtype: str
        """
        return self._access_method

    @access_method.setter
    def access_method(self, access_method):
        r"""Sets the access_method of this OutputResp.

        **参数解释**：数据输入通道路径（local_dir）的下发方式。 **取值范围**： - parameter：超参形式 - env：环境变量形式

        :param access_method: The access_method of this OutputResp.
        :type access_method: str
        """
        self._access_method = access_method

    @property
    def remote(self):
        r"""Gets the remote of this OutputResp.

        :return: The remote of this OutputResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RemoteResp`
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        r"""Sets the remote of this OutputResp.

        :param remote: The remote of this OutputResp.
        :type remote: :class:`huaweicloudsdkmodelarts.v1.RemoteResp`
        """
        self._remote = remote

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
        if not isinstance(other, OutputResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
