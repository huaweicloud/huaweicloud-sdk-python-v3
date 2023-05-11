# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRecordIssueCountsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical': 'int',
        'serious': 'int',
        'normal': 'int',
        'prompt': 'int'
    }

    attribute_map = {
        'critical': 'critical',
        'serious': 'serious',
        'normal': 'normal',
        'prompt': 'prompt'
    }

    def __init__(self, critical=None, serious=None, normal=None, prompt=None):
        """CheckRecordIssueCountsInfo

        The model defined in huaweicloud sdk

        :param critical: 致命问题
        :type critical: int
        :param serious: 严重问题
        :type serious: int
        :param normal: 常规问题
        :type normal: int
        :param prompt: 提示问题
        :type prompt: int
        """
        
        

        self._critical = None
        self._serious = None
        self._normal = None
        self._prompt = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if serious is not None:
            self.serious = serious
        if normal is not None:
            self.normal = normal
        if prompt is not None:
            self.prompt = prompt

    @property
    def critical(self):
        """Gets the critical of this CheckRecordIssueCountsInfo.

        致命问题

        :return: The critical of this CheckRecordIssueCountsInfo.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this CheckRecordIssueCountsInfo.

        致命问题

        :param critical: The critical of this CheckRecordIssueCountsInfo.
        :type critical: int
        """
        self._critical = critical

    @property
    def serious(self):
        """Gets the serious of this CheckRecordIssueCountsInfo.

        严重问题

        :return: The serious of this CheckRecordIssueCountsInfo.
        :rtype: int
        """
        return self._serious

    @serious.setter
    def serious(self, serious):
        """Sets the serious of this CheckRecordIssueCountsInfo.

        严重问题

        :param serious: The serious of this CheckRecordIssueCountsInfo.
        :type serious: int
        """
        self._serious = serious

    @property
    def normal(self):
        """Gets the normal of this CheckRecordIssueCountsInfo.

        常规问题

        :return: The normal of this CheckRecordIssueCountsInfo.
        :rtype: int
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this CheckRecordIssueCountsInfo.

        常规问题

        :param normal: The normal of this CheckRecordIssueCountsInfo.
        :type normal: int
        """
        self._normal = normal

    @property
    def prompt(self):
        """Gets the prompt of this CheckRecordIssueCountsInfo.

        提示问题

        :return: The prompt of this CheckRecordIssueCountsInfo.
        :rtype: int
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """Sets the prompt of this CheckRecordIssueCountsInfo.

        提示问题

        :param prompt: The prompt of this CheckRecordIssueCountsInfo.
        :type prompt: int
        """
        self._prompt = prompt

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
        if not isinstance(other, CheckRecordIssueCountsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
