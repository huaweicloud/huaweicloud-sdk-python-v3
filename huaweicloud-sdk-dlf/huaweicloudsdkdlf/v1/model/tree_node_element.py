# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeNodeElement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'parent_directory_id': 'str',
        'name': 'str',
        'element_id': 'str',
        'owner': 'str',
        'process_type': 'str',
        'is_single_node_job': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'parent_directory_id': 'parent_directory_id',
        'name': 'name',
        'element_id': 'element_id',
        'owner': 'owner',
        'process_type': 'process_type',
        'is_single_node_job': 'is_single_node_job'
    }

    def __init__(self, type=None, parent_directory_id=None, name=None, element_id=None, owner=None, process_type=None, is_single_node_job=None):
        """TreeNodeElement

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param parent_directory_id: 
        :type parent_directory_id: str
        :param name: 
        :type name: str
        :param element_id: 
        :type element_id: str
        :param owner: 
        :type owner: str
        :param process_type: 
        :type process_type: str
        :param is_single_node_job: 
        :type is_single_node_job: bool
        """
        
        

        self._type = None
        self._parent_directory_id = None
        self._name = None
        self._element_id = None
        self._owner = None
        self._process_type = None
        self._is_single_node_job = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if parent_directory_id is not None:
            self.parent_directory_id = parent_directory_id
        if name is not None:
            self.name = name
        if element_id is not None:
            self.element_id = element_id
        if owner is not None:
            self.owner = owner
        if process_type is not None:
            self.process_type = process_type
        if is_single_node_job is not None:
            self.is_single_node_job = is_single_node_job

    @property
    def type(self):
        """Gets the type of this TreeNodeElement.

        :return: The type of this TreeNodeElement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TreeNodeElement.

        :param type: The type of this TreeNodeElement.
        :type type: str
        """
        self._type = type

    @property
    def parent_directory_id(self):
        """Gets the parent_directory_id of this TreeNodeElement.

        :return: The parent_directory_id of this TreeNodeElement.
        :rtype: str
        """
        return self._parent_directory_id

    @parent_directory_id.setter
    def parent_directory_id(self, parent_directory_id):
        """Sets the parent_directory_id of this TreeNodeElement.

        :param parent_directory_id: The parent_directory_id of this TreeNodeElement.
        :type parent_directory_id: str
        """
        self._parent_directory_id = parent_directory_id

    @property
    def name(self):
        """Gets the name of this TreeNodeElement.

        :return: The name of this TreeNodeElement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TreeNodeElement.

        :param name: The name of this TreeNodeElement.
        :type name: str
        """
        self._name = name

    @property
    def element_id(self):
        """Gets the element_id of this TreeNodeElement.

        :return: The element_id of this TreeNodeElement.
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this TreeNodeElement.

        :param element_id: The element_id of this TreeNodeElement.
        :type element_id: str
        """
        self._element_id = element_id

    @property
    def owner(self):
        """Gets the owner of this TreeNodeElement.

        :return: The owner of this TreeNodeElement.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TreeNodeElement.

        :param owner: The owner of this TreeNodeElement.
        :type owner: str
        """
        self._owner = owner

    @property
    def process_type(self):
        """Gets the process_type of this TreeNodeElement.

        :return: The process_type of this TreeNodeElement.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this TreeNodeElement.

        :param process_type: The process_type of this TreeNodeElement.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def is_single_node_job(self):
        """Gets the is_single_node_job of this TreeNodeElement.

        :return: The is_single_node_job of this TreeNodeElement.
        :rtype: bool
        """
        return self._is_single_node_job

    @is_single_node_job.setter
    def is_single_node_job(self, is_single_node_job):
        """Sets the is_single_node_job of this TreeNodeElement.

        :param is_single_node_job: The is_single_node_job of this TreeNodeElement.
        :type is_single_node_job: bool
        """
        self._is_single_node_job = is_single_node_job

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
        if not isinstance(other, TreeNodeElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
