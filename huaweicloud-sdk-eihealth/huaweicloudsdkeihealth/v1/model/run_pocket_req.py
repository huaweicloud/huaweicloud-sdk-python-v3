# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPocketReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'center': 'list[float]',
        'size': 'list[float]',
        'padding': 'float'
    }

    attribute_map = {
        'center': 'center',
        'size': 'size',
        'padding': 'padding'
    }

    def __init__(self, center=None, size=None, padding=None):
        r"""RunPocketReq

        The model defined in huaweicloud sdk

        :param center: 口袋中心坐标
        :type center: list[float]
        :param size: 口袋大小
        :type size: list[float]
        :param padding: 口袋的padding值
        :type padding: float
        """
        
        

        self._center = None
        self._size = None
        self._padding = None
        self.discriminator = None

        self.center = center
        self.size = size
        self.padding = padding

    @property
    def center(self):
        r"""Gets the center of this RunPocketReq.

        口袋中心坐标

        :return: The center of this RunPocketReq.
        :rtype: list[float]
        """
        return self._center

    @center.setter
    def center(self, center):
        r"""Sets the center of this RunPocketReq.

        口袋中心坐标

        :param center: The center of this RunPocketReq.
        :type center: list[float]
        """
        self._center = center

    @property
    def size(self):
        r"""Gets the size of this RunPocketReq.

        口袋大小

        :return: The size of this RunPocketReq.
        :rtype: list[float]
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RunPocketReq.

        口袋大小

        :param size: The size of this RunPocketReq.
        :type size: list[float]
        """
        self._size = size

    @property
    def padding(self):
        r"""Gets the padding of this RunPocketReq.

        口袋的padding值

        :return: The padding of this RunPocketReq.
        :rtype: float
        """
        return self._padding

    @padding.setter
    def padding(self, padding):
        r"""Sets the padding of this RunPocketReq.

        口袋的padding值

        :param padding: The padding of this RunPocketReq.
        :type padding: float
        """
        self._padding = padding

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
        if not isinstance(other, RunPocketReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
