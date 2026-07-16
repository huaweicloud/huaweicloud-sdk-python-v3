# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowExecutionsRequest:

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
        'workspace_id': 'str',
        'limit': 'str',
        'sort_by': 'str',
        'offset': 'str',
        'labels': 'str',
        'status': 'str',
        'scene_id': 'str',
        'order': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'workspace_id': 'workspace_id',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'offset': 'offset',
        'labels': 'labels',
        'status': 'status',
        'scene_id': 'scene_id',
        'order': 'order'
    }

    def __init__(self, workflow_id=None, workspace_id=None, limit=None, sort_by=None, offset=None, labels=None, status=None, scene_id=None, order=None):
        r"""ListWorkflowExecutionsRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流的ID。
        :type workflow_id: str
        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param limit: 分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。
        :type limit: str
        :param sort_by: 排序依据字段，例如sort_by&#x3D;create_time，则表示以条目的创建时间进行排序。
        :type sort_by: str
        :param offset: 分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。
        :type offset: str
        :param labels: 执行记录标签。
        :type labels: str
        :param status: 执行记录状态。
        :type status: str
        :param scene_id: 场景ID。
        :type scene_id: str
        :param order: 排序的方式。该字段必须与sort_by同时使用。 缺省值: desc 枚举值： - asc：表示升序排列， - desc：降序排列。
        :type order: str
        """
        
        

        self._workflow_id = None
        self._workspace_id = None
        self._limit = None
        self._sort_by = None
        self._offset = None
        self._labels = None
        self._status = None
        self._scene_id = None
        self._order = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if offset is not None:
            self.offset = offset
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status
        if scene_id is not None:
            self.scene_id = scene_id
        if order is not None:
            self.order = order

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ListWorkflowExecutionsRequest.

        工作流的ID。

        :return: The workflow_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ListWorkflowExecutionsRequest.

        工作流的ID。

        :param workflow_id: The workflow_id of this ListWorkflowExecutionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListWorkflowExecutionsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListWorkflowExecutionsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ListWorkflowExecutionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkflowExecutionsRequest.

        分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。

        :return: The limit of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkflowExecutionsRequest.

        分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。

        :param limit: The limit of this ListWorkflowExecutionsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListWorkflowExecutionsRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :return: The sort_by of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListWorkflowExecutionsRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :param sort_by: The sort_by of this ListWorkflowExecutionsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkflowExecutionsRequest.

        分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。

        :return: The offset of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkflowExecutionsRequest.

        分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。

        :param offset: The offset of this ListWorkflowExecutionsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def labels(self):
        r"""Gets the labels of this ListWorkflowExecutionsRequest.

        执行记录标签。

        :return: The labels of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListWorkflowExecutionsRequest.

        执行记录标签。

        :param labels: The labels of this ListWorkflowExecutionsRequest.
        :type labels: str
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this ListWorkflowExecutionsRequest.

        执行记录状态。

        :return: The status of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWorkflowExecutionsRequest.

        执行记录状态。

        :param status: The status of this ListWorkflowExecutionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def scene_id(self):
        r"""Gets the scene_id of this ListWorkflowExecutionsRequest.

        场景ID。

        :return: The scene_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this ListWorkflowExecutionsRequest.

        场景ID。

        :param scene_id: The scene_id of this ListWorkflowExecutionsRequest.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def order(self):
        r"""Gets the order of this ListWorkflowExecutionsRequest.

        排序的方式。该字段必须与sort_by同时使用。 缺省值: desc 枚举值： - asc：表示升序排列， - desc：降序排列。

        :return: The order of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListWorkflowExecutionsRequest.

        排序的方式。该字段必须与sort_by同时使用。 缺省值: desc 枚举值： - asc：表示升序排列， - desc：降序排列。

        :param order: The order of this ListWorkflowExecutionsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListWorkflowExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
