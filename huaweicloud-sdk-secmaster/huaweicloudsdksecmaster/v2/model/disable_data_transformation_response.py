# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisableDataTransformationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_transformation_id': 'str',
        'status': 'str',
        'process_status': 'str'
    }

    attribute_map = {
        'data_transformation_id': 'data_transformation_id',
        'status': 'status',
        'process_status': 'process_status'
    }

    def __init__(self, data_transformation_id=None, status=None, process_status=None):
        r"""DisableDataTransformationResponse

        The model defined in huaweicloud sdk

        :param data_transformation_id: UUID
        :type data_transformation_id: str
        :param status: **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param process_status: **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   
        :type process_status: str
        """
        
        super().__init__()

        self._data_transformation_id = None
        self._status = None
        self._process_status = None
        self.discriminator = None

        if data_transformation_id is not None:
            self.data_transformation_id = data_transformation_id
        if status is not None:
            self.status = status
        if process_status is not None:
            self.process_status = process_status

    @property
    def data_transformation_id(self):
        r"""Gets the data_transformation_id of this DisableDataTransformationResponse.

        UUID

        :return: The data_transformation_id of this DisableDataTransformationResponse.
        :rtype: str
        """
        return self._data_transformation_id

    @data_transformation_id.setter
    def data_transformation_id(self, data_transformation_id):
        r"""Sets the data_transformation_id of this DisableDataTransformationResponse.

        UUID

        :param data_transformation_id: The data_transformation_id of this DisableDataTransformationResponse.
        :type data_transformation_id: str
        """
        self._data_transformation_id = data_transformation_id

    @property
    def status(self):
        r"""Gets the status of this DisableDataTransformationResponse.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this DisableDataTransformationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DisableDataTransformationResponse.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this DisableDataTransformationResponse.
        :type status: str
        """
        self._status = status

    @property
    def process_status(self):
        r"""Gets the process_status of this DisableDataTransformationResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   

        :return: The process_status of this DisableDataTransformationResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this DisableDataTransformationResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   

        :param process_status: The process_status of this DisableDataTransformationResponse.
        :type process_status: str
        """
        self._process_status = process_status

    def to_dict(self):
        import warnings
        warnings.warn("DisableDataTransformationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, DisableDataTransformationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
