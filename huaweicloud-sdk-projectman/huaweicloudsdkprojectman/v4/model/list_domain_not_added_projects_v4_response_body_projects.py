# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainNotAddedProjectsV4ResponseBodyProjects:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_num_id': 'int',
        'project_id': 'str',
        'project_name': 'str',
        'description': 'str',
        'created_time': 'int',
        'updated_time': 'int',
        'project_type': 'str',
        'creator': 'ListDomainNotAddedProjectsV4ResponseBodyCreator'
    }

    attribute_map = {
        'project_num_id': 'project_num_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'description': 'description',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'project_type': 'project_type',
        'creator': 'creator'
    }

    def __init__(self, project_num_id=None, project_id=None, project_name=None, description=None, created_time=None, updated_time=None, project_type=None, creator=None):
        """ListDomainNotAddedProjectsV4ResponseBodyProjects

        The model defined in huaweicloud sdk

        :param project_num_id: 项目数字id
        :type project_num_id: int
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名
        :type project_name: str
        :param description: 项目描述
        :type description: str
        :param created_time: 项目创建时间
        :type created_time: int
        :param updated_time: 项目更新时间
        :type updated_time: int
        :param project_type: 项目类型
        :type project_type: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4ResponseBodyCreator`
        """
        
        

        self._project_num_id = None
        self._project_id = None
        self._project_name = None
        self._description = None
        self._created_time = None
        self._updated_time = None
        self._project_type = None
        self._creator = None
        self.discriminator = None

        if project_num_id is not None:
            self.project_num_id = project_num_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if project_type is not None:
            self.project_type = project_type
        if creator is not None:
            self.creator = creator

    @property
    def project_num_id(self):
        """Gets the project_num_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目数字id

        :return: The project_num_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        """Sets the project_num_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目数字id

        :param project_num_id: The project_num_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type project_num_id: int
        """
        self._project_num_id = project_num_id

    @property
    def project_id(self):
        """Gets the project_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目id

        :return: The project_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目id

        :param project_id: The project_id of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目名

        :return: The project_name of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目名

        :param project_name: The project_name of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def description(self):
        """Gets the description of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目描述

        :return: The description of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目描述

        :param description: The description of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        """Gets the created_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目创建时间

        :return: The created_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目创建时间

        :param created_time: The created_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目更新时间

        :return: The updated_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目更新时间

        :param updated_time: The updated_time of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def project_type(self):
        """Gets the project_type of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目类型

        :return: The project_type of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        项目类型

        :param project_type: The project_type of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def creator(self):
        """Gets the creator of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        :return: The creator of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4ResponseBodyCreator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListDomainNotAddedProjectsV4ResponseBodyProjects.

        :param creator: The creator of this ListDomainNotAddedProjectsV4ResponseBodyProjects.
        :type creator: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4ResponseBodyCreator`
        """
        self._creator = creator

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
        if not isinstance(other, ListDomainNotAddedProjectsV4ResponseBodyProjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
