# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkFlowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'workflow_urn': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'created_by': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'definition': 'WorkflowCreateBody'
    }

    attribute_map = {
        'id': 'id',
        'workflow_urn': 'workflow_urn',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'created_by': 'created_by',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'definition': 'definition'
    }

    def __init__(self, id=None, workflow_urn=None, created_time=None, updated_time=None, created_by=None, lts_group_id=None, lts_stream_id=None, definition=None):
        """ShowWorkFlowResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID，流程定义ID
        :type id: str
        :param workflow_urn: 函数工作流URN, 格式为： urn:fss:&lt;region_id&gt;:&lt;project_id&gt;:workflow:\\&lt;package\\&gt;:&lt;workflow_name&gt;:\\&lt;version\\&gt; 注意： package当前只支持default version当前只支持latest
        :type workflow_urn: str
        :param created_time: 流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type created_time: str
        :param updated_time: 流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type updated_time: str
        :param created_by: 流程创建者
        :type created_by: str
        :param lts_group_id: 快速函数流日志组ID，仅快速模式函数流且日志级别不为NONE时
        :type lts_group_id: str
        :param lts_stream_id: 快速函数流日志流ID，仅快速模式函数流且日志级别不为NONE时返回。
        :type lts_stream_id: str
        :param definition: 
        :type definition: :class:`huaweicloudsdkfunctiongraph.v2.WorkflowCreateBody`
        """
        
        super(ShowWorkFlowResponse, self).__init__()

        self._id = None
        self._workflow_urn = None
        self._created_time = None
        self._updated_time = None
        self._created_by = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._definition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if workflow_urn is not None:
            self.workflow_urn = workflow_urn
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if created_by is not None:
            self.created_by = created_by
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_stream_id is not None:
            self.lts_stream_id = lts_stream_id
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        """Gets the id of this ShowWorkFlowResponse.

        唯一标识ID，流程定义ID

        :return: The id of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowWorkFlowResponse.

        唯一标识ID，流程定义ID

        :param id: The id of this ShowWorkFlowResponse.
        :type id: str
        """
        self._id = id

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this ShowWorkFlowResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :return: The workflow_urn of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this ShowWorkFlowResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :param workflow_urn: The workflow_urn of this ShowWorkFlowResponse.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def created_time(self):
        """Gets the created_time of this ShowWorkFlowResponse.

        流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The created_time of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowWorkFlowResponse.

        流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param created_time: The created_time of this ShowWorkFlowResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowWorkFlowResponse.

        流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The updated_time of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowWorkFlowResponse.

        流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param updated_time: The updated_time of this ShowWorkFlowResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_by(self):
        """Gets the created_by of this ShowWorkFlowResponse.

        流程创建者

        :return: The created_by of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShowWorkFlowResponse.

        流程创建者

        :param created_by: The created_by of this ShowWorkFlowResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def lts_group_id(self):
        """Gets the lts_group_id of this ShowWorkFlowResponse.

        快速函数流日志组ID，仅快速模式函数流且日志级别不为NONE时

        :return: The lts_group_id of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        """Sets the lts_group_id of this ShowWorkFlowResponse.

        快速函数流日志组ID，仅快速模式函数流且日志级别不为NONE时

        :param lts_group_id: The lts_group_id of this ShowWorkFlowResponse.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        """Gets the lts_stream_id of this ShowWorkFlowResponse.

        快速函数流日志流ID，仅快速模式函数流且日志级别不为NONE时返回。

        :return: The lts_stream_id of this ShowWorkFlowResponse.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        """Sets the lts_stream_id of this ShowWorkFlowResponse.

        快速函数流日志流ID，仅快速模式函数流且日志级别不为NONE时返回。

        :param lts_stream_id: The lts_stream_id of this ShowWorkFlowResponse.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def definition(self):
        """Gets the definition of this ShowWorkFlowResponse.

        :return: The definition of this ShowWorkFlowResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.WorkflowCreateBody`
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowWorkFlowResponse.

        :param definition: The definition of this ShowWorkFlowResponse.
        :type definition: :class:`huaweicloudsdkfunctiongraph.v2.WorkflowCreateBody`
        """
        self._definition = definition

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
        if not isinstance(other, ShowWorkFlowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
