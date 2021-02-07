# coding: utf-8

import pprint
import re

import six





class IoTAForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_source_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'data_source_id': 'data_source_id',
        'project_id': 'project_id'
    }

    def __init__(self, data_source_id=None, project_id=None):
        """IoTAForwarding - a model defined in huaweicloud sdk"""
        
        

        self._data_source_id = None
        self._project_id = None
        self.discriminator = None

        self.data_source_id = data_source_id
        self.project_id = project_id

    @property
    def data_source_id(self):
        """Gets the data_source_id of this IoTAForwarding.

        IoTA服务对应的数据源Id

        :return: The data_source_id of this IoTAForwarding.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this IoTAForwarding.

        IoTA服务对应的数据源Id

        :param data_source_id: The data_source_id of this IoTAForwarding.
        :type: str
        """
        self._data_source_id = data_source_id

    @property
    def project_id(self):
        """Gets the project_id of this IoTAForwarding.

        IoTA服务对应的projectId信息

        :return: The project_id of this IoTAForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IoTAForwarding.

        IoTA服务对应的projectId信息

        :param project_id: The project_id of this IoTAForwarding.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoTAForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
