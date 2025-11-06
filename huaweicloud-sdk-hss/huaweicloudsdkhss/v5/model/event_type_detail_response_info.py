# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventTypeDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type_name': 'str',
        'event_type_num': 'int',
        'event_type_list': 'list[EventTypeResponseInfo]'
    }

    attribute_map = {
        'event_type_name': 'event_type_name',
        'event_type_num': 'event_type_num',
        'event_type_list': 'event_type_list'
    }

    def __init__(self, event_type_name=None, event_type_num=None, event_type_list=None):
        r"""EventTypeDetailResponseInfo

        The model defined in huaweicloud sdk

        :param event_type_name: 大类别对应的名字:   - malicious_software：恶意软件   - \&quot;exploit_attack\&quot;：漏洞利用   - \&quot;system_abnormal_behavior\&quot;：系统异常行为   - \&quot;user_abnormal_behavior\&quot;：用户异常行为   - \&quot;network_abnormal_access\&quot;：网络异常访问   - \&quot;resource_recon\&quot;：资源侦查   - \&quot;risk_audit\&quot;：风险审计   - \&quot;information_destroy\&quot;：信息破坏   - \&quot;denial_of_service\&quot;：拒绝服务攻击   - \&quot;advanced_threat\&quot;：高级威胁   - \&quot;extend\&quot;：其余未列出的，里面的类别显示到外层中
        :type event_type_name: str
        :param event_type_num: 事件类别的总数量
        :type event_type_num: int
        :param event_type_list: 小类别对应的名称与数量列表
        :type event_type_list: list[:class:`huaweicloudsdkhss.v5.EventTypeResponseInfo`]
        """
        
        

        self._event_type_name = None
        self._event_type_num = None
        self._event_type_list = None
        self.discriminator = None

        if event_type_name is not None:
            self.event_type_name = event_type_name
        if event_type_num is not None:
            self.event_type_num = event_type_num
        if event_type_list is not None:
            self.event_type_list = event_type_list

    @property
    def event_type_name(self):
        r"""Gets the event_type_name of this EventTypeDetailResponseInfo.

        大类别对应的名字:   - malicious_software：恶意软件   - \"exploit_attack\"：漏洞利用   - \"system_abnormal_behavior\"：系统异常行为   - \"user_abnormal_behavior\"：用户异常行为   - \"network_abnormal_access\"：网络异常访问   - \"resource_recon\"：资源侦查   - \"risk_audit\"：风险审计   - \"information_destroy\"：信息破坏   - \"denial_of_service\"：拒绝服务攻击   - \"advanced_threat\"：高级威胁   - \"extend\"：其余未列出的，里面的类别显示到外层中

        :return: The event_type_name of this EventTypeDetailResponseInfo.
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        r"""Sets the event_type_name of this EventTypeDetailResponseInfo.

        大类别对应的名字:   - malicious_software：恶意软件   - \"exploit_attack\"：漏洞利用   - \"system_abnormal_behavior\"：系统异常行为   - \"user_abnormal_behavior\"：用户异常行为   - \"network_abnormal_access\"：网络异常访问   - \"resource_recon\"：资源侦查   - \"risk_audit\"：风险审计   - \"information_destroy\"：信息破坏   - \"denial_of_service\"：拒绝服务攻击   - \"advanced_threat\"：高级威胁   - \"extend\"：其余未列出的，里面的类别显示到外层中

        :param event_type_name: The event_type_name of this EventTypeDetailResponseInfo.
        :type event_type_name: str
        """
        self._event_type_name = event_type_name

    @property
    def event_type_num(self):
        r"""Gets the event_type_num of this EventTypeDetailResponseInfo.

        事件类别的总数量

        :return: The event_type_num of this EventTypeDetailResponseInfo.
        :rtype: int
        """
        return self._event_type_num

    @event_type_num.setter
    def event_type_num(self, event_type_num):
        r"""Sets the event_type_num of this EventTypeDetailResponseInfo.

        事件类别的总数量

        :param event_type_num: The event_type_num of this EventTypeDetailResponseInfo.
        :type event_type_num: int
        """
        self._event_type_num = event_type_num

    @property
    def event_type_list(self):
        r"""Gets the event_type_list of this EventTypeDetailResponseInfo.

        小类别对应的名称与数量列表

        :return: The event_type_list of this EventTypeDetailResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.EventTypeResponseInfo`]
        """
        return self._event_type_list

    @event_type_list.setter
    def event_type_list(self, event_type_list):
        r"""Sets the event_type_list of this EventTypeDetailResponseInfo.

        小类别对应的名称与数量列表

        :param event_type_list: The event_type_list of this EventTypeDetailResponseInfo.
        :type event_type_list: list[:class:`huaweicloudsdkhss.v5.EventTypeResponseInfo`]
        """
        self._event_type_list = event_type_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventTypeDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
