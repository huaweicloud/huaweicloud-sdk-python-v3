# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlansResponseDesignStage:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'case_count': 'int',
        'issue_count': 'int',
        'issue_covered_count': 'str'
    }

    attribute_map = {
        'case_count': 'case_count',
        'issue_count': 'issue_count',
        'issue_covered_count': 'issue_covered_count'
    }

    def __init__(self, case_count=None, issue_count=None, issue_covered_count=None):
        """ShowPlansResponseDesignStage - a model defined in huaweicloud sdk"""
        
        

        self._case_count = None
        self._issue_count = None
        self._issue_covered_count = None
        self.discriminator = None

        if case_count is not None:
            self.case_count = case_count
        if issue_count is not None:
            self.issue_count = issue_count
        if issue_covered_count is not None:
            self.issue_covered_count = issue_covered_count

    @property
    def case_count(self):
        """Gets the case_count of this ShowPlansResponseDesignStage.

        用例个数

        :return: The case_count of this ShowPlansResponseDesignStage.
        :rtype: int
        """
        return self._case_count

    @case_count.setter
    def case_count(self, case_count):
        """Sets the case_count of this ShowPlansResponseDesignStage.

        用例个数

        :param case_count: The case_count of this ShowPlansResponseDesignStage.
        :type: int
        """
        self._case_count = case_count

    @property
    def issue_count(self):
        """Gets the issue_count of this ShowPlansResponseDesignStage.

        需求个数

        :return: The issue_count of this ShowPlansResponseDesignStage.
        :rtype: int
        """
        return self._issue_count

    @issue_count.setter
    def issue_count(self, issue_count):
        """Sets the issue_count of this ShowPlansResponseDesignStage.

        需求个数

        :param issue_count: The issue_count of this ShowPlansResponseDesignStage.
        :type: int
        """
        self._issue_count = issue_count

    @property
    def issue_covered_count(self):
        """Gets the issue_covered_count of this ShowPlansResponseDesignStage.

        已被用例关联的需求个数

        :return: The issue_covered_count of this ShowPlansResponseDesignStage.
        :rtype: str
        """
        return self._issue_covered_count

    @issue_covered_count.setter
    def issue_covered_count(self, issue_covered_count):
        """Sets the issue_covered_count of this ShowPlansResponseDesignStage.

        已被用例关联的需求个数

        :param issue_covered_count: The issue_covered_count of this ShowPlansResponseDesignStage.
        :type: str
        """
        self._issue_covered_count = issue_covered_count

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
        if not isinstance(other, ShowPlansResponseDesignStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
