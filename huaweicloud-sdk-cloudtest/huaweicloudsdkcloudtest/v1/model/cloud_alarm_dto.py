# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudAlarmDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_name': 'str',
        'cloud_service_region_id': 'str',
        'cloud_service_site': 'str',
        'enable': 'str',
        'level': 'str',
        'micro_service_group_name': 'str',
        'micro_service_name': 'str'
    }

    attribute_map = {
        'cloud_service_name': 'cloudServiceName',
        'cloud_service_region_id': 'cloudServiceRegionId',
        'cloud_service_site': 'cloudServiceSite',
        'enable': 'enable',
        'level': 'level',
        'micro_service_group_name': 'microServiceGroupName',
        'micro_service_name': 'microServiceName'
    }

    def __init__(self, cloud_service_name=None, cloud_service_region_id=None, cloud_service_site=None, enable=None, level=None, micro_service_group_name=None, micro_service_name=None):
        r"""CloudAlarmDto

        The model defined in huaweicloud sdk

        :param cloud_service_name: 云服务名称
        :type cloud_service_name: str
        :param cloud_service_region_id: 云服务区域标识
        :type cloud_service_region_id: str
        :param cloud_service_site: 云服务站点：默认中国站
        :type cloud_service_site: str
        :param enable: 是否开启CloudAlarm配置
        :type enable: str
        :param level: 告警级别
        :type level: str
        :param micro_service_group_name: 微服务组名称
        :type micro_service_group_name: str
        :param micro_service_name: 微服务名称
        :type micro_service_name: str
        """
        
        

        self._cloud_service_name = None
        self._cloud_service_region_id = None
        self._cloud_service_site = None
        self._enable = None
        self._level = None
        self._micro_service_group_name = None
        self._micro_service_name = None
        self.discriminator = None

        if cloud_service_name is not None:
            self.cloud_service_name = cloud_service_name
        if cloud_service_region_id is not None:
            self.cloud_service_region_id = cloud_service_region_id
        if cloud_service_site is not None:
            self.cloud_service_site = cloud_service_site
        if enable is not None:
            self.enable = enable
        if level is not None:
            self.level = level
        if micro_service_group_name is not None:
            self.micro_service_group_name = micro_service_group_name
        if micro_service_name is not None:
            self.micro_service_name = micro_service_name

    @property
    def cloud_service_name(self):
        r"""Gets the cloud_service_name of this CloudAlarmDto.

        云服务名称

        :return: The cloud_service_name of this CloudAlarmDto.
        :rtype: str
        """
        return self._cloud_service_name

    @cloud_service_name.setter
    def cloud_service_name(self, cloud_service_name):
        r"""Sets the cloud_service_name of this CloudAlarmDto.

        云服务名称

        :param cloud_service_name: The cloud_service_name of this CloudAlarmDto.
        :type cloud_service_name: str
        """
        self._cloud_service_name = cloud_service_name

    @property
    def cloud_service_region_id(self):
        r"""Gets the cloud_service_region_id of this CloudAlarmDto.

        云服务区域标识

        :return: The cloud_service_region_id of this CloudAlarmDto.
        :rtype: str
        """
        return self._cloud_service_region_id

    @cloud_service_region_id.setter
    def cloud_service_region_id(self, cloud_service_region_id):
        r"""Sets the cloud_service_region_id of this CloudAlarmDto.

        云服务区域标识

        :param cloud_service_region_id: The cloud_service_region_id of this CloudAlarmDto.
        :type cloud_service_region_id: str
        """
        self._cloud_service_region_id = cloud_service_region_id

    @property
    def cloud_service_site(self):
        r"""Gets the cloud_service_site of this CloudAlarmDto.

        云服务站点：默认中国站

        :return: The cloud_service_site of this CloudAlarmDto.
        :rtype: str
        """
        return self._cloud_service_site

    @cloud_service_site.setter
    def cloud_service_site(self, cloud_service_site):
        r"""Sets the cloud_service_site of this CloudAlarmDto.

        云服务站点：默认中国站

        :param cloud_service_site: The cloud_service_site of this CloudAlarmDto.
        :type cloud_service_site: str
        """
        self._cloud_service_site = cloud_service_site

    @property
    def enable(self):
        r"""Gets the enable of this CloudAlarmDto.

        是否开启CloudAlarm配置

        :return: The enable of this CloudAlarmDto.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CloudAlarmDto.

        是否开启CloudAlarm配置

        :param enable: The enable of this CloudAlarmDto.
        :type enable: str
        """
        self._enable = enable

    @property
    def level(self):
        r"""Gets the level of this CloudAlarmDto.

        告警级别

        :return: The level of this CloudAlarmDto.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CloudAlarmDto.

        告警级别

        :param level: The level of this CloudAlarmDto.
        :type level: str
        """
        self._level = level

    @property
    def micro_service_group_name(self):
        r"""Gets the micro_service_group_name of this CloudAlarmDto.

        微服务组名称

        :return: The micro_service_group_name of this CloudAlarmDto.
        :rtype: str
        """
        return self._micro_service_group_name

    @micro_service_group_name.setter
    def micro_service_group_name(self, micro_service_group_name):
        r"""Sets the micro_service_group_name of this CloudAlarmDto.

        微服务组名称

        :param micro_service_group_name: The micro_service_group_name of this CloudAlarmDto.
        :type micro_service_group_name: str
        """
        self._micro_service_group_name = micro_service_group_name

    @property
    def micro_service_name(self):
        r"""Gets the micro_service_name of this CloudAlarmDto.

        微服务名称

        :return: The micro_service_name of this CloudAlarmDto.
        :rtype: str
        """
        return self._micro_service_name

    @micro_service_name.setter
    def micro_service_name(self, micro_service_name):
        r"""Sets the micro_service_name of this CloudAlarmDto.

        微服务名称

        :param micro_service_name: The micro_service_name of this CloudAlarmDto.
        :type micro_service_name: str
        """
        self._micro_service_name = micro_service_name

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
        if not isinstance(other, CloudAlarmDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
