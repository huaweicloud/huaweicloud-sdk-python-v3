# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IPDStatusVO:

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
        'name': 'str',
        'belonging': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'belonging': 'belonging'
    }

    def __init__(self, code=None, name=None, belonging=None):
        r"""IPDStatusVO

        The model defined in huaweicloud sdk

        :param code: 状态编码
        :type code: str
        :param name: 状态名称
        :type name: str
        :param belonging: 工作项的状态属性
        :type belonging: str
        """
        
        

        self._code = None
        self._name = None
        self._belonging = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if belonging is not None:
            self.belonging = belonging

    @property
    def code(self):
        r"""Gets the code of this IPDStatusVO.

        状态编码

        :return: The code of this IPDStatusVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this IPDStatusVO.

        状态编码

        :param code: The code of this IPDStatusVO.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this IPDStatusVO.

        状态名称

        :return: The name of this IPDStatusVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IPDStatusVO.

        状态名称

        :param name: The name of this IPDStatusVO.
        :type name: str
        """
        self._name = name

    @property
    def belonging(self):
        r"""Gets the belonging of this IPDStatusVO.

        工作项的状态属性

        :return: The belonging of this IPDStatusVO.
        :rtype: str
        """
        return self._belonging

    @belonging.setter
    def belonging(self, belonging):
        r"""Sets the belonging of this IPDStatusVO.

        工作项的状态属性

        :param belonging: The belonging of this IPDStatusVO.
        :type belonging: str
        """
        self._belonging = belonging

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
        if not isinstance(other, IPDStatusVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
