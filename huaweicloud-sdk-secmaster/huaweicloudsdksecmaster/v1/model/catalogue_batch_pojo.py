# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogueBatchPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_display': 'bool',
        'id': 'str',
        'second_alias_zh': 'str',
        'second_alias_en': 'str'
    }

    attribute_map = {
        'is_display': 'is_display',
        'id': 'id',
        'second_alias_zh': 'second_alias_zh',
        'second_alias_en': 'second_alias_en'
    }

    def __init__(self, is_display=None, id=None, second_alias_zh=None, second_alias_en=None):
        r"""CatalogueBatchPojo

        The model defined in huaweicloud sdk

        :param is_display: 是否显示
        :type is_display: bool
        :param id: 目录编码
        :type id: str
        :param second_alias_zh: 二级目录中文别名
        :type second_alias_zh: str
        :param second_alias_en: 二级目录中文别名
        :type second_alias_en: str
        """
        
        

        self._is_display = None
        self._id = None
        self._second_alias_zh = None
        self._second_alias_en = None
        self.discriminator = None

        if is_display is not None:
            self.is_display = is_display
        if id is not None:
            self.id = id
        if second_alias_zh is not None:
            self.second_alias_zh = second_alias_zh
        if second_alias_en is not None:
            self.second_alias_en = second_alias_en

    @property
    def is_display(self):
        r"""Gets the is_display of this CatalogueBatchPojo.

        是否显示

        :return: The is_display of this CatalogueBatchPojo.
        :rtype: bool
        """
        return self._is_display

    @is_display.setter
    def is_display(self, is_display):
        r"""Sets the is_display of this CatalogueBatchPojo.

        是否显示

        :param is_display: The is_display of this CatalogueBatchPojo.
        :type is_display: bool
        """
        self._is_display = is_display

    @property
    def id(self):
        r"""Gets the id of this CatalogueBatchPojo.

        目录编码

        :return: The id of this CatalogueBatchPojo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CatalogueBatchPojo.

        目录编码

        :param id: The id of this CatalogueBatchPojo.
        :type id: str
        """
        self._id = id

    @property
    def second_alias_zh(self):
        r"""Gets the second_alias_zh of this CatalogueBatchPojo.

        二级目录中文别名

        :return: The second_alias_zh of this CatalogueBatchPojo.
        :rtype: str
        """
        return self._second_alias_zh

    @second_alias_zh.setter
    def second_alias_zh(self, second_alias_zh):
        r"""Sets the second_alias_zh of this CatalogueBatchPojo.

        二级目录中文别名

        :param second_alias_zh: The second_alias_zh of this CatalogueBatchPojo.
        :type second_alias_zh: str
        """
        self._second_alias_zh = second_alias_zh

    @property
    def second_alias_en(self):
        r"""Gets the second_alias_en of this CatalogueBatchPojo.

        二级目录中文别名

        :return: The second_alias_en of this CatalogueBatchPojo.
        :rtype: str
        """
        return self._second_alias_en

    @second_alias_en.setter
    def second_alias_en(self, second_alias_en):
        r"""Sets the second_alias_en of this CatalogueBatchPojo.

        二级目录中文别名

        :param second_alias_en: The second_alias_en of this CatalogueBatchPojo.
        :type second_alias_en: str
        """
        self._second_alias_en = second_alias_en

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
        if not isinstance(other, CatalogueBatchPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
