# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_type': 'str',
        'job_id': 'str',
        'is_show_breakpoint_position': 'bool'
    }

    attribute_map = {
        'delete_type': 'delete_type',
        'job_id': 'job_id',
        'is_show_breakpoint_position': 'is_show_breakpoint_position'
    }

    def __init__(self, delete_type=None, job_id=None, is_show_breakpoint_position=None):
        """DeleteJobReq

        The model defined in huaweicloud sdk

        :param delete_type: terminate:结束迁移任务,force_terminate:强制结束迁移任务,delete:删除迁移任务
        :type delete_type: str
        :param job_id: 任务ID
        :type job_id: str
        :param is_show_breakpoint_position: MySQL为源，实时迁移，实时同步，数据订阅，实时灾备结束任务时是否展示断点信息
        :type is_show_breakpoint_position: bool
        """
        
        

        self._delete_type = None
        self._job_id = None
        self._is_show_breakpoint_position = None
        self.discriminator = None

        self.delete_type = delete_type
        self.job_id = job_id
        if is_show_breakpoint_position is not None:
            self.is_show_breakpoint_position = is_show_breakpoint_position

    @property
    def delete_type(self):
        """Gets the delete_type of this DeleteJobReq.

        terminate:结束迁移任务,force_terminate:强制结束迁移任务,delete:删除迁移任务

        :return: The delete_type of this DeleteJobReq.
        :rtype: str
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        """Sets the delete_type of this DeleteJobReq.

        terminate:结束迁移任务,force_terminate:强制结束迁移任务,delete:删除迁移任务

        :param delete_type: The delete_type of this DeleteJobReq.
        :type delete_type: str
        """
        self._delete_type = delete_type

    @property
    def job_id(self):
        """Gets the job_id of this DeleteJobReq.

        任务ID

        :return: The job_id of this DeleteJobReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DeleteJobReq.

        任务ID

        :param job_id: The job_id of this DeleteJobReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def is_show_breakpoint_position(self):
        """Gets the is_show_breakpoint_position of this DeleteJobReq.

        MySQL为源，实时迁移，实时同步，数据订阅，实时灾备结束任务时是否展示断点信息

        :return: The is_show_breakpoint_position of this DeleteJobReq.
        :rtype: bool
        """
        return self._is_show_breakpoint_position

    @is_show_breakpoint_position.setter
    def is_show_breakpoint_position(self, is_show_breakpoint_position):
        """Sets the is_show_breakpoint_position of this DeleteJobReq.

        MySQL为源，实时迁移，实时同步，数据订阅，实时灾备结束任务时是否展示断点信息

        :param is_show_breakpoint_position: The is_show_breakpoint_position of this DeleteJobReq.
        :type is_show_breakpoint_position: bool
        """
        self._is_show_breakpoint_position = is_show_breakpoint_position

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
        if not isinstance(other, DeleteJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
