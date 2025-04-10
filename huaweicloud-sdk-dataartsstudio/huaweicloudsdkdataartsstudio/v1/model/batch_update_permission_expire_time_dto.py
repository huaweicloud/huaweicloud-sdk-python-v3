# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePermissionExpireTimeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'expire_time': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        'expire_time': 'expire_time'
    }

    def __init__(self, ids=None, expire_time=None):
        r"""BatchUpdatePermissionExpireTimeDTO

        The model defined in huaweicloud sdk

        :param ids: 数据密级id列表，数据密级id可以通过查询接口获取。
        :type ids: list[str]
        :param expire_time: 到期时间
        :type expire_time: int
        """
        
        

        self._ids = None
        self._expire_time = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def ids(self):
        r"""Gets the ids of this BatchUpdatePermissionExpireTimeDTO.

        数据密级id列表，数据密级id可以通过查询接口获取。

        :return: The ids of this BatchUpdatePermissionExpireTimeDTO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchUpdatePermissionExpireTimeDTO.

        数据密级id列表，数据密级id可以通过查询接口获取。

        :param ids: The ids of this BatchUpdatePermissionExpireTimeDTO.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def expire_time(self):
        r"""Gets the expire_time of this BatchUpdatePermissionExpireTimeDTO.

        到期时间

        :return: The expire_time of this BatchUpdatePermissionExpireTimeDTO.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this BatchUpdatePermissionExpireTimeDTO.

        到期时间

        :param expire_time: The expire_time of this BatchUpdatePermissionExpireTimeDTO.
        :type expire_time: int
        """
        self._expire_time = expire_time

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
        if not isinstance(other, BatchUpdatePermissionExpireTimeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
