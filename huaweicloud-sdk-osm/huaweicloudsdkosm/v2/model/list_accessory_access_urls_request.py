# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessoryAccessUrlsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'accessory_ids': 'list[str]',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'accessory_ids': 'accessory_ids',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, group_id=None, accessory_ids=None, x_site=None, x_language=None, x_time_zone=None):
        """ListAccessoryAccessUrlsRequest

        The model defined in huaweicloud sdk

        :param group_id: 组id
        :type group_id: str
        :param accessory_ids: 附件id列表
        :type accessory_ids: list[str]
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._group_id = None
        self._accessory_ids = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.group_id = group_id
        self.accessory_ids = accessory_ids
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def group_id(self):
        """Gets the group_id of this ListAccessoryAccessUrlsRequest.

        组id

        :return: The group_id of this ListAccessoryAccessUrlsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListAccessoryAccessUrlsRequest.

        组id

        :param group_id: The group_id of this ListAccessoryAccessUrlsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def accessory_ids(self):
        """Gets the accessory_ids of this ListAccessoryAccessUrlsRequest.

        附件id列表

        :return: The accessory_ids of this ListAccessoryAccessUrlsRequest.
        :rtype: list[str]
        """
        return self._accessory_ids

    @accessory_ids.setter
    def accessory_ids(self, accessory_ids):
        """Sets the accessory_ids of this ListAccessoryAccessUrlsRequest.

        附件id列表

        :param accessory_ids: The accessory_ids of this ListAccessoryAccessUrlsRequest.
        :type accessory_ids: list[str]
        """
        self._accessory_ids = accessory_ids

    @property
    def x_site(self):
        """Gets the x_site of this ListAccessoryAccessUrlsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListAccessoryAccessUrlsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListAccessoryAccessUrlsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListAccessoryAccessUrlsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListAccessoryAccessUrlsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListAccessoryAccessUrlsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListAccessoryAccessUrlsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListAccessoryAccessUrlsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListAccessoryAccessUrlsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListAccessoryAccessUrlsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListAccessoryAccessUrlsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListAccessoryAccessUrlsRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, ListAccessoryAccessUrlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
