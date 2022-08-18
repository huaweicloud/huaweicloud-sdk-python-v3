# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkFlowResponse(SdkResponse):

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
        'name': 'str',
        'description': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'workflow_urn': 'workflow_urn',
        'name': 'name',
        'description': 'description',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'created_by': 'created_by'
    }

    def __init__(self, id=None, workflow_urn=None, name=None, description=None, created_time=None, updated_time=None, created_by=None):
        """UpdateWorkFlowResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID，流程定义ID
        :type id: str
        :param workflow_urn: 函数工作流URN, 格式为： urn:fss:&lt;region_id&gt;:&lt;project_id&gt;:workflow:\\&lt;package\\&gt;:&lt;workflow_name&gt;:\\&lt;version\\&gt; 注意： package当前只支持default version当前只支持latest
        :type workflow_urn: str
        :param name: 流程定义名称
        :type name: str
        :param description: 流程定义描述
        :type description: str
        :param created_time: 流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type created_time: str
        :param updated_time: 流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type updated_time: str
        :param created_by: 流程创建者
        :type created_by: str
        """
        
        super(UpdateWorkFlowResponse, self).__init__()

        self._id = None
        self._workflow_urn = None
        self._name = None
        self._description = None
        self._created_time = None
        self._updated_time = None
        self._created_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if workflow_urn is not None:
            self.workflow_urn = workflow_urn
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this UpdateWorkFlowResponse.

        唯一标识ID，流程定义ID

        :return: The id of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateWorkFlowResponse.

        唯一标识ID，流程定义ID

        :param id: The id of this UpdateWorkFlowResponse.
        :type id: str
        """
        self._id = id

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this UpdateWorkFlowResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :return: The workflow_urn of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this UpdateWorkFlowResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :param workflow_urn: The workflow_urn of this UpdateWorkFlowResponse.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def name(self):
        """Gets the name of this UpdateWorkFlowResponse.

        流程定义名称

        :return: The name of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateWorkFlowResponse.

        流程定义名称

        :param name: The name of this UpdateWorkFlowResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateWorkFlowResponse.

        流程定义描述

        :return: The description of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateWorkFlowResponse.

        流程定义描述

        :param description: The description of this UpdateWorkFlowResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        """Gets the created_time of this UpdateWorkFlowResponse.

        流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The created_time of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateWorkFlowResponse.

        流程创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param created_time: The created_time of this UpdateWorkFlowResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this UpdateWorkFlowResponse.

        流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The updated_time of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this UpdateWorkFlowResponse.

        流程修改时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param updated_time: The updated_time of this UpdateWorkFlowResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_by(self):
        """Gets the created_by of this UpdateWorkFlowResponse.

        流程创建者

        :return: The created_by of this UpdateWorkFlowResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UpdateWorkFlowResponse.

        流程创建者

        :param created_by: The created_by of this UpdateWorkFlowResponse.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, UpdateWorkFlowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
