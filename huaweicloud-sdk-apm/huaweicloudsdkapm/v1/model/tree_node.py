# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'parent': 'str',
        'real_id': 'int',
        'name': 'str',
        'display_name': 'str',
        'app_name': 'str',
        'app_id': 'int',
        'is_admin': 'bool',
        'is_root': 'bool',
        'business_id': 'int',
        'node_type': 'str',
        'region': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'parent': 'parent',
        'real_id': 'real_id',
        'name': 'name',
        'display_name': 'display_name',
        'app_name': 'app_name',
        'app_id': 'app_id',
        'is_admin': 'is_admin',
        'is_root': 'is_root',
        'business_id': 'business_id',
        'node_type': 'node_type',
        'region': 'region',
        'is_default': 'is_default'
    }

    def __init__(self, id=None, parent=None, real_id=None, name=None, display_name=None, app_name=None, app_id=None, is_admin=None, is_root=None, business_id=None, node_type=None, region=None, is_default=None):
        """TreeNode

        The model defined in huaweicloud sdk

        :param id: 拓扑树节点id
        :type id: str
        :param parent: 拓扑树节点的父节点
        :type parent: str
        :param real_id: 拓扑树节点的实际id
        :type real_id: int
        :param name: 拓扑树节点名称
        :type name: str
        :param display_name: 拓扑树节点展示名称
        :type display_name: str
        :param app_name: 组件名称
        :type app_name: str
        :param app_id: 组件id
        :type app_id: int
        :param is_admin: 是否是管理节点
        :type is_admin: bool
        :param is_root: 是否是根节点
        :type is_root: bool
        :param business_id: 应用id
        :type business_id: int
        :param node_type: 节点类型
        :type node_type: str
        :param region: 区域
        :type region: str
        :param is_default: 是否是默认的节点
        :type is_default: bool
        """
        
        

        self._id = None
        self._parent = None
        self._real_id = None
        self._name = None
        self._display_name = None
        self._app_name = None
        self._app_id = None
        self._is_admin = None
        self._is_root = None
        self._business_id = None
        self._node_type = None
        self._region = None
        self._is_default = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent is not None:
            self.parent = parent
        if real_id is not None:
            self.real_id = real_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if is_admin is not None:
            self.is_admin = is_admin
        if is_root is not None:
            self.is_root = is_root
        if business_id is not None:
            self.business_id = business_id
        if node_type is not None:
            self.node_type = node_type
        if region is not None:
            self.region = region
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this TreeNode.

        拓扑树节点id

        :return: The id of this TreeNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TreeNode.

        拓扑树节点id

        :param id: The id of this TreeNode.
        :type id: str
        """
        self._id = id

    @property
    def parent(self):
        """Gets the parent of this TreeNode.

        拓扑树节点的父节点

        :return: The parent of this TreeNode.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this TreeNode.

        拓扑树节点的父节点

        :param parent: The parent of this TreeNode.
        :type parent: str
        """
        self._parent = parent

    @property
    def real_id(self):
        """Gets the real_id of this TreeNode.

        拓扑树节点的实际id

        :return: The real_id of this TreeNode.
        :rtype: int
        """
        return self._real_id

    @real_id.setter
    def real_id(self, real_id):
        """Sets the real_id of this TreeNode.

        拓扑树节点的实际id

        :param real_id: The real_id of this TreeNode.
        :type real_id: int
        """
        self._real_id = real_id

    @property
    def name(self):
        """Gets the name of this TreeNode.

        拓扑树节点名称

        :return: The name of this TreeNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TreeNode.

        拓扑树节点名称

        :param name: The name of this TreeNode.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this TreeNode.

        拓扑树节点展示名称

        :return: The display_name of this TreeNode.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TreeNode.

        拓扑树节点展示名称

        :param display_name: The display_name of this TreeNode.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def app_name(self):
        """Gets the app_name of this TreeNode.

        组件名称

        :return: The app_name of this TreeNode.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this TreeNode.

        组件名称

        :param app_name: The app_name of this TreeNode.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this TreeNode.

        组件id

        :return: The app_id of this TreeNode.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TreeNode.

        组件id

        :param app_id: The app_id of this TreeNode.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def is_admin(self):
        """Gets the is_admin of this TreeNode.

        是否是管理节点

        :return: The is_admin of this TreeNode.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this TreeNode.

        是否是管理节点

        :param is_admin: The is_admin of this TreeNode.
        :type is_admin: bool
        """
        self._is_admin = is_admin

    @property
    def is_root(self):
        """Gets the is_root of this TreeNode.

        是否是根节点

        :return: The is_root of this TreeNode.
        :rtype: bool
        """
        return self._is_root

    @is_root.setter
    def is_root(self, is_root):
        """Sets the is_root of this TreeNode.

        是否是根节点

        :param is_root: The is_root of this TreeNode.
        :type is_root: bool
        """
        self._is_root = is_root

    @property
    def business_id(self):
        """Gets the business_id of this TreeNode.

        应用id

        :return: The business_id of this TreeNode.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TreeNode.

        应用id

        :param business_id: The business_id of this TreeNode.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def node_type(self):
        """Gets the node_type of this TreeNode.

        节点类型

        :return: The node_type of this TreeNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this TreeNode.

        节点类型

        :param node_type: The node_type of this TreeNode.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def region(self):
        """Gets the region of this TreeNode.

        区域

        :return: The region of this TreeNode.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TreeNode.

        区域

        :param region: The region of this TreeNode.
        :type region: str
        """
        self._region = region

    @property
    def is_default(self):
        """Gets the is_default of this TreeNode.

        是否是默认的节点

        :return: The is_default of this TreeNode.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this TreeNode.

        是否是默认的节点

        :param is_default: The is_default of this TreeNode.
        :type is_default: bool
        """
        self._is_default = is_default

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
        if not isinstance(other, TreeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
