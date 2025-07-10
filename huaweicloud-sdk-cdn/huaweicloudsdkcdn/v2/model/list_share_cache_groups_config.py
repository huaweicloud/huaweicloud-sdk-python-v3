# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareCacheGroupsConfig:

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
        'group_name': 'str',
        'create_time': 'int',
        'share_cache_records': 'list[ListShareCacheGroupsRecord]',
        'primary_domain': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_name': 'group_name',
        'create_time': 'create_time',
        'share_cache_records': 'share_cache_records',
        'primary_domain': 'primary_domain'
    }

    def __init__(self, id=None, group_name=None, create_time=None, share_cache_records=None, primary_domain=None):
        r"""ListShareCacheGroupsConfig

        The model defined in huaweicloud sdk

        :param id: 共享缓存ID
        :type id: str
        :param group_name: 共享缓存组名
        :type group_name: str
        :param create_time: 共享缓存创建时间
        :type create_time: int
        :param share_cache_records: 共享缓存域名记录
        :type share_cache_records: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsRecord`]
        :param primary_domain: 共享缓存组主域名
        :type primary_domain: str
        """
        
        

        self._id = None
        self._group_name = None
        self._create_time = None
        self._share_cache_records = None
        self._primary_domain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_name is not None:
            self.group_name = group_name
        if create_time is not None:
            self.create_time = create_time
        if share_cache_records is not None:
            self.share_cache_records = share_cache_records
        if primary_domain is not None:
            self.primary_domain = primary_domain

    @property
    def id(self):
        r"""Gets the id of this ListShareCacheGroupsConfig.

        共享缓存ID

        :return: The id of this ListShareCacheGroupsConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListShareCacheGroupsConfig.

        共享缓存ID

        :param id: The id of this ListShareCacheGroupsConfig.
        :type id: str
        """
        self._id = id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListShareCacheGroupsConfig.

        共享缓存组名

        :return: The group_name of this ListShareCacheGroupsConfig.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListShareCacheGroupsConfig.

        共享缓存组名

        :param group_name: The group_name of this ListShareCacheGroupsConfig.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ListShareCacheGroupsConfig.

        共享缓存创建时间

        :return: The create_time of this ListShareCacheGroupsConfig.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListShareCacheGroupsConfig.

        共享缓存创建时间

        :param create_time: The create_time of this ListShareCacheGroupsConfig.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def share_cache_records(self):
        r"""Gets the share_cache_records of this ListShareCacheGroupsConfig.

        共享缓存域名记录

        :return: The share_cache_records of this ListShareCacheGroupsConfig.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsRecord`]
        """
        return self._share_cache_records

    @share_cache_records.setter
    def share_cache_records(self, share_cache_records):
        r"""Sets the share_cache_records of this ListShareCacheGroupsConfig.

        共享缓存域名记录

        :param share_cache_records: The share_cache_records of this ListShareCacheGroupsConfig.
        :type share_cache_records: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsRecord`]
        """
        self._share_cache_records = share_cache_records

    @property
    def primary_domain(self):
        r"""Gets the primary_domain of this ListShareCacheGroupsConfig.

        共享缓存组主域名

        :return: The primary_domain of this ListShareCacheGroupsConfig.
        :rtype: str
        """
        return self._primary_domain

    @primary_domain.setter
    def primary_domain(self, primary_domain):
        r"""Sets the primary_domain of this ListShareCacheGroupsConfig.

        共享缓存组主域名

        :param primary_domain: The primary_domain of this ListShareCacheGroupsConfig.
        :type primary_domain: str
        """
        self._primary_domain = primary_domain

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
        if not isinstance(other, ListShareCacheGroupsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
