# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLastHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'repository_name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'repository_name': 'repository_name'
    }

    def __init__(self, project_id=None, repository_name=None):
        """ShowLastHistoryRequest

        The model defined in huaweicloud sdk

        :param project_id: DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)
        :type project_id: str
        :param repository_name: 代码仓库名，不支持中文
        :type repository_name: str
        """
        
        

        self._project_id = None
        self._repository_name = None
        self.discriminator = None

        self.project_id = project_id
        self.repository_name = repository_name

    @property
    def project_id(self):
        """Gets the project_id of this ShowLastHistoryRequest.

        DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)

        :return: The project_id of this ShowLastHistoryRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowLastHistoryRequest.

        DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)

        :param project_id: The project_id of this ShowLastHistoryRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repository_name(self):
        """Gets the repository_name of this ShowLastHistoryRequest.

        代码仓库名，不支持中文

        :return: The repository_name of this ShowLastHistoryRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this ShowLastHistoryRequest.

        代码仓库名，不支持中文

        :param repository_name: The repository_name of this ShowLastHistoryRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

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
        if not isinstance(other, ShowLastHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
