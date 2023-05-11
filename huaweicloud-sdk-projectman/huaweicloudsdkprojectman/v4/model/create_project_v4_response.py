# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectV4Response(SdkResponse):

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
        'project_type': 'str',
        'user_num_id': 'int'
    }

    attribute_map = {
        'project_num_id': 'project_num_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'description': 'description',
        'project_type': 'project_type',
        'user_num_id': 'user_num_id'
    }

    def __init__(self, project_num_id=None, project_id=None, project_name=None, description=None, project_type=None, user_num_id=None):
        """CreateProjectV4Response

        The model defined in huaweicloud sdk

        :param project_num_id: 项目数字id
        :type project_num_id: int
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名
        :type project_name: str
        :param description: 项目描述
        :type description: str
        :param project_type: 项目类型
        :type project_type: str
        :param user_num_id: 创建者的数字id
        :type user_num_id: int
        """
        
        super(CreateProjectV4Response, self).__init__()

        self._project_num_id = None
        self._project_id = None
        self._project_name = None
        self._description = None
        self._project_type = None
        self._user_num_id = None
        self.discriminator = None

        if project_num_id is not None:
            self.project_num_id = project_num_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if description is not None:
            self.description = description
        if project_type is not None:
            self.project_type = project_type
        if user_num_id is not None:
            self.user_num_id = user_num_id

    @property
    def project_num_id(self):
        """Gets the project_num_id of this CreateProjectV4Response.

        项目数字id

        :return: The project_num_id of this CreateProjectV4Response.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        """Sets the project_num_id of this CreateProjectV4Response.

        项目数字id

        :param project_num_id: The project_num_id of this CreateProjectV4Response.
        :type project_num_id: int
        """
        self._project_num_id = project_num_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateProjectV4Response.

        项目id

        :return: The project_id of this CreateProjectV4Response.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateProjectV4Response.

        项目id

        :param project_id: The project_id of this CreateProjectV4Response.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this CreateProjectV4Response.

        项目名

        :return: The project_name of this CreateProjectV4Response.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateProjectV4Response.

        项目名

        :param project_name: The project_name of this CreateProjectV4Response.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def description(self):
        """Gets the description of this CreateProjectV4Response.

        项目描述

        :return: The description of this CreateProjectV4Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProjectV4Response.

        项目描述

        :param description: The description of this CreateProjectV4Response.
        :type description: str
        """
        self._description = description

    @property
    def project_type(self):
        """Gets the project_type of this CreateProjectV4Response.

        项目类型

        :return: The project_type of this CreateProjectV4Response.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this CreateProjectV4Response.

        项目类型

        :param project_type: The project_type of this CreateProjectV4Response.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def user_num_id(self):
        """Gets the user_num_id of this CreateProjectV4Response.

        创建者的数字id

        :return: The user_num_id of this CreateProjectV4Response.
        :rtype: int
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        """Sets the user_num_id of this CreateProjectV4Response.

        创建者的数字id

        :param user_num_id: The user_num_id of this CreateProjectV4Response.
        :type user_num_id: int
        """
        self._user_num_id = user_num_id

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
        if not isinstance(other, CreateProjectV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
