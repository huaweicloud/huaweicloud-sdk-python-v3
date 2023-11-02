# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorDataObjectDetailIndicatorType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indicator_type': 'str',
        'id': 'str',
        'category': 'str',
        'layout_id': 'str'
    }

    attribute_map = {
        'indicator_type': 'indicator_type',
        'id': 'id',
        'category': 'category',
        'layout_id': 'layout_id'
    }

    def __init__(self, indicator_type=None, id=None, category=None, layout_id=None):
        """IndicatorDataObjectDetailIndicatorType

        The model defined in huaweicloud sdk

        :param indicator_type: 情报类型
        :type indicator_type: str
        :param id: 情报类型ID
        :type id: str
        :param category: 目录
        :type category: str
        :param layout_id: 布局ID
        :type layout_id: str
        """
        
        

        self._indicator_type = None
        self._id = None
        self._category = None
        self._layout_id = None
        self.discriminator = None

        if indicator_type is not None:
            self.indicator_type = indicator_type
        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if layout_id is not None:
            self.layout_id = layout_id

    @property
    def indicator_type(self):
        """Gets the indicator_type of this IndicatorDataObjectDetailIndicatorType.

        情报类型

        :return: The indicator_type of this IndicatorDataObjectDetailIndicatorType.
        :rtype: str
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this IndicatorDataObjectDetailIndicatorType.

        情报类型

        :param indicator_type: The indicator_type of this IndicatorDataObjectDetailIndicatorType.
        :type indicator_type: str
        """
        self._indicator_type = indicator_type

    @property
    def id(self):
        """Gets the id of this IndicatorDataObjectDetailIndicatorType.

        情报类型ID

        :return: The id of this IndicatorDataObjectDetailIndicatorType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndicatorDataObjectDetailIndicatorType.

        情报类型ID

        :param id: The id of this IndicatorDataObjectDetailIndicatorType.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        """Gets the category of this IndicatorDataObjectDetailIndicatorType.

        目录

        :return: The category of this IndicatorDataObjectDetailIndicatorType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this IndicatorDataObjectDetailIndicatorType.

        目录

        :param category: The category of this IndicatorDataObjectDetailIndicatorType.
        :type category: str
        """
        self._category = category

    @property
    def layout_id(self):
        """Gets the layout_id of this IndicatorDataObjectDetailIndicatorType.

        布局ID

        :return: The layout_id of this IndicatorDataObjectDetailIndicatorType.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this IndicatorDataObjectDetailIndicatorType.

        布局ID

        :param layout_id: The layout_id of this IndicatorDataObjectDetailIndicatorType.
        :type layout_id: str
        """
        self._layout_id = layout_id

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
        if not isinstance(other, IndicatorDataObjectDetailIndicatorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
