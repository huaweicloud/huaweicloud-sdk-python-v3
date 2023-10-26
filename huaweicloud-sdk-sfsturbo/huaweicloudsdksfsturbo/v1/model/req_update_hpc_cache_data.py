# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqUpdateHpcCacheData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gc_time': 'int',
        'ck_time': 'int',
        'nas': 'list[ConfigNasTarget]',
        'obs': 'list[ConfigObsTarget]'
    }

    attribute_map = {
        'gc_time': 'gc_time',
        'ck_time': 'ck_time',
        'nas': 'nas',
        'obs': 'obs'
    }

    def __init__(self, gc_time=None, ck_time=None, nas=None, obs=None):
        """ReqUpdateHpcCacheData

        The model defined in huaweicloud sdk

        :param gc_time: 冷数据淘汰时间。单位：小时。指定时间内线上缓存的数据如果没有被访问则会自动从缓存中删除。0表示数据不会因为时间原因自动从缓存中删除。
        :type gc_time: int
        :param ck_time: 后端校验时间。单位：秒。指定时间间隔进行线上缓存文件与后端存储文件比较，存在变化则自动更新。0表示文件进行实时校验。
        :type ck_time: int
        :param nas: 配置 nas 后端的信息, 和 obs 字段为二选一的关系
        :type nas: list[:class:`huaweicloudsdksfsturbo.v1.ConfigNasTarget`]
        :param obs: 配置 obs 后端的信息, 和 nas 字段为二选一的关系
        :type obs: list[:class:`huaweicloudsdksfsturbo.v1.ConfigObsTarget`]
        """
        
        

        self._gc_time = None
        self._ck_time = None
        self._nas = None
        self._obs = None
        self.discriminator = None

        self.gc_time = gc_time
        self.ck_time = ck_time
        if nas is not None:
            self.nas = nas
        if obs is not None:
            self.obs = obs

    @property
    def gc_time(self):
        """Gets the gc_time of this ReqUpdateHpcCacheData.

        冷数据淘汰时间。单位：小时。指定时间内线上缓存的数据如果没有被访问则会自动从缓存中删除。0表示数据不会因为时间原因自动从缓存中删除。

        :return: The gc_time of this ReqUpdateHpcCacheData.
        :rtype: int
        """
        return self._gc_time

    @gc_time.setter
    def gc_time(self, gc_time):
        """Sets the gc_time of this ReqUpdateHpcCacheData.

        冷数据淘汰时间。单位：小时。指定时间内线上缓存的数据如果没有被访问则会自动从缓存中删除。0表示数据不会因为时间原因自动从缓存中删除。

        :param gc_time: The gc_time of this ReqUpdateHpcCacheData.
        :type gc_time: int
        """
        self._gc_time = gc_time

    @property
    def ck_time(self):
        """Gets the ck_time of this ReqUpdateHpcCacheData.

        后端校验时间。单位：秒。指定时间间隔进行线上缓存文件与后端存储文件比较，存在变化则自动更新。0表示文件进行实时校验。

        :return: The ck_time of this ReqUpdateHpcCacheData.
        :rtype: int
        """
        return self._ck_time

    @ck_time.setter
    def ck_time(self, ck_time):
        """Sets the ck_time of this ReqUpdateHpcCacheData.

        后端校验时间。单位：秒。指定时间间隔进行线上缓存文件与后端存储文件比较，存在变化则自动更新。0表示文件进行实时校验。

        :param ck_time: The ck_time of this ReqUpdateHpcCacheData.
        :type ck_time: int
        """
        self._ck_time = ck_time

    @property
    def nas(self):
        """Gets the nas of this ReqUpdateHpcCacheData.

        配置 nas 后端的信息, 和 obs 字段为二选一的关系

        :return: The nas of this ReqUpdateHpcCacheData.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ConfigNasTarget`]
        """
        return self._nas

    @nas.setter
    def nas(self, nas):
        """Sets the nas of this ReqUpdateHpcCacheData.

        配置 nas 后端的信息, 和 obs 字段为二选一的关系

        :param nas: The nas of this ReqUpdateHpcCacheData.
        :type nas: list[:class:`huaweicloudsdksfsturbo.v1.ConfigNasTarget`]
        """
        self._nas = nas

    @property
    def obs(self):
        """Gets the obs of this ReqUpdateHpcCacheData.

        配置 obs 后端的信息, 和 nas 字段为二选一的关系

        :return: The obs of this ReqUpdateHpcCacheData.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ConfigObsTarget`]
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this ReqUpdateHpcCacheData.

        配置 obs 后端的信息, 和 nas 字段为二选一的关系

        :param obs: The obs of this ReqUpdateHpcCacheData.
        :type obs: list[:class:`huaweicloudsdksfsturbo.v1.ConfigObsTarget`]
        """
        self._obs = obs

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
        if not isinstance(other, ReqUpdateHpcCacheData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
