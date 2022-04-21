# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, limit=None, marker=None, vpc_id=None):
        """ListSubnetsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源id，为空时查询第一页
        :type marker: str
        :param vpc_id: 按照vpc_id过滤查询  企业项目细粒度授权场景下，该字段必传
        :type vpc_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._vpc_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListSubnetsRequest.

        每页返回的个数

        :return: The limit of this ListSubnetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubnetsRequest.

        每页返回的个数

        :param limit: The limit of this ListSubnetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSubnetsRequest.

        分页查询起始的资源id，为空时查询第一页

        :return: The marker of this ListSubnetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSubnetsRequest.

        分页查询起始的资源id，为空时查询第一页

        :param marker: The marker of this ListSubnetsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListSubnetsRequest.

        按照vpc_id过滤查询  企业项目细粒度授权场景下，该字段必传

        :return: The vpc_id of this ListSubnetsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListSubnetsRequest.

        按照vpc_id过滤查询  企业项目细粒度授权场景下，该字段必传

        :param vpc_id: The vpc_id of this ListSubnetsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListSubnetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
