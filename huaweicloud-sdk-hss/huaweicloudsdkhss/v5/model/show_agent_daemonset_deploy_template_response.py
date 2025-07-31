# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentDaemonsetDeployTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_default': 'bool',
        'runtime_info': 'list[RuntimeRequestBody]',
        'schedule_info': 'DeployTemplateInfoScheduleInfo'
    }

    attribute_map = {
        'is_default': 'is_default',
        'runtime_info': 'runtime_info',
        'schedule_info': 'schedule_info'
    }

    def __init__(self, is_default=None, runtime_info=None, schedule_info=None):
        r"""ShowAgentDaemonsetDeployTemplateResponse

        The model defined in huaweicloud sdk

        :param is_default: 是否默认模板
        :type is_default: bool
        :param runtime_info: 容器运行时配置
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        :param schedule_info: 
        :type schedule_info: :class:`huaweicloudsdkhss.v5.DeployTemplateInfoScheduleInfo`
        """
        
        super(ShowAgentDaemonsetDeployTemplateResponse, self).__init__()

        self._is_default = None
        self._runtime_info = None
        self._schedule_info = None
        self.discriminator = None

        if is_default is not None:
            self.is_default = is_default
        if runtime_info is not None:
            self.runtime_info = runtime_info
        if schedule_info is not None:
            self.schedule_info = schedule_info

    @property
    def is_default(self):
        r"""Gets the is_default of this ShowAgentDaemonsetDeployTemplateResponse.

        是否默认模板

        :return: The is_default of this ShowAgentDaemonsetDeployTemplateResponse.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this ShowAgentDaemonsetDeployTemplateResponse.

        是否默认模板

        :param is_default: The is_default of this ShowAgentDaemonsetDeployTemplateResponse.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def runtime_info(self):
        r"""Gets the runtime_info of this ShowAgentDaemonsetDeployTemplateResponse.

        容器运行时配置

        :return: The runtime_info of this ShowAgentDaemonsetDeployTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        return self._runtime_info

    @runtime_info.setter
    def runtime_info(self, runtime_info):
        r"""Sets the runtime_info of this ShowAgentDaemonsetDeployTemplateResponse.

        容器运行时配置

        :param runtime_info: The runtime_info of this ShowAgentDaemonsetDeployTemplateResponse.
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        self._runtime_info = runtime_info

    @property
    def schedule_info(self):
        r"""Gets the schedule_info of this ShowAgentDaemonsetDeployTemplateResponse.

        :return: The schedule_info of this ShowAgentDaemonsetDeployTemplateResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.DeployTemplateInfoScheduleInfo`
        """
        return self._schedule_info

    @schedule_info.setter
    def schedule_info(self, schedule_info):
        r"""Sets the schedule_info of this ShowAgentDaemonsetDeployTemplateResponse.

        :param schedule_info: The schedule_info of this ShowAgentDaemonsetDeployTemplateResponse.
        :type schedule_info: :class:`huaweicloudsdkhss.v5.DeployTemplateInfoScheduleInfo`
        """
        self._schedule_info = schedule_info

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
        if not isinstance(other, ShowAgentDaemonsetDeployTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
