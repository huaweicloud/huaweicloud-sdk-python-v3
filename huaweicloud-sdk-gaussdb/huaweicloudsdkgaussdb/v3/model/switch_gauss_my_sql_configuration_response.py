# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchGaussMySqlConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'param_group_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'param_group_name': 'param_group_name'
    }

    def __init__(self, job_id=None, param_group_name=None):
        r"""SwitchGaussMySqlConfigurationResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：  应用参数模板的任务ID。  **取值范围**：  不涉及。
        :type job_id: str
        :param param_group_name: **参数解释**：  参数模板的名称。  **取值范围**：  支持Default-TaurusDB V2.0和用户自定义参数模板，其中Default-TaurusDB V2.0表示TaurusDB系统默认参数模板。
        :type param_group_name: str
        """
        
        super().__init__()

        self._job_id = None
        self._param_group_name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if param_group_name is not None:
            self.param_group_name = param_group_name

    @property
    def job_id(self):
        r"""Gets the job_id of this SwitchGaussMySqlConfigurationResponse.

        **参数解释**：  应用参数模板的任务ID。  **取值范围**：  不涉及。

        :return: The job_id of this SwitchGaussMySqlConfigurationResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SwitchGaussMySqlConfigurationResponse.

        **参数解释**：  应用参数模板的任务ID。  **取值范围**：  不涉及。

        :param job_id: The job_id of this SwitchGaussMySqlConfigurationResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def param_group_name(self):
        r"""Gets the param_group_name of this SwitchGaussMySqlConfigurationResponse.

        **参数解释**：  参数模板的名称。  **取值范围**：  支持Default-TaurusDB V2.0和用户自定义参数模板，其中Default-TaurusDB V2.0表示TaurusDB系统默认参数模板。

        :return: The param_group_name of this SwitchGaussMySqlConfigurationResponse.
        :rtype: str
        """
        return self._param_group_name

    @param_group_name.setter
    def param_group_name(self, param_group_name):
        r"""Sets the param_group_name of this SwitchGaussMySqlConfigurationResponse.

        **参数解释**：  参数模板的名称。  **取值范围**：  支持Default-TaurusDB V2.0和用户自定义参数模板，其中Default-TaurusDB V2.0表示TaurusDB系统默认参数模板。

        :param param_group_name: The param_group_name of this SwitchGaussMySqlConfigurationResponse.
        :type param_group_name: str
        """
        self._param_group_name = param_group_name

    def to_dict(self):
        import warnings
        warnings.warn("SwitchGaussMySqlConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SwitchGaussMySqlConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
