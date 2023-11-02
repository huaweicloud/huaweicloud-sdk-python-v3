# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowRequest:

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
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, eihealth_project_id=None, name=None, version=None):
        """ListWorkflowRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param name: 流程名称
        :type name: str
        :param version: 流程版本
        :type version: str
        """
        
        

        self._eihealth_project_id = None
        self._name = None
        self._version = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListWorkflowRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListWorkflowRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListWorkflowRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListWorkflowRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def name(self):
        """Gets the name of this ListWorkflowRequest.

        流程名称

        :return: The name of this ListWorkflowRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListWorkflowRequest.

        流程名称

        :param name: The name of this ListWorkflowRequest.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this ListWorkflowRequest.

        流程版本

        :return: The version of this ListWorkflowRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListWorkflowRequest.

        流程版本

        :param version: The version of this ListWorkflowRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
