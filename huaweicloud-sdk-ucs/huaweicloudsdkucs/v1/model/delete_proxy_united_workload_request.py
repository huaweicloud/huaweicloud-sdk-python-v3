# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteProxyUnitedWorkloadRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clustergroupid': 'str',
        'kind': 'str',
        'namespace': 'str',
        'name': 'str'
    }

    attribute_map = {
        'clustergroupid': 'clustergroupid',
        'kind': 'kind',
        'namespace': 'namespace',
        'name': 'name'
    }

    def __init__(self, clustergroupid=None, kind=None, namespace=None, name=None):
        r"""DeleteProxyUnitedWorkloadRequest

        The model defined in huaweicloud sdk

        :param clustergroupid: 容器舰队id
        :type clustergroupid: str
        :param kind: 工作负载的类型
        :type kind: str
        :param namespace: 命名空间
        :type namespace: str
        :param name: 工作负载的名称
        :type name: str
        """
        
        

        self._clustergroupid = None
        self._kind = None
        self._namespace = None
        self._name = None
        self.discriminator = None

        self.clustergroupid = clustergroupid
        self.kind = kind
        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name

    @property
    def clustergroupid(self):
        r"""Gets the clustergroupid of this DeleteProxyUnitedWorkloadRequest.

        容器舰队id

        :return: The clustergroupid of this DeleteProxyUnitedWorkloadRequest.
        :rtype: str
        """
        return self._clustergroupid

    @clustergroupid.setter
    def clustergroupid(self, clustergroupid):
        r"""Sets the clustergroupid of this DeleteProxyUnitedWorkloadRequest.

        容器舰队id

        :param clustergroupid: The clustergroupid of this DeleteProxyUnitedWorkloadRequest.
        :type clustergroupid: str
        """
        self._clustergroupid = clustergroupid

    @property
    def kind(self):
        r"""Gets the kind of this DeleteProxyUnitedWorkloadRequest.

        工作负载的类型

        :return: The kind of this DeleteProxyUnitedWorkloadRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this DeleteProxyUnitedWorkloadRequest.

        工作负载的类型

        :param kind: The kind of this DeleteProxyUnitedWorkloadRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def namespace(self):
        r"""Gets the namespace of this DeleteProxyUnitedWorkloadRequest.

        命名空间

        :return: The namespace of this DeleteProxyUnitedWorkloadRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this DeleteProxyUnitedWorkloadRequest.

        命名空间

        :param namespace: The namespace of this DeleteProxyUnitedWorkloadRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this DeleteProxyUnitedWorkloadRequest.

        工作负载的名称

        :return: The name of this DeleteProxyUnitedWorkloadRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteProxyUnitedWorkloadRequest.

        工作负载的名称

        :param name: The name of this DeleteProxyUnitedWorkloadRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, DeleteProxyUnitedWorkloadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
