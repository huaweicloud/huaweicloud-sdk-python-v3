# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecordRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'app_id': 'str',
        'obs_addr': 'RecordObsFileAddr',
        'record_formats': 'list[str]',
        'hls_config': 'HLSRecordConfig',
        'mp4_config': 'MP4RecordConfig',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'app_id': 'app_id',
        'obs_addr': 'obs_addr',
        'record_formats': 'record_formats',
        'hls_config': 'hls_config',
        'mp4_config': 'mp4_config',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, rule_id=None, app_id=None, obs_addr=None, record_formats=None, hls_config=None, mp4_config=None, create_time=None, update_time=None, x_request_id=None):
        r"""UpdateRecordRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 规则id，由服务端返回。创建或修改规则的时候不携带
        :type rule_id: str
        :param app_id: 应用id
        :type app_id: str
        :param obs_addr: 
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        :param record_formats: 录制格式：HLS格式或者MP4格式
        :type record_formats: list[str]
        :param hls_config: 
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        :param mp4_config: 
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        :param create_time: 创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type create_time: str
        :param update_time: 更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateRecordRuleResponse, self).__init__()

        self._rule_id = None
        self._app_id = None
        self._obs_addr = None
        self._record_formats = None
        self._hls_config = None
        self._mp4_config = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if app_id is not None:
            self.app_id = app_id
        if obs_addr is not None:
            self.obs_addr = obs_addr
        if record_formats is not None:
            self.record_formats = record_formats
        if hls_config is not None:
            self.hls_config = hls_config
        if mp4_config is not None:
            self.mp4_config = mp4_config
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateRecordRuleResponse.

        规则id，由服务端返回。创建或修改规则的时候不携带

        :return: The rule_id of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateRecordRuleResponse.

        规则id，由服务端返回。创建或修改规则的时候不携带

        :param rule_id: The rule_id of this UpdateRecordRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateRecordRuleResponse.

        应用id

        :return: The app_id of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateRecordRuleResponse.

        应用id

        :param app_id: The app_id of this UpdateRecordRuleResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def obs_addr(self):
        r"""Gets the obs_addr of this UpdateRecordRuleResponse.

        :return: The obs_addr of this UpdateRecordRuleResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        r"""Sets the obs_addr of this UpdateRecordRuleResponse.

        :param obs_addr: The obs_addr of this UpdateRecordRuleResponse.
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        self._obs_addr = obs_addr

    @property
    def record_formats(self):
        r"""Gets the record_formats of this UpdateRecordRuleResponse.

        录制格式：HLS格式或者MP4格式

        :return: The record_formats of this UpdateRecordRuleResponse.
        :rtype: list[str]
        """
        return self._record_formats

    @record_formats.setter
    def record_formats(self, record_formats):
        r"""Sets the record_formats of this UpdateRecordRuleResponse.

        录制格式：HLS格式或者MP4格式

        :param record_formats: The record_formats of this UpdateRecordRuleResponse.
        :type record_formats: list[str]
        """
        self._record_formats = record_formats

    @property
    def hls_config(self):
        r"""Gets the hls_config of this UpdateRecordRuleResponse.

        :return: The hls_config of this UpdateRecordRuleResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        return self._hls_config

    @hls_config.setter
    def hls_config(self, hls_config):
        r"""Sets the hls_config of this UpdateRecordRuleResponse.

        :param hls_config: The hls_config of this UpdateRecordRuleResponse.
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        self._hls_config = hls_config

    @property
    def mp4_config(self):
        r"""Gets the mp4_config of this UpdateRecordRuleResponse.

        :return: The mp4_config of this UpdateRecordRuleResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        return self._mp4_config

    @mp4_config.setter
    def mp4_config(self, mp4_config):
        r"""Sets the mp4_config of this UpdateRecordRuleResponse.

        :param mp4_config: The mp4_config of this UpdateRecordRuleResponse.
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        self._mp4_config = mp4_config

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateRecordRuleResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The create_time of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateRecordRuleResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param create_time: The create_time of this UpdateRecordRuleResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateRecordRuleResponse.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateRecordRuleResponse.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this UpdateRecordRuleResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateRecordRuleResponse.

        :return: The x_request_id of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateRecordRuleResponse.

        :param x_request_id: The x_request_id of this UpdateRecordRuleResponse.
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
        if not isinstance(other, UpdateRecordRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
