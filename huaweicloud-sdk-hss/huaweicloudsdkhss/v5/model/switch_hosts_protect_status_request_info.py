# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchHostsProtectStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'charging_mode': 'str',
        'resource_id': 'str',
        'host_id_list': 'list[str]',
        'tags': 'list[TagInfo]'
    }

    attribute_map = {
        'version': 'version',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'host_id_list': 'host_id_list',
        'tags': 'tags'
    }

    def __init__(self, version=None, charging_mode=None, resource_id=None, host_id_list=None, tags=None):
        r"""SwitchHostsProtectStatusRequestInfo

        The model defined in huaweicloud sdk

        :param version: 主机开通的版本，包含如下:   - hss.version.null ：无，代表关闭防护。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。
        :type version: str
        :param charging_mode: 付费模式，当version不为“hss.version.null”时，则需必填该参数   - packet_cycle : 包周期   - on_demand : 按需
        :type charging_mode: str
        :param resource_id: HSS配额ID，不填该参数时，则随机选择对应版本配额
        :type resource_id: str
        :param host_id_list: 服务器列表
        :type host_id_list: list[str]
        :param tags: 资源标签列表
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        
        

        self._version = None
        self._charging_mode = None
        self._resource_id = None
        self._host_id_list = None
        self._tags = None
        self.discriminator = None

        self.version = version
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        self.host_id_list = host_id_list
        if tags is not None:
            self.tags = tags

    @property
    def version(self):
        r"""Gets the version of this SwitchHostsProtectStatusRequestInfo.

        主机开通的版本，包含如下:   - hss.version.null ：无，代表关闭防护。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :return: The version of this SwitchHostsProtectStatusRequestInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SwitchHostsProtectStatusRequestInfo.

        主机开通的版本，包含如下:   - hss.version.null ：无，代表关闭防护。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :param version: The version of this SwitchHostsProtectStatusRequestInfo.
        :type version: str
        """
        self._version = version

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SwitchHostsProtectStatusRequestInfo.

        付费模式，当version不为“hss.version.null”时，则需必填该参数   - packet_cycle : 包周期   - on_demand : 按需

        :return: The charging_mode of this SwitchHostsProtectStatusRequestInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SwitchHostsProtectStatusRequestInfo.

        付费模式，当version不为“hss.version.null”时，则需必填该参数   - packet_cycle : 包周期   - on_demand : 按需

        :param charging_mode: The charging_mode of this SwitchHostsProtectStatusRequestInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SwitchHostsProtectStatusRequestInfo.

        HSS配额ID，不填该参数时，则随机选择对应版本配额

        :return: The resource_id of this SwitchHostsProtectStatusRequestInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SwitchHostsProtectStatusRequestInfo.

        HSS配额ID，不填该参数时，则随机选择对应版本配额

        :param resource_id: The resource_id of this SwitchHostsProtectStatusRequestInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SwitchHostsProtectStatusRequestInfo.

        服务器列表

        :return: The host_id_list of this SwitchHostsProtectStatusRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SwitchHostsProtectStatusRequestInfo.

        服务器列表

        :param host_id_list: The host_id_list of this SwitchHostsProtectStatusRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def tags(self):
        r"""Gets the tags of this SwitchHostsProtectStatusRequestInfo.

        资源标签列表

        :return: The tags of this SwitchHostsProtectStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SwitchHostsProtectStatusRequestInfo.

        资源标签列表

        :param tags: The tags of this SwitchHostsProtectStatusRequestInfo.
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        self._tags = tags

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
        if not isinstance(other, SwitchHostsProtectStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
