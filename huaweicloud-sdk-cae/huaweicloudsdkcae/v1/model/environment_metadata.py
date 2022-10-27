# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'annotations': 'object',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'job_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'job_id': 'job_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, annotations=None, id=None, name=None, status=None, type=None, job_id=None, created_at=None, updated_at=None):
        """EnvironmentMetadata

        The model defined in huaweicloud sdk

        :param annotations: 附加信息。
        :type annotations: object
        :param id: 环境id。
        :type id: str
        :param name: 环境名称。
        :type name: str
        :param status: 环境状态。
        :type status: str
        :param type: 环境类型。
        :type type: str
        :param job_id: 任务id。
        :type job_id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._annotations = None
        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self._job_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if job_id is not None:
            self.job_id = job_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def annotations(self):
        """Gets the annotations of this EnvironmentMetadata.

        附加信息。

        :return: The annotations of this EnvironmentMetadata.
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this EnvironmentMetadata.

        附加信息。

        :param annotations: The annotations of this EnvironmentMetadata.
        :type annotations: object
        """
        self._annotations = annotations

    @property
    def id(self):
        """Gets the id of this EnvironmentMetadata.

        环境id。

        :return: The id of this EnvironmentMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentMetadata.

        环境id。

        :param id: The id of this EnvironmentMetadata.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnvironmentMetadata.

        环境名称。

        :return: The name of this EnvironmentMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentMetadata.

        环境名称。

        :param name: The name of this EnvironmentMetadata.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this EnvironmentMetadata.

        环境状态。

        :return: The status of this EnvironmentMetadata.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnvironmentMetadata.

        环境状态。

        :param status: The status of this EnvironmentMetadata.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this EnvironmentMetadata.

        环境类型。

        :return: The type of this EnvironmentMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EnvironmentMetadata.

        环境类型。

        :param type: The type of this EnvironmentMetadata.
        :type type: str
        """
        self._type = type

    @property
    def job_id(self):
        """Gets the job_id of this EnvironmentMetadata.

        任务id。

        :return: The job_id of this EnvironmentMetadata.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this EnvironmentMetadata.

        任务id。

        :param job_id: The job_id of this EnvironmentMetadata.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def created_at(self):
        """Gets the created_at of this EnvironmentMetadata.

        创建时间。

        :return: The created_at of this EnvironmentMetadata.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EnvironmentMetadata.

        创建时间。

        :param created_at: The created_at of this EnvironmentMetadata.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EnvironmentMetadata.

        更新时间。

        :return: The updated_at of this EnvironmentMetadata.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EnvironmentMetadata.

        更新时间。

        :param updated_at: The updated_at of this EnvironmentMetadata.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, EnvironmentMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
