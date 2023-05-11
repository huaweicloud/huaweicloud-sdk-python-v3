# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEvaluationProjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'evaluation_projects': 'list[EvaluationProject]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'evaluation_projects': 'evaluation_projects'
    }

    def __init__(self, total_count=None, evaluation_projects=None):
        """ListEvaluationProjectsResponse

        The model defined in huaweicloud sdk

        :param total_count: 评估项目总数。
        :type total_count: int
        :param evaluation_projects: 当前页的评估项目列表。
        :type evaluation_projects: list[:class:`huaweicloudsdkugo.v1.EvaluationProject`]
        """
        
        super(ListEvaluationProjectsResponse, self).__init__()

        self._total_count = None
        self._evaluation_projects = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if evaluation_projects is not None:
            self.evaluation_projects = evaluation_projects

    @property
    def total_count(self):
        """Gets the total_count of this ListEvaluationProjectsResponse.

        评估项目总数。

        :return: The total_count of this ListEvaluationProjectsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEvaluationProjectsResponse.

        评估项目总数。

        :param total_count: The total_count of this ListEvaluationProjectsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def evaluation_projects(self):
        """Gets the evaluation_projects of this ListEvaluationProjectsResponse.

        当前页的评估项目列表。

        :return: The evaluation_projects of this ListEvaluationProjectsResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.EvaluationProject`]
        """
        return self._evaluation_projects

    @evaluation_projects.setter
    def evaluation_projects(self, evaluation_projects):
        """Sets the evaluation_projects of this ListEvaluationProjectsResponse.

        当前页的评估项目列表。

        :param evaluation_projects: The evaluation_projects of this ListEvaluationProjectsResponse.
        :type evaluation_projects: list[:class:`huaweicloudsdkugo.v1.EvaluationProject`]
        """
        self._evaluation_projects = evaluation_projects

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
        if not isinstance(other, ListEvaluationProjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
