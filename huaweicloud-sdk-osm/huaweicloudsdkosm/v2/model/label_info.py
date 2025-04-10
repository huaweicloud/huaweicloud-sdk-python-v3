# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_id': 'int',
        'name': 'str',
        'color': 'str'
    }

    attribute_map = {
        'label_id': 'label_id',
        'name': 'name',
        'color': 'color'
    }

    def __init__(self, label_id=None, name=None, color=None):
        r"""LabelInfo

        The model defined in huaweicloud sdk

        :param label_id: 标签id
        :type label_id: int
        :param name: 标签描述
        :type name: str
        :param color: 颜色id
        :type color: str
        """
        
        

        self._label_id = None
        self._name = None
        self._color = None
        self.discriminator = None

        if label_id is not None:
            self.label_id = label_id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color

    @property
    def label_id(self):
        r"""Gets the label_id of this LabelInfo.

        标签id

        :return: The label_id of this LabelInfo.
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this LabelInfo.

        标签id

        :param label_id: The label_id of this LabelInfo.
        :type label_id: int
        """
        self._label_id = label_id

    @property
    def name(self):
        r"""Gets the name of this LabelInfo.

        标签描述

        :return: The name of this LabelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LabelInfo.

        标签描述

        :param name: The name of this LabelInfo.
        :type name: str
        """
        self._name = name

    @property
    def color(self):
        r"""Gets the color of this LabelInfo.

        颜色id

        :return: The color of this LabelInfo.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelInfo.

        颜色id

        :param color: The color of this LabelInfo.
        :type color: str
        """
        self._color = color

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
        if not isinstance(other, LabelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
