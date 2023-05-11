# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEntitiesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'project_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'project_id': 'project_id',
        'status': 'status'
    }

    def __init__(self, image_id=None, project_id=None, status=None):
        """JobEntitiesResult

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID。
        :type image_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param status: 任务状态。
        :type status: str
        """
        
        

        self._image_id = None
        self._project_id = None
        self._status = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status

    @property
    def image_id(self):
        """Gets the image_id of this JobEntitiesResult.

        镜像ID。

        :return: The image_id of this JobEntitiesResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this JobEntitiesResult.

        镜像ID。

        :param image_id: The image_id of this JobEntitiesResult.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def project_id(self):
        """Gets the project_id of this JobEntitiesResult.

        项目ID。

        :return: The project_id of this JobEntitiesResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JobEntitiesResult.

        项目ID。

        :param project_id: The project_id of this JobEntitiesResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this JobEntitiesResult.

        任务状态。

        :return: The status of this JobEntitiesResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobEntitiesResult.

        任务状态。

        :param status: The status of this JobEntitiesResult.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, JobEntitiesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
