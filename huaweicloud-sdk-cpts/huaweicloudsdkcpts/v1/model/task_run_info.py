# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskRunInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'run_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'run_type': 'run_type'
    }

    def __init__(self, id=None, run_type=None):
        r"""TaskRunInfo

        The model defined in huaweicloud sdk

        :param id: 任务id
        :type id: int
        :param run_type: 任务类型（0：旧版本任务；1：新版本任务）
        :type run_type: int
        """
        
        

        self._id = None
        self._run_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if run_type is not None:
            self.run_type = run_type

    @property
    def id(self):
        r"""Gets the id of this TaskRunInfo.

        任务id

        :return: The id of this TaskRunInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskRunInfo.

        任务id

        :param id: The id of this TaskRunInfo.
        :type id: int
        """
        self._id = id

    @property
    def run_type(self):
        r"""Gets the run_type of this TaskRunInfo.

        任务类型（0：旧版本任务；1：新版本任务）

        :return: The run_type of this TaskRunInfo.
        :rtype: int
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        r"""Sets the run_type of this TaskRunInfo.

        任务类型（0：旧版本任务；1：新版本任务）

        :param run_type: The run_type of this TaskRunInfo.
        :type run_type: int
        """
        self._run_type = run_type

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
        if not isinstance(other, TaskRunInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
