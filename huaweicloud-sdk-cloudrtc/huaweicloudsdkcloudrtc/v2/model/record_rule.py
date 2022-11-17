# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordRule:

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
        'update_time': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'app_id': 'app_id',
        'obs_addr': 'obs_addr',
        'record_formats': 'record_formats',
        'hls_config': 'hls_config',
        'mp4_config': 'mp4_config',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, rule_id=None, app_id=None, obs_addr=None, record_formats=None, hls_config=None, mp4_config=None, create_time=None, update_time=None):
        """RecordRule

        The model defined in huaweicloud sdk

        :param rule_id: 规则id，由服务端返回。创建或修改规则的时候不携带
        :type rule_id: str
        :param app_id: 应用id
        :type app_id: str
        :param obs_addr: 
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        :param record_formats: 录制格式：hls格式或者mp4格式
        :type record_formats: list[str]
        :param hls_config: 
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        :param mp4_config: 
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        :param create_time: 创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type create_time: str
        :param update_time: 更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        """
        
        

        self._rule_id = None
        self._app_id = None
        self._obs_addr = None
        self._record_formats = None
        self._hls_config = None
        self._mp4_config = None
        self._create_time = None
        self._update_time = None
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

    @property
    def rule_id(self):
        """Gets the rule_id of this RecordRule.

        规则id，由服务端返回。创建或修改规则的时候不携带

        :return: The rule_id of this RecordRule.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this RecordRule.

        规则id，由服务端返回。创建或修改规则的时候不携带

        :param rule_id: The rule_id of this RecordRule.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def app_id(self):
        """Gets the app_id of this RecordRule.

        应用id

        :return: The app_id of this RecordRule.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RecordRule.

        应用id

        :param app_id: The app_id of this RecordRule.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def obs_addr(self):
        """Gets the obs_addr of this RecordRule.

        :return: The obs_addr of this RecordRule.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        """Sets the obs_addr of this RecordRule.

        :param obs_addr: The obs_addr of this RecordRule.
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        self._obs_addr = obs_addr

    @property
    def record_formats(self):
        """Gets the record_formats of this RecordRule.

        录制格式：hls格式或者mp4格式

        :return: The record_formats of this RecordRule.
        :rtype: list[str]
        """
        return self._record_formats

    @record_formats.setter
    def record_formats(self, record_formats):
        """Sets the record_formats of this RecordRule.

        录制格式：hls格式或者mp4格式

        :param record_formats: The record_formats of this RecordRule.
        :type record_formats: list[str]
        """
        self._record_formats = record_formats

    @property
    def hls_config(self):
        """Gets the hls_config of this RecordRule.

        :return: The hls_config of this RecordRule.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        return self._hls_config

    @hls_config.setter
    def hls_config(self, hls_config):
        """Sets the hls_config of this RecordRule.

        :param hls_config: The hls_config of this RecordRule.
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        self._hls_config = hls_config

    @property
    def mp4_config(self):
        """Gets the mp4_config of this RecordRule.

        :return: The mp4_config of this RecordRule.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        return self._mp4_config

    @mp4_config.setter
    def mp4_config(self, mp4_config):
        """Sets the mp4_config of this RecordRule.

        :param mp4_config: The mp4_config of this RecordRule.
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        self._mp4_config = mp4_config

    @property
    def create_time(self):
        """Gets the create_time of this RecordRule.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The create_time of this RecordRule.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordRule.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param create_time: The create_time of this RecordRule.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RecordRule.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this RecordRule.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RecordRule.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this RecordRule.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, RecordRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
