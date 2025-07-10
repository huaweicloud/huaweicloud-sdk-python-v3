# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatMappingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_map_type': 'str',
        'nat_map_value': 'str',
        'nat_ip': 'str',
        'nat_port': 'str',
        'vag_ip': 'str',
        'access_filter_type': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'nat_map_type': 'nat_map_type',
        'nat_map_value': 'nat_map_value',
        'nat_ip': 'nat_ip',
        'nat_port': 'nat_port',
        'vag_ip': 'vag_ip',
        'access_filter_type': 'access_filter_type',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, nat_map_type=None, nat_map_value=None, nat_ip=None, nat_port=None, vag_ip=None, access_filter_type=None, enterprise_project_id=None, tags=None):
        r"""UpdateNatMappingConfig

        The model defined in huaweicloud sdk

        :param nat_map_type: NAT映射类型。 - PORT:端口映射. - HOST:地址映射,最多支持配置10个地址.
        :type nat_map_type: str
        :param nat_map_value: nat_map_type为PORT时表示端口,取值9443/9445. nat_map_type为HOST时表示接入地址.
        :type nat_map_value: str
        :param nat_ip: nat Ip。
        :type nat_ip: str
        :param nat_port: nat端口,取值范围0-65535。
        :type nat_port: str
        :param vag_ip: vag Ip。
        :type vag_ip: str
        :param access_filter_type: 是否支持标签、企业项目管理。0表示不开启，1表示开启。
        :type access_filter_type: int
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param tags: 标签对象。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        
        

        self._nat_map_type = None
        self._nat_map_value = None
        self._nat_ip = None
        self._nat_port = None
        self._vag_ip = None
        self._access_filter_type = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if nat_map_type is not None:
            self.nat_map_type = nat_map_type
        if nat_map_value is not None:
            self.nat_map_value = nat_map_value
        if nat_ip is not None:
            self.nat_ip = nat_ip
        if nat_port is not None:
            self.nat_port = nat_port
        if vag_ip is not None:
            self.vag_ip = vag_ip
        if access_filter_type is not None:
            self.access_filter_type = access_filter_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def nat_map_type(self):
        r"""Gets the nat_map_type of this UpdateNatMappingConfig.

        NAT映射类型。 - PORT:端口映射. - HOST:地址映射,最多支持配置10个地址.

        :return: The nat_map_type of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._nat_map_type

    @nat_map_type.setter
    def nat_map_type(self, nat_map_type):
        r"""Sets the nat_map_type of this UpdateNatMappingConfig.

        NAT映射类型。 - PORT:端口映射. - HOST:地址映射,最多支持配置10个地址.

        :param nat_map_type: The nat_map_type of this UpdateNatMappingConfig.
        :type nat_map_type: str
        """
        self._nat_map_type = nat_map_type

    @property
    def nat_map_value(self):
        r"""Gets the nat_map_value of this UpdateNatMappingConfig.

        nat_map_type为PORT时表示端口,取值9443/9445. nat_map_type为HOST时表示接入地址.

        :return: The nat_map_value of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._nat_map_value

    @nat_map_value.setter
    def nat_map_value(self, nat_map_value):
        r"""Sets the nat_map_value of this UpdateNatMappingConfig.

        nat_map_type为PORT时表示端口,取值9443/9445. nat_map_type为HOST时表示接入地址.

        :param nat_map_value: The nat_map_value of this UpdateNatMappingConfig.
        :type nat_map_value: str
        """
        self._nat_map_value = nat_map_value

    @property
    def nat_ip(self):
        r"""Gets the nat_ip of this UpdateNatMappingConfig.

        nat Ip。

        :return: The nat_ip of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._nat_ip

    @nat_ip.setter
    def nat_ip(self, nat_ip):
        r"""Sets the nat_ip of this UpdateNatMappingConfig.

        nat Ip。

        :param nat_ip: The nat_ip of this UpdateNatMappingConfig.
        :type nat_ip: str
        """
        self._nat_ip = nat_ip

    @property
    def nat_port(self):
        r"""Gets the nat_port of this UpdateNatMappingConfig.

        nat端口,取值范围0-65535。

        :return: The nat_port of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._nat_port

    @nat_port.setter
    def nat_port(self, nat_port):
        r"""Sets the nat_port of this UpdateNatMappingConfig.

        nat端口,取值范围0-65535。

        :param nat_port: The nat_port of this UpdateNatMappingConfig.
        :type nat_port: str
        """
        self._nat_port = nat_port

    @property
    def vag_ip(self):
        r"""Gets the vag_ip of this UpdateNatMappingConfig.

        vag Ip。

        :return: The vag_ip of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._vag_ip

    @vag_ip.setter
    def vag_ip(self, vag_ip):
        r"""Sets the vag_ip of this UpdateNatMappingConfig.

        vag Ip。

        :param vag_ip: The vag_ip of this UpdateNatMappingConfig.
        :type vag_ip: str
        """
        self._vag_ip = vag_ip

    @property
    def access_filter_type(self):
        r"""Gets the access_filter_type of this UpdateNatMappingConfig.

        是否支持标签、企业项目管理。0表示不开启，1表示开启。

        :return: The access_filter_type of this UpdateNatMappingConfig.
        :rtype: int
        """
        return self._access_filter_type

    @access_filter_type.setter
    def access_filter_type(self, access_filter_type):
        r"""Sets the access_filter_type of this UpdateNatMappingConfig.

        是否支持标签、企业项目管理。0表示不开启，1表示开启。

        :param access_filter_type: The access_filter_type of this UpdateNatMappingConfig.
        :type access_filter_type: int
        """
        self._access_filter_type = access_filter_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateNatMappingConfig.

        企业项目ID。

        :return: The enterprise_project_id of this UpdateNatMappingConfig.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateNatMappingConfig.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this UpdateNatMappingConfig.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this UpdateNatMappingConfig.

        标签对象。

        :return: The tags of this UpdateNatMappingConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateNatMappingConfig.

        标签对象。

        :param tags: The tags of this UpdateNatMappingConfig.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
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
        if not isinstance(other, UpdateNatMappingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
