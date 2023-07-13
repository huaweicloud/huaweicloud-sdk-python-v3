# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModCorpDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'ModCorpBasicDTO',
        'admin_info': 'ModAdminDTO',
        'group_id': 'str',
        'property_info': 'list[OrgPropertyDTO]'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'admin_info': 'adminInfo',
        'group_id': 'groupId',
        'property_info': 'propertyInfo'
    }

    def __init__(self, basic_info=None, admin_info=None, group_id=None, property_info=None):
        """ModCorpDTO

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.ModCorpBasicDTO`
        :param admin_info: 
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.ModAdminDTO`
        :param group_id: 媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。
        :type group_id: str
        :param property_info: 可配置项信息。
        :type property_info: list[:class:`huaweicloudsdkmeeting.v1.OrgPropertyDTO`]
        """
        
        

        self._basic_info = None
        self._admin_info = None
        self._group_id = None
        self._property_info = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if admin_info is not None:
            self.admin_info = admin_info
        if group_id is not None:
            self.group_id = group_id
        if property_info is not None:
            self.property_info = property_info

    @property
    def basic_info(self):
        """Gets the basic_info of this ModCorpDTO.

        :return: The basic_info of this ModCorpDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ModCorpBasicDTO`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ModCorpDTO.

        :param basic_info: The basic_info of this ModCorpDTO.
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.ModCorpBasicDTO`
        """
        self._basic_info = basic_info

    @property
    def admin_info(self):
        """Gets the admin_info of this ModCorpDTO.

        :return: The admin_info of this ModCorpDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ModAdminDTO`
        """
        return self._admin_info

    @admin_info.setter
    def admin_info(self, admin_info):
        """Sets the admin_info of this ModCorpDTO.

        :param admin_info: The admin_info of this ModCorpDTO.
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.ModAdminDTO`
        """
        self._admin_info = admin_info

    @property
    def group_id(self):
        """Gets the group_id of this ModCorpDTO.

        媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。

        :return: The group_id of this ModCorpDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ModCorpDTO.

        媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。

        :param group_id: The group_id of this ModCorpDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def property_info(self):
        """Gets the property_info of this ModCorpDTO.

        可配置项信息。

        :return: The property_info of this ModCorpDTO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.OrgPropertyDTO`]
        """
        return self._property_info

    @property_info.setter
    def property_info(self, property_info):
        """Sets the property_info of this ModCorpDTO.

        可配置项信息。

        :param property_info: The property_info of this ModCorpDTO.
        :type property_info: list[:class:`huaweicloudsdkmeeting.v1.OrgPropertyDTO`]
        """
        self._property_info = property_info

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
        if not isinstance(other, ModCorpDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
