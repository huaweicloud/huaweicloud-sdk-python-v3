# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationUpdateRequestEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resume_mode': 'str'
    }

    attribute_map = {
        'resume_mode': 'resume_mode'
    }

    def __init__(self, resume_mode=None):
        """MigrationUpdateRequestEntity

        The model defined in huaweicloud sdk

        :param resume_mode: 模式
        :type resume_mode: str
        """
        
        

        self._resume_mode = None
        self.discriminator = None

        if resume_mode is not None:
            self.resume_mode = resume_mode

    @property
    def resume_mode(self):
        """Gets the resume_mode of this MigrationUpdateRequestEntity.

        模式

        :return: The resume_mode of this MigrationUpdateRequestEntity.
        :rtype: str
        """
        return self._resume_mode

    @resume_mode.setter
    def resume_mode(self, resume_mode):
        """Sets the resume_mode of this MigrationUpdateRequestEntity.

        模式

        :param resume_mode: The resume_mode of this MigrationUpdateRequestEntity.
        :type resume_mode: str
        """
        self._resume_mode = resume_mode

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
        if not isinstance(other, MigrationUpdateRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
