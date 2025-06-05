# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'existing_agencies': 'list[AgencyDto]',
        'wanted_agencies': 'list[AgencyDto]',
        'redundant_agencies': 'list[AgencyDto]'
    }

    attribute_map = {
        'existing_agencies': 'existing_agencies',
        'wanted_agencies': 'wanted_agencies',
        'redundant_agencies': 'redundant_agencies'
    }

    def __init__(self, existing_agencies=None, wanted_agencies=None, redundant_agencies=None):
        r"""ShowAgencyResponse

        The model defined in huaweicloud sdk

        :param existing_agencies: 当前存在的委托权限列表。
        :type existing_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        :param wanted_agencies: 仍需要的委托权限列表。
        :type wanted_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        :param redundant_agencies: 冗余的委托权限列表。
        :type redundant_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        
        super(ShowAgencyResponse, self).__init__()

        self._existing_agencies = None
        self._wanted_agencies = None
        self._redundant_agencies = None
        self.discriminator = None

        if existing_agencies is not None:
            self.existing_agencies = existing_agencies
        if wanted_agencies is not None:
            self.wanted_agencies = wanted_agencies
        if redundant_agencies is not None:
            self.redundant_agencies = redundant_agencies

    @property
    def existing_agencies(self):
        r"""Gets the existing_agencies of this ShowAgencyResponse.

        当前存在的委托权限列表。

        :return: The existing_agencies of this ShowAgencyResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        return self._existing_agencies

    @existing_agencies.setter
    def existing_agencies(self, existing_agencies):
        r"""Sets the existing_agencies of this ShowAgencyResponse.

        当前存在的委托权限列表。

        :param existing_agencies: The existing_agencies of this ShowAgencyResponse.
        :type existing_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        self._existing_agencies = existing_agencies

    @property
    def wanted_agencies(self):
        r"""Gets the wanted_agencies of this ShowAgencyResponse.

        仍需要的委托权限列表。

        :return: The wanted_agencies of this ShowAgencyResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        return self._wanted_agencies

    @wanted_agencies.setter
    def wanted_agencies(self, wanted_agencies):
        r"""Sets the wanted_agencies of this ShowAgencyResponse.

        仍需要的委托权限列表。

        :param wanted_agencies: The wanted_agencies of this ShowAgencyResponse.
        :type wanted_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        self._wanted_agencies = wanted_agencies

    @property
    def redundant_agencies(self):
        r"""Gets the redundant_agencies of this ShowAgencyResponse.

        冗余的委托权限列表。

        :return: The redundant_agencies of this ShowAgencyResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        return self._redundant_agencies

    @redundant_agencies.setter
    def redundant_agencies(self, redundant_agencies):
        r"""Sets the redundant_agencies of this ShowAgencyResponse.

        冗余的委托权限列表。

        :param redundant_agencies: The redundant_agencies of this ShowAgencyResponse.
        :type redundant_agencies: list[:class:`huaweicloudsdkeihealth.v1.AgencyDto`]
        """
        self._redundant_agencies = redundant_agencies

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
        if not isinstance(other, ShowAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
