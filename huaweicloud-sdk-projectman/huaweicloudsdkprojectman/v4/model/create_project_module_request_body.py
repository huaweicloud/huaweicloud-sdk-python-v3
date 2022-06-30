# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectModuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'module_name': 'str',
        'parent_module_id': 'int',
        'owner': 'UserRequest'
    }

    attribute_map = {
        'description': 'description',
        'module_name': 'module_name',
        'parent_module_id': 'parent_module_id',
        'owner': 'owner'
    }

    def __init__(self, description=None, module_name=None, parent_module_id=None, owner=None):
        """CreateProjectModuleRequestBody

        The model defined in huaweicloud sdk

        :param description: 模块描述
        :type description: str
        :param module_name: 模块名称
        :type module_name: str
        :param parent_module_id: 父模块id
        :type parent_module_id: int
        :param owner: 
        :type owner: :class:`huaweicloudsdkprojectman.v4.UserRequest`
        """
        
        

        self._description = None
        self._module_name = None
        self._parent_module_id = None
        self._owner = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.module_name = module_name
        if parent_module_id is not None:
            self.parent_module_id = parent_module_id
        self.owner = owner

    @property
    def description(self):
        """Gets the description of this CreateProjectModuleRequestBody.

        模块描述

        :return: The description of this CreateProjectModuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProjectModuleRequestBody.

        模块描述

        :param description: The description of this CreateProjectModuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def module_name(self):
        """Gets the module_name of this CreateProjectModuleRequestBody.

        模块名称

        :return: The module_name of this CreateProjectModuleRequestBody.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this CreateProjectModuleRequestBody.

        模块名称

        :param module_name: The module_name of this CreateProjectModuleRequestBody.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def parent_module_id(self):
        """Gets the parent_module_id of this CreateProjectModuleRequestBody.

        父模块id

        :return: The parent_module_id of this CreateProjectModuleRequestBody.
        :rtype: int
        """
        return self._parent_module_id

    @parent_module_id.setter
    def parent_module_id(self, parent_module_id):
        """Sets the parent_module_id of this CreateProjectModuleRequestBody.

        父模块id

        :param parent_module_id: The parent_module_id of this CreateProjectModuleRequestBody.
        :type parent_module_id: int
        """
        self._parent_module_id = parent_module_id

    @property
    def owner(self):
        """Gets the owner of this CreateProjectModuleRequestBody.


        :return: The owner of this CreateProjectModuleRequestBody.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserRequest`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateProjectModuleRequestBody.


        :param owner: The owner of this CreateProjectModuleRequestBody.
        :type owner: :class:`huaweicloudsdkprojectman.v4.UserRequest`
        """
        self._owner = owner

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
        if not isinstance(other, CreateProjectModuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
