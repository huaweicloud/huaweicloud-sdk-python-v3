# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveJobRunConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_resource_type': 'str',
        'single_job_in_room': 'bool'
    }

    attribute_map = {
        'allow_resource_type': 'allow_resource_type',
        'single_job_in_room': 'single_job_in_room'
    }

    def __init__(self, allow_resource_type=None, single_job_in_room=None):
        r"""LiveJobRunConfig

        The model defined in huaweicloud sdk

        :param allow_resource_type: 允许使用资源类型。 * PERIOD：使用包周期资源 * ONDEMAND：使用按需资源 * UNLIMITED：不限制资源类型 * ONE_TIME：一次性资源
        :type allow_resource_type: str
        :param single_job_in_room: 一个直播间是否仅允许一个正在直播的任务。 * true: 限制直播间仅允许一个任务运行。 * false: 不限制直播间任务运行数量。
        :type single_job_in_room: bool
        """
        
        

        self._allow_resource_type = None
        self._single_job_in_room = None
        self.discriminator = None

        if allow_resource_type is not None:
            self.allow_resource_type = allow_resource_type
        if single_job_in_room is not None:
            self.single_job_in_room = single_job_in_room

    @property
    def allow_resource_type(self):
        r"""Gets the allow_resource_type of this LiveJobRunConfig.

        允许使用资源类型。 * PERIOD：使用包周期资源 * ONDEMAND：使用按需资源 * UNLIMITED：不限制资源类型 * ONE_TIME：一次性资源

        :return: The allow_resource_type of this LiveJobRunConfig.
        :rtype: str
        """
        return self._allow_resource_type

    @allow_resource_type.setter
    def allow_resource_type(self, allow_resource_type):
        r"""Sets the allow_resource_type of this LiveJobRunConfig.

        允许使用资源类型。 * PERIOD：使用包周期资源 * ONDEMAND：使用按需资源 * UNLIMITED：不限制资源类型 * ONE_TIME：一次性资源

        :param allow_resource_type: The allow_resource_type of this LiveJobRunConfig.
        :type allow_resource_type: str
        """
        self._allow_resource_type = allow_resource_type

    @property
    def single_job_in_room(self):
        r"""Gets the single_job_in_room of this LiveJobRunConfig.

        一个直播间是否仅允许一个正在直播的任务。 * true: 限制直播间仅允许一个任务运行。 * false: 不限制直播间任务运行数量。

        :return: The single_job_in_room of this LiveJobRunConfig.
        :rtype: bool
        """
        return self._single_job_in_room

    @single_job_in_room.setter
    def single_job_in_room(self, single_job_in_room):
        r"""Sets the single_job_in_room of this LiveJobRunConfig.

        一个直播间是否仅允许一个正在直播的任务。 * true: 限制直播间仅允许一个任务运行。 * false: 不限制直播间任务运行数量。

        :param single_job_in_room: The single_job_in_room of this LiveJobRunConfig.
        :type single_job_in_room: bool
        """
        self._single_job_in_room = single_job_in_room

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
        if not isinstance(other, LiveJobRunConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
