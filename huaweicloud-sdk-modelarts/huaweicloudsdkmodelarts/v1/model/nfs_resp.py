# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NfsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nfs_server_path': 'str',
        'local_path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'nfs_server_path': 'nfs_server_path',
        'local_path': 'local_path',
        'read_only': 'read_only'
    }

    def __init__(self, nfs_server_path=None, local_path=None, read_only=None):
        r"""NfsResp

        The model defined in huaweicloud sdk

        :param nfs_server_path: **参数解释**：nfs服务端路径，如：“10.10.10.10:/example/path”。 **取值范围**：不涉及。
        :type nfs_server_path: str
        :param local_path: **参数解释**：挂载到训练容器中的路径，如：“/example/path”。 **取值范围**：不涉及。
        :type local_path: str
        :param read_only: **参数解释**：nfs挂载卷在容器中是否只读。 **取值范围**： - true：只读 - false：非只读
        :type read_only: bool
        """
        
        

        self._nfs_server_path = None
        self._local_path = None
        self._read_only = None
        self.discriminator = None

        if nfs_server_path is not None:
            self.nfs_server_path = nfs_server_path
        if local_path is not None:
            self.local_path = local_path
        if read_only is not None:
            self.read_only = read_only

    @property
    def nfs_server_path(self):
        r"""Gets the nfs_server_path of this NfsResp.

        **参数解释**：nfs服务端路径，如：“10.10.10.10:/example/path”。 **取值范围**：不涉及。

        :return: The nfs_server_path of this NfsResp.
        :rtype: str
        """
        return self._nfs_server_path

    @nfs_server_path.setter
    def nfs_server_path(self, nfs_server_path):
        r"""Sets the nfs_server_path of this NfsResp.

        **参数解释**：nfs服务端路径，如：“10.10.10.10:/example/path”。 **取值范围**：不涉及。

        :param nfs_server_path: The nfs_server_path of this NfsResp.
        :type nfs_server_path: str
        """
        self._nfs_server_path = nfs_server_path

    @property
    def local_path(self):
        r"""Gets the local_path of this NfsResp.

        **参数解释**：挂载到训练容器中的路径，如：“/example/path”。 **取值范围**：不涉及。

        :return: The local_path of this NfsResp.
        :rtype: str
        """
        return self._local_path

    @local_path.setter
    def local_path(self, local_path):
        r"""Sets the local_path of this NfsResp.

        **参数解释**：挂载到训练容器中的路径，如：“/example/path”。 **取值范围**：不涉及。

        :param local_path: The local_path of this NfsResp.
        :type local_path: str
        """
        self._local_path = local_path

    @property
    def read_only(self):
        r"""Gets the read_only of this NfsResp.

        **参数解释**：nfs挂载卷在容器中是否只读。 **取值范围**： - true：只读 - false：非只读

        :return: The read_only of this NfsResp.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this NfsResp.

        **参数解释**：nfs挂载卷在容器中是否只读。 **取值范围**： - true：只读 - false：非只读

        :param read_only: The read_only of this NfsResp.
        :type read_only: bool
        """
        self._read_only = read_only

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
        if not isinstance(other, NfsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
