# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCorpDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CorpBasicDTO',
        'admin_info': 'AdminDTO',
        'res_info': 'AddCorpResDTO',
        'group_id': 'str',
        'property_info': 'list[OrgPropertyDTO]'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'admin_info': 'adminInfo',
        'res_info': 'resInfo',
        'group_id': 'groupId',
        'property_info': 'propertyInfo'
    }

    def __init__(self, basic_info=None, admin_info=None, res_info=None, group_id=None, property_info=None):
        r"""AddCorpDTO

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.CorpBasicDTO`
        :param admin_info: 
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.AdminDTO`
        :param res_info: 
        :type res_info: :class:`huaweicloudsdkmeeting.v1.AddCorpResDTO`
        :param group_id: 媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。
        :type group_id: str
        :param property_info: 可配置项信息。
        :type property_info: list[:class:`huaweicloudsdkmeeting.v1.OrgPropertyDTO`]
        """
        
        

        self._basic_info = None
        self._admin_info = None
        self._res_info = None
        self._group_id = None
        self._property_info = None
        self.discriminator = None

        self.basic_info = basic_info
        self.admin_info = admin_info
        if res_info is not None:
            self.res_info = res_info
        if group_id is not None:
            self.group_id = group_id
        if property_info is not None:
            self.property_info = property_info

    @property
    def basic_info(self):
        r"""Gets the basic_info of this AddCorpDTO.

        :return: The basic_info of this AddCorpDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CorpBasicDTO`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this AddCorpDTO.

        :param basic_info: The basic_info of this AddCorpDTO.
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.CorpBasicDTO`
        """
        self._basic_info = basic_info

    @property
    def admin_info(self):
        r"""Gets the admin_info of this AddCorpDTO.

        :return: The admin_info of this AddCorpDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.AdminDTO`
        """
        return self._admin_info

    @admin_info.setter
    def admin_info(self, admin_info):
        r"""Sets the admin_info of this AddCorpDTO.

        :param admin_info: The admin_info of this AddCorpDTO.
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.AdminDTO`
        """
        self._admin_info = admin_info

    @property
    def res_info(self):
        r"""Gets the res_info of this AddCorpDTO.

        :return: The res_info of this AddCorpDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.AddCorpResDTO`
        """
        return self._res_info

    @res_info.setter
    def res_info(self, res_info):
        r"""Sets the res_info of this AddCorpDTO.

        :param res_info: The res_info of this AddCorpDTO.
        :type res_info: :class:`huaweicloudsdkmeeting.v1.AddCorpResDTO`
        """
        self._res_info = res_info

    @property
    def group_id(self):
        r"""Gets the group_id of this AddCorpDTO.

        媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。

        :return: The group_id of this AddCorpDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddCorpDTO.

        媒体接入（包括SBC和MCU）分组id，可通过[[SP管理员查询资源信息](https://support.huaweicloud.com/api-meeting/meeting_21_1537.html)](tag:hws)[[SP管理员查询资源信息](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1537.html)](tag:hk)接口查询获取。

        :param group_id: The group_id of this AddCorpDTO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def property_info(self):
        r"""Gets the property_info of this AddCorpDTO.

        可配置项信息。

        :return: The property_info of this AddCorpDTO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.OrgPropertyDTO`]
        """
        return self._property_info

    @property_info.setter
    def property_info(self, property_info):
        r"""Sets the property_info of this AddCorpDTO.

        可配置项信息。

        :param property_info: The property_info of this AddCorpDTO.
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
        if not isinstance(other, AddCorpDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
