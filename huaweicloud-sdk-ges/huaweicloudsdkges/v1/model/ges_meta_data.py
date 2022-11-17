# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GesMetaData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'labels': 'list[Label]'
    }

    attribute_map = {
        'labels': 'labels'
    }

    def __init__(self, labels=None):
        """GesMetaData

        The model defined in huaweicloud sdk

        :param labels: Label数据结构集合。
        :type labels: list[:class:`huaweicloudsdkges.v1.Label`]
        """
        
        

        self._labels = None
        self.discriminator = None

        self.labels = labels

    @property
    def labels(self):
        """Gets the labels of this GesMetaData.

        Label数据结构集合。

        :return: The labels of this GesMetaData.
        :rtype: list[:class:`huaweicloudsdkges.v1.Label`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GesMetaData.

        Label数据结构集合。

        :param labels: The labels of this GesMetaData.
        :type labels: list[:class:`huaweicloudsdkges.v1.Label`]
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
        if not isinstance(other, GesMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
