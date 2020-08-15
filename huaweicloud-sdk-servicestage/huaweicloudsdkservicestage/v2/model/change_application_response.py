# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ChangeApplicationResponse(SdkResponse):


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
        'creator': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'creator': 'creator',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, creator=None, project_id=None, enterprise_project_id=None, create_time=None, update_time=None):
        """ChangeApplicationResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._creator = None
        self._project_id = None
        self._enterprise_project_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if creator is not None:
            self.creator = creator
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ChangeApplicationResponse.

        应用ID。

        :return: The id of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeApplicationResponse.

        应用ID。

        :param id: The id of this ChangeApplicationResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ChangeApplicationResponse.

        应用名称。

        :return: The name of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeApplicationResponse.

        应用名称。

        :param name: The name of this ChangeApplicationResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ChangeApplicationResponse.

        应用描述。

        :return: The description of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeApplicationResponse.

        应用描述。

        :param description: The description of this ChangeApplicationResponse.
        :type: str
        """
        self._description = description

    @property
    def creator(self):
        """Gets the creator of this ChangeApplicationResponse.

        创建人。

        :return: The creator of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ChangeApplicationResponse.

        创建人。

        :param creator: The creator of this ChangeApplicationResponse.
        :type: str
        """
        self._creator = creator

    @property
    def project_id(self):
        """Gets the project_id of this ChangeApplicationResponse.

        项目ID。

        :return: The project_id of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ChangeApplicationResponse.

        项目ID。

        :param project_id: The project_id of this ChangeApplicationResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ChangeApplicationResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ChangeApplicationResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ChangeApplicationResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ChangeApplicationResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        """Gets the create_time of this ChangeApplicationResponse.

        创建时间。

        :return: The create_time of this ChangeApplicationResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ChangeApplicationResponse.

        创建时间。

        :param create_time: The create_time of this ChangeApplicationResponse.
        :type: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ChangeApplicationResponse.

        修改时间。

        :return: The update_time of this ChangeApplicationResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ChangeApplicationResponse.

        修改时间。

        :param update_time: The update_time of this ChangeApplicationResponse.
        :type: int
        """
        self._update_time = update_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
