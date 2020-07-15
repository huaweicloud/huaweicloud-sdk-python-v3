# coding: utf-8

import pprint
import re

import six





class GlanceDeleteImageRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'delete_backup': 'bool'
    }

    attribute_map = {
        'delete_backup': 'delete_backup'
    }

    def __init__(self, delete_backup=None):
        """GlanceDeleteImageRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._delete_backup = None
        self.discriminator = None

        if delete_backup is not None:
            self.delete_backup = delete_backup

    @property
    def delete_backup(self):
        """Gets the delete_backup of this GlanceDeleteImageRequestBody.

        取值为：true和false true：表示删除整机镜像时，同时删除其关联的云服务器备份。 false：表示只删除整机镜像，不删除其关联的云服务器备份。

        :return: The delete_backup of this GlanceDeleteImageRequestBody.
        :rtype: bool
        """
        return self._delete_backup

    @delete_backup.setter
    def delete_backup(self, delete_backup):
        """Sets the delete_backup of this GlanceDeleteImageRequestBody.

        取值为：true和false true：表示删除整机镜像时，同时删除其关联的云服务器备份。 false：表示只删除整机镜像，不删除其关联的云服务器备份。

        :param delete_backup: The delete_backup of this GlanceDeleteImageRequestBody.
        :type: bool
        """
        self._delete_backup = delete_backup

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
        if not isinstance(other, GlanceDeleteImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
