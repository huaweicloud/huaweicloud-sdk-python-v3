# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVisionActiveCodeResultDTO:

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
        'active_code': 'str',
        'dev_name': 'str',
        'dev_type': 'str',
        'dept_code': 'str',
        'dept_name': 'str',
        'expire_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'active_code': 'activeCode',
        'dev_name': 'devName',
        'dev_type': 'devType',
        'dept_code': 'deptCode',
        'dept_name': 'deptName',
        'expire_date': 'expireDate'
    }

    def __init__(self, id=None, active_code=None, dev_name=None, dev_type=None, dept_code=None, dept_name=None, expire_date=None):
        """QueryVisionActiveCodeResultDTO

        The model defined in huaweicloud sdk

        :param id: 激活码唯一标识。
        :type id: str
        :param active_code: 激活码。
        :type active_code: str
        :param dev_name: 终端名称。
        :type dev_name: str
        :param dev_type: 终端类型。
        :type dev_type: str
        :param dept_code: 部门编码。
        :type dept_code: str
        :param dept_name: 部门名称。
        :type dept_name: str
        :param expire_date: 失效时间戳。
        :type expire_date: int
        """
        
        

        self._id = None
        self._active_code = None
        self._dev_name = None
        self._dev_type = None
        self._dept_code = None
        self._dept_name = None
        self._expire_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if active_code is not None:
            self.active_code = active_code
        if dev_name is not None:
            self.dev_name = dev_name
        if dev_type is not None:
            self.dev_type = dev_type
        if dept_code is not None:
            self.dept_code = dept_code
        if dept_name is not None:
            self.dept_name = dept_name
        if expire_date is not None:
            self.expire_date = expire_date

    @property
    def id(self):
        """Gets the id of this QueryVisionActiveCodeResultDTO.

        激活码唯一标识。

        :return: The id of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryVisionActiveCodeResultDTO.

        激活码唯一标识。

        :param id: The id of this QueryVisionActiveCodeResultDTO.
        :type id: str
        """
        self._id = id

    @property
    def active_code(self):
        """Gets the active_code of this QueryVisionActiveCodeResultDTO.

        激活码。

        :return: The active_code of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._active_code

    @active_code.setter
    def active_code(self, active_code):
        """Sets the active_code of this QueryVisionActiveCodeResultDTO.

        激活码。

        :param active_code: The active_code of this QueryVisionActiveCodeResultDTO.
        :type active_code: str
        """
        self._active_code = active_code

    @property
    def dev_name(self):
        """Gets the dev_name of this QueryVisionActiveCodeResultDTO.

        终端名称。

        :return: The dev_name of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._dev_name

    @dev_name.setter
    def dev_name(self, dev_name):
        """Sets the dev_name of this QueryVisionActiveCodeResultDTO.

        终端名称。

        :param dev_name: The dev_name of this QueryVisionActiveCodeResultDTO.
        :type dev_name: str
        """
        self._dev_name = dev_name

    @property
    def dev_type(self):
        """Gets the dev_type of this QueryVisionActiveCodeResultDTO.

        终端类型。

        :return: The dev_type of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._dev_type

    @dev_type.setter
    def dev_type(self, dev_type):
        """Sets the dev_type of this QueryVisionActiveCodeResultDTO.

        终端类型。

        :param dev_type: The dev_type of this QueryVisionActiveCodeResultDTO.
        :type dev_type: str
        """
        self._dev_type = dev_type

    @property
    def dept_code(self):
        """Gets the dept_code of this QueryVisionActiveCodeResultDTO.

        部门编码。

        :return: The dept_code of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this QueryVisionActiveCodeResultDTO.

        部门编码。

        :param dept_code: The dept_code of this QueryVisionActiveCodeResultDTO.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def dept_name(self):
        """Gets the dept_name of this QueryVisionActiveCodeResultDTO.

        部门名称。

        :return: The dept_name of this QueryVisionActiveCodeResultDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this QueryVisionActiveCodeResultDTO.

        部门名称。

        :param dept_name: The dept_name of this QueryVisionActiveCodeResultDTO.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def expire_date(self):
        """Gets the expire_date of this QueryVisionActiveCodeResultDTO.

        失效时间戳。

        :return: The expire_date of this QueryVisionActiveCodeResultDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this QueryVisionActiveCodeResultDTO.

        失效时间戳。

        :param expire_date: The expire_date of this QueryVisionActiveCodeResultDTO.
        :type expire_date: int
        """
        self._expire_date = expire_date

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
        if not isinstance(other, QueryVisionActiveCodeResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
