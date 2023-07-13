# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportWorkflowReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'source_workflow_id': 'str',
        'destination_workflow_name': 'str',
        'destination_workflow_version': 'str'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'source_workflow_id': 'source_workflow_id',
        'destination_workflow_name': 'destination_workflow_name',
        'destination_workflow_version': 'destination_workflow_version'
    }

    def __init__(self, source_project_id=None, source_workflow_id=None, destination_workflow_name=None, destination_workflow_version=None):
        """ImportWorkflowReq

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_workflow_id: 源流程id
        :type source_workflow_id: str
        :param destination_workflow_name: 目标流程名称 取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。
        :type destination_workflow_name: str
        :param destination_workflow_version: 目标流程版本 取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。
        :type destination_workflow_version: str
        """
        
        

        self._source_project_id = None
        self._source_workflow_id = None
        self._destination_workflow_name = None
        self._destination_workflow_version = None
        self.discriminator = None

        self.source_project_id = source_project_id
        self.source_workflow_id = source_workflow_id
        self.destination_workflow_name = destination_workflow_name
        self.destination_workflow_version = destination_workflow_version

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ImportWorkflowReq.

        源项目id

        :return: The source_project_id of this ImportWorkflowReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ImportWorkflowReq.

        源项目id

        :param source_project_id: The source_project_id of this ImportWorkflowReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_workflow_id(self):
        """Gets the source_workflow_id of this ImportWorkflowReq.

        源流程id

        :return: The source_workflow_id of this ImportWorkflowReq.
        :rtype: str
        """
        return self._source_workflow_id

    @source_workflow_id.setter
    def source_workflow_id(self, source_workflow_id):
        """Sets the source_workflow_id of this ImportWorkflowReq.

        源流程id

        :param source_workflow_id: The source_workflow_id of this ImportWorkflowReq.
        :type source_workflow_id: str
        """
        self._source_workflow_id = source_workflow_id

    @property
    def destination_workflow_name(self):
        """Gets the destination_workflow_name of this ImportWorkflowReq.

        目标流程名称 取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。

        :return: The destination_workflow_name of this ImportWorkflowReq.
        :rtype: str
        """
        return self._destination_workflow_name

    @destination_workflow_name.setter
    def destination_workflow_name(self, destination_workflow_name):
        """Sets the destination_workflow_name of this ImportWorkflowReq.

        目标流程名称 取值范围[1,56]，允许大小写字母、数字、以及特殊字符中划线(-)和下划线(_)。

        :param destination_workflow_name: The destination_workflow_name of this ImportWorkflowReq.
        :type destination_workflow_name: str
        """
        self._destination_workflow_name = destination_workflow_name

    @property
    def destination_workflow_version(self):
        """Gets the destination_workflow_version of this ImportWorkflowReq.

        目标流程版本 取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :return: The destination_workflow_version of this ImportWorkflowReq.
        :rtype: str
        """
        return self._destination_workflow_version

    @destination_workflow_version.setter
    def destination_workflow_version(self, destination_workflow_version):
        """Sets the destination_workflow_version of this ImportWorkflowReq.

        目标流程版本 取值范围[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :param destination_workflow_version: The destination_workflow_version of this ImportWorkflowReq.
        :type destination_workflow_version: str
        """
        self._destination_workflow_version = destination_workflow_version

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
        if not isinstance(other, ImportWorkflowReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
