# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManageableGroupDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_name': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'full_name': 'full_name',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, full_name=None, id=None, name=None):
        r"""ManageableGroupDto

        The model defined in huaweicloud sdk

        :param full_name: 代码组全名
        :type full_name: str
        :param id: 代码组id
        :type id: int
        :param name: 代码组名
        :type name: str
        """
        
        

        self._full_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def full_name(self):
        r"""Gets the full_name of this ManageableGroupDto.

        代码组全名

        :return: The full_name of this ManageableGroupDto.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this ManageableGroupDto.

        代码组全名

        :param full_name: The full_name of this ManageableGroupDto.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def id(self):
        r"""Gets the id of this ManageableGroupDto.

        代码组id

        :return: The id of this ManageableGroupDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ManageableGroupDto.

        代码组id

        :param id: The id of this ManageableGroupDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ManageableGroupDto.

        代码组名

        :return: The name of this ManageableGroupDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ManageableGroupDto.

        代码组名

        :param name: The name of this ManageableGroupDto.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ManageableGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
