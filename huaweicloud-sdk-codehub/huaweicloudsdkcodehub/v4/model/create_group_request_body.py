# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupRequestBody:

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
        'parent_id': 'int',
        'visibility': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'visibility': 'visibility',
        'description': 'description'
    }

    def __init__(self, name=None, parent_id=None, visibility=None, description=None):
        r"""CreateGroupRequestBody

        The model defined in huaweicloud sdk

        :param name: 代码组名称
        :type name: str
        :param parent_id: 父级代码组id, 不传默认在项目下创建代码组
        :type parent_id: int
        :param visibility: 可见性, private public
        :type visibility: str
        :param description: 描述
        :type description: str
        """
        
        

        self._name = None
        self._parent_id = None
        self._visibility = None
        self._description = None
        self.discriminator = None

        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if visibility is not None:
            self.visibility = visibility
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreateGroupRequestBody.

        代码组名称

        :return: The name of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGroupRequestBody.

        代码组名称

        :param name: The name of this CreateGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CreateGroupRequestBody.

        父级代码组id, 不传默认在项目下创建代码组

        :return: The parent_id of this CreateGroupRequestBody.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CreateGroupRequestBody.

        父级代码组id, 不传默认在项目下创建代码组

        :param parent_id: The parent_id of this CreateGroupRequestBody.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def visibility(self):
        r"""Gets the visibility of this CreateGroupRequestBody.

        可见性, private public

        :return: The visibility of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this CreateGroupRequestBody.

        可见性, private public

        :param visibility: The visibility of this CreateGroupRequestBody.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def description(self):
        r"""Gets the description of this CreateGroupRequestBody.

        描述

        :return: The description of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGroupRequestBody.

        描述

        :param description: The description of this CreateGroupRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
