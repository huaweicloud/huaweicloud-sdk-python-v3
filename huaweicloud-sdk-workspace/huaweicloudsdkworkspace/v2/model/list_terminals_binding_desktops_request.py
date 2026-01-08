# coding: utf-8

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
        'computer_names': 'list[str]',
        'mac': 'str',
        'mac_list': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'count_only': 'bool'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'computer_names': 'computer_names',
        'mac': 'mac',
        'mac_list': 'mac_list',
        'offset': 'offset',
        'limit': 'limit',
        'count_only': 'count_only'
    }

    def __init__(self, computer_name=None, computer_names=None, mac=None, mac_list=None, offset=None, limit=None, count_only=None):
        r"""ListTerminalsBindingDesktopsRequest

        The model defined in huaweicloud sdk

        :param computer_name: 桌面名。
        :type computer_name: str
        :param computer_names: 桌面名列表。
        :type computer_names: list[str]
        :param mac: mac地址。
        :type mac: str
        :param mac_list: mac地址列表。
        :type mac_list: list[str]
        :param offset: 起始数。
        :type offset: int
        :param limit: 数量。
        :type limit: int
        :param count_only: 是否只查询结果总条数。
        :type count_only: bool
        """
        
        

        self._computer_name = None
        self._computer_names = None
        self._mac = None
        self._mac_list = None
        self._offset = None
        self._limit = None
        self._count_only = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if computer_names is not None:
            self.computer_names = computer_names
        if mac is not None:
            self.mac = mac
        if mac_list is not None:
            self.mac_list = mac_list
        self.offset = offset
        self.limit = limit
        if count_only is not None:
            self.count_only = count_only

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ListTerminalsBindingDesktopsRequest.

        桌面名。

        :return: The computer_name of this ListTerminalsBindingDesktopsRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ListTerminalsBindingDesktopsRequest.

        桌面名。

        :param computer_name: The computer_name of this ListTerminalsBindingDesktopsRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def computer_names(self):
        r"""Gets the computer_names of this ListTerminalsBindingDesktopsRequest.

        桌面名列表。

        :return: The computer_names of this ListTerminalsBindingDesktopsRequest.
        :rtype: list[str]
        """
        return self._computer_names

    @computer_names.setter
    def computer_names(self, computer_names):
        r"""Sets the computer_names of this ListTerminalsBindingDesktopsRequest.

        桌面名列表。

        :param computer_names: The computer_names of this ListTerminalsBindingDesktopsRequest.
        :type computer_names: list[str]
        """
        self._computer_names = computer_names

    @property
    def mac(self):
        r"""Gets the mac of this ListTerminalsBindingDesktopsRequest.

        mac地址。

        :return: The mac of this ListTerminalsBindingDesktopsRequest.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        r"""Sets the mac of this ListTerminalsBindingDesktopsRequest.

        mac地址。

        :param mac: The mac of this ListTerminalsBindingDesktopsRequest.
        :type mac: str
        """
        self._mac = mac

    @property
    def mac_list(self):
        r"""Gets the mac_list of this ListTerminalsBindingDesktopsRequest.

        mac地址列表。

        :return: The mac_list of this ListTerminalsBindingDesktopsRequest.
        :rtype: list[str]
        """
        return self._mac_list

    @mac_list.setter
    def mac_list(self, mac_list):
        r"""Sets the mac_list of this ListTerminalsBindingDesktopsRequest.

        mac地址列表。

        :param mac_list: The mac_list of this ListTerminalsBindingDesktopsRequest.
        :type mac_list: list[str]
        """
        self._mac_list = mac_list

    @property
    def offset(self):
        r"""Gets the offset of this ListTerminalsBindingDesktopsRequest.

        起始数。

        :return: The offset of this ListTerminalsBindingDesktopsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTerminalsBindingDesktopsRequest.

        起始数。

        :param offset: The offset of this ListTerminalsBindingDesktopsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTerminalsBindingDesktopsRequest.

        数量。

        :return: The limit of this ListTerminalsBindingDesktopsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTerminalsBindingDesktopsRequest.

        数量。

        :param limit: The limit of this ListTerminalsBindingDesktopsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def count_only(self):
        r"""Gets the count_only of this ListTerminalsBindingDesktopsRequest.

        是否只查询结果总条数。

        :return: The count_only of this ListTerminalsBindingDesktopsRequest.
        :rtype: bool
        """
        return self._count_only

    @count_only.setter
    def count_only(self, count_only):
        r"""Sets the count_only of this ListTerminalsBindingDesktopsRequest.

        是否只查询结果总条数。

        :param count_only: The count_only of this ListTerminalsBindingDesktopsRequest.
        :type count_only: bool
        """
        self._count_only = count_only

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
