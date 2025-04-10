# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlanExecLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'plan_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'plan_id': 'plan_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, plan_id=None, limit=None, offset=None):
        r"""ListPlanExecLogsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param plan_id: 计划ID
        :type plan_id: str
        :param limit: 查询条数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._plan_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.plan_id = plan_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListPlanExecLogsRequest.

        集群ID

        :return: The cluster_id of this ListPlanExecLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListPlanExecLogsRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListPlanExecLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this ListPlanExecLogsRequest.

        计划ID

        :return: The plan_id of this ListPlanExecLogsRequest.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this ListPlanExecLogsRequest.

        计划ID

        :param plan_id: The plan_id of this ListPlanExecLogsRequest.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPlanExecLogsRequest.

        查询条数

        :return: The limit of this ListPlanExecLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPlanExecLogsRequest.

        查询条数

        :param limit: The limit of this ListPlanExecLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPlanExecLogsRequest.

        偏移量

        :return: The offset of this ListPlanExecLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPlanExecLogsRequest.

        偏移量

        :param offset: The offset of this ListPlanExecLogsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPlanExecLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
