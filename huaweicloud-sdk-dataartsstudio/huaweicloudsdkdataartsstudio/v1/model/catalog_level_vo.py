# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogLevelVO:

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
        'level': 'int',
        'name_ch': 'str',
        'name_en': 'str'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'name_ch': 'name_ch',
        'name_en': 'name_en'
    }

    def __init__(self, id=None, level=None, name_ch=None, name_en=None):
        r"""CatalogLevelVO

        The model defined in huaweicloud sdk

        :param id: 编号，ID字符串。
        :type id: str
        :param level: 层级。取值范围为1-7。
        :type level: int
        :param name_ch: 中文名称。
        :type name_ch: str
        :param name_en: 英文名称。
        :type name_en: str
        """
        
        

        self._id = None
        self._level = None
        self._name_ch = None
        self._name_en = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if name_ch is not None:
            self.name_ch = name_ch
        if name_en is not None:
            self.name_en = name_en

    @property
    def id(self):
        r"""Gets the id of this CatalogLevelVO.

        编号，ID字符串。

        :return: The id of this CatalogLevelVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CatalogLevelVO.

        编号，ID字符串。

        :param id: The id of this CatalogLevelVO.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        r"""Gets the level of this CatalogLevelVO.

        层级。取值范围为1-7。

        :return: The level of this CatalogLevelVO.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CatalogLevelVO.

        层级。取值范围为1-7。

        :param level: The level of this CatalogLevelVO.
        :type level: int
        """
        self._level = level

    @property
    def name_ch(self):
        r"""Gets the name_ch of this CatalogLevelVO.

        中文名称。

        :return: The name_ch of this CatalogLevelVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        r"""Sets the name_ch of this CatalogLevelVO.

        中文名称。

        :param name_ch: The name_ch of this CatalogLevelVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def name_en(self):
        r"""Gets the name_en of this CatalogLevelVO.

        英文名称。

        :return: The name_en of this CatalogLevelVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CatalogLevelVO.

        英文名称。

        :param name_en: The name_en of this CatalogLevelVO.
        :type name_en: str
        """
        self._name_en = name_en

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
        if not isinstance(other, CatalogLevelVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
