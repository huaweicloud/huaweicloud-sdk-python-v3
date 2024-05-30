# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizedFieldsVOList:

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
        'fields': 'list[CustomizedFieldsVO]'
    }

    attribute_map = {
        'type': 'type',
        'fields': 'fields'
    }

    def __init__(self, type=None, fields=None):
        """CustomizedFieldsVOList

        The model defined in huaweicloud sdk

        :param type: 自定义项类型。 枚举值：   - TABLE: 表自定义项   - ATTRIBUTE: 属性自定义项   - SUBJECT: 主题自定义项   - METRIC: 业务指标自定义项 
        :type type: str
        :param fields: 自定义项列表。
        :type fields: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomizedFieldsVO`]
        """
        
        

        self._type = None
        self._fields = None
        self.discriminator = None

        self.type = type
        if fields is not None:
            self.fields = fields

    @property
    def type(self):
        """Gets the type of this CustomizedFieldsVOList.

        自定义项类型。 枚举值：   - TABLE: 表自定义项   - ATTRIBUTE: 属性自定义项   - SUBJECT: 主题自定义项   - METRIC: 业务指标自定义项 

        :return: The type of this CustomizedFieldsVOList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomizedFieldsVOList.

        自定义项类型。 枚举值：   - TABLE: 表自定义项   - ATTRIBUTE: 属性自定义项   - SUBJECT: 主题自定义项   - METRIC: 业务指标自定义项 

        :param type: The type of this CustomizedFieldsVOList.
        :type type: str
        """
        self._type = type

    @property
    def fields(self):
        """Gets the fields of this CustomizedFieldsVOList.

        自定义项列表。

        :return: The fields of this CustomizedFieldsVOList.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomizedFieldsVO`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CustomizedFieldsVOList.

        自定义项列表。

        :param fields: The fields of this CustomizedFieldsVOList.
        :type fields: list[:class:`huaweicloudsdkdataartsstudio.v1.CustomizedFieldsVO`]
        """
        self._fields = fields

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
        if not isinstance(other, CustomizedFieldsVOList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
