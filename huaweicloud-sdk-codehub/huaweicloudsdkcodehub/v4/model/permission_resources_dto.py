# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionResourcesDto:

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
        'name_cn': 'str',
        'resource_name_display': 'str',
        'resource_name_cn_display': 'str',
        'path': 'str',
        'scope': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'name_cn': 'name_cn',
        'resource_name_display': 'resource_name_display',
        'resource_name_cn_display': 'resource_name_cn_display',
        'path': 'path',
        'scope': 'scope',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, name_cn=None, resource_name_display=None, resource_name_cn_display=None, path=None, scope=None, created_at=None, updated_at=None):
        r"""PermissionResourcesDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 资源id。
        :type id: int
        :param name: **参数解释：** 资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param name_cn: **参数解释：** 资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name_cn: str
        :param resource_name_display: **参数解释：** 禁用资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type resource_name_display: str
        :param resource_name_cn_display: **参数解释：** 禁用资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type resource_name_cn_display: str
        :param path: **参数解释：** 权限路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type path: str
        :param scope: **参数解释：** 资源类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type scope: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._name_cn = None
        self._resource_name_display = None
        self._resource_name_cn_display = None
        self._path = None
        self._scope = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_cn is not None:
            self.name_cn = name_cn
        if resource_name_display is not None:
            self.resource_name_display = resource_name_display
        if resource_name_cn_display is not None:
            self.resource_name_cn_display = resource_name_cn_display
        if path is not None:
            self.path = path
        if scope is not None:
            self.scope = scope
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this PermissionResourcesDto.

        **参数解释：** 资源id。

        :return: The id of this PermissionResourcesDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PermissionResourcesDto.

        **参数解释：** 资源id。

        :param id: The id of this PermissionResourcesDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PermissionResourcesDto.

        **参数解释：** 资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this PermissionResourcesDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PermissionResourcesDto.

        **参数解释：** 资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this PermissionResourcesDto.
        :type name: str
        """
        self._name = name

    @property
    def name_cn(self):
        r"""Gets the name_cn of this PermissionResourcesDto.

        **参数解释：** 资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name_cn of this PermissionResourcesDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this PermissionResourcesDto.

        **参数解释：** 资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name_cn: The name_cn of this PermissionResourcesDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def resource_name_display(self):
        r"""Gets the resource_name_display of this PermissionResourcesDto.

        **参数解释：** 禁用资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The resource_name_display of this PermissionResourcesDto.
        :rtype: str
        """
        return self._resource_name_display

    @resource_name_display.setter
    def resource_name_display(self, resource_name_display):
        r"""Sets the resource_name_display of this PermissionResourcesDto.

        **参数解释：** 禁用资源名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param resource_name_display: The resource_name_display of this PermissionResourcesDto.
        :type resource_name_display: str
        """
        self._resource_name_display = resource_name_display

    @property
    def resource_name_cn_display(self):
        r"""Gets the resource_name_cn_display of this PermissionResourcesDto.

        **参数解释：** 禁用资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The resource_name_cn_display of this PermissionResourcesDto.
        :rtype: str
        """
        return self._resource_name_cn_display

    @resource_name_cn_display.setter
    def resource_name_cn_display(self, resource_name_cn_display):
        r"""Sets the resource_name_cn_display of this PermissionResourcesDto.

        **参数解释：** 禁用资源中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param resource_name_cn_display: The resource_name_cn_display of this PermissionResourcesDto.
        :type resource_name_cn_display: str
        """
        self._resource_name_cn_display = resource_name_cn_display

    @property
    def path(self):
        r"""Gets the path of this PermissionResourcesDto.

        **参数解释：** 权限路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The path of this PermissionResourcesDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PermissionResourcesDto.

        **参数解释：** 权限路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param path: The path of this PermissionResourcesDto.
        :type path: str
        """
        self._path = path

    @property
    def scope(self):
        r"""Gets the scope of this PermissionResourcesDto.

        **参数解释：** 资源类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The scope of this PermissionResourcesDto.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this PermissionResourcesDto.

        **参数解释：** 资源类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param scope: The scope of this PermissionResourcesDto.
        :type scope: str
        """
        self._scope = scope

    @property
    def created_at(self):
        r"""Gets the created_at of this PermissionResourcesDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this PermissionResourcesDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PermissionResourcesDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this PermissionResourcesDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PermissionResourcesDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this PermissionResourcesDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PermissionResourcesDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this PermissionResourcesDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, PermissionResourcesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
