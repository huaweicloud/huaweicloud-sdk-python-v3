# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowStepExecutionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'order': 'str',
        'sort_by': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'limit': 'limit',
        'offset': 'offset',
        'order': 'order',
        'sort_by': 'sort_by'
    }

    def __init__(self, workflow_id=None, limit=None, offset=None, order=None, sort_by=None):
        r"""ListWorkflowStepExecutionRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流的ID。
        :type workflow_id: str
        :param limit: 返回的数据条目数。
        :type limit: int
        :param offset: 数据条目偏移量。
        :type offset: int
        :param order: instance order
        :type order: str
        :param sort_by: 排序依据字段，例如sort_by&#x3D;create_time，则表示以条目的创建时间进行排序。
        :type sort_by: str
        """
        
        

        self._workflow_id = None
        self._limit = None
        self._offset = None
        self._order = None
        self._sort_by = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ListWorkflowStepExecutionRequest.

        工作流的ID。

        :return: The workflow_id of this ListWorkflowStepExecutionRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ListWorkflowStepExecutionRequest.

        工作流的ID。

        :param workflow_id: The workflow_id of this ListWorkflowStepExecutionRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkflowStepExecutionRequest.

        返回的数据条目数。

        :return: The limit of this ListWorkflowStepExecutionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkflowStepExecutionRequest.

        返回的数据条目数。

        :param limit: The limit of this ListWorkflowStepExecutionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkflowStepExecutionRequest.

        数据条目偏移量。

        :return: The offset of this ListWorkflowStepExecutionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkflowStepExecutionRequest.

        数据条目偏移量。

        :param offset: The offset of this ListWorkflowStepExecutionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this ListWorkflowStepExecutionRequest.

        instance order

        :return: The order of this ListWorkflowStepExecutionRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListWorkflowStepExecutionRequest.

        instance order

        :param order: The order of this ListWorkflowStepExecutionRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListWorkflowStepExecutionRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :return: The sort_by of this ListWorkflowStepExecutionRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListWorkflowStepExecutionRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :param sort_by: The sort_by of this ListWorkflowStepExecutionRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListWorkflowStepExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
