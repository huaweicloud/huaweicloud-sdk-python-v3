# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataBucket:

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
        'data_event': 'list[str]'
    }

    attribute_map = {
        'data_bucket_name': 'data_bucket_name',
        'data_event': 'data_event'
    }

    def __init__(self, data_bucket_name=None, data_event=None):
        """DataBucket

        The model defined in huaweicloud sdk

        :param data_bucket_name: 数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。
        :type data_bucket_name: str
        :param data_event: 数据类追踪器追踪的操作类型。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。
        :type data_event: list[str]
        """
        
        

        self._data_bucket_name = None
        self._data_event = None
        self.discriminator = None

        if data_bucket_name is not None:
            self.data_bucket_name = data_bucket_name
        if data_event is not None:
            self.data_event = data_event

    @property
    def data_bucket_name(self):
        """Gets the data_bucket_name of this DataBucket.

        数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。

        :return: The data_bucket_name of this DataBucket.
        :rtype: str
        """
        return self._data_bucket_name

    @data_bucket_name.setter
    def data_bucket_name(self, data_bucket_name):
        """Sets the data_bucket_name of this DataBucket.

        数据类追踪器追踪对象的桶名。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。 - 追踪器一旦创建追踪桶无法修改。

        :param data_bucket_name: The data_bucket_name of this DataBucket.
        :type data_bucket_name: str
        """
        self._data_bucket_name = data_bucket_name

    @property
    def data_event(self):
        """Gets the data_event of this DataBucket.

        数据类追踪器追踪的操作类型。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。

        :return: The data_event of this DataBucket.
        :rtype: list[str]
        """
        return self._data_event

    @data_event.setter
    def data_event(self, data_event):
        """Sets the data_event of this DataBucket.

        数据类追踪器追踪的操作类型。 - 当启用或者停用数据类追踪器时，该参数为必选。 - 管理类追踪器无此参数。

        :param data_event: The data_event of this DataBucket.
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
        if not isinstance(other, DataBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
