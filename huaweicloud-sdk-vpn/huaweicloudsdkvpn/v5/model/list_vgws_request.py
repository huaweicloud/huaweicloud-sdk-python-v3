# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVgwsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vgw_id': 'str',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'vgw_id': 'vgw_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, vgw_id=None, enterprise_project_id=None):
        """ListVgwsRequest

        The model defined in huaweicloud sdk

        :param vgw_id: vgw ID
        :type vgw_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: list[str]
        """
        
        

        self._vgw_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if vgw_id is not None:
            self.vgw_id = vgw_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def vgw_id(self):
        """Gets the vgw_id of this ListVgwsRequest.

        vgw ID

        :return: The vgw_id of this ListVgwsRequest.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this ListVgwsRequest.

        vgw ID

        :param vgw_id: The vgw_id of this ListVgwsRequest.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVgwsRequest.

        企业项目id

        :return: The enterprise_project_id of this ListVgwsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVgwsRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListVgwsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListVgwsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
