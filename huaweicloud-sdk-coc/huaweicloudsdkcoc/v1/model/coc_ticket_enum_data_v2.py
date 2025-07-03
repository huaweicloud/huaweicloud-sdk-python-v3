# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocTicketEnumDataV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prop_id': 'str',
        'biz_id': 'str',
        'name_zh': 'str',
        'name_en': 'str'
    }

    attribute_map = {
        'prop_id': 'prop_id',
        'biz_id': 'biz_id',
        'name_zh': 'name_zh',
        'name_en': 'name_en'
    }

    def __init__(self, prop_id=None, biz_id=None, name_zh=None, name_en=None):
        r"""CocTicketEnumDataV2

        The model defined in huaweicloud sdk

        :param prop_id: 匹配属性字段
        :type prop_id: str
        :param biz_id: 字段值
        :type biz_id: str
        :param name_zh: 中文名称
        :type name_zh: str
        :param name_en: 英文名称
        :type name_en: str
        """
        
        

        self._prop_id = None
        self._biz_id = None
        self._name_zh = None
        self._name_en = None
        self.discriminator = None

        if prop_id is not None:
            self.prop_id = prop_id
        if biz_id is not None:
            self.biz_id = biz_id
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en

    @property
    def prop_id(self):
        r"""Gets the prop_id of this CocTicketEnumDataV2.

        匹配属性字段

        :return: The prop_id of this CocTicketEnumDataV2.
        :rtype: str
        """
        return self._prop_id

    @prop_id.setter
    def prop_id(self, prop_id):
        r"""Sets the prop_id of this CocTicketEnumDataV2.

        匹配属性字段

        :param prop_id: The prop_id of this CocTicketEnumDataV2.
        :type prop_id: str
        """
        self._prop_id = prop_id

    @property
    def biz_id(self):
        r"""Gets the biz_id of this CocTicketEnumDataV2.

        字段值

        :return: The biz_id of this CocTicketEnumDataV2.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this CocTicketEnumDataV2.

        字段值

        :param biz_id: The biz_id of this CocTicketEnumDataV2.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def name_zh(self):
        r"""Gets the name_zh of this CocTicketEnumDataV2.

        中文名称

        :return: The name_zh of this CocTicketEnumDataV2.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this CocTicketEnumDataV2.

        中文名称

        :param name_zh: The name_zh of this CocTicketEnumDataV2.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this CocTicketEnumDataV2.

        英文名称

        :return: The name_en of this CocTicketEnumDataV2.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CocTicketEnumDataV2.

        英文名称

        :param name_en: The name_en of this CocTicketEnumDataV2.
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
        if not isinstance(other, CocTicketEnumDataV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
