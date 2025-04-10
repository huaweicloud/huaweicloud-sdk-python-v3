# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupResponse(SdkResponse):

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
        'full_name': 'object',
        'id': 'int',
        'name': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'description': 'description',
        'full_name': 'full_name',
        'id': 'id',
        'name': 'name',
        'visibility': 'visibility'
    }

    def __init__(self, description=None, full_name=None, id=None, name=None, visibility=None):
        r"""CreateGroupResponse

        The model defined in huaweicloud sdk

        :param description: 代码组描述信息
        :type description: str
        :param full_name: 代码组全名
        :type full_name: object
        :param id: 代码组id
        :type id: int
        :param name: 错误码
        :type name: str
        :param visibility: 可见性, private public
        :type visibility: str
        """
        
        super(CreateGroupResponse, self).__init__()

        self._description = None
        self._full_name = None
        self._id = None
        self._name = None
        self._visibility = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if visibility is not None:
            self.visibility = visibility

    @property
    def description(self):
        r"""Gets the description of this CreateGroupResponse.

        代码组描述信息

        :return: The description of this CreateGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGroupResponse.

        代码组描述信息

        :param description: The description of this CreateGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def full_name(self):
        r"""Gets the full_name of this CreateGroupResponse.

        代码组全名

        :return: The full_name of this CreateGroupResponse.
        :rtype: object
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this CreateGroupResponse.

        代码组全名

        :param full_name: The full_name of this CreateGroupResponse.
        :type full_name: object
        """
        self._full_name = full_name

    @property
    def id(self):
        r"""Gets the id of this CreateGroupResponse.

        代码组id

        :return: The id of this CreateGroupResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateGroupResponse.

        代码组id

        :param id: The id of this CreateGroupResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateGroupResponse.

        错误码

        :return: The name of this CreateGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGroupResponse.

        错误码

        :param name: The name of this CreateGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def visibility(self):
        r"""Gets the visibility of this CreateGroupResponse.

        可见性, private public

        :return: The visibility of this CreateGroupResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this CreateGroupResponse.

        可见性, private public

        :param visibility: The visibility of this CreateGroupResponse.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, CreateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
