# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryTaskCompletionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'type': 'type'
    }

    def __init__(self, workspace=None, type=None):
        """ListFactoryTaskCompletionRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID
        :type workspace: str
        :param type: 查询任务的类型，默认为all，查询所有任务。 类型有：Dummy、CDM Job、MRS Hive SQL、MRS Spark SQL、MRS Impala SQL、DLI SQL、DLI Spark、Python、DWS SQL、Shell、MRS ClickHouse、MRS HetuEngine
        :type type: str
        """
        
        

        self._workspace = None
        self._type = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if type is not None:
            self.type = type

    @property
    def workspace(self):
        """Gets the workspace of this ListFactoryTaskCompletionRequest.

        工作空间ID

        :return: The workspace of this ListFactoryTaskCompletionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListFactoryTaskCompletionRequest.

        工作空间ID

        :param workspace: The workspace of this ListFactoryTaskCompletionRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def type(self):
        """Gets the type of this ListFactoryTaskCompletionRequest.

        查询任务的类型，默认为all，查询所有任务。 类型有：Dummy、CDM Job、MRS Hive SQL、MRS Spark SQL、MRS Impala SQL、DLI SQL、DLI Spark、Python、DWS SQL、Shell、MRS ClickHouse、MRS HetuEngine

        :return: The type of this ListFactoryTaskCompletionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListFactoryTaskCompletionRequest.

        查询任务的类型，默认为all，查询所有任务。 类型有：Dummy、CDM Job、MRS Hive SQL、MRS Spark SQL、MRS Impala SQL、DLI SQL、DLI Spark、Python、DWS SQL、Shell、MRS ClickHouse、MRS HetuEngine

        :param type: The type of this ListFactoryTaskCompletionRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListFactoryTaskCompletionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
