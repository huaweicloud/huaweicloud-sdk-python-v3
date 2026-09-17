# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Project:

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
        'name': 'str',
        'description': 'str',
        'created_time': 'int',
        'updated_time': 'int',
        'project_code': 'str',
        'region': 'str',
        'is_archived': 'bool',
        'type': 'str',
        'creator': 'User'
    }

    attribute_map = {
        'project_num_id': 'project_num_id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'project_code': 'project_code',
        'region': 'region',
        'is_archived': 'is_archived',
        'type': 'type',
        'creator': 'creator'
    }

    def __init__(self, project_num_id=None, project_id=None, name=None, description=None, created_time=None, updated_time=None, project_code=None, region=None, is_archived=None, type=None, creator=None):
        r"""Project

        The model defined in huaweicloud sdk

        :param project_num_id: devcloud项目的数字id
        :type project_num_id: int
        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param name: 项目名称
        :type name: str
        :param description: 项目描述
        :type description: str
        :param created_time: 项目创建时间
        :type created_time: int
        :param updated_time: 项目更新时间
        :type updated_time: int
        :param project_code: 项目代号
        :type project_code: str
        :param region: 区域region
        :type region: str
        :param is_archived: 是否归档
        :type is_archived: bool
        :param type: 项目类型
        :type type: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkprojectman.v4.User`
        """
        
        

        self._project_num_id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._created_time = None
        self._updated_time = None
        self._project_code = None
        self._region = None
        self._is_archived = None
        self._type = None
        self._creator = None
        self.discriminator = None

        if project_num_id is not None:
            self.project_num_id = project_num_id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if project_code is not None:
            self.project_code = project_code
        if region is not None:
            self.region = region
        if is_archived is not None:
            self.is_archived = is_archived
        if type is not None:
            self.type = type
        if creator is not None:
            self.creator = creator

    @property
    def project_num_id(self):
        r"""Gets the project_num_id of this Project.

        devcloud项目的数字id

        :return: The project_num_id of this Project.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        r"""Sets the project_num_id of this Project.

        devcloud项目的数字id

        :param project_num_id: The project_num_id of this Project.
        :type project_num_id: int
        """
        self._project_num_id = project_num_id

    @property
    def project_id(self):
        r"""Gets the project_id of this Project.

        devcloud项目的32位id

        :return: The project_id of this Project.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Project.

        devcloud项目的32位id

        :param project_id: The project_id of this Project.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this Project.

        项目名称

        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Project.

        项目名称

        :param name: The name of this Project.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Project.

        项目描述

        :return: The description of this Project.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Project.

        项目描述

        :param description: The description of this Project.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        r"""Gets the created_time of this Project.

        项目创建时间

        :return: The created_time of this Project.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this Project.

        项目创建时间

        :param created_time: The created_time of this Project.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this Project.

        项目更新时间

        :return: The updated_time of this Project.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this Project.

        项目更新时间

        :param updated_time: The updated_time of this Project.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def project_code(self):
        r"""Gets the project_code of this Project.

        项目代号

        :return: The project_code of this Project.
        :rtype: str
        """
        return self._project_code

    @project_code.setter
    def project_code(self, project_code):
        r"""Sets the project_code of this Project.

        项目代号

        :param project_code: The project_code of this Project.
        :type project_code: str
        """
        self._project_code = project_code

    @property
    def region(self):
        r"""Gets the region of this Project.

        区域region

        :return: The region of this Project.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this Project.

        区域region

        :param region: The region of this Project.
        :type region: str
        """
        self._region = region

    @property
    def is_archived(self):
        r"""Gets the is_archived of this Project.

        是否归档

        :return: The is_archived of this Project.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        r"""Sets the is_archived of this Project.

        是否归档

        :param is_archived: The is_archived of this Project.
        :type is_archived: bool
        """
        self._is_archived = is_archived

    @property
    def type(self):
        r"""Gets the type of this Project.

        项目类型

        :return: The type of this Project.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Project.

        项目类型

        :param type: The type of this Project.
        :type type: str
        """
        self._type = type

    @property
    def creator(self):
        r"""Gets the creator of this Project.

        :return: The creator of this Project.
        :rtype: :class:`huaweicloudsdkprojectman.v4.User`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this Project.

        :param creator: The creator of this Project.
        :type creator: :class:`huaweicloudsdkprojectman.v4.User`
        """
        self._creator = creator

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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
