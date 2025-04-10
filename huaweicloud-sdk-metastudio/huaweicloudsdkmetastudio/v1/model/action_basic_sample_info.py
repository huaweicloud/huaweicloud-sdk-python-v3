# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionBasicSampleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name_zh': 'str',
        'action_name_en': 'str',
        'action_tag': 'str',
        'catalog': 'str',
        'recommended_value': 'int',
        'is_selected': 'bool'
    }

    attribute_map = {
        'action_name_zh': 'action_name_zh',
        'action_name_en': 'action_name_en',
        'action_tag': 'action_tag',
        'catalog': 'catalog',
        'recommended_value': 'recommended_value',
        'is_selected': 'is_selected'
    }

    def __init__(self, action_name_zh=None, action_name_en=None, action_tag=None, catalog=None, recommended_value=None, is_selected=None):
        r"""ActionBasicSampleInfo

        The model defined in huaweicloud sdk

        :param action_name_zh: 原子动作中文名称。
        :type action_name_zh: str
        :param action_name_en: 原子动作英文名称。
        :type action_name_en: str
        :param action_tag: 原子动作标签。
        :type action_tag: str
        :param catalog: 原子动作标签。
        :type catalog: str
        :param recommended_value: 推荐等级。
        :type recommended_value: int
        :param is_selected: 是否选择此动作。
        :type is_selected: bool
        """
        
        

        self._action_name_zh = None
        self._action_name_en = None
        self._action_tag = None
        self._catalog = None
        self._recommended_value = None
        self._is_selected = None
        self.discriminator = None

        if action_name_zh is not None:
            self.action_name_zh = action_name_zh
        if action_name_en is not None:
            self.action_name_en = action_name_en
        self.action_tag = action_tag
        if catalog is not None:
            self.catalog = catalog
        if recommended_value is not None:
            self.recommended_value = recommended_value
        if is_selected is not None:
            self.is_selected = is_selected

    @property
    def action_name_zh(self):
        r"""Gets the action_name_zh of this ActionBasicSampleInfo.

        原子动作中文名称。

        :return: The action_name_zh of this ActionBasicSampleInfo.
        :rtype: str
        """
        return self._action_name_zh

    @action_name_zh.setter
    def action_name_zh(self, action_name_zh):
        r"""Sets the action_name_zh of this ActionBasicSampleInfo.

        原子动作中文名称。

        :param action_name_zh: The action_name_zh of this ActionBasicSampleInfo.
        :type action_name_zh: str
        """
        self._action_name_zh = action_name_zh

    @property
    def action_name_en(self):
        r"""Gets the action_name_en of this ActionBasicSampleInfo.

        原子动作英文名称。

        :return: The action_name_en of this ActionBasicSampleInfo.
        :rtype: str
        """
        return self._action_name_en

    @action_name_en.setter
    def action_name_en(self, action_name_en):
        r"""Sets the action_name_en of this ActionBasicSampleInfo.

        原子动作英文名称。

        :param action_name_en: The action_name_en of this ActionBasicSampleInfo.
        :type action_name_en: str
        """
        self._action_name_en = action_name_en

    @property
    def action_tag(self):
        r"""Gets the action_tag of this ActionBasicSampleInfo.

        原子动作标签。

        :return: The action_tag of this ActionBasicSampleInfo.
        :rtype: str
        """
        return self._action_tag

    @action_tag.setter
    def action_tag(self, action_tag):
        r"""Sets the action_tag of this ActionBasicSampleInfo.

        原子动作标签。

        :param action_tag: The action_tag of this ActionBasicSampleInfo.
        :type action_tag: str
        """
        self._action_tag = action_tag

    @property
    def catalog(self):
        r"""Gets the catalog of this ActionBasicSampleInfo.

        原子动作标签。

        :return: The catalog of this ActionBasicSampleInfo.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this ActionBasicSampleInfo.

        原子动作标签。

        :param catalog: The catalog of this ActionBasicSampleInfo.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def recommended_value(self):
        r"""Gets the recommended_value of this ActionBasicSampleInfo.

        推荐等级。

        :return: The recommended_value of this ActionBasicSampleInfo.
        :rtype: int
        """
        return self._recommended_value

    @recommended_value.setter
    def recommended_value(self, recommended_value):
        r"""Sets the recommended_value of this ActionBasicSampleInfo.

        推荐等级。

        :param recommended_value: The recommended_value of this ActionBasicSampleInfo.
        :type recommended_value: int
        """
        self._recommended_value = recommended_value

    @property
    def is_selected(self):
        r"""Gets the is_selected of this ActionBasicSampleInfo.

        是否选择此动作。

        :return: The is_selected of this ActionBasicSampleInfo.
        :rtype: bool
        """
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        r"""Sets the is_selected of this ActionBasicSampleInfo.

        是否选择此动作。

        :param is_selected: The is_selected of this ActionBasicSampleInfo.
        :type is_selected: bool
        """
        self._is_selected = is_selected

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
        if not isinstance(other, ActionBasicSampleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
