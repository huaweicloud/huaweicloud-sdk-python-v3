# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddressItemsUsingGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'key_word': 'str',
        'limit': 'int',
        'offset': 'int',
        'address': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'key_word': 'key_word',
        'limit': 'limit',
        'offset': 'offset',
        'address': 'address'
    }

    def __init__(self, set_id=None, key_word=None, limit=None, offset=None, address=None):
        """ListAddressItemsUsingGetRequest

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param key_word: 关键字
        :type key_word: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param address: ip地址
        :type address: str
        """
        
        

        self._set_id = None
        self._key_word = None
        self._limit = None
        self._offset = None
        self._address = None
        self.discriminator = None

        self.set_id = set_id
        if key_word is not None:
            self.key_word = key_word
        self.limit = limit
        self.offset = offset
        if address is not None:
            self.address = address

    @property
    def set_id(self):
        """Gets the set_id of this ListAddressItemsUsingGetRequest.

        地址组id

        :return: The set_id of this ListAddressItemsUsingGetRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ListAddressItemsUsingGetRequest.

        地址组id

        :param set_id: The set_id of this ListAddressItemsUsingGetRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def key_word(self):
        """Gets the key_word of this ListAddressItemsUsingGetRequest.

        关键字

        :return: The key_word of this ListAddressItemsUsingGetRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this ListAddressItemsUsingGetRequest.

        关键字

        :param key_word: The key_word of this ListAddressItemsUsingGetRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def limit(self):
        """Gets the limit of this ListAddressItemsUsingGetRequest.

        每页显示个数

        :return: The limit of this ListAddressItemsUsingGetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAddressItemsUsingGetRequest.

        每页显示个数

        :param limit: The limit of this ListAddressItemsUsingGetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAddressItemsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListAddressItemsUsingGetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAddressItemsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListAddressItemsUsingGetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def address(self):
        """Gets the address of this ListAddressItemsUsingGetRequest.

        ip地址

        :return: The address of this ListAddressItemsUsingGetRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListAddressItemsUsingGetRequest.

        ip地址

        :param address: The address of this ListAddressItemsUsingGetRequest.
        :type address: str
        """
        self._address = address

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
        if not isinstance(other, ListAddressItemsUsingGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
