# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainNotAddedProjectsV4Request:

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
        'limit': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, offset=None, limit=None):
        """ListDomainNotAddedProjectsV4Request

        The model defined in huaweicloud sdk

        :param offset: 分页索引，偏移量,offset是limit的整数倍，limit&#x3D;10,offset&#x3D;0,10,20...
        :type offset: int
        :param limit: 每页显示的数量,每页最多显示100条
        :type limit: int
        """
        
        

        self._offset = None
        self._limit = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDomainNotAddedProjectsV4Request.

        分页索引，偏移量,offset是limit的整数倍，limit=10,offset=0,10,20...

        :return: The offset of this ListDomainNotAddedProjectsV4Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDomainNotAddedProjectsV4Request.

        分页索引，偏移量,offset是limit的整数倍，limit=10,offset=0,10,20...

        :param offset: The offset of this ListDomainNotAddedProjectsV4Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDomainNotAddedProjectsV4Request.

        每页显示的数量,每页最多显示100条

        :return: The limit of this ListDomainNotAddedProjectsV4Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDomainNotAddedProjectsV4Request.

        每页显示的数量,每页最多显示100条

        :param limit: The limit of this ListDomainNotAddedProjectsV4Request.
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
        if not isinstance(other, ListDomainNotAddedProjectsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
