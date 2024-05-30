# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeTableFieldValueVO:

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
        'fd_id': 'str',
        'fd_value': 'str',
        'ordinal': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'fd_id': 'fd_id',
        'fd_value': 'fd_value',
        'ordinal': 'ordinal',
        'description': 'description'
    }

    def __init__(self, id=None, fd_id=None, fd_value=None, ordinal=None, description=None):
        """CodeTableFieldValueVO

        The model defined in huaweicloud sdk

        :param id: 码表字段ID，填写String类型替代Long类型。
        :type id: str
        :param fd_id: 所属码表属性ID，填写String类型替代Long类型。
        :type fd_id: str
        :param fd_value: 码表属性值。
        :type fd_value: str
        :param ordinal: 序号。
        :type ordinal: int
        :param description: 描述。
        :type description: str
        """
        
        

        self._id = None
        self._fd_id = None
        self._fd_value = None
        self._ordinal = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if fd_id is not None:
            self.fd_id = fd_id
        if fd_value is not None:
            self.fd_value = fd_value
        if ordinal is not None:
            self.ordinal = ordinal
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this CodeTableFieldValueVO.

        码表字段ID，填写String类型替代Long类型。

        :return: The id of this CodeTableFieldValueVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodeTableFieldValueVO.

        码表字段ID，填写String类型替代Long类型。

        :param id: The id of this CodeTableFieldValueVO.
        :type id: str
        """
        self._id = id

    @property
    def fd_id(self):
        """Gets the fd_id of this CodeTableFieldValueVO.

        所属码表属性ID，填写String类型替代Long类型。

        :return: The fd_id of this CodeTableFieldValueVO.
        :rtype: str
        """
        return self._fd_id

    @fd_id.setter
    def fd_id(self, fd_id):
        """Sets the fd_id of this CodeTableFieldValueVO.

        所属码表属性ID，填写String类型替代Long类型。

        :param fd_id: The fd_id of this CodeTableFieldValueVO.
        :type fd_id: str
        """
        self._fd_id = fd_id

    @property
    def fd_value(self):
        """Gets the fd_value of this CodeTableFieldValueVO.

        码表属性值。

        :return: The fd_value of this CodeTableFieldValueVO.
        :rtype: str
        """
        return self._fd_value

    @fd_value.setter
    def fd_value(self, fd_value):
        """Sets the fd_value of this CodeTableFieldValueVO.

        码表属性值。

        :param fd_value: The fd_value of this CodeTableFieldValueVO.
        :type fd_value: str
        """
        self._fd_value = fd_value

    @property
    def ordinal(self):
        """Gets the ordinal of this CodeTableFieldValueVO.

        序号。

        :return: The ordinal of this CodeTableFieldValueVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this CodeTableFieldValueVO.

        序号。

        :param ordinal: The ordinal of this CodeTableFieldValueVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def description(self):
        """Gets the description of this CodeTableFieldValueVO.

        描述。

        :return: The description of this CodeTableFieldValueVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodeTableFieldValueVO.

        描述。

        :param description: The description of this CodeTableFieldValueVO.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CodeTableFieldValueVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
