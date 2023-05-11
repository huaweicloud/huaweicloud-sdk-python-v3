# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtraInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item': 'str',
        'value': 'str',
        'note': 'list[str]'
    }

    attribute_map = {
        'item': 'item',
        'value': 'value',
        'note': 'note'
    }

    def __init__(self, item=None, value=None, note=None):
        """ExtraInfoList

        The model defined in huaweicloud sdk

        :param item: 表示key值，可能是qq, wechat, alipay及bank等。 
        :type item: str
        :param value: 表示value值，对应qq, wechat, alipay及bank等的账号。 
        :type value: str
        :param note: 对应item关联的额外信息，为bank时第一个默认为户名，第二个为开户行，为alipay时第一个默认为账号名。 
        :type note: list[str]
        """
        
        

        self._item = None
        self._value = None
        self._note = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if value is not None:
            self.value = value
        if note is not None:
            self.note = note

    @property
    def item(self):
        """Gets the item of this ExtraInfoList.

        表示key值，可能是qq, wechat, alipay及bank等。 

        :return: The item of this ExtraInfoList.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this ExtraInfoList.

        表示key值，可能是qq, wechat, alipay及bank等。 

        :param item: The item of this ExtraInfoList.
        :type item: str
        """
        self._item = item

    @property
    def value(self):
        """Gets the value of this ExtraInfoList.

        表示value值，对应qq, wechat, alipay及bank等的账号。 

        :return: The value of this ExtraInfoList.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExtraInfoList.

        表示value值，对应qq, wechat, alipay及bank等的账号。 

        :param value: The value of this ExtraInfoList.
        :type value: str
        """
        self._value = value

    @property
    def note(self):
        """Gets the note of this ExtraInfoList.

        对应item关联的额外信息，为bank时第一个默认为户名，第二个为开户行，为alipay时第一个默认为账号名。 

        :return: The note of this ExtraInfoList.
        :rtype: list[str]
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ExtraInfoList.

        对应item关联的额外信息，为bank时第一个默认为户名，第二个为开户行，为alipay时第一个默认为账号名。 

        :param note: The note of this ExtraInfoList.
        :type note: list[str]
        """
        self._note = note

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
        if not isinstance(other, ExtraInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
