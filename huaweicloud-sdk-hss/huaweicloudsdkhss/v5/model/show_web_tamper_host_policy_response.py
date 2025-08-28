# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebTamperHostPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_dir_num': 'int',
        'protect_dir_info': 'WtpProtectDirResponseInfo',
        'enable_timing_off': 'bool',
        'timing_off_config_info': 'ListTimingOffConfigInfoResponseInfo',
        'enable_rasp_protect': 'bool',
        'rasp_path': 'str',
        'enable_privileged_process': 'bool',
        'privileged_child_status': 'bool',
        'privileged_process_path_list': 'list[str]',
        'privileged_process_info': 'ListPrivilegedProcessResponseInfo'
    }

    attribute_map = {
        'protect_dir_num': 'protect_dir_num',
        'protect_dir_info': 'protect_dir_info',
        'enable_timing_off': 'enable_timing_off',
        'timing_off_config_info': 'timing_off_config_info',
        'enable_rasp_protect': 'enable_rasp_protect',
        'rasp_path': 'rasp_path',
        'enable_privileged_process': 'enable_privileged_process',
        'privileged_child_status': 'privileged_child_status',
        'privileged_process_path_list': 'privileged_process_path_list',
        'privileged_process_info': 'privileged_process_info'
    }

    def __init__(self, protect_dir_num=None, protect_dir_info=None, enable_timing_off=None, timing_off_config_info=None, enable_rasp_protect=None, rasp_path=None, enable_privileged_process=None, privileged_child_status=None, privileged_process_path_list=None, privileged_process_info=None):
        r"""ShowWebTamperHostPolicyResponse

        The model defined in huaweicloud sdk

        :param protect_dir_num: **参数解释**: 防护目录数 **取值范围**: 取值0-50 
        :type protect_dir_num: int
        :param protect_dir_info: 
        :type protect_dir_info: :class:`huaweicloudsdkhss.v5.WtpProtectDirResponseInfo`
        :param enable_timing_off: **参数解释**: 定时开关状态 **取值范围**: - True ：开启定时关闭防护功能。 - False ：未开启定时关闭防护功能。 
        :type enable_timing_off: bool
        :param timing_off_config_info: 
        :type timing_off_config_info: :class:`huaweicloudsdkhss.v5.ListTimingOffConfigInfoResponseInfo`
        :param enable_rasp_protect: **参数解释**: 动态网页防篡改开启状态 **取值范围**: - True ：开启动态网页防篡改防护。 - False ：未开启动态网页防篡改防护。 
        :type enable_rasp_protect: bool
        :param rasp_path: **参数解释**: 动态网页防篡改的Tomcat bin目录 **取值范围**: 字符长度0-512位 
        :type rasp_path: str
        :param enable_privileged_process: **参数解释**: 特权进程开启状态 **取值范围**: - True ：开启特权进程。 - False ：未开启特权进程。 
        :type enable_privileged_process: bool
        :param privileged_child_status: **参数解释**: 特权进程子进程可信状态，需先开启特权进程 **取值范围**: - True ：开启特权进程子进程可信。 - False ：未开启特权进程子进程可信。 
        :type privileged_child_status: bool
        :param privileged_process_path_list: **参数解释**: 特权进程文件路径列表 **取值范围**: 最少0条，最多10条 
        :type privileged_process_path_list: list[str]
        :param privileged_process_info: 
        :type privileged_process_info: :class:`huaweicloudsdkhss.v5.ListPrivilegedProcessResponseInfo`
        """
        
        super(ShowWebTamperHostPolicyResponse, self).__init__()

        self._protect_dir_num = None
        self._protect_dir_info = None
        self._enable_timing_off = None
        self._timing_off_config_info = None
        self._enable_rasp_protect = None
        self._rasp_path = None
        self._enable_privileged_process = None
        self._privileged_child_status = None
        self._privileged_process_path_list = None
        self._privileged_process_info = None
        self.discriminator = None

        if protect_dir_num is not None:
            self.protect_dir_num = protect_dir_num
        if protect_dir_info is not None:
            self.protect_dir_info = protect_dir_info
        if enable_timing_off is not None:
            self.enable_timing_off = enable_timing_off
        if timing_off_config_info is not None:
            self.timing_off_config_info = timing_off_config_info
        if enable_rasp_protect is not None:
            self.enable_rasp_protect = enable_rasp_protect
        if rasp_path is not None:
            self.rasp_path = rasp_path
        if enable_privileged_process is not None:
            self.enable_privileged_process = enable_privileged_process
        if privileged_child_status is not None:
            self.privileged_child_status = privileged_child_status
        if privileged_process_path_list is not None:
            self.privileged_process_path_list = privileged_process_path_list
        if privileged_process_info is not None:
            self.privileged_process_info = privileged_process_info

    @property
    def protect_dir_num(self):
        r"""Gets the protect_dir_num of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 防护目录数 **取值范围**: 取值0-50 

        :return: The protect_dir_num of this ShowWebTamperHostPolicyResponse.
        :rtype: int
        """
        return self._protect_dir_num

    @protect_dir_num.setter
    def protect_dir_num(self, protect_dir_num):
        r"""Sets the protect_dir_num of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 防护目录数 **取值范围**: 取值0-50 

        :param protect_dir_num: The protect_dir_num of this ShowWebTamperHostPolicyResponse.
        :type protect_dir_num: int
        """
        self._protect_dir_num = protect_dir_num

    @property
    def protect_dir_info(self):
        r"""Gets the protect_dir_info of this ShowWebTamperHostPolicyResponse.

        :return: The protect_dir_info of this ShowWebTamperHostPolicyResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.WtpProtectDirResponseInfo`
        """
        return self._protect_dir_info

    @protect_dir_info.setter
    def protect_dir_info(self, protect_dir_info):
        r"""Sets the protect_dir_info of this ShowWebTamperHostPolicyResponse.

        :param protect_dir_info: The protect_dir_info of this ShowWebTamperHostPolicyResponse.
        :type protect_dir_info: :class:`huaweicloudsdkhss.v5.WtpProtectDirResponseInfo`
        """
        self._protect_dir_info = protect_dir_info

    @property
    def enable_timing_off(self):
        r"""Gets the enable_timing_off of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 定时开关状态 **取值范围**: - True ：开启定时关闭防护功能。 - False ：未开启定时关闭防护功能。 

        :return: The enable_timing_off of this ShowWebTamperHostPolicyResponse.
        :rtype: bool
        """
        return self._enable_timing_off

    @enable_timing_off.setter
    def enable_timing_off(self, enable_timing_off):
        r"""Sets the enable_timing_off of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 定时开关状态 **取值范围**: - True ：开启定时关闭防护功能。 - False ：未开启定时关闭防护功能。 

        :param enable_timing_off: The enable_timing_off of this ShowWebTamperHostPolicyResponse.
        :type enable_timing_off: bool
        """
        self._enable_timing_off = enable_timing_off

    @property
    def timing_off_config_info(self):
        r"""Gets the timing_off_config_info of this ShowWebTamperHostPolicyResponse.

        :return: The timing_off_config_info of this ShowWebTamperHostPolicyResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTimingOffConfigInfoResponseInfo`
        """
        return self._timing_off_config_info

    @timing_off_config_info.setter
    def timing_off_config_info(self, timing_off_config_info):
        r"""Sets the timing_off_config_info of this ShowWebTamperHostPolicyResponse.

        :param timing_off_config_info: The timing_off_config_info of this ShowWebTamperHostPolicyResponse.
        :type timing_off_config_info: :class:`huaweicloudsdkhss.v5.ListTimingOffConfigInfoResponseInfo`
        """
        self._timing_off_config_info = timing_off_config_info

    @property
    def enable_rasp_protect(self):
        r"""Gets the enable_rasp_protect of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 动态网页防篡改开启状态 **取值范围**: - True ：开启动态网页防篡改防护。 - False ：未开启动态网页防篡改防护。 

        :return: The enable_rasp_protect of this ShowWebTamperHostPolicyResponse.
        :rtype: bool
        """
        return self._enable_rasp_protect

    @enable_rasp_protect.setter
    def enable_rasp_protect(self, enable_rasp_protect):
        r"""Sets the enable_rasp_protect of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 动态网页防篡改开启状态 **取值范围**: - True ：开启动态网页防篡改防护。 - False ：未开启动态网页防篡改防护。 

        :param enable_rasp_protect: The enable_rasp_protect of this ShowWebTamperHostPolicyResponse.
        :type enable_rasp_protect: bool
        """
        self._enable_rasp_protect = enable_rasp_protect

    @property
    def rasp_path(self):
        r"""Gets the rasp_path of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 动态网页防篡改的Tomcat bin目录 **取值范围**: 字符长度0-512位 

        :return: The rasp_path of this ShowWebTamperHostPolicyResponse.
        :rtype: str
        """
        return self._rasp_path

    @rasp_path.setter
    def rasp_path(self, rasp_path):
        r"""Sets the rasp_path of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 动态网页防篡改的Tomcat bin目录 **取值范围**: 字符长度0-512位 

        :param rasp_path: The rasp_path of this ShowWebTamperHostPolicyResponse.
        :type rasp_path: str
        """
        self._rasp_path = rasp_path

    @property
    def enable_privileged_process(self):
        r"""Gets the enable_privileged_process of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程开启状态 **取值范围**: - True ：开启特权进程。 - False ：未开启特权进程。 

        :return: The enable_privileged_process of this ShowWebTamperHostPolicyResponse.
        :rtype: bool
        """
        return self._enable_privileged_process

    @enable_privileged_process.setter
    def enable_privileged_process(self, enable_privileged_process):
        r"""Sets the enable_privileged_process of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程开启状态 **取值范围**: - True ：开启特权进程。 - False ：未开启特权进程。 

        :param enable_privileged_process: The enable_privileged_process of this ShowWebTamperHostPolicyResponse.
        :type enable_privileged_process: bool
        """
        self._enable_privileged_process = enable_privileged_process

    @property
    def privileged_child_status(self):
        r"""Gets the privileged_child_status of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程子进程可信状态，需先开启特权进程 **取值范围**: - True ：开启特权进程子进程可信。 - False ：未开启特权进程子进程可信。 

        :return: The privileged_child_status of this ShowWebTamperHostPolicyResponse.
        :rtype: bool
        """
        return self._privileged_child_status

    @privileged_child_status.setter
    def privileged_child_status(self, privileged_child_status):
        r"""Sets the privileged_child_status of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程子进程可信状态，需先开启特权进程 **取值范围**: - True ：开启特权进程子进程可信。 - False ：未开启特权进程子进程可信。 

        :param privileged_child_status: The privileged_child_status of this ShowWebTamperHostPolicyResponse.
        :type privileged_child_status: bool
        """
        self._privileged_child_status = privileged_child_status

    @property
    def privileged_process_path_list(self):
        r"""Gets the privileged_process_path_list of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程文件路径列表 **取值范围**: 最少0条，最多10条 

        :return: The privileged_process_path_list of this ShowWebTamperHostPolicyResponse.
        :rtype: list[str]
        """
        return self._privileged_process_path_list

    @privileged_process_path_list.setter
    def privileged_process_path_list(self, privileged_process_path_list):
        r"""Sets the privileged_process_path_list of this ShowWebTamperHostPolicyResponse.

        **参数解释**: 特权进程文件路径列表 **取值范围**: 最少0条，最多10条 

        :param privileged_process_path_list: The privileged_process_path_list of this ShowWebTamperHostPolicyResponse.
        :type privileged_process_path_list: list[str]
        """
        self._privileged_process_path_list = privileged_process_path_list

    @property
    def privileged_process_info(self):
        r"""Gets the privileged_process_info of this ShowWebTamperHostPolicyResponse.

        :return: The privileged_process_info of this ShowWebTamperHostPolicyResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ListPrivilegedProcessResponseInfo`
        """
        return self._privileged_process_info

    @privileged_process_info.setter
    def privileged_process_info(self, privileged_process_info):
        r"""Sets the privileged_process_info of this ShowWebTamperHostPolicyResponse.

        :param privileged_process_info: The privileged_process_info of this ShowWebTamperHostPolicyResponse.
        :type privileged_process_info: :class:`huaweicloudsdkhss.v5.ListPrivilegedProcessResponseInfo`
        """
        self._privileged_process_info = privileged_process_info

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
        if not isinstance(other, ShowWebTamperHostPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
