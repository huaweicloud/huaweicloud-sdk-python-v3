# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataBucketQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_bucket_name': 'str',
        'search_enabled': 'bool',
        'data_event': 'list[str]'
    }

    attribute_map = {
        'data_bucket_name': 'data_bucket_name',
        'search_enabled': 'search_enabled',
        'data_event': 'data_event'
    }

    def __init__(self, data_bucket_name=None, search_enabled=None, data_event=None):
        """DataBucketQuery

        The model defined in huaweicloud sdk

        :param data_bucket_name: 标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。
        :type data_bucket_name: str
        :param search_enabled: 追踪桶日志是否支持搜索。
        :type search_enabled: bool
        :param data_event: 数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。
        :type data_event: list[str]
        """
        
        

        self._data_bucket_name = None
        self._search_enabled = None
        self._data_event = None
        self.discriminator = None

        if data_bucket_name is not None:
            self.data_bucket_name = data_bucket_name
        if search_enabled is not None:
            self.search_enabled = search_enabled
        if data_event is not None:
            self.data_event = data_event

    @property
    def data_bucket_name(self):
        """Gets the data_bucket_name of this DataBucketQuery.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :return: The data_bucket_name of this DataBucketQuery.
        :rtype: str
        """
        return self._data_bucket_name

    @data_bucket_name.setter
    def data_bucket_name(self, data_bucket_name):
        """Sets the data_bucket_name of this DataBucketQuery.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :param data_bucket_name: The data_bucket_name of this DataBucketQuery.
        :type data_bucket_name: str
        """
        self._data_bucket_name = data_bucket_name

    @property
    def search_enabled(self):
        """Gets the search_enabled of this DataBucketQuery.

        追踪桶日志是否支持搜索。

        :return: The search_enabled of this DataBucketQuery.
        :rtype: bool
        """
        return self._search_enabled

    @search_enabled.setter
    def search_enabled(self, search_enabled):
        """Sets the search_enabled of this DataBucketQuery.

        追踪桶日志是否支持搜索。

        :param search_enabled: The search_enabled of this DataBucketQuery.
        :type search_enabled: bool
        """
        self._search_enabled = search_enabled

    @property
    def data_event(self):
        """Gets the data_event of this DataBucketQuery.

        数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。

        :return: The data_event of this DataBucketQuery.
        :rtype: list[str]
        """
        return self._data_event

    @data_event.setter
    def data_event(self, data_event):
        """Sets the data_event of this DataBucketQuery.

        数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。

        :param data_event: The data_event of this DataBucketQuery.
        :type data_event: list[str]
        """
        self._data_event = data_event

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
        if not isinstance(other, DataBucketQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
