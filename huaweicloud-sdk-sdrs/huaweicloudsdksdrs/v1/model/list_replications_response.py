# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replications': 'list[ShowReplicationParams]',
        'count': 'int'
    }

    attribute_map = {
        'replications': 'replications',
        'count': 'count'
    }

    def __init__(self, replications=None, count=None):
        r"""ListReplicationsResponse

        The model defined in huaweicloud sdk

        :param replications: 复制对列表。
        :type replications: list[:class:`huaweicloudsdksdrs.v1.ShowReplicationParams`]
        :param count: 列表中包含的复制对个数。
        :type count: int
        """
        
        super(ListReplicationsResponse, self).__init__()

        self._replications = None
        self._count = None
        self.discriminator = None

        if replications is not None:
            self.replications = replications
        if count is not None:
            self.count = count

    @property
    def replications(self):
        r"""Gets the replications of this ListReplicationsResponse.

        复制对列表。

        :return: The replications of this ListReplicationsResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ShowReplicationParams`]
        """
        return self._replications

    @replications.setter
    def replications(self, replications):
        r"""Sets the replications of this ListReplicationsResponse.

        复制对列表。

        :param replications: The replications of this ListReplicationsResponse.
        :type replications: list[:class:`huaweicloudsdksdrs.v1.ShowReplicationParams`]
        """
        self._replications = replications

    @property
    def count(self):
        r"""Gets the count of this ListReplicationsResponse.

        列表中包含的复制对个数。

        :return: The count of this ListReplicationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListReplicationsResponse.

        列表中包含的复制对个数。

        :param count: The count of this ListReplicationsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListReplicationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
