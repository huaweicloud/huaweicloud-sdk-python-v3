# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'resource_id': 'str',
        'alarm_infos': 'list[AlarmInfo]'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_id': 'resource_id',
        'alarm_infos': 'alarm_infos'
    }

    def __init__(self, resource_name=None, resource_id=None, alarm_infos=None):
        r"""AlarmHost

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_id: 资源id
        :type resource_id: str
        :param alarm_infos: 告警信息
        :type alarm_infos: list[:class:`huaweicloudsdkclouddc.v1.AlarmInfo`]
        """
        
        

        self._resource_name = None
        self._resource_id = None
        self._alarm_infos = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        if alarm_infos is not None:
            self.alarm_infos = alarm_infos

    @property
    def resource_name(self):
        r"""Gets the resource_name of this AlarmHost.

        资源名称

        :return: The resource_name of this AlarmHost.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this AlarmHost.

        资源名称

        :param resource_name: The resource_name of this AlarmHost.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this AlarmHost.

        资源id

        :return: The resource_id of this AlarmHost.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AlarmHost.

        资源id

        :param resource_id: The resource_id of this AlarmHost.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def alarm_infos(self):
        r"""Gets the alarm_infos of this AlarmHost.

        告警信息

        :return: The alarm_infos of this AlarmHost.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmInfo`]
        """
        return self._alarm_infos

    @alarm_infos.setter
    def alarm_infos(self, alarm_infos):
        r"""Sets the alarm_infos of this AlarmHost.

        告警信息

        :param alarm_infos: The alarm_infos of this AlarmHost.
        :type alarm_infos: list[:class:`huaweicloudsdkclouddc.v1.AlarmInfo`]
        """
        self._alarm_infos = alarm_infos

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
        if not isinstance(other, AlarmHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
