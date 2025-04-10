# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestScheduleCycleConfDTO:

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
        'media_types': 'str',
        'start_time': 'str',
        'length': 'int',
        'is_auto_record': 'int',
        'conf_config_info': 'CycleSubConfConfigDTO',
        'record_auth_type': 'int',
        'description': 'str'
    }

    attribute_map = {
        'cycle_sub_conf_id': 'cycleSubConfID',
        'media_types': 'mediaTypes',
        'start_time': 'startTime',
        'length': 'length',
        'is_auto_record': 'isAutoRecord',
        'conf_config_info': 'confConfigInfo',
        'record_auth_type': 'recordAuthType',
        'description': 'description'
    }

    def __init__(self, cycle_sub_conf_id=None, media_types=None, start_time=None, length=None, is_auto_record=None, conf_config_info=None, record_auth_type=None, description=None):
        r"""RestScheduleCycleConfDTO

        The model defined in huaweicloud sdk

        :param cycle_sub_conf_id: 子会议UUID。
        :type cycle_sub_conf_id: str
        :param media_types: 会议的媒体类型。 * Voice：语音会议 * HDVideo：视频会议 
        :type media_types: str
        :param start_time: 会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 &gt; * 如果没有指定开始时间或填空串，则表示会议马上开始 &gt; * 时间是UTC时间，即0时区的时间 
        :type start_time: str
        :param length: 会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。 
        :type length: int
        :param is_auto_record: 会议是否自动启动录制，在录播类型为：录播、录播+直播时才生效。默认为不自动启动。 * 1：自动启动录制 * 0：不自动启动录制 
        :type is_auto_record: int
        :param conf_config_info: 
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        :param record_auth_type: 录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 * 0：可通过链接观看/下载 * 1：企业用户可观看/下载 * 2：与会者可观看/下载 
        :type record_auth_type: int
        :param description: 会议描述，长度限制为200个字符。
        :type description: str
        """
        
        

        self._cycle_sub_conf_id = None
        self._media_types = None
        self._start_time = None
        self._length = None
        self._is_auto_record = None
        self._conf_config_info = None
        self._record_auth_type = None
        self._description = None
        self.discriminator = None

        self.cycle_sub_conf_id = cycle_sub_conf_id
        self.media_types = media_types
        self.start_time = start_time
        self.length = length
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
        r"""Gets the cycle_sub_conf_id of this RestScheduleCycleConfDTO.

        子会议UUID。

        :return: The cycle_sub_conf_id of this RestScheduleCycleConfDTO.
        :rtype: str
        """
        return self._cycle_sub_conf_id

    @cycle_sub_conf_id.setter
    def cycle_sub_conf_id(self, cycle_sub_conf_id):
        r"""Sets the cycle_sub_conf_id of this RestScheduleCycleConfDTO.

        子会议UUID。

        :param cycle_sub_conf_id: The cycle_sub_conf_id of this RestScheduleCycleConfDTO.
        :type cycle_sub_conf_id: str
        """
        self._cycle_sub_conf_id = cycle_sub_conf_id

    @property
    def media_types(self):
        r"""Gets the media_types of this RestScheduleCycleConfDTO.

        会议的媒体类型。 * Voice：语音会议 * HDVideo：视频会议 

        :return: The media_types of this RestScheduleCycleConfDTO.
        :rtype: str
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        r"""Sets the media_types of this RestScheduleCycleConfDTO.

        会议的媒体类型。 * Voice：语音会议 * HDVideo：视频会议 

        :param media_types: The media_types of this RestScheduleCycleConfDTO.
        :type media_types: str
        """
        self._media_types = media_types

    @property
    def start_time(self):
        r"""Gets the start_time of this RestScheduleCycleConfDTO.

        会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 > * 如果没有指定开始时间或填空串，则表示会议马上开始 > * 时间是UTC时间，即0时区的时间 

        :return: The start_time of this RestScheduleCycleConfDTO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RestScheduleCycleConfDTO.

        会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 > * 如果没有指定开始时间或填空串，则表示会议马上开始 > * 时间是UTC时间，即0时区的时间 

        :param start_time: The start_time of this RestScheduleCycleConfDTO.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def length(self):
        r"""Gets the length of this RestScheduleCycleConfDTO.

        会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。 

        :return: The length of this RestScheduleCycleConfDTO.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this RestScheduleCycleConfDTO.

        会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。 

        :param length: The length of this RestScheduleCycleConfDTO.
        :type length: int
        """
        self._length = length

    @property
    def is_auto_record(self):
        r"""Gets the is_auto_record of this RestScheduleCycleConfDTO.

        会议是否自动启动录制，在录播类型为：录播、录播+直播时才生效。默认为不自动启动。 * 1：自动启动录制 * 0：不自动启动录制 

        :return: The is_auto_record of this RestScheduleCycleConfDTO.
        :rtype: int
        """
        return self._is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, is_auto_record):
        r"""Sets the is_auto_record of this RestScheduleCycleConfDTO.

        会议是否自动启动录制，在录播类型为：录播、录播+直播时才生效。默认为不自动启动。 * 1：自动启动录制 * 0：不自动启动录制 

        :param is_auto_record: The is_auto_record of this RestScheduleCycleConfDTO.
        :type is_auto_record: int
        """
        self._is_auto_record = is_auto_record

    @property
    def conf_config_info(self):
        r"""Gets the conf_config_info of this RestScheduleCycleConfDTO.

        :return: The conf_config_info of this RestScheduleCycleConfDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        r"""Sets the conf_config_info of this RestScheduleCycleConfDTO.

        :param conf_config_info: The conf_config_info of this RestScheduleCycleConfDTO.
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.CycleSubConfConfigDTO`
        """
        self._conf_config_info = conf_config_info

    @property
    def record_auth_type(self):
        r"""Gets the record_auth_type of this RestScheduleCycleConfDTO.

        录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 * 0：可通过链接观看/下载 * 1：企业用户可观看/下载 * 2：与会者可观看/下载 

        :return: The record_auth_type of this RestScheduleCycleConfDTO.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        r"""Sets the record_auth_type of this RestScheduleCycleConfDTO.

        录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 * 0：可通过链接观看/下载 * 1：企业用户可观看/下载 * 2：与会者可观看/下载 

        :param record_auth_type: The record_auth_type of this RestScheduleCycleConfDTO.
        :type record_auth_type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def description(self):
        r"""Gets the description of this RestScheduleCycleConfDTO.

        会议描述，长度限制为200个字符。

        :return: The description of this RestScheduleCycleConfDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RestScheduleCycleConfDTO.

        会议描述，长度限制为200个字符。

        :param description: The description of this RestScheduleCycleConfDTO.
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
        if not isinstance(other, RestScheduleCycleConfDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
