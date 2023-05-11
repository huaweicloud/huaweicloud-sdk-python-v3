# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateCn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int'
    }

    attribute_map = {
        'num': 'num'
    }

    def __init__(self, num=None):
        """BatchCreateCn

        The model defined in huaweicloud sdk

        :param num: 批量增加CN节点任务完成，集群总CN数量。集群支持的CN节点数量与集群当前版本和节点数量相关，具体支持范围可根据“查询集群CN节点”查询，“min_num”为支持的最小数量，max_num为支持的最大数量。
        :type num: int
        """
        
        

        self._num = None
        self.discriminator = None

        self.num = num

    @property
    def num(self):
        """Gets the num of this BatchCreateCn.

        批量增加CN节点任务完成，集群总CN数量。集群支持的CN节点数量与集群当前版本和节点数量相关，具体支持范围可根据“查询集群CN节点”查询，“min_num”为支持的最小数量，max_num为支持的最大数量。

        :return: The num of this BatchCreateCn.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this BatchCreateCn.

        批量增加CN节点任务完成，集群总CN数量。集群支持的CN节点数量与集群当前版本和节点数量相关，具体支持范围可根据“查询集群CN节点”查询，“min_num”为支持的最小数量，max_num为支持的最大数量。

        :param num: The num of this BatchCreateCn.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, BatchCreateCn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
