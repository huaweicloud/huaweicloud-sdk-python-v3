# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareResultOverview:

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
        'content_compare_result': 'str'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'content_compare_result': 'content_compare_result'
    }

    def __init__(self, source_db_name=None, target_db_name=None, content_compare_result=None):
        """ContentCompareResultOverview

        The model defined in huaweicloud sdk

        :param source_db_name: 源库名称。
        :type source_db_name: str
        :param target_db_name: 目标库名称。
        :type target_db_name: str
        :param content_compare_result: 对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比
        :type content_compare_result: str
        """
        
        

        self._source_db_name = None
        self._target_db_name = None
        self._content_compare_result = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.target_db_name = target_db_name
        self.content_compare_result = content_compare_result

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ContentCompareResultOverview.

        源库名称。

        :return: The source_db_name of this ContentCompareResultOverview.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ContentCompareResultOverview.

        源库名称。

        :param source_db_name: The source_db_name of this ContentCompareResultOverview.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this ContentCompareResultOverview.

        目标库名称。

        :return: The target_db_name of this ContentCompareResultOverview.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this ContentCompareResultOverview.

        目标库名称。

        :param target_db_name: The target_db_name of this ContentCompareResultOverview.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def content_compare_result(self):
        """Gets the content_compare_result of this ContentCompareResultOverview.

        对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :return: The content_compare_result of this ContentCompareResultOverview.
        :rtype: str
        """
        return self._content_compare_result

    @content_compare_result.setter
    def content_compare_result(self, content_compare_result):
        """Sets the content_compare_result of this ContentCompareResultOverview.

        对比结果。 - CONSISTENT-一致 - INCONSISTENT-不一致 - COMPARING-正在对比 - WAITING_FOR_COMPARISON-等待对比 - FAILED_TO_COMPARE-对比失败 - TARGET_DB_NOT_EXIT-目标库不存在 - CAN_NOT_COMPARE-无法对比

        :param content_compare_result: The content_compare_result of this ContentCompareResultOverview.
        :type content_compare_result: str
        """
        self._content_compare_result = content_compare_result

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
        if not isinstance(other, ContentCompareResultOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
