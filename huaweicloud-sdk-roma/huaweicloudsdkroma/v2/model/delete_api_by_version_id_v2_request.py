# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteApiByVersionIdV2Request:

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
        'version_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'version_id': 'version_id'
    }

    def __init__(self, instance_id=None, version_id=None):
        """DeleteApiByVersionIdV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param version_id: API版本的编号
        :type version_id: str
        """
        
        

        self._instance_id = None
        self._version_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.version_id = version_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteApiByVersionIdV2Request.

        实例ID

        :return: The instance_id of this DeleteApiByVersionIdV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteApiByVersionIdV2Request.

        实例ID

        :param instance_id: The instance_id of this DeleteApiByVersionIdV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def version_id(self):
        """Gets the version_id of this DeleteApiByVersionIdV2Request.

        API版本的编号

        :return: The version_id of this DeleteApiByVersionIdV2Request.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DeleteApiByVersionIdV2Request.

        API版本的编号

        :param version_id: The version_id of this DeleteApiByVersionIdV2Request.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, DeleteApiByVersionIdV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
