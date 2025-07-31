# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterEventResourceResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enforcement_action': 'str',
        'group': 'str',
        'message': 'str',
        'name': 'str',
        'namespace': 'str',
        'version': 'str',
        'kind': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'enforcement_action': 'enforcement_action',
        'group': 'group',
        'message': 'message',
        'name': 'name',
        'namespace': 'namespace',
        'version': 'version',
        'kind': 'kind',
        'resource_name': 'resource_name'
    }

    def __init__(self, enforcement_action=None, group=None, message=None, name=None, namespace=None, version=None, kind=None, resource_name=None):
        r"""ClusterEventResourceResponseInfo

        The model defined in huaweicloud sdk

        :param enforcement_action: 执行动作
        :type enforcement_action: str
        :param group: Group
        :type group: str
        :param message: 信息
        :type message: str
        :param name: 名称
        :type name: str
        :param namespace: 命名空间
        :type namespace: str
        :param version: 版本
        :type version: str
        :param kind: 资源类型
        :type kind: str
        :param resource_name: 资源名称
        :type resource_name: str
        """
        
        

        self._enforcement_action = None
        self._group = None
        self._message = None
        self._name = None
        self._namespace = None
        self._version = None
        self._kind = None
        self._resource_name = None
        self.discriminator = None

        if enforcement_action is not None:
            self.enforcement_action = enforcement_action
        if group is not None:
            self.group = group
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if version is not None:
            self.version = version
        if kind is not None:
            self.kind = kind
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def enforcement_action(self):
        r"""Gets the enforcement_action of this ClusterEventResourceResponseInfo.

        执行动作

        :return: The enforcement_action of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._enforcement_action

    @enforcement_action.setter
    def enforcement_action(self, enforcement_action):
        r"""Sets the enforcement_action of this ClusterEventResourceResponseInfo.

        执行动作

        :param enforcement_action: The enforcement_action of this ClusterEventResourceResponseInfo.
        :type enforcement_action: str
        """
        self._enforcement_action = enforcement_action

    @property
    def group(self):
        r"""Gets the group of this ClusterEventResourceResponseInfo.

        Group

        :return: The group of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ClusterEventResourceResponseInfo.

        Group

        :param group: The group of this ClusterEventResourceResponseInfo.
        :type group: str
        """
        self._group = group

    @property
    def message(self):
        r"""Gets the message of this ClusterEventResourceResponseInfo.

        信息

        :return: The message of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ClusterEventResourceResponseInfo.

        信息

        :param message: The message of this ClusterEventResourceResponseInfo.
        :type message: str
        """
        self._message = message

    @property
    def name(self):
        r"""Gets the name of this ClusterEventResourceResponseInfo.

        名称

        :return: The name of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterEventResourceResponseInfo.

        名称

        :param name: The name of this ClusterEventResourceResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ClusterEventResourceResponseInfo.

        命名空间

        :return: The namespace of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ClusterEventResourceResponseInfo.

        命名空间

        :param namespace: The namespace of this ClusterEventResourceResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def version(self):
        r"""Gets the version of this ClusterEventResourceResponseInfo.

        版本

        :return: The version of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClusterEventResourceResponseInfo.

        版本

        :param version: The version of this ClusterEventResourceResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def kind(self):
        r"""Gets the kind of this ClusterEventResourceResponseInfo.

        资源类型

        :return: The kind of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ClusterEventResourceResponseInfo.

        资源类型

        :param kind: The kind of this ClusterEventResourceResponseInfo.
        :type kind: str
        """
        self._kind = kind

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ClusterEventResourceResponseInfo.

        资源名称

        :return: The resource_name of this ClusterEventResourceResponseInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ClusterEventResourceResponseInfo.

        资源名称

        :param resource_name: The resource_name of this ClusterEventResourceResponseInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ClusterEventResourceResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
