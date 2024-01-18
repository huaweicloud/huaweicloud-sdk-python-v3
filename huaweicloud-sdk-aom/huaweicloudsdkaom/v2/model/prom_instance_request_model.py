# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PromInstanceRequestModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prom_name': 'str',
        'prom_type': 'str',
        'prom_version': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'prom_name': 'prom_name',
        'prom_type': 'prom_type',
        'prom_version': 'prom_version',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id'
    }

    def __init__(self, prom_name=None, prom_type=None, prom_version=None, enterprise_project_id=None, project_id=None):
        """PromInstanceRequestModel

        The model defined in huaweicloud sdk

        :param prom_name: Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。
        :type prom_name: str
        :param prom_type: Prometheus实例类型（暂时不支持VPC、KUBERNETES）。
        :type prom_type: str
        :param prom_version: Prometheus实例版本号。
        :type prom_version: str
        :param enterprise_project_id: Prometheus实例所属的企业项目。
        :type enterprise_project_id: str
        :param project_id: Prometheus实例所属projectId。
        :type project_id: str
        """
        
        

        self._prom_name = None
        self._prom_type = None
        self._prom_version = None
        self._enterprise_project_id = None
        self._project_id = None
        self.discriminator = None

        self.prom_name = prom_name
        self.prom_type = prom_type
        if prom_version is not None:
            self.prom_version = prom_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def prom_name(self):
        """Gets the prom_name of this PromInstanceRequestModel.

        Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。

        :return: The prom_name of this PromInstanceRequestModel.
        :rtype: str
        """
        return self._prom_name

    @prom_name.setter
    def prom_name(self, prom_name):
        """Sets the prom_name of this PromInstanceRequestModel.

        Prometheus实例名称 名称不能以下划线或中划线开头结尾，只含有中文、英文、数字、下划线、中划线、长度1-100。

        :param prom_name: The prom_name of this PromInstanceRequestModel.
        :type prom_name: str
        """
        self._prom_name = prom_name

    @property
    def prom_type(self):
        """Gets the prom_type of this PromInstanceRequestModel.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :return: The prom_type of this PromInstanceRequestModel.
        :rtype: str
        """
        return self._prom_type

    @prom_type.setter
    def prom_type(self, prom_type):
        """Sets the prom_type of this PromInstanceRequestModel.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :param prom_type: The prom_type of this PromInstanceRequestModel.
        :type prom_type: str
        """
        self._prom_type = prom_type

    @property
    def prom_version(self):
        """Gets the prom_version of this PromInstanceRequestModel.

        Prometheus实例版本号。

        :return: The prom_version of this PromInstanceRequestModel.
        :rtype: str
        """
        return self._prom_version

    @prom_version.setter
    def prom_version(self, prom_version):
        """Sets the prom_version of this PromInstanceRequestModel.

        Prometheus实例版本号。

        :param prom_version: The prom_version of this PromInstanceRequestModel.
        :type prom_version: str
        """
        self._prom_version = prom_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PromInstanceRequestModel.

        Prometheus实例所属的企业项目。

        :return: The enterprise_project_id of this PromInstanceRequestModel.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PromInstanceRequestModel.

        Prometheus实例所属的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this PromInstanceRequestModel.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this PromInstanceRequestModel.

        Prometheus实例所属projectId。

        :return: The project_id of this PromInstanceRequestModel.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PromInstanceRequestModel.

        Prometheus实例所属projectId。

        :param project_id: The project_id of this PromInstanceRequestModel.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, PromInstanceRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
