# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SortInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asc': 'bool',
        'field': 'str'
    }

    attribute_map = {
        'asc': 'asc',
        'field': 'field'
    }

    def __init__(self, asc=None, field=None):
        r"""SortInfo

        The model defined in huaweicloud sdk

        :param asc: 是否升序
        :type asc: bool
        :param field: 排序字段
        :type field: str
        """
        
        

        self._asc = None
        self._field = None
        self.discriminator = None

        if asc is not None:
            self.asc = asc
        if field is not None:
            self.field = field

    @property
    def asc(self):
        r"""Gets the asc of this SortInfo.

        是否升序

        :return: The asc of this SortInfo.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this SortInfo.

        是否升序

        :param asc: The asc of this SortInfo.
        :type asc: bool
        """
        self._asc = asc

    @property
    def field(self):
        r"""Gets the field of this SortInfo.

        排序字段

        :return: The field of this SortInfo.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this SortInfo.

        排序字段

        :param field: The field of this SortInfo.
        :type field: str
        """
        self._field = field

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
        if not isinstance(other, SortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
