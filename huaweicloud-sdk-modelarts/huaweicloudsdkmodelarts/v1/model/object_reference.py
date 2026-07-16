# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'namespace': 'str',
        'name': 'str',
        'uid': 'str',
        'resource_version': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'namespace': 'namespace',
        'name': 'name',
        'uid': 'uid',
        'resource_version': 'resourceVersion'
    }

    def __init__(self, kind=None, api_version=None, namespace=None, name=None, uid=None, resource_version=None):
        r"""ObjectReference

        The model defined in huaweicloud sdk

        :param kind: **参数解释**： 资源对象的API类型，例如，DaemonSet、Deployment 等。 **取值范围**： 不涉及。
        :type kind: str
        :param api_version: **参数解释**： 资源对象的API版本。 **取值范围**： 不涉及。
        :type api_version: str
        :param namespace: **参数解释**： 资源对象的命名空间。 **取值范围**： 不涉及。
        :type namespace: str
        :param name: **参数解释**： 资源对象的名称。 **取值范围**： 不涉及。
        :type name: str
        :param uid: **参数解释**： 资源对象的唯一标识符（UID）。 **取值范围**： 不涉及。
        :type uid: str
        :param resource_version: **参数解释**： 资源对象的当前版本。 **取值范围**： 不涉及。
        :type resource_version: str
        """
        
        

        self._kind = None
        self._api_version = None
        self._namespace = None
        self._name = None
        self._uid = None
        self._resource_version = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if resource_version is not None:
            self.resource_version = resource_version

    @property
    def kind(self):
        r"""Gets the kind of this ObjectReference.

        **参数解释**： 资源对象的API类型，例如，DaemonSet、Deployment 等。 **取值范围**： 不涉及。

        :return: The kind of this ObjectReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ObjectReference.

        **参数解释**： 资源对象的API类型，例如，DaemonSet、Deployment 等。 **取值范围**： 不涉及。

        :param kind: The kind of this ObjectReference.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this ObjectReference.

        **参数解释**： 资源对象的API版本。 **取值范围**： 不涉及。

        :return: The api_version of this ObjectReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ObjectReference.

        **参数解释**： 资源对象的API版本。 **取值范围**： 不涉及。

        :param api_version: The api_version of this ObjectReference.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def namespace(self):
        r"""Gets the namespace of this ObjectReference.

        **参数解释**： 资源对象的命名空间。 **取值范围**： 不涉及。

        :return: The namespace of this ObjectReference.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ObjectReference.

        **参数解释**： 资源对象的命名空间。 **取值范围**： 不涉及。

        :param namespace: The namespace of this ObjectReference.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this ObjectReference.

        **参数解释**： 资源对象的名称。 **取值范围**： 不涉及。

        :return: The name of this ObjectReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectReference.

        **参数解释**： 资源对象的名称。 **取值范围**： 不涉及。

        :param name: The name of this ObjectReference.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this ObjectReference.

        **参数解释**： 资源对象的唯一标识符（UID）。 **取值范围**： 不涉及。

        :return: The uid of this ObjectReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ObjectReference.

        **参数解释**： 资源对象的唯一标识符（UID）。 **取值范围**： 不涉及。

        :param uid: The uid of this ObjectReference.
        :type uid: str
        """
        self._uid = uid

    @property
    def resource_version(self):
        r"""Gets the resource_version of this ObjectReference.

        **参数解释**： 资源对象的当前版本。 **取值范围**： 不涉及。

        :return: The resource_version of this ObjectReference.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        r"""Sets the resource_version of this ObjectReference.

        **参数解释**： 资源对象的当前版本。 **取值范围**： 不涉及。

        :param resource_version: The resource_version of this ObjectReference.
        :type resource_version: str
        """
        self._resource_version = resource_version

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
        if not isinstance(other, ObjectReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
