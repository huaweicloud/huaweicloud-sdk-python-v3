# coding: utf-8

import re
import six



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
        'create_time': 'str',
        'description': 'str',
        'group': 'str',
        'id': 'int',
        'name': 'str',
        'source': 'int',
        'update_time': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'description': 'description',
        'group': 'group',
        'id': 'id',
        'name': 'name',
        'source': 'source',
        'update_time': 'update_time'
    }

    def __init__(self, create_time=None, description=None, group=None, id=None, name=None, source=None, update_time=None):
        """Project

        The model defined in huaweicloud sdk

        :param create_time: create_time
        :type create_time: str
        :param description: description
        :type description: str
        :param group: group
        :type group: str
        :param id: id
        :type id: int
        :param name: name
        :type name: str
        :param source: source
        :type source: int
        :param update_time: update_time
        :type update_time: str
        """
        
        

        self._create_time = None
        self._description = None
        self._group = None
        self._id = None
        self._name = None
        self._source = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if source is not None:
            self.source = source
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this Project.

        create_time

        :return: The create_time of this Project.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Project.

        create_time

        :param create_time: The create_time of this Project.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this Project.

        description

        :return: The description of this Project.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        description

        :param description: The description of this Project.
        :type description: str
        """
        self._description = description

    @property
    def group(self):
        """Gets the group of this Project.

        group

        :return: The group of this Project.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Project.

        group

        :param group: The group of this Project.
        :type group: str
        """
        self._group = group

    @property
    def id(self):
        """Gets the id of this Project.

        id

        :return: The id of this Project.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        id

        :param id: The id of this Project.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.

        name

        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        name

        :param name: The name of this Project.
        :type name: str
        """
        self._name = name

    @property
    def source(self):
        """Gets the source of this Project.

        source

        :return: The source of this Project.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Project.

        source

        :param source: The source of this Project.
        :type source: int
        """
        self._source = source

    @property
    def update_time(self):
        """Gets the update_time of this Project.

        update_time

        :return: The update_time of this Project.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Project.

        update_time

        :param update_time: The update_time of this Project.
        :type update_time: str
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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
