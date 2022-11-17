# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'user_name': 'str',
        'computer_name': 'str',
        'desktop_ip': 'str',
        'offset': 'int',
        'limit': 'int',
        'desktop_id': 'str',
        'desktop_type': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'status': 'status',
        'user_name': 'user_name',
        'computer_name': 'computer_name',
        'desktop_ip': 'desktop_ip',
        'offset': 'offset',
        'limit': 'limit',
        'desktop_id': 'desktop_id',
        'desktop_type': 'desktop_type',
        'tag': 'tag'
    }

    def __init__(self, status=None, user_name=None, computer_name=None, desktop_ip=None, offset=None, limit=None, desktop_id=None, desktop_type=None, tag=None):
        """ListDesktopsDetailRequest

        The model defined in huaweicloud sdk

        :param status: 桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。
        :type status: str
        :param user_name: 桌面所属用户。
        :type user_name: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param desktop_ip: 桌面IP地址。
        :type desktop_ip: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-500，默认值500。
        :type limit: int
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_type: 桌面类型。  - DEDICATED：专属桌面。
        :type desktop_type: str
        :param tag: 桌面的标签。样例：  - key1&#x3D;value1。 - key1&#x3D;value1，key2&#x3D;value2。
        :type tag: str
        """
        
        

        self._status = None
        self._user_name = None
        self._computer_name = None
        self._desktop_ip = None
        self._offset = None
        self._limit = None
        self._desktop_id = None
        self._desktop_type = None
        self._tag = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if computer_name is not None:
            self.computer_name = computer_name
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if tag is not None:
            self.tag = tag

    @property
    def status(self):
        """Gets the status of this ListDesktopsDetailRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。

        :return: The status of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDesktopsDetailRequest.

        桌面状态。  - ACTIVE：运行中。 - SHUTOFF：关机。 - ERROR：异常。

        :param status: The status of this ListDesktopsDetailRequest.
        :type status: str
        """
        self._status = status

    @property
    def user_name(self):
        """Gets the user_name of this ListDesktopsDetailRequest.

        桌面所属用户。

        :return: The user_name of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListDesktopsDetailRequest.

        桌面所属用户。

        :param user_name: The user_name of this ListDesktopsDetailRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def computer_name(self):
        """Gets the computer_name of this ListDesktopsDetailRequest.

        桌面名。

        :return: The computer_name of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ListDesktopsDetailRequest.

        桌面名。

        :param computer_name: The computer_name of this ListDesktopsDetailRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def desktop_ip(self):
        """Gets the desktop_ip of this ListDesktopsDetailRequest.

        桌面IP地址。

        :return: The desktop_ip of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        """Sets the desktop_ip of this ListDesktopsDetailRequest.

        桌面IP地址。

        :param desktop_ip: The desktop_ip of this ListDesktopsDetailRequest.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def offset(self):
        """Gets the offset of this ListDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopsDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopsDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDesktopsDetailRequest.

        用于分页查询，取值范围0-500，默认值500。

        :return: The limit of this ListDesktopsDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDesktopsDetailRequest.

        用于分页查询，取值范围0-500，默认值500。

        :param limit: The limit of this ListDesktopsDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ListDesktopsDetailRequest.

        桌面ID。

        :return: The desktop_id of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ListDesktopsDetailRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ListDesktopsDetailRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_type(self):
        """Gets the desktop_type of this ListDesktopsDetailRequest.

        桌面类型。  - DEDICATED：专属桌面。

        :return: The desktop_type of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this ListDesktopsDetailRequest.

        桌面类型。  - DEDICATED：专属桌面。

        :param desktop_type: The desktop_type of this ListDesktopsDetailRequest.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def tag(self):
        """Gets the tag of this ListDesktopsDetailRequest.

        桌面的标签。样例：  - key1=value1。 - key1=value1，key2=value2。

        :return: The tag of this ListDesktopsDetailRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListDesktopsDetailRequest.

        桌面的标签。样例：  - key1=value1。 - key1=value1，key2=value2。

        :param tag: The tag of this ListDesktopsDetailRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ListDesktopsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
