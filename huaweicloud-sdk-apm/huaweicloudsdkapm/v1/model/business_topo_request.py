# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessTopoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_business_id': 'int',
        'env_tag_list': 'list[int]',
        'direction': 'str',
        'end_time': 'str',
        'start_time': 'str',
        'filter_user': 'bool'
    }

    attribute_map = {
        'target_business_id': 'target_business_id',
        'env_tag_list': 'env_tag_list',
        'direction': 'direction',
        'end_time': 'end_time',
        'start_time': 'start_time',
        'filter_user': 'filter_user'
    }

    def __init__(self, target_business_id=None, env_tag_list=None, direction=None, end_time=None, start_time=None, filter_user=None):
        """BusinessTopoRequest

        The model defined in huaweicloud sdk

        :param target_business_id: 目标应用id。
        :type target_business_id: int
        :param env_tag_list: 环境标签列表，可为空。
        :type env_tag_list: list[int]
        :param direction: 方向，可为空。
        :type direction: str
        :param end_time: 结束时间。
        :type end_time: str
        :param start_time: 开始时间。
        :type start_time: str
        :param filter_user: 过滤。
        :type filter_user: bool
        """
        
        

        self._target_business_id = None
        self._env_tag_list = None
        self._direction = None
        self._end_time = None
        self._start_time = None
        self._filter_user = None
        self.discriminator = None

        self.target_business_id = target_business_id
        if env_tag_list is not None:
            self.env_tag_list = env_tag_list
        if direction is not None:
            self.direction = direction
        self.end_time = end_time
        self.start_time = start_time
        if filter_user is not None:
            self.filter_user = filter_user

    @property
    def target_business_id(self):
        """Gets the target_business_id of this BusinessTopoRequest.

        目标应用id。

        :return: The target_business_id of this BusinessTopoRequest.
        :rtype: int
        """
        return self._target_business_id

    @target_business_id.setter
    def target_business_id(self, target_business_id):
        """Sets the target_business_id of this BusinessTopoRequest.

        目标应用id。

        :param target_business_id: The target_business_id of this BusinessTopoRequest.
        :type target_business_id: int
        """
        self._target_business_id = target_business_id

    @property
    def env_tag_list(self):
        """Gets the env_tag_list of this BusinessTopoRequest.

        环境标签列表，可为空。

        :return: The env_tag_list of this BusinessTopoRequest.
        :rtype: list[int]
        """
        return self._env_tag_list

    @env_tag_list.setter
    def env_tag_list(self, env_tag_list):
        """Sets the env_tag_list of this BusinessTopoRequest.

        环境标签列表，可为空。

        :param env_tag_list: The env_tag_list of this BusinessTopoRequest.
        :type env_tag_list: list[int]
        """
        self._env_tag_list = env_tag_list

    @property
    def direction(self):
        """Gets the direction of this BusinessTopoRequest.

        方向，可为空。

        :return: The direction of this BusinessTopoRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this BusinessTopoRequest.

        方向，可为空。

        :param direction: The direction of this BusinessTopoRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def end_time(self):
        """Gets the end_time of this BusinessTopoRequest.

        结束时间。

        :return: The end_time of this BusinessTopoRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BusinessTopoRequest.

        结束时间。

        :param end_time: The end_time of this BusinessTopoRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this BusinessTopoRequest.

        开始时间。

        :return: The start_time of this BusinessTopoRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BusinessTopoRequest.

        开始时间。

        :param start_time: The start_time of this BusinessTopoRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def filter_user(self):
        """Gets the filter_user of this BusinessTopoRequest.

        过滤。

        :return: The filter_user of this BusinessTopoRequest.
        :rtype: bool
        """
        return self._filter_user

    @filter_user.setter
    def filter_user(self, filter_user):
        """Sets the filter_user of this BusinessTopoRequest.

        过滤。

        :param filter_user: The filter_user of this BusinessTopoRequest.
        :type filter_user: bool
        """
        self._filter_user = filter_user

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
        if not isinstance(other, BusinessTopoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
