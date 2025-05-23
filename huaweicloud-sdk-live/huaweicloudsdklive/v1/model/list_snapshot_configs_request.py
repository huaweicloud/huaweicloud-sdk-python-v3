# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domain=None, app_name=None, limit=None, offset=None):
        r"""ListSnapshotConfigsRequest

        The model defined in huaweicloud sdk

        :param domain: 域名
        :type domain: str
        :param app_name: 应用名称
        :type app_name: str
        :param limit: 每页记录数  取值范围[1,100]  默认值：10
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        """
        
        

        self._domain = None
        self._app_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domain(self):
        r"""Gets the domain of this ListSnapshotConfigsRequest.

        域名

        :return: The domain of this ListSnapshotConfigsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListSnapshotConfigsRequest.

        域名

        :param domain: The domain of this ListSnapshotConfigsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this ListSnapshotConfigsRequest.

        应用名称

        :return: The app_name of this ListSnapshotConfigsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListSnapshotConfigsRequest.

        应用名称

        :param app_name: The app_name of this ListSnapshotConfigsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def limit(self):
        r"""Gets the limit of this ListSnapshotConfigsRequest.

        每页记录数  取值范围[1,100]  默认值：10

        :return: The limit of this ListSnapshotConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSnapshotConfigsRequest.

        每页记录数  取值范围[1,100]  默认值：10

        :param limit: The limit of this ListSnapshotConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSnapshotConfigsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListSnapshotConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSnapshotConfigsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListSnapshotConfigsRequest.
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
        if not isinstance(other, ListSnapshotConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
