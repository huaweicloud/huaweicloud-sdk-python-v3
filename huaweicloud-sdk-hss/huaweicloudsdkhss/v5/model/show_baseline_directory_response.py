# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineDirectoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_condition': 'SecurityCheckTaskCondition',
        'baseline_directory_list': 'list[ShowBaselineDirectoryInfo]',
        'pwd_directory_list': 'list[ShowPwdDirectoryInfo]'
    }

    attribute_map = {
        'task_condition': 'task_condition',
        'baseline_directory_list': 'baseline_directory_list',
        'pwd_directory_list': 'pwd_directory_list'
    }

    def __init__(self, task_condition=None, baseline_directory_list=None, pwd_directory_list=None):
        r"""ShowBaselineDirectoryResponse

        The model defined in huaweicloud sdk

        :param task_condition: 
        :type task_condition: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        :param baseline_directory_list: **参数解释** 基线检查策略目录
        :type baseline_directory_list: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfo`]
        :param pwd_directory_list: **参数解释** 基线检查策略目录
        :type pwd_directory_list: list[:class:`huaweicloudsdkhss.v5.ShowPwdDirectoryInfo`]
        """
        
        super(ShowBaselineDirectoryResponse, self).__init__()

        self._task_condition = None
        self._baseline_directory_list = None
        self._pwd_directory_list = None
        self.discriminator = None

        if task_condition is not None:
            self.task_condition = task_condition
        if baseline_directory_list is not None:
            self.baseline_directory_list = baseline_directory_list
        if pwd_directory_list is not None:
            self.pwd_directory_list = pwd_directory_list

    @property
    def task_condition(self):
        r"""Gets the task_condition of this ShowBaselineDirectoryResponse.

        :return: The task_condition of this ShowBaselineDirectoryResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        """
        return self._task_condition

    @task_condition.setter
    def task_condition(self, task_condition):
        r"""Sets the task_condition of this ShowBaselineDirectoryResponse.

        :param task_condition: The task_condition of this ShowBaselineDirectoryResponse.
        :type task_condition: :class:`huaweicloudsdkhss.v5.SecurityCheckTaskCondition`
        """
        self._task_condition = task_condition

    @property
    def baseline_directory_list(self):
        r"""Gets the baseline_directory_list of this ShowBaselineDirectoryResponse.

        **参数解释** 基线检查策略目录

        :return: The baseline_directory_list of this ShowBaselineDirectoryResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfo`]
        """
        return self._baseline_directory_list

    @baseline_directory_list.setter
    def baseline_directory_list(self, baseline_directory_list):
        r"""Sets the baseline_directory_list of this ShowBaselineDirectoryResponse.

        **参数解释** 基线检查策略目录

        :param baseline_directory_list: The baseline_directory_list of this ShowBaselineDirectoryResponse.
        :type baseline_directory_list: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfo`]
        """
        self._baseline_directory_list = baseline_directory_list

    @property
    def pwd_directory_list(self):
        r"""Gets the pwd_directory_list of this ShowBaselineDirectoryResponse.

        **参数解释** 基线检查策略目录

        :return: The pwd_directory_list of this ShowBaselineDirectoryResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowPwdDirectoryInfo`]
        """
        return self._pwd_directory_list

    @pwd_directory_list.setter
    def pwd_directory_list(self, pwd_directory_list):
        r"""Sets the pwd_directory_list of this ShowBaselineDirectoryResponse.

        **参数解释** 基线检查策略目录

        :param pwd_directory_list: The pwd_directory_list of this ShowBaselineDirectoryResponse.
        :type pwd_directory_list: list[:class:`huaweicloudsdkhss.v5.ShowPwdDirectoryInfo`]
        """
        self._pwd_directory_list = pwd_directory_list

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
        if not isinstance(other, ShowBaselineDirectoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
