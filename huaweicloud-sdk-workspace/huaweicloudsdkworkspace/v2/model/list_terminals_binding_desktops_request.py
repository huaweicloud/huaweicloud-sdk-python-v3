# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTerminalsBindingDesktopsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computer_name': 'str',
        'mac': 'str',
        'offset': 'int',
        'limit': 'int',
        'count_only': 'bool'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'mac': 'mac',
        'offset': 'offset',
        'limit': 'limit',
        'count_only': 'count_only'
    }

    def __init__(self, computer_name=None, mac=None, offset=None, limit=None, count_only=None):
        """ListTerminalsBindingDesktopsRequest

        The model defined in huaweicloud sdk

        :param computer_name: 桌面名。
        :type computer_name: str
        :param mac: mac地址。
        :type mac: str
        :param offset: 起始数。
        :type offset: int
        :param limit: 数量。
        :type limit: int
        :param count_only: 是否只查询结果总条数
        :type count_only: bool
        """
        
        

        self._computer_name = None
        self._mac = None
        self._offset = None
        self._limit = None
        self._count_only = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if mac is not None:
            self.mac = mac
        self.offset = offset
        self.limit = limit
        if count_only is not None:
            self.count_only = count_only

    @property
    def computer_name(self):
        """Gets the computer_name of this ListTerminalsBindingDesktopsRequest.

        桌面名。

        :return: The computer_name of this ListTerminalsBindingDesktopsRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ListTerminalsBindingDesktopsRequest.

        桌面名。

        :param computer_name: The computer_name of this ListTerminalsBindingDesktopsRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def mac(self):
        """Gets the mac of this ListTerminalsBindingDesktopsRequest.

        mac地址。

        :return: The mac of this ListTerminalsBindingDesktopsRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this ListTerminalsBindingDesktopsRequest.

        mac地址。

        :param mac: The mac of this ListTerminalsBindingDesktopsRequest.
        :type mac: str
        """
        self._mac = mac

    @property
    def offset(self):
        """Gets the offset of this ListTerminalsBindingDesktopsRequest.

        起始数。

        :return: The offset of this ListTerminalsBindingDesktopsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTerminalsBindingDesktopsRequest.

        起始数。

        :param offset: The offset of this ListTerminalsBindingDesktopsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTerminalsBindingDesktopsRequest.

        数量。

        :return: The limit of this ListTerminalsBindingDesktopsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTerminalsBindingDesktopsRequest.

        数量。

        :param limit: The limit of this ListTerminalsBindingDesktopsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def count_only(self):
        """Gets the count_only of this ListTerminalsBindingDesktopsRequest.

        是否只查询结果总条数

        :return: The count_only of this ListTerminalsBindingDesktopsRequest.
        :rtype: bool
        """
        return self._count_only

    @count_only.setter
    def count_only(self, count_only):
        """Sets the count_only of this ListTerminalsBindingDesktopsRequest.

        是否只查询结果总条数

        :param count_only: The count_only of this ListTerminalsBindingDesktopsRequest.
        :type count_only: bool
        """
        self._count_only = count_only

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
        if not isinstance(other, ListTerminalsBindingDesktopsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
