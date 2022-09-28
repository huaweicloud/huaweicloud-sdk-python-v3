# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteProjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'x_delete_now': 'bool'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'x_delete_now': 'X-Delete-Now'
    }

    def __init__(self, eihealth_project_id=None, x_delete_now=None):
        """DeleteProjectRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param x_delete_now: 非核心项目删除立即删除标记
        :type x_delete_now: bool
        """
        
        

        self._eihealth_project_id = None
        self._x_delete_now = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if x_delete_now is not None:
            self.x_delete_now = x_delete_now

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this DeleteProjectRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this DeleteProjectRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this DeleteProjectRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this DeleteProjectRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def x_delete_now(self):
        """Gets the x_delete_now of this DeleteProjectRequest.

        非核心项目删除立即删除标记

        :return: The x_delete_now of this DeleteProjectRequest.
        :rtype: bool
        """
        return self._x_delete_now

    @x_delete_now.setter
    def x_delete_now(self, x_delete_now):
        """Sets the x_delete_now of this DeleteProjectRequest.

        非核心项目删除立即删除标记

        :param x_delete_now: The x_delete_now of this DeleteProjectRequest.
        :type x_delete_now: bool
        """
        self._x_delete_now = x_delete_now

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
        if not isinstance(other, DeleteProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
