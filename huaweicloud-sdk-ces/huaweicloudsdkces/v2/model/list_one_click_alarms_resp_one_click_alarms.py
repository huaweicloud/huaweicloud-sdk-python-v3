# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOneClickAlarmsRespOneClickAlarms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'one_click_alarm_id': 'str',
        'namespace': 'str',
        'description': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'one_click_alarm_id': 'one_click_alarm_id',
        'namespace': 'namespace',
        'description': 'description',
        'enabled': 'enabled'
    }

    def __init__(self, one_click_alarm_id=None, namespace=None, description=None, enabled=None):
        r"""ListOneClickAlarmsRespOneClickAlarms

        The model defined in huaweicloud sdk

        :param one_click_alarm_id: 一键告警ID
        :type one_click_alarm_id: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param description: 一键告警描述，长度范围[0,256]，该字段默认值为空字符串
        :type description: str
        :param enabled: 是否启用一键告警。true:开启，false：关闭。
        :type enabled: bool
        """
        
        

        self._one_click_alarm_id = None
        self._namespace = None
        self._description = None
        self._enabled = None
        self.discriminator = None

        self.one_click_alarm_id = one_click_alarm_id
        self.namespace = namespace
        self.description = description
        self.enabled = enabled

    @property
    def one_click_alarm_id(self):
        r"""Gets the one_click_alarm_id of this ListOneClickAlarmsRespOneClickAlarms.

        一键告警ID

        :return: The one_click_alarm_id of this ListOneClickAlarmsRespOneClickAlarms.
        :rtype: str
        """
        return self._one_click_alarm_id

    @one_click_alarm_id.setter
    def one_click_alarm_id(self, one_click_alarm_id):
        r"""Sets the one_click_alarm_id of this ListOneClickAlarmsRespOneClickAlarms.

        一键告警ID

        :param one_click_alarm_id: The one_click_alarm_id of this ListOneClickAlarmsRespOneClickAlarms.
        :type one_click_alarm_id: str
        """
        self._one_click_alarm_id = one_click_alarm_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListOneClickAlarmsRespOneClickAlarms.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this ListOneClickAlarmsRespOneClickAlarms.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListOneClickAlarmsRespOneClickAlarms.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this ListOneClickAlarmsRespOneClickAlarms.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def description(self):
        r"""Gets the description of this ListOneClickAlarmsRespOneClickAlarms.

        一键告警描述，长度范围[0,256]，该字段默认值为空字符串

        :return: The description of this ListOneClickAlarmsRespOneClickAlarms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListOneClickAlarmsRespOneClickAlarms.

        一键告警描述，长度范围[0,256]，该字段默认值为空字符串

        :param description: The description of this ListOneClickAlarmsRespOneClickAlarms.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this ListOneClickAlarmsRespOneClickAlarms.

        是否启用一键告警。true:开启，false：关闭。

        :return: The enabled of this ListOneClickAlarmsRespOneClickAlarms.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListOneClickAlarmsRespOneClickAlarms.

        是否启用一键告警。true:开启，false：关闭。

        :param enabled: The enabled of this ListOneClickAlarmsRespOneClickAlarms.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, ListOneClickAlarmsRespOneClickAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
