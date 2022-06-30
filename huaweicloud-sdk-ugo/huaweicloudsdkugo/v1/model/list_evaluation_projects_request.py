# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEvaluationProjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'evaluation_project_name': 'str',
        'evaluation_project_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'evaluation_project_name': 'evaluation_project_name',
        'evaluation_project_status': 'evaluation_project_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, evaluation_project_name=None, evaluation_project_status=None, offset=None, limit=None):
        """ListEvaluationProjectsRequest

        The model defined in huaweicloud sdk

        :param evaluation_project_name: 评估项目名称（模糊搜索）。
        :type evaluation_project_name: str
        :param evaluation_project_status: 评估项目状态。
        :type evaluation_project_status: str
        :param offset: 分页查询的偏移量。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._evaluation_project_name = None
        self._evaluation_project_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if evaluation_project_name is not None:
            self.evaluation_project_name = evaluation_project_name
        if evaluation_project_status is not None:
            self.evaluation_project_status = evaluation_project_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this ListEvaluationProjectsRequest.

        评估项目名称（模糊搜索）。

        :return: The evaluation_project_name of this ListEvaluationProjectsRequest.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this ListEvaluationProjectsRequest.

        评估项目名称（模糊搜索）。

        :param evaluation_project_name: The evaluation_project_name of this ListEvaluationProjectsRequest.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def evaluation_project_status(self):
        """Gets the evaluation_project_status of this ListEvaluationProjectsRequest.

        评估项目状态。

        :return: The evaluation_project_status of this ListEvaluationProjectsRequest.
        :rtype: str
        """
        return self._evaluation_project_status

    @evaluation_project_status.setter
    def evaluation_project_status(self, evaluation_project_status):
        """Sets the evaluation_project_status of this ListEvaluationProjectsRequest.

        评估项目状态。

        :param evaluation_project_status: The evaluation_project_status of this ListEvaluationProjectsRequest.
        :type evaluation_project_status: str
        """
        self._evaluation_project_status = evaluation_project_status

    @property
    def offset(self):
        """Gets the offset of this ListEvaluationProjectsRequest.

        分页查询的偏移量。

        :return: The offset of this ListEvaluationProjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEvaluationProjectsRequest.

        分页查询的偏移量。

        :param offset: The offset of this ListEvaluationProjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEvaluationProjectsRequest.

        每页显示的条目数量。

        :return: The limit of this ListEvaluationProjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEvaluationProjectsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListEvaluationProjectsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEvaluationProjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
