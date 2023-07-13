# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportWorkflowResponse(SdkResponse):

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
        'import_workflow_status': 'str',
        'import_app_results': 'list[ImportAppRsp]'
    }

    attribute_map = {
        'id': 'id',
        'import_workflow_status': 'import_workflow_status',
        'import_app_results': 'import_app_results'
    }

    def __init__(self, id=None, import_workflow_status=None, import_app_results=None):
        """ImportWorkflowResponse

        The model defined in huaweicloud sdk

        :param id: 流程ID
        :type id: str
        :param import_workflow_status: 导入流程结果状态, 包括以下状态：IMPORT_SUCCESS,IMPORT_FAIL
        :type import_workflow_status: str
        :param import_app_results: 导入应用详情
        :type import_app_results: list[:class:`huaweicloudsdkeihealth.v1.ImportAppRsp`]
        """
        
        super(ImportWorkflowResponse, self).__init__()

        self._id = None
        self._import_workflow_status = None
        self._import_app_results = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if import_workflow_status is not None:
            self.import_workflow_status = import_workflow_status
        if import_app_results is not None:
            self.import_app_results = import_app_results

    @property
    def id(self):
        """Gets the id of this ImportWorkflowResponse.

        流程ID

        :return: The id of this ImportWorkflowResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportWorkflowResponse.

        流程ID

        :param id: The id of this ImportWorkflowResponse.
        :type id: str
        """
        self._id = id

    @property
    def import_workflow_status(self):
        """Gets the import_workflow_status of this ImportWorkflowResponse.

        导入流程结果状态, 包括以下状态：IMPORT_SUCCESS,IMPORT_FAIL

        :return: The import_workflow_status of this ImportWorkflowResponse.
        :rtype: str
        """
        return self._import_workflow_status

    @import_workflow_status.setter
    def import_workflow_status(self, import_workflow_status):
        """Sets the import_workflow_status of this ImportWorkflowResponse.

        导入流程结果状态, 包括以下状态：IMPORT_SUCCESS,IMPORT_FAIL

        :param import_workflow_status: The import_workflow_status of this ImportWorkflowResponse.
        :type import_workflow_status: str
        """
        self._import_workflow_status = import_workflow_status

    @property
    def import_app_results(self):
        """Gets the import_app_results of this ImportWorkflowResponse.

        导入应用详情

        :return: The import_app_results of this ImportWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ImportAppRsp`]
        """
        return self._import_app_results

    @import_app_results.setter
    def import_app_results(self, import_app_results):
        """Sets the import_app_results of this ImportWorkflowResponse.

        导入应用详情

        :param import_app_results: The import_app_results of this ImportWorkflowResponse.
        :type import_app_results: list[:class:`huaweicloudsdkeihealth.v1.ImportAppRsp`]
        """
        self._import_app_results = import_app_results

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
        if not isinstance(other, ImportWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
