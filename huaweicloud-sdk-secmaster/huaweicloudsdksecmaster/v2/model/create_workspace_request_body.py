# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkspaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'view_bind_id': 'str',
        'is_view': 'bool',
        'name': 'str',
        'description': 'str',
        'project_name': 'str',
        'tags': 'list[TagsPojo]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'view_bind_id': 'view_bind_id',
        'is_view': 'is_view',
        'name': 'name',
        'description': 'description',
        'project_name': 'project_name',
        'tags': 'tags'
    }

    def __init__(self, region_id=None, enterprise_project_id=None, enterprise_project_name=None, view_bind_id=None, is_view=None, name=None, description=None, project_name=None, tags=None):
        r"""CreateWorkspaceRequestBody

        The model defined in huaweicloud sdk

        :param region_id: 区域id
        :type region_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param view_bind_id: 视图绑定的空间id
        :type view_bind_id: str
        :param is_view: 是否是视图
        :type is_view: bool
        :param name: 工作空间名称
        :type name: str
        :param description: 工作空间描述
        :type description: str
        :param project_name: 项目名称
        :type project_name: str
        :param tags: 标签数组
        :type tags: list[:class:`huaweicloudsdksecmaster.v2.TagsPojo`]
        """
        
        

        self._region_id = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._view_bind_id = None
        self._is_view = None
        self._name = None
        self._description = None
        self._project_name = None
        self._tags = None
        self.discriminator = None

        self.region_id = region_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if view_bind_id is not None:
            self.view_bind_id = view_bind_id
        if is_view is not None:
            self.is_view = is_view
        self.name = name
        if description is not None:
            self.description = description
        self.project_name = project_name
        if tags is not None:
            self.tags = tags

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateWorkspaceRequestBody.

        区域id

        :return: The region_id of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateWorkspaceRequestBody.

        区域id

        :param region_id: The region_id of this CreateWorkspaceRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateWorkspaceRequestBody.

        企业项目id

        :return: The enterprise_project_id of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateWorkspaceRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateWorkspaceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this CreateWorkspaceRequestBody.

        企业项目名称

        :return: The enterprise_project_name of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this CreateWorkspaceRequestBody.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this CreateWorkspaceRequestBody.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def view_bind_id(self):
        r"""Gets the view_bind_id of this CreateWorkspaceRequestBody.

        视图绑定的空间id

        :return: The view_bind_id of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._view_bind_id

    @view_bind_id.setter
    def view_bind_id(self, view_bind_id):
        r"""Sets the view_bind_id of this CreateWorkspaceRequestBody.

        视图绑定的空间id

        :param view_bind_id: The view_bind_id of this CreateWorkspaceRequestBody.
        :type view_bind_id: str
        """
        self._view_bind_id = view_bind_id

    @property
    def is_view(self):
        r"""Gets the is_view of this CreateWorkspaceRequestBody.

        是否是视图

        :return: The is_view of this CreateWorkspaceRequestBody.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this CreateWorkspaceRequestBody.

        是否是视图

        :param is_view: The is_view of this CreateWorkspaceRequestBody.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def name(self):
        r"""Gets the name of this CreateWorkspaceRequestBody.

        工作空间名称

        :return: The name of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWorkspaceRequestBody.

        工作空间名称

        :param name: The name of this CreateWorkspaceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateWorkspaceRequestBody.

        工作空间描述

        :return: The description of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWorkspaceRequestBody.

        工作空间描述

        :param description: The description of this CreateWorkspaceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def project_name(self):
        r"""Gets the project_name of this CreateWorkspaceRequestBody.

        项目名称

        :return: The project_name of this CreateWorkspaceRequestBody.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this CreateWorkspaceRequestBody.

        项目名称

        :param project_name: The project_name of this CreateWorkspaceRequestBody.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def tags(self):
        r"""Gets the tags of this CreateWorkspaceRequestBody.

        标签数组

        :return: The tags of this CreateWorkspaceRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.TagsPojo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateWorkspaceRequestBody.

        标签数组

        :param tags: The tags of this CreateWorkspaceRequestBody.
        :type tags: list[:class:`huaweicloudsdksecmaster.v2.TagsPojo`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateWorkspaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
