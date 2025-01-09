# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAppsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[str]',
        'reserve_obs_file': 'bool'
    }

    attribute_map = {
        'items': 'items',
        'reserve_obs_file': 'reserve_obs_file'
    }

    def __init__(self, items=None, reserve_obs_file=None):
        """BatchDeleteAppsReq

        The model defined in huaweicloud sdk

        :param items: 批量唯一标识请求列表，一次请求数量区间 [1, 50]。
        :type items: list[str]
        :param reserve_obs_file: 是否保留OBS桶文件，如果不保留删除应用时，会同时删除OBS桶文件(默认false)。 * &#39;true&#39; - 保留OBS桶文件,不做任何操作。 * &#39;false&#39; - 不保留OBS桶文件,删除应用时同时删除OBS桶文件。
        :type reserve_obs_file: bool
        """
        
        

        self._items = None
        self._reserve_obs_file = None
        self.discriminator = None

        self.items = items
        if reserve_obs_file is not None:
            self.reserve_obs_file = reserve_obs_file

    @property
    def items(self):
        """Gets the items of this BatchDeleteAppsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 50]。

        :return: The items of this BatchDeleteAppsReq.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BatchDeleteAppsReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 50]。

        :param items: The items of this BatchDeleteAppsReq.
        :type items: list[str]
        """
        self._items = items

    @property
    def reserve_obs_file(self):
        """Gets the reserve_obs_file of this BatchDeleteAppsReq.

        是否保留OBS桶文件，如果不保留删除应用时，会同时删除OBS桶文件(默认false)。 * 'true' - 保留OBS桶文件,不做任何操作。 * 'false' - 不保留OBS桶文件,删除应用时同时删除OBS桶文件。

        :return: The reserve_obs_file of this BatchDeleteAppsReq.
        :rtype: bool
        """
        return self._reserve_obs_file

    @reserve_obs_file.setter
    def reserve_obs_file(self, reserve_obs_file):
        """Sets the reserve_obs_file of this BatchDeleteAppsReq.

        是否保留OBS桶文件，如果不保留删除应用时，会同时删除OBS桶文件(默认false)。 * 'true' - 保留OBS桶文件,不做任何操作。 * 'false' - 不保留OBS桶文件,删除应用时同时删除OBS桶文件。

        :param reserve_obs_file: The reserve_obs_file of this BatchDeleteAppsReq.
        :type reserve_obs_file: bool
        """
        self._reserve_obs_file = reserve_obs_file

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
        if not isinstance(other, BatchDeleteAppsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
