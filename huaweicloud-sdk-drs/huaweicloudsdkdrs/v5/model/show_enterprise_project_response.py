# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnterpriseProjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'enterprise_project_list': 'list[EnterpriseProject]'
    }

    attribute_map = {
        'count': 'count',
        'enterprise_project_list': 'enterprise_project_list'
    }

    def __init__(self, count=None, enterprise_project_list=None):
        """ShowEnterpriseProjectResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param enterprise_project_list: 企业项目列表。
        :type enterprise_project_list: list[:class:`huaweicloudsdkdrs.v5.EnterpriseProject`]
        """
        
        super(ShowEnterpriseProjectResponse, self).__init__()

        self._count = None
        self._enterprise_project_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if enterprise_project_list is not None:
            self.enterprise_project_list = enterprise_project_list

    @property
    def count(self):
        """Gets the count of this ShowEnterpriseProjectResponse.

        总数。

        :return: The count of this ShowEnterpriseProjectResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowEnterpriseProjectResponse.

        总数。

        :param count: The count of this ShowEnterpriseProjectResponse.
        :type count: int
        """
        self._count = count

    @property
    def enterprise_project_list(self):
        """Gets the enterprise_project_list of this ShowEnterpriseProjectResponse.

        企业项目列表。

        :return: The enterprise_project_list of this ShowEnterpriseProjectResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.EnterpriseProject`]
        """
        return self._enterprise_project_list

    @enterprise_project_list.setter
    def enterprise_project_list(self, enterprise_project_list):
        """Sets the enterprise_project_list of this ShowEnterpriseProjectResponse.

        企业项目列表。

        :param enterprise_project_list: The enterprise_project_list of this ShowEnterpriseProjectResponse.
        :type enterprise_project_list: list[:class:`huaweicloudsdkdrs.v5.EnterpriseProject`]
        """
        self._enterprise_project_list = enterprise_project_list

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
        if not isinstance(other, ShowEnterpriseProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
