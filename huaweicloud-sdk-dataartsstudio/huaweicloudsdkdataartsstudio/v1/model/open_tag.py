# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'tag_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'create_user': 'str',
        'domain_id': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'create_user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tag_id': 'tag_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_user': 'create_user',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'create_user_id': 'create_user_id'
    }

    def __init__(self, name=None, description=None, tag_id=None, create_time=None, update_time=None, create_user=None, domain_id=None, instance_id=None, project_id=None, create_user_id=None):
        """OpenTag

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param tag_id: 
        :type tag_id: str
        :param create_time: 
        :type create_time: int
        :param update_time: 
        :type update_time: int
        :param create_user: 
        :type create_user: str
        :param domain_id: 
        :type domain_id: str
        :param instance_id: 
        :type instance_id: str
        :param project_id: 
        :type project_id: str
        :param create_user_id: 
        :type create_user_id: str
        """
        
        

        self._name = None
        self._description = None
        self._tag_id = None
        self._create_time = None
        self._update_time = None
        self._create_user = None
        self._domain_id = None
        self._instance_id = None
        self._project_id = None
        self._create_user_id = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.tag_id = tag_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_user is not None:
            self.create_user = create_user
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if create_user_id is not None:
            self.create_user_id = create_user_id

    @property
    def name(self):
        """Gets the name of this OpenTag.

        :return: The name of this OpenTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenTag.

        :param name: The name of this OpenTag.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this OpenTag.

        :return: The description of this OpenTag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenTag.

        :param description: The description of this OpenTag.
        :type description: str
        """
        self._description = description

    @property
    def tag_id(self):
        """Gets the tag_id of this OpenTag.

        :return: The tag_id of this OpenTag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this OpenTag.

        :param tag_id: The tag_id of this OpenTag.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def create_time(self):
        """Gets the create_time of this OpenTag.

        :return: The create_time of this OpenTag.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OpenTag.

        :param create_time: The create_time of this OpenTag.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this OpenTag.

        :return: The update_time of this OpenTag.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this OpenTag.

        :param update_time: The update_time of this OpenTag.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_user(self):
        """Gets the create_user of this OpenTag.

        :return: The create_user of this OpenTag.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this OpenTag.

        :param create_user: The create_user of this OpenTag.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def domain_id(self):
        """Gets the domain_id of this OpenTag.

        :return: The domain_id of this OpenTag.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this OpenTag.

        :param domain_id: The domain_id of this OpenTag.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        """Gets the instance_id of this OpenTag.

        :return: The instance_id of this OpenTag.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this OpenTag.

        :param instance_id: The instance_id of this OpenTag.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        """Gets the project_id of this OpenTag.

        :return: The project_id of this OpenTag.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this OpenTag.

        :param project_id: The project_id of this OpenTag.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_user_id(self):
        """Gets the create_user_id of this OpenTag.

        :return: The create_user_id of this OpenTag.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        """Sets the create_user_id of this OpenTag.

        :param create_user_id: The create_user_id of this OpenTag.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

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
        if not isinstance(other, OpenTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
