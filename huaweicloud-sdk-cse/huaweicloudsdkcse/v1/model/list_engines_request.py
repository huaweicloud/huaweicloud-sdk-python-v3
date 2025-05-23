# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnginesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'str',
        'type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, offset=None, limit=None, type=None):
        r"""ListEnginesRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: str
        :param type: 查询所有微服务引擎需要将该值设置为ALL，查询ServiceComb引擎专享版需要将该值设置为CSE，查询注册配置中心需要将该值设置为Nacos，查询网关需要将该值设置为MicroGateway。
        :type type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListEnginesRequest.

        偏移量。

        :return: The offset of this ListEnginesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEnginesRequest.

        偏移量。

        :param offset: The offset of this ListEnginesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEnginesRequest.

        每页显示的条目数量。

        :return: The limit of this ListEnginesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnginesRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListEnginesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListEnginesRequest.

        查询所有微服务引擎需要将该值设置为ALL，查询ServiceComb引擎专享版需要将该值设置为CSE，查询注册配置中心需要将该值设置为Nacos，查询网关需要将该值设置为MicroGateway。

        :return: The type of this ListEnginesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEnginesRequest.

        查询所有微服务引擎需要将该值设置为ALL，查询ServiceComb引擎专享版需要将该值设置为CSE，查询注册配置中心需要将该值设置为Nacos，查询网关需要将该值设置为MicroGateway。

        :param type: The type of this ListEnginesRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListEnginesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
