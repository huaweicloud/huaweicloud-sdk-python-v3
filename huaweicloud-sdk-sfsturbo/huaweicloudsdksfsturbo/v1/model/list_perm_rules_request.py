# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'share_id': 'share_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, share_id=None, limit=None, offset=None):
        r"""ListPermRulesRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param limit: 返回的权限规则个数
        :type limit: int
        :param offset: 返回的权限规则的偏移量
        :type offset: int
        """
        
        

        self._share_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.share_id = share_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def share_id(self):
        r"""Gets the share_id of this ListPermRulesRequest.

        文件系统ID

        :return: The share_id of this ListPermRulesRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ListPermRulesRequest.

        文件系统ID

        :param share_id: The share_id of this ListPermRulesRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPermRulesRequest.

        返回的权限规则个数

        :return: The limit of this ListPermRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPermRulesRequest.

        返回的权限规则个数

        :param limit: The limit of this ListPermRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPermRulesRequest.

        返回的权限规则的偏移量

        :return: The offset of this ListPermRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPermRulesRequest.

        返回的权限规则的偏移量

        :param offset: The offset of this ListPermRulesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPermRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
