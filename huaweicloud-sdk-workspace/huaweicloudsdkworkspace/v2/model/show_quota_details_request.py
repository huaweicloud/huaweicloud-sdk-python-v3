# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'az_code': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'az_code': 'az_code'
    }

    def __init__(self, site_id=None, az_code=None):
        r"""ShowQuotaDetailsRequest

        The model defined in huaweicloud sdk

        :param site_id: 站点ID。
        :type site_id: str
        :param az_code: 可用分区code。
        :type az_code: str
        """
        
        

        self._site_id = None
        self._az_code = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if az_code is not None:
            self.az_code = az_code

    @property
    def site_id(self):
        r"""Gets the site_id of this ShowQuotaDetailsRequest.

        站点ID。

        :return: The site_id of this ShowQuotaDetailsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this ShowQuotaDetailsRequest.

        站点ID。

        :param site_id: The site_id of this ShowQuotaDetailsRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def az_code(self):
        r"""Gets the az_code of this ShowQuotaDetailsRequest.

        可用分区code。

        :return: The az_code of this ShowQuotaDetailsRequest.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ShowQuotaDetailsRequest.

        可用分区code。

        :param az_code: The az_code of this ShowQuotaDetailsRequest.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, ShowQuotaDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
