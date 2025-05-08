# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecutionInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'execution_step_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'execution_step_id': 'execution_step_id'
    }

    def __init__(self, limit=None, offset=None, execution_step_id=None):
        r"""ListExecutionInstancesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 从offset指定的下一条数据开始查询
        :type offset: int
        :param execution_step_id: 工单步骤id
        :type execution_step_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._execution_step_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if execution_step_id is not None:
            self.execution_step_id = execution_step_id

    @property
    def limit(self):
        r"""Gets the limit of this ListExecutionInstancesRequest.

        每页显示的条目数量

        :return: The limit of this ListExecutionInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExecutionInstancesRequest.

        每页显示的条目数量

        :param limit: The limit of this ListExecutionInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListExecutionInstancesRequest.

        从offset指定的下一条数据开始查询

        :return: The offset of this ListExecutionInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExecutionInstancesRequest.

        从offset指定的下一条数据开始查询

        :param offset: The offset of this ListExecutionInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def execution_step_id(self):
        r"""Gets the execution_step_id of this ListExecutionInstancesRequest.

        工单步骤id

        :return: The execution_step_id of this ListExecutionInstancesRequest.
        :rtype: str
        """
        return self._execution_step_id

    @execution_step_id.setter
    def execution_step_id(self, execution_step_id):
        r"""Sets the execution_step_id of this ListExecutionInstancesRequest.

        工单步骤id

        :param execution_step_id: The execution_step_id of this ListExecutionInstancesRequest.
        :type execution_step_id: str
        """
        self._execution_step_id = execution_step_id

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
        if not isinstance(other, ListExecutionInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
