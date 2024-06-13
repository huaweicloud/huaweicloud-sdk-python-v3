# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssuePassDetailsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testing': 'int',
        'finished': 'int',
        'not_tested': 'int'
    }

    attribute_map = {
        'testing': 'testing',
        'finished': 'finished',
        'not_tested': 'not_tested'
    }

    def __init__(self, testing=None, finished=None, not_tested=None):
        """IssuePassDetailsVo

        The model defined in huaweicloud sdk

        :param testing: 统计测试中的需求
        :type testing: int
        :param finished: 统计已完成的需求
        :type finished: int
        :param not_tested: 统计未完成的需求
        :type not_tested: int
        """
        
        

        self._testing = None
        self._finished = None
        self._not_tested = None
        self.discriminator = None

        if testing is not None:
            self.testing = testing
        if finished is not None:
            self.finished = finished
        if not_tested is not None:
            self.not_tested = not_tested

    @property
    def testing(self):
        """Gets the testing of this IssuePassDetailsVo.

        统计测试中的需求

        :return: The testing of this IssuePassDetailsVo.
        :rtype: int
        """
        return self._testing

    @testing.setter
    def testing(self, testing):
        """Sets the testing of this IssuePassDetailsVo.

        统计测试中的需求

        :param testing: The testing of this IssuePassDetailsVo.
        :type testing: int
        """
        self._testing = testing

    @property
    def finished(self):
        """Gets the finished of this IssuePassDetailsVo.

        统计已完成的需求

        :return: The finished of this IssuePassDetailsVo.
        :rtype: int
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this IssuePassDetailsVo.

        统计已完成的需求

        :param finished: The finished of this IssuePassDetailsVo.
        :type finished: int
        """
        self._finished = finished

    @property
    def not_tested(self):
        """Gets the not_tested of this IssuePassDetailsVo.

        统计未完成的需求

        :return: The not_tested of this IssuePassDetailsVo.
        :rtype: int
        """
        return self._not_tested

    @not_tested.setter
    def not_tested(self, not_tested):
        """Sets the not_tested of this IssuePassDetailsVo.

        统计未完成的需求

        :param not_tested: The not_tested of this IssuePassDetailsVo.
        :type not_tested: int
        """
        self._not_tested = not_tested

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
        if not isinstance(other, IssuePassDetailsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
