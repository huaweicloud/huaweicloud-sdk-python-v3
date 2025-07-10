# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetRequest:

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
        'nat_name': 'str',
        'eip': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'nat_name': 'nat_name',
        'eip': 'eip'
    }

    def __init__(self, enterprise_project_id=None, nat_name=None, eip=None):
        r"""ListInternetRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param nat_name: NAT网关名称。
        :type nat_name: str
        :param eip: EIP地址。
        :type eip: str
        """
        
        

        self._enterprise_project_id = None
        self._nat_name = None
        self._eip = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if nat_name is not None:
            self.nat_name = nat_name
        if eip is not None:
            self.eip = eip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInternetRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListInternetRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInternetRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListInternetRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def nat_name(self):
        r"""Gets the nat_name of this ListInternetRequest.

        NAT网关名称。

        :return: The nat_name of this ListInternetRequest.
        :rtype: str
        """
        return self._nat_name

    @nat_name.setter
    def nat_name(self, nat_name):
        r"""Sets the nat_name of this ListInternetRequest.

        NAT网关名称。

        :param nat_name: The nat_name of this ListInternetRequest.
        :type nat_name: str
        """
        self._nat_name = nat_name

    @property
    def eip(self):
        r"""Gets the eip of this ListInternetRequest.

        EIP地址。

        :return: The eip of this ListInternetRequest.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this ListInternetRequest.

        EIP地址。

        :param eip: The eip of this ListInternetRequest.
        :type eip: str
        """
        self._eip = eip

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
        if not isinstance(other, ListInternetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
