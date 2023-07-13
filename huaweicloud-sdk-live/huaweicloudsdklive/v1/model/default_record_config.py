# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultRecordConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_format': 'list[VideoFormatVar]',
        'obs_addr': 'RecordObsFileAddr',
        'hls_config': 'HLSRecordConfig',
        'flv_config': 'FLVRecordConfig',
        'mp4_config': 'MP4RecordConfig'
    }

    attribute_map = {
        'record_format': 'record_format',
        'obs_addr': 'obs_addr',
        'hls_config': 'hls_config',
        'flv_config': 'flv_config',
        'mp4_config': 'mp4_config'
    }

    def __init__(self, record_format=None, obs_addr=None, hls_config=None, flv_config=None, mp4_config=None):
        """DefaultRecordConfig

        The model defined in huaweicloud sdk

        :param record_format: 录制格式，当前支持：FLV，HLS，MP4三种格式，设置格式时必须使用大写字母
        :type record_format: list[:class:`huaweicloudsdklive.v1.VideoFormatVar`]
        :param obs_addr: 
        :type obs_addr: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        :param hls_config: 
        :type hls_config: :class:`huaweicloudsdklive.v1.HLSRecordConfig`
        :param flv_config: 
        :type flv_config: :class:`huaweicloudsdklive.v1.FLVRecordConfig`
        :param mp4_config: 
        :type mp4_config: :class:`huaweicloudsdklive.v1.MP4RecordConfig`
        """
        
        

        self._record_format = None
        self._obs_addr = None
        self._hls_config = None
        self._flv_config = None
        self._mp4_config = None
        self.discriminator = None

        self.record_format = record_format
        self.obs_addr = obs_addr
        if hls_config is not None:
            self.hls_config = hls_config
        if flv_config is not None:
            self.flv_config = flv_config
        if mp4_config is not None:
            self.mp4_config = mp4_config

    @property
    def record_format(self):
        """Gets the record_format of this DefaultRecordConfig.

        录制格式，当前支持：FLV，HLS，MP4三种格式，设置格式时必须使用大写字母

        :return: The record_format of this DefaultRecordConfig.
        :rtype: list[:class:`huaweicloudsdklive.v1.VideoFormatVar`]
        """
        return self._record_format

    @record_format.setter
    def record_format(self, record_format):
        """Sets the record_format of this DefaultRecordConfig.

        录制格式，当前支持：FLV，HLS，MP4三种格式，设置格式时必须使用大写字母

        :param record_format: The record_format of this DefaultRecordConfig.
        :type record_format: list[:class:`huaweicloudsdklive.v1.VideoFormatVar`]
        """
        self._record_format = record_format

    @property
    def obs_addr(self):
        """Gets the obs_addr of this DefaultRecordConfig.

        :return: The obs_addr of this DefaultRecordConfig.
        :rtype: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        """Sets the obs_addr of this DefaultRecordConfig.

        :param obs_addr: The obs_addr of this DefaultRecordConfig.
        :type obs_addr: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        """
        self._obs_addr = obs_addr

    @property
    def hls_config(self):
        """Gets the hls_config of this DefaultRecordConfig.

        :return: The hls_config of this DefaultRecordConfig.
        :rtype: :class:`huaweicloudsdklive.v1.HLSRecordConfig`
        """
        return self._hls_config

    @hls_config.setter
    def hls_config(self, hls_config):
        """Sets the hls_config of this DefaultRecordConfig.

        :param hls_config: The hls_config of this DefaultRecordConfig.
        :type hls_config: :class:`huaweicloudsdklive.v1.HLSRecordConfig`
        """
        self._hls_config = hls_config

    @property
    def flv_config(self):
        """Gets the flv_config of this DefaultRecordConfig.

        :return: The flv_config of this DefaultRecordConfig.
        :rtype: :class:`huaweicloudsdklive.v1.FLVRecordConfig`
        """
        return self._flv_config

    @flv_config.setter
    def flv_config(self, flv_config):
        """Sets the flv_config of this DefaultRecordConfig.

        :param flv_config: The flv_config of this DefaultRecordConfig.
        :type flv_config: :class:`huaweicloudsdklive.v1.FLVRecordConfig`
        """
        self._flv_config = flv_config

    @property
    def mp4_config(self):
        """Gets the mp4_config of this DefaultRecordConfig.

        :return: The mp4_config of this DefaultRecordConfig.
        :rtype: :class:`huaweicloudsdklive.v1.MP4RecordConfig`
        """
        return self._mp4_config

    @mp4_config.setter
    def mp4_config(self, mp4_config):
        """Sets the mp4_config of this DefaultRecordConfig.

        :param mp4_config: The mp4_config of this DefaultRecordConfig.
        :type mp4_config: :class:`huaweicloudsdklive.v1.MP4RecordConfig`
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
        if not isinstance(other, DefaultRecordConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
