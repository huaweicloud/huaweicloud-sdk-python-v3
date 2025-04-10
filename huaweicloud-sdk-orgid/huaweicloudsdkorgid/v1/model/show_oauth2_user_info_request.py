# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOauth2UserInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_org_id_authorization': 'str'
    }

    attribute_map = {
        'x_org_id_authorization': 'X-OrgID-Authorization'
    }

    def __init__(self, x_org_id_authorization=None):
        r"""ShowOauth2UserInfoRequest

        The model defined in huaweicloud sdk

        :param x_org_id_authorization: 用户访问凭证，即 user_access_token, 示例值：\&quot;Bearer u-7f1bcd13fc57d46bac21793a18e560\&quot;
        :type x_org_id_authorization: str
        """
        
        

        self._x_org_id_authorization = None
        self.discriminator = None

        self.x_org_id_authorization = x_org_id_authorization

    @property
    def x_org_id_authorization(self):
        r"""Gets the x_org_id_authorization of this ShowOauth2UserInfoRequest.

        用户访问凭证，即 user_access_token, 示例值：\"Bearer u-7f1bcd13fc57d46bac21793a18e560\"

        :return: The x_org_id_authorization of this ShowOauth2UserInfoRequest.
        :rtype: str
        """
        return self._x_org_id_authorization

    @x_org_id_authorization.setter
    def x_org_id_authorization(self, x_org_id_authorization):
        r"""Sets the x_org_id_authorization of this ShowOauth2UserInfoRequest.

        用户访问凭证，即 user_access_token, 示例值：\"Bearer u-7f1bcd13fc57d46bac21793a18e560\"

        :param x_org_id_authorization: The x_org_id_authorization of this ShowOauth2UserInfoRequest.
        :type x_org_id_authorization: str
        """
        self._x_org_id_authorization = x_org_id_authorization

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
        if not isinstance(other, ShowOauth2UserInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
