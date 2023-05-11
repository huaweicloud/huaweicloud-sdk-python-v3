# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationBaseV3:

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
        'name': 'str',
        'description': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'icon': 'icon'
    }

    def __init__(self, id=None, name=None, description=None, region_id=None, region_name=None, project_id=None, project_name=None, icon=None):
        """ApplicationBaseV3

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param region_id: 区域id
        :type region_id: str
        :param region_name: 区域名称
        :type region_name: str
        :param project_id: 所属项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param icon: 应用图标
        :type icon: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._region_id = None
        self._region_name = None
        self._project_id = None
        self._project_name = None
        self._icon = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.region_id = region_id
        self.region_name = region_name
        self.project_id = project_id
        self.project_name = project_name
        if icon is not None:
            self.icon = icon

    @property
    def id(self):
        """Gets the id of this ApplicationBaseV3.

        应用id

        :return: The id of this ApplicationBaseV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationBaseV3.

        应用id

        :param id: The id of this ApplicationBaseV3.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplicationBaseV3.

        应用名称

        :return: The name of this ApplicationBaseV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationBaseV3.

        应用名称

        :param name: The name of this ApplicationBaseV3.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ApplicationBaseV3.

        应用描述

        :return: The description of this ApplicationBaseV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationBaseV3.

        应用描述

        :param description: The description of this ApplicationBaseV3.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        """Gets the region_id of this ApplicationBaseV3.

        区域id

        :return: The region_id of this ApplicationBaseV3.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ApplicationBaseV3.

        区域id

        :param region_id: The region_id of this ApplicationBaseV3.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this ApplicationBaseV3.

        区域名称

        :return: The region_name of this ApplicationBaseV3.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ApplicationBaseV3.

        区域名称

        :param region_name: The region_name of this ApplicationBaseV3.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ApplicationBaseV3.

        所属项目id

        :return: The project_id of this ApplicationBaseV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ApplicationBaseV3.

        所属项目id

        :param project_id: The project_id of this ApplicationBaseV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ApplicationBaseV3.

        项目名称

        :return: The project_name of this ApplicationBaseV3.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ApplicationBaseV3.

        项目名称

        :param project_name: The project_name of this ApplicationBaseV3.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def icon(self):
        """Gets the icon of this ApplicationBaseV3.

        应用图标

        :return: The icon of this ApplicationBaseV3.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ApplicationBaseV3.

        应用图标

        :param icon: The icon of this ApplicationBaseV3.
        :type icon: str
        """
        self._icon = icon

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
        if not isinstance(other, ApplicationBaseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
