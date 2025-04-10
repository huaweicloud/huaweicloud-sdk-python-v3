# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueListFilterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iteration_ids': 'list[str]',
        'pi_sprints': 'list[IssueListPiFilterInfo]',
        'subject': 'str',
        'module_id': 'str',
        'status_id': 'str'
    }

    attribute_map = {
        'iteration_ids': 'iteration_ids',
        'pi_sprints': 'pi_sprints',
        'subject': 'subject',
        'module_id': 'module_id',
        'status_id': 'status_id'
    }

    def __init__(self, iteration_ids=None, pi_sprints=None, subject=None, module_id=None, status_id=None):
        r"""IssueListFilterInfo

        The model defined in huaweicloud sdk

        :param iteration_ids: 迭代id列表
        :type iteration_ids: list[str]
        :param pi_sprints: pi过滤条件
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        :param subject: 需求名
        :type subject: str
        :param module_id: 模块id
        :type module_id: str
        :param status_id: 需求状态id
        :type status_id: str
        """
        
        

        self._iteration_ids = None
        self._pi_sprints = None
        self._subject = None
        self._module_id = None
        self._status_id = None
        self.discriminator = None

        if iteration_ids is not None:
            self.iteration_ids = iteration_ids
        if pi_sprints is not None:
            self.pi_sprints = pi_sprints
        if subject is not None:
            self.subject = subject
        if module_id is not None:
            self.module_id = module_id
        if status_id is not None:
            self.status_id = status_id

    @property
    def iteration_ids(self):
        r"""Gets the iteration_ids of this IssueListFilterInfo.

        迭代id列表

        :return: The iteration_ids of this IssueListFilterInfo.
        :rtype: list[str]
        """
        return self._iteration_ids

    @iteration_ids.setter
    def iteration_ids(self, iteration_ids):
        r"""Sets the iteration_ids of this IssueListFilterInfo.

        迭代id列表

        :param iteration_ids: The iteration_ids of this IssueListFilterInfo.
        :type iteration_ids: list[str]
        """
        self._iteration_ids = iteration_ids

    @property
    def pi_sprints(self):
        r"""Gets the pi_sprints of this IssueListFilterInfo.

        pi过滤条件

        :return: The pi_sprints of this IssueListFilterInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        return self._pi_sprints

    @pi_sprints.setter
    def pi_sprints(self, pi_sprints):
        r"""Sets the pi_sprints of this IssueListFilterInfo.

        pi过滤条件

        :param pi_sprints: The pi_sprints of this IssueListFilterInfo.
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        self._pi_sprints = pi_sprints

    @property
    def subject(self):
        r"""Gets the subject of this IssueListFilterInfo.

        需求名

        :return: The subject of this IssueListFilterInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this IssueListFilterInfo.

        需求名

        :param subject: The subject of this IssueListFilterInfo.
        :type subject: str
        """
        self._subject = subject

    @property
    def module_id(self):
        r"""Gets the module_id of this IssueListFilterInfo.

        模块id

        :return: The module_id of this IssueListFilterInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this IssueListFilterInfo.

        模块id

        :param module_id: The module_id of this IssueListFilterInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def status_id(self):
        r"""Gets the status_id of this IssueListFilterInfo.

        需求状态id

        :return: The status_id of this IssueListFilterInfo.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this IssueListFilterInfo.

        需求状态id

        :param status_id: The status_id of this IssueListFilterInfo.
        :type status_id: str
        """
        self._status_id = status_id

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
        if not isinstance(other, IssueListFilterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
