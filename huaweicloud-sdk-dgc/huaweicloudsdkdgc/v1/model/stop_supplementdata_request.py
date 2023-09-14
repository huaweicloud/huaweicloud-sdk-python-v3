# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopSupplementdataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'instance_name': 'instanceName'
    }

    def __init__(self, workspace=None, instance_name=None):
        """StopSupplementdataRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param instance_name: 补数据名称.
        :type instance_name: str
        """
        
        

        self._workspace = None
        self._instance_name = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.instance_name = instance_name

    @property
    def workspace(self):
        """Gets the workspace of this StopSupplementdataRequest.

        工作空间id

        :return: The workspace of this StopSupplementdataRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this StopSupplementdataRequest.

        工作空间id

        :param workspace: The workspace of this StopSupplementdataRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def instance_name(self):
        """Gets the instance_name of this StopSupplementdataRequest.

        补数据名称.

        :return: The instance_name of this StopSupplementdataRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this StopSupplementdataRequest.

        补数据名称.

        :param instance_name: The instance_name of this StopSupplementdataRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, StopSupplementdataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
