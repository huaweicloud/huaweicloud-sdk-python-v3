# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareBandwidthTypeShowResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'bandwidth_type': 'str',
        'public_border_group': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'name_en': 'str',
        'name_zh': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'bandwidth_type': 'bandwidth_type',
        'public_border_group': 'public_border_group',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'name_en': 'name_en',
        'name_zh': 'name_zh',
        'description': 'description'
    }

    def __init__(self, id=None, bandwidth_type=None, public_border_group=None, created_at=None, updated_at=None, name_en=None, name_zh=None, description=None):
        """ShareBandwidthTypeShowResp

        The model defined in huaweicloud sdk

        :param id: 支持带宽类型的id
        :type id: str
        :param bandwidth_type: 带宽类型
        :type bandwidth_type: str
        :param public_border_group: 中心站点or边缘站点，默认展示
        :type public_border_group: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param name_en: 带宽类型的英文表述
        :type name_en: str
        :param name_zh: 带宽类型的中文表述
        :type name_zh: str
        :param description: 带宽类型描述信息
        :type description: str
        """
        
        

        self._id = None
        self._bandwidth_type = None
        self._public_border_group = None
        self._created_at = None
        self._updated_at = None
        self._name_en = None
        self._name_zh = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if name_en is not None:
            self.name_en = name_en
        if name_zh is not None:
            self.name_zh = name_zh
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ShareBandwidthTypeShowResp.

        支持带宽类型的id

        :return: The id of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShareBandwidthTypeShowResp.

        支持带宽类型的id

        :param id: The id of this ShareBandwidthTypeShowResp.
        :type id: str
        """
        self._id = id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this ShareBandwidthTypeShowResp.

        带宽类型

        :return: The bandwidth_type of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this ShareBandwidthTypeShowResp.

        带宽类型

        :param bandwidth_type: The bandwidth_type of this ShareBandwidthTypeShowResp.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ShareBandwidthTypeShowResp.

        中心站点or边缘站点，默认展示

        :return: The public_border_group of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ShareBandwidthTypeShowResp.

        中心站点or边缘站点，默认展示

        :param public_border_group: The public_border_group of this ShareBandwidthTypeShowResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def created_at(self):
        """Gets the created_at of this ShareBandwidthTypeShowResp.

        创建时间

        :return: The created_at of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShareBandwidthTypeShowResp.

        创建时间

        :param created_at: The created_at of this ShareBandwidthTypeShowResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShareBandwidthTypeShowResp.

        更新时间

        :return: The updated_at of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShareBandwidthTypeShowResp.

        更新时间

        :param updated_at: The updated_at of this ShareBandwidthTypeShowResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def name_en(self):
        """Gets the name_en of this ShareBandwidthTypeShowResp.

        带宽类型的英文表述

        :return: The name_en of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this ShareBandwidthTypeShowResp.

        带宽类型的英文表述

        :param name_en: The name_en of this ShareBandwidthTypeShowResp.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_zh(self):
        """Gets the name_zh of this ShareBandwidthTypeShowResp.

        带宽类型的中文表述

        :return: The name_zh of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        """Sets the name_zh of this ShareBandwidthTypeShowResp.

        带宽类型的中文表述

        :param name_zh: The name_zh of this ShareBandwidthTypeShowResp.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def description(self):
        """Gets the description of this ShareBandwidthTypeShowResp.

        带宽类型描述信息

        :return: The description of this ShareBandwidthTypeShowResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShareBandwidthTypeShowResp.

        带宽类型描述信息

        :param description: The description of this ShareBandwidthTypeShowResp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ShareBandwidthTypeShowResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
