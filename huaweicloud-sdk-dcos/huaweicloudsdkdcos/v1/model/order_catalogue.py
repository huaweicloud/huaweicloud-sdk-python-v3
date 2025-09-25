# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderCatalogue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'type': 'str',
        'sub_type': 'str',
        'subscribe': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'type': 'type',
        'sub_type': 'sub_type',
        'subscribe': 'subscribe'
    }

    def __init__(self, code=None, type=None, sub_type=None, subscribe=None):
        r"""OrderCatalogue

        The model defined in huaweicloud sdk

        :param code: 服务单类型编码
        :type code: str
        :param type: 类型
        :type type: str
        :param sub_type: 子类型
        :type sub_type: str
        :param subscribe: 是否已开通
        :type subscribe: bool
        """
        
        

        self._code = None
        self._type = None
        self._sub_type = None
        self._subscribe = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if subscribe is not None:
            self.subscribe = subscribe

    @property
    def code(self):
        r"""Gets the code of this OrderCatalogue.

        服务单类型编码

        :return: The code of this OrderCatalogue.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this OrderCatalogue.

        服务单类型编码

        :param code: The code of this OrderCatalogue.
        :type code: str
        """
        self._code = code

    @property
    def type(self):
        r"""Gets the type of this OrderCatalogue.

        类型

        :return: The type of this OrderCatalogue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OrderCatalogue.

        类型

        :param type: The type of this OrderCatalogue.
        :type type: str
        """
        self._type = type

    @property
    def sub_type(self):
        r"""Gets the sub_type of this OrderCatalogue.

        子类型

        :return: The sub_type of this OrderCatalogue.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this OrderCatalogue.

        子类型

        :param sub_type: The sub_type of this OrderCatalogue.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def subscribe(self):
        r"""Gets the subscribe of this OrderCatalogue.

        是否已开通

        :return: The subscribe of this OrderCatalogue.
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        r"""Sets the subscribe of this OrderCatalogue.

        是否已开通

        :param subscribe: The subscribe of this OrderCatalogue.
        :type subscribe: bool
        """
        self._subscribe = subscribe

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
        if not isinstance(other, OrderCatalogue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
