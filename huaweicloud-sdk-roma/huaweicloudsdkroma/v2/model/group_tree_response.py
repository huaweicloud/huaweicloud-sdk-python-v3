# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupTreeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'parent_id': 'int',
        'children': 'list[GroupTreeResponse]',
        'app_id': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_id': 'parent_id',
        'children': 'children',
        'app_id': 'app_id',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, name=None, parent_id=None, children=None, app_id=None, permissions=None):
        """GroupTreeResponse

        The model defined in huaweicloud sdk

        :param id: 分组id
        :type id: int
        :param name: 分组名称
        :type name: str
        :param parent_id: 父分组id
        :type parent_id: int
        :param children: 子分组
        :type children: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        :param app_id: 应用id
        :type app_id: str
        :param permissions: 权限
        :type permissions: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._parent_id = None
        self._children = None
        self._app_id = None
        self._permissions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if children is not None:
            self.children = children
        if app_id is not None:
            self.app_id = app_id
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this GroupTreeResponse.

        分组id

        :return: The id of this GroupTreeResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupTreeResponse.

        分组id

        :param id: The id of this GroupTreeResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupTreeResponse.

        分组名称

        :return: The name of this GroupTreeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupTreeResponse.

        分组名称

        :param name: The name of this GroupTreeResponse.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this GroupTreeResponse.

        父分组id

        :return: The parent_id of this GroupTreeResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this GroupTreeResponse.

        父分组id

        :param parent_id: The parent_id of this GroupTreeResponse.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def children(self):
        """Gets the children of this GroupTreeResponse.

        子分组

        :return: The children of this GroupTreeResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this GroupTreeResponse.

        子分组

        :param children: The children of this GroupTreeResponse.
        :type children: list[:class:`huaweicloudsdkroma.v2.GroupTreeResponse`]
        """
        self._children = children

    @property
    def app_id(self):
        """Gets the app_id of this GroupTreeResponse.

        应用id

        :return: The app_id of this GroupTreeResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this GroupTreeResponse.

        应用id

        :param app_id: The app_id of this GroupTreeResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def permissions(self):
        """Gets the permissions of this GroupTreeResponse.

        权限

        :return: The permissions of this GroupTreeResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupTreeResponse.

        权限

        :param permissions: The permissions of this GroupTreeResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

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
        if not isinstance(other, GroupTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
