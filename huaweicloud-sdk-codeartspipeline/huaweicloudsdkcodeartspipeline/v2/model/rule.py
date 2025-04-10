# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'version': 'str',
        'operator': 'str',
        'operate_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'version': 'version',
        'operator': 'operator',
        'operate_time': 'operate_time'
    }

    def __init__(self, id=None, type=None, name=None, version=None, operator=None, operate_time=None):
        r"""Rule

        The model defined in huaweicloud sdk

        :param id: 规则ID
        :type id: str
        :param type: 规则类型
        :type type: str
        :param name: 规则名称
        :type name: str
        :param version: 规则版本
        :type version: str
        :param operator: 最近操作人员
        :type operator: str
        :param operate_time: 最近操作时间
        :type operate_time: int
        """
        
        

        self._id = None
        self._type = None
        self._name = None
        self._version = None
        self._operator = None
        self._operate_time = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.name = name
        self.version = version
        self.operator = operator
        self.operate_time = operate_time

    @property
    def id(self):
        r"""Gets the id of this Rule.

        规则ID

        :return: The id of this Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Rule.

        规则ID

        :param id: The id of this Rule.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this Rule.

        规则类型

        :return: The type of this Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Rule.

        规则类型

        :param type: The type of this Rule.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this Rule.

        规则名称

        :return: The name of this Rule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Rule.

        规则名称

        :param name: The name of this Rule.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this Rule.

        规则版本

        :return: The version of this Rule.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Rule.

        规则版本

        :param version: The version of this Rule.
        :type version: str
        """
        self._version = version

    @property
    def operator(self):
        r"""Gets the operator of this Rule.

        最近操作人员

        :return: The operator of this Rule.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Rule.

        最近操作人员

        :param operator: The operator of this Rule.
        :type operator: str
        """
        self._operator = operator

    @property
    def operate_time(self):
        r"""Gets the operate_time of this Rule.

        最近操作时间

        :return: The operate_time of this Rule.
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this Rule.

        最近操作时间

        :param operate_time: The operate_time of this Rule.
        :type operate_time: int
        """
        self._operate_time = operate_time

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
