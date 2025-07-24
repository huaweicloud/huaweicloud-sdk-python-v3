# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackendTargetsRequest:

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
        'marker': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, share_id=None, limit=None, marker=None):
        r"""ListBackendTargetsRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param limit: 查询列表返回元素个数
        :type limit: int
        :param marker: 查询列表偏移量
        :type marker: str
        """
        
        

        self._share_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.share_id = share_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def share_id(self):
        r"""Gets the share_id of this ListBackendTargetsRequest.

        文件系统ID

        :return: The share_id of this ListBackendTargetsRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ListBackendTargetsRequest.

        文件系统ID

        :param share_id: The share_id of this ListBackendTargetsRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def limit(self):
        r"""Gets the limit of this ListBackendTargetsRequest.

        查询列表返回元素个数

        :return: The limit of this ListBackendTargetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackendTargetsRequest.

        查询列表返回元素个数

        :param limit: The limit of this ListBackendTargetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListBackendTargetsRequest.

        查询列表偏移量

        :return: The marker of this ListBackendTargetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListBackendTargetsRequest.

        查询列表偏移量

        :param marker: The marker of this ListBackendTargetsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListBackendTargetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
