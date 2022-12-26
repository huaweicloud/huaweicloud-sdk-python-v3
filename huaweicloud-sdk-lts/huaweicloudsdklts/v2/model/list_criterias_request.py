# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCriteriasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'topic_id': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'topic_id': 'topic_id',
        'search_type': 'search_type'
    }

    def __init__(self, group_id=None, topic_id=None, search_type=None):
        """ListCriteriasRequest

        The model defined in huaweicloud sdk

        :param group_id: 租户想查询的日志流所在的日志组的groupid，一般为36位字符串。  缺省值：None  最小长度：36  最大长度：36
        :type group_id: str
        :param topic_id: 日志流id
        :type topic_id: str
        :param search_type: 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION
        :type search_type: str
        """
        
        

        self._group_id = None
        self._topic_id = None
        self._search_type = None
        self.discriminator = None

        self.group_id = group_id
        self.topic_id = topic_id
        if search_type is not None:
            self.search_type = search_type

    @property
    def group_id(self):
        """Gets the group_id of this ListCriteriasRequest.

        租户想查询的日志流所在的日志组的groupid，一般为36位字符串。  缺省值：None  最小长度：36  最大长度：36

        :return: The group_id of this ListCriteriasRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListCriteriasRequest.

        租户想查询的日志流所在的日志组的groupid，一般为36位字符串。  缺省值：None  最小长度：36  最大长度：36

        :param group_id: The group_id of this ListCriteriasRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def topic_id(self):
        """Gets the topic_id of this ListCriteriasRequest.

        日志流id

        :return: The topic_id of this ListCriteriasRequest.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this ListCriteriasRequest.

        日志流id

        :param topic_id: The topic_id of this ListCriteriasRequest.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def search_type(self):
        """Gets the search_type of this ListCriteriasRequest.

        原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :return: The search_type of this ListCriteriasRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this ListCriteriasRequest.

        原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :param search_type: The search_type of this ListCriteriasRequest.
        :type search_type: str
        """
        self._search_type = search_type

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
        if not isinstance(other, ListCriteriasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
