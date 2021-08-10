# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectCompareResultOverview:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'object_compare_result': 'str',
        'target_count': 'int',
        'source_count': 'int',
        'diff_count': 'int'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_compare_result': 'object_compare_result',
        'target_count': 'target_count',
        'source_count': 'source_count',
        'diff_count': 'diff_count'
    }

    def __init__(self, object_type=None, object_compare_result=None, target_count=None, source_count=None, diff_count=None):
        """ObjectCompareResultOverview - a model defined in huaweicloud sdk"""
        
        

        self._object_type = None
        self._object_compare_result = None
        self._target_count = None
        self._source_count = None
        self._diff_count = None
        self.discriminator = None

        self.object_type = object_type
        self.object_compare_result = object_compare_result
        self.target_count = target_count
        self.source_count = source_count
        self.diff_count = diff_count

    @property
    def object_type(self):
        """Gets the object_type of this ObjectCompareResultOverview.

        对象类型。

        :return: The object_type of this ObjectCompareResultOverview.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ObjectCompareResultOverview.

        对象类型。

        :param object_type: The object_type of this ObjectCompareResultOverview.
        :type: str
        """
        self._object_type = object_type

    @property
    def object_compare_result(self):
        """Gets the object_compare_result of this ObjectCompareResultOverview.

        对比结果。

        :return: The object_compare_result of this ObjectCompareResultOverview.
        :rtype: str
        """
        return self._object_compare_result

    @object_compare_result.setter
    def object_compare_result(self, object_compare_result):
        """Sets the object_compare_result of this ObjectCompareResultOverview.

        对比结果。

        :param object_compare_result: The object_compare_result of this ObjectCompareResultOverview.
        :type: str
        """
        self._object_compare_result = object_compare_result

    @property
    def target_count(self):
        """Gets the target_count of this ObjectCompareResultOverview.

        该类型的对象在目标库的个数。

        :return: The target_count of this ObjectCompareResultOverview.
        :rtype: int
        """
        return self._target_count

    @target_count.setter
    def target_count(self, target_count):
        """Sets the target_count of this ObjectCompareResultOverview.

        该类型的对象在目标库的个数。

        :param target_count: The target_count of this ObjectCompareResultOverview.
        :type: int
        """
        self._target_count = target_count

    @property
    def source_count(self):
        """Gets the source_count of this ObjectCompareResultOverview.

        该类型的对象在源库的个数。

        :return: The source_count of this ObjectCompareResultOverview.
        :rtype: int
        """
        return self._source_count

    @source_count.setter
    def source_count(self, source_count):
        """Sets the source_count of this ObjectCompareResultOverview.

        该类型的对象在源库的个数。

        :param source_count: The source_count of this ObjectCompareResultOverview.
        :type: int
        """
        self._source_count = source_count

    @property
    def diff_count(self):
        """Gets the diff_count of this ObjectCompareResultOverview.

        源库和目标库的差异数量。

        :return: The diff_count of this ObjectCompareResultOverview.
        :rtype: int
        """
        return self._diff_count

    @diff_count.setter
    def diff_count(self, diff_count):
        """Sets the diff_count of this ObjectCompareResultOverview.

        源库和目标库的差异数量。

        :param diff_count: The diff_count of this ObjectCompareResultOverview.
        :type: int
        """
        self._diff_count = diff_count

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
        if not isinstance(other, ObjectCompareResultOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
