# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlackHoleEventRecordItem:

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
        'tenant_name': 'str',
        'vip': 'str',
        'vip_id': 'str',
        'instance_id': 'str',
        'event_type': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'tenant_name': 'tenant_name',
        'vip': 'vip',
        'vip_id': 'vip_id',
        'instance_id': 'instance_id',
        'event_type': 'event_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, project_id=None, tenant_name=None, vip=None, vip_id=None, instance_id=None, event_type=None, start_time=None, end_time=None):
        r"""ListBlackHoleEventRecordItem

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param tenant_name: 租户名
        :type tenant_name: str
        :param vip: 高防ip
        :type vip: str
        :param vip_id: ip id
        :type vip_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param event_type: 事件类型 block-黑洞中，unblock-黑洞结束
        :type event_type: str
        :param start_time: 封堵开始时间
        :type start_time: int
        :param end_time: 封堵结束时间
        :type end_time: int
        """
        
        

        self._project_id = None
        self._tenant_name = None
        self._vip = None
        self._vip_id = None
        self._instance_id = None
        self._event_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.project_id = project_id
        self.tenant_name = tenant_name
        self.vip = vip
        self.vip_id = vip_id
        self.instance_id = instance_id
        self.event_type = event_type
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def project_id(self):
        r"""Gets the project_id of this ListBlackHoleEventRecordItem.

        项目id

        :return: The project_id of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListBlackHoleEventRecordItem.

        项目id

        :param project_id: The project_id of this ListBlackHoleEventRecordItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ListBlackHoleEventRecordItem.

        租户名

        :return: The tenant_name of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ListBlackHoleEventRecordItem.

        租户名

        :param tenant_name: The tenant_name of this ListBlackHoleEventRecordItem.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def vip(self):
        r"""Gets the vip of this ListBlackHoleEventRecordItem.

        高防ip

        :return: The vip of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        r"""Sets the vip of this ListBlackHoleEventRecordItem.

        高防ip

        :param vip: The vip of this ListBlackHoleEventRecordItem.
        :type vip: str
        """
        self._vip = vip

    @property
    def vip_id(self):
        r"""Gets the vip_id of this ListBlackHoleEventRecordItem.

        ip id

        :return: The vip_id of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._vip_id

    @vip_id.setter
    def vip_id(self, vip_id):
        r"""Sets the vip_id of this ListBlackHoleEventRecordItem.

        ip id

        :param vip_id: The vip_id of this ListBlackHoleEventRecordItem.
        :type vip_id: str
        """
        self._vip_id = vip_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBlackHoleEventRecordItem.

        实例id

        :return: The instance_id of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBlackHoleEventRecordItem.

        实例id

        :param instance_id: The instance_id of this ListBlackHoleEventRecordItem.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def event_type(self):
        r"""Gets the event_type of this ListBlackHoleEventRecordItem.

        事件类型 block-黑洞中，unblock-黑洞结束

        :return: The event_type of this ListBlackHoleEventRecordItem.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListBlackHoleEventRecordItem.

        事件类型 block-黑洞中，unblock-黑洞结束

        :param event_type: The event_type of this ListBlackHoleEventRecordItem.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBlackHoleEventRecordItem.

        封堵开始时间

        :return: The start_time of this ListBlackHoleEventRecordItem.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBlackHoleEventRecordItem.

        封堵开始时间

        :param start_time: The start_time of this ListBlackHoleEventRecordItem.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBlackHoleEventRecordItem.

        封堵结束时间

        :return: The end_time of this ListBlackHoleEventRecordItem.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBlackHoleEventRecordItem.

        封堵结束时间

        :param end_time: The end_time of this ListBlackHoleEventRecordItem.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListBlackHoleEventRecordItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
