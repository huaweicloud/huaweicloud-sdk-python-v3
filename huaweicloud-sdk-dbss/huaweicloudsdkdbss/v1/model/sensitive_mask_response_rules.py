# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SensitiveMaskResponseRules:

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
        'name': 'str',
        'type': 'str',
        'regex': 'str',
        'mask_value': 'str',
        'status': 'str',
        'operate_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'regex': 'regex',
        'mask_value': 'mask_value',
        'status': 'status',
        'operate_time': 'operate_time'
    }

    def __init__(self, id=None, name=None, type=None, regex=None, mask_value=None, status=None, operate_time=None):
        """SensitiveMaskResponseRules

        The model defined in huaweicloud sdk

        :param id: 规则ID
        :type id: str
        :param name: 规则名称
        :type name: str
        :param type: 规则类型
        :type type: str
        :param regex: 规则正则表达式
        :type regex: str
        :param mask_value: 替换值
        :type mask_value: str
        :param status: 规则状态
        :type status: str
        :param operate_time: 操作时间
        :type operate_time: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._regex = None
        self._mask_value = None
        self._status = None
        self._operate_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if regex is not None:
            self.regex = regex
        if mask_value is not None:
            self.mask_value = mask_value
        if status is not None:
            self.status = status
        if operate_time is not None:
            self.operate_time = operate_time

    @property
    def id(self):
        """Gets the id of this SensitiveMaskResponseRules.

        规则ID

        :return: The id of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SensitiveMaskResponseRules.

        规则ID

        :param id: The id of this SensitiveMaskResponseRules.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SensitiveMaskResponseRules.

        规则名称

        :return: The name of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SensitiveMaskResponseRules.

        规则名称

        :param name: The name of this SensitiveMaskResponseRules.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this SensitiveMaskResponseRules.

        规则类型

        :return: The type of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SensitiveMaskResponseRules.

        规则类型

        :param type: The type of this SensitiveMaskResponseRules.
        :type type: str
        """
        self._type = type

    @property
    def regex(self):
        """Gets the regex of this SensitiveMaskResponseRules.

        规则正则表达式

        :return: The regex of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this SensitiveMaskResponseRules.

        规则正则表达式

        :param regex: The regex of this SensitiveMaskResponseRules.
        :type regex: str
        """
        self._regex = regex

    @property
    def mask_value(self):
        """Gets the mask_value of this SensitiveMaskResponseRules.

        替换值

        :return: The mask_value of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._mask_value

    @mask_value.setter
    def mask_value(self, mask_value):
        """Sets the mask_value of this SensitiveMaskResponseRules.

        替换值

        :param mask_value: The mask_value of this SensitiveMaskResponseRules.
        :type mask_value: str
        """
        self._mask_value = mask_value

    @property
    def status(self):
        """Gets the status of this SensitiveMaskResponseRules.

        规则状态

        :return: The status of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SensitiveMaskResponseRules.

        规则状态

        :param status: The status of this SensitiveMaskResponseRules.
        :type status: str
        """
        self._status = status

    @property
    def operate_time(self):
        """Gets the operate_time of this SensitiveMaskResponseRules.

        操作时间

        :return: The operate_time of this SensitiveMaskResponseRules.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this SensitiveMaskResponseRules.

        操作时间

        :param operate_time: The operate_time of this SensitiveMaskResponseRules.
        :type operate_time: str
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
        if not isinstance(other, SensitiveMaskResponseRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
