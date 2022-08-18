# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'display_name': 'str',
        'logo': 'str',
        'name': 'str',
        'path': 'str',
        'project_type': 'str',
        'region': 'str',
        'source': 'SourceStorage',
        'tags': 'list[str]',
        'template_id': 'int',
        'arch': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'logo': 'logo',
        'name': 'name',
        'path': 'path',
        'project_type': 'project_type',
        'region': 'region',
        'source': 'source',
        'tags': 'tags',
        'template_id': 'template_id',
        'arch': 'arch'
    }

    def __init__(self, description=None, display_name=None, logo=None, name=None, path=None, project_type=None, region=None, source=None, tags=None, template_id=None, arch=None):
        """ProjectTemplates

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param display_name: 显示名
        :type display_name: str
        :param logo: 图标
        :type logo: str
        :param name: 模板名
        :type name: str
        :param path: 路径
        :type path: str
        :param project_type: 项目类型
        :type project_type: str
        :param region: 区域
        :type region: str
        :param source: 
        :type source: :class:`huaweicloudsdkcloudide.v2.SourceStorage`
        :param tags: tags
        :type tags: list[str]
        :param template_id: 模板id
        :type template_id: int
        :param arch: cpu架构
        :type arch: str
        """
        
        

        self._description = None
        self._display_name = None
        self._logo = None
        self._name = None
        self._path = None
        self._project_type = None
        self._region = None
        self._source = None
        self._tags = None
        self._template_id = None
        self._arch = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if project_type is not None:
            self.project_type = project_type
        if region is not None:
            self.region = region
        if source is not None:
            self.source = source
        if tags is not None:
            self.tags = tags
        if template_id is not None:
            self.template_id = template_id
        if arch is not None:
            self.arch = arch

    @property
    def description(self):
        """Gets the description of this ProjectTemplates.

        描述

        :return: The description of this ProjectTemplates.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectTemplates.

        描述

        :param description: The description of this ProjectTemplates.
        :type description: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this ProjectTemplates.

        显示名

        :return: The display_name of this ProjectTemplates.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ProjectTemplates.

        显示名

        :param display_name: The display_name of this ProjectTemplates.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def logo(self):
        """Gets the logo of this ProjectTemplates.

        图标

        :return: The logo of this ProjectTemplates.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this ProjectTemplates.

        图标

        :param logo: The logo of this ProjectTemplates.
        :type logo: str
        """
        self._logo = logo

    @property
    def name(self):
        """Gets the name of this ProjectTemplates.

        模板名

        :return: The name of this ProjectTemplates.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectTemplates.

        模板名

        :param name: The name of this ProjectTemplates.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this ProjectTemplates.

        路径

        :return: The path of this ProjectTemplates.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProjectTemplates.

        路径

        :param path: The path of this ProjectTemplates.
        :type path: str
        """
        self._path = path

    @property
    def project_type(self):
        """Gets the project_type of this ProjectTemplates.

        项目类型

        :return: The project_type of this ProjectTemplates.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this ProjectTemplates.

        项目类型

        :param project_type: The project_type of this ProjectTemplates.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def region(self):
        """Gets the region of this ProjectTemplates.

        区域

        :return: The region of this ProjectTemplates.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ProjectTemplates.

        区域

        :param region: The region of this ProjectTemplates.
        :type region: str
        """
        self._region = region

    @property
    def source(self):
        """Gets the source of this ProjectTemplates.


        :return: The source of this ProjectTemplates.
        :rtype: :class:`huaweicloudsdkcloudide.v2.SourceStorage`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ProjectTemplates.


        :param source: The source of this ProjectTemplates.
        :type source: :class:`huaweicloudsdkcloudide.v2.SourceStorage`
        """
        self._source = source

    @property
    def tags(self):
        """Gets the tags of this ProjectTemplates.

        tags

        :return: The tags of this ProjectTemplates.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProjectTemplates.

        tags

        :param tags: The tags of this ProjectTemplates.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def template_id(self):
        """Gets the template_id of this ProjectTemplates.

        模板id

        :return: The template_id of this ProjectTemplates.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ProjectTemplates.

        模板id

        :param template_id: The template_id of this ProjectTemplates.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def arch(self):
        """Gets the arch of this ProjectTemplates.

        cpu架构

        :return: The arch of this ProjectTemplates.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ProjectTemplates.

        cpu架构

        :param arch: The arch of this ProjectTemplates.
        :type arch: str
        """
        self._arch = arch

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
        if not isinstance(other, ProjectTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
