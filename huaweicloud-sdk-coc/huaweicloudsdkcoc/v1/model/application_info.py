# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationInfo:

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
        'code': 'str',
        'description': 'str',
        'domain_id': 'str',
        'parent_id': 'str',
        'path': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'description': 'description',
        'domain_id': 'domain_id',
        'parent_id': 'parent_id',
        'path': 'path',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, code=None, description=None, domain_id=None, parent_id=None, path=None, create_time=None, update_time=None):
        """ApplicationInfo

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param code: 
        :type code: str
        :param description: 
        :type description: str
        :param domain_id: 
        :type domain_id: str
        :param parent_id: 
        :type parent_id: str
        :param path: 
        :type path: str
        :param create_time: 
        :type create_time: str
        :param update_time: 
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._description = None
        self._domain_id = None
        self._parent_id = None
        self._path = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if parent_id is not None:
            self.parent_id = parent_id
        if path is not None:
            self.path = path
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ApplicationInfo.

        :return: The id of this ApplicationInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationInfo.

        :param id: The id of this ApplicationInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplicationInfo.

        :return: The name of this ApplicationInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationInfo.

        :param name: The name of this ApplicationInfo.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this ApplicationInfo.

        :return: The code of this ApplicationInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApplicationInfo.

        :param code: The code of this ApplicationInfo.
        :type code: str
        """
        self._code = code

    @property
    def description(self):
        """Gets the description of this ApplicationInfo.

        :return: The description of this ApplicationInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationInfo.

        :param description: The description of this ApplicationInfo.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this ApplicationInfo.

        :return: The domain_id of this ApplicationInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ApplicationInfo.

        :param domain_id: The domain_id of this ApplicationInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def parent_id(self):
        """Gets the parent_id of this ApplicationInfo.

        :return: The parent_id of this ApplicationInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ApplicationInfo.

        :param parent_id: The parent_id of this ApplicationInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def path(self):
        """Gets the path of this ApplicationInfo.

        :return: The path of this ApplicationInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApplicationInfo.

        :param path: The path of this ApplicationInfo.
        :type path: str
        """
        self._path = path

    @property
    def create_time(self):
        """Gets the create_time of this ApplicationInfo.

        :return: The create_time of this ApplicationInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApplicationInfo.

        :param create_time: The create_time of this ApplicationInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ApplicationInfo.

        :return: The update_time of this ApplicationInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ApplicationInfo.

        :param update_time: The update_time of this ApplicationInfo.
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
        if not isinstance(other, ApplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
