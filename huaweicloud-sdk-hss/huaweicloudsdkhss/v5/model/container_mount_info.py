# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerMountInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_path': 'str',
        'mount_path': 'str',
        'mount_propagation': 'str',
        'read_only': 'bool',
        'mount_name': 'str',
        'sub_path': 'str',
        'sub_path_expr': 'str'
    }

    attribute_map = {
        'host_path': 'host_path',
        'mount_path': 'mount_path',
        'mount_propagation': 'mount_propagation',
        'read_only': 'read_only',
        'mount_name': 'mount_name',
        'sub_path': 'sub_path',
        'sub_path_expr': 'sub_path_expr'
    }

    def __init__(self, host_path=None, mount_path=None, mount_propagation=None, read_only=None, mount_name=None, sub_path=None, sub_path_expr=None):
        r"""ContainerMountInfo

        The model defined in huaweicloud sdk

        :param host_path: 主机路径
        :type host_path: str
        :param mount_path: 挂载路径
        :type mount_path: str
        :param mount_propagation: 挂载传播方式
        :type mount_propagation: str
        :param read_only: 是否只读
        :type read_only: bool
        :param mount_name: 卷名称
        :type mount_name: str
        :param sub_path: 子路径
        :type sub_path: str
        :param sub_path_expr: 子路径表达式
        :type sub_path_expr: str
        """
        
        

        self._host_path = None
        self._mount_path = None
        self._mount_propagation = None
        self._read_only = None
        self._mount_name = None
        self._sub_path = None
        self._sub_path_expr = None
        self.discriminator = None

        if host_path is not None:
            self.host_path = host_path
        if mount_path is not None:
            self.mount_path = mount_path
        if mount_propagation is not None:
            self.mount_propagation = mount_propagation
        if read_only is not None:
            self.read_only = read_only
        if mount_name is not None:
            self.mount_name = mount_name
        if sub_path is not None:
            self.sub_path = sub_path
        if sub_path_expr is not None:
            self.sub_path_expr = sub_path_expr

    @property
    def host_path(self):
        r"""Gets the host_path of this ContainerMountInfo.

        主机路径

        :return: The host_path of this ContainerMountInfo.
        :rtype: str
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        r"""Sets the host_path of this ContainerMountInfo.

        主机路径

        :param host_path: The host_path of this ContainerMountInfo.
        :type host_path: str
        """
        self._host_path = host_path

    @property
    def mount_path(self):
        r"""Gets the mount_path of this ContainerMountInfo.

        挂载路径

        :return: The mount_path of this ContainerMountInfo.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this ContainerMountInfo.

        挂载路径

        :param mount_path: The mount_path of this ContainerMountInfo.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def mount_propagation(self):
        r"""Gets the mount_propagation of this ContainerMountInfo.

        挂载传播方式

        :return: The mount_propagation of this ContainerMountInfo.
        :rtype: str
        """
        return self._mount_propagation

    @mount_propagation.setter
    def mount_propagation(self, mount_propagation):
        r"""Sets the mount_propagation of this ContainerMountInfo.

        挂载传播方式

        :param mount_propagation: The mount_propagation of this ContainerMountInfo.
        :type mount_propagation: str
        """
        self._mount_propagation = mount_propagation

    @property
    def read_only(self):
        r"""Gets the read_only of this ContainerMountInfo.

        是否只读

        :return: The read_only of this ContainerMountInfo.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this ContainerMountInfo.

        是否只读

        :param read_only: The read_only of this ContainerMountInfo.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def mount_name(self):
        r"""Gets the mount_name of this ContainerMountInfo.

        卷名称

        :return: The mount_name of this ContainerMountInfo.
        :rtype: str
        """
        return self._mount_name

    @mount_name.setter
    def mount_name(self, mount_name):
        r"""Sets the mount_name of this ContainerMountInfo.

        卷名称

        :param mount_name: The mount_name of this ContainerMountInfo.
        :type mount_name: str
        """
        self._mount_name = mount_name

    @property
    def sub_path(self):
        r"""Gets the sub_path of this ContainerMountInfo.

        子路径

        :return: The sub_path of this ContainerMountInfo.
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        r"""Sets the sub_path of this ContainerMountInfo.

        子路径

        :param sub_path: The sub_path of this ContainerMountInfo.
        :type sub_path: str
        """
        self._sub_path = sub_path

    @property
    def sub_path_expr(self):
        r"""Gets the sub_path_expr of this ContainerMountInfo.

        子路径表达式

        :return: The sub_path_expr of this ContainerMountInfo.
        :rtype: str
        """
        return self._sub_path_expr

    @sub_path_expr.setter
    def sub_path_expr(self, sub_path_expr):
        r"""Sets the sub_path_expr of this ContainerMountInfo.

        子路径表达式

        :param sub_path_expr: The sub_path_expr of this ContainerMountInfo.
        :type sub_path_expr: str
        """
        self._sub_path_expr = sub_path_expr

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
        if not isinstance(other, ContainerMountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
