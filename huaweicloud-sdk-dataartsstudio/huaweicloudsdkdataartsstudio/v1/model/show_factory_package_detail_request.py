# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryPackageDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_id': 'str',
        'workspace': 'str'
    }

    attribute_map = {
        'package_id': 'package_id',
        'workspace': 'workspace'
    }

    def __init__(self, package_id=None, workspace=None):
        """ShowFactoryPackageDetailRequest

        The model defined in huaweicloud sdk

        :param package_id: 发布包ID
        :type package_id: str
        :param workspace: 工作空间ID，默认查询default
        :type workspace: str
        """
        
        

        self._package_id = None
        self._workspace = None
        self.discriminator = None

        self.package_id = package_id
        if workspace is not None:
            self.workspace = workspace

    @property
    def package_id(self):
        """Gets the package_id of this ShowFactoryPackageDetailRequest.

        发布包ID

        :return: The package_id of this ShowFactoryPackageDetailRequest.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ShowFactoryPackageDetailRequest.

        发布包ID

        :param package_id: The package_id of this ShowFactoryPackageDetailRequest.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def workspace(self):
        """Gets the workspace of this ShowFactoryPackageDetailRequest.

        工作空间ID，默认查询default

        :return: The workspace of this ShowFactoryPackageDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowFactoryPackageDetailRequest.

        工作空间ID，默认查询default

        :param workspace: The workspace of this ShowFactoryPackageDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ShowFactoryPackageDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
