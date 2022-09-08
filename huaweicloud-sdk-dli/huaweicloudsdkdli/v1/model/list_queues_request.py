# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_type': 'str',
        'tags': 'str',
        'with_charge_info': 'bool',
        'with_priv': 'bool'
    }

    attribute_map = {
        'queue_type': 'queue_type',
        'tags': 'tags',
        'with_charge_info': 'with-charge-info',
        'with_priv': 'with-priv'
    }

    def __init__(self, queue_type=None, tags=None, with_charge_info=None, with_priv=None):
        """ListQueuesRequest

        The model defined in huaweicloud sdk

        :param queue_type: 队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。
        :type queue_type: str
        :param tags: 查询根据标签进行过滤
        :type tags: str
        :param with_charge_info: 是否返回收费信息
        :type with_charge_info: bool
        :param with_priv: 是否返回权限信息。
        :type with_priv: bool
        """
        
        

        self._queue_type = None
        self._tags = None
        self._with_charge_info = None
        self._with_priv = None
        self.discriminator = None

        if queue_type is not None:
            self.queue_type = queue_type
        if tags is not None:
            self.tags = tags
        if with_charge_info is not None:
            self.with_charge_info = with_charge_info
        if with_priv is not None:
            self.with_priv = with_priv

    @property
    def queue_type(self):
        """Gets the queue_type of this ListQueuesRequest.

        队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。

        :return: The queue_type of this ListQueuesRequest.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this ListQueuesRequest.

        队列的类型,。有如下三种类型： sql general all 如果不指定，默认为sql。

        :param queue_type: The queue_type of this ListQueuesRequest.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def tags(self):
        """Gets the tags of this ListQueuesRequest.

        查询根据标签进行过滤

        :return: The tags of this ListQueuesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListQueuesRequest.

        查询根据标签进行过滤

        :param tags: The tags of this ListQueuesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def with_charge_info(self):
        """Gets the with_charge_info of this ListQueuesRequest.

        是否返回收费信息

        :return: The with_charge_info of this ListQueuesRequest.
        :rtype: bool
        """
        return self._with_charge_info

    @with_charge_info.setter
    def with_charge_info(self, with_charge_info):
        """Sets the with_charge_info of this ListQueuesRequest.

        是否返回收费信息

        :param with_charge_info: The with_charge_info of this ListQueuesRequest.
        :type with_charge_info: bool
        """
        self._with_charge_info = with_charge_info

    @property
    def with_priv(self):
        """Gets the with_priv of this ListQueuesRequest.

        是否返回权限信息。

        :return: The with_priv of this ListQueuesRequest.
        :rtype: bool
        """
        return self._with_priv

    @with_priv.setter
    def with_priv(self, with_priv):
        """Sets the with_priv of this ListQueuesRequest.

        是否返回权限信息。

        :param with_priv: The with_priv of this ListQueuesRequest.
        :type with_priv: bool
        """
        self._with_priv = with_priv

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
        if not isinstance(other, ListQueuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
