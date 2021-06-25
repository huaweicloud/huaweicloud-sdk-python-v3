# coding: utf-8

import pprint
import re

import six





class LineCompareResultOverview:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'target_db_name': 'str',
        'line_compare_result': 'str'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'line_compare_result': 'line_compare_result'
    }

    def __init__(self, source_db_name=None, target_db_name=None, line_compare_result=None):
        """LineCompareResultOverview - a model defined in huaweicloud sdk"""
        
        

        self._source_db_name = None
        self._target_db_name = None
        self._line_compare_result = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.target_db_name = target_db_name
        self.line_compare_result = line_compare_result

    @property
    def source_db_name(self):
        """Gets the source_db_name of this LineCompareResultOverview.

        源库名称。

        :return: The source_db_name of this LineCompareResultOverview.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this LineCompareResultOverview.

        源库名称。

        :param source_db_name: The source_db_name of this LineCompareResultOverview.
        :type: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this LineCompareResultOverview.

        目标库名称。

        :return: The target_db_name of this LineCompareResultOverview.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this LineCompareResultOverview.

        目标库名称。

        :param target_db_name: The target_db_name of this LineCompareResultOverview.
        :type: str
        """
        self._target_db_name = target_db_name

    @property
    def line_compare_result(self):
        """Gets the line_compare_result of this LineCompareResultOverview.

        对比结果。

        :return: The line_compare_result of this LineCompareResultOverview.
        :rtype: str
        """
        return self._line_compare_result

    @line_compare_result.setter
    def line_compare_result(self, line_compare_result):
        """Sets the line_compare_result of this LineCompareResultOverview.

        对比结果。

        :param line_compare_result: The line_compare_result of this LineCompareResultOverview.
        :type: str
        """
        self._line_compare_result = line_compare_result

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LineCompareResultOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other