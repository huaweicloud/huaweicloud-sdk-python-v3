# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WaterfallPageListParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, marker=None, limit=None):
        r"""WaterfallPageListParam

        The model defined in huaweicloud sdk

        :param marker: 页面的分页标志位,为分页的最后一条记录的id
        :type marker: str
        :param limit: 查询返回记录的数量限制。limit可以为空，如果值小于1或者大于100，则会使用默认值100
        :type limit: int
        """
        
        

        self._marker = None
        self._limit = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this WaterfallPageListParam.

        页面的分页标志位,为分页的最后一条记录的id

        :return: The marker of this WaterfallPageListParam.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this WaterfallPageListParam.

        页面的分页标志位,为分页的最后一条记录的id

        :param marker: The marker of this WaterfallPageListParam.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this WaterfallPageListParam.

        查询返回记录的数量限制。limit可以为空，如果值小于1或者大于100，则会使用默认值100

        :return: The limit of this WaterfallPageListParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this WaterfallPageListParam.

        查询返回记录的数量限制。limit可以为空，如果值小于1或者大于100，则会使用默认值100

        :param limit: The limit of this WaterfallPageListParam.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, WaterfallPageListParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
