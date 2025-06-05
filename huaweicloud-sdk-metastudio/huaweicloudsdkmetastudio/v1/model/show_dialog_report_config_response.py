# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDialogReportConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'obs_bucket_name': 'str',
        'obs_endpoint': 'str',
        'enable_dialog_report': 'bool',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_endpoint': 'obs_endpoint',
        'enable_dialog_report': 'enable_dialog_report',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, project_id=None, obs_bucket_name=None, obs_endpoint=None, enable_dialog_report=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowDialogReportConfigResponse

        The model defined in huaweicloud sdk

        :param project_id: 租户ID。
        :type project_id: str
        :param obs_bucket_name: **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及
        :type obs_bucket_name: str
        :param obs_endpoint: **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及
        :type obs_endpoint: str
        :param enable_dialog_report: 对话结果上报开关
        :type enable_dialog_report: bool
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowDialogReportConfigResponse, self).__init__()

        self._project_id = None
        self._obs_bucket_name = None
        self._obs_endpoint = None
        self._enable_dialog_report = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if obs_endpoint is not None:
            self.obs_endpoint = obs_endpoint
        if enable_dialog_report is not None:
            self.enable_dialog_report = enable_dialog_report
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowDialogReportConfigResponse.

        租户ID。

        :return: The project_id of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowDialogReportConfigResponse.

        租户ID。

        :param project_id: The project_id of this ShowDialogReportConfigResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ShowDialogReportConfigResponse.

        **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :return: The obs_bucket_name of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ShowDialogReportConfigResponse.

        **参数解释**： 接收对话结果上报的obs桶名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :param obs_bucket_name: The obs_bucket_name of this ShowDialogReportConfigResponse.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_endpoint(self):
        r"""Gets the obs_endpoint of this ShowDialogReportConfigResponse.

        **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :return: The obs_endpoint of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._obs_endpoint

    @obs_endpoint.setter
    def obs_endpoint(self, obs_endpoint):
        r"""Sets the obs_endpoint of this ShowDialogReportConfigResponse.

        **参数解释**： 接收对话结果上报的obs终端节点。 **约束限制**： 需要为obs合法终端节点。 **取值范围**： 字符长度1-64 **默认取值**： 不涉及

        :param obs_endpoint: The obs_endpoint of this ShowDialogReportConfigResponse.
        :type obs_endpoint: str
        """
        self._obs_endpoint = obs_endpoint

    @property
    def enable_dialog_report(self):
        r"""Gets the enable_dialog_report of this ShowDialogReportConfigResponse.

        对话结果上报开关

        :return: The enable_dialog_report of this ShowDialogReportConfigResponse.
        :rtype: bool
        """
        return self._enable_dialog_report

    @enable_dialog_report.setter
    def enable_dialog_report(self, enable_dialog_report):
        r"""Sets the enable_dialog_report of this ShowDialogReportConfigResponse.

        对话结果上报开关

        :param enable_dialog_report: The enable_dialog_report of this ShowDialogReportConfigResponse.
        :type enable_dialog_report: bool
        """
        self._enable_dialog_report = enable_dialog_report

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDialogReportConfigResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDialogReportConfigResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowDialogReportConfigResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowDialogReportConfigResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowDialogReportConfigResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowDialogReportConfigResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowDialogReportConfigResponse.

        :return: The x_request_id of this ShowDialogReportConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowDialogReportConfigResponse.

        :param x_request_id: The x_request_id of this ShowDialogReportConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowDialogReportConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
