# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopDomainNamesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_domain_names': 'list[dict(str, object)]'
    }

    attribute_map = {
        'top_domain_names': 'top_domain_names'
    }

    def __init__(self, top_domain_names=None):
        r"""ShowTopDomainNamesResponse

        The model defined in huaweicloud sdk

        :param top_domain_names: top域名信息
        :type top_domain_names: list[dict(str, object)]
        """
        
        super(ShowTopDomainNamesResponse, self).__init__()

        self._top_domain_names = None
        self.discriminator = None

        if top_domain_names is not None:
            self.top_domain_names = top_domain_names

    @property
    def top_domain_names(self):
        r"""Gets the top_domain_names of this ShowTopDomainNamesResponse.

        top域名信息

        :return: The top_domain_names of this ShowTopDomainNamesResponse.
        :rtype: list[dict(str, object)]
        """
        return self._top_domain_names

    @top_domain_names.setter
    def top_domain_names(self, top_domain_names):
        r"""Sets the top_domain_names of this ShowTopDomainNamesResponse.

        top域名信息

        :param top_domain_names: The top_domain_names of this ShowTopDomainNamesResponse.
        :type top_domain_names: list[dict(str, object)]
        """
        self._top_domain_names = top_domain_names

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
        if not isinstance(other, ShowTopDomainNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
