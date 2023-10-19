# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpRegionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'description_cn': 'str',
        'description_en': 'str',
        'region_type': 'int'
    }

    attribute_map = {
        'region_id': 'region_id',
        'description_cn': 'description_cn',
        'description_en': 'description_en',
        'region_type': 'region_type'
    }

    def __init__(self, region_id=None, description_cn=None, description_en=None, region_type=None):
        """IpRegionDto

        The model defined in huaweicloud sdk

        :param region_id: 区域id
        :type region_id: str
        :param description_cn: 中文描述
        :type description_cn: str
        :param description_en: 英文描述
        :type description_en: str
        :param region_type: 区域类型，0表示国家，1表示省份，2表示大洲
        :type region_type: int
        """
        
        

        self._region_id = None
        self._description_cn = None
        self._description_en = None
        self._region_type = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if description_cn is not None:
            self.description_cn = description_cn
        if description_en is not None:
            self.description_en = description_en
        if region_type is not None:
            self.region_type = region_type

    @property
    def region_id(self):
        """Gets the region_id of this IpRegionDto.

        区域id

        :return: The region_id of this IpRegionDto.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this IpRegionDto.

        区域id

        :param region_id: The region_id of this IpRegionDto.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def description_cn(self):
        """Gets the description_cn of this IpRegionDto.

        中文描述

        :return: The description_cn of this IpRegionDto.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this IpRegionDto.

        中文描述

        :param description_cn: The description_cn of this IpRegionDto.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def description_en(self):
        """Gets the description_en of this IpRegionDto.

        英文描述

        :return: The description_en of this IpRegionDto.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        """Sets the description_en of this IpRegionDto.

        英文描述

        :param description_en: The description_en of this IpRegionDto.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def region_type(self):
        """Gets the region_type of this IpRegionDto.

        区域类型，0表示国家，1表示省份，2表示大洲

        :return: The region_type of this IpRegionDto.
        :rtype: int
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this IpRegionDto.

        区域类型，0表示国家，1表示省份，2表示大洲

        :param region_type: The region_type of this IpRegionDto.
        :type region_type: int
        """
        self._region_type = region_type

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
        if not isinstance(other, IpRegionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
