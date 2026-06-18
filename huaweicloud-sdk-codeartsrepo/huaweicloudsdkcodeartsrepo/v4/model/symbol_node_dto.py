# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SymbolNodeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_def': 'DefEntryDto',
        'children': 'list[SymbolNodeDto]'
    }

    attribute_map = {
        '_def': 'def',
        'children': 'children'
    }

    def __init__(self, _def=None, children=None):
        r"""SymbolNodeDto

        The model defined in huaweicloud sdk

        :param _def: 
        :type _def: :class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`
        :param children: **参数解释：** 子节点信息
        :type children: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        
        

        self.__def = None
        self._children = None
        self.discriminator = None

        if _def is not None:
            self._def = _def
        if children is not None:
            self.children = children

    @property
    def _def(self):
        r"""Gets the _def of this SymbolNodeDto.

        :return: The _def of this SymbolNodeDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`
        """
        return self.__def

    @_def.setter
    def _def(self, _def):
        r"""Sets the _def of this SymbolNodeDto.

        :param _def: The _def of this SymbolNodeDto.
        :type _def: :class:`huaweicloudsdkcodeartsrepo.v4.DefEntryDto`
        """
        self.__def = _def

    @property
    def children(self):
        r"""Gets the children of this SymbolNodeDto.

        **参数解释：** 子节点信息

        :return: The children of this SymbolNodeDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this SymbolNodeDto.

        **参数解释：** 子节点信息

        :param children: The children of this SymbolNodeDto.
        :type children: list[:class:`huaweicloudsdkcodeartsrepo.v4.SymbolNodeDto`]
        """
        self._children = children

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
        if not isinstance(other, SymbolNodeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
