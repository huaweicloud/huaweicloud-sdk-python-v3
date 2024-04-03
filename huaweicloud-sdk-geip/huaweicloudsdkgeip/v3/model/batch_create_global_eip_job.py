# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateGlobalEipJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'job_id': 'job_id'
    }

    def __init__(self, id=None, name=None, job_id=None):
        """BatchCreateGlobalEipJob

        The model defined in huaweicloud sdk

        :param id: 全域弹性公网IP的ID
        :type id: str
        :param name: - 功能说明：全域弹性公网IP名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param job_id: 请求完成的job id
        :type job_id: str
        """
        
        

        self._id = None
        self._name = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        """Gets the id of this BatchCreateGlobalEipJob.

        全域弹性公网IP的ID

        :return: The id of this BatchCreateGlobalEipJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchCreateGlobalEipJob.

        全域弹性公网IP的ID

        :param id: The id of this BatchCreateGlobalEipJob.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BatchCreateGlobalEipJob.

        - 功能说明：全域弹性公网IP名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BatchCreateGlobalEipJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateGlobalEipJob.

        - 功能说明：全域弹性公网IP名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BatchCreateGlobalEipJob.
        :type name: str
        """
        self._name = name

    @property
    def job_id(self):
        """Gets the job_id of this BatchCreateGlobalEipJob.

        请求完成的job id

        :return: The job_id of this BatchCreateGlobalEipJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BatchCreateGlobalEipJob.

        请求完成的job id

        :param job_id: The job_id of this BatchCreateGlobalEipJob.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, BatchCreateGlobalEipJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
