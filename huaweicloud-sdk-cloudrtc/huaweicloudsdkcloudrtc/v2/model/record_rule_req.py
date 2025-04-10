# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_addr': 'RecordObsFileAddr',
        'record_formats': 'list[str]',
        'hls_config': 'HLSRecordConfig',
        'mp4_config': 'MP4RecordConfig'
    }

    attribute_map = {
        'obs_addr': 'obs_addr',
        'record_formats': 'record_formats',
        'hls_config': 'hls_config',
        'mp4_config': 'mp4_config'
    }

    def __init__(self, obs_addr=None, record_formats=None, hls_config=None, mp4_config=None):
        r"""RecordRuleReq

        The model defined in huaweicloud sdk

        :param obs_addr: 
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        :param record_formats:  录制格式：支持HLS格式和MP4格式（HLS和MP4为大写）。   - 若配置HLS则必须携带HLSRecordConfig参数  - 若配置MP4则需要携带MP4RecordConfig 
        :type record_formats: list[str]
        :param hls_config: 
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        :param mp4_config: 
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        
        

        self._obs_addr = None
        self._record_formats = None
        self._hls_config = None
        self._mp4_config = None
        self.discriminator = None

        self.obs_addr = obs_addr
        self.record_formats = record_formats
        if hls_config is not None:
            self.hls_config = hls_config
        if mp4_config is not None:
            self.mp4_config = mp4_config

    @property
    def obs_addr(self):
        r"""Gets the obs_addr of this RecordRuleReq.

        :return: The obs_addr of this RecordRuleReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        r"""Sets the obs_addr of this RecordRuleReq.

        :param obs_addr: The obs_addr of this RecordRuleReq.
        :type obs_addr: :class:`huaweicloudsdkcloudrtc.v2.RecordObsFileAddr`
        """
        self._obs_addr = obs_addr

    @property
    def record_formats(self):
        r"""Gets the record_formats of this RecordRuleReq.

         录制格式：支持HLS格式和MP4格式（HLS和MP4为大写）。   - 若配置HLS则必须携带HLSRecordConfig参数  - 若配置MP4则需要携带MP4RecordConfig 

        :return: The record_formats of this RecordRuleReq.
        :rtype: list[str]
        """
        return self._record_formats

    @record_formats.setter
    def record_formats(self, record_formats):
        r"""Sets the record_formats of this RecordRuleReq.

         录制格式：支持HLS格式和MP4格式（HLS和MP4为大写）。   - 若配置HLS则必须携带HLSRecordConfig参数  - 若配置MP4则需要携带MP4RecordConfig 

        :param record_formats: The record_formats of this RecordRuleReq.
        :type record_formats: list[str]
        """
        self._record_formats = record_formats

    @property
    def hls_config(self):
        r"""Gets the hls_config of this RecordRuleReq.

        :return: The hls_config of this RecordRuleReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        return self._hls_config

    @hls_config.setter
    def hls_config(self, hls_config):
        r"""Sets the hls_config of this RecordRuleReq.

        :param hls_config: The hls_config of this RecordRuleReq.
        :type hls_config: :class:`huaweicloudsdkcloudrtc.v2.HLSRecordConfig`
        """
        self._hls_config = hls_config

    @property
    def mp4_config(self):
        r"""Gets the mp4_config of this RecordRuleReq.

        :return: The mp4_config of this RecordRuleReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        return self._mp4_config

    @mp4_config.setter
    def mp4_config(self, mp4_config):
        r"""Sets the mp4_config of this RecordRuleReq.

        :param mp4_config: The mp4_config of this RecordRuleReq.
        :type mp4_config: :class:`huaweicloudsdkcloudrtc.v2.MP4RecordConfig`
        """
        self._mp4_config = mp4_config

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
        if not isinstance(other, RecordRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
