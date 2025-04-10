# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfOrgResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_id': 'str'
    }

    attribute_map = {
        'org_id': 'orgID'
    }

    def __init__(self, org_id=None):
        r"""ShowConfOrgResponse

        The model defined in huaweicloud sdk

        :param org_id: SP管理员根据会议ID查询该会议归属的企业ID。
        :type org_id: str
        """
        
        super(ShowConfOrgResponse, self).__init__()

        self._org_id = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id

    @property
    def org_id(self):
        r"""Gets the org_id of this ShowConfOrgResponse.

        SP管理员根据会议ID查询该会议归属的企业ID。

        :return: The org_id of this ShowConfOrgResponse.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        r"""Sets the org_id of this ShowConfOrgResponse.

        SP管理员根据会议ID查询该会议归属的企业ID。

        :param org_id: The org_id of this ShowConfOrgResponse.
        :type org_id: str
        """
        self._org_id = org_id

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
        if not isinstance(other, ShowConfOrgResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
