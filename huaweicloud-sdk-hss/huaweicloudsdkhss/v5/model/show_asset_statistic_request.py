# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id'
    }

    def __init__(self, enterprise_project_id=None, host_id=None):
        """ShowAssetStatisticRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param host_id: host id
        :type host_id: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowAssetStatisticRequest.

        企业项目

        :return: The enterprise_project_id of this ShowAssetStatisticRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowAssetStatisticRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ShowAssetStatisticRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        """Gets the host_id of this ShowAssetStatisticRequest.

        host id

        :return: The host_id of this ShowAssetStatisticRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ShowAssetStatisticRequest.

        host id

        :param host_id: The host_id of this ShowAssetStatisticRequest.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, ShowAssetStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
