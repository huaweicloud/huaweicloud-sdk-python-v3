# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoscalePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'autoscale_type': 'str',
        'max_auto_created': 'int',
        'min_idle': 'int',
        'once_auto_created': 'int'
    }

    attribute_map = {
        'autoscale_type': 'autoscale_type',
        'max_auto_created': 'max_auto_created',
        'min_idle': 'min_idle',
        'once_auto_created': 'once_auto_created'
    }

    def __init__(self, autoscale_type=None, max_auto_created=None, min_idle=None, once_auto_created=None):
        r"""AutoscalePolicy

        The model defined in huaweicloud sdk

        :param autoscale_type: 弹性伸缩类型，ACCESS_CREATED：接入时创建，AUTO_CREATED：弹性伸缩。
        :type autoscale_type: str
        :param max_auto_created: 自动创建桌面上限。
        :type max_auto_created: int
        :param min_idle: 空闲桌面低于多少时开始自动创建桌面。
        :type min_idle: int
        :param once_auto_created: 一次自动创建桌面的数量。
        :type once_auto_created: int
        """
        
        

        self._autoscale_type = None
        self._max_auto_created = None
        self._min_idle = None
        self._once_auto_created = None
        self.discriminator = None

        if autoscale_type is not None:
            self.autoscale_type = autoscale_type
        if max_auto_created is not None:
            self.max_auto_created = max_auto_created
        if min_idle is not None:
            self.min_idle = min_idle
        if once_auto_created is not None:
            self.once_auto_created = once_auto_created

    @property
    def autoscale_type(self):
        r"""Gets the autoscale_type of this AutoscalePolicy.

        弹性伸缩类型，ACCESS_CREATED：接入时创建，AUTO_CREATED：弹性伸缩。

        :return: The autoscale_type of this AutoscalePolicy.
        :rtype: str
        """
        return self._autoscale_type

    @autoscale_type.setter
    def autoscale_type(self, autoscale_type):
        r"""Sets the autoscale_type of this AutoscalePolicy.

        弹性伸缩类型，ACCESS_CREATED：接入时创建，AUTO_CREATED：弹性伸缩。

        :param autoscale_type: The autoscale_type of this AutoscalePolicy.
        :type autoscale_type: str
        """
        self._autoscale_type = autoscale_type

    @property
    def max_auto_created(self):
        r"""Gets the max_auto_created of this AutoscalePolicy.

        自动创建桌面上限。

        :return: The max_auto_created of this AutoscalePolicy.
        :rtype: int
        """
        return self._max_auto_created

    @max_auto_created.setter
    def max_auto_created(self, max_auto_created):
        r"""Sets the max_auto_created of this AutoscalePolicy.

        自动创建桌面上限。

        :param max_auto_created: The max_auto_created of this AutoscalePolicy.
        :type max_auto_created: int
        """
        self._max_auto_created = max_auto_created

    @property
    def min_idle(self):
        r"""Gets the min_idle of this AutoscalePolicy.

        空闲桌面低于多少时开始自动创建桌面。

        :return: The min_idle of this AutoscalePolicy.
        :rtype: int
        """
        return self._min_idle

    @min_idle.setter
    def min_idle(self, min_idle):
        r"""Sets the min_idle of this AutoscalePolicy.

        空闲桌面低于多少时开始自动创建桌面。

        :param min_idle: The min_idle of this AutoscalePolicy.
        :type min_idle: int
        """
        self._min_idle = min_idle

    @property
    def once_auto_created(self):
        r"""Gets the once_auto_created of this AutoscalePolicy.

        一次自动创建桌面的数量。

        :return: The once_auto_created of this AutoscalePolicy.
        :rtype: int
        """
        return self._once_auto_created

    @once_auto_created.setter
    def once_auto_created(self, once_auto_created):
        r"""Sets the once_auto_created of this AutoscalePolicy.

        一次自动创建桌面的数量。

        :param once_auto_created: The once_auto_created of this AutoscalePolicy.
        :type once_auto_created: int
        """
        self._once_auto_created = once_auto_created

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
        if not isinstance(other, AutoscalePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
