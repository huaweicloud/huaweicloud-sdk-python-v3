# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeLabelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'labels': 'list[NodeLabelRsp]'
    }

    attribute_map = {
        'count': 'count',
        'labels': 'labels'
    }

    def __init__(self, count=None, labels=None):
        """ListNodeLabelResponse

        The model defined in huaweicloud sdk

        :param count: 节点标签数量
        :type count: int
        :param labels: 数据对象列表
        :type labels: list[:class:`huaweicloudsdkeihealth.v1.NodeLabelRsp`]
        """
        
        super(ListNodeLabelResponse, self).__init__()

        self._count = None
        self._labels = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if labels is not None:
            self.labels = labels

    @property
    def count(self):
        """Gets the count of this ListNodeLabelResponse.

        节点标签数量

        :return: The count of this ListNodeLabelResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListNodeLabelResponse.

        节点标签数量

        :param count: The count of this ListNodeLabelResponse.
        :type count: int
        """
        self._count = count

    @property
    def labels(self):
        """Gets the labels of this ListNodeLabelResponse.

        数据对象列表

        :return: The labels of this ListNodeLabelResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NodeLabelRsp`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ListNodeLabelResponse.

        数据对象列表

        :param labels: The labels of this ListNodeLabelResponse.
        :type labels: list[:class:`huaweicloudsdkeihealth.v1.NodeLabelRsp`]
        """
        self._labels = labels

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
        if not isinstance(other, ListNodeLabelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
