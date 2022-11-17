# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRomaInstanceListV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'instances': 'list[RomaInstanceCheckListRespInstances]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'instances': 'instances'
    }

    def __init__(self, total=None, size=None, instances=None):
        """CheckRomaInstanceListV2Response

        The model defined in huaweicloud sdk

        :param total: 列表总数
        :type total: int
        :param size: 本页数量
        :type size: int
        :param instances: 实例列表
        :type instances: list[:class:`huaweicloudsdkroma.v2.RomaInstanceCheckListRespInstances`]
        """
        
        super(CheckRomaInstanceListV2Response, self).__init__()

        self._total = None
        self._size = None
        self._instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if instances is not None:
            self.instances = instances

    @property
    def total(self):
        """Gets the total of this CheckRomaInstanceListV2Response.

        列表总数

        :return: The total of this CheckRomaInstanceListV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CheckRomaInstanceListV2Response.

        列表总数

        :param total: The total of this CheckRomaInstanceListV2Response.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this CheckRomaInstanceListV2Response.

        本页数量

        :return: The size of this CheckRomaInstanceListV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CheckRomaInstanceListV2Response.

        本页数量

        :param size: The size of this CheckRomaInstanceListV2Response.
        :type size: int
        """
        self._size = size

    @property
    def instances(self):
        """Gets the instances of this CheckRomaInstanceListV2Response.

        实例列表

        :return: The instances of this CheckRomaInstanceListV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.RomaInstanceCheckListRespInstances`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this CheckRomaInstanceListV2Response.

        实例列表

        :param instances: The instances of this CheckRomaInstanceListV2Response.
        :type instances: list[:class:`huaweicloudsdkroma.v2.RomaInstanceCheckListRespInstances`]
        """
        self._instances = instances

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
        if not isinstance(other, CheckRomaInstanceListV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
