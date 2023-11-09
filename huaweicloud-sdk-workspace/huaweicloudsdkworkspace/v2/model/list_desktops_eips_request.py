# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsEipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'user_name': 'str',
        'address': 'str',
        'offset': 'int',
        'limit': 'int',
        'state': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'user_name': 'user_name',
        'address': 'address',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state'
    }

    def __init__(self, enterprise_project_id=None, desktop_id=None, desktop_name=None, user_name=None, address=None, offset=None, limit=None, state=None):
        """ListDesktopsEipsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param user_name: 桌面所属用户。
        :type user_name: str
        :param address: EIP地址。
        :type address: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。
        :type limit: int
        :param state: EIP绑定状态。 - bind：表示已绑定的EIP。 - unbind：表示未绑定的EIP。
        :type state: str
        """
        
        

        self._enterprise_project_id = None
        self._desktop_id = None
        self._desktop_name = None
        self._user_name = None
        self._address = None
        self._offset = None
        self._limit = None
        self._state = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if user_name is not None:
            self.user_name = user_name
        if address is not None:
            self.address = address
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDesktopsEipsRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDesktopsEipsRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListDesktopsEipsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ListDesktopsEipsRequest.

        桌面ID。

        :return: The desktop_id of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ListDesktopsEipsRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ListDesktopsEipsRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this ListDesktopsEipsRequest.

        桌面名称。

        :return: The desktop_name of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this ListDesktopsEipsRequest.

        桌面名称。

        :param desktop_name: The desktop_name of this ListDesktopsEipsRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def user_name(self):
        """Gets the user_name of this ListDesktopsEipsRequest.

        桌面所属用户。

        :return: The user_name of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListDesktopsEipsRequest.

        桌面所属用户。

        :param user_name: The user_name of this ListDesktopsEipsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def address(self):
        """Gets the address of this ListDesktopsEipsRequest.

        EIP地址。

        :return: The address of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListDesktopsEipsRequest.

        EIP地址。

        :param address: The address of this ListDesktopsEipsRequest.
        :type address: str
        """
        self._address = address

    @property
    def offset(self):
        """Gets the offset of this ListDesktopsEipsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopsEipsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopsEipsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopsEipsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDesktopsEipsRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :return: The limit of this ListDesktopsEipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDesktopsEipsRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :param limit: The limit of this ListDesktopsEipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        """Gets the state of this ListDesktopsEipsRequest.

        EIP绑定状态。 - bind：表示已绑定的EIP。 - unbind：表示未绑定的EIP。

        :return: The state of this ListDesktopsEipsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListDesktopsEipsRequest.

        EIP绑定状态。 - bind：表示已绑定的EIP。 - unbind：表示未绑定的EIP。

        :param state: The state of this ListDesktopsEipsRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ListDesktopsEipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
