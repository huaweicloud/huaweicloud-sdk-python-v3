# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InspectResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'count_num': 'int',
        'multiplicity': 'float',
        'legal_rate': 'float'
    }

    attribute_map = {
        'type': 'type',
        'count_num': 'count_num',
        'multiplicity': 'multiplicity',
        'legal_rate': 'legal_rate'
    }

    def __init__(self, type=None, count_num=None, multiplicity=None, legal_rate=None):
        r"""InspectResult

        The model defined in huaweicloud sdk

        :param type: 数据类型。
        :type type: str
        :param count_num: 条目数。
        :type count_num: int
        :param multiplicity: 重复读。
        :type multiplicity: float
        :param legal_rate: 合法率。
        :type legal_rate: float
        """
        
        

        self._type = None
        self._count_num = None
        self._multiplicity = None
        self._legal_rate = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if count_num is not None:
            self.count_num = count_num
        if multiplicity is not None:
            self.multiplicity = multiplicity
        if legal_rate is not None:
            self.legal_rate = legal_rate

    @property
    def type(self):
        r"""Gets the type of this InspectResult.

        数据类型。

        :return: The type of this InspectResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InspectResult.

        数据类型。

        :param type: The type of this InspectResult.
        :type type: str
        """
        self._type = type

    @property
    def count_num(self):
        r"""Gets the count_num of this InspectResult.

        条目数。

        :return: The count_num of this InspectResult.
        :rtype: int
        """
        return self._count_num

    @count_num.setter
    def count_num(self, count_num):
        r"""Sets the count_num of this InspectResult.

        条目数。

        :param count_num: The count_num of this InspectResult.
        :type count_num: int
        """
        self._count_num = count_num

    @property
    def multiplicity(self):
        r"""Gets the multiplicity of this InspectResult.

        重复读。

        :return: The multiplicity of this InspectResult.
        :rtype: float
        """
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity):
        r"""Sets the multiplicity of this InspectResult.

        重复读。

        :param multiplicity: The multiplicity of this InspectResult.
        :type multiplicity: float
        """
        self._multiplicity = multiplicity

    @property
    def legal_rate(self):
        r"""Gets the legal_rate of this InspectResult.

        合法率。

        :return: The legal_rate of this InspectResult.
        :rtype: float
        """
        return self._legal_rate

    @legal_rate.setter
    def legal_rate(self, legal_rate):
        r"""Sets the legal_rate of this InspectResult.

        合法率。

        :param legal_rate: The legal_rate of this InspectResult.
        :type legal_rate: float
        """
        self._legal_rate = legal_rate

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
        if not isinstance(other, InspectResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
