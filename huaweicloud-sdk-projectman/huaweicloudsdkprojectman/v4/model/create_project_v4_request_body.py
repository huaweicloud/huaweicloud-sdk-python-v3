# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectV4RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_name': 'str',
        'description': 'str',
        'source': 'str',
        'project_type': 'str',
        'enterprise_id': 'str',
        'template_id': 'int'
    }

    attribute_map = {
        'project_name': 'project_name',
        'description': 'description',
        'source': 'source',
        'project_type': 'project_type',
        'enterprise_id': 'enterprise_id',
        'template_id': 'template_id'
    }

    def __init__(self, project_name=None, description=None, source=None, project_type=None, enterprise_id=None, template_id=None):
        """CreateProjectV4RequestBody

        The model defined in huaweicloud sdk

        :param project_name: 项目名称
        :type project_name: str
        :param description: 项目描述
        :type description: str
        :param source: 项目来源
        :type source: str
        :param project_type: 项目类型 scrum, xboard(看板项目), basic, phoenix(凤凰项目)
        :type project_type: str
        :param enterprise_id: 项目要绑定的企业项目ID
        :type enterprise_id: str
        :param template_id: 用户创建的项目模板id
        :type template_id: int
        """
        
        

        self._project_name = None
        self._description = None
        self._source = None
        self._project_type = None
        self._enterprise_id = None
        self._template_id = None
        self.discriminator = None

        self.project_name = project_name
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        self.project_type = project_type
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if template_id is not None:
            self.template_id = template_id

    @property
    def project_name(self):
        """Gets the project_name of this CreateProjectV4RequestBody.

        项目名称

        :return: The project_name of this CreateProjectV4RequestBody.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateProjectV4RequestBody.

        项目名称

        :param project_name: The project_name of this CreateProjectV4RequestBody.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def description(self):
        """Gets the description of this CreateProjectV4RequestBody.

        项目描述

        :return: The description of this CreateProjectV4RequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProjectV4RequestBody.

        项目描述

        :param description: The description of this CreateProjectV4RequestBody.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this CreateProjectV4RequestBody.

        项目来源

        :return: The source of this CreateProjectV4RequestBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateProjectV4RequestBody.

        项目来源

        :param source: The source of this CreateProjectV4RequestBody.
        :type source: str
        """
        self._source = source

    @property
    def project_type(self):
        """Gets the project_type of this CreateProjectV4RequestBody.

        项目类型 scrum, xboard(看板项目), basic, phoenix(凤凰项目)

        :return: The project_type of this CreateProjectV4RequestBody.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this CreateProjectV4RequestBody.

        项目类型 scrum, xboard(看板项目), basic, phoenix(凤凰项目)

        :param project_type: The project_type of this CreateProjectV4RequestBody.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this CreateProjectV4RequestBody.

        项目要绑定的企业项目ID

        :return: The enterprise_id of this CreateProjectV4RequestBody.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this CreateProjectV4RequestBody.

        项目要绑定的企业项目ID

        :param enterprise_id: The enterprise_id of this CreateProjectV4RequestBody.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def template_id(self):
        """Gets the template_id of this CreateProjectV4RequestBody.

        用户创建的项目模板id

        :return: The template_id of this CreateProjectV4RequestBody.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateProjectV4RequestBody.

        用户创建的项目模板id

        :param template_id: The template_id of this CreateProjectV4RequestBody.
        :type template_id: int
        """
        self._template_id = template_id

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
        if not isinstance(other, CreateProjectV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
