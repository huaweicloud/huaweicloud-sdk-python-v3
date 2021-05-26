# coding: utf-8

import pprint
import re

import six





class ListResourceGroupRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'status': 'str',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'status': 'status',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_name=None, group_id=None, status=None, start=None, limit=None):
        """ListResourceGroupRequest - a model defined in huaweicloud sdk"""
        
        

        self._group_name = None
        self._group_id = None
        self._status = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if status is not None:
            self.status = status
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_name(self):
        """Gets the group_name of this ListResourceGroupRequest.

        资源分组的名称；长度为1-128，只能包含0-9/a-z/A-Z/_/-或汉字；如：ResourceGroup-Test01。

        :return: The group_name of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListResourceGroupRequest.

        资源分组的名称；长度为1-128，只能包含0-9/a-z/A-Z/_/-或汉字；如：ResourceGroup-Test01。

        :param group_name: The group_name of this ListResourceGroupRequest.
        :type: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this ListResourceGroupRequest.

        资源分组的ID，长度为1-128，只能包含0-9/a-z/A-Z；如：rg16063743652226ew93e64p。

        :return: The group_id of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListResourceGroupRequest.

        资源分组的ID，长度为1-128，只能包含0-9/a-z/A-Z；如：rg16063743652226ew93e64p。

        :param group_id: The group_id of this ListResourceGroupRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def status(self):
        """Gets the status of this ListResourceGroupRequest.

        资源分组健康状态，值可为health、unhealth、no_alarm_rule；health表示健康，

        :return: The status of this ListResourceGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListResourceGroupRequest.

        资源分组健康状态，值可为health、unhealth、no_alarm_rule；health表示健康，

        :param status: The status of this ListResourceGroupRequest.
        :type: str
        """
        self._status = status

    @property
    def start(self):
        """Gets the start of this ListResourceGroupRequest.

        分页起始值，类型为integer，默认值为0。

        :return: The start of this ListResourceGroupRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListResourceGroupRequest.

        分页起始值，类型为integer，默认值为0。

        :param start: The start of this ListResourceGroupRequest.
        :type: int
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListResourceGroupRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :return: The limit of this ListResourceGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceGroupRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :param limit: The limit of this ListResourceGroupRequest.
        :type: int
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListResourceGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
