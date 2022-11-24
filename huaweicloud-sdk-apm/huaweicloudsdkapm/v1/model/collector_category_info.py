# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectorCategoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_id': 'int',
        'category_name': 'str',
        'display_name': 'str',
        'sequence': 'int'
    }

    attribute_map = {
        'category_id': 'category_id',
        'category_name': 'category_name',
        'display_name': 'display_name',
        'sequence': 'sequence'
    }

    def __init__(self, category_id=None, category_name=None, display_name=None, sequence=None):
        """CollectorCategoryInfo

        The model defined in huaweicloud sdk

        :param category_id: 采集器类别id。
        :type category_id: int
        :param category_name: 采集器类别名称。
        :type category_name: str
        :param display_name: 采集器类别展示名称。
        :type display_name: str
        :param sequence: 序列号。
        :type sequence: int
        """
        
        

        self._category_id = None
        self._category_name = None
        self._display_name = None
        self._sequence = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if display_name is not None:
            self.display_name = display_name
        if sequence is not None:
            self.sequence = sequence

    @property
    def category_id(self):
        """Gets the category_id of this CollectorCategoryInfo.

        采集器类别id。

        :return: The category_id of this CollectorCategoryInfo.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CollectorCategoryInfo.

        采集器类别id。

        :param category_id: The category_id of this CollectorCategoryInfo.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this CollectorCategoryInfo.

        采集器类别名称。

        :return: The category_name of this CollectorCategoryInfo.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this CollectorCategoryInfo.

        采集器类别名称。

        :param category_name: The category_name of this CollectorCategoryInfo.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def display_name(self):
        """Gets the display_name of this CollectorCategoryInfo.

        采集器类别展示名称。

        :return: The display_name of this CollectorCategoryInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CollectorCategoryInfo.

        采集器类别展示名称。

        :param display_name: The display_name of this CollectorCategoryInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def sequence(self):
        """Gets the sequence of this CollectorCategoryInfo.

        序列号。

        :return: The sequence of this CollectorCategoryInfo.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CollectorCategoryInfo.

        序列号。

        :param sequence: The sequence of this CollectorCategoryInfo.
        :type sequence: int
        """
        self._sequence = sequence

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
        if not isinstance(other, CollectorCategoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
