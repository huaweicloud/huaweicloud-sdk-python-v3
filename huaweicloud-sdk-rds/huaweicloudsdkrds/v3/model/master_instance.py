# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'region': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'region': 'region',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, instance_id=None, region=None, project_id=None, project_name=None):
        """MasterInstance

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param region: 区域。
        :type region: str
        :param project_id: 项目ID。
        :type project_id: str
        :param project_name: 项目名称。
        :type project_name: str
        """
        
        

        self._instance_id = None
        self._region = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.region = region
        self.project_id = project_id
        self.project_name = project_name

    @property
    def instance_id(self):
        """Gets the instance_id of this MasterInstance.

        实例ID。

        :return: The instance_id of this MasterInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this MasterInstance.

        实例ID。

        :param instance_id: The instance_id of this MasterInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def region(self):
        """Gets the region of this MasterInstance.

        区域。

        :return: The region of this MasterInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MasterInstance.

        区域。

        :param region: The region of this MasterInstance.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        """Gets the project_id of this MasterInstance.

        项目ID。

        :return: The project_id of this MasterInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MasterInstance.

        项目ID。

        :param project_id: The project_id of this MasterInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this MasterInstance.

        项目名称。

        :return: The project_name of this MasterInstance.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this MasterInstance.

        项目名称。

        :param project_name: The project_name of this MasterInstance.
        :type project_name: str
        """
        self._project_name = project_name

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
        if not isinstance(other, MasterInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
