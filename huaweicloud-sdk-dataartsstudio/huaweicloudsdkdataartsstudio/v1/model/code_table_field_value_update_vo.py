# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeTableFieldValueUpdateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'to_add': 'list[CodeTableFieldVO]',
        'to_modify': 'list[CodeTableFieldVO]',
        'to_remove': 'list[CodeTableFieldVO]'
    }

    attribute_map = {
        'to_add': 'to_add',
        'to_modify': 'to_modify',
        'to_remove': 'to_remove'
    }

    def __init__(self, to_add=None, to_modify=None, to_remove=None):
        """CodeTableFieldValueUpdateVO

        The model defined in huaweicloud sdk

        :param to_add: 新增码表属性、属性值列表。
        :type to_add: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        :param to_modify: 编辑码表属性值列表。
        :type to_modify: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        :param to_remove: 删除码表属性ID列表。
        :type to_remove: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        
        

        self._to_add = None
        self._to_modify = None
        self._to_remove = None
        self.discriminator = None

        if to_add is not None:
            self.to_add = to_add
        if to_modify is not None:
            self.to_modify = to_modify
        if to_remove is not None:
            self.to_remove = to_remove

    @property
    def to_add(self):
        """Gets the to_add of this CodeTableFieldValueUpdateVO.

        新增码表属性、属性值列表。

        :return: The to_add of this CodeTableFieldValueUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        return self._to_add

    @to_add.setter
    def to_add(self, to_add):
        """Sets the to_add of this CodeTableFieldValueUpdateVO.

        新增码表属性、属性值列表。

        :param to_add: The to_add of this CodeTableFieldValueUpdateVO.
        :type to_add: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        self._to_add = to_add

    @property
    def to_modify(self):
        """Gets the to_modify of this CodeTableFieldValueUpdateVO.

        编辑码表属性值列表。

        :return: The to_modify of this CodeTableFieldValueUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        return self._to_modify

    @to_modify.setter
    def to_modify(self, to_modify):
        """Sets the to_modify of this CodeTableFieldValueUpdateVO.

        编辑码表属性值列表。

        :param to_modify: The to_modify of this CodeTableFieldValueUpdateVO.
        :type to_modify: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        self._to_modify = to_modify

    @property
    def to_remove(self):
        """Gets the to_remove of this CodeTableFieldValueUpdateVO.

        删除码表属性ID列表。

        :return: The to_remove of this CodeTableFieldValueUpdateVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        return self._to_remove

    @to_remove.setter
    def to_remove(self, to_remove):
        """Sets the to_remove of this CodeTableFieldValueUpdateVO.

        删除码表属性ID列表。

        :param to_remove: The to_remove of this CodeTableFieldValueUpdateVO.
        :type to_remove: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldVO`]
        """
        self._to_remove = to_remove

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
        if not isinstance(other, CodeTableFieldValueUpdateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
