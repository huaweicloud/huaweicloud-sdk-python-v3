# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OwnerReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'name': 'str',
        'uid': 'str',
        'controller': 'bool',
        'block_owner_deletion': 'bool'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'name': 'name',
        'uid': 'uid',
        'controller': 'controller',
        'block_owner_deletion': 'blockOwnerDeletion'
    }

    def __init__(self, api_version=None, kind=None, name=None, uid=None, controller=None, block_owner_deletion=None):
        r"""OwnerReference

        The model defined in huaweicloud sdk

        :param api_version: 标识引用对象的API版本
        :type api_version: str
        :param kind: 引用对象的类型
        :type kind: str
        :param name: 引用对象的名称
        :type name: str
        :param uid: 引用对象的uid
        :type uid: str
        :param controller: 如果为true，表示该引用指向管理该资源的控制器
        :type controller: bool
        :param block_owner_deletion: 当为true且拥有者有名为\&quot;foregroundDeletion\&quot;的finalizer 时，会阻止拥有者被删除，直到这个引用被移除
        :type block_owner_deletion: bool
        """
        
        

        self._api_version = None
        self._kind = None
        self._name = None
        self._uid = None
        self._controller = None
        self._block_owner_deletion = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if controller is not None:
            self.controller = controller
        if block_owner_deletion is not None:
            self.block_owner_deletion = block_owner_deletion

    @property
    def api_version(self):
        r"""Gets the api_version of this OwnerReference.

        标识引用对象的API版本

        :return: The api_version of this OwnerReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this OwnerReference.

        标识引用对象的API版本

        :param api_version: The api_version of this OwnerReference.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this OwnerReference.

        引用对象的类型

        :return: The kind of this OwnerReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this OwnerReference.

        引用对象的类型

        :param kind: The kind of this OwnerReference.
        :type kind: str
        """
        self._kind = kind

    @property
    def name(self):
        r"""Gets the name of this OwnerReference.

        引用对象的名称

        :return: The name of this OwnerReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OwnerReference.

        引用对象的名称

        :param name: The name of this OwnerReference.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this OwnerReference.

        引用对象的uid

        :return: The uid of this OwnerReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this OwnerReference.

        引用对象的uid

        :param uid: The uid of this OwnerReference.
        :type uid: str
        """
        self._uid = uid

    @property
    def controller(self):
        r"""Gets the controller of this OwnerReference.

        如果为true，表示该引用指向管理该资源的控制器

        :return: The controller of this OwnerReference.
        :rtype: bool
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        r"""Sets the controller of this OwnerReference.

        如果为true，表示该引用指向管理该资源的控制器

        :param controller: The controller of this OwnerReference.
        :type controller: bool
        """
        self._controller = controller

    @property
    def block_owner_deletion(self):
        r"""Gets the block_owner_deletion of this OwnerReference.

        当为true且拥有者有名为\"foregroundDeletion\"的finalizer 时，会阻止拥有者被删除，直到这个引用被移除

        :return: The block_owner_deletion of this OwnerReference.
        :rtype: bool
        """
        return self._block_owner_deletion

    @block_owner_deletion.setter
    def block_owner_deletion(self, block_owner_deletion):
        r"""Sets the block_owner_deletion of this OwnerReference.

        当为true且拥有者有名为\"foregroundDeletion\"的finalizer 时，会阻止拥有者被删除，直到这个引用被移除

        :param block_owner_deletion: The block_owner_deletion of this OwnerReference.
        :type block_owner_deletion: bool
        """
        self._block_owner_deletion = block_owner_deletion

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
        if not isinstance(other, OwnerReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
