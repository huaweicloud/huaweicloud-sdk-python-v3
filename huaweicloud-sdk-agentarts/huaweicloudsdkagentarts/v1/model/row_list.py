# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RowList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_by': 'str',
        'value': 'str'
    }

    attribute_map = {
        'group_by': 'group_by',
        'value': 'value'
    }

    def __init__(self, group_by=None, value=None):
        r"""RowList

        The model defined in huaweicloud sdk

        :param group_by: 分组名
        :type group_by: str
        :param value: 分组值
        :type value: str
        """
        
        

        self._group_by = None
        self._value = None
        self.discriminator = None

        self.group_by = group_by
        self.value = value

    @property
    def group_by(self):
        r"""Gets the group_by of this RowList.

        分组名

        :return: The group_by of this RowList.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this RowList.

        分组名

        :param group_by: The group_by of this RowList.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def value(self):
        r"""Gets the value of this RowList.

        分组值

        :return: The value of this RowList.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RowList.

        分组值

        :param value: The value of this RowList.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, RowList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
