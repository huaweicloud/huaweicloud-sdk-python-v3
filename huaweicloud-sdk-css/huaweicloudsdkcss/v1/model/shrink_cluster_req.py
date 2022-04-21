# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'shrink': 'list[ShrinkNodeReq]'
    }

    attribute_map = {
        'shrink': 'shrink'
    }

    def __init__(self, shrink=None):
        """ShrinkClusterReq

        The model defined in huaweicloud sdk

        :param shrink: 需要缩容的节点类型和数量集合。
        :type shrink: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        """
        
        

        self._shrink = None
        self.discriminator = None

        self.shrink = shrink

    @property
    def shrink(self):
        """Gets the shrink of this ShrinkClusterReq.

        需要缩容的节点类型和数量集合。

        :return: The shrink of this ShrinkClusterReq.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        """
        return self._shrink

    @shrink.setter
    def shrink(self, shrink):
        """Sets the shrink of this ShrinkClusterReq.

        需要缩容的节点类型和数量集合。

        :param shrink: The shrink of this ShrinkClusterReq.
        :type shrink: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        """
        self._shrink = shrink

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
        if not isinstance(other, ShrinkClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
