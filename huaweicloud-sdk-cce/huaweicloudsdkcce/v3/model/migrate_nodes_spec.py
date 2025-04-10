# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateNodesSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os': 'str',
        'extend_param': 'MigrateNodeExtendParam',
        'login': 'Login',
        'runtime': 'Runtime',
        'nodes': 'list[NodeItem]'
    }

    attribute_map = {
        'os': 'os',
        'extend_param': 'extendParam',
        'login': 'login',
        'runtime': 'runtime',
        'nodes': 'nodes'
    }

    def __init__(self, os=None, extend_param=None, login=None, runtime=None, nodes=None):
        r"""MigrateNodesSpec

        The model defined in huaweicloud sdk

        :param os: 操作系统类型，须精确到版本号。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 
        :type os: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.MigrateNodeExtendParam`
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        :param nodes: 待操作节点列表
        :type nodes: list[:class:`huaweicloudsdkcce.v3.NodeItem`]
        """
        
        

        self._os = None
        self._extend_param = None
        self._login = None
        self._runtime = None
        self._nodes = None
        self.discriminator = None

        self.os = os
        if extend_param is not None:
            self.extend_param = extend_param
        self.login = login
        if runtime is not None:
            self.runtime = runtime
        self.nodes = nodes

    @property
    def os(self):
        r"""Gets the os of this MigrateNodesSpec.

        操作系统类型，须精确到版本号。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :return: The os of this MigrateNodesSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this MigrateNodesSpec.

        操作系统类型，须精确到版本号。 当指定“alpha.cce/NodeImageID”参数时，“os”参数必须和用户自定义镜像的操作系统一致。 

        :param os: The os of this MigrateNodesSpec.
        :type os: str
        """
        self._os = os

    @property
    def extend_param(self):
        r"""Gets the extend_param of this MigrateNodesSpec.

        :return: The extend_param of this MigrateNodesSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.MigrateNodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this MigrateNodesSpec.

        :param extend_param: The extend_param of this MigrateNodesSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.MigrateNodeExtendParam`
        """
        self._extend_param = extend_param

    @property
    def login(self):
        r"""Gets the login of this MigrateNodesSpec.

        :return: The login of this MigrateNodesSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this MigrateNodesSpec.

        :param login: The login of this MigrateNodesSpec.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def runtime(self):
        r"""Gets the runtime of this MigrateNodesSpec.

        :return: The runtime of this MigrateNodesSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this MigrateNodesSpec.

        :param runtime: The runtime of this MigrateNodesSpec.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def nodes(self):
        r"""Gets the nodes of this MigrateNodesSpec.

        待操作节点列表

        :return: The nodes of this MigrateNodesSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodeItem`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this MigrateNodesSpec.

        待操作节点列表

        :param nodes: The nodes of this MigrateNodesSpec.
        :type nodes: list[:class:`huaweicloudsdkcce.v3.NodeItem`]
        """
        self._nodes = nodes

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
        if not isinstance(other, MigrateNodesSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
