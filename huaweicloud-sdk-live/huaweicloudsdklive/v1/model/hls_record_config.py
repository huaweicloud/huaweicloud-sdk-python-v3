# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HLSRecordConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_cycle': 'int',
        'record_prefix': 'str',
        'record_ts_prefix': 'str',
        'record_slice_duration': 'int',
        'record_max_duration_to_merge_file': 'int'
    }

    attribute_map = {
        'record_cycle': 'record_cycle',
        'record_prefix': 'record_prefix',
        'record_ts_prefix': 'record_ts_prefix',
        'record_slice_duration': 'record_slice_duration',
        'record_max_duration_to_merge_file': 'record_max_duration_to_merge_file'
    }

    def __init__(self, record_cycle=None, record_prefix=None, record_ts_prefix=None, record_slice_duration=None, record_max_duration_to_merge_file=None):
        """HLSRecordConfig

        The model defined in huaweicloud sdk

        :param record_cycle: 单位为秒，周期录制时长，最小1分钟（60秒），最大12小时。如果为0则整个流录制一个文件。
        :type record_cycle: int
        :param record_prefix: 录制m3u8文件含路径和文件名的前缀， 默认Record/{publish_domain}/{app}/{record_type}/{record_format}/{stream}_{file_start_time}/{stream}_{file_start_time}
        :type record_prefix: str
        :param record_ts_prefix: 录制ts文件名的前缀， 默认{file_start_time_unix}_{file_end_time_unix}_{ts_sequence_number}
        :type record_ts_prefix: str
        :param record_slice_duration: 录制HLS时ts的切片时长，非必须，缺省为10，单位秒，最小2，最大60
        :type record_slice_duration: int
        :param record_max_duration_to_merge_file: 录制HLS文件拼接时长，如果流中断超过该时间，则生成新文件。单位秒。如果为0表示流中断就生成新文件，如果为-1则表示相同的流中断恢复后继续在30天内的前一个文件保存。默认为0。
        :type record_max_duration_to_merge_file: int
        """
        
        

        self._record_cycle = None
        self._record_prefix = None
        self._record_ts_prefix = None
        self._record_slice_duration = None
        self._record_max_duration_to_merge_file = None
        self.discriminator = None

        self.record_cycle = record_cycle
        if record_prefix is not None:
            self.record_prefix = record_prefix
        if record_ts_prefix is not None:
            self.record_ts_prefix = record_ts_prefix
        if record_slice_duration is not None:
            self.record_slice_duration = record_slice_duration
        if record_max_duration_to_merge_file is not None:
            self.record_max_duration_to_merge_file = record_max_duration_to_merge_file

    @property
    def record_cycle(self):
        """Gets the record_cycle of this HLSRecordConfig.

        单位为秒，周期录制时长，最小1分钟（60秒），最大12小时。如果为0则整个流录制一个文件。

        :return: The record_cycle of this HLSRecordConfig.
        :rtype: int
        """
        return self._record_cycle

    @record_cycle.setter
    def record_cycle(self, record_cycle):
        """Sets the record_cycle of this HLSRecordConfig.

        单位为秒，周期录制时长，最小1分钟（60秒），最大12小时。如果为0则整个流录制一个文件。

        :param record_cycle: The record_cycle of this HLSRecordConfig.
        :type record_cycle: int
        """
        self._record_cycle = record_cycle

    @property
    def record_prefix(self):
        """Gets the record_prefix of this HLSRecordConfig.

        录制m3u8文件含路径和文件名的前缀， 默认Record/{publish_domain}/{app}/{record_type}/{record_format}/{stream}_{file_start_time}/{stream}_{file_start_time}

        :return: The record_prefix of this HLSRecordConfig.
        :rtype: str
        """
        return self._record_prefix

    @record_prefix.setter
    def record_prefix(self, record_prefix):
        """Sets the record_prefix of this HLSRecordConfig.

        录制m3u8文件含路径和文件名的前缀， 默认Record/{publish_domain}/{app}/{record_type}/{record_format}/{stream}_{file_start_time}/{stream}_{file_start_time}

        :param record_prefix: The record_prefix of this HLSRecordConfig.
        :type record_prefix: str
        """
        self._record_prefix = record_prefix

    @property
    def record_ts_prefix(self):
        """Gets the record_ts_prefix of this HLSRecordConfig.

        录制ts文件名的前缀， 默认{file_start_time_unix}_{file_end_time_unix}_{ts_sequence_number}

        :return: The record_ts_prefix of this HLSRecordConfig.
        :rtype: str
        """
        return self._record_ts_prefix

    @record_ts_prefix.setter
    def record_ts_prefix(self, record_ts_prefix):
        """Sets the record_ts_prefix of this HLSRecordConfig.

        录制ts文件名的前缀， 默认{file_start_time_unix}_{file_end_time_unix}_{ts_sequence_number}

        :param record_ts_prefix: The record_ts_prefix of this HLSRecordConfig.
        :type record_ts_prefix: str
        """
        self._record_ts_prefix = record_ts_prefix

    @property
    def record_slice_duration(self):
        """Gets the record_slice_duration of this HLSRecordConfig.

        录制HLS时ts的切片时长，非必须，缺省为10，单位秒，最小2，最大60

        :return: The record_slice_duration of this HLSRecordConfig.
        :rtype: int
        """
        return self._record_slice_duration

    @record_slice_duration.setter
    def record_slice_duration(self, record_slice_duration):
        """Sets the record_slice_duration of this HLSRecordConfig.

        录制HLS时ts的切片时长，非必须，缺省为10，单位秒，最小2，最大60

        :param record_slice_duration: The record_slice_duration of this HLSRecordConfig.
        :type record_slice_duration: int
        """
        self._record_slice_duration = record_slice_duration

    @property
    def record_max_duration_to_merge_file(self):
        """Gets the record_max_duration_to_merge_file of this HLSRecordConfig.

        录制HLS文件拼接时长，如果流中断超过该时间，则生成新文件。单位秒。如果为0表示流中断就生成新文件，如果为-1则表示相同的流中断恢复后继续在30天内的前一个文件保存。默认为0。

        :return: The record_max_duration_to_merge_file of this HLSRecordConfig.
        :rtype: int
        """
        return self._record_max_duration_to_merge_file

    @record_max_duration_to_merge_file.setter
    def record_max_duration_to_merge_file(self, record_max_duration_to_merge_file):
        """Sets the record_max_duration_to_merge_file of this HLSRecordConfig.

        录制HLS文件拼接时长，如果流中断超过该时间，则生成新文件。单位秒。如果为0表示流中断就生成新文件，如果为-1则表示相同的流中断恢复后继续在30天内的前一个文件保存。默认为0。

        :param record_max_duration_to_merge_file: The record_max_duration_to_merge_file of this HLSRecordConfig.
        :type record_max_duration_to_merge_file: int
        """
        self._record_max_duration_to_merge_file = record_max_duration_to_merge_file

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
        if not isinstance(other, HLSRecordConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
