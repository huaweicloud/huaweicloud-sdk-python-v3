# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_job_id': 'int',
        'new_job_id': 'int',
        'remark': 'str'
    }

    attribute_map = {
        'old_job_id': 'old_job_id',
        'new_job_id': 'new_job_id',
        'remark': 'remark'
    }

    def __init__(self, old_job_id=None, new_job_id=None, remark=None):
        """JobMap

        The model defined in huaweicloud sdk

        :param old_job_id: 导入文件中的作业ID。
        :type old_job_id: int
        :param new_job_id: 导入完成后作业ID，若is_cover&#x3D;false，服务中已有同名的作业，则为-1。
        :type new_job_id: int
        :param remark: 导入作业结果信息。
        :type remark: str
        """
        
        

        self._old_job_id = None
        self._new_job_id = None
        self._remark = None
        self.discriminator = None

        if old_job_id is not None:
            self.old_job_id = old_job_id
        if new_job_id is not None:
            self.new_job_id = new_job_id
        if remark is not None:
            self.remark = remark

    @property
    def old_job_id(self):
        """Gets the old_job_id of this JobMap.

        导入文件中的作业ID。

        :return: The old_job_id of this JobMap.
        :rtype: int
        """
        return self._old_job_id

    @old_job_id.setter
    def old_job_id(self, old_job_id):
        """Sets the old_job_id of this JobMap.

        导入文件中的作业ID。

        :param old_job_id: The old_job_id of this JobMap.
        :type old_job_id: int
        """
        self._old_job_id = old_job_id

    @property
    def new_job_id(self):
        """Gets the new_job_id of this JobMap.

        导入完成后作业ID，若is_cover=false，服务中已有同名的作业，则为-1。

        :return: The new_job_id of this JobMap.
        :rtype: int
        """
        return self._new_job_id

    @new_job_id.setter
    def new_job_id(self, new_job_id):
        """Sets the new_job_id of this JobMap.

        导入完成后作业ID，若is_cover=false，服务中已有同名的作业，则为-1。

        :param new_job_id: The new_job_id of this JobMap.
        :type new_job_id: int
        """
        self._new_job_id = new_job_id

    @property
    def remark(self):
        """Gets the remark of this JobMap.

        导入作业结果信息。

        :return: The remark of this JobMap.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this JobMap.

        导入作业结果信息。

        :param remark: The remark of this JobMap.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, JobMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
