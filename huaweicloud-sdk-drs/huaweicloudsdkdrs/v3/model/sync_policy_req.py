# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncPolicyReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'conflict_policy': 'str',
        'filter_ddl_policy': 'str',
        'ddl_trans': 'bool',
        'index_trans': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'conflict_policy': 'conflict_policy',
        'filter_ddl_policy': 'filter_ddl_policy',
        'ddl_trans': 'ddl_trans',
        'index_trans': 'index_trans'
    }

    def __init__(self, job_id=None, conflict_policy=None, filter_ddl_policy=None, ddl_trans=None, index_trans=None):
        """SyncPolicyReq - a model defined in huaweicloud sdk"""
        
        

        self._job_id = None
        self._conflict_policy = None
        self._filter_ddl_policy = None
        self._ddl_trans = None
        self._index_trans = None
        self.discriminator = None

        self.job_id = job_id
        self.conflict_policy = conflict_policy
        self.filter_ddl_policy = filter_ddl_policy
        if ddl_trans is not None:
            self.ddl_trans = ddl_trans
        if index_trans is not None:
            self.index_trans = index_trans

    @property
    def job_id(self):
        """Gets the job_id of this SyncPolicyReq.

        任务ID。

        :return: The job_id of this SyncPolicyReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SyncPolicyReq.

        任务ID。

        :param job_id: The job_id of this SyncPolicyReq.
        :type: str
        """
        self._job_id = job_id

    @property
    def conflict_policy(self):
        """Gets the conflict_policy of this SyncPolicyReq.

        冲突策略。 - ignore：忽略 - overwrite：覆盖 - stop：报错

        :return: The conflict_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        """Sets the conflict_policy of this SyncPolicyReq.

        冲突策略。 - ignore：忽略 - overwrite：覆盖 - stop：报错

        :param conflict_policy: The conflict_policy of this SyncPolicyReq.
        :type: str
        """
        self._conflict_policy = conflict_policy

    @property
    def filter_ddl_policy(self):
        """Gets the filter_ddl_policy of this SyncPolicyReq.

        过滤DDL策略。

        :return: The filter_ddl_policy of this SyncPolicyReq.
        :rtype: str
        """
        return self._filter_ddl_policy

    @filter_ddl_policy.setter
    def filter_ddl_policy(self, filter_ddl_policy):
        """Sets the filter_ddl_policy of this SyncPolicyReq.

        过滤DDL策略。

        :param filter_ddl_policy: The filter_ddl_policy of this SyncPolicyReq.
        :type: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def ddl_trans(self):
        """Gets the ddl_trans of this SyncPolicyReq.

        同步增量是否同步DDL。

        :return: The ddl_trans of this SyncPolicyReq.
        :rtype: bool
        """
        return self._ddl_trans

    @ddl_trans.setter
    def ddl_trans(self, ddl_trans):
        """Sets the ddl_trans of this SyncPolicyReq.

        同步增量是否同步DDL。

        :param ddl_trans: The ddl_trans of this SyncPolicyReq.
        :type: bool
        """
        self._ddl_trans = ddl_trans

    @property
    def index_trans(self):
        """Gets the index_trans of this SyncPolicyReq.

        同步增量是否同步索引。

        :return: The index_trans of this SyncPolicyReq.
        :rtype: bool
        """
        return self._index_trans

    @index_trans.setter
    def index_trans(self, index_trans):
        """Sets the index_trans of this SyncPolicyReq.

        同步增量是否同步索引。

        :param index_trans: The index_trans of this SyncPolicyReq.
        :type: bool
        """
        self._index_trans = index_trans

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
        if not isinstance(other, SyncPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
