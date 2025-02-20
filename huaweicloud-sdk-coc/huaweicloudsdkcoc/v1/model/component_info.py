# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInfo:

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
        'domain_id': 'str',
        'application_id': 'str',
        'path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'domain_id': 'domain_id',
        'application_id': 'application_id',
        'path': 'path'
    }

    def __init__(self, id=None, name=None, code=None, domain_id=None, application_id=None, path=None):
        """ComponentInfo

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param code: 
        :type code: str
        :param domain_id: 
        :type domain_id: str
        :param application_id: 
        :type application_id: str
        :param path: 
        :type path: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._domain_id = None
        self._application_id = None
        self._path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if application_id is not None:
            self.application_id = application_id
        if path is not None:
            self.path = path

    @property
    def id(self):
        """Gets the id of this ComponentInfo.

        :return: The id of this ComponentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentInfo.

        :param id: The id of this ComponentInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentInfo.

        :return: The name of this ComponentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentInfo.

        :param name: The name of this ComponentInfo.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this ComponentInfo.

        :return: The code of this ComponentInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ComponentInfo.

        :param code: The code of this ComponentInfo.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        """Gets the domain_id of this ComponentInfo.

        :return: The domain_id of this ComponentInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ComponentInfo.

        :param domain_id: The domain_id of this ComponentInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def application_id(self):
        """Gets the application_id of this ComponentInfo.

        :return: The application_id of this ComponentInfo.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ComponentInfo.

        :param application_id: The application_id of this ComponentInfo.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def path(self):
        """Gets the path of this ComponentInfo.

        :return: The path of this ComponentInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComponentInfo.

        :param path: The path of this ComponentInfo.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
