# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CycleSubConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cycle_sub_conf_id': 'str',
        'conference_id': 'str',
        'media_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'is_auto_record': 'int',
        'conf_config_info': 'CycleSubConfConfigDTO',
        'record_auth_type': 'int',
        'description': 'str'
    }

    attribute_map = {
        'cycle_sub_conf_id': 'cycleSubConfID',
        'conference_id': 'conferenceID',
        'media_type': 'mediaType',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'is_auto_record': 'isAutoRecord',
        'conf_config_info': 'confConfigInfo',
        'record_auth_type': 'recordAuthType',
        'description': 'description'
    }

    def __init__(self, cycle_sub_conf_id=None, conference_id=None, media_type=None, start_time=None, end_time=None, is_auto_record=None, conf_config_info=None, record_auth_type=None, description=None):
        r"""CycleSubConf

        The model defined in huaweicloud sdk

        :param cycle_sub_conf_id: 子会议UUID。
        :type cycle_sub_conf_id: str
        :param conference_id: 会议ID。
        :type conference_id: str
        :param media_type: 会议的媒体类型。 * Voice：语音 * Video：标清视频 * HDVideo：高清视频 * Data：数据 
        :type media_type: str
        :param start_time: 会议起始时间(格式：YYYY-MM-DD HH:MM)。
        :type start_time: str
        :param end_time: 会议结束时间(格式：YYYY-MM-DD HH:MM)。
        :type end_time: str
        :param is_auto_record: 是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动 
        :type is_auto_record: int
        :param conf_config_info: 
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        :param record_auth_type: 观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载 
        :type record_auth_type: int
        :param description: 会议描述。长度限制为200个字符。
        :type description: str
        """
        
        

        self._cycle_sub_conf_id = None
        self._conference_id = None
        self._media_type = None
        self._start_time = None
        self._end_time = None
        self._is_auto_record = None
        self._conf_config_info = None
        self._record_auth_type = None
        self._description = None
        self.discriminator = None

        self.cycle_sub_conf_id = cycle_sub_conf_id
        if conference_id is not None:
            self.conference_id = conference_id
        if media_type is not None:
            self.media_type = media_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if is_auto_record is not None:
            self.is_auto_record = is_auto_record
        if conf_config_info is not None:
            self.conf_config_info = conf_config_info
        if record_auth_type is not None:
            self.record_auth_type = record_auth_type
        if description is not None:
            self.description = description

    @property
    def cycle_sub_conf_id(self):
        r"""Gets the cycle_sub_conf_id of this CycleSubConf.

        子会议UUID。

        :return: The cycle_sub_conf_id of this CycleSubConf.
        :rtype: str
        """
        return self._cycle_sub_conf_id

    @cycle_sub_conf_id.setter
    def cycle_sub_conf_id(self, cycle_sub_conf_id):
        r"""Sets the cycle_sub_conf_id of this CycleSubConf.

        子会议UUID。

        :param cycle_sub_conf_id: The cycle_sub_conf_id of this CycleSubConf.
        :type cycle_sub_conf_id: str
        """
        self._cycle_sub_conf_id = cycle_sub_conf_id

    @property
    def conference_id(self):
        r"""Gets the conference_id of this CycleSubConf.

        会议ID。

        :return: The conference_id of this CycleSubConf.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        r"""Sets the conference_id of this CycleSubConf.

        会议ID。

        :param conference_id: The conference_id of this CycleSubConf.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def media_type(self):
        r"""Gets the media_type of this CycleSubConf.

        会议的媒体类型。 * Voice：语音 * Video：标清视频 * HDVideo：高清视频 * Data：数据 

        :return: The media_type of this CycleSubConf.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        r"""Sets the media_type of this CycleSubConf.

        会议的媒体类型。 * Voice：语音 * Video：标清视频 * HDVideo：高清视频 * Data：数据 

        :param media_type: The media_type of this CycleSubConf.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def start_time(self):
        r"""Gets the start_time of this CycleSubConf.

        会议起始时间(格式：YYYY-MM-DD HH:MM)。

        :return: The start_time of this CycleSubConf.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CycleSubConf.

        会议起始时间(格式：YYYY-MM-DD HH:MM)。

        :param start_time: The start_time of this CycleSubConf.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CycleSubConf.

        会议结束时间(格式：YYYY-MM-DD HH:MM)。

        :return: The end_time of this CycleSubConf.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CycleSubConf.

        会议结束时间(格式：YYYY-MM-DD HH:MM)。

        :param end_time: The end_time of this CycleSubConf.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_auto_record(self):
        r"""Gets the is_auto_record of this CycleSubConf.

        是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动 

        :return: The is_auto_record of this CycleSubConf.
        :rtype: int
        """
        return self._is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, is_auto_record):
        r"""Sets the is_auto_record of this CycleSubConf.

        是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动 

        :param is_auto_record: The is_auto_record of this CycleSubConf.
        :type is_auto_record: int
        """
        self._is_auto_record = is_auto_record

    @property
    def conf_config_info(self):
        r"""Gets the conf_config_info of this CycleSubConf.

        :return: The conf_config_info of this CycleSubConf.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        r"""Sets the conf_config_info of this CycleSubConf.

        :param conf_config_info: The conf_config_info of this CycleSubConf.
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        """
        self._conf_config_info = conf_config_info

    @property
    def record_auth_type(self):
        r"""Gets the record_auth_type of this CycleSubConf.

        观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载 

        :return: The record_auth_type of this CycleSubConf.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        r"""Sets the record_auth_type of this CycleSubConf.

        观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载 

        :param record_auth_type: The record_auth_type of this CycleSubConf.
        :type record_auth_type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def description(self):
        r"""Gets the description of this CycleSubConf.

        会议描述。长度限制为200个字符。

        :return: The description of this CycleSubConf.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CycleSubConf.

        会议描述。长度限制为200个字符。

        :param description: The description of this CycleSubConf.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CycleSubConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
