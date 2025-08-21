# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'full_name': 'str',
        'full_path': 'str',
        'my_role': 'GroupMyRoleDto',
        'name': 'str',
        'parent_id': 'int',
        'creator_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'full_name',
        'full_path': 'full_path',
        'my_role': 'my_role',
        'name': 'name',
        'parent_id': 'parent_id',
        'creator_id': 'creator_id'
    }

    def __init__(self, id=None, full_name=None, full_path=None, my_role=None, name=None, parent_id=None, creator_id=None):
        r"""TransferGroupResponse

        The model defined in huaweicloud sdk

        :param id: 代码组id
        :type id: int
        :param full_name: 代码组全名称
        :type full_name: str
        :param full_path: 代码组全路径
        :type full_path: str
        :param my_role: 
        :type my_role: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDto`
        :param name: 代码组名称
        :type name: str
        :param parent_id: 代码组父级id
        :type parent_id: int
        :param creator_id: 代码组所有者id
        :type creator_id: int
        """
        
        super(TransferGroupResponse, self).__init__()

        self._id = None
        self._full_name = None
        self._full_path = None
        self._my_role = None
        self._name = None
        self._parent_id = None
        self._creator_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if full_name is not None:
            self.full_name = full_name
        if full_path is not None:
            self.full_path = full_path
        if my_role is not None:
            self.my_role = my_role
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if creator_id is not None:
            self.creator_id = creator_id

    @property
    def id(self):
        r"""Gets the id of this TransferGroupResponse.

        代码组id

        :return: The id of this TransferGroupResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TransferGroupResponse.

        代码组id

        :param id: The id of this TransferGroupResponse.
        :type id: int
        """
        self._id = id

    @property
    def full_name(self):
        r"""Gets the full_name of this TransferGroupResponse.

        代码组全名称

        :return: The full_name of this TransferGroupResponse.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this TransferGroupResponse.

        代码组全名称

        :param full_name: The full_name of this TransferGroupResponse.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def full_path(self):
        r"""Gets the full_path of this TransferGroupResponse.

        代码组全路径

        :return: The full_path of this TransferGroupResponse.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this TransferGroupResponse.

        代码组全路径

        :param full_path: The full_path of this TransferGroupResponse.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def my_role(self):
        r"""Gets the my_role of this TransferGroupResponse.

        :return: The my_role of this TransferGroupResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDto`
        """
        return self._my_role

    @my_role.setter
    def my_role(self, my_role):
        r"""Sets the my_role of this TransferGroupResponse.

        :param my_role: The my_role of this TransferGroupResponse.
        :type my_role: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDto`
        """
        self._my_role = my_role

    @property
    def name(self):
        r"""Gets the name of this TransferGroupResponse.

        代码组名称

        :return: The name of this TransferGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TransferGroupResponse.

        代码组名称

        :param name: The name of this TransferGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this TransferGroupResponse.

        代码组父级id

        :return: The parent_id of this TransferGroupResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this TransferGroupResponse.

        代码组父级id

        :param parent_id: The parent_id of this TransferGroupResponse.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this TransferGroupResponse.

        代码组所有者id

        :return: The creator_id of this TransferGroupResponse.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this TransferGroupResponse.

        代码组所有者id

        :param creator_id: The creator_id of this TransferGroupResponse.
        :type creator_id: int
        """
        self._creator_id = creator_id

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
        if not isinstance(other, TransferGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
